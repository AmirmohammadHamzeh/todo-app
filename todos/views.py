from rest_framework import generics, permissions
from .models import Todo
from .serializers import TodoSerializer
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class TodoListCreateView(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Todo.objects.none()  # برای Swagger schema
        return Todo.objects.filter(user=self.request.user)


class TodoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Todo.objects.none()  # برای Swagger schema
        return Todo.objects.filter(user=self.request.user)


# todos/views.py


class TodoSearchView(generics.ListAPIView):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'q', openapi.IN_QUERY,
                description="Search term for title or description",
                type=openapi.TYPE_STRING
            ),
        ],
        operation_description="Perform a full-text search on todos using PostgreSQL SearchVector"
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        if query:
            search_vector = (
                    SearchVector('title', weight='A') +
                    SearchVector('description', weight='B')
            )
            search_query = SearchQuery(query)
            return Todo.objects.annotate(
                rank=SearchRank(search_vector, search_query)
            ).filter(rank__gte=0.1).order_by('-rank', 'created_at')
        return Todo.objects.none()
