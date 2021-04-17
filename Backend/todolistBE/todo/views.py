from rest_framework import viewsets,mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Tag
from todo import serializers
from rest_framework import generics
from todo.models import Todo


# Create your views here.

class TagViewSet(viewsets.GenericViewSet,mixins.ListModelMixin):
    """manage tags in the database """

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Tag.objects.all()
    serializer_class = serializers.TagSerializer

    def get_queryset(self):
        """return objects for the current auth user only """
        return self.queryset.filter(author=self.request.user).order_by('-name')


class TodoList(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.ToDoSerializer
    def get_queryset(self):
        """return objects for the current auth user only """
        return self.queryset.filter(author=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.ToDoSerializer
