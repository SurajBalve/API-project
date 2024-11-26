from rest_framework import serializers
from .models import Student
class Studentserializer(serializers.ModelSerializer):
    def start_with_r(Value):
        if Value[0].lower() != 's':
            raise serializers.ValidationError('city must be Ranchi')
        
    name = serializers.CharField(validators = [start_with_r])
    class Meta:
        model = Student
        fields = ['name','roll','city']
   
    def validate_roll(self,value): #Field level validator
        if value >=10:
         raise serializers.ValidationError('seat full')
        return value
     
    def validate(self, data):   #object level validator
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'Omkar' and ct.lower() != 'Pathardi':
         raise serializers.ValidationError('city must be Ranchi')
        return data
    
    