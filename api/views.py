from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from drf_yasg.utils import swagger_auto_schema
from .tasks import *
from celery.result import AsyncResult
from .serializers import *

class GenerateTask(APIView):

    @swagger_auto_schema(operation_description="Start a long running task via API endpoint")
    def post(self, request):
        task_id = add.delay(2,3)  
        print(task_id)
        return Response({'task_id':str(task_id)},status=status.HTTP_201_CREATED)

class TaskStatus(APIView):

    @swagger_auto_schema(query_serializer=taskSerializer, operation_description="Check status of long running task via API endpoint")
    def get(self, request):
        serializer = taskSerializer(data=request.GET)
        serializer.is_valid(raise_exception=True)
        task_id = serializer.validated_data['task_id']
        res = AsyncResult(task_id)
        task_status = res.ready()
        return Response({'task_status':task_status},status=status.HTTP_200_OK)

class TaskResult(APIView):

    @swagger_auto_schema(query_serializer=taskSerializer, operation_description="Get results of long running task via API endpoint")
    def get(self, request):
        serializer = taskSerializer(data=request.GET)
        serializer.is_valid(raise_exception=True)
        task_id = serializer.validated_data['task_id']
        result = add.AsyncResult(task_id)
        taskStatus = result.status
        traceback = result.traceback
        result = result.result
        if isinstance(result, Exception):
            return Response({
                'status': taskStatus,
                'error': str(result),
                'traceback': traceback,
                })
        else:
            return Response({'status':taskStatus,'result': result},status=status.HTTP_200_OK)
