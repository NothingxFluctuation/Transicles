from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^about/$',views.about,name='about'),
    url(r'^contact/$',views.contact,name='contact'),
    url(r'^newsletter/$',views.newsletter,name='newsletter'),
    url(r'^privacy/$',views.privacy,name='privacy'),
    url(r'^search/$',views.search,name='search'),
    url(r'^terms/$',views.terms, name='terms'),
    url(r'^data/$',views.data, name='data'),
    url(r'^shaka/$',views.shaka,name='shaka'),
	
]
