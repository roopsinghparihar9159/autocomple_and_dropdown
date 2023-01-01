from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import Country
# Create your views here.
def home(request):
    return render(request,'mainapp/index.html')

def jsonlink(request):
    query = list(Country.objects.values())
    # title = json.dumps(query.__dict__)
    # print(query)
    return JsonResponse(query,safe=False)