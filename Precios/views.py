from django.shortcuts import render

def lista_precios(request):
    servicios_disponibles = [
        {'servicio': 'Cambio de Aceite', 'precio': 25000},
        {'servicio': 'Alineación y Balanceo', 'precio': 15000},
        {'servicio': 'Revisión Técnica', 'precio': 35000},
    ]
    contexto = {
        'titulo': 'Lista de Precios',
        'lista_servicios': servicios_disponibles
    }
    return render(request, 'precios/lista.html', contexto)