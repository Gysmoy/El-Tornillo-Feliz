# Librerías Importadas
from tkinter import ttk
from tkinter import *
from datetime import date
from datetime import datetime
import os

# Funciones
def previsualizar():
    # Producto
    prevprod.set('')
    prevprod.set(productos[getcodigo.get()][0])
    # Precio x Cantidad
    prevcost.set('')
    prevcost.set('{} {}'.format('S/.', abs( round(float(productos[getcodigo.get()][2]) * int(getcost.get()) , 2) ) ))

def insertar():
    try:
        codigo = getcodigo.get()
        descripcion = productos[codigo][0]
        unidad = productos[codigo][1]
        cantidad = abs(int(getcost.get()))
        precio = productos[codigo][2]
        subtotal = round(cantidad * precio , 2)

        boleta.append([codigo, descripcion, unidad, cantidad, precio, subtotal])
        tabla()
    except:
        print('¡Hubo un error al insertar datos en la boleta!')

def imprimir():
    os.system ("cls")
    today = date.today()
    now = datetime.now()
    # Header
    print('''{}
{:^100}
{}
{:50}{:50}
{:50}{:50}
{}
{}
{}
┃{:^10}┃{:^51}┃{:^8}┃{:^6}┃{:^8}┃{:^10}┃
{}'''.format(
    100*'━',
    'Ferretería El Tornillo Feliz 🔧🔨',
    100*'━',
    'DNI       : ' + str(DNI.get()), 'Fecha     : ' + str(today.day) + '-' + str(today.month) + '-' + str(today.year) + ' ' + str(now.hour) + ':' + str(now.minute),
    'Apellidos : ' + str(Apellidos.get()), 'Nombres   : ' + str(Nombres.get()),
    'Dirección : ' + str(Direccion.get()),
    'Teléfono  : ' + str(Telefono.get()),
    100*'━',
    'Código','Descripción','Unidad','Cant','Precio','Subtotal',
    100*'━'
    ))

    total = 0
    for item in range(len(boleta)):
        print('''┃{:^10} {:51} {:^8} {:^6} {:8} {:10}┃'''.format(
        boleta[item][0],
        boleta[item][1],
        boleta[item][2],
        boleta[item][3],
        boleta[item][4],
        boleta[item][5]
        ))
        total += boleta[item][5]
    
    print('''{}
{:^79}┃{:^8}:{:10}┃
{:^79}{}'''.format(
    100*'━',
    '', 'Total', round(total,2),
    '', 21*'━'
))

    # Borrando los datos
    getcodigo.set('000001')
    prevprod.set('')
    getcost.set('1')
    prevcost.set('')
    DNI.set('')
    Apellidos.set('')
    Nombres.set('')
    Direccion.set('')
    Telefono.set('')
    for borrar in range(len(boleta)):
        boleta.pop()
    tabla()
    previsualizar()

def addproduct():
    print('Esta opción no está disponible en esta versión')

def tabla():
    # Estilos a la tabla
    style = ttk.Style()
    style.theme_use('clam')
    style.configure('Treeview',
        background = '#848484',
        rowheight = 25,
        fieldbackground = '#242526'
    )
    style.map('Treeview',
        background = [('selected', '#3a3b3c')]
    )

    # Tabla de lista de productos
    Lista = ttk.Treeview(ventana)
    Lista.place(x = 10, y = 285, width = 700, height = 250)
    Lista['columns'] = ('Descripcion', 'Unidad', 'Cantidad', 'Precio', 'Subtotal')

    # Nombre de las columnas
    Lista.column('#0', anchor = CENTER, width = 80, minwidth = 80)
    Lista.column('Descripcion', anchor = W, width = 300, minwidth = 300)
    Lista.column('Unidad', anchor = CENTER, width = 60, minwidth = 60)
    Lista.column('Cantidad', anchor = CENTER, width = 60, minwidth = 60)
    Lista.column('Precio', anchor = CENTER, width = 98, minwidth = 98)
    Lista.column('Subtotal', anchor = CENTER, width = 98, minwidth = 98)

    # Encabezado de las columnas
    Lista.heading('#0', text = 'Código', anchor = CENTER)
    Lista.heading('Descripcion', text = 'Descripción', anchor = CENTER)
    Lista.heading('Unidad', text = 'Unidad', anchor = CENTER)
    Lista.heading('Cantidad', text = 'Cantidad', anchor = CENTER)
    Lista.heading('Precio', text = 'Precio', anchor = CENTER)
    Lista.heading('Subtotal', text = 'Subtotal', anchor = CENTER)

    # Insertando productos en la tabla
    for n in range(len(boleta)):
        codigo = boleta[n][0]
        descripcion = boleta[n][1]
        unidad = boleta[n][2]
        cantidad = boleta[n][3]
        precio = boleta[n][4]
        subtotal = boleta[n][5]
        Lista.insert(parent = '', index = 'end', iid = n, text = codigo, values = (descripcion, unidad, cantidad, precio, subtotal))


# Configuración de la Ventana Tk
ventana = Tk()
ventana.title('Gysmoy Solution 1.0')
ventana.geometry('720x600')
ventana.resizable(width = 0, height = 0)
ventana.configure(bg = '#18191a')

# Key y Value de productos
id_productos = [
    '000001', '000002', '000003', '000004', '000005',
    '000006', '000007', '000008', '000009', '000010',
    '000011', '000012', '000013', '000014', '000015']

productos = {
    '000001':['Linterna Recargable LED', 'Unidad', 12.00],
    '000002':['Nivel', 'Unidad', 15.00],
    '000003':['Taladro Recargable y/o Eléctrico', 'Unidad', 225.00],
    '000004':['Juego de Llaves', 'Caja', 600.00],
    '000005':['Escalera', 'Unidad', 400.00],
    '000006':['Alicate', 'Unidad', 20.00],
    '000007':['Cinta de medir o métrica', 'Metro', 5.00],
    '000008':['Martillo', 'Unidad', 15.00],
    '000009':['Destornillador de paleta', 'Unidad', 12.00],
    '000010':['Pala', 'Unidad', 25.00],
    '000011':['Escuadras y Reglas Milimetricas', 'Caja', 15.00],
    '000012':['Amoladora', 'Unidad', 220.00],
    '000013':['Serrucho', 'Unidad', 50.00],
    '000014':['Cinta Aislante', 'Unidad', 3.00],
    '000015':['Cuerda de Nylon', 'Metro', 0.10]}

boleta = list()

# Asignación de variables
getcodigo = StringVar()
prevprod = StringVar()
getcost = StringVar()
prevcost = StringVar()
DNI = StringVar()
Apellidos = StringVar()
Nombres = StringVar()
Direccion = StringVar()
Telefono = StringVar()

# Título General
Label(ventana, text = '🔧 Ferretería El Tornillo Feliz 🔨', bg = '#18191a', fg = '#2e89ff', font = '"Bradley Hand ITC" 20 bold').pack(pady=10)

# Botón Añadir
Button(ventana, text='➕', bg = '#2e89ff', fg = 'white', font = '"Verdana" 12', border = '0', activebackground = '#075af5', activeforeground = '#ffffff', command = addproduct).place(x = 675, y = 15, width=25, height=25)

# Labels & Entries
Label(ventana, text = 'DNI: ', bg = '#18191a', fg = 'white', font = '15').place(x = 20, y = 60)
Entry(ventana, bg = '#3a3b3c', fg = 'white', font = '15', border = '0', textvariable = DNI).place(x = 140, y = 60, width=200, height=25)

Label(ventana, text = 'Apellidos: ', bg = '#18191a', fg = 'white', font = '15').place(x = 20, y = 100)
Entry(ventana, bg = '#3a3b3c', fg = 'white', font = '15', border = '0', textvariable = Apellidos).place(x = 140, y = 100, width=200, height=25)

Label(ventana, text = 'Nombres: ', bg = '#18191a', fg = 'white', font = '15').place(x = 380, y = 100)
Entry(ventana, bg = '#3a3b3c', fg = 'white', font = '15', border = '0', textvariable = Nombres).place(x = 500, y = 100, width=200, height=25)

Label(ventana, text = 'Dirección: ', bg = '#18191a', fg = 'white', font = '15').place(x = 20, y = 140)
Entry(ventana, bg = '#3a3b3c', fg = 'white', font = '15', border = '0', textvariable = Direccion).place(x = 140, y = 140, width=560, height=25)

Label(ventana, text = 'Teléfono: ', bg = '#18191a', fg = 'white', font = '15').place(x = 20, y = 180)
Entry(ventana, bg = '#3a3b3c', fg = 'white', font = '15', border = '0', textvariable = Telefono).place(x = 140, y = 180, width=560, height=25)

# Spinbox de Código de producto
Label(ventana, text = 'Código: ', bg = '#18191a', fg = 'white', font = '15').place(x = 20, y = 230)
Spinbox(ventana, bg = '#3a3b3c', fg = 'white', font = '15', border = '0', values = id_productos, textvariable = getcodigo, command = previsualizar).place(x = 140, y = 230, width=80, height=25)
Label(ventana, bg = '#18191a', fg = 'grey', font = '10', textvariable = prevprod).place(x = 140, y = 255)

Label(ventana, text = 'Cantidad: ', bg = '#18191a', fg = 'white', font = '15').place(x = 260, y = 230)
Spinbox(ventana, bg = '#3a3b3c', fg = 'white', font = '15', border = '0', from_ = 1, to = 9*'9', textvariable = getcost, command = previsualizar).place(x = 380, y = 230, width=80, height=25)
Label(ventana, bg = '#18191a', fg = 'grey', font = '10', textvariable = prevcost).place(x = 380, y = 255)

Button(ventana, text='Añadir al carrito', bg = '#2e89ff', fg = 'white', font = '"Verdana" 12', border = '0', activebackground = '#075af5', activeforeground = '#ffffff', command = insertar).place(x = 500, y = 230, width=200, height=25)

Button(ventana, text='Imprimir boleta', bg = '#2e89ff', fg = 'white', font = '"Verdana" 12', border = '0', activebackground = '#075af5', activeforeground = '#ffffff', command = imprimir).place(x = 260, y = 555, width=200, height=25)

previsualizar()
tabla()

ventana.mainloop()
