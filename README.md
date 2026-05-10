# Practica de Laboratorio: Modulaciones Digitales M-PSK

Este repositorio contiene el desarrollo y los archivos correspondientes a la practica de modulaciones por desplazamiento de fase (M-PSK). El objetivo es analizar el comportamiento de estas señales en banda base y su respuesta en frecuencia.

## Contenido de la rama
En este espacio se encuentran los siguientes recursos:
- Carpeta GNURadio: Contiene los flujogramas en formato .grc con las implementaciones de QPSK y 8-PSK.
- Carpeta Informe: Contiene el documento final con los analisis detallados y las mediciones obtenidas.


## Instrucciones para el uso de los archivos
Para replicar los resultados obtenidos en el laboratorio se deben seguir estos pasos:
1. Abrir el software de radio definida por software (GNURadio).
2. Cargar alguno de los archivos .grc ubicados en la carpeta de GNURadio.
3. Ejecutar la simulacion para observar el diagrama de constelacion y el espectro de potencia.
4. Se pueden modificar los bloques de ruido o las tablas de verdad para ver como cambia la posicion de los puntos y la tasa de error.

## Puntos clave del analisis
- Relacion entre la tasa de simbolos (Rs) y el ancho de banda ocupado por la señal.
- Observacion de la envolvente compleja para identificar variaciones de fase y amplitud.
- Impacto del ruido en la dispersion de los simbolos dentro del plano complejo.
- Diferencias de robustez entre esquemas de distinto orden (M).

