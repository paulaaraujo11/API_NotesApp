from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from note.models import Note

class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = ('id','title','description','deadline_date','enabled')

   