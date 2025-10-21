# Create your views here.
from django.shortcuts import render, redirect
from .models import GalleryImage
from .forms import LeadForm

def home(request):
    images = GalleryImage.objects.all()
    return render(request, "main/home.html", {"images": images})

def about(request):
    return render(request, "main/about.html")

def services(request):
    return render(request, "main/services.html")

def contact(request):
    if request.method == "POST":
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("success")
    else:
        form = LeadForm()
    return render(request, "main/contact.html", {"form": form})

def success(request):
    return render(request, "main/success.html")
