from django.contrib.auth.models import User, Group
from agenda.models import Compromisso, Local, Convidado
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField


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


class LocalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Local
        fields = ['url', 'nome', 'rua', 'numero', 'foto']


class CompromissoSerializer(serializers.HyperlinkedModelSerializer):
    convidados = ConvidadoSerializer(many=True)
    local = LocalSerializer(many=False)
    dt_ini = SerializerMethodField()
    class Meta:
        model = Compromisso
        fields = ['url', 'descricao', 'dt_ini', 'data_fim', 'local', 'convidados']

    def get_dt_ini(self, obj):
        return obj.data_inicio.strftime("%d/%B/%Y")



