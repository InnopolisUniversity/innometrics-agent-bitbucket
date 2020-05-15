from bitbucket_agent.models import Report
from rest_framework import serializers


class ReportSerializer(serializers.ModelSerializer):
    actor = serializers.JSONField()
    raw = serializers.CharField(required=False)

    class Meta:
        model = Report
        fields = ["actor", "eventKey", "date", "HMAC", "raw"]

    def to_internal_value(self, data):
        ret = super().to_internal_value(data)
        # data.pop("eventKey", None)
        # data.pop("date", None)
        # data.pop("actor", None)
        data.pop("HMAC", None)
        ret.update({"raw": data.get("raw", {})})
        return ret
