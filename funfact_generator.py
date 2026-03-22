import requests
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *
from pprint import PrettyPrinter

printer = PrettyPrinter()
put_text("Welcome to Fax Check web")
facts=[]
Url= f"https://uselessfacts.jsph.pl/random.json?language=en"

def get_data():
    data = requests.get(Url).json()['text']
    facts.append(data)
    clear('display')
    with use_scope('display'):
        for fact in facts:
            put_text(fact)
        put_row([
        None,
        put_button(label="Click",color='success',onclick=get_data),
        None
        ], size='1fr auto 1fr') 
    



put_scope('display')
get_data()





