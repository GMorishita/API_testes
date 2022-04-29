from rest_framework.response import Response
from django.contrib.auth.models import User

from usuarios.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


class ConstUsuarios(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, format=None):
        """
        A funcao esta retornando todos os usuários por API
        @param1: usuarios
        @param2: serializer
        @return: 200: API está retornando todos os usuarios.
        @raise 404: se os objetos nao foram encontrados
        """
        usuarios = User.objects.all()
        serializer = UserSerializer(usuarios, many=True, context={'request': request})

        return Response(serializer.data)


class Const1Usuario(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, pk):
        """
        A funcao esta retornando todos os usuários por API
        @param1: usuario
        @param2: serializer
        @return: 200: API está retornando todos os usuarios.
        @raise 404: se os objetos nao foram encontrados
        """
        usuario = User.objects.filter(pk=pk)
        serializer = UserSerializer(usuario, many=True, context={'request': request})

        if not usuario:
            return Response({'mensagem': 'Não existe um usuário com este Primary Key'})

        return Response(serializer.data)


class DeleteUsuario(APIView):
    permission_classes = (IsAuthenticated, )
    def delete(self, request, pk):
        """
        A funcao esta retornando todos os usuários por API
        @param1: usuario
        @param2: serializer
        @return: 200: API está retornando todos os usuarios.
        @raise 404: se os objetos nao foram encontrados
        """
        usuario = User.objects.filter(pk=pk)
        serializer = UserSerializer(usuario, many=True, context={'request': request})

        if usuario:
            usuario.delete()
            return Response({'mensagem': 'Usuário deletado com sucesso'})
        else:
            return Response({'mensagem': 'Não existe um usuário com este Primary Key'})


class CriarUsuario(APIView):
    # permission_classes = (IsAuthenticated, )
    def post(self, request):
        """
        A funcao esta retornando todos os usuários por API
        @param1: dados_usuario
        @param2: usuario_existe
        @param3: usuario
        @return: 200: API está retornando todos os usuarios.
        @raise 404: se os objetos nao foram encontrados
        """
        dados_usuario = request.data
        usuario_existe = dados_usuario['email']
        usuario = User.objects.filter(username=usuario_existe)
        if usuario:
            return Response({'mensagem': 'Um usuário já tem este email, informe outro username'})
        else:
            usuario = User.objects.create(
                email=dados_usuario['email'],
                username=dados_usuario['email'],
            )
            usuario.set_password(dados_usuario['password'])
            usuario.save()
            return Response({'mensagem': 'Usuario criado com sucesso!'})


class UpdateUsuario(APIView):
    permission_classes = (IsAuthenticated, )
    def put(self, request):
        """
        A funcao esta retornando todos os usuários por API
        @param1: dados_usuario
        @param2: usuario
        @return: 200: API está retornando todos os usuarios.
        @raise 404: se os objetos nao foram encontrados
        """
        dados_usuario = request.data
        usuario = User.objects.filter(pk=dados_usuario['pk'])
        if usuario:
            usuario.update(
                email=dados_usuario['email'],
                username=dados_usuario['email'],
                password=dados_usuario['password'],
            )
            return Response({'mensagem': 'Usuario atualizado'})
        else:
            return Response({'mensagem': 'Não existe um usuário com essa Primary Key'})
