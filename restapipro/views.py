from rest_framework.views import APIView
from rest_framework.response import Response
from restapp.serializers import StudentsSerializer
from restapp.models import Students
from rest_framework.permissions import IsAuthenticated

class Testview(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
       qs = Students.objects.all()
       serializer = StudentsSerializer(qs, many=True)
       data = serializer.data   
       return Response(data)
    
    def post(self, request, *args, **kwargs):
        serializer = StudentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
