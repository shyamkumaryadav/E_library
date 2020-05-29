from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views import generic
from . import mixins
from django.db.models import Q
from . import models
from . import forms

class HomeView(generic.TemplateView):
    template_name = 'system/home.html'
    extra_context = {'title': 'Home'}


class aboutView(generic.TemplateView):
    template_name = 'system/about.html'
    extra_context = {'title': 'About'}

class TermsView(generic.TemplateView):
    template_name = 'system/terms.html'
    extra_context = {'title': 'Terms'}

class ViewBookView(generic.ListView):
    model = models.Book
    search_kwarg = 'q'
    paginate_by = 5
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

class AuthorManagementView(mixins.AdminRequiredMixin, generic.CreateView, generic.ListView):
    template_name = 'system/adminauthormanagement.html'
    model = models.BookAuthor
    search_kwarg = 'q'
    paginate_by = 3
    success_url = reverse_lazy('system:authormanagement')
    ordering = 'first_name'
    form_class = forms.BookAuthorForm
    extra_context = {'title': 'Author management'}

    def get_queryset(self):
        search_kwarg = self.search_kwarg
        name = self.kwargs.get(
            search_kwarg) or self.request.GET.get(search_kwarg)
        if name:
            object_list = self.model.objects.filter(first_name__icontains=name)
        else:
            object_list = self.model.objects.all()
        return object_list


class AuthorManagementUpdateView(generic.UpdateView, generic.DeleteView):
    template_name = 'system/adminauthormanagement.html'
    model = models.BookAuthor
    success_url = reverse_lazy('system:authormanagement')
    form_class = forms.BookAuthorForm
    extra_context = {'title': 'Author management'}

    def post(self, request, *args, **kwargs):
        if self.request.POST['Delete']:
            self.model.objects.filter(pk=self.request.POST['Delete']).delete()
            return redirect(self.success_url)
        return super().post(request, *args, **kwargs)

class MemberManagementView(generic.TemplateView):
    template_name = 'system/adminmembermanagement.html'
    extra_context = {'title': 'Member management'}

class BookIssuingView(generic.TemplateView):
    template_name = 'system/adminbookissuing.html'
    extra_context = {'title': 'admin book issuing'}

class BookInventoryView(generic.TemplateView):
    template_name = 'system/adminbookinventory.html'
    extra_context = {'title': 'admin book inventory'}


class PublisherManagementView(generic.TemplateView):
    template_name = 'system/adminpublishermanagement.html'
    extra_context = {'title': 'admin publisher management'}

class ShyamkumaryadavView(generic.TemplateView):
    template_name = 'system/shyamkumaryadav.html'
    extra_context = {'title': 'shyamkumar yadav'}
