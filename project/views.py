from django.shortcuts import render,get_object_or_404
from .models import Proyek
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView

# Create your views here.
# def index(request):
#     proyeks= Proyek.objects.all()
#     paginator= Paginator(proyeks,5)
#     page_number= request.GET.get('page')
#     page_object=paginator.get_page(page_number)
#     context={
#         'title':'Projects',
#         'items': ['SQL', 'Power BI', 'Tableau', 'Dash', 'Django', 'Data Science', 'Classification'],
#         'proyek':proyeks,
#         'page_number':page_object
#     }
#     return render(request,'project/index.html',context)



class indexView(ListView):
    model = Proyek
    ordering = ['-tanggal']
    paginate_by = 6
    template_name = 'project/index.html'

    # Menambahkan extra_context langsung di dalam get_context_data
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Projects'
        context['item'] = ['Excel','SQL', 'Power-BI',
                           'Python','Streamlit', 'Django']
        return context

    def get_queryset(self):
        queryset = super().get_queryset()  # Mendapatkan queryset dasar dari ListView
        category = self.kwargs.get('category')

        if category and category != "ALL":
            queryset = queryset.filter(category__icontains=category)

        return queryset
    
    
    
    
def detail(request, slug):
    proyek = get_object_or_404(Proyek, slug=slug)
    context = {
        'title': 'Detail Projects',
        'proyek': proyek,
    }

    return render(request, 'project/detail.html', context)


