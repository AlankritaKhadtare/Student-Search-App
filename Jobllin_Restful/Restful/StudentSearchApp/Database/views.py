from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from Database.models import *
from django.urls import reverse
from Database.forms import UserForm
from django.contrib import messages
from django.db.models import Q

# Create your views here.

def student_list(request):
    context = {}
    students = Student.objects.all()
    context['students'] = students
    return render(request, 'Database/index.html', context)

def student_details(request, id = None):
    context = {}
    try:
        student = Student.objects.get(id=id)
    except:
        raise Http404
    context['student'] = get_object_or_404(Student,id=id)
    return render(request, 'Database/details.html', context)

def student_add(request):
    if request.method == "POST":
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('Student_list'))
        else:
            return render(request, 'database/add.html', {"user_form":user_form})
    else:
        user_form=UserForm()
        return render(request, 'database/add.html', {"user_form":user_form})

def student_edit(request, id=None):
    student = get_object_or_404(Student, id=id)
    if request.method == "POST":
        user_form = UserForm(request.POST, instance=student)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('Student_list'))
        else:
            return render(request, 'database/edit.html', {"user_form":user_form})
    else:
        user_form=UserForm(instance=student)
        return render(request, 'database/edit.html', {"user_form":user_form})

def student_delete(request, id=None):
    student=get_object_or_404(Student,id=id)
    if request.method=="POST":
        student.delete()
        return HttpResponseRedirect(reverse('Student_list'))
    else:
        context={}
        context['student']=student
        return render(request, 'database/delete.html', context)

def student_search(request):
    if request.method=="POST":
        roll=request.POST['Roll']
        name=request.POST['Name']
        age=request.POST['Age']
        clas=request.POST['Class']
        mail=request.POST['Mail']
        addr=request.POST['Address']
        match ={}
        flag=0

        if roll:
            match=Student.objects.filter(Q(st_roll__iexacts=roll))
            flag=1
         
        if name:
            match=Student.objects.filter(Q(st_name__icontains=name))
            flag=1

        if age:
            match=Student.objects.filter(Q(st_age__icontains=age))
            flag=1
        
        if clas:
            match=Student.objects.filter(Q(st_class__icontains=clas))
            flag=1
        
        if mail:
            match=Student.objects.filter(Q(st_mail__icontains=mail))
            flag=1
        
        if addr:
            match=Student.objects.filter(Q(st_address__icontains=addr))
            flag=1


        if match:
            return render(request, 'database/search.html', {'sr':match})
            flag=1 

        if not(match) and flag==1:
            messages.error(request,'No Result Found...!!!')

        else:
            match=Student.objects.all()
            
            if match:
                return render(request, 'database/search.html', {'sr':match})
            else:
                messages.error(request,'No Result Found...!!!')
    else:
        return render(request, 'database/search.html')