from django.urls import path
from geminiTest.views import index

urlpatterns = [
    path('', index, name='index'),
]
