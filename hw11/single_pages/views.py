from django.shortcuts import render

def landing(request):
    return render(
        request,
        'single_pages/landing.html'
    )

def index(request):
    return render(
        request,
        'single_pages/index.html'
    )

def layout(request):
    return render(
        request,
        'single_pages/layout.html'
    )

def isy(request):
    return render(
        request,
        'single_pages/isy.html'
    )

def kjh(request):
    return render(
        request,
        'single_pages/kjh.html'
    )

def project(request):
    return render(
        request,
        'single_pages/project.html'
    )

