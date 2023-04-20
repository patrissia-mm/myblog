#python
from datetime import timedelta, datetime
#django
from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify
from django.urls import reverse_lazy
#aplicaciones de terceros
from model_utils.models import TimeStampedModel
from ckeditor_uploader.fields import RichTextUploadingField

from .managers import EntryManager

class Category(TimeStampedModel):
    """ Categorías de una entrada """
    short_name = models.CharField(
        'Nombre Corto',
        max_length= 15,
        unique=True
    )
    name = models.CharField(
        'Name',
        max_length=30
    )

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.name
    
class Tag(TimeStampedModel):
    """Etiquetas de un artículo"""
    name = models.CharField(
        'Nombre',
        max_length=30
    )

    class Meta:
        verbose_name = 'Etiqueta'
        verbose_name_plural = 'Tags'
    
    def __str__(self):
        return self.name
    
class Entry(TimeStampedModel):
    """ Entradas al blog """
    user = models.ForeignKey(
        #se usa la variable configurada en el settings  para administrar todos los uauarios de django
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    tag = models.ManyToManyField(Tag)
    title = models.CharField(
        'Título',
        max_length=200
    )
    resume = models.TextField()
    content = RichTextUploadingField('contenido')
    public = models.BooleanField(default=False)
    image=models.ImageField(
        'Imagen',
        upload_to='Entry',
    )
    portada = models.BooleanField(default=False)
    in_home = models.BooleanField(default=False)
    slug = models.SlugField(editable=False, max_length=300)

    objects = EntryManager()

    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy(
            'entrada_app:entry-detail', 
            kwargs = {
                'slug': self.slug
            }
        )
    
    def save(self, *args, **kwargs):
        #calculamos el total de segundos de la hora actual
        now = datetime.now()
        total_time = timedelta(
            hours=now.hour,
            minutes=now.minute,
            seconds=now.second
        )
        seconds = int(total_time.total_seconds())
        slug_unique = '%s %s' % (self.title, str(seconds))
        self.slug = slugify(slug_unique)
        super(Entry, self).save(*args, **kwargs)




    

