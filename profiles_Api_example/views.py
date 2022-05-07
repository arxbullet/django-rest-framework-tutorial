from ast import Is
from rest_framework import status, viewsets, filters
from profiles_Api_example import serializers, models, permissions
from rest_framework.views import APIView, Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly


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

    def put(self, request, pk=None):
        """maneja actualizar un objeto"""
        return Response({'method':'PUT'})

    def patch(self, request, pk=None):
        """maneja actualizar parcialmente un objeto"""
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        """maneja borrar un objeto"""
        return Response({'method':'DELETE'})


    #VIEW SET

class helloViewSet(viewsets.ViewSet):

    serializers_class = serializers.HelloSerializer

    def list(self, request):
        a_viewset = [
            'usamos acciones  (list, create, retrieve, update, partial_upate)',
            'automaticamente mapea a los URLs usando RRouters',
            'provee mas funcionalidad con menos codigo',
        ]
    
        return Response({'message ': 'hello', 'a_viewset': a_viewset})

    
    def create(self, request):
        """crear nuevo mensaje de hola mundo"""

        serializer = self.serializers_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hola {name}'
            return Response({'message':message})

        else :
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )
       

    def retrieve(self, request, pk=None):
        """obtiene un objeto y su id"""
        return Response({'http_method':'GET'})

    def update(self, request, pk=None):
        """actualiza un objeto"""
        return Response({'http_method':'PUT'})

    def partial_update(self, request, pk=None):
        """actualizar parcialmente un objeto"""
        return Response({'http_method':'PATCH'})

    def destroy(self, request, pk=None):
        """ borrar un objeto"""
        return Response({'http_method':'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """crear y actualizar perfiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email')#agregamos coma para que python sepa que es una tupla
    
class UserLoginApiView(ObtainAuthToken):
    '''crear tokens de autenticacion de usuario'''

    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class UserProfileFeedViewSet(viewsets.ModelViewSet):
    '''Maneja el crear, leer y actualizar el profile fit'''

    serializer_class = serializers.ProfileItemSerializers
    queryset = models.ProfileFeedItem.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnStatus,
                          IsAuthenticatedOrReadOnly) #si no queremos que no se lea sin autenticarse cambiaremos esto por isAutenticated
   # filter_backends = (filters.SearchFilter,)
   # search_fields = ('name','email')#agregamos coma para que python sepa que es una tupla

    def perform_create(self, serializer):
       '''setea el perfil de usuario para el usuario autenticado'''
       serializer.save(user_profile=self.request.user)
