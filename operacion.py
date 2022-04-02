from Trabajador import *

class Operaciones(trabajador):

    def Sueldo_trabajador(self):

        if self.Categoria_trabajador == "A":
            self.sueldoBase = 3000

        elif self.Categoria_trabajador == "B":
            self.sueldoBase = 2500

        else: 
            self.sueldoBase = 2000
        print('')
        print(">>SUELDO BASE:", self.sueldoBase)

        return self.sueldoBase


    def horas_extras(self):

        if self.Categoria_trabajador == "A":
            self.Pago_extra = ((self.sueldoBase/240)* self.Horas_trabajador)
        
        elif self.Categoria_trabajador == "B":
            self.Pago_extra = ((self.sueldoBase/240)* self.Horas_trabajador) 

        else:
            self.Pago_extra = ((self.sueldoBase/240)* self.Horas_trabajador)

        
        print(">>HORAS EXTRAS:",self.Pago_extra)
        return self.Pago_extra


    def Descuento(self):

        if self.Categoria_trabajador == "A":
            self.Descuento1 = (self.sueldoBase/240) * (self.Tardanza_trabajador/60)

        elif self.Categoria_trabajador == "B":
            self.Descuento1 = (self.sueldoBase/240) * (self.Tardanza_trabajador/60)

        else:
            self.Descuento1 = (self.sueldoBase/240) * (self.Tardanza_trabajador/60)

        
        print('>>DESCUENTO:', self.Descuento1)
        return self.Descuento1

    
    def Total(self):

        if self.Categoria_trabajador == "A":
            self.total = self.sueldoBase +  self.Pago_extra - self.Descuento1

        elif self.Categoria_trabajador == "B":
            self.total = self.sueldoBase +  self.Pago_extra - self.Descuento1

        else: 
            self.total = self.sueldoBase +  self.Pago_extra - self.Descuento1


    def boleta(self):
        print('\n')
        print('|-------------------------BOLETA DE PAGO---------------------------')
        print('|')
        print('|>>NOMBRE                    :', self.Nombre_trabajador)
        print('|>>CATEGORIA                 :', self.Categoria_trabajador)
        print('|>>SUELDO BASICO             :', self.sueldoBase)
        print('|>>DESCUENTO TARDANZA        :', self.Descuento1)
        print('|>>PAGO HORAS EXTRAS         :', self.Pago_extra)
        print('|>>SUELDO NETO               :', self.total)