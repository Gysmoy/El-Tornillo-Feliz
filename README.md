# El Tornillo Feliz
Solución del Trabajo del Curso (Algoritmia para la programación del Software)

# Librerías Importadas 
<p>Se importa las librerías tkinter (para la ventana), datetime (para mostrar la hora y fecha de ejecución de la compra) y os para limpiar la consola cuando se realice una nueva petición<p>
<pre>
from tkinter import ttk
from tkinter import *
from datetime import date
from datetime import datetime
import os
</pre>

# Declaración de funciones
<p>Primero la de <b>previsualizar</b>, esto hara que cuando se elija un producto por su codigo, se muestre debajo una información general acerca del producto (para ser más específico, se muestra el nombre y el costo en cuanto a la cantidad)</p>
<pre>
def previsualizar():
    prevprod.set('')
    prevprod.set(productos[getcodigo.get()][0])
    prevcost.set('')
    prevcost.set('{} {}'.format('S/.', abs( round(float(productos[getcodigo.get()][2]) * int(getcost.get()) , 2) ) ))
</pre>
<p>La función <b>insertar</b> inserta los datos del prodcuto que se va a comprar dentro de una lista llamada boleta (la cual ha sido declarada como una lista vacía).<br>Luego se hace una limpieza de los Entries y la lista <b>boleta</b> de la ventana, para una nueva petición</p>
<pre>
def insertar():
    try:
        codigo = getcodigo.get()
        descripcion = productos[codigo][0]
        unidad = productos[codigo][1]
        cantidad = abs(int(getcost.get()))
        precio = productos[codigo][2]
        subtotal = round(cantidad * precio , 2)<br>
        boleta.append([codigo, descripcion, unidad, cantidad, precio, subtotal])
        tabla()
    except:
        print('¡Hubo un error al insertar datos en la boleta!')
</pre>
<p>la función <b>imprimir</b> imprime los datos introducidos en la ventana (incluyendo los productos) en la consola de python en forma de boleta de ventas</p>
<pre>
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
    ))<br>
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
        total += boleta[item][5]<br>
    print('''{}
{:^79}┃{:^8}:{:10}┃
{:^79}{}'''.format(
    100*'━',
    '', 'Total', round(total,2),
    '', 21*'━'
))<br>
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
</pre>
<p>La función <b>addproduct</b> tiene como objetivo añadir un nuevo producto a la lista de productos existentes en la ferretería (por ahora es solo idea, por eso se muestra el mensaje de que aún no está disponible)</p>
<pre>
def addproduct():
    print('Esta opción no está disponible en esta versión')
</pre>

# Configuración de la tabla ttk
<p>La tabla esta dentro de una función porque se hará un formateo y llamado de ella a medida que se agregue un nuevo producto en la lista <b>boleta</b>.</p>
<pre>
def tabla():
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
    Lista = ttk.Treeview(ventana)
    Lista.place(x = 10, y = 285, width = 700, height = 250)
    Lista['columns'] = ('Descripcion', 'Unidad', 'Cantidad', 'Precio', 'Subtotal')<br>
    Lista.column('#0', anchor = CENTER, width = 80, minwidth = 80)
    Lista.column('Descripcion', anchor = W, width = 300, minwidth = 300)
    Lista.column('Unidad', anchor = CENTER, width = 60, minwidth = 60)
    Lista.column('Cantidad', anchor = CENTER, width = 60, minwidth = 60)
    Lista.column('Precio', anchor = CENTER, width = 98, minwidth = 98)
    Lista.column('Subtotal', anchor = CENTER, width = 98, minwidth = 98)<br>
    Lista.heading('#0', text = 'Código', anchor = CENTER)
    Lista.heading('Descripcion', text = 'Descripción', anchor = CENTER)
    Lista.heading('Unidad', text = 'Unidad', anchor = CENTER)
    Lista.heading('Cantidad', text = 'Cantidad', anchor = CENTER)
    Lista.heading('Precio', text = 'Precio', anchor = CENTER)
    Lista.heading('Subtotal', text = 'Subtotal', anchor = CENTER)
    for n in range(len(boleta)):
        codigo = boleta[n][0]
        descripcion = boleta[n][1]
        unidad = boleta[n][2]
        cantidad = boleta[n][3]
        precio = boleta[n][4]
        subtotal = boleta[n][5]
        Lista.insert(parent = '', index = 'end', iid = n, text = codigo, values = (descripcion, unidad, cantidad, precio, subtotal))
</pre>
<p>La tabla hace uso de un tema preestablecido de nombre <b>clam</b> pero también se hace algunas modificaciones de esta para que pueda conjugar con el color de fondo de la ventana</p>

# Configuración de la ventana Tkinter
<p>Las configuraciones de la ventana contienen: Nombre, medida (<b>no resizable</b>) y fondo de color #18191A (<b>HEX</b>)</p>
<pre>
ventana = Tk()
ventana.title('Gysmoy Solution 1.0')
ventana.geometry('720x600')
ventana.resizable(width = 0, height = 0)
ventana.configure(bg = '#18191a')
</pre>

# Creación de la lista de IDs de los productos
<p>Primero creamos una lista con los IDs de los produtos, la cual nos servirá para hacer un llamado a los demas datos de los productos que se encuentran en el diccionario <b>productos</b>.</p>
<pre>
id_productos = [
    '000001', '000002', '000003', '000004', '000005',
    '000006', '000007', '000008', '000009', '000010',
    '000011', '000012', '000013', '000014', '000015']
</pre>

# Se crea el diccionario de los productos
<p>Este diccionario es declarado con el fin de interactuar con los IDs de los productos que estan dentro de la lista <b>id_productos</b></p>
<pre>
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
</pre>
<p>Se declara una lista vacía <code>boleta = list()</code> al iniciar el programa, dentro de esta se insertarán los datos de los prodcutos que se comprarán: Código, Descripción, Unidad de medida, Cantidad, Precio Unitario y Precio x Cantidad</p>

# Asignación de variables
<p>Se hace una asignación de variables para que puedan interactura con los <b>Entry</b>'s de la <b>ventana</b>.</p>
<pre>
getcodigo = StringVar()
prevprod = StringVar()
getcost = StringVar()
prevcost = StringVar()
DNI = StringVar()
Apellidos = StringVar()
Nombres = StringVar()
Direccion = StringVar()
Telefono = StringVar()
</pre>

# Creación de Labels, Entries y Buttons
<p>Primero el título: background similar al de la ventana, foreground de color <b>azul claro</b>, fuente <b>Bradley Hand ITC</b> y de tamaño <b>20 en negrita</b></p>
<pre>
Label(ventana, text = '🔧 Ferretería El Tornillo Feliz 🔨', bg = '#18191a', fg = '#2e89ff', font = '"Bradley Hand ITC" 20 bold').pack(pady=10)
</pre>
<p>Primero botón de la ventana. Este boton hace un llamado a la función <b>addproduct</b>.</p>
<pre>
Button(ventana, text='➕', bg = '#2e89ff', fg = 'white', font = '"Verdana" 12', border = '0', activebackground = '#075af5', activeforeground = '#ffffff', command = addproduct).place(x = 675, y = 15, width=25, height=25)
</pre>
<p>Aqui están los <b>Label</b>'s y <b>Entry</b>'s de la ventana.</p>
<pre>
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

Label(ventana, text = 'Código: ', bg = '#18191a', fg = 'white', font = '15').place(x = 20, y = 230)
Spinbox(ventana, bg = '#3a3b3c', fg = 'white', font = '15', border = '0', values = id_productos, textvariable = getcodigo, command = previsualizar).place(x = 140, y = 230, width=80, height=25)
Label(ventana, bg = '#18191a', fg = 'grey', font = '10', textvariable = prevprod).place(x = 140, y = 255)

Label(ventana, text = 'Cantidad: ', bg = '#18191a', fg = 'white', font = '15').place(x = 260, y = 230)
Spinbox(ventana, bg = '#3a3b3c', fg = 'white', font = '15', border = '0', from_ = 1, to = 9*'9', textvariable = getcost, command = previsualizar).place(x = 380, y = 230, width=80, height=25)
Label(ventana, bg = '#18191a', fg = 'grey', font = '10', textvariable = prevcost).place(x = 380, y = 255)
</pre>

# Botones <i>Añadir al carrito</i> e <i>Imprimir boleta</i>.
<p>Botón <b>Añadir al carrito</b>, este hace un llamado a la función <b>insertar</b> la cual inserta los datos del producto y sus respectivos extras (cantidad, subtotal)</p>
<pre>
Button(ventana, text='Añadir al carrito', bg = '#2e89ff', fg = 'white', font = '"Verdana" 12', border = '0', activebackground = '#075af5', activeforeground = '#ffffff', command = insertar).place(x = 500, y = 230, width=200, height=25)
</pre>
<p>Botón <b>Imprimir boleta</b>, llama a la función <b>imprimir</b> para que imprima lso datos de los entries y la tabla. Finalmente limpia la ventana y la prepara para una nueva petición</p>
<pre>
Button(ventana, text='Imprimir boleta', bg = '#2e89ff', fg = 'white', font = '"Verdana" 12', border = '0', activebackground = '#075af5', activeforeground = '#ffffff', command = imprimir).place(x = 260, y = 555, width=200, height=25)
</pre>

# Llamando a las funciones que aún no estan activas
<p>La función <b>previsualizar</b> aún no se muestra en la ventana, por ello se le hace un llamado con <code>previsualizar()</code>. Del mismo modo se hace un llamado a la función <b>tabla</b> con <code>tabla()</code>.</p>

# Evitar cierre por <i>arranque directo</i>
<p>Si la ventana se corre desde el <i>Simbolo del sistema</i>, Tkinter se cierra de forma inesperada, por eso se hace un <code>ventana.mainloop()</code> para permanecer la ventana activa.</p
