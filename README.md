# Mi Proyecto Automotriz - Evaluación Sumativa 2

## Propósito y Proyección
Este proyecto es una aplicación backend funcional desarrollada en Django, conectada a una base de datos PostgreSQL. Permite gestionar un catálogo automotriz utilizando operaciones CRUD, validaciones de seguridad y administración desde el panel de Django.

## Integrante
* Benjamin Millalonco

## Requisitos e Instalación (Para el evaluador)
1. Clonar el repositorio: `git clone https://github.com/hxcCoder/Evaluacion-sumativa-3.git`
2. Entrar a la carpeta: `cd evaluacion-sumativa-3`
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

---

## Usuarios de Prueba para Evaluación (Sin contraseñas reales)

Para probar los endpoints protegidos de la API REST mediante Postman o Insomnia:

* **Usuario de prueba:** `admin_api` (o cualquier usuario creado con `createsuperuser`)
* **Contraseña:** *(Definida localmente al ejecutar `createsuperuser`)*

---

## Estructura de Endpoints de la API REST

### Autenticación JWT
| Método | Ruta | Propósito | Protección |
| :--- | :--- | :--- | :--- |
| **POST** | `/api/token/` | Obtener tokens `access` y `refresh` | Pública |
| **POST** | `/api/token/refresh/` | Renovar el token de acceso vencido | Pública |

### Recurso Principal: Vehículos (`/api/autos/`)
| Método | Ruta de referencia | Propósito | Protección |
| :--- | :--- | :--- | :--- |
| **GET** | `/api/autos/` | Listar todos los vehículos del catálogo | Pública |
| **GET** | `/api/autos/<id>/` | Consultar el detalle de un vehículo específico | JWT Obligatorio |
| **POST** | `/api/autos/` | Registrar un nuevo vehículo | JWT Obligatorio |
| **PUT** | `/api/autos/<id>/` | Actualizar un vehículo existente | JWT Obligatorio |
| **DELETE** | `/api/autos/<id>/` | Eliminar un vehículo del catálogo | JWT Obligatorio |

> **Nota de Seguridad:** Las solicitudes protegidas requieren el envío del token de acceso en el encabezado HTTP de la petición:
> `Authorization: Bearer <tu_access_token>`