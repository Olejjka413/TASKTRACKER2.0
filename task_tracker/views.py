from .serailizers import *
from rest_framework.views import APIView
from rest_framework.response import Response
import jwt
from user.models import User

class TeamListView(APIView):
    def get(self, request):
        team = Team.objects.all()
        data = TeamSerializer(team, many=True).data
        return Response(data)

    def post(self, request):
        if 'name' not in request.data:
            return Response({'message': "Team's name must not be empty"})
        try:
            candidate = Team.objects.get(name=request.data['name'])
            return Response({'message': "Team's name already claimed"})
        except Team.DoesNotExist:
            team = Team.objects.create(name=request.data['name'])
            return Response({'message': 'success', 'team_id': team.id})

class TeamDetailView(APIView):
    def get(self, request, pk):
        try:
            team = Team.objects.get(id=pk)
            data = TeamSerializer(team).data
            return Response(data)
        except Team.DoesNotExist:
            return Response({'message': 'team not found'})


class PlannedListView(APIView):
    def get(self, request):
        token = request.COOKIES.get('token')
        if not token:
            return Response({'message': 'Unauthorized'})

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return Response({'message': 'Unauthenticated'})

        user = User.objects.get(id=payload['id'])
        team = Team.objects.get(user=user)

        planned_tasks = Planned.objects.filter(team=team)
        data = PlannedSerializer(planned_tasks, many=True).data
        return Response(data)

    def post(self, request):
        token = request.COOKIES.get('token')
        if not token:
            return Response({'message': 'Unauthorized'})

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return Response({'message': 'Unauthenticated'})

        user = User.objects.get(id=payload['id'])
        team = Team.objects.get(user=user)

        if 'title' not in request.data:
            return Response({'message': 'Task must have an title'})
        elif 'date' not in request.data:
            return Response({'message': 'Task must have an deadline'})

        new_planned_task = Planned.objects.create(team=team, title=request.data['title'], description=request.data['description'], date=request.data['date'])
        new_planned_task.save()
        return Response({'message': 'success'})


class PlannedDetailView(APIView):
    def patch(self, request, pk):
        token = request.COOKIES.get('token')
        if not token:
            return Response({'message': 'Unauthorized'})

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return Response({'message': 'Unauthenticated'})

        user = User.objects.get(id=payload['id'])
        team = Team.objects.get(user=user)

        try:
            candidate = Planned.objects.get(id=pk, team=team)
            if 'title' in request.data:
                candidate.title = request.data['title']

            if 'description' in request.data:
                candidate.description = request.data['description']

            if 'date' in request.data:
                candidate.date = request.data['date']

            candidate.save()
        except Planned.DoesNotExist:
            return Response({'message': 'Does not exist'})

        return Response({'message': 'success'})


    def delete(self, request, pk):
        token = request.COOKIES.get('token')
        if not token:
            return Response({'message': 'Unauthorized'})

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return Response({'message': 'Unauthenticated'})

        user = User.objects.get(id=payload['id'])
        team = Team.objects.get(user=user)

        try:
            candidate = Planned.objects.get(id=pk, team=team)
            candidate.delete()
        except Planned.DoesNotExist:
            return Response({'message': 'Does not exist'})

        return Response({'message': 'success'})


class FinishedListView(APIView):
    def get(self, request):
        token = request.COOKIES.get('token')
        if not token:
            return Response({'message': 'Unauthorized'})

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return Response({'message': 'Unauthenticated'})

        user = User.objects.get(id=payload['id'])
        team = Team.objects.get(user=user)

        finished_tasks = Finished.objects.filter(team=team)
        data = FinishedSerializer(finished_tasks, many=True).data
        return Response(data)

    def post(self, request):
        token = request.COOKIES.get('token')
        if not token:
            return Response({'message': 'Unauthorized'})

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return Response({'message': 'Unauthenticated'})

        user = User.objects.get(id=payload['id'])
        team = Team.objects.get(user=user)

        if 'title' not in request.data:
            return Response({'message': 'Task must have an title'})
        elif 'date' not in request.data:
            return Response({'message': 'Task must have an deadline'})

        new_finished_task = Finished.objects.create(team=team, title=request.data['title'], description=request.data['description'], date=request.data['date'])
        new_finished_task.save()
        return Response({'message': 'success'})


class FinishedDetailView(APIView):
    def patch(self, request, pk):
        token = request.COOKIES.get('token')
        if not token:
            return Response({'message': 'Unauthorized'})

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return Response({'message': 'Unauthenticated'})

        user = User.objects.get(id=payload['id'])
        team = Team.objects.get(user=user)

        try:
            candidate = Finished.objects.get(id=pk, team=team)
            if 'title' in request.data:
                candidate.title = request.data['title']

            if 'description' in request.data:
                candidate.description = request.data['description']

            if 'date' in request.data:
                candidate.date = request.data['date']

            candidate.save()
        except Finished.DoesNotExist:
            return Response({'message': 'Does not exist'})

        return Response({'message': 'success'})


    def delete(self, request, pk):
        token = request.COOKIES.get('token')
        if not token:
            return Response({'message': 'Unauthorized'})

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return Response({'message': 'Unauthenticated'})

        user = User.objects.get(id=payload['id'])
        team = Team.objects.get(user=user)

        try:
            candidate = Finished.objects.get(id=pk, team=team)
            candidate.delete()
        except Finished.DoesNotExist:
            return Response({'message': 'Does not exist'})

        return Response({'message': 'success'})


class CurrentListView(APIView):
    def get(self, request):
        token = request.COOKIES.get('token')
        if not token:
            return Response({'message': 'Unauthorized'})

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return Response({'message': 'Unauthenticated'})

        user = User.objects.get(id=payload['id'])
        team = Team.objects.get(user=user)

        current_tasks = Current.objects.filter(team=team)
        data = CurrentSerializer(current_tasks, many=True).data
        return Response(data)

    def post(self, request):
        token = request.COOKIES.get('token')
        if not token:
            return Response({'message': 'Unauthorized'})

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return Response({'message': 'Unauthenticated'})

        user = User.objects.get(id=payload['id'])
        team = Team.objects.get(user=user)

        if 'title' not in request.data:
            return Response({'message': 'Task must have an title'})
        elif 'date' not in request.data:
            return Response({'message': 'Task must have an deadline'})

        new_current_task = Planned.objects.create(team=team, title=request.data['title'], description=request.data['description'], date=request.data['date'])
        new_current_task.save()
        return Response({'message': 'success'})


class CurrentDetailView(APIView):
    def patch(self, request, pk):
        token = request.COOKIES.get('token')
        if not token:
            return Response({'message': 'Unauthorized'})

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return Response({'message': 'Unauthenticated'})

        user = User.objects.get(id=payload['id'])
        team = Team.objects.get(user=user)

        try:
            candidate = Current.objects.get(id=pk, team=team)
            if 'title' in request.data:
                candidate.title = request.data['title']

            if 'description' in request.data:
                candidate.description = request.data['description']

            if 'date' in request.data:
                candidate.date = request.data['date']

            candidate.save()
        except Current.DoesNotExist:
            return Response({'message': 'Does not exist'})

        return Response({'message': 'success'})


    def delete(self, request, pk):
        token = request.COOKIES.get('token')
        if not token:
            return Response({'message': 'Unauthorized'})

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return Response({'message': 'Unauthenticated'})

        user = User.objects.get(id=payload['id'])
        team = Team.objects.get(user=user)

        try:
            candidate = Current.objects.get(id=pk, team=team)
            candidate.delete()
        except Current.DoesNotExist:
            return Response({'message': 'Does not exist'})

        return Response({'message': 'success'})


class FailedListView(APIView):
    def get(self, request):
        token = request.COOKIES.get('token')
        if not token:
            return Response({'message': 'Unauthorized'})

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return Response({'message': 'Unauthenticated'})

        user = User.objects.get(id=payload['id'])
        team = Team.objects.get(user=user)

        failed_tasks = Failed.objects.filter(team=team)
        data = PlannedSerializer(failed_tasks, many=True).data
        return Response(data)

    def post(self, request):
        token = request.COOKIES.get('token')
        if not token:
            return Response({'message': 'Unauthorized'})

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return Response({'message': 'Unauthenticated'})

        user = User.objects.get(id=payload['id'])
        team = Team.objects.get(user=user)

        if 'title' not in request.data:
            return Response({'message': 'Task must have an title'})
        elif 'date' not in request.data:
            return Response({'message': 'Task must have an deadline'})

        new_failed_task = Planned.objects.create(team=team, title=request.data['title'], description=request.data['description'], date=request.data['date'])
        new_failed_task.save()
        return Response({'message': 'success'})


class FailedDetailView(APIView):
    def patch(self, request, pk):
        token = request.COOKIES.get('token')
        if not token:
            return Response({'message': 'Unauthorized'})

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return Response({'message': 'Unauthenticated'})

        user = User.objects.get(id=payload['id'])
        team = Team.objects.get(user=user)

        try:
            candidate = Failed.objects.get(id=pk, team=team)
            if 'title' in request.data:
                candidate.title = request.data['title']

            if 'description' in request.data:
                candidate.description = request.data['description']

            if 'date' in request.data:
                candidate.date = request.data['date']

            candidate.save()
        except Failed.DoesNotExist:
            return Response({'message': 'Does not exist'})

        return Response({'message': 'success'})


    def delete(self, request, pk):
        token = request.COOKIES.get('token')
        if not token:
            return Response({'message': 'Unauthorized'})

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return Response({'message': 'Unauthenticated'})

        user = User.objects.get(id=payload['id'])
        team = Team.objects.get(user=user)

        try:
            candidate = Failed.objects.get(id=pk, team=team)
            candidate.delete()
        except Failed.DoesNotExist:
            return Response({'message': 'Does not exist'})

        return Response({'message': 'success'})