from rest_framework.generics import ListAPIView

from events.serializers import EventSerializer
from events.models import Event


class EventsView(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
