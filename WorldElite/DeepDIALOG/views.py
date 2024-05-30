#from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404
from .models import SummitTalk, LeaderTalk

def home(request):
    return render(request, 'home.html')

def summit_talk(request):
    talks = SummitTalk.objects.all()
    return render(request, 'summit_talk.html', {'talks': talks})

def leader_talk(request):
    talks = LeaderTalk.objects.all()
    return render(request, 'leader_talk.html', {'talks': talks})

def about_us(request):
    return render(request, 'about_us.html')

def contact_us(request):
    return render(request, 'contact_us.html')

def summit_detail(request, id):
    talk = get_object_or_404(SummitTalk, id=id)
    return render(request, 'summit_detail.html', {'talk': talk})
