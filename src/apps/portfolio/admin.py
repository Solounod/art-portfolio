from django.contrib import admin
from .models import Category, Artwork, ArtworkImage

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'slug')
    prepopulated_fields = {'slug': ('name',)} 
    search_fields = ('name',)

class ArtworkImageInline(admin.TabularInline):
    model = ArtworkImage
    extra = 1 
    fields = ('image', 'caption', 'order')

class ArtworkAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'year', 'is_visible')
    list_filter = ('category', 'is_visible', 'year')
    search_fields = ('title', 'description', 'technique')
    prepopulated_fields = {'slug': ('title',)}
    
   
    inlines = [ArtworkImageInline]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Artwork, ArtworkAdmin)
