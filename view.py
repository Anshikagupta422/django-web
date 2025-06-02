
from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    data={
        'title':'Home page',
        'clist':['java','python','c++','c','php'],
        'number':[1,2,3,4,5,6,7,8,9,10],
        'student_details':[
            {'name':'sachin','age':20},
            {'name':'rohit','age':20},
            {'name':'virat','age':20},
            {'name':'dhoni','age':20},
            {'name':'rahul','age':20},
        ]
        
    }
    return render(request,"index.html",data)

def aboutUS(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def courseDetails(request , courseid):
    return HttpResponse(courseid)