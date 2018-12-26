from django.db import models


class Store(models.Model):
    id = models.PositiveSmallIntegerField(primary_key = True)
    name = models.CharField(max_length = 20)
    type = models.CharField(max_length = 20, null = True, blank = True)
    phone = models.PositiveSmallIntegerField(max_length = 10, null = True, blank = True)
    email = models.EmailField(max_length = 35, null = True, blank = True)
    street = models.CharField(max_length = 35)
    city = models.CharField(max_length = 20)
    zip = models.PositiveSmallIntegerField(max_length = 5)
    storeManager = models.CharField(max_length = 20)


class Product(models.Model):
    id = models.PositiveSmallIntegerField(primary_key = True)
    name = models.CharField(max_length = 20)
    type = models.CharField(max_length = 20)
    supplier = models.ForeignKey(Supplier, on_delete = models.CASCADE, null = True, blank = True)
    sells = models.ManyToManyField(Store, through='Selling')

class Selling(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    store_id = models.ForeignKey(Store, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places = 2)
    discount = models.PositiveSmallIntegerField(max_length = 3, null = True, blank = True)
    start_date = models.DateField(null = True, blank = True)
    finish_date = models.DateField(null = True, blank = True)



class Supplier(models.Model):
    name = models.CharField(max_length = 20, primary_key = True)
    phone = models.PositiveSmallIntegerField(max_length = 10, null = True, blank = True)
    street = models.CharField(max_length = 35, null = True, blank = True)
    city = models.CharField(max_length = 20, null = True, blank = True)
    zip = models.PositiveSmallIntegerField(max_length = 5, null = True, blank = True)


class Orders(models.Model):
    id = models.PositiveSmallIntegerField(primary_key = True)
    store_id = models.ForeignKey(Store, on_delete = models.CASCADE)
    product_id = models.ManyToManyField(Product, through = 'Has')
    client = models.CharField(max_length = 20)
    STATUSES = (
        ('0', 'Packing'),
        ('1', 'Delivering'),
        ('2', 'Delivered')
    )
    status = models.CharField(max_length = 1, choices = STATUSES, default = None, blank = True, null = True)
    cost = models.DecimalField(decimal_places = 2)

class Has(models.Model):
    product_id = models.ForeignKey(Product)
    order_id = models.ForeignKey(Orders)
    quantity = models.DecimalField(decimal_places = 3)
