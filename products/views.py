from django.shortcuts import render, redirect
from .models import Libro, Author, Comment
from .forms import CommentsForm

def index(request):
    #logica

    #Aqui llamamos a todos los productos
    products = Libro.objects.all()
    authors = Author.objects.all()
    
    return render( request,'products/list_of_products.html', {'products': products, 'authors': authors})


def show_author(request, id ):
    
    product = Libro.objects.get(id=id)
    
    return render(request, 'products/show_author.html', {'product':product})



def show_product(request, id):
    
    product = Libro.objects.get(id=id)
    
    comments = Comment.objects.filter(product=id)
    
    form = CommentsForm()
    
    return render(request, 'products/show_product.html',
                  {'product':product, 
                   'comments':comments, 
                   'form':form})
    


def add_new_comment(request, id):
    
    if request.method == 'POST':
        
        form = CommentsForm(request.POST)
        
        if form.is_valid:
            user = request.user
            product = Libro.objects.get(id=id)
            new_comment = form.save(commit=False)
            new_comment.author = user
            new_comment.product = product
            
            new_comment.save()
        return redirect('show_product',id)
    
    return redirect('show_product',id)
