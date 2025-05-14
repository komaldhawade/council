from django.contrib import admin
from django.urls import path
from countrywebsite import views  # adjust as needed

urlpatterns = [
    path('admin/', admin.site.urls),  # Place this first
    path('/', views.base),  # Place this first
    path('about-gibf/', views.about_gibf, name='about_gibf'),
    path('president-message/', views.president_message, name='president_message'),
    path('gibf-iso-certificate/', views.gibf_iso_certificate, name='gibf_iso_certificate'),
    path('legal-documents/', views.legal_documents, name='legal_documents'),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('<slug:slug>/', views.country_homepage, name='country_homepage'),  # Catch-all comes later

]