from django.db import models

# Create your models here.
class Filial(models.Model):
    cnpjFilial = models.CharField(max_length=14)
    endereco = models.CharField(max_length=100)
    qtdFunc = models.IntegerField()

class Pessoa(models.Model):
    nome_P = models.CharField(max_length=50, default='')
    telefone_P = models.CharField(max_length=20)
    endereco_P = models.CharField(max_length=100)
    email_P = models.CharField(max_length=50)
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
    dataContratacao_Func = models.DateTimeField('data de contratação')
    salario_Func = models.FloatField()

    def __str__(self):
        return str(self.__dict__)

    class Meta:
        abstract = True

class Adm_Local(Funcionario):
    senha_adm = models.CharField(max_length=16)

class Tecnico(Funcionario):
    areaAtuacao = models.CharField(max_length=20,default='')
    def __str__(self):
        return str(self.__dict__)
