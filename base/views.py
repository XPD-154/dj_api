from django.shortcuts import render
import requests
import json
import mysql.connector
from mysql.connector import Error
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

'''
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

'''

# Create your views here.

#function to connect to existing database
def connect():
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database,
        autocommit=True
    )
    cur = connection.cursor(dictionary=True)
    return cur

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/rooms',
        'GET /api/rooms/ :id'
    ]
    return Response(routes)


@api_view(['GET'])
def checkall(request):

    try:
        connect()
        query = """SELECT * FROM astpp_currency_table"""
        cur.execute(query)
        result = cur.fetchall()

        if result == []:
            return Response({"status": "error", "message": "data not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            #email = result[0]['CLemail']
            #return Response({"email": email, "message": "data found"})
            return HttpResponse(json.dumps(result, indent=4, sort_keys=True, default=str), content_type="application/json")

    except Error as e:
        error_result = str(e)
        return Response({"status": "error", "message": error_result}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def check(request):

    try:
        connect()
        unique_id = request.GET.get('unique_id', False)

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

    except Error as e:
        error_result = str(e)
        return Response({"status": "error", "message": error_result}, status=status.HTTP_404_NOT_FOUND)




