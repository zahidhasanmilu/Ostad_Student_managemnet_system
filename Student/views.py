from django.shortcuts import redirect, render, HttpResponse
from django.urls import reverse_lazy
from .models import Students
from .forms import StudentForm
from django.contrib import messages
from django.views.generic import ListView, TemplateView, CreateView, UpdateView, DeleteView


# Create your views here.
###############################################################
# def home(request):
#     students = Students.objects.all()

#     context = {
#         'students': students
#     }
#     return render(request, 'home.html',context)

class Home(ListView):
    model = Students
    template_name = 'home.html'
    context_object_name = 'students'

###############################################################


# def create_student(request):
#     form = StudentForm()
#     if request.method == 'POST':
#         form = StudentForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Student created successfully.')
#             return redirect('home')
#         else:
#             return HttpResponse('Something went wrong')
#     return render(request, 'create_student.html', context={'form': form})

class Create_student(CreateView):
    model = Students
    template_name = 'create_student.html'
    form_class = StudentForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # Get the student name from the form data (before saving)
        student_name = form.cleaned_data['name']
        messages.success(self.request, f'"{student_name}" - Student created successfully.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Student not created. Please check the form.')
        return render(self.request, self.template_name, {'form': form})
    

###############################################################

# def update_student(request, student_id):
#     student = Students.objects.get(id=student_id)
#     form = StudentForm(instance=student)
#     if request.method == 'POST':
#         form = StudentForm(request.POST, request.FILES, instance=student)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Student updated successfully.')
#             return redirect('home')
#         else:
#             return HttpResponse('Something went wrong')
#     return render(request, 'create_student.html', context={'form': form, 'update': True})


class UpdateStudent(UpdateView):
    model = Students
    template_name = 'create_student.html'
    form_class = StudentForm
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'student_id'
    context_object_name = 'student'

    def form_valid(self, form):
        student_name = self.object.name
        messages.success(self.request, f'"{student_name}" - Student updated successfully.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Student not updated.')
        return render(self.request, self.template_name, {'form': form})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["update"] = True
        return context


###############################################################


# def delete_student(request, student_id):
#     student = Students.objects.get(id=student_id)
#     student.delete()
#     messages.success(request, 'Student deleted successfully.')
#     return redirect('home')


class Delete_student(DeleteView):
    model = Students
    pk_url_kwarg = "student_id"
    template_name = 'delete_student.html'
    success_url = reverse_lazy('home')
    context_object_name = 'student'
    
    
    def delete(self, request, *args, **kwargs):
        # Add success message
        student_name = self.get_object().name  # Retrieve the student name before deletion
        messages.success(self.request, f'Student "{student_name}" deleted successfully.')
        return super().delete(request, *args, **kwargs)
    