# appname/views.py
from django.shortcuts import render
from django.http import HttpResponse
from django.template.defaultfilters import title
from django.utils.termcolors import RESET

from .models import *
from . import gemini
import markdown

def home(request):
    if request.method == 'POST':
        response = gemini.chat_session.send_message(request.POST['input']).text
        md = markdown.Markdown()
        response = md.convert(response)

        form = Statement()
        reset_button = Reset()
        return render(request, 'home.html', {'form': form, 'response': response})
    else:
        form = Statement()
        return render(request, 'home.html', {'form': form, 'title': 'Enter data', 'response': 'Enter some basic data to begin:'})

def about(request):
    return HttpResponse("This is the about page")

# def statement(request):
#     form = Statement()
#     return render(request, 'home.html', {'form': form})