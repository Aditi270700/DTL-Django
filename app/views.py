from django.shortcuts import render
from .models import Student

# Create your views here.
def home(request):
    stu = Student.objects.all()
    print(stu)
    return render(request, 'home.html',{'data':stu.values(),'data2':"kuch nhi"})