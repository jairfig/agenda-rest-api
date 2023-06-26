from rest_framework import viewsets, permissions
from rest_framework.filters import SearchFilter
from django.contrib.auth.models import User, Group
from agenda.api.serializers import UserSerializer, GroupSerializer, CompromissoSerializer, LocalSerializer, ConvidadoSerializer
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


class ConvidadoViewSet(viewsets.ModelViewSet):
    queryset = Convidado.objects.all()
    serializer_class = ConvidadoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CompromissoViewSet(viewsets.ModelViewSet):
    queryset = Compromisso.objects.all()
    serializer_class = CompromissoSerializer
    permission_classes = [permissions.IsAuthenticated]
    # filterset_fields = ('descricao', 'data_inicio', )
    filter_backends = (SearchFilter, )
    search_fields = ('descricao', '^data_inicio', )

    def get_queryset(self):
        queryset = Compromisso.objects.all()
        try:
            usuario_logado = self.request.user.username
            convidado = Convidado.objects.get(usuario__username=usuario_logado)
            return queryset.filter(convidados=convidado)
        except:
            return queryset

    def list(self, request, *args, **kwargs):
        return super(CompromissoViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        pass


class LocalViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']
    queryset = Local.objects.all()
    serializer_class = LocalSerializer
