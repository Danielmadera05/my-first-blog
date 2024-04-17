from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Publicacion
from .forms import PublicacionForm
from django.shortcuts import redirect

# Muestra las publicaciones realizadas
def post_list(request):
    #Realiza una consulta de posts realizado y los ordena por fecha de pulicacion
    publicacion = Publicacion.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #Se crea una variable posts que almacene el resultado de la consulta y se muestre en la pagina HTML
    return render(request, 'blog/post_list.html', {'posts': publicacion})

#Muestra los detalles de una publicacion en especifica
def post_detail (request, pk):
    post = get_object_or_404(Publicacion, pk=pk)#Pagina de error en caso de no exister la PK buscada
    return render(request, 'blog/post_detail.html', {'post': post})

#Permite crear una nueva publicacion
def post_new(request):
    #Verifica si se quiere guardar un post o crear uno nuevo
    if request.method == "POST":
        form = PublicacionForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user #Toma la info del usuario que este activo en el momento
            post.published_date = timezone.now()
            post.save()
            
            return redirect('post_detail', pk=post.pk)#Si todo es correcto redirige al usuario a la pagina post_detail
    else:
        form = PublicacionForm()
    return render(request, 'blog/post_edit.html', {'form': form})

#Permite editar un post registrado
def post_edit(request, pk):
    post = get_object_or_404(Publicacion, pk=pk)
    if request.method == "POST":
        form = PublicacionForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            
            return redirect('post_detail', pk=post.pk)
    else:
        form = PublicacionForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})