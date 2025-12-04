from django.contrib import admin
from .models import ArtistProfile, SocialLink

@admin.register(ArtistProfile)
class ArtistProfileAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if ArtistProfile.objects.exists():
            return False
        return True

@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'order')
    list_editable = ('order',)