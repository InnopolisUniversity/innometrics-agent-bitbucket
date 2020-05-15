from bitbucket_agent.models import Report
from rest_framework import serializers


class ReportSerializer(serializers.ModelSerializer):
    actor = serializers.JSONField()
    payload = serializers.JSONField(required=False)

    class Meta:
        model = Report
        fields = ["actor", "eventKey", "date", "HMAC", "payload"]

    def to_internal_value(self, data):
        ret = super().to_internal_value(data)
        # data.pop("eventKey", None)
        # data.pop("date", None)
        # data.pop("actor", None)
        data.pop("HMAC", None)
        ret.update({"payload": data})
        return ret
