from django import forms

class LoginForm(forms.Form):
    email = forms.CharField(label="E-mail", max_length=50)
    senha = forms.CharField(label="Senha", max_length=16)

class CadastroFuncForm(forms.Form):
    nome_P = forms.CharField(label="Nome", max_length=50)
    telefone_P = forms.CharField(label="Telefone", max_length=20)
    endereco_P = forms.CharField(label="Endereço", max_length=100)
    email_P = forms.CharField(label="E-mail", max_length=50)
    cnpjFilial = forms.CharField(label="CNPJ da filial associada", max_length=14)
    cpf_P = forms.CharField(label="CPF", max_length=11)
    dataContratacao_Func = forms.DateTimeField(label="Data de contratação")
    salario_Func = forms.FloatField(label="Salário")

class CadastroTecForm(CadastroFuncForm):
    areaAtuacao = forms.CharField(label="Área de atuação")

class ConsultaFuncForm(forms.Form):
    cpf_P = forms.CharField(label="CPF do funcionário", max_length=11)

class AlteracaoFuncForm(forms.Form):
    cpf_P = forms.CharField(label="CPF do funcionário", max_length=11)
    campo = forms.CharField(label="Informe o campo que deseja alterar", max_length=50)
    novoValor = forms.CharField(label="Informe o novo valor deste campo", max_length=100)
