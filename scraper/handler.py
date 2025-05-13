from datetime import datetime, timedelta
import os, json
import pandas as pd
import firebase_admin
from firebase_admin import credentials, firestore
from logger import logger

def convert_date(input_date: str):
    today = datetime.today()
    if "天" in input_date:
        days_ahead = int(input_date.replace("天", ""))
        target_date = today - timedelta(days=days_ahead)
    
    elif "月" in input_date:
        try:
            if "下午" in input_date or "上午" in input_date:
                date_part = input_date.split("下")[0]
                month, day = map(int, date_part.replace("日", "").split("月"))
            else:
                month, day = map(int, input_date.replace("日", "").split("月"))

            target_date = datetime(today.year, month, day)
        except Exception as e:
            return f"Invalid format: {e}"
    
    else:
        return "Invalid date format"
    
    return target_date.strftime("%Y年%m月%d日")

def invalid_date(input_date: str, limit: int = 7):
    today = datetime.today()
    date = datetime.strptime(input_date, "%Y年%m月%d日")
    if abs((today - date).days) > int(limit):
        return True
    
    return False

def packing(datas):
    select_df = pd.DataFrame(datas, columns = ['date', 'content', 'picture'])
    data = json.loads(select_df.to_json(orient = 'records'))

    if os.path.exists('news.json'):
        os.remove('news.json')
    
    with open('news.json', 'w', encoding='UTF-8') as f:
        json.dump(data, f, ensure_ascii=False)

def use_firebase(data):
    count = len(data)
    try:
        credentials_path = os.path.join(os.path.dirname(__file__), "serviceAccountKey.json")
        cred = credentials.Certificate(credentials_path)
        firebase_admin.initialize_app(cred)
        db = firestore.client()
        db.collection('blocks').document('news').set({"title": "近期公告", "data": data, "count": count})
        logger.info("Data successfully sent to Firebase")
    except Exception as e:
        logger.error("Error using Firebase: %s", str(e))
        return False