from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
# Create your views here.
def index(request):
    template=loader.get_template('art/index.html')
    return HttpResponse(template.render())
def about(request):
    template=loader.get_template('art/about.html')
    return HttpResponse(template.render())
def contact(request):
    template=loader.get_template('art/contact.html')
    return HttpResponse(template.render())
def newsletter(request):
    template=loader.get_template('art/newsletter.html')
    return HttpResponse(template.render())
def privacy(request):
    template=loader.get_template('art/privacy.html')
    return HttpResponse(template.render())
def search(requst):
    template=loader.get_template('art/search.html')
    return HttpResponse(template.render())
def terms(request):
    template=loader.get_template('art/terms.html')
    return HttpResponse(template.render())
