from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import TeacherModel
from .forms import TeacherForm


# Create your views here.
#prints all the teachers on index page
def index(request):
    allTeachers = TeacherModel.objects.all()
    context = {
        "allTeachers": allTeachers
    }
    return render(request, "teacherInvoiceApp/index.html", context)

# provides a form for the form page
def invoice(request):
    teacherForm = TeacherForm(request.POST or None)
    if teacherForm.is_valid():
        teacherForm.save()
        return redirect(index)
    context = {
        "teacherForm": teacherForm
    }
    return render(request, "teacherInvoiceApp/invoiceForm.html", context)
