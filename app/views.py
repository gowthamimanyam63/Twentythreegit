from django.shortcuts import render

# Create your views here.
def staticmdb(request):
    return render(request,'staticmdb.html')