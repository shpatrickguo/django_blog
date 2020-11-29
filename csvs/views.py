import csv
import os
import json
import pandas as pd
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from .forms import CsvForm
from .models import CsvFileUpload
from sales.models import Sale


# def upload_file_view(request):
#     form = CsvModelForm(request.POST or None, request.FILES or None)
#     if form.is_valid():
#         form.save()
#         form = CsvModelForm()
#         obj = Csv.objects.get(activated=False)
#         with open(obj.file_name.path, 'r') as f:
#             reader = csv. reader(f)

#             for i, row in enumerate(reader):
#                 if i == 0:
#                     pass
#                 else:
#                     row = "".join(row)
#                     row = row.replace*(";", "")
#                     row = row.split()
#                     product = row[1].upper()
#                     user = User.objects.get(username=row[3])
#                     Sale.objects.create(
#                         product = product,
#                         quantity = int(row[2]),
#                         salesman = user,
#                     )
#             obj.activated = True
#             obj.save()
#     return render(request, 'csvs/upload.html', {'form': form})


class CsvFormView(TemplateView):
    template_name = 'upload.html'

    def get(self, request):
        form = CsvModelForm()
        files = CsvFileUpload.objects.all()

        args = {'form': form, 'file': files}

        return render(request, self.template_name, args)
    
    def post(self, request):
        if request.method == 'POST':
            form = CsvForm(request.POST, request.FILES)
            if form.is_valid():
                csv_file = request.FILES['csvfile']