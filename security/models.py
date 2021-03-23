from django.db import models

# Create your models here.
class ActivityLog(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    action = models.CharField(max_length=300)


