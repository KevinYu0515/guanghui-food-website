from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
import os
from logger import logger

# intervalTrigger = CronTrigger(hour=17, minute=5, second=0, timezone='Asia/Taipei')
intervalTrigger = CronTrigger(minute="*/1", second=0, timezone='Asia/Taipei')

def APschedulerMonitor(Task):               
    scheduler = BackgroundScheduler()
    scheduler.add_job(Task, intervalTrigger, id='catch_news_job')
    scheduler.start()
    for job in scheduler.get_jobs():
        logger.info(f"Job ID: {job.id}, Next Run Time: {job.next_run_time}, Trigger: {job.trigger}")
    logger.info("Scheduler is running...") 

def run_catch_news():
    os.system("python catch_news.py")

if __name__ == '__main__':
  APschedulerMonitor(run_catch_news)
  
