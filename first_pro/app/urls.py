from django.urls import path
from app.views import index, items, create

urlpatterns = [
    path('', index, name='index'),
    path('items/<int:id>/', items, name='items'),
    path('create/', create, name='create')


]