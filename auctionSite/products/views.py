from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
# from .serializers import UserSerializer
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email',)


class UserLoginView(APIView):
    def post(self, request):
        email = request.data.get('email')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            # If user does not exist, create a new user
            user = User(email=email)
            user.save()

        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
