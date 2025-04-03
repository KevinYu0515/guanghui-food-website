from datetime import datetime, timedelta
import os, json
import pandas as pd

def convert_date(input_date: str):
    today = datetime.today()
    
    if "天" in input_date:
        days_ahead = int(input_date.replace("天", ""))
        target_date = today - timedelta(days=days_ahead)
    
    elif "月" in input_date:
        month_day = input_date.replace("日", "").split("月")
        month = int(month_day[0])
        day = int(month_day[1])
        target_date = datetime(today.year, month, day)
    
    else:
        return "Invalid date format"
    
    return target_date.strftime("%Y年%m月%d日")

def packing(datas):
    select_df = pd.DataFrame(datas, columns = ['date', 'content', 'picture'])
    data = json.loads(select_df.to_json(orient = 'records'))

    if os.path.exists('news.json'):
        os.remove('news.json')
    
    with open('news.json', 'w', encoding='UTF-8') as f:
        json.dump(data, f, ensure_ascii=False)