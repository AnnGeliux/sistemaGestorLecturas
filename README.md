# 📚 Gestor de Lecturas

[![Licencia MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.2.4-brightgreen.svg)](https://www.djangoproject.com/)
[![MariaDB](https://img.shields.io/badge/MariaDB-10.x-blue.svg)](https://mariadb.org/)

Aplicación web desarrollada con **Django** y **MariaDB** para la gestión de lecturas, libros y metas de lectura.  
Permite a los usuarios registrar libros, seguir el progreso de sus lecturas, crear y asignar metas, tomar notas y visualizar estadísticas.  
Incluye funcionalidades para usuarios administradores y usuarios normales, control de permisos, y una interfaz moderna y responsiva desarrollada con **HTML**, **CSS** y **JavaScript**.

---

## ✨ Características principales
- **Registro y autenticación** de usuarios personalizados.
- **Gestión de libros** y progreso de lectura.
- **Creación y asignación de metas** de lectura a usuarios.
- **Notas** asociadas a libros y metas.
- **Panel de estadísticas** con gráficos.
- **Permisos diferenciados** para administradores y usuarios normales.
- **Interfaz responsiva y moderna**.

Ideal para **clubes de lectura**, **bibliotecas personales** o **instituciones educativas**.

---

## 🚀 Instalación en Windows

### 1️⃣ Requisitos previos
- **Python 3.10 o superior** instalado. [Descargar aquí](https://www.python.org/downloads/)
- **MariaDB 10.x** instalado y configurado. [Descargar aquí](https://mariadb.org/download/)
- **Git** instalado. [Descargar aquí](https://git-scm.com/download/win)

> Durante la instalación de Python en Windows, marca la opción **"Add Python to PATH"**.

---

### 2️⃣ Clonar el repositorio
Abre **PowerShell** o **CMD** y ejecuta:
```bash
git clone https://github.com/AnnGeliux/sistemaGestorLecturas.git
cd sistemaGestorLecturas
```

---

### 3️⃣ Crear y activar el entorno virtual
```bash
python -m venv venv
venv\Scripts\activate
```

---

### 4️⃣ Instalar dependencias
```bash
pip install -r requirements.txt
```

---

### 5️⃣ Configurar la base de datos MariaDB
1. Abre **HeidiSQL**, **MySQL Workbench** o la consola de MariaDB.
2. Crea la base de datos:
   ```sql
   CREATE DATABASE gestor_lecturas CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   ```
3. En el archivo `settings.py` de Django, configura las credenciales:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'gestor_lecturas',
           'USER': 'root',  # O tu usuario de MariaDB
           'PASSWORD': 'tu_contraseña',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   ```

---

### 6️⃣ Aplicar migraciones
```bash
python manage.py migrate
```

---

### 7️⃣ Iniciar el servidor
```bash
python manage.py runserver
```

Accede a la aplicación en: **http://127.0.0.1:8000/**

---

## 🧩 Tecnologías utilizadas
- [Python 3.10+](https://www.python.org/)
- [Django 5.2.4](https://www.djangoproject.com/)
- [MariaDB 10.x](https://mariadb.org/)
- [mysqlclient 2.2.7](https://pypi.org/project/mysqlclient/)
- [PyMySQL 1.1.1](https://pypi.org/project/PyMySQL/)
- [Pillow 11.3.0](https://pypi.org/project/Pillow/)
- [asgiref 3.9.1](https://pypi.org/project/asgiref/)
- [sqlparse 0.5.3](https://pypi.org/project/sqlparse/)
- [tzdata 2025.2](https://pypi.org/project/tzdata/)
- HTML5
- CSS3
- JavaScript
- [Chart.js](https://www.chartjs.org/) *(para las estadísticas)*


---

## 📄 Licencia
Este proyecto está bajo la licencia **MIT** - mira el archivo [LICENSE](LICENSE) para más detalles.

---
