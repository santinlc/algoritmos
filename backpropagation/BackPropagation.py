from Perceptron import PerceptronPython as Perceptron

#Criando vetor com entradas e saidas para OR
entradas = [[0,0],[0,1],[1,0],[1,1]]
saidas = [0,1,1,1]
rede = Perceptron(entradas,saidas,0.5,1000,-1,Verbose=True)
rede.treinar()
rede.teste([0,0])