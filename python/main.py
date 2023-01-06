from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.background import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
import os

intervalTrigger = CronTrigger(year="*",month="*",day="*",hour=23, minute=48)

def APschedulerMonitor(Task):               
  scheduler = BackgroundScheduler()
  scheduler.add_job(Task, intervalTrigger, id='test_job1')
  scheduler.start()

# cmd_news = "python python/catch_news.py"
# cmd_comments = "python python/catch_comment.py"
# Task = os.system(cmd_comments)
# Task = os.system(cmd_news)
def testPrint():
  i+=1
  print("Hello_%d", i)

if __name__ == '__main__':
  i = 0
  APschedulerMonitor(testPrint)
  print("Hi")
