from django import forms
from .models import School,Person
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
# Create your forms here.




class SchoolForm(forms.Form):
    name = forms.CharField(label='Title', max_length=100)
    country = forms.CharField(label='Country', max_length=50)
    region = forms.CharField(label='Region', max_length=50)
    city = forms.CharField(label='City', max_length=50)
    address = forms.CharField(label='Address', max_length=255)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['placeholder'] = visible.field.label
            visible.field.widget.attrs['class'] = 'text_field_input'

class AdminForSchoolForm(forms.Form):
    
    
    first_name = forms.CharField(label='First Name', max_length=50)
    middle_name = forms.CharField(label='Middle Name', max_length=50)
    last_name = forms.CharField(label='Last Name', max_length=50)
    address_for_admin = forms.CharField(label="Admin's address", max_length=255)

    username = forms.CharField(label='Username', max_length=50)
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password',max_length=40, widget=forms.PasswordInput())

    # school
    # status ('administrator', 'Administrator')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['placeholder'] = visible.field.label
            visible.field.widget.attrs['class'] = 'text_field_input'

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'text_field_input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'text_field_input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'text_field_input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'text_field_input'}))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['placeholder'] = visible.field.label
            # visible.field.widget.attrs['class'] = 'text_field_input'

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'text_field_input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'text_field_input'}))
