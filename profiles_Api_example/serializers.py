from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    '''serializa un campo para probar nuestro apiview'''
    name = serializers.CharField(max_length=10)