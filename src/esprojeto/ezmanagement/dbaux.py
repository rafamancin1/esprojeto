from .models import *

def consultar_filial(cnpj):
    filial = None
    try:
        filial = Filial.objects.get(cnpjFilial=cnpj)
    except Filial.DoesNotExist:
        pass
    return filial

def consultar_funcionario(cpf):
    func = None
    try:
        func = Adm_Local.objects.get(cpf_P=cpf)
    except Adm_Local.DoesNotExist:
        pass
    try:
        func = Tecnico.objects.get(cpf_P=cpf)
    except Tecnico.DoesNotExist:
        pass
    return func

def lista_funcionarios():
    func = []
    try:
        for e in Adm_Local.objects.all():
            func.append(e)
    except Adm_Local.DoesNotExist:
        pass
    try:
        for e in Tecnico.objects.all():
            func.append(e)
    except Tecnico.DoesNotExist:
        pass
    return func

def lista_produtos():
    try:
        return Produto.objects.all()
    except:
        return []
def lista_fornecedores():
    try:
        return Fornecedor.objects.all()
    except:
        return []
