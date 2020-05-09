# from django.contrib.auth.models import User, Group
from bitbucket_agent.models import Report
from rest_framework import serializers

#
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'groups']
#
#
# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ['url', 'name']
#
#
# class ActorSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Actor
#         fields = '__all__'


class ReportSerializer(serializers.ModelSerializer):
    actor = serializers.JSONField()
    payload = serializers.JSONField(required=False)

    class Meta:
        model = Report
        fields = ["actor", "eventKey", "date", "payload"]

    def to_internal_value(self, data):
        ret = super().to_internal_value(data)
        data.pop("eventKey", None)
        data.pop("date", None)
        data.pop("actor", None)
        ret.update({"payload": data})
        return ret
