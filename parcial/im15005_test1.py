class Corridas_ArribaAbajo(object):
    """docstring for Corridas_ArribaAbajo"""
    def __init__(self, lista_numeros):
        self.lista_numeros = lista_numeros
        self.n = self.lista_numeros.__len__()
        self.unos_y_ceros = list({})
        self.numero_de_corridas = -1
        self.varianza = 0
        self.miu = 0
        #self.hipotesis=="Los numeros aletorios no son aceptados"
        self.z=0
        #self.u
        self.start()

    def start(self):
        for i in range(1,self.n): # del 1 al n-1( ya que comienza en cero
            # Si el numero es menor o igual que el anterior se pone cero
            if self.lista_numeros[i] <= self.lista_numeros[i-1]:
                self.unos_y_ceros.append(0)
            else: # Si no se pone 1
                self.unos_y_ceros.append(1)
            
            if i == 1: # Si ES el primer caso
                self.numero_de_corridas = 1
            else: 
                if self.unos_y_ceros[i-1] != self.unos_y_ceros[i-2]:
                    self.numero_de_corridas += 1
                    
        
        ceros = self.unos_y_ceros.count(0)
        unos = self.unos_y_ceros.count(1)
        u1 = 2*(ceros*unos)/(self.n) + 0.5
        numerador=2*(ceros*unos)*((2*ceros*unos)-self.n)
        denominador=(self.n)**2*(self.n-1)
        o=numerador/denominador
        
        self.varianza = o
        self.mui = u1
        z=(self.numero_de_corridas-u1)/o
        self.z=z
        print "Valor Esperado",u1
        print "Varianza",o
        print "Z",z
        print "Hipotesis: numeros aletorios no son aceptados"
        
        #print self.n
    def __str__(self):
        return "Lista de Numeros: %s\nSecuencia: %s\nN de corridas: %s"%(self.lista_numeros, self.unos_y_ceros, self.numero_de_corridas)
        


if __name__ == '__main__':
    
    lista_numeros=[41, 68, 89, 94, 74, 91, 55, 62, 36, 27,
					19, 72, 75, 9, 54, 2, 1, 36, 16, 28,
					18, 1, 95, 69, 18, 47, 23, 32, 82, 53,
					31, 42, 73, 4, 83, 45, 13, 57,63, 29]
    cab = Corridas_ArribaAbajo(lista_numeros)
    print cab
