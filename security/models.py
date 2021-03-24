from random import choice

from twilio.rest import Client

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ActivityLog(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    action = models.CharField(max_length=300)

class TwoFactorAuthentification(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    code = models.CharField(max_length=6)
    sent_on = models.DateTimeField(auto_now_add=True)

    @classmethod
    def send_code(cls, user, to_phone):
        account_sid = "AC5a082b2b57a8b32da3373225b7a80677"
        auth_token = "7abe16cc9db1fe30b760369bb845ae14"
        client = Client(account_sid, auth_token)
        digits = "0123456789"
        code = ''.join([choice(digits) for i in range(6)])
        cls.objects.create(
            user=user,
            code=code,
        )
        message = client.messages.create(
            to=to_phone,
            from="+12813695268",
            body="Your auth code:" + code
        )
