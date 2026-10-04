# Mi Proyecto Automotriz - Evaluación Sumativa 2

## Propósito y Proyección
Este proyecto es una aplicación backend funcional desarrollada en Django, conectada a una base de datos PostgreSQL. Permite gestionar un catálogo automotriz utilizando operaciones CRUD, validaciones de seguridad y administración desde el panel de Django.

## Integrante
* Benjamin Millalonco

## Requisitos e Instalación (Para el evaluador)
1. Clonar el repositorio: `git clone https://github.com/hxcCoder/Evaluacion-sumativa-1.git`
2. Entrar a la carpeta: `cd evaluacion-sumativa-1`
3. Crear y activar entorno virtual:
   * Windows: `python -m venv .venv` y luego `.venv\Scripts\activate`
   * Mac/Linux: `python3 -m venv .venv` y luego `source .venv/bin/activate`
4. Instalar dependencias: `pip install -r requirements.txt`

## Configuración de Base de Datos y Variables de Entorno
1. Crear una base de datos vacía en PostgreSQL.
2. Copiar el archivo `.env.example` y renombrarlo a `.env`.
3. Abrir el archivo `.env` y completar los datos con las credenciales locales de su PostgreSQL:
   ```env
   SECRET_KEY=tu_secret_key
   DEBUG=True
   DB_NAME=tu_base_de_datos
   DB_USER=tu_usuario
   DB_PASSWORD=tu_password
   DB_HOST=localhost
   DB_PORT=5432

   Aplicar las migraciones para crear las tablas: python manage.py migrate

1) Crear un superusuario para acceder al admin: python manage.py createsuperuser

2) Ejecutar el servidor: python manage.py runserver

## Estructura del Proyecto
- core: Contiene las rutas generales y vistas estáticas.

- Autos: Implementa el CRUD de vehículos, con conexión a base de datos, validaciones y formularios web.

- Precios: Contiene el listado estático de precios de servicios.