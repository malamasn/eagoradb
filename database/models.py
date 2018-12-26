from django.db import models


class Store(models.Model):
    id = models.PositiveSmallIntegerField(primary_key = True)
    name = models.CharField(max_length = 20)
    type = models.CharField(max_length = 20, null = True, blank = True)
    phone = models.PositiveSmallIntegerField(null = True, blank = True)
    email = models.EmailField(max_length = 35, null = True, blank = True)
    street = models.CharField(max_length = 35, null = True, blank= True)
    city = models.CharField(max_length = 20, null = True, blank= True)
    zip = models.PositiveSmallIntegerField(null = True, blank= True)
    storeManager = models.CharField(max_length = 20)

class Supplier(models.Model):
    name = models.CharField(max_length = 20, primary_key = True)
    phone = models.PositiveSmallIntegerField(null = True, blank = True)
    street = models.CharField(max_length = 35, null = True, blank = True)
    city = models.CharField(max_length = 20, null = True, blank = True)
    zip = models.PositiveSmallIntegerField(null = True, blank = True)

class Product(models.Model):
    id = models.PositiveSmallIntegerField(primary_key = True)
    name = models.CharField(max_length = 20)
    type = models.CharField(max_length = 20)
    supplier = models.ForeignKey(Supplier, on_delete = models.CASCADE, null = True, blank = True)
    sells = models.ManyToManyField(Store, through='Selling')

class Selling(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    store_id = models.ForeignKey(Store, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits = 7, decimal_places = 2)
    discount = models.PositiveSmallIntegerField(null = True, blank = True)
    start_date = models.DateField(null = True, blank = True)
    finish_date = models.DateField(null = True, blank = True)



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
    cost = models.DecimalField(max_digits = 7, decimal_places = 2)

class Has(models.Model):
    product_id = models.ForeignKey(Product, on_delete = models.CASCADE)
    order_id = models.ForeignKey(Orders, on_delete = models.CASCADE)
    quantity = models.DecimalField(max_digits = 7, decimal_places = 3)
