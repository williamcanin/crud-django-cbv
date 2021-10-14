from django import template

register = template.Library()


@register.simple_tag
def buttons_action():
    return ["Editar", "Delelar", "Adicionar", "Cancelar", "Salvar"]
