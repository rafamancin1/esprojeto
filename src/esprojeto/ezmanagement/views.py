from django.shortcuts import render
from .models import *
from .forms import *
from .consulta import *

# Create your views here.
def index(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']
            context = {'nomeFunc' : email}
            try:
                func = Adm_Local.objects.get(email_P=email, senha_adm=senha)
                return render(request, 'ezmanagement/menu_inicial.html', context)
            except Adm_Local.DoesNotExist:
                form = LoginForm()
                return render(request, 'ezmanagement/login_erro.html', {'form' : form})
    else:
        form = LoginForm()
        return render(request, 'ezmanagement/index.html', {'form' : form})

def menu_inicial(request):
    return render(request, 'ezmanagement/menu_inicial.html')

def cadastro(request):
    return render(request, 'ezmanagement/menu_cadastro.html')

def remocao(request):
    return render(request, 'ezmanagement/menu_remocao.html')

def alteracao(request):
    return render(request, 'ezmanagement/menu_alteracao.html')

def consulta(request):
    return render(request, 'ezmanagement/menu_consulta.html')

def cadastro_funcionario(request):
    return render(request, "ezmanagement/cadastro_funcionario.html")

def cadastro_tecnico(request):
    if request.method == "POST":
        form = CadastroTecForm(request.POST)
        if form.is_valid():
            func = Tecnico(**form.cleaned_data)
            cnpjAssoc = form.cleaned_data["cnpjFilial"]
            filialAssoc = consultar_filial(cnpjAssoc)
            if filialAssoc != None:
                func.filialAssociada = filialAssoc
                func.save()
                return render(request, 'ezmanagement/cadastro_sucesso.html')
            else:
                return render(request, 'ezmanagement/cadastro_erro.html')
        else:
            return render(request, 'ezmanagement/cadastro_erro.html')
    else:
        form = CadastroFuncForm()
        return render(request, 'ezmanagement/cadastro_funcionario.html', {'form' : form})

def cadastro_representante(request):
    pass

def cadastro_engenheiro(request):
    pass

def alteracao_funcionario(request):
    if request.method == "POST":
        form = AlteracaoFuncForm(request.POST)
        if form.is_valid():
            cpf = form.cleaned_data["cpf_P"]
            campo = form.cleaned_data["campo"]
            novoValor = form.cleaned_data["novoValor"]
            func = consultar_funcionario(cpf)
            if func == None:
                return render(request, 'ezmanagement/alteracao_erro.html')
            if campo == "Nome":
                func.nome_P = novoValor
            elif campo == "Endereço":
                func.endereco_P = novoValor
            elif campo == "Telefone":
                func.endereco_P = novoValor
            else:
                return render(request, 'ezmanagement/alteracao_erro.html')
            func.save()
            return render(request, 'ezmanagement/alteracao_sucesso.html')
        else:
            return render(request, 'ezmanagement/alteracao_erro.html')
    else:
        form = AlteracaoFuncForm()
        return render(request, 'ezmanagement/alteracao_funcionario.html', {'form' : form})


def remocao_funcionario(request):
    if request.method == "POST":
        form = ConsultaFuncForm(request.POST)
        if form.is_valid():
            cpf = form.cleaned_data["cpf_P"]
            func = consultar_funcionario(cpf)
            if func != None:
                func.delete()
                return render(request, 'ezmanagement/remocao_sucesso.html')
            else:
                return render(request, 'ezmanagement/remocao_erro.html')
    else:
        form = ConsultaFuncForm()
        return render(request, 'ezmanagement/remocao_funcionario.html', {'form' : form})

def consulta_funcionario(request):
    if request.method == "POST":
        form = ConsultaFuncForm(request.POST)
        if form.is_valid():
            cpf = form.cleaned_data["cpf_P"]
            func = consultar_funcionario(cpf)
            if func != None:
                return render(request, 'ezmanagement/informacoes_funcionario.html', {'func' : func})
            else:
                return render(request, 'ezmanagement/consulta_erro.html')

    else:
        form = ConsultaFuncForm()
        return render(request, 'ezmanagement/consulta_funcionario.html', {'form' : form})
