from django.shortcuts import render
from django.utils import timezone
from .models import Publicacion

# Create your views here.
def post_list(request):
    #Realiza una consulta de posts realizado y los ordena por fecha de pulicacion
    publicacion = Publicacion.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #Se crea una variable posts que almacene el resultado de la consulta y se muestre en la pagina HTML
    return render(request, 'blog/post_list.html', {'posts': publicacion})