from tkinter import *
from tkinter import messagebox
import sqlite3


# ----------------------------------------------------- Funciones Conectar

def conexionBBDD():
    mi_conexion = sqlite3.connect('Usuarios')
    mi_cursor = mi_conexion.cursor()
    try:
        mi_cursor.execute('''
            CREATE TABLE DATOSUSUARIOS (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE_USUARIO VARCHAR(50),
            PASSWORD VARCHAR(50),
            APELLIDO VARCHAR(10),
            DIRECCION VARCHAR(50),
            COMENTARIOS VARCHAR(100))
            ''')
        messagebox.showinfo("BBDD", "BBDD creada con éxito")
    except:
        messagebox.showwarning('Atención', 'La base de datos ya existe')


# ----------------------------------------------------- Funciones Salir

def salir():
    valor = messagebox.askquestion('Salir', '¿Desea salir de la aplicación?')
    if valor == 'yes':
        root.destroy()


# ----------------------------------------------------- Funciones Limpiar campos

def limpiar_campos():
    mi_id.set('')
    mi_nombre.set('')
    mi_apellido.set('')
    mi_direccion.set('')
    mi_pass.set('')
    texto_comentario.delete(1.0, END)


# ----------------------------------------------------- Funciones Create

def create():
    mi_conexion = sqlite3.connect('Usuarios')
    mi_cursor = mi_conexion.cursor()

    datos = mi_nombre.get(),mi_pass.get(),mi_apellido.get(),mi_direccion.get(),texto_comentario.get("1.0", END)

    mi_cursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL,?,?,?,?,?)",(datos))
    mi_conexion.commit()
    messagebox.showinfo("BBDD", "Registro insertado con éxito")


# ----------------------------------------------------- Funciones Leer

def read():
    mi_conexion = sqlite3.connect('Usuarios')
    mi_cursor = mi_conexion.cursor()
    mi_cursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID=" + mi_id.get())

    el_usuario = mi_cursor.fetchall()

    for usuario in el_usuario:
        mi_id.set(usuario[0])
        mi_nombre.set(usuario[1])
        mi_pass.set(usuario[2])
        mi_apellido.set(usuario[3])
        mi_direccion.set(usuario[4])
        texto_comentario.insert(1.0, usuario[5])

    mi_conexion.commit()

# ----------------------------------------------------- Funciones Actualizar

def update():
    mi_conexion = sqlite3.connect('Usuarios')
    mi_cursor = mi_conexion.cursor()

    datos = mi_nombre.get(),mi_pass.get(),mi_apellido.get(),mi_direccion.get(),texto_comentario.get("1.0", END)

    mi_cursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO=?, PASSWORD=?, APELLIDO=?, DIRECCION=?, COMENTARIOS=?" +
                      "WHERE ID=" + mi_id.get(),(datos))

    mi_conexion.commit()
    messagebox.showinfo("BBDD", "Registro actualizado con éxito")


# ----------------------------------------------------- Funciones Actualizar

def delete():
    mi_conexion = sqlite3.connect('Usuarios')
    mi_cursor = mi_conexion.cursor()
    mi_cursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID=" + mi_id.get())

    mi_conexion.commit()

    messagebox.showinfo("BBDD", "Registro borrado con éxito")


# ----------------------------------------------------- Funciones ayuda

def ayuda():
    valor = messagebox.showinfo("licencia", "FREE")

# ----------------------------------------------------- Funciones Acerca

def acerca():
    valor = messagebox.showinfo("Acerca de...", "App creada con Python")



# ----------------------------------------------------- Barra menu

root = Tk()

barra_menu = Menu(root)
root.config(menu=barra_menu, width=400, height=400)

bbdd_menu = Menu(barra_menu, tearoff=0)
bbdd_menu.add_command(label='Conectar', command=conexionBBDD)
bbdd_menu.add_command(label='Salir', command=salir)

borrar_menu = Menu(barra_menu, tearoff=0)
borrar_menu.add_cascade(label='Borrar campos', command=limpiar_campos)

crud_menu = Menu(barra_menu, tearoff=0)
crud_menu.add_command(label='Crear', command=create)
crud_menu.add_command(label='Leer', command=read)
crud_menu.add_command(label='Actualizar', command=update)
crud_menu.add_command(label='Borrar', command=delete)

ayuda_menu = Menu(barra_menu, tearoff=0)
ayuda_menu.add_command(label='Licencia', command=ayuda)
ayuda_menu.add_command(label='Acerca de...', command=acerca)

barra_menu.add_cascade(label='BBDD', menu=bbdd_menu)
barra_menu.add_cascade(label='Borrar', menu=borrar_menu)
barra_menu.add_cascade(label='CRUD', menu=crud_menu)
barra_menu.add_cascade(label='Ayuda', menu=ayuda_menu)

# ----------------------------------------------------- Campos
mi_frame = Frame(root)
mi_frame.pack()

mi_id = StringVar()
mi_nombre = StringVar()
mi_apellido = StringVar()
mi_pass = StringVar()
mi_direccion = StringVar()

cuadro_id = Entry(mi_frame, textvariable=mi_id)
cuadro_id.grid(row=0, column=1, padx=10, pady=10)

cuadro_nombre = Entry(mi_frame, textvariable=mi_nombre)
cuadro_nombre.grid(row=1, column=1, padx=10, pady=10)
cuadro_nombre.config(fg='red')

cuadro_pass = Entry(mi_frame, textvariable=mi_pass)
cuadro_pass.grid(row=2, column=1, padx=10, pady=10)
cuadro_pass.config(show='*')

cuadro_apellido = Entry(mi_frame, textvariable=mi_apellido)
cuadro_apellido.grid(row=3, column=1, padx=10, pady=10)

cuadro_direccion = Entry(mi_frame, textvariable=mi_direccion)
cuadro_direccion.grid(row=4, column=1, padx=10, pady=10)

texto_comentario = Text(mi_frame, width=16, height=5)
texto_comentario.grid(row=5, column=1, padx=10, pady=10)
scrollVert = Scrollbar(mi_frame, command=texto_comentario.yview)
scrollVert.grid(row=5, column=2, sticky='nsew')

texto_comentario.config(yscrollcommand=scrollVert.set)

# ----------------------------------------------------- Label

label_id = Label(mi_frame, text='Id:')
label_id.grid(row=0, column=0, sticky='e', pady=10, padx=10)

label_nombre = Label(mi_frame, text='Nombre:')
label_nombre.grid(row=1, column=0, sticky='e', padx=10, pady=10)

label_pass = Label(mi_frame, text='Contraseña:')
label_pass.grid(row=2, column=0, sticky='e', pady=10, padx=10)

label_apellido = Label(mi_frame, text='Apellido:')
label_apellido.grid(row=3, column=0, sticky='e', pady=10, padx=10)

label_direccion = Label(mi_frame, text='Dirección:')
label_direccion.grid(row=4, column=0, sticky='e', pady=10, padx=10)

label_texto = Label(mi_frame, text='Comentario:')
label_texto.grid(row=5, column=0, sticky='ne', pady=10, padx=10)

# ----------------------------------------------------- Botones

mi_frame2 = Frame(root)
mi_frame2.pack()

boton_crear = Button(mi_frame2, text='Create', command=create)
boton_crear.grid(row=1, column=0, sticky='e', padx=10, pady=10)

boton_leer = Button(mi_frame2, text='Read', command=read)
boton_leer.grid(row=1, column=1, sticky='e', padx=10, pady=10)

boton_actualizar = Button(mi_frame2, text='Update', command=update)
boton_actualizar.grid(row=1, column=2, sticky='e', padx=10, pady=10)

boton_borrar = Button(mi_frame2, text='Delete', command=delete)
boton_borrar.grid(row=1, column=3, sticky='e', padx=10, pady=10)

root.mainloop()
