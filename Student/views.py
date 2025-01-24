from django.shortcuts import redirect, render,HttpResponse
from .models import Students
from .forms import StudentForm
from django.contrib import messages

# Create your views here.

def home(request):
    students = Students.objects.all()
    
    context = {
        'students': students
    }
    return render(request, 'home.html',context)

def create_student(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student created successfully.')
            return redirect('home')
        else:
            return HttpResponse('Something went wrong')
    return render(request, 'create_student.html', context={'form': form})

def update_student(request, student_id):
    student = Students.objects.get(id=student_id)
    form = StudentForm(instance=student)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student updated successfully.')
            return redirect('home')
        else:
            return HttpResponse('Something went wrong')
    return render(request, 'create_student.html', context={'form': form, 'update': True})


def delete_student(request, student_id):
    student = Students.objects.get(id=student_id)
    student.delete()
    messages.success(request, 'Student deleted successfully.')
    return redirect('home')