# Proyecto-Analisis-de-partidas-Rocket-League
Un proyecto que tiene como objetivo analizar las estadisticas de una cierta cantidad de partidas del videojuego rocket league y a partir de estas definir el rendimiento del usuario y que tanto afecto en su rango.

##Contexto: 
Rocket League es un videojuego competitivo que combina fútbol con vehículos. Dentro de sus modos de juego existen las partidas competitivas 2v2. El juego utiliza un sistema en el que los jugadores tienen un MMR (Matchmaking Rating), que representa su nivel de habilidad y, a partir de este, se determina su rango. Los rangos competitivos se organizan en categorías y, dentro de cada categoría, existen diferentes subrangos y cuatro divisiones por subrango (exceptuando el rango final). Este proyecto busca analizar el rendimiento del jugador a partir de sus estadísticas de partidas, como goles, asistencias, salvadas y tiros, para determinar su rendimiento, actualizar su MMR y determinar su rango y división.

##Idea: 
Un proyecto que pueda calcular partidas de rocket con sus resultados y sus estadísticas como goles, victorias, asistencias y saves para ver el rendimiento promedio de un jugador en una cierta cantidad de partidas solicitadas.

##Problema: 
Tengo estadísticas de mis últimas partidas jugadas pero el juego no me permite identificar tendencias de manera automática, el programa arregla esto analizando las estadísticas de tus últimas partidas para definir información sobre cómo fue mi rendimiento, que tanto afecto en mi rango y cual es mi nivel actual.

El objetivo del programa es que te pida tu MMR inicial y que a partir de esto te diga tu MMR actual que es el mismo que el inicial pero irá cambiando por partida. También quiero que dependiendo del MMR indique el rango y división del jugador de manera automática.
Una vez completado esto el programa te pedirá la cantidad de partidas que jugaste, luego él empezará por partida 1 y preguntará el resultado de la partida para identificar si fue victoria o derrota. De las partidas te pediría las estadísticas de estas como los goles, asistencias, salvadas y tiros de la partida. A partir de esta información usará un sistema de puntos en el que determinará que tan buen rendimiento tuvo el jugador en la partida. Una vez se encontraran estos datos iría al siguiente paso donde dependiendo del resultado de la partida y el rendimiento que tuvo el jugador se le añadirá o bajará una cierta cantidad de puntos al MMR actual del jugador. Cuando se terminen de analizar todas las partidas el programa hará un promedio de gol, asistencia, tiros y saves y cuál fue su mejor partida basado en rendimiento personal y mostrará cuál fue el MMR final.

##Pseudocodigo:

##Entradas:
1. Solicitar al usuario su MMR inicial.
2. Solicitar la cantidad de partidas que desea analizar.
3. Para cada partida, solicitar:
   3.1. Resultado de la partida: victoria o derrota.
   3.2. Cantidad de goles.
   3.3. Cantidad de asistencias.
   3.4. Cantidad de salvadas.
   3.5. Cantidad de tiros.

##Proceso:
4. Asignar el MMR inicial como MMR actual.
5. Determinar el rango y división correspondientes al MMR actual.
6. Repetir el siguiente proceso para cada partida:
   6.1. Mostrar el número de la partida que se está analizando.
   6.2. Almacenar el resultado y las estadísticas obtenidas.
   6.3. Calcular un puntaje de rendimiento utilizando las estadísticas de la partida.
   6.4. Determinar cuánto MMR debe ganar o perder el jugador utilizando el resultado de la partida y su rendimiento.
   6.5. Actualizar el MMR actual.
   6.6. Comparar el rendimiento de la partida con el de las partidas anteriores para determinar si es la mejor partida registrada.

7. Una vez analizadas todas las partidas:
   7.1. Calcular el promedio de goles.
   7.2. Calcular el promedio de asistencias.
   7.3. Calcular el promedio de salvadas.
   7.4. Calcular el promedio de tiros.
   7.5. Calcular el rendimiento promedio.
   7.6. Determinar cuál fue la mejor partida según el rendimiento.
   7.7. Determinar nuevamente el rango y división correspondientes al MMR final.

##Salidas:
8. Mostrar el MMR inicial.
9. Mostrar el MMR final.
10. Mostrar el rango final.
11. Mostrar la división final.
12. Mostrar el rendimiento promedio.
13. Mostrar la mejor partida y su rendimiento.





