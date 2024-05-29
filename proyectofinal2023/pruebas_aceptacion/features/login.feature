Característica: Inicio de sesión
Como usuario del sistema del INIFAP
quiero iniciar sesión
para realizar mis actividades cotidianas.

Escenario: Credenciales validas
Dado que ingreso a la url "http://localhost:8000/"
Y escribo mi usuario "admin" y mi contraseña "1234"
Cuando presiono el botón de Ingresar
Entonces puedo ver en el banner "Administración de Django"

Escenario: Credenciales invalidas
Dado que ingreso a la url "http://localhost:8000/admin/login"
Y escribo mi usuario "usuario123" y mi contraseña "12345678"
Cuando presiono el botón de Ingresar
Entonces puedo ver el mensaje "Por favor introduza nombre de usuario y contraseña correctos de una cuenta de staff. Note que puede que ambos campos sean estrictos en relación a diferencias entre mayúsculas y minúsculas."
