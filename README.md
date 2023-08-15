# Translation Repo
This repo demonstrates power of coding to an api and how coding to an api enables us to have loose connections between components, promoting plug and play architecture.

This repo implements a simple translation service. User can input English text and the service will return translations in French, German and Spanish. It will also save these translations into a db of choice.

## UI Stack
This repos contains basic ui implementation for 
- Angular
- React Native

Due to limitation of these technologies, the url for the translation server is set in places in code as needed by the ui stack.

## Servers and apis for translation stack
### Translation Server
This server is called from ui layer to translate and store strings in various languages.

It will call a model server identified by 'MODEL_SERVER_API_URL' environment variable and then store the original as well as translation into a db accesible through 'DB_SERVER_API_URL' environment variable.

##### Environment Variable Identifier
**TRANSLATION_SERVER_API_URL**
##### API
**Translate**
*POST* */translate*
JSON Posted:
    `fromLang` : Two character language code. Must be en, de, fr or es
    `fromStr`  : String to translate
   `toLang`   : language code for the translation
   
JSON Returned:
    `fromLang` : Two character language code. Must be en, de, fr or es
    `fromStr`  : String to translate
    `toLang`   : language code for the translation
    `toStr`    : Translated String in specified language
        
### Model Server      
This server is called from the translation server to translate an input string in a language to another language.  

This server uses flan_t5_large server for translation.

##### Environment Variable Identifier
**MODEL_SERVER_API_URL**
##### API
**Translate**
*POST* */translate*
JSON Posted:
    `fromLang` : Two character language code. Must be en, de, fr or es
    `fromStr`  : String to translate
   `toLang`   : language code for the translation
   
JSON Returned:
    `fromLang` : Two character language code. Must be en, de, fr or es
    `fromStr`  : String to translate
    `toLang`   : language code for the translation
    `toStr`    : Translated String in specified language
        

### DB Server      
This server is called from the translation server to store translations between languages. It will be passed both the original and translated strings. It will store both the strings separately, linking them both through md5 of original string

##### Environment Variable Identifier
**DB_SERVER_API_URL**
##### API
**Translate**
*POST* */save-translation*
JSON Posted:
    `fromLang` : Two character language code. Must be en, de, fr or es
    `fromStr`  : String to translate
    `toLang`   : language code for the translation
    `toStr`    : Translated String in specified language
   
JSON Returned:
    `fromLang` : Two character language code. Must be en, de, fr or es
    `fromStr`  : String to translate
    `toLang`   : language code for the translation
    `toStr`    : Translated String in specified language
        