from tkinter import *
import random
import operator
import os
from tkinter import messagebox
from tkinter import ttk

i = 0
opcion = 0
lista_canciones = []
lista_imagenes = []
lista_videos = []
listas_canciones = []
albumes_imagenes = []
albumes_videos = []


# ver listas y albumes creados por el usuario
class ver_listas:

    def __init__(self, tipo, lista):
        self.tipo = tipo
        self.lista = lista
        self.tamaño = len(self.lista)
        self.i=0

    def ver_listaM(self):

        def clickedVolver():
            root.destroy()
            menuPrincipal = ventanaMusica()

        cx=10
        cy=125
        root = Tk()
        root.geometry('626x417')
        root.title("RePOO")
        text = Label(root, text='LISTAS')
        text.place(x=10, y=20)
        text.config(font=("Verdana", 30))
        btnVolver = Button(root, text="Volver", command=clickedVolver)
        btnVolver.place(x=525, y=350, height=35, width=60)


        if self.tamaño==0:
            messagebox.showinfo('RePOO', 'No hay listas')
#mostrar listas en pantalla y autoajustar
        while self.i < self.tamaño:
            lista = Listbox(root, activestyle="underline")
            lista.place_configure(x=cx, y=cy)
            text = Label(root, text='LISTA ' + str(self.i+1))
            text.place(x=cx, y=cy-25)
#variable que Autoajusta cx
            cx+=125
            listaAux = self.lista[self.i]
            j = 0
            while j < len(self.lista[self.i]):
                lista.insert(END, listaAux[j])
                j += 1
            self.i += 1
        root.mainloop()

    def ver_listaI(self):

        def clickedVolver():
            root.destroy()
            menuPrincipal = ventanaImagen()

        cx = 10
        cy = 125
        root = Tk()
        root.geometry('626x417')
        root.title("RePOO")
        text = Label(root, text='ALBUMES')
        text.place(x=10, y=20)
        text.config(font=("Verdana", 30))
        btnVolver = Button(root, text="Volver", command=clickedVolver)
        btnVolver.place(x=525, y=350, height=35, width=60)

        if self.tamaño==0:
            messagebox.showinfo('RePOO', 'No hay albumes')

        while self.i < self.tamaño:
            lista = Listbox(root, activestyle="underline")
            lista.place_configure(x=cx, y=cy)
            text = Label(root, text='LISTA ' + str(self.i+1))
            text.place(x=cx, y=cy-25)
            cx+=125
            listaAux = self.lista[self.i]
            j = 0
            while j < len(self.lista[self.i]):
                lista.insert(END, listaAux[j])
                j += 1
            self.i += 1
        root.mainloop()

    def ver_listaV(self):
        cx = 10
        cy = 125
        root = Tk()
        root.geometry('626x417')
        root.title("RePOO")
        text = Label(root, text='ALBUMES')
        text.place(x=10, y=20)
        text.config(font=("Verdana", 30))
        btnVolver = Button(root, text="Volver", command=clickedVolver)
        btnVolver.place(x=525, y=350, height=35, width=60)

        if self.tamaño==0:
            messagebox.showinfo('RePOO', 'No hay albumes')

        while self.i < self.tamaño:
            lista = Listbox(root, activestyle="underline")
            lista.place_configure(x=cx, y=cy)
            text = Label(root, text='LISTA ' + str(self.i+1))
            text.place(x=cx, y=cy-25)
            cx+=125
            listaAux = self.lista[self.i]
            j = 0
            while j < len(self.lista[self.i]):
                lista.insert(END, listaAux[j])
                j += 1
            self.i += 1
        root.mainloop()
# abre bibliotecas disponibles
class Ver_Todo:
    def __init__(self, lista):
        self.lista = lista
        self.sublista = []

    def ver_Lista_Musica(self):

        def clickedVolver():
            root.destroy()
            menuPrincipal = ventanaMusica()

        root = Tk()
        root.geometry('626x417')
        root.title("RePOO")
        text = Label(root, text='BIBLIOTECA')
        text.place(x=10, y=20)
        text.config(font=("Verdana", 30))
        tv = ttk.Treeview(root)
        tv['columns'] = ('Interprete', 'Album', 'Año', "Genero")
        tv.heading("#0", text='Nombre')
        tv.column("#0", anchor="center", width=100)
        tv.heading('Interprete', text='Interprete')
        tv.column('Interprete', anchor='center', width=100)
        tv.heading('Album', text='Album')
        tv.column('Album', anchor='center', width=100)
        tv.heading('Año', text='Año')
        tv.column('Año', anchor='center', width=100)
        tv.heading('Genero', text='Genero')
        tv.column('Genero', anchor='center', width=100)
        btnVolver = Button(root, text="Volver", command=clickedVolver)
        btnVolver.place(x=525, y=350, height=35, width=60)
#clasificador de caracteristicas
        for i in range(len(self.lista)):
            nombre = str(self.lista[i].get_nombre())
            interprete = str(self.lista[i].interprete)
            Album = str(self.lista[i].album)
            año = str(self.lista[i].año)
            genero = str(self.lista[i].genero)
            tv.insert("", END, text=nombre, values=[interprete,Album,año,genero])

        tv.place(x=10, y=125)
        root.mainloop()

    def ver_Lista_Imagen(self):

        def clickedVolver():
            root.destroy()
            menuPrincipal = ventanaImagen()

        root = Tk()
        root.geometry('626x417')
        root.title("RePOO")
        text = Label(root, text='BIBLIOTECA')
        text.place(x=10, y=20)
        text.config(font=("Verdana", 30))
        tv = ttk.Treeview(root)
        tv['columns'] = ('Interprete', 'Album', 'Año')
        tv.heading("#0", text='Nombre')
        tv.column("#0", anchor="center", width=100)
        tv.heading('Interprete', text='Interprete')
        tv.column('Interprete', anchor='center', width=100)
        tv.heading('Album', text='Album')
        tv.column('Album', anchor='center', width=100)
        tv.heading('Año', text='Año')
        tv.column('Año', anchor='center', width=100)
        btnVolver = Button(root, text="Volver", command=clickedVolver)
        btnVolver.place(x=525, y=350, height=35, width=60)

        for i in range(len(self.lista)):
            nombre = str(self.lista[i].get_nombre())
            interprete = str(self.lista[i].interprete)
            Album = str(self.lista[i].album)
            año = str(self.lista[i].año)
            tv.insert("", END, text=nombre, values=[interprete, Album, año])

        tv.place(x=10, y=125)
        root.mainloop()

    def ver_Lista_Video(self):

        def clickedVolver():
            root.destroy()
            menuPrincipal = ventanaImagen()

        root = Tk()
        root.geometry('626x417')
        root.title("RePOO")
        text = Label(root, text='BIBLIOTECA')
        text.place(x=10, y=20)
        text.config(font=("Verdana", 30))
        tv = ttk.Treeview(root)
        tv['columns'] = ('Interprete', 'Album', 'Año')
        tv.heading("#0", text='Nombre')
        tv.column("#0", anchor="center", width=100)
        tv.heading('Interprete', text='Interprete')
        tv.column('Interprete', anchor='center', width=100)
        tv.heading('Album', text='Album')
        tv.column('Album', anchor='center', width=100)
        tv.heading('Año', text='Año')
        tv.column('Año', anchor='center', width=100)
        btnVolver = Button(root, text="Volver", command=clickedVolver)
        btnVolver.place(x=525, y=350, height=35, width=60)

        for i in range(len(self.lista)):
            nombre = str(self.lista[i].get_nombre())
            interprete = str(self.lista[i].interprete)
            Album = str(self.lista[i].album)
            año = str(self.lista[i].año)
            tv.insert("", END, text=nombre, values=[interprete, Album, año])

        tv.place(x=10, y=125)
        root.mainloop()


# crear listas y albumes hechos por el usuario
class crear_listas:

    def __init__(self, tipo, listaPrincipal):
        self.tipo = tipo
        self.listaPrincipal = listaPrincipal
        self.n = None

    def crear_lista(self):
        root = Tk()
        root.geometry('626x417')
        root.title("RePOO")
        archivo = open("Archivo.txt", "a")
        nombres = []
        for i in range(len(self.listaPrincipal)):
            nombres.append(self.listaPrincipal[i].nombre)
        lista = []

        def clickedVolver():
            root.destroy()
            if self.tipo == "cancion":
                menuPrincipal = ventanaMusica()
            elif self.tipo == "imagen":
                menuPrincipal = ventanaImagen()
            elif self.tipo == "video":
                menuPrincipal = ventanaVideo()
#boton de guarde
        def clickedGuardar():
            nombre = str(txtN.get())
            if nombre != "":
                if self.verificar_nombre(nombres, nombre):
                    lista.append(nombre)
                    archivo.write(nombre + "#")
            if self.tipo == "cancion":
                listas_canciones.append(lista)
            elif self.tipo == "imagen":
                albumes_imagenes.append(lista)
            elif self.tipo == "video":
                albumes_videos.append(lista)
            messagebox.showinfo('RePOO', 'Guardado')
            root.destroy()
            if self.tipo == "cancion":
                menuPrincipal = ventanaMusica()
            elif self.tipo == "imagen":
                menuPrincipal = ventanaImagen()
            elif self.tipo == "video":
                menuPrincipal = ventanaVideo()
#Boton para agregar otra
        def clickedAgregarOtra():
            nombre = str(txtN.get())
            if self.verificar_nombre(nombres, nombre):
                lista.append(nombre)
                archivo.write(nombre + "#")
                messagebox.showinfo('RePOO', 'Agregado')
            else:
                messagebox.showinfo('RePOO', 'Nombre No Encontrado')

            txtN.delete(0, END)

        if self.tipo == "cancion":
            text = Label(root, text='CREAR LISTA')
            text.place(x=10, y=20)
            text.config(font=("Verdana", 30))
            NombreLM = Label(root, text='Nombre')
            NombreLM.place(x=10, y=100)
            NombreLM.config(font=("Verdana", 10))
            archivo.write("\n" + "listaCanciones" + "#")
            txtN = Entry(root, width=25)
            txtN.place(x=125, y=100)
            btnVolver = Button(root, text="Volver", command=clickedVolver)
            btnVolver.place(x=525, y=350, height=35, width=100)
            btnGuardar = Button(root, text="Guardar Todo", command=clickedGuardar)
            btnGuardar.place(x=10, y=350, height=35, width=100)
            btnAgregarOtra = Button(root, text="Agregar Otra", command=clickedAgregarOtra)
            btnAgregarOtra.place(x=10, y=150, height=35, width=100)

        elif self.tipo == "imagen":
            text = Label(root, text='CREAR ALBUM')
            text.place(x=10, y=20)
            text.config(font=("Verdana", 30))
            NombreLM = Label(root, text='Nombre')
            NombreLM.place(x=10, y=100)
            NombreLM.config(font=("Verdana", 10))
            archivo.write("\n" + "listaImagenes" + "#")
            txtN = Entry(root, width=25)
            txtN.place(x=125, y=100)
            btnVolver = Button(root, text="Volver", command=clickedVolver)
            btnVolver.place(x=525, y=350, height=35, width=100)
            btnGuardar = Button(root, text="Guardar Todo", command=clickedGuardar)
            btnGuardar.place(x=10, y=350, height=35, width=100)
            btnAgregarOtra = Button(root, text="Agregar Otra", command=clickedAgregarOtra)
            btnAgregarOtra.place(x=10, y=150, height=35, width=100)

        elif self.tipo == "video":
            text = Label(root, text='CREAR ALBUM')
            text.place(x=10, y=20)
            text.config(font=("Verdana", 30))
            NombreLM = Label(root, text='Nombre')
            NombreLM.place(x=10, y=100)
            NombreLM.config(font=("Verdana", 10))
            archivo.write("\n" + "listaVideos" + "#")
            txtN = Entry(root, width=25)
            txtN.place(x=125, y=100)
            btnVolver = Button(root, text="Volver", command=clickedVolver)
            btnVolver.place(x=525, y=350, height=35, width=100)
            btnGuardar = Button(root, text="Guardar Todo", command=clickedGuardar)
            btnGuardar.place(x=10, y=350, height=35, width=100)
            btnAgregarOtra = Button(root, text="Agregar Otra", command=clickedAgregarOtra)
            btnAgregarOtra.place(x=10, y=150, height=35, width=100)

    # verificar el nombre ingresado existe
    def verificar_nombre(self, nombres, nombre):
        if nombre in nombres:
            return True
        else:
            return False

#ingresar datos
class ingresar:
    def __init__(self):
        pass

    def ingresar_cancion(self):
        root = Tk()
        root.geometry('626x417')
        root.title("RePOO")

        def clickedVolver():
            root.destroy()
            menuPrincipal = ventanaMusica()

        def clickedGuardar():
            archivo = open("Archivo.txt", "a")
            nombre = str(txtN.get())
            inter = str(txtI.get())
            album = str(txtAL.get())
            año = str(txtAN.get())
            genero = str(txtG.get())
            lista_canciones.append(cancion(nombre, inter, album, año, genero))
            archivo.write("\n" +
                          "cancion" + "#" + nombre + "#" + inter + "#" + album + "#" + str(año) + "#" + genero + "#")
            messagebox.showinfo('RePOO', 'Guardado')
            root.destroy()
            ingreso = ingresar()
            ingreso.ingresar_cancion()

        text = Label(root, text='AGREGAR CANCION')
        text.place(x=10, y=20)
        text.config(font=("Verdana", 30))
        NombreLM = Label(root, text='Nombre')
        NombreLM.place(x=10, y=100)
        NombreLM.config(font=("Verdana", 10))
        InterLM = Label(root, text='Interprete')
        InterLM.place(x=10, y=150)
        InterLM.config(font=("Verdana", 10))
        AlbumLM = Label(root, text='Album')
        AlbumLM.place(x=10, y=200)
        AlbumLM.config(font=("Verdana", 10))
        AnioLM = Label(root, text='Año')
        AnioLM.place(x=10, y=250)
        AnioLM.config(font=("Verdana", 10))
        GeneroLM = Label(root, text='Genero')
        GeneroLM.place(x=10, y=300)
        GeneroLM.config(font=("Verdana", 10))
        btnVolver = Button(root, text="Volver", command=clickedVolver)
        btnVolver.place(x=525, y=350, height=35, width=60)
        btnGuardar = Button(root, text="Guardar", command=clickedGuardar)
        btnGuardar.place(x=10, y=350, height=35, width=60)
        txtN = Entry(root, width=25)
        txtN.place(x=125, y=100)
        txtI = Entry(root, width=25)
        txtI.place(x=125, y=150)
        txtAL = Entry(root, width=25)
        txtAL.place(x=125, y=200)
        txtAN = Entry(root, width=25)
        txtAN.place(x=125, y=250)
        txtG = Entry(root, width=25)
        txtG.place(x=125, y=300)

        root.mainloop()

    # agregar y guardar imagen en el archivo

    def ingresar_imagen(self):
        root = Tk()
        root.geometry('626x417')
        root.title("RePOO")

        def clickedVolver():
            root.destroy()
            menuPrincipal = ventanaImagen()

        def clickedGuardar():
            archivo = open("Archivo.txt", "a")
            Nombre = str(txtN.get())
            Inter = str(txtI.get())
            Album = str(txtAL.get())
            Año = str(txtAN.get())
            lista_imagenes.append(imagen(Nombre, Inter, Album, Año))
            archivo.write("\n"
                          + "imagen" + "#" + Nombre + "#" + Inter + "#" + Album + "#" + str(Año) + "#")
            messagebox.showinfo('RePOO', 'Guardado')
            root.destroy()
            ingreso = ingresar()
            ingreso.ingresar_imagen()

        text = Label(root, text='AGREGAR CANCION')
        text.place(x=10, y=20)
        text.config(font=("Verdana", 30))
        NombreLM = Label(root, text='Nombre')
        NombreLM.place(x=10, y=100)
        NombreLM.config(font=("Verdana", 10))
        InterLM = Label(root, text='Interprete')
        InterLM.place(x=10, y=150)
        InterLM.config(font=("Verdana", 10))
        AlbumLM = Label(root, text='Album')
        AlbumLM.place(x=10, y=200)
        AlbumLM.config(font=("Verdana", 10))
        AnioLM = Label(root, text='Año')
        AnioLM.place(x=10, y=250)
        AnioLM.config(font=("Verdana", 10))
        btnVolver = Button(root, text="Volver", command=clickedVolver)
        btnVolver.place(x=525, y=350, height=35, width=60)
        btnGuardar = Button(root, text="Guardar", command=clickedGuardar)
        btnGuardar.place(x=10, y=350, height=35, width=60)
        txtN = Entry(root, width=25)
        txtN.place(x=125, y=100)
        txtI = Entry(root, width=25)
        txtI.place(x=125, y=150)
        txtAL = Entry(root, width=25)
        txtAL.place(x=125, y=200)
        txtAN = Entry(root, width=25)
        txtAN.place(x=125, y=250)
        root.mainloop()

    # agregar y guardar video en el archivo
    def ingresar_video(self):
        root = Tk()
        root.geometry('626x417')
        root.title("RePOO")

        def clickedVolver():
            root.destroy()
            menuPrincipal = ventanaVideo()

        def clickedGuardar():
            archivo = open("Archivo.txt", "a")
            Nombre = str(txtN.get())
            Inter = str(txtI.get())
            Album = str(txtAL.get())
            Año = str(txtAN.get())
            lista_imagenes.append(video(Nombre, Inter, Album, Año))
            archivo.write("\n"
                          + "video" + "#" + Nombre + "#" + Inter + "#" + Album + "#" + str(Año) + "#")
            messagebox.showinfo('RePOO', 'Guardado')
            root.destroy()
            ingreso = ingresar()
            ingreso.ingresar_video()

        text = Label(root, text='AGREGAR CANCION')
        text.place(x=10, y=20)
        text.config(font=("Verdana", 30))
        NombreLM = Label(root, text='Nombre')
        NombreLM.place(x=10, y=100)
        NombreLM.config(font=("Verdana", 10))
        InterLM = Label(root, text='Interprete')
        InterLM.place(x=10, y=150)
        InterLM.config(font=("Verdana", 10))
        AlbumLM = Label(root, text='Album')
        AlbumLM.place(x=10, y=200)
        AlbumLM.config(font=("Verdana", 10))
        AnioLM = Label(root, text='Año')
        AnioLM.place(x=10, y=250)
        AnioLM.config(font=("Verdana", 10))
        btnVolver = Button(root, text="Volver", command=clickedVolver)
        btnVolver.place(x=525, y=350, height=35, width=60)
        btnGuardar = Button(root, text="Guardar", command=clickedGuardar)
        btnGuardar.place(x=10, y=350, height=35, width=60)
        txtN = Entry(root, width=25)
        txtN.place(x=125, y=100)
        txtI = Entry(root, width=25)
        txtI.place(x=125, y=150)
        txtAL = Entry(root, width=25)
        txtAL.place(x=125, y=200)
        txtAN = Entry(root, width=25)
        txtAN.place(x=125, y=250)

        root.mainloop()

# crear ventana musica
def ventanaMusica():
    root = Tk()
    root.geometry('626x417')
    root.title("RePOO")

    def clickedVolver():
        root.destroy()
        menuPrincipal = ventana()

    def clickedAgregar():
        root.destroy()
        ingreso = ingresar()
        ingreso.ingresar_cancion()

    def clickedCrearL():
        root.destroy()
        crearLista = crear_listas("cancion", lista_canciones)
        crearLista.crear_lista()

    def clickedVerBiblioteca():
        root.destroy()
        lista = Ver_Todo(lista_canciones)
        lista.ver_Lista_Musica()

    def clickedVerListas():
        root.destroy()
        verListas = ver_listas(cancion, listas_canciones)
        verListas.ver_listaM()

    text = Label(root, text='MUSICA')
    text.place(x=100, y=100)
    text.config(font=("Verdana", 50))
    # añadir botones

    btnAgregar = Button(root, text="Agregar Cancion", command=clickedAgregar)
    btnAgregar.place(x=50, y=200, height=50, width=100)
    btnCrearL = Button(root, text="Crear Lista", command=clickedCrearL)
    btnCrearL.place(x=175, y=200, height=50, width=100)
    btnVerL = Button(root, text="Ver Listas",command=clickedVerListas)
    btnVerL.place(x=300, y=200, height=50, width=100)
    btnVerB = Button(root, text="Ver Biblioteca", command=clickedVerBiblioteca)
    btnVerB.place(x=425, y=200, height=50, width=100)
    btnVolver = Button(root, text="Volver", command=clickedVolver)
    btnVolver.place(x=525, y=350, height=35, width=60)
    root.mainloop()

#crear ventana imagen
def ventanaImagen():
    root = Tk()
    root.geometry('626x417')
    root.title("RePOO")

    def clickedVolver():
        root.destroy()
        menuPrincipal = ventana()

    def clickedAgregar():
        root.destroy()
        ingreso = ingresar()
        ingreso.ingresar_imagen()

    def clickedCrearL():
        root.destroy()
        crearLista = crear_listas("imagen", lista_imagenes)
        crearLista.crear_lista()

    def clickedVerBiblioteca():
        root.destroy()
        lista = Ver_Todo(lista_imagenes)
        lista.ver_Lista_Imagen()

    def clickedVerListas():
        root.destroy()
        verListas = ver_listas(imagen, albumes_imagenes)
        verListas.ver_listaI()

    text = Label(root, text='IMAGEN')
    text.place(x=100, y=100)
    text.config(font=("Verdana", 50))
    # añadir botones

    btnMusica = Button(root, text="Agregar Imagen", command=clickedAgregar)
    btnMusica.place(x=50, y=200, height=50, width=100)
    btnImagen = Button(root, text="Crear Album", command=clickedCrearL)
    btnImagen.place(x=175, y=200, height=50, width=100)
    btnVideo = Button(root, text="Ver Albumes",command=clickedVerListas)
    btnVideo.place(x=300, y=200, height=50, width=100)
    btnVideo = Button(root, text="Ver Biblioteca", command=clickedVerBiblioteca)
    btnVideo.place(x=425, y=200, height=50, width=100)
    btnVideo = Button(root, text="Volver", command=clickedVolver)
    btnVideo.place(x=525, y=350, height=35, width=60)
    root.mainloop()

#crear ventana video
def ventanaVideo():
    root = Tk()
    root.geometry('626x417')
    root.title("RePOO")

    def clickedVolver():
        root.destroy()
        menuPrincipal = ventana()

    def clickedAgregar():
        root.destroy()
        ingreso = ingresar()
        ingreso.ingresar_video()

    def clickedCrearL():
        root.destroy()
        crearLista = crear_listas("video", lista_videos)
        crearLista.crear_lista()

    def clickedVerBiblioteca():
        root.destroy()
        lista = Ver_Todo(lista_canciones)
        lista.ver_Lista_Video()

    def clickedVerListas():
        root.destroy()
        verListas = ver_listas(video, albumes_videos)
        verListas.ver_listaV()

    text = Label(root, text='VIDEO')
    text.place(x=100, y=100)
    text.config(font=("Verdana", 50))
    # añadir botones

    btnMusica = Button(root, text="Agregar Video", command=clickedAgregar)
    btnMusica.place(x=50, y=200, height=50, width=100)
    btnImagen = Button(root, text="Crear Album", command=clickedCrearL)
    btnImagen.place(x=175, y=200, height=50, width=100)
    btnVideo = Button(root, text="Ver Albumes",command=clickedVerListas)
    btnVideo.place(x=300, y=200, height=50, width=100)
    btnVideo = Button(root, text="Ver Biblioteca", command=clickedVerBiblioteca)
    btnVideo.place(x=425, y=200, height=50, width=100)
    btnVideo = Button(root, text="Volver", command=clickedVolver)
    btnVideo.place(x=525, y=350, height=35, width=60)
    root.mainloop()

# crea ventana principal
def ventana():
    root = Tk()
    root.geometry('626x417')
    root.title("RePOO")

    def clickedMusica():
        root.destroy()
        musicaMM = ventanaMusica()

    def clickedImagen():
        root.destroy()
        ImagenMM = ventanaImagen()

    def clickedVideo():
        root.destroy()
        VideoMM = ventanaVideo()

    def clickedCerrar():
        root.destroy()

    # añadir imagen
    # imagen1 = PhotoImage(file='fondoV2.gif')
    # label1 = Label(root, image=imagen1)
    # label1.pack(side='top', fill='both', expand='yes')
    # añadir texto
    text = Label(root, text='bienvenido a RePOO')
    text.place(x=100, y=100)
    text.config(font=("Verdana", 30))
    # añadir botones
    btnMusica = Button(root, text="musica", command=clickedMusica)
    btnMusica.place(x=50, y=200, height=50, width=100)
    btnImagen = Button(root, text="Imagen", command=clickedImagen)
    btnImagen.place(x=250, y=200, height=50, width=100)
    btnVideo = Button(root, text="Videos", command=clickedVideo)
    btnVideo.place(x=450, y=200, height=50, width=100)
    btnVideo = Button(root, text="Cerrar", command=clickedCerrar)
    btnVideo.place(x=300, y=350, height=35, width=60)
    root.mainloop()

#clase de todos los archivos multimedia
class multimedia:
    def __init__(self, nombre, album, interprete, año):
        self.nombre = nombre
        self.album = album
        self.interprete = interprete
        self.año = año

    def get_nombre(self):
        return self.nombre

    def get_album(self):
        return self.album

    def get_interprete(self):
        return self.interprete

    def get_año(self):
        return self.año

# class cancion hereda de multimedia
class cancion(multimedia):
    def __init__(self, nombre, interprete, album, año, genero):
        self.nombre = nombre
        self.album = album
        self.interprete = interprete
        self.año = año
        self.genero = genero

    def get_genero(self):
        return self.genero

    def get_nombre(self):
        return self.nombre

    def get_interprete(self):
        return self.interprete

    def get_album(self):
        return self.album

    def get_año(self):
        return self.año

# hereda de multimedia
class imagen(multimedia):
    pass

# hereda de multimedia
class video(multimedia):
    pass


class Order:
    def __init__(self, lista, resultado, tipo):
        self.lista = lista
        self.resultado = resultado
        self.tipo = tipo

    def mostrar_ordenado(self):
        if self.tipo == "nombre":
            for i in range(len(self.resultado)):
                for j in range(len(self.lista)):
                    if self.resultado[i] == self.lista[j].nombre:
                        print(self.lista[j].nombre, self.lista[j].interprete, self.lista[j].album, self.lista[j].año)
        elif self.tipo == "autor":
            for i in range(len(self.resultado)):
                for j in range(len(self.lista)):
                    if self.resultado[i] == self.lista[j].interprete:
                        print(self.lista[j].interprete, self.lista[j].nombre, self.lista[j].album, self.lista[j].año)
        elif self.tipo == "album":
            for i in range(len(self.resultado)):
                for j in range(len(self.lista)):
                    if self.resultado[i] == self.lista[j].album:
                        print(self.lista[j].album, self.lista[j].nombre, self.lista[j].interprete, self.lista[j].año)
        elif self.tipo == "año":
            for i in range(len(self.resultado)):
                for j in range(len(self.lista)):
                    if self.resultado[i] == self.lista[j].año:
                        print(self.lista[j].año, self.lista[j].nombre, self.lista[j].interprete, self.lista[j].album)
        elif self.tipo == "genero":
            for i in range(len(self.resultado)):
                for j in range(len(self.lista)):
                    if self.resultado[i] == self.lista[j].genero:
                        print(self.lista[j].genero, self.lista[j].nombre, self.lista[j].interprete, self.lista[j].album,
                              self.lista[j].año)


class Ver:
    def __init__(self, lista):
        self.lista = lista
        self.sublista = []


class ver_alfabeticamente(Ver):
    def ver_alfabeticamente(self):
        for i in range(len(self.lista)):
            self.sublista.append(self.lista[i].nombre)

        resultado = sorted(self.sublista, key=operator.itemgetter(0))
        resultado1 = []
        for i in resultado:
            if i not in resultado1:
                resultado1.append(i)
        ordenado = Order(self.lista, resultado1, "nombre")
        ordenado.mostrar_ordenado()


class ver_por_autor(Ver):
    # ordenar los datos guardados por autor
    def ver_por_autor(self):
        for i in range(len(self.lista)):
            self.sublista.append(self.lista[i].interprete)

        resultado = sorted(self.sublista, key=operator.itemgetter(0))
        resultado1 = []
        for i in resultado:
            if i not in resultado1:
                resultado1.append(i)
        ordenado = Order(self.lista, resultado1, "autor")
        ordenado.mostrar_ordenado()


class ver_por_album(Ver):
    # ordenar los datos guaardados por album
    def ver_por_album(self):
        for i in range(len(self.lista)):
            self.sublista.append(self.lista[i].album)

        resultado = sorted(self.sublista, key=operator.itemgetter(0))
        resultado1 = []
        for i in resultado:
            if i not in resultado1:
                resultado1.append(i)
        ordenado = Order(self.lista, resultado1, "album")
        ordenado.mostrar_ordenado()


class ver_por_año(Ver):
    # ordenar los datos guardados por año
    def ver_por_año(self):
        for i in range(len(self.lista)):
            self.sublista.append(self.lista[i].año)

        resultado = sorted(self.sublista, key=operator.itemgetter(0))
        resultado1 = []
        for i in resultado:
            if i not in resultado1:
                resultado1.append(i)
        ordenado = Order(self.lista, resultado1, "año")
        ordenado.mostrar_ordenado()


class ver_por_genero(Ver):
    # ordenar los datos guardados por genero
    def ver_por_genero(self):
        for i in range(len(self.lista)):
            self.sublista.append(self.lista[i].genero)

        resultado = sorted(self.sublista, key=operator.itemgetter(0))
        resultado1 = []
        for i in resultado:
            if i not in resultado1:
                resultado1.append(i)
        ordenado = Order(self.lista, resultado1, "genero")
        ordenado.mostrar_ordenado()

# main ejecutable del programa
class Reproductor_multimedia:

    def __init__(self):
        pass

    def main(self):
        with open("Archivo.txt") as archivo:
            lineas = archivo.readlines()
            i = 0

            for item in lineas:
                caracteres = lineas[i].split("#")
                if caracteres[0] == "cancion":
                    lista_canciones.append(
                        cancion(caracteres[1], caracteres[2], caracteres[3], caracteres[4], caracteres[5]))
                    i += 1
                elif caracteres[0] == "imagen":
                    lista_imagenes.append(imagen(caracteres[1], caracteres[2], caracteres[3], caracteres[4], ))
                    i += 1
                elif caracteres[0] == "video":
                    lista_videos.append(imagen(caracteres[1], caracteres[2], caracteres[3], caracteres[4], ))
                    i += 1
                elif caracteres[0] == "listaCanciones":
                    lista = []
                    nombres = len(caracteres)
                    j = 1
                    while j < nombres:
                        lista.append(caracteres[j])
                        j += 1
                    listas_canciones.append(lista)
                    i += 1
                elif caracteres[0] == "listaImagenes":
                    lista = []
                    nombres = len(caracteres)
                    j = 1
                    while j < nombres:
                        lista.append(caracteres[j])
                        j += 1
                    albumes_imagenes.append(lista)
                    i += 1
                elif caracteres[0] == "listaVideos":
                    lista = []
                    nombres = len(caracteres)
                    j = 1
                    while j < nombres:
                        lista.append(caracteres[j])
                        j += 1
                    albumes_videos.append(lista)
                    i += 1
                elif caracteres[0] == "\n":
                    i += 1
                else:
                    print("error en el archivo, por favor reviselo")
                    exit()

        Reproductor = ventana()

reproducir = Reproductor_multimedia()
reproducir.main()