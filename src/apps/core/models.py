from django.db import models

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        abstract = True

class ArtistProfile(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre Artístico")
    bio = models.TextField(verbose_name="Biografía / Sobre mí") 
    photo = models.ImageField(upload_to='profile/', verbose_name="Foto de perfil", blank=True, null=True)
    contact_email = models.EmailField(verbose_name="Email de contacto", blank=True)

    class Meta:
        verbose_name = "Perfil del Artista"
        verbose_name_plural = "Perfil del Artista"

    def __str__(self):
        return self.name


class SocialLink(models.Model):
  
    PLATFORM_CHOICES = (
        ('instagram', 'Instagram'),
        ('facebook', 'Facebook'),
        ('twitter', 'Twitter/X'),
        ('linkedin', 'LinkedIn'),
        ('whatsapp', 'WhatsApp'),
        ('other', 'Otro'),
    )
    
    name = models.CharField(max_length=50, verbose_name="Nombre (ej: Instagram)")
    url = models.URLField(verbose_name="Enlace URL")
    icon_class = models.CharField(
        max_length=50, 
        blank=True, 
        help_text="Clase de icono (ej: bi bi-instagram o fa-brands fa-instagram)"
    )
    
    order = models.PositiveIntegerField(default=0, verbose_name="Orden")

    class Meta:
        verbose_name = "Red Social"
        verbose_name_plural = "Redes Sociales"
        ordering = ['order']

    def __str__(self):
        return self.name