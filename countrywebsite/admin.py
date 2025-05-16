from django.contrib import admin

from .models import CountryWebsite, HomePageContent, AboutCountry, BusinessOpportunities, BusinessAndMedia

admin.site.register(CountryWebsite)
admin.site.register(HomePageContent)
admin.site.register(AboutCountry)
admin.site.register(BusinessOpportunities)
admin.site.register(BusinessAndMedia)
