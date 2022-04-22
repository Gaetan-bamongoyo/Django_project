from rest_framework import serializers
from employee.models import Poste,Employee

class EmployeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
    
class PosteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poste
        fields = '__all__'
        