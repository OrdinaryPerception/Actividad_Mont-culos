
class MonticuloBinario:
    def __init__(self):
        self.listaMonticulo = [0]
        self.tamanoActual = 0


    def infiltArriba(self,i):
        while i // 2 > 0:
          if self.listaMonticulo[i].gravedad == self.listaMonticulo[i // 2].gravedad:
              if self.listaMonticulo[i].prioridad < self.listaMonticulo[i // 2].prioridad:
                  tmp = self.listaMonticulo[i // 2]
                  self.listaMonticulo[i // 2] = self.listaMonticulo[i]
                  self.listaMonticulo[i] = tmp 
          elif self.listaMonticulo[i].gravedad < self.listaMonticulo[i // 2].gravedad:
             tmp = self.listaMonticulo[i // 2]
             self.listaMonticulo[i // 2] = self.listaMonticulo[i]
             self.listaMonticulo[i] = tmp
          i = i // 2
          
    def __crear_solicitud(self):
        nombre=input("Ingrese el nombre: ")
        edad=input("Ingrese la edad: ")
        direccion=input("Ingrese la direccion: ")
        motivo=input("Ingrese el motivo: ")
        gravedad=input("Ingrese la gravedad: ")
        return Dato(nombre,int(edad),direccion,motivo,int(gravedad))

    def insertar(self):
      k=self.__crear_solicitud()
      self.listaMonticulo.append(k)
      self.tamanoActual = self.tamanoActual + 1
      self.infiltArriba(self.tamanoActual)
      print(f"Su solicitud será atendida en: {self.listaMonticulo.index(k)-1} turnos")

    def infiltAbajo(self,i):
      while (i * 2) <= self.tamanoActual:
          hm = self.hijoMin(i)
          if self.listaMonticulo[i].gravedad == self.listaMonticulo[hm].gravedad:
              if self.listaMonticulo[i].prioridad > self.listaMonticulo[hm].prioridad:
                tmp = self.listaMonticulo[i]
                self.listaMonticulo[i] = self.listaMonticulo[hm]
                self.listaMonticulo[hm] = tmp
                
          elif self.listaMonticulo[i].gravedad > self.listaMonticulo[hm].gravedad:
              tmp = self.listaMonticulo[i]
              self.listaMonticulo[i] = self.listaMonticulo[hm]
              self.listaMonticulo[hm] = tmp
          i = hm

    def hijoMin(self,i):
      if i * 2 + 1 > self.tamanoActual: 
          return i * 2
      else:
          if self.listaMonticulo[i*2].gravedad == self.listaMonticulo[i*2+1].gravedad:
              if self.listaMonticulo[i*2].prioridad < self.listaMonticulo[i*2+1].prioridad:
                  return i*2
              else:
                  return i*2+1
          elif self.listaMonticulo[i*2].gravedad < self.listaMonticulo[i*2+1].gravedad:
              return i * 2
          else:
              return i * 2 + 1

    def eliminarMin(self):
      valorSacado = self.listaMonticulo[1]
      self.listaMonticulo[1] = self.listaMonticulo[self.tamanoActual]
      self.tamanoActual = self.tamanoActual - 1
      self.listaMonticulo.pop()
      self.infiltAbajo(1)
      print(f"""La siguiente solicitud será atendida:
                Nombre: {valorSacado.Nombre}
                Edad: {valorSacado.edad}
                Dirección: {valorSacado.direccion}
                Motivo: {valorSacado.motivo}
                Unidad Móvil: {self.unidad_móvil(valorSacado.gravedad)}
            """)
      
    def unidad_móvil(self,gravedad):
        if gravedad <3:
            return "Patrulla y unidades de refuerzo"
        else: return "Unidad motorizada"

    def construirMonticulo(self,unaLista):
      i = len(unaLista) // 2
      self.tamanoActual = len(unaLista)
      self.listaMonticulo = [0] + unaLista[:]
      while (i > 0):
          self.infiltAbajo(i)
          i = i - 1
          
    def imprimir_cola(self):
        for dato in self.listaMonticulo:
            if dato==0:continue
            print(dato.Nombre)


class Dato:
    def __init__(self,Nombre,edad,direccion,Motivo,gravedad):
        self.Nombre=Nombre
        self.edad=edad
        self.direccion=direccion
        self.motivo=Motivo
        self.gravedad=gravedad
        self.prioridad= self.calc_prior()
        
    def calc_prior(self):
        if self.edad<12:
            return 1
        elif self.edad>65:
             return 2
        else:
            return 4
        
dato1=Dato("Juan",34,"Cll 18","Vecinos ruidosos",3)
dato2=Dato("Maria",25,"Cra 4","Riña Callejera",1)
dato3=Dato("Diego",14,"Cra 8","Lesión",1)

miMonticulo = MonticuloBinario()
miMonticulo.construirMonticulo([dato1,dato2,dato3])
miMonticulo.eliminarMin()
miMonticulo.eliminarMin()
miMonticulo.eliminarMin()


