from django.shortcuts import render
from .models import Student
from .serializer import Studentserializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.
class StudentAPI(APIView):
   def get(self,request,pk= None,format=None):
       id = pk
       if id  is not None:
           stu = Student.objects.get(id=id)
           serializer = Studentserializer(stu)
           return Response(serializer.data)
       stu = Student.objects.all()
       serializer = Studentserializer(stu,many=True)
       return Response(serializer.data)
    
   def post(self,request,pk=None,format = None):
       serializer = Studentserializer(data = request.data)
       if serializer.is_valid():
          serializer.save()
          return Response({'msg':'Data Saved'})
       return Response(serializer.errors)   
        
   def put(self,request,pk,format = None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = Studentserializer(stu,data = request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated'})
        return Response(serializer.errors)
    
   def patch(self,request,pk,format = None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = Studentserializer(stu,data = request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated'})
        return Response(serializer.errors)
    
   def delete(self,request,pk,formt=None):
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'Record':'Deleted'})