from django.shortcuts import render
from django.http import HttpResponse 

# create views here

def index(request):
	return HttpResponse("<h1 style='color:red; text-align:center; font-size:100px;margin-top:200px; background-color:green;'vee_nits123</h1>")

def show(request):
	return render(request,'index.html')

def display(request):
	name="vee_nits123"
	return render(request,'disp.html',{'uname':name})

def sample(request):
	name="vee_nits123"
	dept="CSE"
	return render(request,"sample.html",{'name':name,'dept':dept})