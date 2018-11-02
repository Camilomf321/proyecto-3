#Crear clase y sus respectivos diccionarios
class aprendiz:
    saludos = {
        'hola': 'buenas tardes',
        'buenas': 'en que puedo ayudarte',
        'holi': 'gg holi',
        'que se dice': 'nada ¿y tu?',
        'holita': 'hola compita'

    }
    pais = {
        'colombia': 'bogota',
        'venezuela': 'caracas',
        'chile': 'santiago de chile',
        'españa': 'madrid',
        'ecuador': 'quito',
        'francia': 'paris',
        'japon': 'tokio',
        'italia': 'roma',



    }
    despedidas = {

        'hasta luego': 'Nospi',
        'chaolin': 'Que te vaya bien',
        'nos vemos': 'vemola'
    }

    def setNombre(self, Nombre):
        self.Nombre = Nombre;
#Funcion para agregar respuesta a diccionario
    def agregar_Palabra(self, pregunta, respuesta):
        self.pais[pregunta] = respuesta

# Saluda y guarda el nombre en una variable
def main():
    aprendiendo = aprendiz()
    Saludo = input("Hola \n")

    Nombre = input("¿Tu nombre es?\n")

    despedida = aprendiendo.despedidas

    print("Buenas buenas " + Nombre + " ¿Como va todo? ")

# Se crea un ciclo while si la pregunta esta en el diccionario se retorna la respuesta, si no esta pide la respuesta y la agrega
    while True:
        pregunta = input("Dime un pais y yo te digo su capital o terminas el programa con una despedida\n")

        if pregunta in aprendiendo.pais:
            print("La capital es " + aprendiendo.pais[pregunta] + "\n")
        elif pregunta in despedida:
            print(despedida[pregunta] + " " + Nombre)
            break
        else:
            print("Hey yo que voy a saber responder eso \n")
            respuesta = input("como podría responder a eso? \n")
            aprendiendo.agregar_Palabra(pregunta, respuesta)
            print("agregado!")


main()
