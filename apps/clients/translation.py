from modeltranslation.translator import translator, TranslationOptions
from .models import ClientModel


class NewsClientModel(TranslationOptions):
    fields = ("obs",)
    required_languages = ("pt-br", "en")


translator.register(ClientModel, NewsClientModel)
