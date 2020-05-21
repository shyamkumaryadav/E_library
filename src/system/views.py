from django.shortcuts import render
from django.http import JsonResponse
from django.views import generic
from django.db.models import Q
from .models import Book
from .forms import ExampleForm


from django.template.context_processors import csrf
from crispy_forms.utils import render_crispy_form


def save_example_form(request):
    form = ExampleForm(request.POST)
    ctx = {}
    ctx.update(csrf(request))
    form_html = render_crispy_form(form, context=ctx)
    return JsonResponse({'success': False, 'form_html': form_html})


def home(request):
    template_name = 'system/home.html'
    context = {
        'title': 'Home'
    }
    return render(request, template_name, context)


def about(request):
    template_name = 'system/about.html'
    context = {
        'title': 'About'
    }
    return render(request, template_name, context)


def terms(request):
    template_name = 'system/terms.html'
    context = {
        'title': 'Terms',
    }
    return render(request, template_name, context)


class ViewBookView(generic.ListView):
    model = Book
    search_kwarg = 'q'
    paginate_by = 6
    ordering = 'name'
    template_name = 'system/viewbooks.html'

    def get_queryset(self):
        search_kwarg = self.search_kwarg
        name = self.kwargs.get(
            search_kwarg) or self.request.GET.get(search_kwarg)
        if name:
            object_list = self.model.objects.filter(name__icontains=name)
        else:
            object_list = self.model.objects.all()
        return object_list


def adminauthormanagement(request):
    template_name = 'system/adminauthormanagement.html'
    context = {
        'title': 'admin author management'
    }
    return render(request, template_name, context)


def adminmembermanagement(request):
    template_name = 'system/adminmembermanagement.html'
    context = {
        'title': 'admin member management'
    }

    return render(request, template_name, context)


def adminbookissuing(request):
    template_name = 'system/adminbookissuing.html'
    context = {
        'title': 'admin book issuing'
    }
    return render(request, template_name, context)


def adminbookinventory(request):
    template_name = 'system/adminbookinventory.html'
    context = {
        'title': 'admin book inventory'
    }
    return render(request, template_name, context)


def adminpublishermanagement(request):
    template_name = 'system/adminpublishermanagement.html'
    context = {
        'title': 'admin publisher management'
    }
    return render(request, template_name, context)


def shyamkumaryadav(request):
    template_name = 'system/shyamkumaryadav.html'
    context = {
        'title': 'shyamkumar yadav'
    }
    return render(request, template_name, context)
