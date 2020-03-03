from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


class HelloApiView(APIView):
    '''Test API View'''
    serializer_class = serializers.HelloSerializer

    def get(self, reqeust, format=None):
        '''Returs a list of APIView features'''
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django view',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLS',
        ]

        context = {
        'mesasage' : 'Hello!',
        'an_apiview': an_apiview,
        }

        return Response(context)

    def post(self, request):
        '''Create hello message with our name'''
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            context = {
                'message': message,
            }
            return Response(context)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        '''Handling updating an object'''
        context = {
        'method' : 'put',
        }
        return Response(context)

    def patch(self, request, pk=None):
        '''Handle a partial update of an object'''
        context = {
        'method' : 'patch',
        }
        return Response(context)

    def delete(self, request, pk=None):
        '''Delete an object'''
        context = {
        'method' : 'delete',
        }
        return Response(context)
