from rest_framework import viewsets, permissions, generics
from .models import Chain, Store, Employee
from .serializers import ChainSerializer, StoreSerializer, EmployeeSerializer

from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework.authtoken.models import Token


# class LoginView(views.APIView):
#     def post(self, request, format=None):
#         data = request.data

#         username = data.get('username', None)
#         password = data.get('password', None)

#         user = authenticate(username=username, password=password)

#         if user is not None:
#             if user.is_active:
#                 login(request, user)

#                 return Response(status=status.HTTP_200_OK)
#             else:
#                 return Response(status=status.HTTP_404_NOT_FOUND)
#         else:
#             return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(["POST"])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username=username, password=password)
    if not user:
        return Response({"error": "Login failed"}, status=HTTP_401_UNAUTHORIZED)

    token, _ = Token.objects.get_or_create(user=user)
    return Response({"token": token.key})

class ChainViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Chain objects """
    model = Chain
    queryset = Chain.objects.all()
    serializer_class = ChainSerializer
    permission_classes = [
        IsAuthenticated
    ]


class StoreViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Store objects """
    model = Store
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
#    permission_classes = [
#        permissions.AllowAny
#    ]


class EmployeeViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Employee objects """
    model = Employee
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
#    permission_classes = [
#        permissions.AllowAny
#    ]
