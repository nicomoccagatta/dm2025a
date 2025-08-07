## Hipótesis Experimental del Problema 
  Al menos 10 de las variables creadas mediante Feature Engineering con Random Forest forma parte de las 20 más importantes en la explicación del modelo predictivo y su inclusión aumenta la ganancia del modelo

## Sesgo Cognitivo
  El modelo base va a agregar una mayor ganancia vs la no creación de variables mediante Feature Engineering Random Forest
  Al aplicarse diferentes modificaciones a los hiperparámetros del Random Forest se logrará encontrar una modificación en uno o más de uno de estos que conseguirá maximizar la ganancia en el modelo y por qué no aportar más variables creados por RF al TOP 20.

## Variables Definidas
  Considerando que los hiperparámetros de Random Forest son los siguientes:
    Num_iterations: cantidad de árboles del RF
    Num_leaves: cantidad de hojas de cada árbol
    Min_data_in_leaf: cantidad mínima de registros que debe tener cada hoja del RF
    Feature_fraction_bynode: es equivalente al hiperparámetro mtry de Random Forest, 0.2 significa que se construirá cada split de cada árbol tomando únicamente el 20% de los campos disponibles

## Relación con la profundidad del árbol (max_depth):
  * Num_leaves y max_depth (profundidad máxima) están relacionados.
  * Num_leaves define el número máximo de hojas, mientras que max_depth controla la profundidad máxima del árbol.
  * Un valor alto de max_depth permite que el árbol crezca más profundo y, por tanto, que haya más particiones, lo que puede aumentar el número de hojas.
  * Sin embargo, aunque la profundidad sea alta, el número de hojas puede estar limitado si num_leaves tiene un valor pequeño.


## Diseño Experimental FE Random Forest
  1 - En primer lugar se corre el modelo con el script de Feature Engineering Random Forest con las variables que vienen definidas por defecto:
  * Num_iterations: 20
  * Num_leaves: 16
  * Min_data_in_leaf: 1000
  * Feature_fraction_bynode: 0.2

  2 - Una vez corrido el modelo base, se realizará una nueva corrida donde se apagará todo el código relacionado al Feature Engineering Random Forest, para así determinar las ganancias obtenidas sin la utilización del mismo.

  3 - Luego de esto se procederá a avanzar con múltiples corridas modificando Num_iterations y Num_leaves de forma de poder determinar si estas variaciones no solo agregan variables de importancia RF al modelo sino fundamentalmente si aportan mayor ganancia. 
