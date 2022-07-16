from django.shortcuts import render
from invoices.models import Invoice
from django.http import HttpResponse

def hello_world(request):
    obj = Invoice.objects.get(id=1)
    # print(obj.get_tags())
    qs = Invoice.objects.all()
    # print(obj.get_positions())
    # print(obj.get_total_amount())
    print(qs.__dict__)
    
    # context = {
        
    # }
    
    # return render(request, "template_name", context)
    return HttpResponse(str(obj.number))