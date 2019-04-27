from django.shortcuts import render
from django.views.generic import TemplateView, View, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from . import models
from django.urls import reverse_lazy
# Create your views here.


# def index(request):
# return render(request, 'index.html')


# class CBView(View):
# def get(self, request):
# return HttpResponse("LETS SEE IF THIS IS WORKING!!!")

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'BASIC INJECTION!'

        return context

# list out all schools in the database


class SchoolListView(ListView):
    # ListView class automatically creates 'school_List' (takes class, lowercases it and adds _List to end by default)
    # with context_object_name we can define our own object name
    context_object_name = 'schools'
    # connect view to model
    model = models.School


# show details of each school in schoolmodel database
class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'adv_app/school_detail.html'


class SchoolCreateView(CreateView):
    # create view requires you set the fields from whatever model you want to create
    fields = ('name', 'principal', 'location')
    model = models.School


class SchoolUpdateView(UpdateView):
    fields = ('name', 'principal')
    model = models.School


class SchoolDeleteView(DeleteView):
    model = models.School
    # reverse_lazy vs reverse basically means its only called once success is true instead of automatically called each time
    success_url = reverse_lazy("adv_app:list")
