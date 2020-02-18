from rest_framework import viewsets

from .models import Note
from .serializers import NoteSerializer


class NoteViewSet(viewsets.ModelViewSet):

    model = Note
    serializer_class = NoteSerializer
    queryset = Note.objects.all()
