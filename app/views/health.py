from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def health_live(request):
    return Response({"status": "live"})

@api_view(['GET'])
def health_ready(request):
    return Response({"status": "ready"})



##health
from django.http import JsonResponse
from pymongo import MongoClient
import redis


def health_check(request):
    health = {}

    #redis check
    try:
        redis_client = redis.Redis(host='localhost', port=6379, db=0)
        redis_client.ping()
        health['redis'] = 'OK'
    except Exception as e:
        health['redis'] = f'Error: {str(e)}'

    #mongoDB check
    try:
        mongo_client = MongoClient('mongodb://localhost:27017/')
        mongo_client.admin.command('ping')
        health['mongodb'] = 'OK'
    except Exception as e:
        health['mongodb'] = f'Error: {str(e)}'

    return JsonResponse(health)