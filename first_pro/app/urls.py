from django.urls import path
from app.views import index, hello, age, page

urlpatterns = [
    path('', index, name='index'),
    path('page', page, name='page'),
    path('<str:name>', hello, name='hello'),
    path('<str:name>/<int:age>', age, name='age'),

]