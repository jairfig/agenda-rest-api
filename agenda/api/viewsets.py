from rest_framework import viewsets, permissions
from django.contrib.auth.models import User, Group
from agenda.api.serializers import UserSerializer, GroupSerializer, CompromissoSerializer
from agenda.models import Compromisso, Convidado


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
        usuario_logado = self.request.user.username
        convidado = Convidado.objects.get(usuario__username=usuario_logado)
        return Compromisso.objects.filter(convidados=convidado)
