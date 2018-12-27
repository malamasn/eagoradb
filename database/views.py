from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic


from .models import *


class HomeView(generic.base.TemplateView):
    template_name = 'database/home.html'

    def get(self, request):

        args = {'msg': 'hello customer'}
        return render(request, self.template_name, args)



class FindProducts(generic.ListView):
    template_name = 'database/find_products.html'
    model = Product

    def get(self, request):
        args = {'msg': 'hello there'}
        return render(request, self.template_name, args)



class FindStores(generic.ListView):
    template_name = 'database/find_stores.html'
    model = Store

    def get(self, request):
        args = {'msg': 'hello there we have these stores for you'}
        return render(request, self.template_name, args)
