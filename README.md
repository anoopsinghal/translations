# translations
 This translation repo has sample code for several servers working together to translate sentences.
 
 Supported languages are : English, German, French and Spanish
 
 model-server:
 
 This is a flask server which will return translations. It uses flan-t5-large model for translating text.
 
 URL : /translations
 Method : POST
 Input Sample: {"fromLang":"en", "fromStr":"I am God", "toLang":"de"}
 Output Sample: {"fromLang":"en", "fromStr":"I am God", "toLang":"de", "toStr":"Ich bin Gott"}
 
