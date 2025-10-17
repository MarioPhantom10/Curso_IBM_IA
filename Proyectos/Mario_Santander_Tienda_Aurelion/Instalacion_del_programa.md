# Autor: Mario Santander

---
Estructura del Proyecto

Mario_Santander_Tienda_Aurelion/
│
├── 📁 assets/
│ └── diagrama_flujo_programa.png # Diagrama visual del flujo del programa
│
├── 📁 database/
│ ├── clientes.xlsx # Datos de clientes
│ ├── productos.xlsx # Datos de productos
│ ├── ventas.xlsx # Datos de ventas
│ └── detalle_ventas.xlsx # Detalle de productos vendidos
│
├── 📁 src/
│ └── Tienda_Aurelion.py # Código principal del programa (archivo que ejecutás)
│
├── 📄 README_Aurelion.md # Descripción general del proyecto
├── 📄 sugerencias_copilot.md # Archivo con mejoras, sugerencias
└── 📄 instalacion_del_programa.md # Instrucciones de instalación

---

## Clonar o descargar el repositorio

git clone / descargar zip

https://github.com/MarioPhantom10/Curso_IBM_IA/tree/main/Proyectos/Mario_Santander_Tienda_Aurelion

## Una vez descargado o clonado

cd Mario_Santander_Tienda_Aurelion

## Crear (opcional) un entorno virtual. Esto evita conflictos con otras instalaciones de Python

python -m venv venv

## Activar el entorno virtual - En Windows

venv\Scripts\activate

## Instalar dependencias necesarias - El programa usa pandas y openpyxl

pip install pandas openpyxl

## Ir a la carpeta del código y correr el archivo principal

cd src
python Tienda_Aurelion.py

## Si todo está bien, debería verse algo así

 Bienvenido al programa de gestión de datos
           Tienda Aurelion

Este programa le permitirá consultar y analizar
los datos de clientes, productos y ventas de la tienda.

## Interactuar con el menú

El usuario simplemente elige opciones

Seleccione una opción:

1. Consultar clientes con más compras
2. Consultar productos más vendidos
3. Consultar ventas por medio de pago
4. Consultar ventas en un periodo
5. Salir
