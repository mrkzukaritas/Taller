# 📌 Proyecto Django REST APIs  

Este proyecto implementa **dos APIs REST** con Django REST Framework y está desplegado en **Render**.  

---

## 📂 Estructura del Proyecto
- **projects** → API para gestionar proyectos.  
- **tareas** → API para gestionar tareas.  

---

## 🔗 Endpoints disponibles  

### 📁 API de Proyectos  
Base URL:  
https://<tu-app>.onrender.com/api/projects/

swift
Copy code

| Método   | Endpoint                 | Descripción                    |
|----------|--------------------------|--------------------------------|
| `GET`    | `/api/projects/`         | Listar todos los proyectos     |
| `POST`   | `/api/projects/`         | Crear un nuevo proyecto        |
| `GET`    | `/api/projects/<id>/`    | Obtener un proyecto específico |
| `PUT`    | `/api/projects/<id>/`    | Actualizar un proyecto         |
| `DELETE` | `/api/projects/<id>/`    | Eliminar un proyecto           |

#### ✅ Ejemplo de Proyecto (JSON)  
```
{
  "id": 1,
  "nombre": "Plataforma Web",
  "descripcion": "Un sistema para gestión de usuarios"
}
```
### 📋 API de Tareas  
Base URL:  
https://taller-api-0w81.onrender.com/Tareas/api/tareas/


| Método   | Endpoint                        | Descripción                   |
|----------|---------------------------------|-------------------------------|
| `GET`    | `/Tareas/api/tareas/`           | Listar todas las tareas       |
| `POST`   | `/Tareas/api/tareas/`           | Crear una nueva tarea         |
| `GET`    | `/Tareas/api/tareas/<id>/`      | Obtener una tarea específica  |
| `PUT`    | `/Tareas/api/tareas/<id>/`      | Actualizar una tarea          |
| `DELETE` | `/Tareas/api/tareas/<id>/`      | Eliminar una tarea            |

#### ✅ Ejemplo de Tarea (JSON)  
```
{
  "id": 1,
  "nombre": "Configurar base de datos",
  "completada": false
}
```

🛠️ Tecnologías usadas
Django 5+

Django REST Framework

drf-spectacular (para documentación OpenAPI / Swagger)

Render (deploy)

📖 Documentación interactiva
Puedes explorar la documentación generada automáticamente con Swagger:

👉 https://taller-api-0w81.onrender.com/docs/
