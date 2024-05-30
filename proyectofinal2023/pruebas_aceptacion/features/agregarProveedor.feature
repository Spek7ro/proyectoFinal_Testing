Característica: Agregar un nuevo proveedor
Como usuario quiero poder registrar 
un nuevo proveedor en el sistema

Escenario: Registro de un proveedor
Dado que ingreso a la url "http://localhost:8000/"
Y escribo mi usuario "admin123" y mi contraseña "1234"
Y presiono el botón de Ingresar
Y le doy clik en el enlace proveedores
Y luego clik en el boton de Agregar
Y escribo el RFC del proveedor "VECJ88032661F"
Y escribo la razon social del proveedor "Fertilizantes Agricolas"
Y escribo la dirección del proveedor "Calle Benito Juarez, 1234, Zac"
Y escribo el telefono del proveedor "5397238920"
Y escribo el correo del proveedor "ferA@gmail.com"
Y selecciono el estado del proveedor "Zacatecas"
Y selecciono el municipio del proveedor "Jerez"
Cuando presiono el boton Agregar
Entonces puedo ver el RFC del proveedor "VECJ88032661F" en la lista de proveedores
