from rest_framework import viewsets, permissions
from rest_framework.response import Response
from django.contrib.auth.models import User, Group
from agenda.api.serializers import UserSerializer, GroupSerializer, CompromissoSerializer, LocalSerializer
from agenda.models import Compromisso, Convidado, Local


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class CompromissoViewSet(viewsets.ModelViewSet):
    queryset = Compromisso.objects.all()
    serializer_class = CompromissoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        #filtrando por query string (buscando compromisso pela descrição)
        id = self.request.query_params.get('id', None)
        descricao = self.request.query_params.get('descricao', None)
        queryset = Compromisso.objects.all()
        if id is not None:
            queryset = queryset.filter(id=id)
        if descricao is not None:
            queryset = queryset.filter(descricao=descricao)
        usuario_logado = self.request.user.username
        convidado = Convidado.objects.get(usuario__username=usuario_logado)
        # queryset.filter(convidados=convidado)
        return queryset.filter(convidados=convidado)

    def list(self, request, *args, **kwargs):
        return super(CompromissoViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        pass


class LocalViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']
    queryset = Local.objects.all()
    serializer_class = LocalSerializer
