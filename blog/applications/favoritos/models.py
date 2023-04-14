from django.db import models
from django.conf import settings
#aplicaciones de terceros
from model_utils.models import TimeStampedModel
from applications.entrada.models import Entry
from .managers import FavoritesManager

class Favorites(TimeStampedModel):
    """Modelo de favoritos"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='user_favorites',
        on_delete=models.CASCADE,
    )

    entry = models.ForeignKey(
        Entry,
        related_name='entry_favorites',
        on_delete=models.CASCADE
    )

    objects = FavoritesManager()
    
    class Meta:
        #para que no se repitan una entrada y un usuario en favoritos
        unique_together = ('user', 'entry')
        verbose_name = 'Entrada Favorita'
        verbose_name_plural = 'Entradas Favoritas'

    def __str__(self):
        return self.entry.title
