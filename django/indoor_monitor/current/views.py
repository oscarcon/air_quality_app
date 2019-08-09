from django.shortcuts import render

# Create your views here.
def current_data(request):
    return render(request, 'current/current_data.html')