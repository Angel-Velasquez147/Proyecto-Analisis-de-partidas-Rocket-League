#Avance del programa que calcula las estadisticas de las partidas de Rocket league.
mmr_inicial= int(input("Ingrese su mmr inicial: "))
cantidad_de_partidas = int(input("cuantas partidas deseas ingresar: "))

#valores que forman las estadisticas

total_goles = 0
total_asistencias = 0
total_salvadas = 0
total_tiros = 0
rendimiento_total = 0


for i in range(1, cantidad_de_partidas+1) :
    print(f"-partida{i}-")
    
    goles = int(input("Cantidad de goles: "))
    asistencias = int(input("Cantidad de asistencias: "))
    salvadas = int(input("Cantidad de salvadas: "))
    tiros = int(input("cantidad de tiros: "))
    
    rendimiento_partida = (goles*100)+(asistencias*50)+(salvadas*50)+(tiros*10)
    print(f"El puntaje obtenido durante la partida {i} fueron {rendimiento_partida} puntos")

    total_goles = total_goles + goles
    total_asistencias = total_asistencias + asistencias
    total_salvadas = total_salvadas + salvadas
    total_tiros = total_tiros + tiros
    rendimiento_total = rendimiento_total + rendimiento_partida

promedio_gol = total_goles/cantidad_de_partidas
promedio_asistencia = total_asistencias/cantidad_de_partidas
promedio_salvada = total_salvadas/cantidad_de_partidas
promedio_tiro = total_tiros/cantidad_de_partidas
rendimiento_promedio = rendimiento_total / cantidad_de_partidas

print("----RESULTADOS DE PARTIDAS ----")
print(f"MMR inicial: {mmr_inicial}")
print(f"Partidas analizadas: {cantidad_de_partidas}")
print(f"promedio de gol por partida: {promedio_gol}")
print(f"promedio de asistencia por partida: {promedio_asistencia}")
print(f"promedio de salvada por partida: {promedio_salvada}")
print(f"promedio de tiro por partida: {promedio_tiro}")
print(f"promedio de rendimiento por todas las partidas: {rendimiento_promedio}")