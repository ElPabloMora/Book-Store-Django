from django.db import models
from django.utils import timezone

#terminar el modelo
class Libro(models.Model):
    
    name = models.CharField(max_length=100)
    author = models.ForeignKey(
        'products.Author',
        on_delete=models.CASCADE,
        related_name='products'
    )
    description = models.TextField(null=True, blank=True)
    
    genero = models.CharField(max_length=50)
    
    image = models.ImageField(blank=True, null=True, upload_to = 'media/products')
    
    price = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)
    
    def __str__(self):
        return f'{self.name} | {self.author}'
    
    
    
class Author(models.Model):
    author =  models.CharField(max_length=200, null=True)
    
    description = models.TextField(null=True, blank=True)
    
    image = models.ImageField(blank=True, null=True, upload_to = 'media/author')
    
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)
    
    def __str__(self):
        return f'{self.author}'


class Comment(models.Model):
    
    product = models.ForeignKey(
        'products.Libro',
        on_delete = models.CASCADE,
        related_name = 'comments'
    )
    author = models.CharField(max_length=200)
    
    text = models.TextField()
    
    created_data = models.DateField(default=timezone.now)
    
    approved_comment = models.BooleanField(default=False)
    
    def approve(self):
        self.approved_comment = True
        self.save()
        
    def __str__(self):
        return self.text