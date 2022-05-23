from rest_framework.views import APIView
from accounts.models import  User
from .serializers import  UserSerializer
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.db.models import Q
from django.contrib.auth.models import update_last_login



class RegisterApiView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        #refresh_token= str(RefreshToken.for_user(user))
        #print(refresh_token)

        # return Response({'user':serializer.data,'token':''})
        return Response(serializer.data)


# class RegisterApiView(CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


class LoginApiView(APIView): 

    def post(self, request):
        # account can be email or phonenumber
        account = request.data['account']  
        password = request.data['password']

        user = User.objects.filter(Q(email=account) | Q(phone_number=account)).first()

        if user is None:
            raise AuthenticationFailed('User not found')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password') 

        # SlidingToken.for_user(user)
        # RefreshToken.for_user(user)
        refresh_token= str(RefreshToken.for_user(user))
        access_token = str(RefreshToken.for_user(user).access_token)    
 
        serializer = UserSerializer(user)
       # return Response({'token':encoded})     
        response = Response()
        # response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'access':access_token,
            'refresh':refresh_token,
            'user':serializer.data,
            'expire':50
        }
        # update last login...
        update_last_login(None, user)
        return response  

  
class UserProfileApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = User.objects.get(pk=request.user.id)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    