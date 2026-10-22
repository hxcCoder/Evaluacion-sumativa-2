
from django.shortcuts import render, redirect, get_object_or_404

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status

from .models import Auto
from .forms import AutoForm
from .serializers import AutoSerializer


# =========================
# VISTAS WEB
# =========================

def catalogo(request):
    autos = Auto.objects.all()
    contexto = {
        'titulo': 'Catálogo de Autos',
        'lista_autos': autos,
    }
    return render(request, 'core/catalogo.html', contexto)


def crear_auto(request):
    if request.method == 'POST':
        form = AutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogo_autos')
    else:
        form = AutoForm()

    return render(request, 'Autos/formulario.html', {'form': form})


def editar_auto(request, id):
    auto = get_object_or_404(Auto, id=id)

    if request.method == 'POST':
        form = AutoForm(request.POST, instance=auto)
        if form.is_valid():
            form.save()
            return redirect('catalogo_autos')
    else:
        form = AutoForm(instance=auto)

    return render(request, 'Autos/formulario.html', {'form': form})


def eliminar_auto(request, id):
    auto = get_object_or_404(Auto, id=id)

    if request.method == 'POST':
        auto.delete()
        return redirect('catalogo_autos')

    return render(
        request,
        'Autos/confirmar_eliminar.html',
        {'auto': auto}
    )


# =========================
# API REST
# =========================

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def lista_autos_api(request):
    if request.method == 'GET':
        autos = Auto.objects.all()
        serializer = AutoSerializer(autos, many=True)
        return Response(serializer.data)

    serializer = AutoSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(
            {
                'mensaje': 'Registro creado',
                'data': serializer.data,
            },
            status=status.HTTP_201_CREATED
        )

    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def detalle_auto_api(request, id):
    try:
        auto = Auto.objects.get(id=id)
    except Auto.DoesNotExist:
        return Response(
            {'detail': 'Not found.'},
            status=status.HTTP_404_NOT_FOUND
        )

    if request.method == 'GET':
        serializer = AutoSerializer(auto)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AutoSerializer(auto, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    elif request.method == 'DELETE':
        auto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
