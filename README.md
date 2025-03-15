# 📌 Proyecto: Registro de Usuarios

## 📝 Descripción

Este es un pequeño sistema de **registro de usuarios** en Python que permite:

- Registrar nuevos usuarios con validaciones para **nombre de usuario, contraseña, email y edad**.
- Ver la lista de usuarios registrados en una **tabla con Pandas**.
- Un menú interactivo para navegar entre las opciones.

## 🚀 Características

✅ Validación de **nombre de usuario** (evita duplicados).\
✅ Validación de **contraseña** (mínimo 6 caracteres).\
✅ Validación de **email** (formato correcto: `usuario@dominio.com`).\
✅ Validación de **edad** (número positivo).\
✅ Uso de **Pandas** para mostrar usuarios registrados en formato tabla.\
✅ Uso de `os.system('cls')` para limpiar la terminal en Windows/Linux.

## 📂 Estructura del Proyecto

```
📂 registro_usuarios/
│── 📂 src/                 # Código fuente
│   │── 📄 menu.py          # Menú de navegación
│   │── 📄 registro.py      # Funciones de registro
│   │── 📄 data.py          # Almacenamiento de datos
│── 📄 requirements.txt     # Librerías necesarias
│── 📄 README.md            # Documentación del proyecto
│── 📄 .gitignore           # Archivos a ignorar en Git
│── 📄 main.py              # Archivo principal
│── 📄 LICENSE              # Archivo de licencia
```

## 🛠 Instalación

1️⃣ Clona el repositorio:

```sh
git clone https://github.com/BrynStvn/registro_usuarios.git
```

2️⃣ Entra en la carpeta del proyecto:

```sh
cd registro_usuarios
```

3️⃣ Instala las dependencias necesarias:

```sh
pip install -r requirements.txt
```

## ▶️ Uso

Ejecuta el siguiente comando para iniciar el programa:

```sh
python src/main.py
```

Sigue las instrucciones en pantalla para **registrar usuarios, ver la lista de usuarios o salir**.

## 📌 Requisitos

- **Python 3.8+**
- **Librerías:** Pandas

## 📜 Licencia

Este proyecto es de código abierto bajo la licencia MIT.

---

📌 **Autor:** Brayan Padilla Yande 👨‍💻

