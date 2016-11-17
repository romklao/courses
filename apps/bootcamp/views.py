from django.shortcuts import render, redirect
from .models import Course

# Create your views here.
def index(request):
    context = {
        "courses": Course.objects.all()
    }

    return render(request, 'index.html', context)

def delete(request):
    course = Course.objects.get(id=request.POST['id'])
    course.delete()
    return redirect('/')

def add(request):
    Course.objects.create(name=request.POST['name'],
                          description=request.POST['description'])

    return redirect('/')
