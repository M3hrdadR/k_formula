from k_formula import start_getting_formula
from k_formula import start_getting_graph


def start():
    print("1. K-formula to graph \n 2. Graph to K-formula \n")
    a = input()
    if a == '1':
        start_getting_formula()
    elif a == '2':
        start_getting_graph()




