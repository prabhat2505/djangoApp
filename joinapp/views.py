from django.shortcuts import render
from django.http import HttpResponse
from .models import Course , Author
from django.db.models import Q

# Create your views here.
def showauthor(request):    
    #Author(name='virendra').save()
    #Authors = Author.objects.all()
   # Course(name='node',author=Authors[0]).save()

   ###########################################
   # child table
    # courses = Course.objects.select_related()
    # #courses = Course.objects.all()
    # for course in courses:
    #     #course.author
    #     return HttpResponse(course.author.id)
    # return HttpResponse(courses[0])
    #########################################

    ##############################################
    courses = Course.objects.select_related('author').values('author__name','name')
    return HttpResponse(courses.query)
    #########################################

   ###########################################
   # parent table
    # courses = Author.objects.prefetch_related()
    
    # return HttpResponse(courses.query)
    #########################################

    #return HttpResponse(Authors.values())
    # return HttpResponse('hi')
    context = {
        'customers':customers
    }
    return render(request,"customer.html",context)

# Create your views here.
def showcourse(request):
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