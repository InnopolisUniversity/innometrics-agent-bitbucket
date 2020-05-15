from bitbucket_agent.models import Report
from bitbucket_agent.serializers import ReportSerializer
from rest_framework import viewsets


class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

    def create(self, request, *args, **kwargs):
        request.data.update({"raw": request.data})
        request.data.update({"HMAC": request.META.get("HTTP_X_HUB_SIGNATURE", None)})
        response = super().create(request, data=request.data)
        return response
