# aprendizado-de-maquina
Este é o repositório do trabalho de Inteligência Artificial do semestre 2020/01 turma 03.

## 1. Procedimento experimental
  Para esse trabalho será utilizado os algoritmos de classificação de **Árvore de Decisão**, **Vizinhos Mais Próximos (KNN)**, ***Naïve Bayes***, **Regressão Logística** e **Redes Neurais MLP**. Devem ser utilizados os algoritmos disponíveis na biblioteca Scikit-learn.

  Para avaliar os algoritmos de classificação, deve-se adotar o procedimento de validação cruzada. Utilizaremos o procedimento **10-fold cross validation estratificado**. Para cada fold, coletaremos a **acurácia** e a **logistic loss**. Ao final, para cada algoritmo em cada dataset, faremos uma média e o desvio padrão dos valores obtidos das medidas de avaliação, utilizando os valores obtidos em cada fold.

  Para todos os algoritmos testados e em todos os datasets, diferentes valores de parâmetros serão testados (no mínimo 5 combinações para cada algoritmo em cada dataset). Será reportado o desempenho de cada algoritmo com cada combinação de parâmetro. Foi recomendado a nós usarmos dispositivos de calibração de parâmetros como o *GridSearch*.
  
## 2. Conjuntos de dados
  Neste trabalho, escolheremos 10 conjuntos de dados de classificação dentre os vários conjuntos disponíveis no repositório da [UCI](https://archive.ics.uci.edu/ml/index.php). A única restrição imposta é que estes datasets escolhidos devem ter, obrigatoriamente, mais do que 100 exemplos.

## 3. Entrega
  Escreveremos um artigo de 8 páginas no formato da SBC, incluindo referências e figuras. O artigo deverá estar em formato PDF, não sendo aceitos artigos em formatos distintos. Neste artigo, devem ser apresentados:
  - Uma introdução, apresentando o problema e o objetivo do trabalho;
  - Uma breve descrição dos algoritmos de classificação utilizados, com referências;
  - Uma explicação do procedimento experimental, incluindo uma explicação do procedimento de validação cruzada;
  - Enumeração e descrição dos datasets utilizados, contendo: nome do dataset, número de exemplos, número de atributos, número de classes e número de exemplos da classe majoritária;
  - Resultados obtidos;
  - Discussão dos resultados (não somente transcrição!);
  - Considerações finais.
  
  Deve incluir a estruturação de um artigo científico: Introdução, Trabalhos Relacionados, Metodologia Experimental, etc. Utilizaremos referências atuais e adequadas.
  Os resultados obtidos serão apresentados por meio de tabelas e gráficos. Nas tabelas, serão mostrados, para todos os datasets, a média geral de cada dataset. Os gráficos ficam a critério dos grupos e devem ser utilizados para ajudar a interpretar os resultados.
