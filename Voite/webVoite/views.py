from django.shortcuts import render
from .forms import form_voite
from .models import *
from django.http import HttpResponse
import json
from django.http import JsonResponse

# Create your views here.
def home(request):
    data = {}
    form = form_voite()
    data['form'] = form
    return render(request, 'webVoite/index.html', data)




def succeess(request):
    data = {}

    # GET IP
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    data['IP'] = ip


    if request.method == 'POST':
        # Form was submitted
        form = form_voite(request.POST)
        print(request.POST)
        if form.is_valid():
            # Form fields passed validation
            Golos = form.cleaned_data
            AcceptVoice = Person.objects.create(Name=Golos['Name'])
            AcceptVoice.IP = ip
            AcceptVoice.floor = request.POST['floor']

            AcceptVoice.save()

        else:
            print("Error")
    if request.POST['floor'] == 'B':
        select_floor = 'Мальчика'
    else:
        select_floor = 'Девочку'
    data['Name']= Golos['Name']
    data['floor'] = select_floor
    print(form.errors)
    return render(request, 'webVoite/success.html', data)

def result(request):
    data = {}
    data['boy'] = Person.objects.filter(floor='B')
    data['girl'] = Person.objects.filter(floor='G')

    return render(request, 'webVoite/results.html', data)

def chart(request):
    data = {}
    data['boy'] = Person.objects.filter(floor='B')
    data['girl'] = Person.objects.filter(floor='G')
    return render(request, 'webVoite/chart.html', data)

def count(request):
    data = {}
    data = {
        "Boy": Person.objects.filter(floor='B').count(),
        "Girl": Person.objects.filter(floor='G').count(),
    }
    return JsonResponse(data)


def delete(request,id):
    data = {}
    try:
        record = Person.objects.get(id=id)
        record.delete()
        data = {
            "id": id,
            "success": "Ok",
        }
    except:
        data = {
            "id": id,
            "success": "False",
        }


    return JsonResponse(data)
