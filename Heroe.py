#Una clase es un molde que esta compuesto de atributos y metodos
# los atributos son propiedades o datos, son variables del lenguaje que yo elija.
#metodos: acciones que hace el molde, es crear funciones del lenguaje que yo elija

class Heroe:

    #se debe crear primero el constructos de la clase que es  igual a una funcion especial
    # es una funcion que permite inicializar los atributos

    def __init__(self,name,height):
        self.poder=None
        self.estatura=height
        self.nombre=name
        self.tipoHeroe=None
        self.cantidadVida=None
    
    def saludar(self):
        print("hola  ")

    #atributos:
    poder=None
    estatura=None
    nombre=None
    tipoHeroe=None
    cantidadVida=None


    

#utilizando la clase=crear una instancia 
#un objeto sin importar el lenguaje es una variable especial

batman= Heroe("Bruce Waine","180")

# con el  obejto accedo a un atributo 
print(batman.nombre)

#con el objeto acceso a una funcion
batman.saludar()
    
    
