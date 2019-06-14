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
