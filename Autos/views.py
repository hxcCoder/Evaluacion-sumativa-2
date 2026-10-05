from django.shortcuts import render, redirect, get_object_or_404
from .models import Auto
from .forms import AutoForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import AutoSerializer


# 1. Modificamos el catálogo para que lea de la Base de Datos real
def catalogo(request):
    autos_disponibles = Auto.objects.all() # Trae todos los autos guardados
    contexto = {
        'titulo': 'Catálogo de Vehículos',
        'lista_autos': autos_disponibles
    }
    return render(request, 'core/catalogo.html', contexto)

# 2. Creamos la nueva vista para agregar autos
def crear_auto(request):
    if request.method == "POST":
        form = AutoForm(request.POST) # Recibe lo que el usuario escribió
        if form.is_valid():
            form.save() # Guarda en la base de datos
            return redirect("catalogo_autos") # Lo manda de vuelta al catálogo
    else:
        form = AutoForm() # Formulario vacío
        return render(request, "Autos/formulario.html", {"form": form})
    
def editar_auto(request, id):
    auto = get_object_or_404(Auto, id=id)
    form = AutoForm(request.POST or None, instance=auto)
    
    if form.is_valid():
        form.save()
        return redirect('catalogo_autos')
    return render(request, 'Autos/formulario.html', {'form': form})

def eliminar_auto(request, id):
    auto = get_object_or_404(Auto, id=id)
    if request.method == 'POST':
        auto.delete()
        return redirect('catalogo_autos')
    return render(request, 'Autos/confirmar_eliminar.html', {'auto': auto})
    
# Vista para la API
@api_view(["GET"])
def lista_autos_api(request):
    autos = Auto.objects.all()
    serializer = AutoSerializer(autos, many=True)
    return Response(serializer.data)