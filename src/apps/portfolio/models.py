# src/apps/portfolio/models.py
from django.db import models
from django.utils.text import slugify
from core.models import TimeStampedModel 

class Category(TimeStampedModel):
    parent = models.ForeignKey(
        'self', 
        null=True, 
        blank=True, 
        on_delete=models.SET_NULL,
        related_name='subcategories',
        verbose_name='Categoría Padre'
    )
    name = models.CharField(max_length=100, verbose_name='Nombre')
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    description = models.TextField(blank=True, verbose_name='Descripción de la categoría')
    cover_image = models.ImageField(upload_to='categories/', blank=True, null=True, verbose_name='Portada')

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        full_path = [self.name]
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return ' > '.join(full_path[::-1])


class Artwork(TimeStampedModel):
    category = models.ForeignKey(
        Category, 
        on_delete=models.PROTECT,
        related_name='artworks',
        verbose_name='Categoría'
    )
    title = models.CharField(max_length=200, verbose_name='Título de la obra')
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    
    technique = models.CharField(max_length=200, verbose_name='Técnica/Materiales', help_text="Ej: Óleo sobre lienzo, Bronce fundido")
    dimensions = models.CharField(max_length=100, verbose_name='Dimensiones', blank=True, help_text="Ej: 120x80 cm")
    year = models.PositiveIntegerField(verbose_name='Año de realización', default=2024)
    
    description = models.TextField(verbose_name='Historia / Descripción', blank=True)
    
    cover_image = models.ImageField(upload_to='artworks/covers/', verbose_name='Imagen de Portada')
    
    is_visible = models.BooleanField(default=True, verbose_name='Visible en la web')

    class Meta:
        verbose_name = 'Obra'
        verbose_name_plural = 'Obras'
        ordering = ['-year', '-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.year})"


class ArtworkImage(models.Model):
    artwork = models.ForeignKey(
        Artwork, 
        on_delete=models.CASCADE, 
        related_name='images',
        verbose_name='Obra'
    )
    image = models.ImageField(upload_to='artworks/gallery/', verbose_name='Imagen')
    caption = models.CharField(max_length=200, blank=True, verbose_name='Pie de foto', help_text="Ej: Vista lateral, Detalle de textura")
    
    order = models.PositiveIntegerField(default=0, verbose_name='Orden')

    class Meta:
        verbose_name = 'Imagen de Galería'
        verbose_name_plural = 'Imágenes de Galería'
        ordering = ['order']

    def __str__(self):
        return f"Img: {self.artwork.title} - {self.caption or 'Sin título'}"