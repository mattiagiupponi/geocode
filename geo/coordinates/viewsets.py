from rest_framework import viewsets
from coordinates.models import RequestHistory
from coordinates.serializers import RequestHistorySerializer


class RequestHistoryViewSet(viewsets.ModelViewSet):
    queryset = RequestHistory.objects.all().order_by('-timestamp')
    serializer_class = RequestHistorySerializer
