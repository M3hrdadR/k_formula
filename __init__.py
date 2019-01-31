from k_formula import start_getting_formula
from k_formula import start_getting_graph


def start():
    print("1. K-formula to graph \n2. Graph to K-formula")
    a = input()
    if a == '1':
        start_getting_formula()
    elif a == '2':
        start_getting_graph()


start()



