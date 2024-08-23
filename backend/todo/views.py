# from django.shortcuts import render
# from rest_framework import viewsets
# from .serializers import TodoSerializer
# from .models import Todo
# # Create your views here.

# class TodoView(viewsets.ModelViewSet):
#     serializer_class = TodoSerializer
#     queryset = Todo.objects.all()
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TodoSerializer
from .models import Todo

# View to handle data submission
@api_view(['POST'])
def create_todo(request):
    if request.method == 'POST':
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# View to handle data retrieval
@api_view(['GET'])
def list_todos(request):
    if request.method == 'GET':
        print("hihihi")
        todos = Todo.objects.all()  
        serializer = TodoSerializer(todos, many=True)
        print(serializer.data)
        return Response(serializer.data)

