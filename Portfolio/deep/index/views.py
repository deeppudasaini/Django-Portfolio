from django.shortcuts import render
from index.models import Project
# Create your views here.
def home(request):
    context={
        'title':"Home Page",
        'project_name':Project.objects.all()
    };
    
    return render(request,'index.html',context);