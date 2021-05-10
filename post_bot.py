#!/home/robson/Documentos/Códigos/python_steem_bots/venv_steem/bin/python

from steem import Steem

from .settings import accounts as accounts

import os
import time


base_posts_path = os.path.dirname(os.path.abspath(__file__))



posts_list = os.listdir(os.path.join( base_posts_path, "posts/"))

for index, post in enumerate(posts_list):
    account_index = index % len(accounts)
    account_chosen = accounts[account_index]['name']
    post_path = os.path.join(base_posts_path,"posts" ,post)

    with open(post_path, 'r') as post_file:
        body  = post_file.read()
        title = post.split('.')[0]
        
        # print({
        #     'title': post.split('.')[0],
        #     'account': account_chosen,
        #     'body': body
        #     })

    tags = accounts[account_index]['tags']

    try:
        accounts[account_index]['steem'].commit.post(title, 
                                                        body, 
                                                        account_chosen,
                                                        tags=tags)
        print(f"Post {title} criado com sucesso pela conta {account_chosen}")
    except Exception as e:
        print(f"Erro ao postar devido a: {e}")
    time.sleep(600)


#for i in range(1):
#    for account in accounts:

