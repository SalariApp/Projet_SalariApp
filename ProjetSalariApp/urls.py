from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Compte.urls')),
    path('dash', include('Dashbord.urls')),
    path('entreprise', include('Entreprise.urls')),
    path('employé', include('Employé.urls'))
]