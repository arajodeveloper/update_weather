import requests,json
from django.shortcuts import render
from .models import Temp
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core import serializers
import json
import sys

# Create your views here.
@api_view(['GET'])
def index(request):
    cities = request.GET['cities']
    begindate, enddate = request.GET['dateRange'].split('-')
    begin = begindate[0:4] + '-' + begindate[4:6] + '-' + begindate[6:8]
    end = enddate[0:4] + '-' + enddate[4:6] + '-' + enddate[6:8]
    print(cities, file=sys.stderr)
    print(begindate, file=sys.stderr)
    print(enddate, file=sys.stderr)
    results = Temp.objects.filter(city=cities, date__gte=begin, date__lte=end)
    return Response(json.loads(serializers.serialize("json", results)))
   