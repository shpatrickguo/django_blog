from django.shortcuts import render
from djagno.http import HttpResponse

# Create your views here.
def upload_file_view(request):
    return HttpResponse('drop a file here')
