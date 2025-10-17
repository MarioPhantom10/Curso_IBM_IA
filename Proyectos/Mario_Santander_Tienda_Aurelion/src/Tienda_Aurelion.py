import pandas as pd
import os
import sys

# ===================== Funciones de carga =====================
def cargar_clientes():
    df = pd.read_excel(os.path.join(DB_DIR, 'clientes.xlsx'))
    df.columns = df.columns.str.strip()
    return df

def cargar_productos():
    df = pd.read_excel(os.path.join(DB_DIR, 'productos.xlsx'))
    df.columns = df.columns.str.strip()
    return df

def cargar_ventas():
    df = pd.read_excel(os.path.join(DB_DIR, 'ventas.xlsx'))
    df.columns = df.columns.str.strip()
    df['fecha'] = pd.to_datetime(df['fecha'])
    return df

def cargar_detalle_ventas():
    df = pd.read_excel(os.path.join(DB_DIR, 'detalle_ventas.xlsx'))
    df.columns = df.columns.str.strip()
    return df

# ===================== Función para imprimir top 3 =====================
def imprimir_top(df, columnas, titulo):
    print(f"\n--- {titulo} ---")
    for i, row in df.iterrows():
        idx = i + 1
        line = f"{idx:<3}"  # ranking
        for col in columnas:
            line += f"{str(row[col]):<30}"
        print(line)

# ===================== Funciones de visualización =====================
def mostrar_bienvenida():
    print("="*60)
    print(" Bienvenido al programa de gestión de datos")
    print("           Tienda Aurelion")
    print("="*60)
    print("Este programa le permitirá consultar y analizar")
    print("los datos de clientes, productos y ventas de la tienda.\n")

def mostrar_menu():
    print("\nSeleccione una opción:")
    print("1. Consultar clientes con más compras")
    print("2. Consultar productos más vendidos")
    print("3. Consultar ventas por medio de pago")
    print("4. Consultar ventas en un periodo")
    print("5. Salir")

# ===================== Consultas =====================
def clientes_con_mas_compras(ventas, clientes):
    compras = ventas['id_cliente'].value_counts().reset_index()
    compras.columns = ['id_cliente', 'total_compras']
    resultado = compras.merge(clientes, on='id_cliente')
    top_clientes = resultado[['nombre_cliente', 'total_compras']].sort_values('total_compras', ascending=False).head(10)
    top_clientes.reset_index(drop=True, inplace=True)
    imprimir_top(top_clientes, ['nombre_cliente','total_compras'], "Clientes con más compras")

def productos_mas_vendidos(detalle_ventas, productos):
    vendidos = detalle_ventas.groupby('id_producto')['cantidad'].sum().reset_index()
    resultado = vendidos.merge(productos, on='id_producto')
    top_productos = resultado[['nombre_producto', 'cantidad']].sort_values('cantidad', ascending=False).head(10)
    top_productos.reset_index(drop=True, inplace=True)
    imprimir_top(top_productos, ['nombre_producto','cantidad'], "Productos más vendidos")

def ventas_por_medio_pago(ventas):
    medios = ventas['medio_pago'].value_counts().reset_index()
    medios.columns = ['medio_pago', 'total_ventas']
    medios.reset_index(drop=True, inplace=True)
    imprimir_top(medios, ['medio_pago','total_ventas'], "Ventas por medio de pago")

def ventas_en_periodo(ventas, detalle_ventas, productos, fecha_inicio, fecha_fin):
    try:
        fecha_inicio_dt = pd.to_datetime(fecha_inicio, dayfirst=True)
        fecha_fin_dt = pd.to_datetime(fecha_fin, dayfirst=True)
    except Exception:
        print("⚠️ Formato de fecha inválido. Debe ser DD-MM-YYYY.")
        return

    fecha_min = ventas['fecha'].min()
    fecha_max = ventas['fecha'].max()
    if fecha_inicio_dt < fecha_min or fecha_fin_dt > fecha_max:
        print("⚠️ Fechas fuera de rango.")
        print(f"Periodo válido: {fecha_min.strftime('%d-%m-%Y')} a {fecha_max.strftime('%d-%m-%Y')}")
        return

    filtro = (ventas['fecha'] >= fecha_inicio_dt) & (ventas['fecha'] <= fecha_fin_dt)
    ventas_filtradas = ventas[filtro]

    if ventas_filtradas.empty:
        print("⚠️ No se encontraron ventas en el rango indicado.")
        return

    detalle_filtrado = detalle_ventas[detalle_ventas['id_venta'].isin(ventas_filtradas['id_venta'])]
    detalle_con_precio = detalle_filtrado.merge(
        productos[['id_producto', 'nombre_producto', 'precio_unitario']],
        on='id_producto',
        how='left'
    )
    detalle_con_precio['importe'] = detalle_con_precio['cantidad'] * detalle_con_precio['precio_unitario']

    print("="*60)
    print(f"--- Ventas del {fecha_inicio_dt.strftime('%d-%m-%Y')} al {fecha_fin_dt.strftime('%d-%m-%Y')} ---")
    print("="*60)

    total = detalle_con_precio['importe'].sum()
    print(f"Total ventas: ${total:,.2f}")
    print(f"Ventas registradas: {len(ventas_filtradas)}")
    print(f"Productos vendidos: {detalle_con_precio['cantidad'].sum()}\n")

    # ==== TOP 3 PRODUCTOS ====
    top_productos = (
        detalle_con_precio.groupby('nombre_producto')['cantidad']
        .sum()
        .reset_index()
        .sort_values('cantidad', ascending=False)
        .head(3)
    )

    if not top_productos.empty:
        print("--- Top 3 productos más vendidos ---")
        for i, row in enumerate(top_productos.itertuples(), 1):
            print(f"{i}. {row.nombre_producto:<40} {int(row.cantidad)} unidades")
        print()

    # ==== MEDIOS DE PAGO ====
    resumen_medios = (
        ventas_filtradas
        .merge(detalle_con_precio[['id_venta', 'importe']], on='id_venta', how='left')
        .groupby('medio_pago')['importe']
        .sum()
        .reset_index()
        .sort_values('importe', ascending=False)
    )

    if not resumen_medios.empty:
        print("--- Ventas por medio de pago ---")
        for _, row in resumen_medios.iterrows():
            print(f"{row['medio_pago']:<20} ${row['importe']:,.2f}")

    print("="*60)
    print("Consulta completada con éxito.\n")

# ===================== Programa principal =====================
if __name__ == "__main__":
    # Verificar si openpyxl está instalado
    try:
        import openpyxl
    except ImportError:
        print("Error: falta la librería 'openpyxl'.")
        print("Instálala con: pip install openpyxl")
        sys.exit(1)

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DB_DIR = os.path.join(BASE_DIR, '..', 'database')

    try:
        clientes = cargar_clientes()
        productos = cargar_productos()
        ventas = cargar_ventas()
        detalle_ventas = cargar_detalle_ventas()
        print("Datos cargados correctamente.\n")
    except Exception as e:
        print(f"Error al cargar los datos: {e}")
        sys.exit(1)

    mostrar_bienvenida()

    while True:
        mostrar_menu()
        opcion = input("Ingrese el número de la opción deseada: ").strip()

        if opcion == "5":
            print("="*60)
            print("Fin del programa. ¡Hasta luego!")
            print("="*60)
            break
        elif opcion == "1":
            clientes_con_mas_compras(ventas, clientes)
        elif opcion == "2":
            productos_mas_vendidos(detalle_ventas, productos)
        elif opcion == "3":
            ventas_por_medio_pago(ventas)
        elif opcion == "4":
            fecha_min = ventas['fecha'].min().strftime('%d-%m-%Y')
            fecha_max = ventas['fecha'].max().strftime('%d-%m-%Y')
            print(f"Ingrese las fechas en formato DD-MM-YYYY")
            print(f"Periodo válido de datos: {fecha_min} a {fecha_max}")
            fecha_inicio = input("Fecha de inicio: ").strip()
            fecha_fin = input("Fecha de fin: ").strip()
            ventas_en_periodo(ventas, detalle_ventas, productos, fecha_inicio, fecha_fin)
        else:
            print("Opción no válida. Intente de nuevo.")
