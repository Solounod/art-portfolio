from portfolio.models import Category
from core.models import SocialLink, ArtistProfile

def global_site_context(request):
    return {
        'navbar_categories': Category.objects.filter(parent__isnull=True).prefetch_related('subcategories'),
        'social_links': SocialLink.objects.all(),
        'site_profile': ArtistProfile.objects.first()
    }