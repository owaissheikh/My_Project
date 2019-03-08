from django.db import models
from django.utils import timezone

class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Categories(models.Model):
    category_id= models.IntegerField(default=0)
    category_name = models.CharField(max_length=200)
    Description= models.CharField(max_length=200)
	
class SubCategories(models.Model):
    Subcategory_id= models.IntegerField(default=0)
    Subcategory_name = models.CharField(max_length=200)
    Description= models.CharField(max_length=200)


class Product(models.Model):
    Product_id= models.IntegerField(default=0)
    Product_name = models.CharField(max_length=200)
    Description= models.CharField(max_length=200)
    category_id= models.IntegerField(default=0)
    Subcategory_id= models.IntegerField(default=0)
    Manufacturer_id= models.IntegerField(default=0)
    Dimension= models.IntegerField(default=0)
    Model_no= models.IntegerField(default=0)
    Price= models.CharField(max_length=200)
    Quantity= models.IntegerField(default=0)
    Quantity_Max= models.IntegerField(default=0)
    Quantity_Min=models.IntegerField(default=0)
    Length= models.IntegerField(default=0)
    Width= models.IntegerField(default=0)
    Height= models.IntegerField(default=0)
    Sort_order= models.IntegerField(default=0)
    Colour= models.CharField(max_length=200)
    Size= models.CharField(max_length=200)
    Package= models.CharField(max_length=200)
    Entry_date = models.DateTimeField('date published')

class Manufacturer(models.Model):
    Manufacturer_id= models.IntegerField(default=0)
    Manufacturer_name = models.CharField(max_length=200)
    Description= models.CharField(max_length=200)
   


class Customer(models.Model):
    Customer_id= models.IntegerField(default=0)
    First_name = models.CharField(max_length=200)
    Last_name = models.CharField(max_length=200)
    Email_id= models.CharField(max_length=200)
    Password= models.CharField(max_length=200)
    Confirm_password= models.CharField(max_length=200)
    Mobile_no= models.IntegerField(default=0)
    Address= models.CharField(max_length=200)
    Entry_date = models.DateTimeField('date published')



class Invoice(models.Model):
    Invoice_id= models.IntegerField(default=0)
    Product_id= models.IntegerField(default=0)
    Product_name = models.CharField(max_length=200)
    Model_no= models.IntegerField(default=0)
    Colour= models.CharField(max_length=200)
    Size= models.CharField(max_length=200)
    Price= models.CharField(max_length=200)
    Quantity= models.IntegerField(default=0)
    Discription= models.CharField(max_length=200)
    Customer_name = models.CharField(max_length=200)
    Email_id= models.CharField(max_length=200)
    Mobile_no= models.IntegerField(default=0)
    Address= models.CharField(max_length=200)

        
