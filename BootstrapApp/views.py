from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')

def booking(request):
    return render(request, 'booking.html')

def team(request):
    return render(request, 'team.html')

def testimonial(request):
    return render(request, 'testimonial.html')

def page_not_found(request):
    return render(request, '404.html')

def contact(request):
    return render(request, 'contact.html')
