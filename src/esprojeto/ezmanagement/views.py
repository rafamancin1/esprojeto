from django.shortcuts import render
from .models import *
from .forms import *
from .dbaux import *

#Varíaveis de estado da sessão

MARGEM_LUCRO = 1.5
# Create your views here.
def index(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']
            request.session['nomeFunc'] = email
            try:
                func = Adm_Local.objects.get(email_P=email, senha_adm=senha)
                request.session['CNPJ_FILIAL'] = func.filialAssociada.cnpjFilial
                return render(request, 'ezmanagement/menu_inicial.html', {'nomeFunc' : email})
            except Adm_Local.DoesNotExist:
                try:
                    func = Representante.objects.get(email_P=email, senha_repr=senha)
                    request.session['CNPJ_FILIAL'] = func.cnpjFilial
                    return render(request, 'ezmanagement/menu_inicial.html', {'nomeFunc' : email})
                except Representante.DoesNotExist:
                    form = LoginForm()
                    return render(request, 'ezmanagement/login_erro.html', {'form' : form})
    else:
        form = LoginForm()
        return render(request, 'ezmanagement/index.html', {'form' : form})

def menu_inicial(request):
    return render(request, 'ezmanagement/menu_inicial.html', {'nomeFunc' : request.session['nomeFunc']})

def cadastro(request):
    return render(request, 'ezmanagement/menu_cadastro.html')

def remocao(request):
    return render(request, 'ezmanagement/menu_remocao.html')

def alteracao(request):
    return render(request, 'ezmanagement/menu_alteracao.html')

def consulta(request):
    return render(request, 'ezmanagement/menu_consulta.html')

def relatorio(request):

    listaFunc = lista_funcionarios()
    listaProdutos = lista_produtos()
    listaFornecedores = lista_fornecedores()
    filial = consultar_filial(request.session['CNPJ_FILIAL'])

    out = "<h5>Informações sobre a filial</h5>"
    out += "<table style=\"border-collapse: separate; border-spacing: 10px;\">"
    out += "<tr><td>CNPJ</td><td>Endereço</td><td>Nº de funcionários</td></tr>"
    out += "<tr><td>"+filial.cnpjFilial+"</td><td>"+filial.endereco+"</td><td>"+str(filial.qtdFunc)+"</td></tr>"
    out += "</table><br><br>"

    out += "<h5>Lista de funcionários</h5>"
    out += "<table border=1>"
    #out += "Nome | CPF | Salário<br>"
    out += "<tr><td>Nome</td><td>CPF</td><td>Salário</td></tr>"
    for f in listaFunc:
        out += "<tr><td>"+f.nome_P+"</td><td>"+f.cpf_P+"</td><td>"+str(f.salario_Func)+"</td></tr>"
    out += "</table><br><br>"

    out += "<h5>Lista de produtos</h5>"
    out += "<table border=1>"
    out += "<tr><td>Nome</td><td>Preço de venda</td></tr>"
    for p in listaProdutos:
        out += "<tr><td>"+p.nome+"</td><td>"+str(p.preco_de_venda)+"</td></tr>"
    out += "</table><br><br>"

    out += "<h5>Lista de Fornecedores</h5>"
    out += "<table border=1>"
    out += "<tr><td>Nome</td><td>CNPJ</td></tr>"
    for f in listaFornecedores:
        out += "<tr><td>"+f.nome_P+"</td><td>"+f.cnpj_P+"</td></tr>"
    out += "</table><br>"
    return render(request, 'ezmanagement/relatorio.html', {'out' : out})

def cadastro_funcionario(request):
    return render(request, "ezmanagement/cadastro_funcionario.html")

def cadastro_tecnico(request):
    if request.method == "POST":
        form = CadastroTecForm(request.POST)
        if form.is_valid():
            func = Tecnico(**form.cleaned_data)
            filialAssoc = consultar_filial(request.session['CNPJ_FILIAL'])
            if filialAssoc != None:
                func.filialAssociada = filialAssoc
                filialAssoc.qtdFunc += 1
                filialAssoc.save()
                func.save()
                del form.cleaned_data['areaAtuacao']
                contrato = Contrato(**form.cleaned_data)
                contrato.filialAssociada = filialAssoc
                contrato.save()
                return render(request, 'ezmanagement/cadastro_sucesso.html')
            else:
                return render(request, 'ezmanagement/cadastro_erro.html')
        else:
            return render(request, 'ezmanagement/cadastro_erro.html')
    else:
        form = CadastroTecForm()
        return render(request, 'ezmanagement/cadastro_tecnico.html', {'form' : form})

def cadastro_representante(request):
    pass

def cadastro_engenheiro(request):
    pass

def cadastro_cliente(request):
    if request.method == "POST":
        form = CadastroPessoaJuridicaForm(request.POST)
        if form.is_valid():
            cliente = Cliente(**form.cleaned_data)
            filialAssoc = consultar_filial(request.session['CNPJ_FILIAL'])
            if filialAssoc != None:
                cliente.filialAssociada = filialAssoc
                cliente.save()
                return render(request, 'ezmanagement/cadastro_sucesso.html')
            else:
                return render(request, 'ezmanagement/cadastro_erro.html')
    else:
        form = CadastroPessoaJuridicaForm()
        return render(request, 'ezmanagement/cadastro_cliente.html', {'form' : form})

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

def alteracao_cliente(request):
    if request.method == "POST":
        form = AlteracaoClienteForm(request.POST)
        if form.is_valid():
            cnpj = form.cleaned_data["cnpj_P"]
            campo = form.cleaned_data["campo"]
            novoValor = form.cleaned_data["novoValor"]
            cliente = consultar_cliente(cnpj)
            if cliente == None:
                return render(request, 'ezmanagement/alteracao_erro.html')
            if campo == "Nome":
                cliente.nome_P = novoValor
            elif campo == "Endereço":
                cliente.endereco_P = novoValor
            elif campo == "Telefone":
                cliente.endereco_P = novoValor
            else:
                return render(request, 'ezmanagement/alteracao_erro.html')
            cliente.save()
            return render(request, 'ezmanagement/alteracao_sucesso.html')
        else:
            return render(request, 'ezmanagement/alteracao_erro.html')
    else:
        form = AlteracaoClienteForm()
        return render(request, 'ezmanagement/alteracao_cliente.html', {'form' : form})

def alteracao_materia_prima(request):
    global MARGEM_LUCRO
    if request.method == "POST":
        form = AlteracaoMateriaForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data["nome_mat"]
            custo = form.cleaned_data["custo_mat"]
            mat = consultar_materia(nome)
            if mat != None:
                for p in lista_produtos():
                    if p.mat_prima_necessaria == mat:
                        p.custo_de_producao += custo - mat.custo_mat
                        p.preco_de_venda = p.custo_de_producao*MARGEM_LUCRO
                        for lot in lista_lotes():
                            if lot.produto_assoc == p:
                                lot.preco_lote = lot.qtd_produtos * p.preco_de_venda
                                lot.save()
                        p.save()
                mat.custo_mat = custo
                mat.save()
                return render(request, 'ezmanagement/alteracao_sucesso.html')
            else:
                return render(request, 'ezmanagement/alteracao_erro.html')
    else:
        form = AlteracaoMateriaForm()
        return render(request, 'ezmanagement/alteracao_materia_prima.html', {'form' : form})


def remocao_funcionario(request):
    if request.method == "POST":
        form = ConsultaFisicaForm(request.POST)
        if form.is_valid():
            cpf = form.cleaned_data["cpf_P"]
            func = consultar_funcionario(cpf)
            contrato = consultar_contrato(cpf)
            if func != None:
                filialAssoc = func.filialAssociada
                filialAssoc.qtdFunc -= 1
                filialAssoc.save()
                func.delete()
                contrato.delete()
                return render(request, 'ezmanagement/remocao_sucesso.html')
            else:
                return render(request, 'ezmanagement/remocao_erro.html')
    else:
        form = ConsultaFisicaForm()
        return render(request, 'ezmanagement/remocao_funcionario.html', {'form' : form})

def remocao_cliente(request):
    if request.method == "POST":
        form = ConsultaJuridicaForm(request.POST)
        if form.is_valid():
            cnpj = form.cleaned_data["cnpj_P"]
            cliente = consultar_cliente(cnpj)
            if cliente != None:
                cliente.delete()
                return render(request, 'ezmanagement/remocao_sucesso.html')
            else:
                return render(request, 'ezmanagement/remocao_erro.html')
    else:
        form = ConsultaJuridicaForm()
        return render(request, 'ezmanagement/remocao_cliente.html', {'form' : form})

def consulta_funcionario(request):
    if request.method == "POST":
        form = ConsultaFisicaForm(request.POST)
        if form.is_valid():
            cpf = form.cleaned_data["cpf_P"]
            func = consultar_funcionario(cpf)
            if func != None:
                return render(request, 'ezmanagement/informacoes_consulta.html', {'info' : func})
            else:
                return render(request, 'ezmanagement/consulta_erro.html')

    else:
        form = ConsultaFisicaForm()
        return render(request, 'ezmanagement/consulta_funcionario.html', {'form' : form})

def consulta_cliente(request):
    if request.method == "POST":
        form = ConsultaJuridicaForm(request.POST)
        if form.is_valid():
            cnpj = form.cleaned_data["cnpj_P"]
            cliente = consultar_cliente(cnpj)
            if cliente != None:
                return render(request, 'ezmanagement/informacoes_consulta.html', {'info' : cliente})
            else:
                return render(request, 'ezmanagement/consulta_erro.html')

    else:
        form = ConsultaJuridicaForm()
        return render(request, 'ezmanagement/consulta_cliente.html', {'form' : form})
