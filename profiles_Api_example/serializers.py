from rest_framework import serializers
from profiles_Api_example import models

class HelloSerializer(serializers.Serializer):
    '''
    serializa un campo para probar nuestro apiview
    Los serializers son clases que nos permiten 
    transformar datos de formatos más propios de Django 
    como objetos que extienden de Model o querysets,
    en formatos más propios del entorno web
    como puedan ser JSON y XML, y nos permiten 
    hacerlo en ambas direcciones.
    '''
    name = serializers.CharField(max_length=10)

    