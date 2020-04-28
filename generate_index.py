coding: 'utf-8'
from horoscope import generate_prophecies
from datetime import datetime as dt

def generate_page(head,body):
    page='<html>'+head+body+'</html>'
    return page

def generate_head(title):
    head='<meta charset = "utf-8">'+'<title>'+title+'</title>'
    return    '<head>'+head+'</head>'

def generate_body(header, paragraphs,link,link_name):
    body='<h1>'+header+'</h1>'
    for p in paragraphs:
        body +='<p>'+p+'</p>'
    body +='<p>'+add_link(link,link_name)+'</p>'
    return '<body>'+body+'</body>'

def save_page(title,header,paragraphs,link,link_name,output='index.html'):
    fp=open(output,'w',encoding='utf-8')
    page=generate_page(head=generate_head(title),body=generate_body(header,paragraphs,link,link_name))
    print(page,file=fp)
    fp.close()
def add_link(link,link_name):
    link=f'<a href="{link}">{link_name}</a>'
    return link

today = dt.now().date()
link_a='about.html'
name = 'О реализации'
save_page("Гороскоп на сегодня ",header=" Что день "+str(today)+' готовит ',paragraphs=generate_prophecies(),link=link_a, link_name=name)




