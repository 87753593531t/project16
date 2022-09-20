from celery import shared_task


from project16.celery import celery_app

@celery_app.task(
    name ='send_sms',
    bind=True,
    default_retry_delay=5,
    max_retries=1,
    asks_late=True
)
def send_sms(self, phone, otp):
    phone_num = str(phone)
    url = '' + phone_num + '&text=' + otp + ''
    print('===== SENT SMS ====', phone, otp, '=====')