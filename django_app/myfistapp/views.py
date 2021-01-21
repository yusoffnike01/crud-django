from django.shortcuts import render
from django.http import HttpResponse
from .models import EMpProfile
# Create your views here.


def home(request):
    #  return HttpResponse("Welcome to my Website")
    return render(request,'myfistapp/myfistapp.html')
    

def about(request):
    # return HttpResponse("About Us")
    name=['Yusoff','Haizq','Aiman']
    age=[1,2,3]
    dict_data={
        'name':zip(name,age)
              }
    return render(request,'myfistapp/about.html',dict_data)

def contact_us(request):
    return render(request,'myfistapp/contactus.html')

def update_table(request):
    return render(request,'myfistapp/updatedata.html')

def insert_data(request):
    name=request.POST.get('ename')
    salary=float(request.POST.get('esalary'))
    try:
        obj=EMpProfile(name=name,salary=salary)
        obj.save()
    except Exception as ex:
        print(ex)
    return HttpResponse("Data Inserted")

def retrieve_data(request):
    mydata=EMpProfile.objects.all()
    data_dict={
        'data':mydata
    }
    return render(request,'myfistapp/display.html',data_dict)

def delete_data(request):
    del_data=request.POST.getlist('datadelete')
    for item in del_data:
        EMpProfile.objects.filter(name=item).delete()
    return HttpResponse("Data has been deleted")

def update_salary(request):
    try:
        name=request.POST.get('ename')
        salary=float(request.POST.get('esalary'))
        EMpProfile.objects.filter(name=name).update(salary=salary)
    except Exception as ex:
        print("Err")
    return HttpResponse("Data Update")

    
      

