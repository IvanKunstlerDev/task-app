from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import TaskSerializer
from .models import Task

class ListTask(APIView):
    def get(self, request):
        if not Task.objects.all().exists():
            return Response('Tasks not found', status.HTTP_404_NOT_FOUND)

        query = Task.objects.all()
        serializer = TaskSerializer(query, many=True)

        return Response(serializer.data, status.HTTP_200_OK)
        

class CreateTask(APIView):
    def post(self, request):
        query = Task.objects.create(
            body = request.data.get('body')
        )
        serializer = TaskSerializer(query)

        return Response(serializer.data, status.HTTP_201_CREATED)

    
class UpdateTask(APIView):
    def put(self, request, id):
        if not Task.objects.get(id=id):
            return Response(f'Task {id} not found', status.HTTP_404_NOT_FOUND)
        
        task = Task.objects.get(id=id)
        task.body = request.data.get('body')
        task.is_completed = request.data.get('is_completed')
        task.save()

        serializer = TaskSerializer(task)

        return Response(serializer.data, status.HTTP_201_CREATED)
    

class DeleteTask(APIView):
    def delete(self, request, id):
        if not Task.objects.get(id=id):
            return Response(f'Task {id} not found', status.HTTP_404_NOT_FOUND)
        
        query = Task.objects.get(id=id)
        serializer = TaskSerializer(query)
        query.delete()

        return Response(serializer.data, status.HTTP_200_OK)