from django.shortcuts import render
import requests
import json
import mysql.connector
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from django.shortcuts import get_object_or_404
#from .models import Prclient, PrclientAPIKey
#from .serializers import ClientSerializer
from dj_api import settings
import xml.etree.ElementTree as ET
#from .permissions import HasPrclientAPIKey

host = settings.host
user = settings.user
password = settings.password
database = settings.database

#connect to existing database
connection = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database,
    autocommit=True
)

#cursor for execution of sql query
cur = connection.cursor(dictionary=True)

# Create your views here.
@api_view(['GET'])
def checkall(request):
    pass


@api_view(['GET'])
def check(request):
    unique_id = request.GET.get('unique_id', False);

    if unique_id:
        query = """SELECT * FROM astpp_currency_table WHERE id = %s"""
        params = (unique_id,)
        cur.execute(query, params)
        result = cur.fetchall()

        if result == []:
            return Response({"status": "error", "message": "data not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            #email = result[0]['CLemail']
            #return Response({"email": email, "message": "data found"})
            return HttpResponse(json.dumps(result, indent=4, sort_keys=True, default=str), content_type="application/json")

    else:
        return Response({"status": "error", "message": "data incomplete"}, status=status.HTTP_404_NOT_FOUND)
