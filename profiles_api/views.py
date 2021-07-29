from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions

class HelloApiView(APIView):
    """ Test API View """

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """ Returns a list of APIView features """

        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self,request):
        """ Create a hello message with our name """
        serializers = self.serializer_class(data=request.data)

        if serializers.is_valid():
            name = serializers.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializers.errors,
                status=status.HTTP_400_BAD_REQUEST    
            )

    def put(self, request, pk=None):
        """ Handle updating an object """
        return Response({'method': 'PUT'})
    
    def patch(self, request, pk=None):
        """ Handle a partial update of an object """
        return Response({'method': 'PATCH'})
    
    def delete(self, request, pk=None):
        """ Delete an object """
        return Response({'method': 'DELETE'})

class HelloViewSet(viewsets.ViewSet):

    serializer_class = serializers.HelloSerializer

    """ TEST API VIEW SET """
    def list (self,request):
        """ RETURN a hello message """
        a_viewset= [
            'Uses actions (list, create, retrive, update, partial_update and destroy)',
            'Automatically maps to url using routers',
            'Provides more functionality and less code'
        ]
        return Response({'message':'Hello View API!','a_viewset':a_viewset})

    def create(self,request):
        """ CREATE a new hello message """
        serializers = self.serializer_class(data=request.data)
        if serializers.is_valid():
            name=serializers.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message':message})
        else:
            return Response(
                serializers.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self,request,pk=None):
        """ Handle getting object by its ID """
        return Response({'http_method':'GET'})

    def update(self,request,pk=None):
        """ Handle updated an object """
        return Response({'http_method':'UPDATE'})

    def partial_update(self,request,pk=None):
        """ Handle updating part of an object """
        return Response({'http_method':'PATCH'})
    
    def destroy(self,request,pk=None):
        """ Handle removing an object """
        return Response({'http_method':'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """ Handle creating and updating profiles """
    serializer_class = serializers.UserProfileSerializer
    queryset= models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permissions_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields= ('name','email',)