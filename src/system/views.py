from system import forms
from system import models
from django.db.models import Q
from system import mixins
from django.views import generic
from django.shortcuts import render, redirect
from django.http import JsonResponse, Http404
from django.urls import reverse_lazy
from django.utils.translation import activate


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
    template_name = 'system/viewbooks.html'

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
    paginate_by = 3
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


class AuthorManagementUpdateView(generic.UpdateView):
    template_name = 'system/adminauthormanagement.html'
    model = models.BookAuthor
    success_url = reverse_lazy('system:authormanagement')
    form_class = forms.BookAuthorForm
    extra_context = {'title': 'Author management'}

    def post(self, request, *args, **kwargs):
        try:
            if self.request.POST.get('Delete'):
                self.model._default_manager.get(
                    pk=self.request.POST.get('Delete')).delete()
                return redirect(self.success_url)
        except self.model.DoesNotExist:
            raise Http404(
                f"No {self.model._meta.verbose_name}s found matching the query")
        return super().post(request, *args, **kwargs)


class MemberManagementView(generic.TemplateView):
    template_name = 'system/adminmembermanagement.html'
    extra_context = {'title': 'Member management'}


class BookIssuingView(generic.TemplateView):
    template_name = 'system/adminbookissuing.html'
    extra_context = {'title': 'admin book issuing'}


class BookInventoryView(mixins.AdminRequiredMixin, generic.ListView, generic.edit.BaseCreateView):
    form_class = forms.BookForm
    model = models.Book
    paginate_by = 3
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
                name__icontains=name)
        else:
            object_list = self.model._default_manager.all()
        print(object_list)
        return object_list


class BookInventoryUpdateView(mixins.AdminRequiredMixin, generic.UpdateView):
    form_class = forms.BookForm
    model = models.Book
    success_url = reverse_lazy('system:bookinventory')
    template_name = 'system/adminbookinventory.html'
    extra_context = {'title': 'admin book inventory Update'}

    def post(self, request, *args, **kwargs):
        try:
            if self.request.POST.get('Delete'):
                self.model._default_manager.get(
                    pk=self.request.POST.get('Delete')).delete()
                return redirect(self.success_url)
        except self.model.DoesNotExist:
            raise Http404(
                f"No {self.model._meta.verbose_name}s found matching the query")
        return super().post(request, *args, **kwargs)


class PublisherManagementView(mixins.AdminRequiredMixin, generic.ListView, generic.edit.BaseCreateView):
    form_class = forms.BookPublishForm
    paginate_by = 3
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
        name = self.request.GET.get(search_kwarg)
        if name:
            object_list = self.model._default_manager.filter(
                name__icontains=name)
        else:
            object_list = self.model._default_manager.all()
        print(object_list)
        return object_list


class PublisherManagementUpdateView(mixins.AdminRequiredMixin, generic.UpdateView):
    template_name = 'system/adminpublishermanagement.html'
    model = models.BookPublish
    success_url = reverse_lazy('system:publishermanagement')
    form_class = forms.BookPublishForm
    extra_context = {'title': 'Author management'}

    def post(self, request, *args, **kwargs):
        try:
            if self.request.POST.get('Delete'):
                self.model._default_manager.get(
                    pk=self.request.POST.get('Delete')).delete()
                return redirect(self.success_url)
        except self.model.DoesNotExist:
            raise Http404(
                f"No {self.model._meta.verbose_name}s found matching the query")
        return super().post(request, *args, **kwargs)


class ShyamkumaryadavView(generic.TemplateView):
    template_name = 'system/shyamkumaryadav.html'
    extra_context = {'title': 'shyamkumar yadav'}
