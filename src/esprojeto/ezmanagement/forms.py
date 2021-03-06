from django import forms

class LoginForm(forms.Form):
    email = forms.CharField(label="E-mail", max_length=50)
    senha = forms.CharField(label="Senha", max_length=16)

class CadastroPessoaForm(forms.Form):
    nome_P = forms.CharField(label="Nome", max_length=50)
    telefone_P = forms.CharField(label="Telefone", max_length=20)
    endereco_P = forms.CharField(label="Endereço", max_length=100)
    email_P = forms.CharField(label="E-mail", max_length=50)

class CadastroPessoaJuridicaForm(CadastroPessoaForm):
    cnpj_P = forms.CharField(label="CNPJ", max_length=11)

class CadastroPessoaFisicaForm(CadastroPessoaForm):
    cpf_P = forms.CharField(label="CPF", max_length=11)

class CadastroFuncForm(CadastroPessoaFisicaForm):
    cnpj_filial = forms.CharField(label="CNPJ da filial", max_length=14)
    dataContratacao_Func = forms.DateTimeField(label="Data de contratação")
    salario_Func = forms.FloatField(label="Salário")

class CadastroContratoForm(CadastroFuncForm):
    data_validade = forms.DateTimeField(label="Data de validade do contrato")

class CadastroContratoTecnicoForm(CadastroContratoForm):
    area_atuacao = forms.CharField(label="Área de atuação", max_length=50)

class ConsultaFisicaForm(forms.Form):
    cpf_P = forms.CharField(label="CPF", max_length=11)

class ConsultaJuridicaForm(forms.Form):
    cnpj_P = forms.CharField(label="CNPJ", max_length=14)

class AlteracaoForm(forms.Form):
    campo = forms.CharField(label="Informe o campo que deseja alterar", max_length=50)
    novoValor = forms.CharField(label="Informe o novo valor deste campo", max_length=100)

class AlteracaoFuncForm(forms.Form):
    campo = forms.CharField(label="Informe o campo que deseja alterar", max_length=50)
    novoValor = forms.CharField(label="Informe o novo valor deste campo", max_length=100)

class AlteracaoClienteForm(forms.Form):
    campo = forms.CharField(label="Informe o campo que deseja alterar", max_length=50)
    novoValor = forms.CharField(label="Informe o novo valor deste campo", max_length=100)

class AlteracaoMateriaForm(forms.Form):
    nome_mat = forms.CharField(label="Nome da matéria prima", max_length=50)
    custo_mat = forms.FloatField(label="Novo custo da matéria prima")
