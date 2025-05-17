from django.shortcuts import render
from .models import ContactModel

# Create your views here.
def index(request):
    contact= ContactModel.objects.all()
    context={
        'title':'Contact',
    }
    return render(request,'contact/index.html',context)