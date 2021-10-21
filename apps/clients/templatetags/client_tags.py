from django import template

register = template.Library()


@register.simple_tag
def clients_legend():
    return {
        "cpf": "Pessoas Físicas (CPF)",
        "cnpj": "Pessoas Jurídicas (CNPJ)",
    }


@register.simple_tag
def client_mask_cpf_cnpj(obj):
    if obj == "cpf":
        return "000.000.000-00"
    elif obj == "cnpj":
        return "00.000.000/0000-00"
    return ""


@register.simple_tag
def client_html_obj_disable(obj):
    if obj is True:
        return "disabled"
    return ""
