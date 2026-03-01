# Borrador

# Informe de Laboratorio: Bloque Diferenciador

## II. METODOLOGÍA
* [cite_start]**Diferenciador**: Resalta las variaciones rápidas en la amplitud mediante la diferencia entre muestras consecutivas: [cite: 2033]
[cite_start]$$y[n]=x[n]-x[n-1]$$ [cite: 2034]

---

## III-B Bloque Diferenciador
[cite_start]El diferenciador es un sistema que procesa una señal de entrada para resaltar los cambios rápidos o transiciones en su amplitud. [cite: 2065] [cite_start]En la práctica, es usado principalmente para detectar los flancos de subida y bajada en señales digitales, lo que nos permite identificar el momento exacto en que ocurre una transición. [cite: 2066] [cite_start]Además, es muy útil para medir la velocidad de cambio de una señal, logrando transformar, por ejemplo, señales triangulares en ondas cuadradas o rampas en valores de voltaje constantes que representan su pendiente. [cite: 2067]

### Diagrama de Flujo del bloque "Diferenciador"
[cite_start]Para esta práctica se realizó pruebas del funcionamiento del bloque "Diferenciador" se tomó 32 kHz como el valor de la frecuencia de muestreo. [cite: 2068] [cite_start]Se tomaron 3 señales de entrada generadas con el bloque "Vector Source", y también se incluyó en el diseño el bloque "Throttle" para limitar la velocidad de procesamiento de las muestras. [cite: 2069] [cite_start]En la Fig. 5 se muestra el diagrama correspondiente al diferenciador. [cite: 2070]

### Señal Constante
[cite_start]Para esta prueba, se usó una señal constante de valor 5. [cite: 2071] [cite_start]En la Fig. 6 obtenida, la señal de salida tomó unicamente valores de 0, esto se da porque, al no haber ninguna variación en la amplitud de la entrada, el bloque realiza constantemente la resta de la muestra actual menos la anterior $(5-5)$. [cite: 2101] [cite_start]Esto confirma que el diferenciador solo toma valores cuando observa cambios en la señal de entrada. [cite: 2102]

### Señal de Rampa
[cite_start]Se tomó una señal de rampa como señal de entrada con magnitud máxima de 5 y con pendiente 1. [cite: 2103] [cite_start]Como se puede ver en la Fig. 7. [cite: 2103] [cite_start]En las gráfica obtenida Fig. 7, se observa que mientras la rampa de entrada crece de manera lineal, la señal de salida se mantiene en un valor constante de 1. [cite: 2104] [cite_start]Esto es porque la señal de entrada tiene una pendiente uniforme y de valor 1; es decir, el cambio de valor entre una muestra y la siguiente será siempre de 1. [cite: 2105] [cite_start]Por otro lado, en el momento en que la rampa alcanza su valor máximo, en este caso 5, y luego cae a 0, en este instante, el bloque diferenciador realiza la operación de restar el valor actual (0) menos el anterior (5), lo que genera ese pico de magnitud -5 que se logra apreciar en la gráfica. [cite: 2105]

### Señal Cuadrada
[cite_start]Y para finalizar con los ensayos del bloque diferenciador, la señal constante fue cambiada por una señal cuadrada de magnitud 1. [cite: 2106] [cite_start]Lo que pudimos notar en la gráfica Fig. 7 es que en la salida que aparecieron dos picos muy claros: uno positivo al principio y otro negativo al final del pulso. [cite: 2110] [cite_start]El primer pico ocurre porque, cuando la señal arra arranca, pasa de 0 a 1 de golpe, y como nuestro código resta el valor actual menos el anterior, el resultado es 1 positivo. [cite: 2111] [cite_start]El segundo pico, toma valores negativos ya que se da cuando el pulso termina y la señal vuelve a cero, ahí la operación es al revés $(0-1),$ lo que nos da el -1 que se ve hacia abajo. [cite: 2112] [cite_start]Básicamente, estos picos nos sirven para identificar exactamente los bordes o "flancos" de la señal, avisándonos justo cuando empieza y cuando termina cada pulso azul, o sea de la señal de entrada. [cite: 2113]
