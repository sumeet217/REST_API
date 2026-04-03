from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import StudentsSerializer
from .models import Students


class StudentListCreateView(APIView):
    """API view to list all students or create a new student."""
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        qs = Students.objects.all()
        serializer = StudentsSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = StudentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
