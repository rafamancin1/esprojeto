from django.db import models
from django.utils import timezone

# Create your models here.
class Filial(models.Model):
    cnpjFilial = models.CharField(max_length=14)
    endereco = models.CharField(max_length=100)
    qtdFunc = models.IntegerField(default=0)

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
        out = self.nome_P + " " + self.cpf_P + " " + str(self.salario_Func)
        return out

    class Meta:
        abstract = True

class Contrato(Funcionario):
    data_validade = models.DateTimeField('data de validade', default=timezone.now())

class Adm_Local(Funcionario):
    senha_adm = models.CharField(max_length=16,default='')
    def __str__(self):
        return super().__str__(self)

class Tecnico(Funcionario):
    areaAtuacao = models.CharField(max_length=20,default='')
    def __str__(self):
        return super().__str__() + " " + self.areaAtuacao + "\n"

class Representante(Funcionario):
    estado_atuacao = models.CharField(max_length=50,default='')
    senha_repr = models.CharField(max_length=16,default='')

    def __str__(self):
        return super().__str__() + " " + self.estado_atuacao + "\n"

class Fornecedor(Pessoa_Juridica):
    pass

class Materia_Prima(models.Model):
    nome_mat = models.CharField(max_length=50,default='')
    custo_mat = models.FloatField(default=0.0)
    fornecedor_assoc = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)

class Produto(models.Model):
    custo_de_producao = models.FloatField(default=0.0)
    preco_de_venda = models.FloatField(default=0.0)
    nome = models.CharField(max_length=50,default='')
    mat_prima_necessaria = models.ForeignKey(Materia_Prima, on_delete=models.CASCADE)

    def __str__(self):
        out = self.nome + " " + str(self.custo_de_producao) + " " + str(self.preco_de_venda) + "\n"
        return out

class Lote_Produto(models.Model):
    qtd_produtos = models.IntegerField(default=0)
    data_validade = models.DateTimeField('data de validade', default=timezone.now())
    data_producao = models.DateTimeField('data de produção', default=timezone.now())
    preco_lote = models.FloatField()
    produto_assoc = models.ForeignKey(Produto, on_delete=models.CASCADE)

class Cliente(Pessoa_Juridica):
    pass
