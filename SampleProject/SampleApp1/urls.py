from django.urls import path
from SampleApp1 import views

urlpatterns=[
	path('one/',views.f11),
	path('two/',views.f22),
    
   # re_path("^.*$",views.homepage),
]