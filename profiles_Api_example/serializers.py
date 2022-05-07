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

class UserProfileSerializer(serializers.Serializer):
    '''serializa objetos tipo usuario'''
    
    class Meta :
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kawargs = {
            'passwd': {
                'write_only':True,
                'style' : {'input_type':'password'}
            }
        }

    def create(self, validated_data):
        'crea y retorna nuevo usuario'
        user = models.UserProfile.objects.create_user(
            email = validated_data['email'],
            name = validated_data['name'],
            password =  validated_data['password']
        )

        return user

    def update(self, instance, validated_data):
        'actualiza nuevo usuario'
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)

class ProfileItemSerializers(serializers.ModelSerializer):
    '''serializador para profile items'''
    class Meta:
        '''configura el serializador para poder trabajar con el modelo'''
        model = models.ProfileFeedItem
        fields = {'id', 'user_profile', 'status_text', 'created_on'}
        extra_kwargs = {'user_profile' : {'read_only':True}}
        