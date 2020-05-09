from bitbucket_agent.models import Report
from bitbucket_agent.serializers import ReportSerializer
from rest_framework import viewsets


class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
