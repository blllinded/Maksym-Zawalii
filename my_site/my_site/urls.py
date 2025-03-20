from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponse

def home(request):
    return HttpResponse("The home page is working!")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home),  
    path("__debug__/", include("debug_toolbar.urls")),  
]



