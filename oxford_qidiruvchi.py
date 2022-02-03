from googletrans import Translator
translator = Translator()
import requests
import json

app_id = '4e00dbe8'
app_key = 'ccd0da328fea015f2266ec7698a30283	'

language = "en-gb"
# word_id = "example"
# url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()
# r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})

# res = r.json()

# print('Res: ', res)
# print('_______________________________________________\nResKeys: ', res.keys())

# print('_______________________________________________\nResults: ', res['results'][0])
# print('_______________________________________________\nResultsKeys: ', res['results'][0].keys())

# # 'lexicalEntries'
# print('_______________________________________________\nlexicalEntries: ', res['results'][0]['lexicalEntries'][0])
# print('_______________________________________________\nlexicalEntriesKeys: ', res['results'][0]['lexicalEntries'][0].keys())

# # entries
# print('_______________________________________________\nentries: ', res['results'][0]['lexicalEntries'][0]['entries'][0])
# print('_______________________________________________\nentriesKeys: ', res['results'][0]['lexicalEntries'][0]['entries'][0].keys())


# # pronunciations
# print('_______________________________________________\npronunciations: ', res['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0])
# print('_______________________________________________\npronunciationsKeys: ', res['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0].keys())


# # senses
# print('_______________________________________________\nsenses: ', res['results'][0]['lexicalEntries'][0]['entries'][0]['senses'])
# print('_______________________________________________\nsenses-Len: ', len(res['results'][0]['lexicalEntries'][0]['entries'][0]['senses']))
# print('_______________________________________________\nsensesKeys: ', res['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0].keys())

# for i in range(len(res['results'][0]['lexicalEntries'][0]['entries'][0]['senses'])):
#     print(f'_______________________________________________\ndefinitions{i+1}: ', res['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][i]['definitions'][0])
#     print(f'_______________________________________________\nshortDefinitions{i+1}: ', res['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][i]['shortDefinitions'][0])
    
    
    
    


def getDefinition(word_id):
    
    url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()
    r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
    res = r.json()
    
    if 'error' in res.keys():
        return False
    
    output = {}
    senses = res['results'][0]['lexicalEntries'][0]['entries'][0]['senses']
    definitions = []
    
    for sense in senses:
        definitions.append(f"👉 {sense['definitions'][0]}")
    
    output['definitions'] = '\n'.join(definitions)
    
    if res['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0].get('audioFile'):
        output['audio'] = res['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0]['audioFile']
    
    return output

# a = getDefinition('apple')
# print(a)

# def tilmoch(ws):
#     lang = translator.detect(f'{ws}').lang
#     print('Lang: ', lang)
#     if ws.split() > 2:
#         des = 'uz' if lang == 'en' else 'en'
#         # a = translator.translate(ws, des).text
#         a = 'salom'
    
#     # else:
#     #     a = getDefinition(ws)
        
#     return a

