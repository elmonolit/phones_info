from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView,CreateView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models,forms
from django.urls import reverse_lazy,reverse
from django.core.paginator import Paginator

class Index(ListView):
    model = models.Brand
    template_name='showcase/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        phone_list = models.Phone_model.objects.all()[:3]
        context['phone_list'] = phone_list
        return context

class PhonesList(ListView):
    paginate_by = 5
    model = models.Phone_model
    template_name = 'showcase/phone_list.html'
    context_object_name = 'phones_list'


class BrandDetail(DetailView):
    model = models.Brand
    template_name = 'showcase/brand_detail.html'

class PhoneDetail(DetailView):
    model = models.Phone_model
    template_name = 'showcase/phone_detail.html'
    context_object_name = 'phone'


class PhoneCreate(LoginRequiredMixin,CreateView):
    form_class = forms.PhoneForm
    template_name = 'showcase/phone_create.html'
    success_url = reverse_lazy('index')
    def get_success_url(self):
        return reverse('phone_detail', kwargs={'slug':self.object.slug})

class BrandCreate(LoginRequiredMixin,CreateView):
    form_class = forms.BrandForm
    template_name = 'showcase/brand_create.html'
    def get_success_url(self):
        return reverse('brand_detail', kwargs={'slug':self.object.slug})

class Search(View):
    def get_objects(self,name_startwith=''):
        objects_list = []
        if name_startwith:
            objects_brand = models.Phone_model.objects.filter(phone_brand=1)
            objects_list = models.Phone_model.objects.filter(phone_model__istartswith=name_startwith)
            # print(name_startwith)
            print(objects_list)
            print(objects_brand[0])
            # objects_list.extend(objects_brand)
        return objects_list

    def get(self,request):
        search_list = []
        starts_with = request.GET['search_bar']
        search_list = self.get_objects(starts_with)
        # print(search_list)
        return render(request, 'showcase/search.html',{'search_list':search_list})