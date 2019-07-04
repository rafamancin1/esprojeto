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

def consultar_cliente(cnpj):
    cliente = None
    try:
        cliente = Cliente.objects.get(cnpj_P=cnpj)
    except Cliente.DoesNotExist:
        pass
    return cliente

def consultar_materia(nome):
    materia = None
    try:
        materia = Materia_Prima.objects.get(nome_mat=nome)
    except Materia.DoesNotExist:
        pass
    return materia

def consultar_contrato(cpf):
    contrato = None
    try:
        contrato = Contrato.objects.get(cpf_P=cpf)
    except Contrato.DoesNotExist:
        pass
    return contrato

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

def lista_lotes():
    try:
        return Lote_Produto.objects.all()
    except:
        return []

def lista_fornecedores():
    try:
        return Fornecedor.objects.all()
    except:
        return []

def alterar_obj(obj_alt, campo, novoValor):
    setattr(obj_alt, campo, novoValor)
    obj_alt.save()
