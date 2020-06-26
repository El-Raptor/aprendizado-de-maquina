"""
    Nome - RGA:
    Fábio Holanda Saraiva Júnior - 2015.1905.006-2
    Felipe Salles Lopez - 2016.1907.032-4
    Lucas Avanzi - 2016.1907.024-3
    Lucas Antonio dos Santos - 2016.1907.013-8
"""


import csv

#caminho para os datasets
dataset_path = [
                "./datasets/arrhythmia/arrhythmia.data",
                "./datasets/balance-scale/balance-scale.data",
                "./datasets/blood-transfusion/transfusion.data",
                "./datasets/echocardiogram/echocardiogram.data",
                "./datasets/glass/glass.data",
                "./datasets/haberman/haberman.data",
                "./datasets/hepatitis/hepatitis.data",
                "./datasets/iris/iris.data",
                "./datasets/lymphography/lymphography.data",
                "./datasets/tae/tae.data"
                ]


def read_input_file(file_path):
    open_file = open(file_path, "r")
    reader = csv.reader(open_file)
    data = list(reader)

    return data



def decision_tree(dataset):
    return 1

def knn(dataset):
    return 2

def naive_bayes(dataset):
    return 3

def regressao_logistica(dataset):
    return 4

def mlp_neural_networks(dataset):
    return 5



if __name__ == '__main__':

    for i in range(10):
        # As seguintes listas armazenam media e desvio padrao para acuracia e f1_score
        metrics_dc = []
        metrics_knn = []
        metrics_nb = []
        metrics_rg = []
        metrics_mlp = []

        data = read_input_file(dataset_path[i])
        print (data)

        '''
        combination = 2 # combination >= 2
        #TODO: aplicar os cinco algoritmos com no minimo 2 combinações
        for i in range(combination):
            metrics_dc.append(decision_tree(data))

            metrics_knn.append(knn(data))

            metrics_nb.append(naive_bayes(data))

            metrics_rg.append(regressao_logistica(data))

            metrics_mlp.append(mlp_neural_networks(data))

        #TODO: medir desempenho
        # 10-fold cross validation estratificado
        # acuracia, f1_score
        # media e desvio padrao
        '''
