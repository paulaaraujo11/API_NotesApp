from rest_framework import viewsets
from tasks.models import Tasks
from tasks.api.serializers import TasksSerializer

class TasksViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer

    def get_queryset(self):
        request = self.request.query_params
        request = request.dict()
        tasks = Tasks.objects.filter(enabled=True)
        for k, val in request.items():
            if val != '' and val != None:
                tasks = tasks.filter(**{k: val})
        return tasks
    
