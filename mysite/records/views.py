from django.shortcuts import render
from django.http  import HttpResponse,Http404
from django.contrib.auth.decorators import login_required
from .models import  records_list
# Create your views here.

@login_required()
def home(request):
    context={
        'records':records_list.objects.all()
    }
    return render(request,'records/home.html',context)

@login_required()
def about(request):

    return  Http404()