from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
import logging

def start():
    logger.warning("WE CAN START SCHEDULER HERE")
    #scheduler = BackgroundScheduler()
    #scheduler.add_job(my_logger, 'interval', seconds=3)
    #scheduler.start()

def my_logger():
    logger = logging.getLogger(__name__)
    logger.warning("UPDATING")