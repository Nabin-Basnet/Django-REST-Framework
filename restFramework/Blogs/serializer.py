from .models import Blog,Comment
from rest_framework import serializers

class commentsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields='__all__'


class blogSerializer(serializers.ModelSerializer):
    comments=commentsSerializer(many=True,read_only=True)
    class Meta:
        model=Blog
        fields='__all__'