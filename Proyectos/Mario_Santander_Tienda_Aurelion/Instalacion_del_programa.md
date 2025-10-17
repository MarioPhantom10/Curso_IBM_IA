# 🏪 Tienda Aurelion  

### Autor: **Mario Santander**

---

## 📂 Estructura del Proyecto

```

Mario_Santander_Tienda_Aurelion/
│
├── 📁 assets/
│   └── diagrama_flujo_programa.png        # Diagrama visual del flujo del programa
│
├── 📁 database/
│   ├── clientes.xlsx                      # Datos de clientes
│   ├── productos.xlsx                     # Datos de productos
│   ├── ventas.xlsx                        # Datos de ventas
│   └── detalle_ventas.xlsx                # Detalle de productos vendidos
│
├── 📁 src/
│   └── Tienda_Aurelion.py                 # Código principal del programa
│
├── 📄 README_Aurelion.md                  # Descripción general del proyecto
├── 📄 sugerencias_copilot.md              # Archivo con mejoras y sugerencias
└── 📄 Instalacion_del_programa.md          # Instrucciones de instalación

````

---

## Descargar el repositorio

```
Entrá a:
👉 https://github.com/MarioPhantom10/Curso_IBM_IA/tree/main/Proyectos/Mario_Santander_Tienda_Aurelion

Hacés clic en "Code" → "Download ZIP"

Extraés el ZIP en tu equipo.
```

---

## 📁 Ingresar al directorio del proyecto

```bash
cd Mario_Santander_Tienda_Aurelion
```

---

## 🧪 Crear (opcional) un entorno virtual

Esto evita conflictos con otras instalaciones de Python:

```bash
python -m venv venv
```

---

## ⚙️ Activar el entorno virtual

**En Windows:**

```bash
venv\Scripts\activate
```

**En macOS / Linux:**

```bash
source venv/bin/activate
```

---

## 📦 Instalar dependencias necesarias

El programa utiliza las librerías `pandas` y `openpyxl`:

```bash
pip install pandas openpyxl
```

---

## ▶️ Ejecutar el programa

Ir a la carpeta del código fuente y correr el archivo principal:

```bash
cd src
python Tienda_Aurelion.py
```

---

## 💻 Ejemplo de salida esperada

```
Bienvenido al programa de gestión de datos
           Tienda Aurelion

Este programa le permitirá consultar y analizar
los datos de clientes, productos y ventas de la tienda.
```

---

## 🧩 Interactuar con el menú

El usuario puede seleccionar una de las siguientes opciones:

```
Seleccione una opción:
1. Consultar clientes con más compras
2. Consultar productos más vendidos
3. Consultar ventas por medio de pago
4. Consultar ventas en un periodo
5. Salir
```

---

## 💡 Recomendaciones

* Asegurate de tener **Python 3.8 o superior** instalado.
* Si el programa no encuentra los archivos `.xlsx`, revisá que estén dentro de la carpeta `database/`.
* Podés personalizar los colores o textos del menú modificando el archivo `Tienda_Aurelion.py` dentro de `src/` Utilizando colores ANSI.

---

## Autor

**Mario Santander**
✨ *Gracias por utilizar **Tienda Aurelion**. Desarrollado como parte del curso **IBM de Inteligencia Artificial**.*
