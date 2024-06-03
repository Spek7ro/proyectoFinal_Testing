Característica: Generar reporte pdf
Como usuario quiero poder generar 
un reporte pdf de los proveedores, 
proyectos, cuentas bancarias y costos

Escenario: Generar reporte pdf de los proveedores
Dado que ingreso a la url "http://localhost:8000/"
Y escribo mi usuario "admin123" y mi contraseña "1234"
Y presiono el botón de Ingresar
Y le doy clik en el enlace proveedores
Y luego doy clik en el boton de lista de proveedores
Y luego doy clik en el boton de generar reporte pdf
Y guardo el archivo pdf en "C:/Users/20201/Downloads" con el nombre "reporte_proveedores.pdf"
Entonces ingreso a la url "C:/Users/20201/Downloads/reporte_proveedores.pdf" y puedo ver el pdf 

Escenario: Generar reporte pdf de los proyectos
Dado que ingreso a la url "http://localhost:8000/"
Y escribo mi usuario "admin123" y mi contraseña "1234"
Y presiono el botón de Ingresar
Y le doy clik en el enlace proyectos
Y luego doy clik en el boton de lista de proyectos
Y luego doy clik en el boton de generar reporte pdf
Y guardo el archivo pdf en "C:/Users/20201/Downloads" con el nombre "reporte_proyectos.pdf"
Entonces ingreso a la url "C:/Users/20201/Downloads/reporte_proyectos.pdf" y puedo ver el pdf 

Escenario: Generar reporte pdf de las cuentas bancarias
Dado que ingreso a la url "http://localhost:8000/"
Y escribo mi usuario "admin123" y mi contraseña "1234"
Y presiono el botón de Ingresar
Y le doy clik en el enlace Cuentas Bancarias
Y luego doy clik en el boton de lista de cuentas bancarias
Y luego doy clik en el boton de generar reporte pdf
Y guardo el archivo pdf en "C:/Users/20201/Downloads" con el nombre "reporte_cuentas.pdf"
Entonces ingreso a la url "C:/Users/20201/Downloads/reporte_cuentas.pdf" y puedo ver el pdf

Escenario: Generar reporte pdf de los costos
Dado que ingreso a la url "http://localhost:8000/"
Y escribo mi usuario "admin123" y mi contraseña "1234"
Y presiono el botón de Ingresar
Y le doy clik en el enlace costos
Y luego doy clik en el boton de lista de costos
Y luego doy clik en el boton de generar reporte pdf
Y guardo el archivo pdf en "C:/Users/20201/Downloads" con el nombre "reporte_costos.pdf"
Entonces ingreso a la url "C:/Users/20201/Downloads/reporte_costos.pdf" y puedo ver el pdf
