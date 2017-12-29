from django.shortcuts import render
import datetime

# Create your views here.
def index(request):
    today = datetime.date.today()
    return render(request, 'base.html', {'today': today})
