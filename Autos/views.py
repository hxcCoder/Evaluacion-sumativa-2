from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import AutoSerializer

@api_view(['GET', 'POST'])
def lista_autos_api(request):
    if request.method == 'GET':
        autos = Auto.objects.all()
        serializer = AutoSerializer(autos, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        if not request.user.is_authenticated:
            return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)
        
        serializer = AutoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"mensaje": "Registro creado", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated]) # Protege toda esta vista
def detalle_auto_api(request, id):
    try:
        auto = Auto.objects.get(id=id)
    except Auto.DoesNotExist:
        return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = AutoSerializer(auto)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = AutoSerializer(auto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        auto.delete()
        return Response({"mensaje": "Registro eliminado"}, status=status.HTTP_204_NO_CONTENT)