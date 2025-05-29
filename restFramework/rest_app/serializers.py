from rest_framework import serializers
from .models import person,student,teacher

class personSerilizers(serializers.ModelSerializer):
    class Meta:
        model=person
        fields='__all__'



class studentSerilizer(serializers.ModelSerializer):
    class Meta:
        model=student
        fields='__all__'

class teacherSerilizer(serializers.ModelSerializer):
    class Meta:
        model=teacher
        fields='__all__'