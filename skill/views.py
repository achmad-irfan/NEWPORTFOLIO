from django.shortcuts import render
from .models import listskill

# Create your views here.
def index(request):
    skills=listskill.objects.all()
    context={
        'title':'Skill',
        'skill':skills
    }
    return render(request,'skill/index.html',context)