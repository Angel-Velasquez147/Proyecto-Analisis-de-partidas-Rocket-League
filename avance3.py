#Avance 2 del programa que calcula las estadisticas de las partidas de Rocket league.
# Este avance añadio funciones a procesos que tenia en el anterior avance
def pedir_mmr_inicial():
    mmr = int(input("Ingrese su mmr inicial: "))
    return mmr

def pedir_cantidad_partidas():
    partidas = int(input("cuantas partidas deseas ingresar: "))
    return partidas

def pedir_datos_partida(numero):
    print(f"-partida {numero}-")
    goles = int(input("Cantidad de goles: "))
    asistencias = int(input("Cantidad de asistencias: "))
    salvadas = int(input("Cantidad de salvadas: "))
    tiros = int(input("cantidad de tiros: "))
    return goles, asistencias, salvadas, tiros

def calcular_rendimiento(goles, asistencias, salvadas, tiros):
    rendimiento_partida = (goles*100)+(asistencias*50)+(salvadas*50)+(tiros*10)
    return rendimiento_partida

def total_estadisticas(goles_totales, asistencias_totales, salvadas_totales, tiros_totales, totalrendimiento, goles, asistencias, salvadas, tiros, rendimiento_partida):
    goles_totales = goles_totales + goles
    asistencias_totales = asistencias_totales + asistencias
    salvadas_totales = salvadas_totales + salvadas
    tiros_totales = tiros_totales + tiros
    totalrendimiento = totalrendimiento + rendimiento_partida
    return goles_totales, asistencias_totales, salvadas_totales, tiros_totales, totalrendimiento

def calcular_promedios(goles_totales, asistencias_totales, salvadas_totales, tiros_totales, totalrendimiento, cantidad_partidas):
    promedio_gol = goles_totales / cantidad_partidas
    promedio_asistencia = asistencias_totales / cantidad_partidas
    promedio_salvada = salvadas_totales / cantidad_partidas
    promedio_tiro = tiros_totales / cantidad_partidas
    rendimiento_promedio = totalrendimiento / cantidad_partidas
    return promedio_gol, promedio_asistencia, promedio_salvada, promedio_tiro, rendimiento_promedio

def mostrar_resultados(mmr_inicial, cantidad_partidas, promedio_gol, promedio_asistencia, promedio_salvada, promedio_tiro, rendimiento_promedio):
    print("----RESULTADOS DE PARTIDAS ----")
    print(f"MMR inicial: {mmr_inicial}")
    print(f"Partidas analizadas: {cantidad_partidas}")
    print(f"promedio de gol por partida: {promedio_gol}")
    print(f"promedio de asistencia por partida: {promedio_asistencia}")
    print(f"promedio de salvada por partida: {promedio_salvada}")
    print(f"promedio de tiro por partida: {promedio_tiro}")
    print(f"rendimiento promedio por todas las partidas: {rendimiento_promedio}")

#--------------------------
#def calcular_rango()
#Aun tengo que analizar como usar esta funcion pues usaria condicionales para ser funcional
#Tambien tendria que ver si es necesario hacer listas para que funcione de manera adecuada o si podria hacer un avance solo usando if/elif
#-------------------------------


mmr_inicial = pedir_mmr_inicial()
cantidad_de_partidas = pedir_cantidad_partidas()

#valores que forman las estadisticas
total_goles = 0
total_asistencias = 0
total_salvadas = 0
total_tiros = 0
rendimiento_total = 0

#Bucle que utilizo para que pregunte las estadisticas de cada partida
for i in range(1, cantidad_de_partidas+1):
    goles, asistencias, salvadas, tiros = pedir_datos_partida(i)
    rendimiento_partida = calcular_rendimiento(goles, asistencias, salvadas, tiros)
    print(f"El puntaje obtenido durante la partida {i} fueron {rendimiento_partida} puntos")

    total_goles, total_asistencias, total_salvadas, total_tiros, rendimiento_total = total_estadisticas(
        total_goles, total_asistencias, total_salvadas, total_tiros, rendimiento_total,
        goles, asistencias, salvadas, tiros, rendimiento_partida
    )

promedio_gol, promedio_asistencia, promedio_salvada, promedio_tiro, rendimiento_promedio = calcular_promedios(
    total_goles, total_asistencias, total_salvadas, total_tiros, rendimiento_total, cantidad_de_partidas
)

mostrar_resultados(mmr_inicial, cantidad_de_partidas, promedio_gol, promedio_asistencia, promedio_salvada, promedio_tiro, rendimiento_promedio)

#Notas sobre avances futuros
#----------------------------------
#Este avance tuvo como objetivo principal añadir funciones a mi programa 
#Mi proyecto final incluira condicionales if elif para calcular_rango(mmr), que decidira tu rango/division a partir del rendimiento y resultados que tuviste
#Tambien planeo usar listas o ciclos para optimizar el codigo de la mejor manera
#----------------------------------
