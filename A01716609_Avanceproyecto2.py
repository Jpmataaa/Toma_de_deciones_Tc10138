import random
#https://github.com/juanmatap12-glitch/Take-of-decisions.git
def operaciones(opcion_1, opcion_2): #En esta funcion se sumaron todos los valores que se le asignan a la variable de la opcion 1
    preguntas = [
    "Impacto a corto plazo: ¿Qué nivel de tranquilidad inmediata te dará elegir esta opción en los próximos 10 días?",
    "Impacto a mediano plazo: ¿Qué tanto bienestar general te aportará en los próximos 10 meses?",
    "Impacto a largo plazo: ¿Qué tan orgulloso te sentirás de haber tomado esta decisión dentro de 10 años?",
    "Autenticidad: ¿Qué tanto se alinea este camino con tus valores principales y quien realmente eres?",
    "Crecimiento: ¿Qué tanto esta elección está impulsada por el deseo de crecer, en lugar del miedo a equivocarte?",
    "Minimización de arrepentimiento: Si el escenario ideal no se cumple, ¿qué tan en paz estarás sabiendo que al menos lo intentaste?",
    "Energía mental: ¿Cuánta energía vital y motivación genuina te aportará (en lugar de provocarte desgaste)?",
    "Autonomía: ¿Qué tanto control mantienes sobre tu propia vida, tiempo e independencia si eliges esto?",
    "Entorno social: ¿Qué tan positivo será el efecto de esta decisión en las relaciones que más te importan?",
    "Intuición pura: Si lanzaras una moneda y el resultado te obligara a tomar esta opción, ¿cuánto alivio sentirías en ese primer segundo?",
    "Costo de oportunidad: Al renunciar a las demás alternativas por tomar esta, ¿qué tanta tranquilidad sientes con lo que dejas ir?",
    "Resiliencia: Si las cosas se complican, ¿qué tanta voluntad y capacidad sientes que tienes para enfrentar los obstáculos exclusivos de esta opción?"
]
    beneficio_1 = []
    riesgo_1 = []
    beneficio_2 = []
    riesgo_2 = []
    print(f"Califica las preguntas de acuerdo a {opcion_1} ")
    for pregunta in preguntas:
        print(pregunta)
        puntaje = int(input("Dame el puntaje de beneficio"))
        riesgo = 10 - puntaje
        beneficio_1.append(puntaje)
        riesgo_1.append(riesgo)
    exito_1 = int(input("Del 1 al 100, ¿qué porcentaje de probabilidad crees que hay de que esta opción salga exactamente como quieres?")) / 100
    fracaso_1 = 1.0 - exito_1
    print(f"Ahora califica las preguntas de acuerdo a {opcion_2} ")    
    for pregunta in preguntas:
        print(pregunta)
        puntaje = int(input("Dame el puntaje de beneficio"))
        riesgo = 10 - puntaje
        beneficio_2.append(puntaje)
        riesgo_2.append(beneficio)
    exito_2 = int(input("Del 1 al 100, ¿qué porcentaje de probabilidad crees que hay de que esta opción salga exactamente como quieres?")) / 100
    fracaso_2 = 1.0 - exito_2
    total_beneficio1 = sum(beneficio_1)
    total_beneficio2 = sum(beneficio_2)
    total_riesgo1 = sum(riesgo_1)
    total_riesgo2 = sum(riesgo_2)
    
    valor_esperado_1 = (total_beneficio1 * exito_1) - (total_riesgo1 * fracaso_1)
    valor_esperado_2 = (total_beneficio2 * exito_2) - (total_riesgo2 * fracaso_2)
    
    print("RESULTADOS")
    if valor_esperado_1 > valor_esperado_2:
        print(f"TU OPCION MAS VIABLE ES {opcion_1}, con la probabilidad de: ", valor_esperado_1)
    elif valor_esperado_1 < valor_esperado_2:
        print(f"TU OPCION MAS VIABLE ES {opcion_2}, con la probabilidad de: ", valor_esperado_2)
    else:
        print("Las probabilidades son iguales")
        
    
    
    
    
def recursos():# aqui inclui algunos recursos psicologicos gratuitos
    recursos = ["Instituto para Prevenir Conductas de Riesgo: 070 / 442-238-7770", "auxiliospsicologicos.municipiodequeretaro.gob.mx, DIF Estatal Querétaro: 442-238-5000", "Consejo Estatal Contra las Adicciones (CECA): 442-212-0408", "Instituto Queretano de las Mujeres: 442-215-3404, Línea de la Vida: 800-911-2000", "Secretaría de la Juventud (SEJUVE): 442-144-3740"]
    for resource in recursos:
        print(resource)

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
                    desicion = (input("¿Cual es la decision que debes tomar"))
                    opcion_1 = (input("Dame tu primera opcion"))
                    opcion_2 = (input("Dame tu segunda opcion"))
                    print("Iniciando serie de preguntas")
                    print("A cada pregunta asignale un valor del 1 al 10 de acuerdo al beneficio que te traiga") #aqui quiero ir dando preguntas y que el puntaje se le sume al buntaje de beneficio
                    operaciones(opcion_1, opcion_2)
        
                case 3:
                    consejo()
                case 4:
                    ejecutando = False
        else:
            print("valor no valido")
    
     
    
    
main()
