from django import template

register = template.Library()


@register.simple_tag
def buttons_action():
    return ["Editar", "Delelar", "Adicionar", "Cancelar", "Salvar"]


@register.simple_tag
def clients_legend():
    return {
        "title": "Legendas",
        "cpf": "Pessoas Físicas (CPF)",
        "cnpj": "Pessoas Jurídicas (CNPJ)",
    }
