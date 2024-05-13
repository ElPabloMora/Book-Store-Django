from django.shortcuts import get_object_or_404, render, redirect
from .models import Libro, Author, Comment, Carrito
from .forms import CommentsForm
from django.core.paginator import Paginator

def index(request):
    #logica

    #Aqui llamamos a todos los productos
    products = Libro.objects.all().order_by('-id')[:8]
    authors = Author.objects.all().order_by('-id')[:8]
    

    
        
    return render( request,'products/list_of_products.html', {'products': products, 'authors': authors})


def special_most_sale(request):
    
    products = Libro.objects.order_by('-count_sale')[:24]
    
    paginator_products = Paginator(products,12)
    
    page_number = request.GET.get("page")
    
    page_obj_prod = paginator_products.get_page(page_number)
    
    return render(request, 'special/special.html', {'products' : page_obj_prod} )


def special_author_page(request, author):
    author = get_object_or_404(Author, author=author)
    
    product = Libro.objects.filter(author=author)
    
    
    paginator_products = Paginator(product,12)
    
    page_number =request.GET.get("page")
    
    page_obj_prod = paginator_products.get_page(page_number)
    
    return render(request, 'special/author_page.html', {'products': page_obj_prod})


def special_price(request):
    
    #Con este __isnull=False le estamos diciendo al filtro que me traiga los datos que en el apartado de special_price no sea nulo.
    product = Libro.objects.filter(special_price__isnull=False)
    
    paginator_products = Paginator(product, 12)
    
    page_number = request.GET.get("page")
    
    page_obj_prod = paginator_products.get_page(page_number)
    
    return render(request, 'special/special_price.html', {'products':page_obj_prod})
    
    
    

def show_genero(request, Genero):

    
    products = Libro.objects.filter(genero=Genero)
    #Concretamente tuve que utilizar author__in para poder filtrar los autores de los libros filtrados por genero
    authors = Author.objects.filter(author__in=products)
    
    #paginator
    
    paginator_products = Paginator(products, 12)
    
    paginator_authors = Paginator(authors, 12)
    
    page_number = request.GET.get("page")    
    
    page_obj_prod = paginator_products.get_page(page_number)
    
    page_obj_author = paginator_authors.get_page(page_number)
    

    return render( request,'generos/genero.html', {'genero':Genero,'products': page_obj_prod, 'authors': page_obj_author})



    


def pay_shoppingCard(request):
    
    carritos = Carrito.objects.filter(usuario=request.user)
 
    
    
    for carrito in carritos:
        product = carrito.producto
        
        cantidadCarrito = carrito.cantidad
        cantidadProducto = product.quantity
        
        if cantidadProducto > cantidadCarrito:
            product.quantity = cantidadProducto - cantidadCarrito
            product.count_sale += carrito.cantidad
            carrito.delete()
            product.save()
            return redirect('ver_carrito')
        else:
             return redirect('ver_carrito')
    
    
def show_filter (request, Genero, min, max):
    
    products = Libro.objects.filter(genero=Genero, price__gte=min, price__lte=max)
    #Concretamente tuve que utilizar author__in para poder filtrar los autores de los libros filtrados por genero
    authors = Author.objects.filter(author__in=products)
    
    #paginator
    
    paginator_products = Paginator(products, 12)
    
    paginator_authors = Paginator(authors, 12)
    
    page_number = request.GET.get("page")    
    
    page_obj_prod = paginator_products.get_page(page_number)
    
    page_obj_author = paginator_authors.get_page(page_number)
    
    
    return render( request,'generos/genero.html', {'genero':Genero,'products': page_obj_prod, 'authors': page_obj_author})
    
    

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
    
    

def add_carrito(request, id):
    libro = Libro.objects.get(id=id)
    print(request.user)
    carrito, creado = Carrito.objects.get_or_create(usuario=request.user, producto=libro)
    if not creado:
        carrito.cantidad += 1
        carrito.save()
    return redirect('index')
    
    
def ver_carrito(request):
    carrito = Carrito.objects.filter(usuario=request.user)
    total = sum(item.producto.price  * item.cantidad for item in carrito)
    return render(request, 'shopping/carritoC.html', {"carrito":carrito, "total":total})
    


def actualizar_cantidad(request, id):
    
    libro = get_object_or_404(Carrito, id=id)
    
    if request.method == 'POST':
        
        new_quantity = request.POST.get('cantidad')
        libro.cantidad = new_quantity
        libro.save()
        
    return redirect('ver_carrito')

def eliminar_carrito(request, id):
    
    libro = get_object_or_404(Carrito, id=id)
    
    if request.method == 'POST':
        libro.delete()
    return redirect('ver_carrito')

    
def delete_comment(request, id_comment, id_libro):
    
    comment = Comment.objects.get(id=id_comment)
    comment.delete()
    return redirect('show_product',id_libro)
    



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
