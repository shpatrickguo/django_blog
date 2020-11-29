from django.urls import path
from .views import csv_view, CsvFormView

app_name = 'csvs'

urlpatterns = [
    #path('', upload_file_view, name='upload-vew'),
    #path('data/', data_view, name="data"),
    path('', CsvFormView.as_view(), name="uploadcsv"),
    path("csvdata/", csv_view, name="csvdata"),
    path("uploadcsv/", CsvFormView.as_view(), name="uploadcsv"),
    
]
