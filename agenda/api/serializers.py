from django.contrib.auth.models import User, Group
from agenda.models import Compromisso, Local, Convidado
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class ConvidadoSerializer(serializers.HyperlinkedModelSerializer):
    usuario = UserSerializer(many=False)
    class Meta:
        model = Convidado
        fields = ['url', 'nome', 'email', 'usuario']


class CompromissoSerializer(serializers.HyperlinkedModelSerializer):
    convidados = ConvidadoSerializer(many=True)
    class Meta:
        model = Compromisso
        fields = ['url', 'descricao', 'data_inicio', 'data_fim', 'local', 'convidados']


class LocalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Local
        fields = ['url', 'nome', 'rua', 'numero', 'foto']


