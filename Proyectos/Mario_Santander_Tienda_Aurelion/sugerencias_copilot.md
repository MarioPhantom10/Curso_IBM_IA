# 🧠 Proyecto Aurelion

## 📝 Sugerencias y Mejoras Aplicadas

Este documento resume las **sugerencias de mejora generadas durante el desarrollo del proyecto Tienda Aurelion**, incluyendo las aportadas por GitHub Copilot y las implementaciones realizadas para mejorar el flujo, la visualización y la compatibilidad con las tablas normalizadas.

---

### 🪄 1. Carga automática de datos al inicio

**💡 Sugerencia:**
Cargar automáticamente los archivos Excel al iniciar el programa, en lugar de solicitarlos manualmente.

**✅ Aplicación:**

* El código ahora carga los datos al inicio.
* Se valida que los archivos se carguen correctamente antes de mostrar el menú principal.
* Se implementó manejo de errores con `try-except` para informar al usuario si ocurre algún problema.

---

### 🧭 2. Menú interactivo simplificado

**💡 Sugerencia:**
Mostrar únicamente las opciones de consulta, eliminando opciones de carga manual.

**✅ Aplicación:**
El menú ahora contiene solo las opciones:

* 1.Consultar clientes con más compras

* 2.Consultar productos más vendidos

* 3.Consultar ventas por medio de pago

* 4.Consultar ventas en un período

* 5.Salir

* El menú es claro, con numeración consecutiva y mensajes informativos.

* Se repite hasta que el usuario decide salir.

---

### ⚙️ 3. Funciones bien nombradas y código modular

**💡 Sugerencia:**
Dividir el código en funciones específicas y descriptivas para cada consulta.

**✅ Aplicación:**
Funciones principales:

* `cargar_clientes()`
* `cargar_productos()`
* `cargar_ventas()`
* `cargar_detalle_ventas()`
* `clientes_con_mas_compras()`
* `productos_mas_vendidos()`
* `ventas_por_medio_pago()`
* `ventas_en_periodo()`

> ⚠️ **Nota:** El código modular facilita el mantenimiento y escalabilidad futura.

---

### 🗃️ 4. Normalización de tablas

**💡 Sugerencia:**
Evitar redundancias y mantener consistencia en las tablas: usar solo identificadores para relacionar datos.

**✅ Aplicación:**

* `detalle_ventas` contiene solo `id_venta`, `id_producto` y `cantidad`.
* `productos` contiene `precio_unitario` y `nombre_producto`.
* `ventas` contiene `id_venta`, `id_cliente`, `medio_pago` y `fecha`.

> ⚠️ **Nota:** Esto permite calcular valores como `importe = cantidad × precio_unitario` sin depender de columnas redundantes.

---

### 📊 5. Visualización de resultados y ranking

**💡 Sugerencia:**
Mostrar ranking numérico y destacar los top 3 en todas las consultas.

**✅ Aplicación:**

* Se agregó ranking en **clientes, productos y medios de pago**.
(En un momento implemente colores ANSI, pero el codigo no quedaba claro, asi que opte por eliminarlos y dejar el texto en blanco)

**Ejemplo de salida en el README:**

#### Clientes con más compras

| #   | Cliente          | Total Compras  |
| --- | ---------------- | -------------  |
| 1 | Bruno Diaz       | 5             |
| 2 | Agustina Flores  | 4             |
| 3 | Olivia Gomez     | 4             |
| 4 | Camila Rodriguez | 4              |
| 5 | Santiago Diaz    | 4              |

#### Productos más vendidos

| #   | Producto                   | Cantidad |
| --- | -------------------------- | -------- |
| 1 | Salsa de Tomate 500g       | 27       |
| 2 | Queso Rallado 150g         | 26       |
| 3 | Hamburguesas Congeladas x4 | 24       |
| 4 | Aceitunas Verdes 200g      | 22       |
| 5 | Vino Blanco 750ml          | 22       |

#### Ventas por medio de pago

| #   | Medio de Pago | Total Ventas |
| --- | ------------- | ------------ |
| 1 | efectivo      | 37           |
| 2 | qr            | 30           |
| 3 | transferencia | 27           |
| 4 | tarjeta       | 26           |

---

### 📅 6. Formato y validación de fechas

**💡 Sugerencia:**
Mostrar fechas en formato **DD-MM-YYYY** y validar que estén dentro del rango de los datos.

**✅ Aplicación:**

* Periodo válido mostrado al usuario antes de ingresar fechas.
* Validación de que las fechas ingresadas no excedan el rango disponible.

### además del total y el top 3 de productos, también muestra un resumen de ventas por medio de pago dentro del periodo de tiempo seleccionado, todo esto con formato limpio

---

Todas estas mejoras aplicadas optimizan la **estructura, claridad y calidad del código**, facilitan la lectura de resultados, aseguran consistencia de datos y mejoran la experiencia del usuario.

En un primer momento, luego de tener funcional al programa, aplique con la ayuda de copilot color ANSI, al menu y opciones. la verdad que visualmente quedaba mucho mejor, pero el codigo no era muy legible, asi que opte por modificarlo y dejarlo solamente con el texto basico en blanco.

---

Autor

**Mario Santander**
Proyecto educativo desarrollado en Python y bases de datos.
