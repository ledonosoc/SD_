# SD_Tarea2
Integrantes: Luis Donoso, Mauricio Inostroza

## Ejecución
En el directorio principal ejecutar el comando docker-compose up

## ¿Por qué Kafka funciona bien en este escenario?.
Como es un servicio que permite el procesado de mensajes de manera asíncrona, es ideal para almacenar la información de la actividad sospechosa de inicios se sesión, para posteriormente ser consultada a través de un consumidor y realizar el analisis de los tiempos en que fueron relizados los intentos.

## Basado en las tecnologías que usted tiene a su disposición (Kafka, backend) ¿Qué haría usted para manejar una gran cantidad de usuarios al mismo tiempo?.
Aprovechando la escalabilidad horizontal de kafka se pueden incrementar la cantidad de brokers utilizados para distribuir la información, y así disminuir la carga recibida entre las maquinas conectadas. Gracias a la fácil inclusion de nuevas máquinas de kafka se obtiene una baja latencia en el procesado de grandes volémenes de datos y además se facilita el procesado desde multiples fuentes.