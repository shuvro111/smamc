from django.shortcuts import render
from .utils import *

# Create your views here.


def index(request):
    english_date = get_dates().get('english_date')
    bangla_date = get_dates().get('bangla_date')

    return render(request, 'home/index.html', {'english_date': english_date, 'bangla_date': bangla_date})

def teachers(request):
    return render(request, 'home/table.html')