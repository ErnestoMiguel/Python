class Mathops:
    #Metodo constuctor de la clase MathOps y verificacion de introduccion de datos
    def __init__(self, num1: float, num2 : float):
        if not isinstance(num1, (int,float)):
                raise ValueError(f'El Tipo de Dato Introducido es {type(num1).__name__}')
        if not isinstance(num2, (int,float)):
                raise ValueError(f'El Tipo de Dato Introducido es {type(num2).__name__}')
        self.num1 = num1
        self.num2 = num2

    def suma(self) -> float:
          #metodo suma
          return self.num1 + self.num2

    def resta(self) -> float:
          #metodo resta
          return self.num1 - self.num2

    def multiplicacion(self) -> float:
          #metodo multiplicacion
          return self.num1 * self.num2

    def division(self) ->float:
        #metodo division con tratamiento de errores
        try:
            return self.num1 / self.num2            
        except ZeroDivisionError:
            return 'Division por cero no permitida'
        
    def exponente(self) -> float:
          #metodo exponenciacion
          return self.num1 ** self.num2    