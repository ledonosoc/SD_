# SD_Tarea2
Integrantes: Luis Donoso, Mauricio Inostroza

## Ejecución
En el directorio principal ejecutar el comando
```
docker-compose up
```

Para realizar el registro de un usuario ejecutar este comando en powershell 
```powershell
$headers = @{}
$headers.Add("Content-Type", "application/json")

$reqUrl = 'http://localhost:5000/register'
$body = '{
    "user": "testuser123@mail.com",
    "pass": "testuserpass123"
}'

$response = Invoke-RestMethod -Uri $reqUrl -Method Post -Headers $headers -ContentType 'application/json' -Body $body
$response | ConvertTo-Json
```
o realizar una request tipo POST con un body Json a través de Postman
```
url: http://localhost:5000/register
```
```
{
    "user": "testuser123@mail.com",
    "pass": "testuserpass123"
}
```
Luego se realiza un login (incorrecto), ejecutando el siguiente comando
```powershell
$headers = @{}
$headers.Add("Content-Type", "application/json")

$reqUrl = 'http://localhost:5000/login'
$body = '{
    "user": "testuser123@mail.com",
    "pass": "contraseñaincorrecta123"
}'

$response = Invoke-RestMethod -Uri $reqUrl -Method Post -Headers $headers -ContentType 'application/json' -Body $body
$response | ConvertTo-Json
```
o realizar una request tipo POST con un body Json a través de Postman
```
url: http://localhost:5000/login
```
```
{
    "user": "testuser123@mail.com",
    "pass": "contraseñaincorrecta123"
}
```
Finalmente para obtener los usuarios bloquedos, se ejecuta lo siguiente
```powershell
$headers = @{}
$headers.Add("Content-Type", "application/json")

$reqUrl = 'http://localhost:5000/blocked-users'
$body = '$headers = @{}

$reqUrl = 'http://localhost:5000/blocked'


$response = Invoke-RestMethod -Uri $reqUrl -Method Get -Headers $headers  
$response | ConvertTo-Json'

$response = Invoke-RestMethod -Uri $reqUrl -Method Get -Headers $headers -ContentType 'application/json' -Body $body
$response | ConvertTo-Json
```
o realizar una request tipo GET a través de Postman (o simplemente entrado desde un navegador a la url)
```
url: http://localhost:5000/blocked-users
```

## ¿Por qué Kafka funciona bien en este escenario?.
Como es un servicio que permite el procesado de mensajes de manera asíncrona, es ideal para almacenar la información de la actividad sospechosa de inicios se sesión, para posteriormente ser consultada a través de un consumidor y realizar el analisis de los tiempos en que fueron relizados los intentos.

## Basado en las tecnologías que usted tiene a su disposición (Kafka, backend) ¿Qué haría usted para manejar una gran cantidad de usuarios al mismo tiempo?.
Aprovechando la escalabilidad horizontal de kafka se pueden incrementar la cantidad de brokers utilizados para distribuir la información, y así disminuir la carga recibida entre las maquinas conectadas. Gracias a la fácil inclusion de nuevas máquinas de kafka se obtiene una baja latencia en el procesado de grandes volémenes de datos y además se facilita el procesado desde multiples fuentes.

