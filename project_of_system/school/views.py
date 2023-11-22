from django.shortcuts import render, redirect
from .forms import SchoolForm,AdminForSchoolForm
from .models import School, Person
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    return render(request, 'school/index.html')

def create_school(request):
    if request.method == 'POST':
        request_post = request.POST
        school_form = SchoolForm(request_post)
        admin_for_school_form = AdminForSchoolForm(request_post)
        if school_form.is_valid() and admin_for_school_form.is_valid():
            # fetch data
            name = school_form.cleaned_data['name']
            country = school_form.cleaned_data['country']
            region = school_form.cleaned_data['region']
            city = school_form.cleaned_data['city']
            address = school_form.cleaned_data['address']
            # Perform actions with the form data, e.g., create a School instance
            ## if object exists just get, else create
            if School.objects.exists():
                if not School.objects.filter(name=name, country=country, region=region, city=city, address=address).exists():
                    school = School(name=name, country=country, region=region, city=city, address=address)
                    school.save()
                else:
                    school = School.objects.get(name=name, country=country, region=region, city=city, address=address)
            else:
                school = School(name=name, country=country, region=region, city=city, address=address)
                school.save()

            ## fetch data
            username = admin_for_school_form.cleaned_data['username']
            email = admin_for_school_form.cleaned_data['email']
            password = admin_for_school_form.cleaned_data['password']
            user = User(username=username,email=email,password=password)
            user.save()
            # .objects.create_user(username=username,email=email,password=password)

            first_name = admin_for_school_form.cleaned_data['first_name']
            middle_name = admin_for_school_form.cleaned_data['middle_name']
            last_name = admin_for_school_form.cleaned_data['last_name']
            address_for_admin = admin_for_school_form.cleaned_data['address_for_admin']
            ## Perform actions with the form data, e.g., create a School instance
            ## if object exists just get, else create
            if Person.objects.exists():
                if not Person.objects.filter(first_name=first_name,middle_name=middle_name,last_name=last_name,address=address_for_admin,school=school,user = user).exists():
                    admin = Person(first_name=first_name,middle_name=middle_name,last_name=last_name,address=address_for_admin,school=school,user = user)
                    admin.save()
                else:
                    admin = Person.objects.get(first_name=first_name,middle_name=middle_name,last_name=last_name,address=address_for_admin,school=school,user = user)
            else:
                admin = Person(first_name=first_name,middle_name=middle_name,last_name=last_name,address=address_for_admin,school=school,user = user) #,status='administrator'
                admin.save()
            # Redirect to a success page or another view
            return redirect('school:create_school')  # Replace 'success_page' with the actual URL name or path

    else:
        school_form = SchoolForm()
        admin_for_school_form = AdminForSchoolForm()
    return render(request, 'school/create_school.html', {'school_form': school_form,'admin_for_school_form': admin_for_school_form})