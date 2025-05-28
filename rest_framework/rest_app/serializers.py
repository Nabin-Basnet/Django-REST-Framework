from rest_framework import serializers
from .models import person

class personSerilizers(serializers.ModelSerializer):
    class Meta:
        model=person
        field='__all__'