from translate import Translator
translator = Translator(to_lang="vi")
translation = translator.translate("How can i help you")
print(translation)