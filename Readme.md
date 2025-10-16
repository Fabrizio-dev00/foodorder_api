# 🍔 foodorder_api — Gestor de Restaurante

## 🧾 Descripción del Proyecto
**foodorder_api** es una API REST desarrollada con **Django** y **Django REST Framework (DRF)** que permite gestionar **Platos** y **Pedidos** de un restaurante.  
Cada pedido puede contener uno o varios platos, y el sistema calcula el total del pedido según los precios de los platos asociados.

> Todo el CRUD se gestiona mediante endpoints de DRF, sin utilizar el panel de administración de Django.

---

## ⚙️ Tecnologías Usadas
| Tecnología | Descripción |
|-------------|--------------|
| 🐍 **Python 3.x** | Lenguaje principal del proyecto |
| 🌐 **Django 4.x** | Framework web backend |
| ⚙️ **Django REST Framework** | Creación de API RESTful |
| 🗃️ **SQLite3** | Base de datos por defecto |

---

## 🚀 Instrucciones para Ejecutar el Servidor

### 1️⃣ Clonar el repositorio
```bash
git clone <tu-repo-url>
cd foodorder_api
2️⃣ Crear entorno virtual e instalar dependencias
bash
Copiar código
python -m venv venv
# En Windows:
venv\Scripts\activate
# En Linux/Mac:
source venv/bin/activate

pip install -r requirements.txt
3️⃣ Aplicar migraciones
bash
Copiar código
python manage.py makemigrations
python manage.py migrate
4️⃣ Ejecutar el servidor
bash
Copiar código
python manage.py runserver
La API estará disponible en:
👉 http://127.0.0.1:8000/api/

📚 Endpoints Disponibles
🥘 Platos
Método	Endpoint	Descripción
GET	/api/platos/	Listar todos los platos
POST	/api/platos/	Crear un nuevo plato
GET	/api/platos/{id}/	Ver detalle de un plato
PUT / PATCH	/api/platos/{id}/	Editar un plato existente
DELETE	/api/platos/{id}/	Eliminar un plato

Ejemplo POST /api/platos/
json
Copiar código
{
  "nombre": "Ceviche Mixto",
  "precio": "25.00",
  "categoria": "Principal"
}
🧾 Pedidos
Método	Endpoint	Descripción
GET	/api/pedidos/	Listar todos los pedidos
POST	/api/pedidos/	Crear un nuevo pedido
GET	/api/pedidos/{id}/	Ver detalle de un pedido
PUT / PATCH	/api/pedidos/{id}/	Editar un pedido existente
DELETE	/api/pedidos/{id}/	Eliminar un pedido
GET	/api/pedidos/?search=texto	Buscar por estado o nombre de plato

Ejemplo POST /api/pedidos/
json
Copiar código
{
  "estado": "PENDIENTE",
  "platos": [1, 2]
}
Ejemplo de respuesta
json
Copiar código
{
  "id": 1,
  "fecha": "2025-10-15T18:40:00Z",
  "total": "45.00",
  "estado": "PENDIENTE",
  "platos": [
    { "id": 1, "nombre": "Ceviche Mixto", "precio": "25.00", "categoria": "Principal" },
    { "id": 2, "nombre": "Lomo Saltado", "precio": "20.00", "categoria": "Principal" }
  ]
}
🔍 Búsqueda
Puedes buscar pedidos por estado o por nombre de plato utilizando el parámetro ?search=.

Ejemplo:

bash
Copiar código
GET /api/pedidos/?search=PENDIENTE
✨ Autor
Desarrollado por Fabrizio Jimenez
📅 Octubre 2025