from django.test import TestCase
from .models import *

# Create your tests here.
class TecnicoTestCase(TestCase):
    def setUp(self):
        Filial.objects.create(cnpjFilial="12345678901234", endereco="Rua 0")
        filial = Filial.objects.get(cnpjFilial="12345678901234")
        Tecnico.objects.create(nome_P="Jose", cpf_P="12345", salario_Func=1000, filialAssociada=filial,
            areaAtuacao="Nada")

    def test_string_tecnico(self):
        tec = Tecnico.objects.get(nome_P="Jose")
        self.assertEqual(str(tec), "Jose 12345 1000.0 Nada\n")

class ProdutoTestCase(TestCase):
    def setUp(self):
        Filial.objects.create(cnpjFilial="12345678901234", endereco="Rua 0")
        filial = Filial.objects.get(cnpjFilial="12345678901234")
        Fornecedor.objects.create(nome_P="Jose", cnpj_P = "12345", filialAssociada=filial)
        forn = Fornecedor.objects.get(nome_P="Jose")
        Materia_Prima.objects.create(nome_mat="Pau", custo_mat=100.0, fornecedor_assoc=forn)
        mat = Materia_Prima.objects.get(nome_mat="Pau")
        Produto.objects.create(nome="Pau de sebo", preco_de_venda=300.0, custo_de_producao=200.0, mat_prima_necessaria=mat)

    def test_string_produto(self):
        prod = Produto.objects.get(nome="Pau de sebo")
        self.assertEqual(str(prod), "Pau de sebo 200.0 300.0\n")
