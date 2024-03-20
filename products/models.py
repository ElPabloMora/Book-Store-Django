from django.db import models
from django.utils import timezone

#terminar el modelo
class Libro(models.Model):
    
    name = models.CharField(max_length=50)
    author = models.ForeignKey(
        'products.Author',
        on_delete=models.CASCADE,
        related_name='products'
    )
    description = models.CharField(max_length=2000)
    genero = models.ForeignKey(
        'products.Genero',
        on_delete = models.CASCADE,
        related_name='products'
    )
    image = models.ImageField(blank=True, null=True, upload_to = 'media/products')
    
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)
    
    def __str__(self):
        return f'{self.name} | {self.author}'