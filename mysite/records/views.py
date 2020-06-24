from django.shortcuts import render
from django.http  import HttpResponse,Http404
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required()
def home(request):
    return render(request,'records/home.html')

@login_required()
def about(request):

    return  Http404()