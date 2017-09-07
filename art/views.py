from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from whois import whois
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
def data(request):
    r=request.GET.get('d',"")
    print(r)
    if r:
        if r.startswith("http") and r.endswith(".com") or r.endswith(".edu") or r.endswith(".net"):
            try:
                data_list=whois(r)
                if data_list.domain:
                    context={'data_list':data_list}
                    return render(request,'/art/data.html',context)
                else:
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            except:
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))





def shaka(request):
    template=loader.get_template('art/data.html')
    return HttpResponse(template.render())
