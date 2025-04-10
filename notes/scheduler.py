from apscheduler.schedulers.background import BackgroundScheduler

from .tasks import check_reminders

scheduler = BackgroundScheduler()


# Функция для запуска планировщика, который будет отслеживать/обновлять напоминания заметок
def start_scheduler():
    if not scheduler.running:
        print('[scheduler] Планировщик запускается...')
        try:
            scheduler.add_job(check_reminders, 'interval', seconds=30)
            scheduler.start()
            print('[scheduler] Планировщик запущен')
        except Exception as e:
            print(f"[scheduler] Ошибка при запуске: {e}")
