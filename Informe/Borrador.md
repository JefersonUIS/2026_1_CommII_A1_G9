# Borrador

## III-B Bloque Diferenciador
El diferenciador es un sistema que procesa una señal de entrada para resaltar los cambios rápidos o transiciones en su amplitud. En la práctica, es usado principalmente para detectar los flancos de subida y bajada en señales digitales, lo que nos permite identificar el momento exacto en que ocurre una transición. Además, es muy útil para medir la velocidad de cambio de una señal, logrando transformar, por ejemplo, señales triangulares en ondas cuadradas o rampas en valores de voltaje constantes que representan su pendiente.

### Diagrama de Flujo del bloque "Diferenciador"
Para esta práctica se realizaron pruebas del funcionamiento del bloque "Diferenciador" utilizando una frecuencia de muestreo de 32 kHz. Se emplearon tres señales de entrada generadas mediante el bloque "Vector Source", integrando un "Throttle" para regular la velocidad de procesamiento. En la Fig. 5 se muestra el diagrama correspondiente a esta implementación.

### Señal Constante
Para esta prueba, se usó una señal constante de valor 5. En la Fig. 6 obtenida, la señal de salida tomó únicamente valores de 0, esto se da porque, al no haber ninguna variación en la amplitud de la entrada, el bloque realiza constantemente la resta de la muestra actual menos la anterior (5 - 5). Esto confirma que el diferenciador solo toma valores cuando observa cambios en la señal de entrada.

### Señal de Rampa
Se tomó una señal de rampa como señal de entrada con magnitud máxima de 5 y con pendiente 1. Como se puede ver en la Fig. 7. En la gráfica obtenida Fig. 7, se observa que mientras la rampa de entrada crece de manera lineal, la señal de salida se mantiene en un valor constante de 1. Esto es porque la señal de entrada tiene una pendiente uniforme y de valor 1; es decir, el cambio de valor entre una muestra y la siguiente será siempre de 1. Por otro lado, en el momento en que la rampa alcanza su valor máximo, en este caso 5, y luego cae a 0, en este instante, el bloque diferenciador realiza la operación de restar el valor actual (0) menos el anterior (5), lo que genera ese pico de magnitud -5 que se logra apreciar en la gráfica.

### Señal Cuadrada
Y para finalizar con los ensayos del bloque diferenciador, la señal constante fue cambiada por una señal cuadrada de magnitud 1. Lo que pudimos notar en la gráfica Fig. 7 es que en la salida aparecieron dos picos muy claros: uno positivo al principio y otro negativo al final del pulso. El primer pico ocurre porque, cuando la señal arranca, pasa de 0 a 1 de golpe, y como nuestro código resta el valor actual menos el anterior, el resultado es 1 positivo. El segundo pico toma valores negativos ya que se da cuando el pulso termina y la señal vuelve a cero; ahí la operación es al revés (0 - 1), lo que nos da el -1 que se ve hacia abajo. Básicamente, estos picos nos sirven para identificar exactamente los bordes o "flancos" de la señal, avisándonos justo cuando empieza y cuando termina cada pulso de la señal de entrada.
