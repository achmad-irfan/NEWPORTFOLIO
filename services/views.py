from django.shortcuts import render
from .models import offer

# Create your views here.
def index(request):
    offers=offer.objects.all()
    context={
        'title':'Services',
        'offer':offers
    }
    return render(request,'services/index.html',context)