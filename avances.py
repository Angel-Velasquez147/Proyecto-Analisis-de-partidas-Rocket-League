#Avance 4 del programa que calcula las estadisticas de las partidas de Rocket league.
# Este avance añadio bucles while debido a que anteriormente ya tenia en mi codigo mi bucle for
# Utilize while solamente para validar que el usuario introduzca lo que el programa necesita para funcionar.
# Dependiendo del rendimiento se calcula el cambio del MMR
# A partir del MMR actual se determinara el rango del jugador
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

#Reemplazar en pedir datos partidas añadiendo la funcion para no hacer como 4 whiles


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

#Esta funcion suma las estadisticas de las distintas partidas para sacar el total
def total_estadisticas(goles_totales, asistencias_totales, salvadas_totales, tiros_totales, totalrendimiento, goles, asistencias, salvadas, tiros, rendimiento_partida):
    goles_totales = goles_totales + goles
    asistencias_totales = asistencias_totales + asistencias
    salvadas_totales = salvadas_totales + salvadas
    tiros_totales = tiros_totales + tiros
    totalrendimiento = totalrendimiento + rendimiento_partida
    return goles_totales, asistencias_totales, salvadas_totales, tiros_totales, totalrendimiento

#Esta funcion utiliza el total de las estadisticas dividiendolo por la cantidad de partidas para obtener el promedio
def calcular_promedios(goles_totales, asistencias_totales, salvadas_totales, tiros_totales, totalrendimiento, cantidad_partidas):
    promedio_gol = goles_totales / cantidad_partidas
    promedio_asistencia = asistencias_totales / cantidad_partidas
    promedio_salvada = salvadas_totales / cantidad_partidas
    promedio_tiro = tiros_totales / cantidad_partidas
    rendimiento_promedio = totalrendimiento / cantidad_partidas
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


mmr_inicial = pedir_mmr_inicial()
mmr = mmr_inicial
cantidad_de_partidas = pedir_cantidad_partidas()

#valores que forman las estadisticas
total_goles = 0
total_asistencias = 0
total_salvadas = 0
total_tiros = 0
rendimiento_total = 0

#Bucle que utilizo para que pregunte las estadisticas de cada partida y use las funciones que cree anteriormente para sacar los resultados
for i in range(1, cantidad_de_partidas+1):
    goles, asistencias, salvadas, tiros, resultado = pedir_datos_partida(i)
    rendimiento_partida = calcular_rendimiento(goles, asistencias, salvadas, tiros)
    desempeño = ver_desempeño(rendimiento_partida)
    mmr = mmr_obtenido(desempeño, mmr, resultado)
    print(f"El puntaje obtenido durante la partida {i} fueron {rendimiento_partida} puntos, tuviste un {desempeño}")

    total_goles, total_asistencias, total_salvadas, total_tiros, rendimiento_total = total_estadisticas(
        total_goles, total_asistencias, total_salvadas, total_tiros, rendimiento_total,
        goles, asistencias, salvadas, tiros, rendimiento_partida
    )

promedio_gol, promedio_asistencia, promedio_salvada, promedio_tiro, rendimiento_promedio = calcular_promedios(
    total_goles, total_asistencias, total_salvadas, total_tiros, rendimiento_total, cantidad_de_partidas
)

rango = calcular_rango(mmr)

mostrar_resultados(mmr_inicial, cantidad_de_partidas, promedio_gol, promedio_asistencia, promedio_salvada, promedio_tiro, rendimiento_promedio, mmr, rango)

#Notas sobre avances futuros
#----------------------------------
#Este avance tuvo como objetivo principal añadir bucles a mi programa
#Planeo usar listas, diccionarios o tuplas para poder hacer u
#Los bucles actuales se pueden ver modificados a medida que mejore mi programa.
#----------------------------------
