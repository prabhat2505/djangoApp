from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer
from django.db.models import Q

# Create your views here.
def home(request):
    return render(request,"home.html",{})

def showcustomer(request):
    #customers = Customer.objects.all() 
    #customers = Customer.objects.filter(city__contains="NYC") | Customer.objects.filter(city__contains="Lyon")
    #customers = Customer.objects.filter(city__contains="Lyon", id="146" )
    #customers = Customer.objects.filter(city__contains="Lyon").values('customerName')
    customers = Customer.objects.filter(city__contains="Lyon").values_list('customerName',flat=True)
    #customers = Customer.objects.filter(Q(city__contains="NYC")|Q(city__contains="Lyon"))
    #customers = Customer.objects.get(id='141') 
    #customers = Customer.objects.filter(id='141') | Customer.objects.filter(id='124')
    #CustomersCnt = Customers.objects.count()
    #customers = Customer.objects.filter(city='NYC').count()
    #customers = Customer.objects.filter(city__contains='NYC').count()
    #customers = Customer.objects.all()[:5]
    #customers = Customer.objects.annotate(num_books=Count('id'))
    # customers = Customer.objects.annotate(Count('id'))
    #customers = Customer.objects.values_list('id', 'eename')
   # return HttpResponse(customers[0].ename)
    #return render(request,"show.html",{'customers':customers}) 
    #return HttpResponse(customers)
    context = {
        'customers':customers
    }
    return render(request,"customer.html",context)

    for customer in customers:
        return HttpResponse(customer.customerName)
        # print(customer.customerName)


    #customers = Customer.objects.order_by('-creditLimit')[1]
    # print(customers.query)
    # return HttpResponse(customers.customerName)
    return HttpResponse(customers.query)


    