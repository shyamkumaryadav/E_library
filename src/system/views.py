from system import forms
from system import models
from django.db.models import Q
from system import mixins
from django.contrib import messages
from django.views import generic
from django.shortcuts import render, redirect
from django.http import JsonResponse, Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.translation import activate
from account.models import User
from django.utils.translation import gettext_lazy as _




class HomeView(generic.TemplateView):
    template_name = 'system/home.html'
    extra_context = {'title': 'Home'}


class privacyView(generic.TemplateView):
    template_name = 'system/privacy.html'
    extra_context = {'title': 'Privacy'}


class TermsView(generic.TemplateView):
    template_name = 'system/terms.html'
    extra_context = {'title': 'Terms'}



class MemberManagementView(mixins.AdminRequiredMixin, generic.UpdateView, generic.ListView):
    template_name = 'system/adminmembermanagement.html'
    model = User
    extra_context = {'title': 'Member management'}
    template_name = 'system/adminmembermanagement.html' 
    search_kwarg = 'q'
    paginate_by = 5
    form_class = forms.MemberForm

    def get_object(self, queryset=None):
        try:
            username = self.request.GET.get('username')
            if queryset is None:
                queryset = self.get_queryset()
                queryset = queryset.filter(username__icontains=username)
                obj = queryset.get()
                return obj
        except:
            pass
    
    def form_valid(self, form):
        form.save(request=self.request)
        return super().form_valid(form)
    
    def post(self, request, *args, **kwargs):
        user = self.get_object()
        if request.POST.get('is_superuser') == '1':
            user.is_superuser = True
        elif request.POST.get('is_superuser') == '0':
            user.is_superuser = False
        if request.POST.get('is_active') == '1':
            user.is_active = True
        elif request.POST.get('is_active') == '0':
            user.is_active = False
        if request.POST.get('send_mail') == '1':
            pass
        user.save()
        return HttpResponseRedirect(self.get_success_url())
    
    def get_success_url(self):
        messages.success(self.request, 'User Update Success.')
        return reverse_lazy('system:membermanagement')

class MemberManagementDeleteView(mixins.AdminRequiredMixin, generic.DeleteView):
    model = User
    http_method_names = ['post',]

    def get_success_url(self):
        messages.success(self.request, 'User Delete Success.')
        return reverse_lazy('system:membermanagement')

class ViewBookView(generic.ListView):
    model = models.Book
    search_kwarg = 'q'
    paginate_by = 5
    template_name = 'system/viewbooks.html'
    extra_context = {'title': 'Books'}
    
    def get_queryset(self, *args, **kwargs):
        search_kwarg = self.search_kwarg
        name = self.request.GET.get(search_kwarg)
        if name:
            object_list = self.model._default_manager.filter(
                name__icontains=name)
        else:
            object_list = self.model._default_manager.all()
        return object_list


class AuthorManagementView(mixins.AdminRequiredMixin, generic.CreateView, generic.ListView):
    template_name = 'system/adminauthormanagement.html'
    model = models.BookAuthor
    search_kwarg = 'q'
    paginate_by = 5
    success_url = reverse_lazy('system:authormanagement')
    form_class = forms.BookAuthorForm
    extra_context = {'title': 'Author management'}

    def get_context_data(self, **kwargs):
        self.object = None
        self.object_list = self.get_queryset()

        form_class = self.get_form_class()
        form = self.get_form(form_class)

        kwargs.update({'object_list': self.object_list, 'form': form})

        context = super(AuthorManagementView,
                        self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        search_kwarg = self.search_kwarg
        name = self.request.GET.get(search_kwarg)
        if name:
            object_list = self.model._default_manager.filter(
                first_name__icontains=name)
        else:
            object_list = self.model._default_manager.all()
        return object_list



class AuthorManagementUpdateView(mixins.AdminRequiredMixin, generic.UpdateView):
    template_name = 'system/adminauthormanagement.html'
    model = models.BookAuthor
    success_url = reverse_lazy('system:authormanagement')
    form_class = forms.BookAuthorForm
    extra_context = {'title': 'Author management'}

class AuthorManagementDeleteView(mixins.AdminRequiredMixin, generic.DeleteView):
    model = models.BookAuthor
    http_method_names = ['post',]

    def get_success_url(self):
        messages.success(self.request, 'Author Delete Success.')
        return reverse_lazy('system:authormanagement')


class BookIssuingView(mixins.AdminRequiredMixin, generic.ListView, generic.edit.BaseCreateView):
    model = models.Issue
    form_class = forms.IssueForm
    paginate_by = 5
    search_kwarg = 'q'
    success_url = reverse_lazy('system:bookissuing')
    template_name = 'system/adminbookissuing.html'
    extra_context = {'title': 'admin book issuing'}

    def get_context_data(self, **kwargs):
        self.object = None
        self.object_list = self.get_queryset()

        form_class = self.get_form_class()
        form = self.get_form(form_class)

        kwargs.update({'object_list': self.object_list, 'form': form})

        context = super(BookIssuingView,
                        self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        search_kwarg = self.search_kwarg
        name = self.request.GET.get(search_kwarg)
        if name:
            object_list = self.model._default_manager.filter(
                Q(name__icontains=name)
            )
        else:
            object_list = self.model._default_manager.all()
        return object_list


class BookInventoryView(mixins.AdminRequiredMixin, generic.ListView, generic.edit.BaseCreateView):
    form_class = forms.BookForm
    model = models.Book
    paginate_by = 5
    search_kwarg = 'q'
    success_url = reverse_lazy('system:bookinventory')
    template_name = 'system/adminbookinventory.html'
    extra_context = {'title': 'admin book inventory'}

    def get_context_data(self, **kwargs):
        self.object = None
        self.object_list = self.get_queryset()

        form_class = self.get_form_class()
        form = self.get_form(form_class)

        kwargs.update({'object_list': self.object_list, 'form': form})

        context = super(BookInventoryView,
                        self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        search_kwarg = self.search_kwarg
        name = self.request.GET.get(search_kwarg)
        if name:
            object_list = self.model._default_manager.filter(
                Q(name__icontains=name)
            )
        else:
            object_list = self.model._default_manager.all()
        return object_list

class BookIssuingUpdateView(mixins.AdminRequiredMixin, generic.UpdateView):
    model = models.Issue
    form_class = forms.IssueForm
    success_url = reverse_lazy('system:bookissuing')
    template_name = 'system/adminbookissuing.html'
    extra_context = {'title': 'admin book issuing'}


class BookIssuingDeleteView(mixins.AdminRequiredMixin, generic.DeleteView):
    model = models.Issue
    http_method_names = ['post',]

    def get_success_url(self):
        messages.success(self.request, 'Issued Book Delete Success.')
        return reverse_lazy('system:bookissuing')

class BookInventoryDetailView(mixins.AdminRequiredMixin, generic.DetailView):
    form_class = forms.BookForm
    model = models.Book
    success_url = reverse_lazy('system:bookinventory')
    template_name = 'system/viewbooksdetail.html'
    extra_context = {'title': 'admin book inventory'}

class BookInventoryUpdateView(mixins.AdminRequiredMixin, generic.UpdateView):
    form_class = forms.BookForm
    model = models.Book
    success_url = reverse_lazy('system:bookinventory')
    template_name = 'system/adminbookinventory.html'
    extra_context = {'title': 'admin book inventory Update'}

class BookInventoryDeleteView(mixins.AdminRequiredMixin, generic.DeleteView):
    model = models.Book
    http_method_names = ['post',]

    def get_success_url(self):
        messages.success(self.request, 'Book Delete Success.')
        return reverse_lazy('system:bookinventory')



class PublisherManagementView(mixins.AdminRequiredMixin, generic.ListView, generic.edit.BaseCreateView):
    form_class = forms.BookPublishForm
    paginate_by = 5
    search_kwarg = 'q'
    model = models.BookPublish
    success_url = reverse_lazy('system:publishermanagement')
    template_name = 'system/adminpublishermanagement.html'
    extra_context = {'title': 'admin publisher management'}

    def get_context_data(self, **kwargs):
        self.object = None
        self.object_list = self.get_queryset()

        form_class = self.get_form_class()
        form = self.get_form(form_class)

        kwargs.update({'object_list': self.object_list, 'form': form})

        context = super(PublisherManagementView,
                        self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        search_kwarg = self.search_kwarg
        search = self.request.GET.get(search_kwarg)
        if search:
            object_list = self.model._default_manager.filter(
                Q(name__icontains=search) | Q(address__icontains=search)
            )
        else:
            object_list = self.model._default_manager.all()
        return object_list


class PublisherManagementUpdateView(mixins.AdminRequiredMixin, generic.UpdateView):
    template_name = 'system/adminpublishermanagement.html'
    model = models.BookPublish
    success_url = reverse_lazy('system:publishermanagement')
    form_class = forms.BookPublishForm
    extra_context = {'title': 'Author management'}

class PublisherManagementDeleteView(mixins.AdminRequiredMixin, generic.DeleteView):
    model = models.BookPublish
    http_method_names = ['post',]

    def get_success_url(self):
        messages.success(self.request, 'Publisher Delete Success.')
        return reverse_lazy('system:publishermanagement')



class ShyamkumaryadavView(generic.TemplateView):
    template_name = 'system/shyamkumaryadav.html'
    extra_context = {'title': 'shyamkumar yadav'}
