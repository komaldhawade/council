from django.db import models

# Create your models here.

# Define max image size
MAX_IMAGE_SIZE_MB = 2  # Maximum file size in MB

# Define dimensions for different image types
HOMEPAGE_IMAGE_DIMENSIONS = (1513, 413)  # BusinessMagazine images

class CountryWebsite(models.Model):
    """Country Website"""
    WebId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    Title = models.CharField(max_length=255)
    Slug = models.SlugField(max_length=255, unique=True)
    MetaDescription = models.CharField(max_length=160, null=True, blank=True)
    MetaKeywords = models.CharField(max_length=255, null=True, blank=True)
    UploadedAt = models.DateTimeField(auto_now_add=True)
    WebsiteUrl = models.URLField(help_text="Council website url")
    def __str__(self):
        return f"{self.name} ({self.country})"


class HomePageContent(models.Model):
    homepage_id = models.AutoField(primary_key=True)
    web_id = models.ForeignKey('CountryWebsite', on_delete=models.CASCADE, db_column='web_id')
    HomepageTitle = models.CharField(max_length=255, blank=True, null=True)
    HomeSlug = models.SlugField(unique=True)
    MetaDescription = models.TextField(blank=True, null=True)
    MetaKeyword = models.CharField(max_length=255, blank=True, null=True)

    HomeBannerImg = models.ImageField(
        upload_to="home_banners/", blank=True, null=True
    )
    HomeImgBannerFileName = models.CharField(
        max_length=255, blank=True, null=True
    )
    HomeBannerImgAltTag = models.CharField(max_length=255, blank=True, null=True)

    LogoImg = models.ImageField(upload_to="logo_images/", blank=True, null=True)
    LogoImgFileName = models.CharField(max_length=255, blank=True, null=True)
    LogoImgAltTag = models.CharField(max_length=255, blank=True, null=True)

    AboutTitle = models.CharField(max_length=255)
    AboutDescription = models.TextField(blank=True, null=True)
    AboutImg = models.ImageField(upload_to="about_images/", blank=True, null=True)
    AboutImgFileName = models.CharField(max_length=255, blank=True, null=True)
    AboutImgAltTag = models.CharField(max_length=255, blank=True, null=True)

    ObjectiveTitle = models.CharField(max_length=255)
    ObjectiveDescription = models.TextField(blank=True, null=True)

    GalleryVideoTitle = models.CharField(max_length=255)
    GalleryImg = models.ImageField(upload_to="gallery_images/", blank=True, null=True)
    GalleryVideoURL = models.URLField(blank=True, null=True) # add youtube video link
    GalleryImgFileName = models.CharField(max_length=255, blank=True, null=True)
    GalleryImgAltTag = models.CharField(max_length=255, blank=True, null=True)

    CountryGlancesTitle = models.CharField(max_length=255)

    OfficialNameTitle = models.CharField(max_length=255)
    OfficialNameParagraph = models.TextField(blank=True, null=True)

    CapitalCityTitle = models.CharField(max_length=255)
    CapitalCityParagraph = models.TextField(blank=True, null=True)

    LocationTitle = models.CharField(max_length=255)
    LocationParagraph = models.TextField(blank=True, null=True)

    AreaTitle = models.CharField(max_length=255)
    AreaParagraph = models.TextField(blank=True, null=True)

    PopulationTitle = models.CharField(max_length=255)
    PopulationParagraph = models.TextField(blank=True, null=True)

    LanguageTitle = models.CharField(max_length=255)
    LanguageParagraph = models.TextField(blank=True, null=True)

    ExportsTitle = models.CharField(max_length=255)
    ExportsParagraph = models.TextField(blank=True, null=True)

    ImportTitle = models.CharField(max_length=255)
    ImportParagraph = models.TextField(blank=True, null=True)

    CurrencyTitle = models.CharField(max_length=255)
    CurrencyParagraph = models.TextField(blank=True, null=True)

    CountryCodeTitle = models.CharField(max_length=255)
    CountryCodeParagraph = models.TextField(blank=True, null=True)

    TimeZoneTitle = models.CharField(max_length=255)
    TimeZoneParagraph = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.HomepageTitle} ({self.web_id})"

class AboutCountry(models.Model):
    aboutcountry_id = models.AutoField(primary_key=True)
    web_id = models.ForeignKey('CountryWebsite', on_delete=models.CASCADE, db_column='web_id')
    aboutcountryTitle = models.CharField(max_length=255, blank=True, null=True)
    aboutcountrySlug = models.SlugField(unique=True)
    MetaDescription = models.TextField(blank=True, null=True)
    MetaKeyword = models.CharField(max_length=255, blank=True, null=True)

    aboutcountryImg = models.ImageField(
        upload_to="about_banners/", blank=True, null=True
    )
    aboutcountryImgBannerFileName = models.CharField(
        max_length=255, blank=True, null=True
    )
    aboutcountryBannerImgAltTag = models.CharField(max_length=255, blank=True, null=True)

    AboutDescription = models.TextField(blank=True, null=True)

    # culture section
    H_TYPE_CHOICES = [
        ("h1", "H1"),
        ("h2", "H2"),
        ("h3", "H3"),
        ("h4", "H4"),
        ("h5", "H5"),
        ("h6", "H6"),
    ]
    h_type = models.CharField(
        max_length=2, choices=H_TYPE_CHOICES, blank=True, null=True
    )
    h_title = models.CharField(max_length=255, blank=True, null=True)
    h_position = models.CharField(
        max_length=10,
        blank=True,
        null=True,
        default="center",
    )
    is_h_ruler = models.BooleanField(default=False)

    p_content = models.TextField(blank=True, null=True)
    li_content = models.TextField(blank=True, null=True)

    section_img = models.ImageField(upload_to="section_images/", blank=True, null=True)
    section_img_file_name = models.CharField(max_length=255, blank=True, null=True)
    section_img_alt_tag = models.CharField(max_length=255, blank=True, null=True)
    section_img_position = models.CharField(
        max_length=50, blank=True, null=True, default="center"
    )

    is_hr = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def save(self, *args, **kwargs):
        if not self.h_position:
            self.h_position = "center"  # fallback if not manually selected
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.article.article_title} - {self.h_title or 'Section'}"



class BusinessOpportunities(models.Model):
    businessopportunities_id = models.AutoField(primary_key=True)
    web_id = models.ForeignKey(CountryWebsite, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50)  # Optional if using FontAwesome icons

class BusinessAndMedia(models.Model):
    businessandmedia_id = models.AutoField(primary_key=True)
    web_id = models.ForeignKey(CountryWebsite, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=100)
    feedback = models.TextField()
    rating = models.IntegerField()
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
