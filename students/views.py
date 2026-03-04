from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student

def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})


def add_student(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        course = request.POST['course']
        age = request.POST['age']

        Student.objects.create(
            name=name,
            email=email,
            course=course,
            age=age
        )

        return redirect('student_list')

    return render(request, 'students/student_form.html')


def update_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        student.name = request.POST['name']
        student.email = request.POST['email']
        student.course = request.POST['course']
        student.age = request.POST['age']
        student.save()

        return redirect('student_list')

    return render(request, 'students/student_form.html', {'student': student})


def delete_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        student.delete()
        return redirect('student_list')

    return render(request, 'students/student_delete.html', {'student': student})
