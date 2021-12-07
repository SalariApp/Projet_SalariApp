from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Compte.urls')),
    path('entreprise', include('Entreprise.urls')),
    path('employé', include('Employé.urls')),
    path('Dashbord', include('Dashbord.urls'))
]