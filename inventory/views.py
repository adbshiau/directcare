from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "inventory/index.html")

def staff(request):
    return render(request, "inventory/staff.html")

def item(request):
    return render(request, "inventory/item.html")

def requisition(request):
    return render(request, "inventory/requisition.html")