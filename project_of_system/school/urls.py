


from django.urls import path
from .views import create_school



app_name = 'school'
urlpatterns = [
    path('create_school/', create_school, name='create_school'),
    # Add other URL patterns as needed
]
