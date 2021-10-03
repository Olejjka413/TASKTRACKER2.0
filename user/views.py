from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import IntegrityError
import datetime
import jwt

from task_tracker.models import Team
from .serializers import UserSerializer
from .models import User


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        response = Response()
        response.data = serializer.data
        response.data['message'] = 'success'
        return response


class LoginView(APIView):
    def post(self, request):
        login = request.data['login']
        password = request.data['password']

        try:
            user = User.objects.get(login=login)
        except Exception:
            return Response({'message': 'User not found'})

        if not user.check_password(password):
            return Response({'message': 'Incorrect password'})

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=5),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()

        response.set_cookie(key='token', value=token, httponly=True)
        response.data = {
            'message': 'success',
            'login': user.login,
        }
        return response


class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('token')

        if not token:
            return Response({'message': 'Unauthenticated'})

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return Response({'message': 'Unauthenticated'})

        data = {}

        user = User.objects.get(id=payload['id'])
        data = UserSerializer(user).data


        return Response(data)


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('token')
        response.data = {
            'message': 'success'
        }

        return response


class UpdateView(APIView):
    def patch(self, request, *args, **kwargs):
        token = request.COOKIES.get('token')

        if not token:
            return Response({'message': 'Unauthenticated'})

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return Response({'message': 'Unauthenticated'})

        user = User.objects.get(id=payload['id'])
        data = request.data

        response = Response()

        try:

            if 'team' in data:
                try:
                    team = Team.objects.get(name=data['team'])
                except Team.DoesNotExist:
                    response.data = {
                        'message': 'failed'
                    }
                user.team = team

            user.save()

            response.data = {
                'message': 'success'
            }
        except IntegrityError:
            response.data = {
                'message': 'failed'
            }

        return response


class DeleteView(APIView):
    def delete(self, request):
        data = request.data
        response = Response()
        token = request.COOKIES.get('token')

        if not token:
            return Response({'message': 'Unauthenticated'})

        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        user = User.objects.get(id=payload['id'])

        if (user.check_password(data.get('password')) and user.login == data.get('login')):
            user.delete()
            response.delete_cookie('token')
            response.data = {
                'message': 'success'
            }
        else:
            response.data = {
                'message': 'failed'
            }

        return response