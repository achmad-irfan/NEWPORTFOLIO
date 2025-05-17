from django.shortcuts import render
from .models import summaries

# Create your views here.
def index(request):
    summarry=summaries.objects.all()
    context={
        'title':'About me',
        'summary':summarry
    }
    return render(request,'about/index.html',context)