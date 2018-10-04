import random

class PerceptronPython:
    
    def __init__(self, entradas, saidas, taxa_aprendizado, maximo_epocas, limiar, Verbose=False):
        self.entradas = entradas
        self.saidas = saidas
        self.taxa_aprendizado = taxa_aprendizado
        self. maximo_epocas =  maximo_epocas
        self.limiar = limiar
        self.num_amostras = len(entradas)
        self.num_atributos = len(entradas[0])
        self.pesos_sinapticos = []
        self.Verbose = Verbose
        
    def treinar(self):
        self.pesos_sinapticos = []
        for i in range(self.num_amostras):
            self.pesos_sinapticos.append(random.random())
        if self.Verbose :
            print ("Pesos sinapticos inicial: ")
            print(self.pesos_sinapticos)
            
        
        for entrada in self.entradas:
            entrada.insert(0,-1)
        
        self.pesos_sinapticos.insert(0, self.limiar)
        
        
        epoca_atual = 1
        
        while True:
          
            possuiErro = False 
            
            for amostra in range(self.num_amostras):
                u = 0
                for atributo in range (self.num_atributos +1):
                    u += self.pesos_sinapticos[atributo]*self.entradas[amostra][atributo]
                y = self.funcao_ativacao(u)
                erro_calculado = self.saidas[amostra] -y
                
                if erro_calculado != 0:
                    possuiErro = True
                    for atributo in range(self.num_atributos+1):
                        novo_peso =  self.pesos_sinapticos[atributo]
                        novo_peso += self.taxa_aprendizado * erro_calculado * self.entradas[amostra][atributo]
                        self.pesos_sinapticos[atributo] = novo_peso
            epoca_atual += 1
            if self.Verbose :
                print("Epoca atual %d " %epoca_atual)
                print(self.pesos_sinapticos)
                
            # Parada do algoritmo
            if not possuiErro or epoca_atual > self.maximo_epocas:
                break
            
            
    #Criando a funcao de ativacao degrau
    def funcao_ativacao(self,u):
        if (u >= 0):
            return 1
        return 0
    
    def teste(self, amostra):
        print ("Para entrada: ")
        amostra.insert(0, -1)
        u = 0
        for i in range(self.num_atributos + 1):
            u += self.pesos_sinapticos[i] * amostra[i]
        y = self.funcao_ativacao(u)
        print(amostra)
        print("resultado:")
        print("classe: %d" %y)
        

