from rest_framework import serializers
from .models import Student

class Studentserializer(serializers.ModelSerializer):
    # name = serializers.CharField(read_only=True)  // for  one field validation
    class Meta:
        model = Student
        fields = ['id','name','roll','city']
        # read_only_fields = ['name','roll']  # validation for multipal field 
        extra_kwargs = {'name': {'read_only':True}}  # this also one method for validation






    
    
    