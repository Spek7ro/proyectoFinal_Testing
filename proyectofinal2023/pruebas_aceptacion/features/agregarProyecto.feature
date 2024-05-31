Característica: Agregar un nuevo proyecto
Como usuario quiero poder registrar 
un nuevo proyecto en el sistema

Escenario: Registro de un proyecto
Dado que ingreso a la url "http://localhost:8000/"
Y escribo mi usuario "admin123" y mi contraseña "1234"
Y presiono el botón de Ingresar
Y le doy clik en el enlace proyectos
Y luego clik en el boton de agregar proyecto
Y escribo el numero del proyecto "10"
Y escribo el nombre del proyecto "Sistema de fertilizantes"
Y escribo el objetivo del proyecto "Proyecto de gestión de fertilizantes para la industria agrícola"
Y escribo el presupuesto del proyecto "2000000"
Y escribo la duracion del proyecto "8"
Y escribo el responsable del proyecto "Juan Perez"
Y selecciono al proveedor del proyecto "Fertilizantes Agricolas"
Cuando presiono el boton Agregar
Entonces puedo ver el nombre del proyecto "Sistema de fertilizantes" en la lista de proyectos
