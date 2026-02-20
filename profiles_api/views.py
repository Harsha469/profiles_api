from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework import status 
from profiles_api import serializers


class HelloApiView(APIView):
    """This is a class absed apiview you are going to full control on this"""

    serializer_class = serializers.HelloSerializer

    def get(self,request,format=None):

        an_apiview = ['Its a class based apiviews used for creating apis',
                      'You need to take over the full control of this class',
                      'validating inputs,fetching data,response,serializind data to json'
                      ]
        
        return Response({'message':'Hello!','an_apiview':an_apiview}) 
    

    def post(self,request):
        
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name} '
            return Response({'message':message})
        else:
            return Response(
                serializer.errors, 
                status = status.HTTP_400_BAD_REQUEST
                )

    def put(self,request,pk=None):

        ''' its going to update an object '''
        return Response({"message":"PUT"})

    def patch(self,request,pk=None):

        ''' its updates in an object not entire object'''
        return Response({'message':'PATCH'})

    def delete(self,request,pk=None):
        ''' its deletes an object '''

        return Response({'message':'DELETE'})