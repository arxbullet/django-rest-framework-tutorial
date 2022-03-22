from email import message
from django.shortcuts import render
from rest_framework import status
from profiles_Api_example import serializers
from rest_framework.views import APIView, Response

# Create your views here.
class helloApiView(APIView):
    """Api view de prueba """

    serializers_class = serializers.HelloSerializer

    def get(self, request, format=None):
        'retornar lista de caracteristicas del api view'
        an_Apiview = [
            'usamos metodos http como funciones (get, post, path, put, delete)',
            'es similar a una view tradicional de django',
            'nos da el mayor control sobre la logica de nuestra app',
            'esta mapeado manualmente a los urls' ,
            'cada funcion debe retornar un response objetct',
            'los response transforman la info en json',
            'solo debemos pasarles listas o diccionarios'
        ]
        return Response({'message ': 'hello', 'an_apiview': an_Apiview})

    def post(self, request):

        serializer = self.serializers_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello{name}'
            return Response({'message':message})

        else :
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )