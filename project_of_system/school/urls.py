


from django.urls import path
from .views import *



app_name = 'school'
urlpatterns = [
    path('', index, name='index'),
    path('create_school/', create_school, name='create_school'),

    path('login/', LoginUser.as_view(), name='login'),
    path('signup/', RegisterUser.as_view(), name='signup'),
    path('done/', done, name='done'),
    # Add other URL patterns as needed
]
