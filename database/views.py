from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.core import serializers
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
import itertools
from decimal import Decimal


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
            my_group = Group.objects.get(name='client')
            my_group.user_set.add(user)
            return redirect(reverse('database:home'))
    else:
        form = SignUpForm()
    return render(request, template_name, {'form': form})




class ProfileView(generic.base.TemplateView):
    template_name = 'database/profile.html'

    def get(self, request):
        form = SignUpForm(instance = request.user)
        args = {'form': form, 'user': request.user}
        return render(request, self.template_name, args)

    def post(self, request):
        form = UserProfileForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            return redirect(reverse('database:profile'))


class PasswordView(generic.base.TemplateView):
    template_name = 'database/change_password.html'

    def get(self, request):
        form = PasswordChangeForm(user = request.user)
        args = {'form': form, 'user': request.user}
        return render(request, self.template_name, args)

    def post(self, request):
        form = PasswordChangeForm(data = request.POST, user = request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('database:view_profile'))
        else:
            return redirect(reverse('database:change_password'))





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

class MakeOrderView(generic.ListView):
    template_name = 'database/make_order.html'
    model = Store

    def get(self, request, pk):
        store = get_object_or_404(Store, pk=pk)
        form = StoreForm(instance = store)
        sells = Selling.objects.filter(store_id = pk)
        args = {'store': store, 'form': form, 'sells': sells}
        return render(request, self.template_name, args)

    def post(self, request, pk):
        #get post data and omit csdftoken and 'order' aka post.name
        orders = request.POST.items()
        orders = itertools.islice(orders, 2, None)

        #create an order
        store = Store.objects.get(pk=pk)
        order_model = Orders.objects.create(store_id = store, client=request.user,
                            status = '0', cost = 0)
        #for every not null/none value make an order
        cost = 0
        for p in orders:
            #skip null/none values
            if p[1] is '0' or p[1] is '':
                continue
            quantity = p[1]
            product = Product.objects.get(pk=p[0])
            Has.objects.create(product_id = product, order_id = order_model, quantity = quantity)
            sell = Selling.objects.filter(product_id = product, store_id = store).values_list('price', flat=True)
            for s in sell:
                price = s
            cost += Decimal(price) * Decimal(quantity)

        Orders.objects.filter(pk = order_model.pk).update(cost = cost)
        return redirect(reverse('database:orders'))

class OrdersView(generic.ListView):
        template_name = 'database/client_orders.html'
        model = Orders

        def get(self, request):
            client = request.user
            form = OrdersForm()
            orders = Orders.objects.filter(client = client)
            args = {'orders': orders, 'form': form}
            return render(request, self.template_name, args)


class OrdersSpecsView(generic.ListView):
    template_name = 'database/orders_specs.html'
    model = Has

    def get(self, request, pk):
        order = Orders.objects.get(pk = pk)
        client = request.user
        form = OrderHasForm()
        has = Has.objects.filter(order_id = pk)
        args = {'has': has, 'form': form, 'order': order}
        return render(request, self.template_name, args)
