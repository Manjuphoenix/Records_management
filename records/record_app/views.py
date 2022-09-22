from django.core.paginator import Paginator
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, CreateView
from django.contrib.auth.decorators import login_required
from .views import *
from .forms import *
from django.urls import path, include
from .models import *
from django.template import loader
from django.db.models import Q

@login_required
def AddRecordsView(request):
    form = AddRecordsForm(request.POST or None)
    count = Mytable.objects.count()
    if form.is_valid():
        form.save()
        messages.success(request, "The next record number will be %d" %(count+170))
        form = AddRecordsForm()
    context = {
            'form': form,
            'count': count+179,
            'new': count+180,
            }
    return render(request, "new.html", context)


def index(request):
    queryset = Mytable.objects.all()
    paginator = Paginator(queryset, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
            "object_list": queryset
            }
    return render(request, "index.html", {'page_obj': page_obj})


def listAuthorRecords(request):
    page = request.GET.get('page', 1)
    query = request.GET.get('q', '')
    if query is None or query == '':
        query = Mytable.objects.all()
        paginator = Paginator(query, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
                "object_list": query
                }
        return render(request, "index.html", {'records': page_obj})
    else:
        record_list = Mytable.objects.filter(author__icontains=query)
        paginator = Paginator(record_list, 10)
        try:
            records_l = paginator.page(page)
        except PageNotAnInteger:
            records_l = paginator.page(1)
        except Emptypage:
            records_l = paginator.page(paginator.num_pages)
        return render(request, 'index.html', {'records': records_l, 'query': query})




def listTitleRecords(request):
    page = request.GET.get('page', 1)
    query = request.GET.get('q', '')
    if query is None or query == '':
        query = Mytable.objects.all()
        paginator = Paginator(query, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
                "object_list": query
                }
        return render(request, "index2.html", {'records': page_obj})
    else:
        record_list = Mytable.objects.filter(title__icontains=query)
        paginator = Paginator(record_list, 10)
        try:
            records_l = paginator.page(page)
        except PageNotAnInteger:
            records_l = paginator.page(1)
        except Emptypage:
            records_l = paginator.page(paginator.num_pages)
        return render(request, 'index2.html', {'records': records_l, 'query': query})



def listKeywordsRecords(request):
    page = request.GET.get('page', 1)
    query = request.GET.get('q', '')
    if query is None or query == '':
        query = Mytable.objects.all()
        paginator = Paginator(query, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
                "object_list": query
                }
        return render(request, "index1.html", {'records': page_obj})
    else:
        record_list = Mytable.objects.filter(keywords__icontains=query)
        paginator = Paginator(record_list, 10)
        try:
            records_l = paginator.page(page)
        except PageNotAnInteger:
            records_l = paginator.page(1)
        except Emptypage:
            records_l = paginator.page(paginator.num_pages)
        return render(request, 'index1.html', {'records': records_l, 'query': query})





def about(request):
    return render(request, "about.html")


class SearchView(ListView):
    template_name = 'index2.html'
    model = Mytable
    paginate_by = 10
    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            object_list = Mytable.objects.filter(Q(title__icontains=query))
            return object_list
        else:
            return Mytable.objects.all()


class SearchViewAuthor(ListView):
    model = Mytable
    paginate_by = 10
    template_name = 'index.html'
    objects = Mytable.objects.all()
    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            object_list = Mytable.objects.filter(Q(author__icontains=query)),
            return object_list
        else:
            return Mytable.objects.all()

class SearchViewKeywords(ListView):
    model = Mytable
    paginate_by = 10
    template_name = 'index1.html'
    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            object_list = Mytable.objects.filter(Q(keywords__icontains=query))
            return object_list
        else:
            return Mytable.objects.all()



def dynamic_record_view(request):
    context['object_list'] = article.objects.filter(title__icontains=request.GET.get('search'))
    return render(request, "../templates/record_detail.html", context)
