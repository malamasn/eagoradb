from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.core import serializers


from .models import *
from .forms import *


class HomeView(generic.base.TemplateView):
    template_name = 'database/home.html'

    def get(self, request):

        args = {'msg': 'hello customer'}
        return render(request, self.template_name, args)

class ProductView(generic.ListView):
    template_name = 'database/product.html'
    model = Product

    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        form = ProductForm(instance = product)

        args = {'product': product, 'form': form}
        return render(request, self.template_name, args)



class FindProducts(generic.ListView):
    template_name = 'database/find_products.html'
    model = Product

    def get(self, request):

        products = serializers.serialize("python", Product.objects.all())
        product_form = ProductForm()
        args = {'products': products, 'product_form':product_form}
        return render(request, self.template_name, args)


class StoreView(generic.ListView):
    template_name = 'database/store.html'
    model = Store

    def get(self, request, pk):
        store = get_object_or_404(Store, pk=pk)
        form = StoreForm(instance = store)
        sells = Selling.objects.filter(store_id = pk)
        product_names = list()
        price_list = list()
        for i in sells:
            print(i.product_id.name, i.price)
        #     product = Product.objects.filter(pk = i.product_id)
        #     product_names.append(product.name)
        #     price_list.append(i.price)

        args = {'store': store, 'form': form,
                'product_names': product_names, 'price_list': price_list,
                'sells': sells}
        return render(request, self.template_name, args)


class FindStores(generic.ListView):
    template_name = 'database/find_stores.html'
    model = Store

    def get(self, request):
        stores = serializers.serialize("python", Store.objects.all())
        store_form = StoreForm()
        args = {'stores': stores, 'store_form':store_form}
        return render(request, self.template_name, args)
