from rest_framework.views import APIView 
from rest_framework.response import Response 


class HelloApiView(APIView):
    """This is a class absed apiview you are going to full control on this"""

    def get(self,request,format=None):

        an_apiview = ['Its a class based apiviews used for creating apis',
                      'You need to take over the full control of this class',
                      'validating inputs,fetching data,response,serializind data to json'
                      ]
        
        return Response({'message':'Hello!','an_apiview':an_apiview}) 
    