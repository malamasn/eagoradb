from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.core import serializers
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect


from .models import *
from .forms import *


def signup(request):
    template_name = 'database/signup.html'

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            credit_card = form.cleaned_data.get('credit_card')
            email = form.cleaned_data.get('email')
            user = authenticate(username=username, password=raw_password,
                                credit_card=credit_card, email=email)
            login(request, user)
            return redirect(render('database:home'))
    else:
        form = SignUpForm()
    return render(request, template_name, {'form': form})


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
        sold = Selling.objects.filter(product_id = pk)
        args = {'product': product, 'form': form, 'sold': sold}
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
        args = {'store': store, 'form': form, 'sells': sells}
        return render(request, self.template_name, args)


class FindStores(generic.ListView):
    template_name = 'database/find_stores.html'
    model = Store

    def get(self, request):
        stores = serializers.serialize("python", Store.objects.all())
        store_form = StoreForm()
        args = {'stores': stores, 'store_form':store_form}
        return render(request, self.template_name, args)
