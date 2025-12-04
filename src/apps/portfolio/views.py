from django.views.generic import TemplateView, DetailView
from django.db.models import Prefetch
from core.models import ArtistProfile
from .models import Category, Artwork, ArtworkImage

class HomeView(TemplateView):
    template_name = "portfolio/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.filter(
            parent__isnull=True
        ).prefetch_related('subcategories')

        context['profile'] = ArtistProfile.objects.first()

        context['latest_artworks'] = Artwork.objects.filter(
            is_visible=True
        ).select_related('category')[:4]
        
        return context


class CategoryDetailView(DetailView):
    model = Category
    template_name = "portfolio/category_detail.html"
    context_object_name = "category"
    slug_url_kwarg = 'slug' 

    def get_queryset(self):
        return Category.objects.prefetch_related(
            Prefetch('artworks', queryset=Artwork.objects.filter(is_visible=True))
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = ArtistProfile.objects.first()
        return context


class ArtworkDetailView(DetailView):
    model = Artwork
    template_name = "portfolio/artwork_detail.html"
    context_object_name = "artwork"
    slug_url_kwarg = 'slug'

    def get_queryset(self):
        return Artwork.objects.filter(is_visible=True).select_related(
            'category'
        ).prefetch_related(
            Prefetch('images', queryset=ArtworkImage.objects.order_by('order'))
        )