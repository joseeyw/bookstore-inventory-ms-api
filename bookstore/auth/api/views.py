from rest_framework import generics, permissions,status
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer
from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LogoutView as KnoxLogoutView, LoginView as KnoxLoginView
from knox import views as knox_views
from knox.auth import TokenAuthentication


# Register API
class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1],
        "status":status.HTTP_201_CREATED
        },status.HTTP_201_CREATED )


class LoginView(generics.GenericAPIView, KnoxLoginView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = LoginSerializer
    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginView, self).post(request, format=None)