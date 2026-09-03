from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models
from .serializer import RegisterModelSerializer, LoginModelSerializer
from rest_framework import status
# Create your views here.

@api_view(['POST'])
def RegisterUser(request):
    print(request.data)
    serializer = RegisterModelSerializer(data=request.data)    
    if serializer.is_valid():
        serializer.save()
        return Response(
            serializer.data, 
            status = status.HTTP_201_CREATED
        )
    return Response(
        serializer.errors,
        status= status.HTTP_400_BAD_REQUEST
    )
    
    
# For the login checking
@api_view(['GET', 'POST'])
def LoginCheck(request):
    print(request.data)
    serializer = LoginModelSerializer(data=request.data)
    
    if serializer.is_valid():
        print("Reaching here.")
        access_token = serializer.validated_data["access"]
        refresh_token = serializer.validated_data["refresh"]
        
        
        return Response(
            {
                "message": "success",
                "data":  {
                    "refresh_token": refresh_token,
                    "access_token": access_token
                }
            }
        )
    return Response(
         {
                "message": "fail",
                "data":  {
                    "error": serializer.error_messages
                }
            }
    )