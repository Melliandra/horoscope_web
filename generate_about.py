from horoscope import times,advices,promises
from generate_index import add_link, generate_page
def generate_head(title):
    title = f'<meta charset ="utf-8"><title>{title}</title>'
    return title
def generate_body(header,link,list1_name,list1,list2_name,list2,list3_name,list3,link_pic):
    body=f'<h1>{header}</h1>'
    body +=f'<p>{add_pic(link_pic)}</p>'
    body += f'<p>{add_list(list1,list1_name)}</p>'
    body += f'<p>{add_list(list2, list2_name)}</p>'
    body += f'<p>{add_list(list3, list3_name)}</p>'
    body += f'<p>{add_link(link,link_name="На главную")}</p>'
    return body

def add_pic(link):
    pic=f'<img src="{link}" weight=100, hight=100>'
    return pic
def add_list(il,name):
    list=f'<ul>{name}'
    for i in il:
        list +=f'<li>{i}</li>'
    list +='</ul>'
    return list

def save_page(title,header,link,list1_name,list1,list2_name,list2,list3_name,list3,link_pic,output = 'about.html'):
    fp=open(output,'w',encoding='utf-8')
    page=generate_page(head=generate_head(title),body=generate_body(header,link,list1_name,list1,list2_name,list2,list3_name,list3,link_pic))
    print(page,file=fp)
    fp.close()

link_a='index.html'
name = 'О реализации'
pic='horoscope.jpg'
save_page("О чем все это ",'Как это работает:',link_a,list1_name = 'Времена дня',list1=times,list2_name ="Глаголы:",list2 =advices,list3_name="Предсказания:",list3 =promises,link_pic=pic)