from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm

# Read: List all students
def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})

# Create: Add a new student
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'students/student_form.html', {'form': form})

# Update: Edit student details
def student_update(request, student_id):
    student = get_object_or_404(Student, StudentID=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/student_form.html', {'form': form})

# Delete: Remove a student record
def student_delete(request, student_id):
    student = get_object_or_404(Student, StudentID=student_id)
    student.delete()
    return redirect('student_list')

# Create your views here.
