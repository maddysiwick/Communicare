"""
URL configuration for Communicare project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Filter import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',views.triage,name='signup'),
    path('signup/doctor/',views.DocSignupView.as_view(),name='docSignup'),
    path('signup/patient/',views.PatientSignupView.as_view(),name='patientSignup'),
    path('home/',views.home,name='home'),
    path('search/',views.searchCriteria.as_view(),name='searchcriteria'),
    path('search/results/<int:distance>/<specialty>/<female>/<male>/',views.searchResults.as_view(),name='searchresults'),
    path('search/results/<int:pk>/',views.docInfo,name='docinfo'),
    path('whatkindinfo/',views.whatkindinfo,name='whatkindinfo'),
    path('qcinfo/',views.qcinfo,name='qcinfo'),
    path('booking/',views.booking,name='booking')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)