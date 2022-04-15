from pyfacebook import Api
from json2html import *
import config
import csv

api = Api(app_id=config.app_id, app_secret=config.app_secret,
          long_term_token=config.long_term_token)
api.get_token_info()
api.get_page_info(username=config.username)

data = api.get_page_posts(page_id=config.page_id,
                          count=None, limit=100, return_json=True)

with open('fbposts.csv', mode='w', encoding='utf-8', newline="") as csv_file:
    write = csv.writer(csv_file, delimiter=';', quotechar="'",
                       quoting=csv.QUOTE_MINIMAL)
    write.writerow(['ID', 'TEXTO', 'IMAGEM', 'URL', 'DATA', 'COMENTARIOS', 'REAÇÕES',
                    'SHARES', 'ANGRY', 'HAHA', 'LIKE', 'LOVE', 'SAD', 'THANKFUL', 'WOW'])
    for itens in data:
        # try:
        write.writerow([
            itens['id'],
            ('-' if 'message' not in itens else itens['message'].replace(
                '\n', ' ').replace('\r', '').replace(';', '.')),
            ('-' if 'picture' not in itens else itens['picture']),
            itens['permalink_url'],
            itens['created_time'].replace('T', ' ').replace('+0000', ''),
            str(itens['comments']['summary']['total_count']),
            str(itens['reactions']['summary']['total_count']),
            ('0' if 'shares' not in itens else str(itens['shares']['count'])),
            str(itens['angry']['summary']['total_count']),
            str(itens['haha']['summary']['total_count']),
            str(itens['like']['summary']['total_count']),
            str(itens['love']['summary']['total_count']),
            str(itens['sad']['summary']['total_count']),
            str(itens['thankful']['summary']['total_count']),
            str(itens['wow']['summary']['total_count'])
        ])
        # except:
        #     print("Error parsing data")

# print('Post', end='\t')
# print('Data', end='\t')
# print('Angry', end='\t')
# print('Like', end='\t')
# print('Love', end='\t')
# print('haha', end='\t')
# print('sad', end='\t')
# print('Wow', end='\t')
# print('Reaction', end='\t')


# for itens in data:
#     print(itens['id'], end="\t")
#     print(itens['message'], end="\t")
#     print(itens['picture'], end="\t")
#     print(itens['permalink_url'], end="\t")
#     print(itens['created_time'], end="\t")
#     print(str(itens['comments']['summary']['total_count']))
#     print(str(itens['reactions']['summary']['total_count']))
#     print(str(itens['angry']['summary']['total_count']), end="\t")
#     print(str(itens['haha']['summary']['total_count']), end="\t")
#     print(str(itens['like']['summary']['total_count']), end="\t")
#     print(str(itens['love']['summary']['total_count']), end="\t")
#     print(str(itens['sad']['summary']['total_count']), end="\t")
#     print(str(itens['thankful']['summary']['total_count']), end="\t")
#     print(str(itens['wow']['summary']['total_count']), end="\t")
