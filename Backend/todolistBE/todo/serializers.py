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
        fields = ('id','title','body','author','created_at','updated_at')
        read_only_fields = ('id','author')

    # def create(self):
    #         vv =  self.context['request'].user
    #         title = self.validated_data['title']
    #         body = self.validated_data['body']
