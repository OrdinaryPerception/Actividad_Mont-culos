
class Dato:
    def __init__(self,Nombre,edad,direccion,Motivo,gravedad):
        self.Nombre=Nombre
        self.edad=edad
        self.direccion=direccion
        self.motivo=Motivo
        self.gravedad=gravedad
        self.prioridad= self.calc_prior()
        
    def calc_prior(self,edad):
        if edad<12:
            return 1
        elif edad>65:
             return 2
        else:
            return 4

dato1=Dato("Juan",45,"Cll 12","Lesión",2)
dato2=Dato("Andrés",17,"Cra 5","Vecinos ruidosos",3)


class MonticuloBinario:
    def __init__(self):
        self.listaMonticulo = [0,dato1,dato2]
        self.tamanoActual = 0
        
        
    def infiltArriba(self,i):
        while i // 2 > 0:
            if 
          elif self.listaMonticulo[i].gravedad < self.listaMonticulo[i // 2].gravedad:
             tmp = self.listaMonticulo[i // 2]
             self.listaMonticulo[i // 2].gravedad = self.listaMonticulo[i].gravedad
             self.listaMonticulo[i] = tmp
          i = i // 2
          
    def insertar(self,k):
      self.listaMonticulo.append(k)
      self.tamanoActual = self.tamanoActual + 1
      self.infiltArriba(self.tamanoActual)

    def infiltAbajo(self,i):
      while (i * 2) <= self.tamanoActual:
          hm = self.hijoMin(i)
          if self.listaMonticulo[i].gravedad > self.listaMonticulo[hm].gravedad:
              tmp = self.listaMonticulo[i]
              self.listaMonticulo[i] = self.listaMonticulo[hm]
              self.listaMonticulo[hm] = tmp
          i = hm

    def hijoMin(self,i):
      if i * 2 + 1 > self.tamanoActual:
          return i * 2
      else:
          if self.listaMonticulo[i*2] < self.listaMonticulo[i*2+1]:
              return i * 2
          else:
              return i * 2 + 1

    def eliminarMin(self):
      valorSacado = self.listaMonticulo[1]
      self.listaMonticulo[1] = self.listaMonticulo[self.tamanoActual]
      self.tamanoActual = self.tamanoActual - 1
      self.listaMonticulo.pop()
      self.infiltAbajo(1)
      return valorSacado

    def construirMonticulo(self,unaLista):
      i = len(unaLista) // 2
      self.tamanoActual = len(unaLista)
      self.listaMonticulo = [0] + unaLista[:]
      while (i > 0):
          self.infiltAbajo(i)
          i = i - 1

miMonticulo = MonticuloBinario()
miMonticulo.construirMonticulo([1,"xd",5,3,4,6,5,5])

#Se construye un monticulo en el cual los valores son las prioridades de cada llamada


class Cola_prior(MonticuloBinario):
    def __init__(self):
        super().__init__()
        
    def agregar_llamada(self):
        nombre=input("Ingrese el nombre: ")
        edad=input("Ingrese la edad: ")
        direccion=input("Ingrese la direccion: ")
        motivo=input("Ingrese el motivo: ")
        gravedad=input("Ingrese la gravedad")
        dato=Dato(nombre,edad,direccion,motivo,gravedad)
        