#Avance 5 del programa que calcula las estadisticas de las partidas de Rocket league.
# Este avance añadio listas a mi codigo 
# Utilize las listas y sus funciones de sum y len para caluclar promedios.
# Tambien aproveche el hecho de que ahora sean listas para crear una funcion que nos indique varios datos
# Los datos de esta nueva funcion son la mejor/peor puntuacion, cantidad de Victorias/Derrotas y MMR maximo
#----------------------------------

#Esta funcion le pide al usuario el mmr inicial
def pedir_mmr_inicial():
    mmr = int(input("Ingrese su mmr inicial: "))
    return mmr

#Esta funcion le pide la cantidad de partidas que desea analizar
def pedir_cantidad_partidas():
    partidas = int(input("cuantas partidas deseas ingresar: "))
    while partidas <= 0:
        print("Debe de ingresar como minimo 1 partida")
        partidas = int(input("cuantas partidas deseas ingresar: "))
    return partidas

#Esta nueva funcion es para validar si las estadisticas que pedimos no son negativas debido a que esto no existe en rocket
def validar_numero(Texto):
    numero = int(input(Texto))
    while numero < 0:
        print("El valor no puede ser negativo: ")
        numero = int(input(Texto))
    return numero

#Esta funcion pide las estadisticas de la partida
def pedir_datos_partida(numero):
    print(f"-partida {numero}-")
    goles = validar_numero("Cantidad de goles: ")
    asistencias = validar_numero("Cantidad de asistencias: ")
    salvadas = validar_numero("Cantidad de salvadas: ")
    tiros = validar_numero("Cantidad de tiros: ")
    resultado = input("Ganaste o perdiste la partida? (G/P): ")
    while resultado != "G" and resultado != "P":
        print("Solo puedes usar G o P para definir el resultado")
        resultado = input("Ganaste o Perdiste la partida? (G/P): ")
    return goles, asistencias, salvadas, tiros, resultado


#Esta funcion analiza el rendimiento de la partida basado en las estadisticas que obtuvo
def calcular_rendimiento(goles, asistencias, salvadas, tiros):
    rendimiento_partida = (goles*100)+(asistencias*50)+(salvadas*50)+(tiros*10)
    return rendimiento_partida

#Esta funcion utiliza el total de las estadisticas dividiendolo por la cantidad de partidas para obtener el promedio
def calcular_promedios(goles, asistencias, salvadas, tiros, rendimientos):
    promedio_gol = sum(goles) / len(goles)
    promedio_asistencia = sum(asistencias) / len(asistencias)
    promedio_salvada = sum(salvadas) / len(salvadas)
    promedio_tiro = sum(tiros) / len(tiros)
    rendimiento_promedio = sum(rendimientos) / len(rendimientos)
    return promedio_gol, promedio_asistencia, promedio_salvada, promedio_tiro, rendimiento_promedio

#Esta funcion muestra los resultados que queremos ver con el programa
def mostrar_resultados(mmr_inicial, cantidad_partidas, promedio_gol, promedio_asistencia, promedio_salvada, promedio_tiro, rendimiento_promedio, mmr, rango):
    print("----RESULTADOS DE PARTIDAS ----")
    print(f"MMR inicial: {mmr_inicial}")
    print(f"Partidas analizadas: {cantidad_partidas}")
    print(f"promedio de gol por partida: {promedio_gol}")
    print(f"promedio de asistencia por partida: {promedio_asistencia}")
    print(f"promedio de salvada por partida: {promedio_salvada}")
    print(f"promedio de tiro por partida: {promedio_tiro}")
    print(f"rendimiento promedio por todas las partidas: {rendimiento_promedio}")
    print(f"MMR final: {mmr}")
    print(f"Rango: {rango}")


#Esta funcion determina el desempeño de la partida basado en los puntos que el jugador obtuvo en la partida
def ver_desempeño(rendimiento_partida):
    if rendimiento_partida >= 400:
        desempeño = "Buen desempeño"
    elif rendimiento_partida >= 150:
        desempeño = "Desempeño promedio"
    else: 
        desempeño = "Mal desempeño"
    return desempeño

#Esta funcion determina como cambia el MMR del jugador dependiendo del resultado de la partida y su desempeño durante esta
def mmr_obtenido(desempeño, mmr, resultado):
    if resultado == "G" and desempeño == "Buen desempeño":
        return mmr + 14
    elif resultado == "G" and desempeño == "Desempeño promedio":
            return mmr + 12
    elif resultado == "G" and desempeño == "Mal desempeño":
            return mmr + 10
    elif resultado == "P" and desempeño == "Buen desempeño":
            return mmr - 10
    elif resultado == "P" and desempeño == "Desempeño promedio":
            return mmr -12
    elif resultado == "P" and desempeño == "Mal desempeño":
            return mmr - 14

#Esta funcion determina que rango eres segun el MMR que tienes actualmente       
def calcular_rango(mmr):
    if mmr <= 174:
        rango = "Bronce I"
    elif mmr <= 231:
        rango = "Bronce II"
    elif mmr <= 290:
        rango = "Bronce III"
    elif mmr <= 352:
        rango = "Plata I"
    elif mmr <= 414:
        rango = "Plata II"
    elif mmr <= 474:
        rango = "Plata III"
    elif mmr <= 533:
        rango = "Oro I"
    elif mmr <= 592:
        rango = "Oro II"
    elif mmr <= 654:
        rango = "Oro III"
    elif mmr <= 713:
        rango = "Platino I"
    elif mmr <= 772:
        rango = "Platino II"
    elif mmr <= 834:
        rango = "Platino III"
    elif mmr <= 914:
        rango = "Diamante I"
    elif mmr <= 994:
        rango = "Diamante II"
    elif mmr <= 1074:
        rango = "Diamante III"
    elif mmr <= 1194:
        rango = "Campeón I"
    elif mmr <= 1314:
        rango = "Campeón II"
    elif mmr <= 1434:
        rango = "Campeón III"
    elif mmr <= 1574:
        rango = "Gran Campeón I"
    elif mmr <= 1705:
        rango = "Gran Campeón II"
    elif mmr <= 1862:
        rango = "Gran Campeón III"
    else:
        rango = "Supersonic Legend"
    return rango  
   
#Esta funcion analiza las distintas partidas para encontrar datos especificos entre las distintas partidas
def Analisis(rendimientos, resultados, historial_mmr):
    mejor = max(rendimientos)
    numero_mejor = rendimientos.index(mejor) +1 
    minimo = min(rendimientos)
    numero_minimo = rendimientos.index(minimo) +1 
    
    victorias = resultados.count("G")
    derrotas = resultados.count("P")  
    
    mmr_maximo = max(historial_mmr) 
    
    print(f"En la partida {numero_mejor} obtuviste {mejor} puntos que fue tu mejor puntuacion")
    print(f"En la partida {numero_minimo}, obtuviste {minimo} puntos que fue tu peor puntuacion")
    print(f"Obtuviste {victorias} victorias")
    print(f"Obtuviste {derrotas} derrotas")
    print(f"Tu mmr maximo fue {mmr_maximo}")

mmr_inicial = pedir_mmr_inicial()
mmr = mmr_inicial
lista_mmr = [mmr]
cantidad_de_partidas = pedir_cantidad_partidas()

#Listas que forman las estadisticas
lista_goles = []
lista_asistencias = []
lista_salvadas = []
lista_tiros = []
lista_resultado = []
lista_rendimiento = []

#Bucle que utilizo para que pregunte las estadisticas de cada partida y use las funciones que cree anteriormente para sacar los resultados
for i in range(1, cantidad_de_partidas+1):
    goles, asistencias, salvadas, tiros, resultado = pedir_datos_partida(i)
    rendimiento_partida = calcular_rendimiento(goles, asistencias, salvadas, tiros)
    desempeño = ver_desempeño(rendimiento_partida)
    mmr = mmr_obtenido(desempeño, mmr, resultado)
    print(f"El puntaje obtenido durante la partida {i} fueron {rendimiento_partida} puntos, tuviste un {desempeño}")

    lista_goles.append(goles)
    lista_asistencias.append(asistencias)
    lista_salvadas.append(salvadas)
    lista_tiros.append(tiros)
    lista_resultado.append(resultado)
    lista_rendimiento.append(rendimiento_partida)
    lista_mmr.append(mmr)
    

promedio_gol, promedio_asistencia, promedio_salvada, promedio_tiro, rendimiento_promedio = calcular_promedios(
lista_goles, lista_asistencias, lista_salvadas, lista_tiros, lista_rendimiento
)

rango = calcular_rango(mmr)

mostrar_resultados(mmr_inicial, cantidad_de_partidas, promedio_gol, promedio_asistencia, promedio_salvada, promedio_tiro, rendimiento_promedio, mmr, rango)

Analisis(lista_rendimiento, lista_resultado, lista_mmr)

#Notas sobre avances futuros
#----------------------------------
#Este avance tuvo como objetivo principal añadir Listas a mi programa
#Planeo usar diccionarios, tuplas o listas anidadas dependiendo de cual sea mejor para dividir cada rango en 4 divisiones
#Las listas actuales se pueden ver modificados a medida que mejore mi programa.
#----------------------------------