from django.shortcuts import render

def index(request):
    return render(request, 'aplikasi/index.html')

def coba(request):
    return render(request, 'aplikasi/coba.html')

def mimil(request):
    return render(request, 'aplikasi/mimil.html')

def index1(request):
    return render(request, 'aplikasi/index1.html')


