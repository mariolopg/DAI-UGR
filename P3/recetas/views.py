from multiprocessing import context
from django.shortcuts import render, Http404
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse

# Create your views here.

from django.shortcuts import  HttpResponse, redirect
from .forms import RecetaForm, IngredienteForm, FotoForm
from .models import Ingrediente, Receta, Foto
from django.contrib import messages

def get_mode(request):
    mode = ''
    if request.session.__contains__('dark_mode'):
        mode = request.session.__getitem__('dark_mode')

    return mode

# Create your views here.
@csrf_exempt
def index(request):
    
    context = {
        'saludado': 'Pepito',
        'modo': get_mode(request)
    }
    return render(request, 'base.html', context)

@csrf_exempt
def busqueda(request):
    name = request.GET.get("search_input")
    recetas = Receta.objects.filter(nombre__icontains = name)
    
    context = {
        'recetas': recetas,
        'modo': get_mode(request)
    }
    
    return render(request, 'busqueda.html', context)

@csrf_exempt
def detalle(request, _id):
    recetas = Receta.objects.filter(id = _id)
    ingredientes = Ingrediente.objects.filter(receta_id = _id)
    fotos = Foto.objects.filter(receta_id = _id)
    
    context = {
        'receta': recetas[0],
        'ingredientes': ingredientes,
        'fotos': fotos,
        'modo': get_mode(request)
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
    try: 
        receta =  Receta.objects.get(id = _id)
    # Si no existe se lanza un error 404
    except Receta.DoesNotExist:
        raise Http404('Not found')

    messages.add_message(request, messages.SUCCESS, 'Receta ' + receta.nombre + ' eliminada correctamente')
    receta.delete()
    return redirect(request.META['HTTP_REFERER'])


@csrf_exempt
def add_receta(request):

    formReceta = RecetaForm(request.POST or None)

    if formReceta.is_valid():
        receta = formReceta.save()
        messages.add_message(request, messages.SUCCESS, 'Receta ' + receta.nombre + ' añadida correctamente')
        return redirect('detalle', _id = receta.id)

    context = {
        'formReceta': formReceta,
        'modo': get_mode(request)  
    }

    return render(request, 'add_receta.html', context)

@csrf_exempt
def receta_edit(request, _id):
    receta = Receta.objects.get(id = _id)
    formReceta = RecetaForm(instance = receta)

    if request.method == 'POST':
        formReceta = RecetaForm(request.POST, instance = receta)

        if formReceta.is_valid():
            formReceta.save()
            messages.add_message(request, messages.SUCCESS, 'Receta ' + receta.nombre + ' editada correctamente')
            return redirect('detalle', _id = receta.id)

    context = {
        'formReceta': formReceta,
        'receta': receta,
        'modo': get_mode(request)  
    }

    return render(request, 'add_receta.html', context)
    