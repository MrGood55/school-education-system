


from django.urls import path
from .views import create_school,index



app_name = 'school'
urlpatterns = [
    path('', index, name='index'),
    path('create_school/', create_school, name='create_school'),
    # Add other URL patterns as needed
]
