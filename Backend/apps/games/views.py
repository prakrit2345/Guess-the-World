from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# Create your views here.

class CreateGameView(APIView):

    # permission_classes = [IsAuthenticated]

    def post(self, request):
        self.request = request

        print(request)


        user = request.user

        print("User information: ",user)

        return Response({
            "success": True,
            "userData": user,
        })
    