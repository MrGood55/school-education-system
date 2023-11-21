from django.shortcuts import render, redirect
from .forms import SchoolForm,AdminForSchoolForm
from .models import School, Person
# Create your views here.



def create_school(request):
    if request.method == 'POST':
        school_form = SchoolForm(request.POST)
        admin_for_school_form = AdminForSchoolForm(request.POST)
        if school_form.is_valid() and admin_for_school_form.is_valid():
            # fetch data
            name = school_form.cleaned_data['name']
            country = school_form.cleaned_data['country']
            region = school_form.cleaned_data['region']
            city = school_form.cleaned_data['city']
            address = school_form.cleaned_data['address']
            # Perform actions with the form data, e.g., create a School instance
            # if object exists just get, else create
            if School.objects.exists():
                if not School.objects.filter(name=name, country=country, region=region, city=city, address=address).exists():
                    school = School(name=name, country=country, region=region, city=city, address=address)
                    school.save()
                else:
                    school = School.objects.get(name=name, country=country, region=region, city=city, address=address)
            else:
                school = School(name=name, country=country, region=region, city=city, address=address)
                school.save()

                

            # fetch data
            first_name = admin_for_school_form.cleaned_data['first_name']
            middle_name = admin_for_school_form.cleaned_data['middle_name']
            last_name = admin_for_school_form.cleaned_data['last_name']
            email = admin_for_school_form.cleaned_data['email']
            nationality = admin_for_school_form.cleaned_data['nationality']
            address_for_admin = admin_for_school_form.cleaned_data['address_for_admin']
            # Perform actions with the form data, e.g., create a School instance
            if Person.objects.exists():
                if not Person.objects.filter(first_name=first_name,middle_name=middle_name,last_name=last_name,email=email,nationality=nationality,address=address_for_admin,school=school.pk).exists():
                    admin = Person(first_name=first_name,middle_name=middle_name,last_name=last_name,email=email,nationality=nationality,address=address_for_admin,school=school.pk)
                    admin.save()
                else:
                    admin = Person.objects.get(first_name=first_name,middle_name=middle_name,last_name=last_name,email=email,nationality=nationality,address=address_for_admin,school=school.pk)
            else:
                admin = Person(first_name=first_name,middle_name=middle_name,last_name=last_name,email=email,nationality=nationality,address=address_for_admin,school=school.pk) #,status='administrator'
                admin.save()

            print(name,country,region,city,address)
            print(f'school id is {school.pk} type is {type(school.pk)}')
            print(first_name,nationality,address_for_admin)


            

            # Redirect to a success page or another view
            # return redirect('success_page')  # Replace 'success_page' with the actual URL name or path

    else:
        school_form = SchoolForm()
        admin_for_school_form = AdminForSchoolForm()
    return render(request, 'school/create_school.html', {'school_form': school_form,'admin_for_school_form': admin_for_school_form})