from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from django.apps import AppConfig

class BotConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bot'

    # def ready(self):
    #     scheduler = BackgroundScheduler(timezone="Asia/Dushanbe")
    #     scheduler.add_job(
    #         Notification, 
    #         trigger=CronTrigger(hour=7, minute=0),
    #         id="notify_students",
    #         replace_existing=True,
    #     )
    #     scheduler.start()
