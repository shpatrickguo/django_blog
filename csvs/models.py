from django.db import models
from datetime import datetime, date

# Create your models here.
class CsvFileUpload(models.Model):
    file_name = models.FileField(upload_to='csvs')
    uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"File id: {self.id}"
