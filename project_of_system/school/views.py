from django.shortcuts import render, redirect
from .forms import SchoolForm,AdminForSchoolForm
from .models import School, Person
# Create your views here.



def create_school(request):
    if request.method == 'POST':
        school_form = SchoolForm(request.POST)
        admin_for_school_form = AdminForSchoolForm(request.POST)
        if school_form.is_valid() and admin_for_school_form.is_valid():
            # Process the form data
            # You can access form.cleaned_data to get the cleaned data
            name = school_form.cleaned_data['name']
            country = school_form.cleaned_data['country']
            region = school_form.cleaned_data['region']
            city = school_form.cleaned_data['city']
            address = school_form.cleaned_data['address']
            # Perform actions with the form data, e.g., create a School instance
            school = School(name=name, country=country, region=region, city=city, address=address)
            school.save()

            first_name = admin_for_school_form.cleaned_data['first_name']
            nationality = admin_for_school_form.cleaned_data['nationality']
            address_for_admin = admin_for_school_form.cleaned_data['address_for_admin']
            print(name,country,region,city,address)
            print(first_name,nationality,address_for_admin)


            

            # Redirect to a success page or another view
            # return redirect('success_page')  # Replace 'success_page' with the actual URL name or path

    else:
        school_form = SchoolForm()
        admin_for_school_form = AdminForSchoolForm()
    return render(request, 'school/create_school.html', {'school_form': school_form,'admin_for_school_form': admin_for_school_form})