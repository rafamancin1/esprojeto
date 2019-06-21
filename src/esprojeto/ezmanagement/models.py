from django.db import models
from django.utils import timezone

# Create your models here.
class Filial(models.Model):
    cnpjFilial = models.CharField(max_length=14)
    endereco = models.CharField(max_length=100)
    qtdFunc = models.IntegerField()

class Pessoa(models.Model):
    nome_P = models.CharField(max_length=50, default='')
    telefone_P = models.CharField(max_length=20,default='')
    endereco_P = models.CharField(max_length=100,default='')
    email_P = models.CharField(max_length=50,default='')
    filialAssociada = models.ForeignKey(Filial, on_delete=models.CASCADE)
    cnpjFilial = models.CharField(max_length=14, default='')
    class Meta:
        abstract = True

class Pessoa_Fisica(Pessoa):
    cpf_P = models.CharField(max_length=11, default='')
    class Meta:
        abstract = True

class Pessoa_Juridica(Pessoa):
    cnpj_P = models.CharField(max_length=14, default='')
    class Meta:
        abstract = True

class Funcionario(Pessoa_Fisica):
    dataContratacao_Func = models.DateTimeField('data de contratação', default=timezone.now())
    salario_Func = models.FloatField(default=1000.00)

    def __str__(self):
        return str(self.__dict__)

    class Meta:
        abstract = True

class Adm_Local(Funcionario):
    senha_adm = models.CharField(max_length=16,default='')

class Tecnico(Funcionario):
    areaAtuacao = models.CharField(max_length=20,default='')
    def __str__(self):
        return str(self.__dict__)

class Representante(Funcionario):
    estado_atuacao = models.CharField(max_length=50,default='')
    senha_repr = models.CharField(max_length=16,default='')

    def __str__(self):
        return str(self.__dict__)

class Fornecedor(Pessoa_Juridica):
    pass

class Materia_Prima(models.Model):
    nome_mat = models.CharField(max_length=50,default='')
    fornecedor_assoc = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)

class Produto(models.Model):
    custo_de_producao = models.FloatField(default=0.0)
    preco_de_venda = models.FloatField(default=0.0)
    nome = models.CharField(max_length=50,default='')
    mat_prima_necessaria = models.ForeignKey(Materia_Prima, on_delete=models.CASCADE)

class Cliente(Pessoa_Juridica):
    pass

class Compras(models.Model):
    cnpj_cliente = models.CharField(max_length=14, default='')
    cnpj_filial = models.CharField(max_length=14, default='')
    nome_produto = models.CharField(max_length=50, default='')
    qtd_produto = models.IntegerField(default=0)
