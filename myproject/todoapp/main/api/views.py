
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from main.models import Task
from .serializers import TaskSerializer

@api_view(['GET'])
def getRoutes(request):
    routes=[
    "get api",
    "get/api/tasks"
    ]
    return Response(routes)


@api_view(['GET'])
def gettasks(request):
    if request.method=='GET':
        tasks=Task.objects.all()
        serializers=TaskSerializer(tasks, many=True)
        return Response(serializers.data)


@api_view(['GET'])
def gettask(request,pk):
    if request.method=='GET':
        task=Task.objects.get(id=pk)
        serializers=TaskSerializer(task)
        return Response(serializers.data)



@api_view(['Delete'])
def deletetask(request,pk):
    if request.method=='Delete':
        print(pk)
        task=Task.objects.get(id=pk)
        print(task)
        serializers=TaskSerializer(task)
        task.delete()
        serializers=TaskSerializer(task)
        return Response(serializers.data)