import csv
import os
import json
import pandas as pd
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from .forms import CsvForm
from .models import CsvFileUpload
from sales.models import Sale


class CsvFormView(TemplateView):
    template_name = 'get_csv.html'

    def get(self, request):
        form = CsvForm()
        files = CsvFileUpload.objects.all()

        args = {'form': form, 'file': files}

        return render(request, self.template_name, args)
    
    def post(self, request):
        if request.method == 'POST':
            form = CsvForm(request.POST, request.FILES)
            if form.is_valid():
                csv_file = request.FILES['csvfile']
                data = pd.read_csv(csv_file)
                df = pd.DataFrame(data)
                df.to_csv('csv_data.csv', index=False)

                if not csv_file.name.endswith('.csv'):
                    messages.error(request, 'File is not CSV type')
                    return redirect('csvs:uploadcsv')
                
                if csv_file.multiple_chunks():
                    messages.error(request, 'Uploaded file is too big (%.2f MB)' % (csv_file.size(1000*1000),))
                    return redirect('csvs:uploadcsv')

            return redirect('csvs:csvdata')
        return render(request, self.template_name)

def csv_view(request):
    data = pd.read_csv('csv_data.csv', header=0)
    df = pd.DataFrame(data)
    pd.set_option('colheader_justify', 'center')
    data_html = df.to_html()
    context = {'csv_data': data_html}

    return render(request, 'csvdata.html', context)

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


