from rest_framework import serializers
from core.models import Tag
from todo.models import Todo

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id','name')
        read_only_fields = ('id',)


class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id','author','title','body','created_at','updated_at')
        read_only_fields = ('id',)
