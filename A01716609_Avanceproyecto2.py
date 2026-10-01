import random
#https://github.com/juanmatap12-glitch/Take-of-decisions.git
def evaluacion_1(): #En esta funcion se sumaron todos los valores que se le asignan a la variable de la opcion 1
    puntuacion_beneficio1 = beneficio_1 + beneficio_2 + beneficio_3 + beneficio_4 + beneficio_5 + beneficio_6 + beneficio_7 + beneficio_8 + beneficio_9 + beneficio_10  #el puntaje de cada beneficio
    puntuacion_riesgo2 = riesgo_1 + riesgo_2 + riesgo_3 + riesgo_4 + riesgo_5 + riesgo_6 + riesgo_7 + riesgo_7 + riesgo_8 + riesgo_9 + riesgo_10 #el puntaje de riesgo
    
def evaluacion_2(): #En esta funcio se sumaran todos los valores que se asignan a la variable de la opcion 2
    
    
    
def recursos():# aqui inclui algunos recursos psicologicos gratuitos
    print("Estos son algunos recursos que te pueden ayudar si estas pasando por problemas emocionales o quieres hablar sobre algun tema")
    print("Ayuda psicologia sejuve:")
    print("Para llamadas: 442-224-2254, para mensajes: 442-144-3740")
    print("Linea de la vida")
    print("800-911-2000")
    print("Simisae")
    print("800-911-3232")
    
    

def consejo():#aqui inclui una serie de consejos y use el random para que sea como un consejo de la galleta de fortuna
    
    consejos = [
        "El tiempo es un río veloz; espera a que las aguas se calmen 24 horas antes de tomar el timón.",
        "Aquel que no plasma sus pensamientos en papel, deja sus sueños a la deriva del viento.",
        "Mira a través del velo del tiempo: ¿qué eco dejará esta elección en 10 minutos, 10 meses y 10 años?",
        "La montaña más alta no se escala de un salto, sino paso a paso sobre las piedras del presente.",
        "No te confundas con los susurros de lo urgente; escucha solo la voz de lo verdaderamente importante.",
        "Abre espacio a lo inesperado; hasta el mapa más antiguo debe dejar margen para las sombras de la duda.",
        "Antes de iniciar la travesía, define con claridad cuál es el puerto que marcara el final del viaje.",
        "No entregues todo tu fuego a una sola chispa; prueba la llama en pequeño antes de encender el faro.",
        "Cuestiona las ilusiones de tu mente; asegúrate de caminar sobre tierra firme y no sobre espejismos.",
        "Saber cerrar la puerta a lo innecesario es el único modo de proteger la luz de tu destino.",
        "El búho ve lo que la noche oculta; busca la mirada de una alma neutral para revelar tus puntos ciegos.",
        "Lo que no se contempla con paciencia y medida, se disuelve en el caos del olvido.",
        "Crea tus propios rituales; lo que se vuelve constante transforma la energía del esfuerzo en fluidez.",
        "No intentes gobernar las tormentas del mundo; domina únicamente las velas de tu propia embarcación.",
        "Toda elección es un sacrificio silencioso; acepta lo que dejas ir para abrazar lo que eliges.",
        "La gota de agua no rompe la piedra por su fuerza, sino por su constante perseverancia.",
        "Evita la parálisis del abismo; poner límites a la duda es el primer paso para manifestar la acción.",
        "Escribe la historia de tus decisiones; el pasado es el libro de sombras que ilumina el futuro.",
        "El espíritu agotado solo produce espejismos; descansa la mente antes de consultar la encrucijada.",
        "El camino no es de piedra fija, se moldea con cada paso; adapta tus velas según el viento cambie."
    ]
    
    revelacion = random.choice(consejos)
    print("Tu consejo es", revelacion)
    
def main():
    print("Bienvenido al programa para toma correcta de deciones")
    print("Que quieres hacer hoy?")
    ejecutando = True

    while ejecutando: #aqui use un while que me sugirio mi hermano
        hacer_hoy = int(input("Selecciona 1 si quieres acceder a los recursos psicologicos, 2 si quieres ayuda para tomar una decision, 3 galleta de la fortuna, 4 si quieres salir"))
        if hacer_hoy <= 4:
            match hacer_hoy:
                
                case 1:
                    recursos()
                case 2:
                    # aqui comenze con el programa principal que es la ayuda para tomar decisiones 
                    desicion = str(input("¿Cual es la decision que debes tomar"))
                    opcion_1 = str(input("Dame tu primera opcion"))
                    opcion_2 = str(input("Dame tu segunda opcion"))
                    print("Iniciando serie de preguntas")
                    print("A cada pregunta asignale un valor del 1 al 10 de acuerdo al beneficio que te traiga") #aqui quiero ir dando preguntas y que el puntaje se le sume al buntaje de beneficio
                    print("Opción 1: ¿Qué tanto bienestar te aportará esta opción en los próximos 10 meses?") 
                    beneficio_1 = int(input("Beneficio:")) 
                    riesgo_1 =  10 - beneficio_1
                    print("Opción 2: Si no eliges la Opción 1 por tomar esta, ¿qué tanto te pesará dentro de 10 meses?")#voy a ir haciendo lo mismo del puntaje con cada pregunta de cada opcion
                    beneficio_2 = int(input("Beneficio:"))
                    riesgo_2 = 10 - beneficio_2

                    
                    
                    
        
                case 3:
                    consejo()
                case 4:
                    ejecutando = False
        else:
            print("valor no valido")
    
     
    
    
main()
