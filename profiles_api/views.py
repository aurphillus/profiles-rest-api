from rest_framework.views import APIView
from rest_framework.response import Response



class HelloApiView(APIView):
    '''Test API View'''

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
