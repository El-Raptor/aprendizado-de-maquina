"""
    Nome - RGA:
    Fábio Holanda Saraiva Júnior - 2015.1905.006-2
    Felipe Salles Lopez - 2016.1907.032-4
    Lucas Avanzi - 2016.1907.024-3
    Lucas Antonio dos Santos - 2016.1907.013-8
"""


import csv

def read_input_file(file_path):
    open_file = open(file_path, "r")
    reader = csv.reader(open_file)
    data = list(reader)

    return data


if __name__ == '__main__':
    #print(read_input_file("./iris.data"))

    #TODO: ler 10 datasets
    
    
    #TODO: aplicar os cinco algoritmoscom no minimo 2 combinações
    
    
    #TODO: medir desempenho
    # 10-fold cross validation estratificado
    # acuracia, f1_score
    # media e desvio padrao

    #TODO: gerar informaçoes de saida
    
    
    
    
    
    
