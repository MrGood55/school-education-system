from django import forms
from .models import School,Person







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
    # middle_name = forms.CharField(label='Middle Name', max_length=50)
    # last_name = forms.CharField(label='Last Name', max_length=50)
    # email = forms.EmailField(label='email', max_length=80)
    nationality = forms.CharField(label='Nationality', max_length=50)
    address_for_admin = forms.CharField(label='Address for admin', max_length=255)

    # school
    # status ('administrator', 'Administrator')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['placeholder'] = visible.field.label
            visible.field.widget.attrs['class'] = 'text_field_input'

