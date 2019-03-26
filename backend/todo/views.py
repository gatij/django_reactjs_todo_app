from django.shortcuts import render
from rest_framework import viewsets          # add this
from .serializers import TodoSerializer      # add this
from .models import Todo 
# Create your views here.

#The 'viewsets' base class provides the implementation for CRUD operations by default,
# what we had to do was specify the 'serializer class' and the 'query set'.
class TodoView(viewsets.ModelViewSet):
	serializer_class = TodoSerializer
	queryset = Todo.objects.all()         # add this
	          
     # add this
	               # add this
