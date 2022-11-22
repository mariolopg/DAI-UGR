from multiprocessing import context
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse

# Create your views here.

from django.shortcuts import  HttpResponse, redirect

from .forms import RecetaForm, IngredienteForm, FotoForm

from .models import Ingrediente, Receta, Foto

# Create your views here.
@csrf_exempt
def index(request):
    mode = ''
    if request.session.__contains__('dark_mode'):
        mode = request.session.__getitem__('dark_mode')
    context = {
        'saludado': 'Pepito',
        'modo': mode
    }
    return render(request, 'base.html', context)

@csrf_exempt
def busqueda(request):
    mode = ''
    if request.session.__contains__('dark_mode'):
        mode = request.session.__getitem__('dark_mode')

    name = request.GET.get("search_input")
    recetas = Receta.objects.filter(nombre__icontains = name)
    
    context = {
        'recetas': recetas,
        'modo': mode
    }
    
    return render(request, 'busqueda.html', context)

@csrf_exempt
def detalle(request, _id):
    mode = ''
    if request.session.__contains__('dark_mode'):
        mode = request.session.__getitem__('dark_mode')

    recetas = Receta.objects.filter(id = _id)
    ingredientes = Ingrediente.objects.filter(receta_id = _id)
    fotos = Foto.objects.filter(receta_id = _id)
    
    context = {
        'receta': recetas[0],
        'ingredientes': ingredientes,
        'fotos': fotos,
        'modo': mode  
    }
    
    return render(request, 'detalle.html', context)

@csrf_exempt
def darkmode(request):
    if request.session.__contains__('dark_mode'):
        if request.session.__getitem__('dark_mode') == '':
            request.session.__setitem__('dark_mode', 'checked')
        else:
            request.session.__setitem__('dark_mode', '')
    else:
        request.session.__setitem__('dark_mode', '')

    return redirect(request.META['HTTP_REFERER'])

@csrf_exempt
def recetas_delete(request, _id):
    Receta.objects.filter(id = _id).delete()
    return redirect(request.META['HTTP_REFERER'])


@csrf_exempt
def add_receta(request):

    mode = ''
    if request.session.__contains__('dark_mode'):
        mode = request.session.__getitem__('dark_mode')

    if request.method == "POST":
        formReceta = RecetaForm(request.POST)

        if formReceta.is_valid():
            post = formReceta.save()

            context = {
                'receta': post,
                'modo': mode  
            }

            return render(request, 'detalle.html', context)

    formReceta = RecetaForm

    context = {
        'formReceta': formReceta,
        'modo': mode  
    }

    return render(request, 'add_receta.html', context)
    