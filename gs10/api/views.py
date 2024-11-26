from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Student
from .serializer import Studentserializer
from rest_framework.response import Response

# Create your views here.
@api_view(['GET','POST','PUT','DELETE'])
def student_api(request):
    if request.method == "GET":
     id = request.data.get('id')
     if id  is not None:
         stu = Student.objects.get(id=id)
         serializer = Studentserializer(stu)
         return Response(serializer.data)
     stu = Student.objects.all()
     serializer = Studentserializer(stu,many=True)
     return Response(serializer.data)
    if request.method == 'POST'  :
        serializer = Studentserializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Saved'})
        return Response(serializer.errors)   
        
    if request.method == 'PUT' :
        id = request.data.get('id')
        stu = Student.objects.get(pk=id)
        serializer = Studentserializer(stu,data = request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated'})
        return Response(serializer.errors)
    
    if request.method == ('DELETE'):
        id = request.data.get('id')
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'Record':'Deleted'})