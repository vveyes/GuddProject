from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import TextID
from .serializers import ClientSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = TextID.objects.all()
    serializer_class = ClientSerializer
    lookup_field = 'uuid'

    @action(detail=False, methods=['post'])
    def new(self, request):
        many = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=many)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    @action(detail=False, methods=['get'])
    def all(self, request):
        queryset = TextID.objects.all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'],
            url_path=r'count_offset/(?P<count>\d+)/(?P<offset>\d+)',
            url_name='count_offset')
    def count_offset(self, request, *args, **kwargs):
        count = kwargs.get('count')
        offset = kwargs.get('offset')

        queryset = TextID.objects.all()[int(offset):int(offset) + int(count)]
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def by_filters(self, request):
        queryset = TextID.objects.all().order_by('-created_at')
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

