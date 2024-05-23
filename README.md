# Api Seguros
Esta es una api que realiza solo operaciones GET básicas del ambito de seguros de vehículos, los datos vienen originalmente de una base de datos Oracle SQL y migrados a una base de datos Mongo DB

## Requerimientos
Se debe tener instalado python 3.10 o superior

## Levantar Aplicación

1- Iniciar entorno virtual
Ejecutar en consola:
```
pipenv shell
```

2- Instalar Librerias
Ejecutar en consola:
```
pipenv install
```

3- Iniciar servidor
Ejecutar en consola:
```
uvicorn main:app --reload
```

Para comprobar abrir en el navegador http://127.0.0.1:8000/docs, la url de la api sera http://127.0.0.1:8000

## Consideraciones
* la API hace opraciones muy pesadas asi a veces es mejor llamar a los métodos GET directamente desde el navegador que desde la herramienta de prueba de apis que da Fast-Api

## Estructura de carpetas
La estructura de carpetas en esta aplicación sigue este orden:

* División por dominio: cada carpeta corresponde a un dominio, ya sea de los vehiculos, de los clientes, las pólizas, etc
* División por funcionalidad, dentro de cada carpeta se realiza una división por funcionalidad dentro del propio dominio

### Dominios:
1. Car Brands - [`business/car_brands/`]: la marcas de los vehículos
2. Car Models - [`business/car_models/`]: los modelos de los vehículos
3. Car Types - [`business/car_types/`]: los tipos de vehículos
4. Cars - [`business/cars/`]: los vehículos registrados
5. Claims - [`business/claims/`]: los denunciós de siniestros cuando se quiere hacer efectiva la póliza
6. Insureds - [`business/insureds/`]: los clientes, en la jerga de seguros se les conoce como "asegurados"
7. Policies - [`business/policies/`]: las pólizas de seguro contratadas

### Modulos:
Cada dominio se divide en los siguientes sub modulos:
1. model.py: definición de las clases asociadas al dominio
2. database.py: las consultas a la base de datos
3. function.py: aqui esta el punto fuerte de la lógica, cualquier intervención, calculo o logica de negocio se maneja aca
4. api.py: solo define las rutas o urls posibles de llamar dentro de la api, por ejemplo para las marcas de vehículos se define "/car_brands" en el archivo api.py y cualquier funcionalidad de la api relacionada a las marcas de vehiculos se llama desde esa url. En estricto rigor debe ser una capa sin logica de negocio, sin embargo si se pueden especificar algunas cosas propias de cada endpoint de la api, como por ejemplo los códigos de error https, filtros por usuario logeado, manejo de ips, etc
