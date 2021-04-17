from django.urls import path
from .views import TagViewSet, TodoDetail, TodoList # new


urlpatterns = [
        path('', TodoList.as_view()), # new
        path('<int:pk>/', TodoDetail.as_view()),
    ]








# from django.urls import path,include
# from rest_framework.routers import DefaultRouter
#
# from todo import views
#
# router = DefaultRouter()
# router.register('tags',views.TagViewSet)
#
#
# app_name = 'todo'
#
# urlpatterns = [
#     path('',include(router.urls))
# ]
