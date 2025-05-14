from django.shortcuts import render, get_object_or_404
from .models import CountryWebsite, HomePageContent


def base(request):
    return render(request, 'base.html')

def country_homepage(request, slug):
    """
    Renders the homepage for a specific country using the slug from CountryWebsite.
    """
    # Get the country website instance
    country = get_object_or_404(CountryWebsite, Slug=slug)

    # Get homepage content associated with the country website
    homepage_content = get_object_or_404(HomePageContent, web_id=country)

    # Context data passed to the template
    context = {
        'country': country,
        'content': homepage_content,
    }

    # Render the homepage template
    return render(request, 'homepage.html', context)

def about_gibf(request):
    return render(request, 'aboutgibf.html') 

def president_message(request):
    return render(request, 'president-message.html')    

def gibf_iso_certificate(request):
    return render(request, 'gibf-iso-certificate.html')    

def legal_documents(request):
    return render(request, 'legal-documents.html')    

def contact_us(request):
    return render(request, 'contact-us.html')    