from .models import Team, Failed, Finished, Current, Planned
from rest_framework.serializers import ModelSerializer


class TeamSerializer(ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class FailedSerializer(ModelSerializer):
    team_name = TeamSerializer(source='team')
    class Meta:
        model = Failed
        fields = '__all__'


class FinishedSerializer(ModelSerializer):
    team_name = TeamSerializer(source='team')
    class Meta:
        model = Finished
        fields = '__all__'


class CurrentSerializer(ModelSerializer):
    team_name = TeamSerializer(source='team')
    class Meta:
        model = Current
        fields = '__all__'


class PlannedSerializer(ModelSerializer):
    team_name = TeamSerializer(source='team')
    class Meta:
        model = Planned
        fields = '__all__'