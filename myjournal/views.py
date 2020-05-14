from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Entry
from django.views.generic import (ListView,
                                DetailView,
                                CreateView,
                                UpdateView,
                                DeleteView
                                )
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


@login_required
def journal(request):
    context = {
        'entries': Entry.objects.all()
    }

    return render(request, 'myjournal/journal.html', context)


# @method_decorator(login_required,name='journal')
class EntryListView(LoginRequiredMixin, ListView):
    model = Entry
    template_name = 'myjournal/journal.html'
    context_object_name = 'entries'
    paginate_by = 2
    
    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user).order_by('-date_posted')


class EntryDetailView(LoginRequiredMixin, DetailView):
    model = Entry



class EntryCreateView(LoginRequiredMixin, CreateView):
    model = Entry
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class EntryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Entry
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



class EntryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Entry
    success_url = '/journal'
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    
    return render(request, 'myjournal/about.html', {'title':'About'})


def home(request):
    
    return render(request, 'myjournal/home.html', {'title':'Home'})