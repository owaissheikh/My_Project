from django.http import HttpResponse
from django.template import loader,context
from django.shortcuts import render
from MyStock.models import Categories
from MyStock.models import SubCategories
from MyStock.models import Manufacturer
from MyStock.models import Invoice
def getcategory(request):
    if 'txtname' in request.GET:
        message= request.GET['txtname']
        message1= int(request.GET['txtcatid'])
        cat=Categories(category_id=int(message1),category_name=str(message),Description='Test')
        cat.save()
        rs=Categories.objects.all();
    else:
        message='You submitted an empty form.'
    
    return render(request,'html/Category1.html',{'query': message, 'query1': message1,'Resultset': rs},context)
	

def getsubcategory(request):
    if 'txtname' in request.GET:
        message= request.GET['txtname']
        message1= int(request.GET['txtcatid'])
        cat=SubCategories(Subcategory_id=int(message1),Subcategory_name=str(message),Description='Test')
        cat.save()
        rs=SubCategories.objects.all();
    else:
        message='You submitted an empty form.'
    
    return render(request,'html/Subcategory1.html',{'query': message, 'query1': message1,'Resultset': rs},context)
	

def getmanufacturer(request):
    if 'txtname' in request.GET:
        message= request.GET['txtname']
        message1= int(request.GET['txtcatid'])
        cat=Manufacturer(Manufacturer_id=int(message1),Manufacturer_name=str(message),Description='Test')
        cat.save()
        rs=Manufacturer.objects.all();
    else:
        message='You submitted an empty form.'
    
    return render(request,'html/Manufacturer1.html',{'query': message, 'query1': message1, 'Resultset': rs},context)

def getinvoice(request):
    if 'iid' in request.GET:
        message1= int(request.GET['iid'])
        message2= int(request.GET['pid'])
        message3= request.GET['pname']
        message4= int(request.GET['mno'])
        message5= request.GET['colour']
        message6= request.GET['size']
        message7= request.GET['price']
        message8= int(request.GET['quantity'])
        message9= request.GET['cname']
        message10= request.GET['email']
        message11= int(request.GET['mono'])
        message12= request.GET['add']
        cat=	Invoice(Invoice_id=int(message1),Product_id=int(message2),Product_name=str(message3),Model_no=int(message4),Colour=str(message5),Size=str(message6),Price=str(message7),Quantity=int(message8),Customer_name=str(message9),Email_id=str(message10),Mobile_no=int(message11),Address=str(message12),Discription='Test')
        cat.save()
        rs=Invoice.objects.all();
    else:
        message='You submitted an empty form.'
    
    return render(request,'html/invoice1.html',{ 'Resultset': rs},context)
	
	

def index(request):
    context=locals()
    return render(request, 'html/index.html',{},context)

def category2(request):
    context=locals()
    return render(request, 'html/category2.html' ,{}, context)

def subcategory2(request):
    context=locals()
    return render(request, 'html/subcategory2.html' ,{}, context)

def Product2(request):
    context=locals()
    return render(request, 'html/Product2.html' ,{}, context)


def Manufacturer2(request):
    context=locals()
    return render(request, 'html/Manufacturer2.html' ,{}, context)

def customer2(request):
    context=locals()
    return render(request, 'html/customer2.html' ,{}, context)

def invoice2(request):
    context=locals()
    return render(request, 'html/invoice2.html' ,{}, context)

def Category1(request):
    context=locals()
    return render(request, 'html/Category1.html' ,{}, context)

def Subcategory1(request):
    context=locals()
    return render(request, 'html/Subcategory1.html' ,{}, context)

def Product1(request):
    context=locals()
    return render(request, 'html/Product1.html' ,{}, context)


def Manufacturer1(request):
    context=locals()
    return render(request, 'html/Manufacturer1.html' ,{}, context)

def Customer1(request):
    context=locals()
    return render(request, 'html/Customer1.html' ,{}, context)

def invoice1(request):
    context=locals()
    return render(request, 'html/invoice1.html' ,{}, context)



