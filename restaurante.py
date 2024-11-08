from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox

operador = ''
precios_comida = [1.52, 1.65, 2.31, 3.22, 1.22, 1.99, 2.06, 2.65]
precios_bebida = [0.25, 0.99, 1.54, 1.21, 1.08, 2.00, 1.58, 1.10]
precios_postre = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]


def click_boton(numero):
    global operador
    operador = operador + numero
    visor.delete(0, END)
    visor.insert(END, operador)


def borrar():
    global operador
    operador = ''
    visor.delete(0, END)
    operador = ''


def revisar_check():
    contador = 0
    for c in cuadro_comida:
        if variable_comida[contador].get() == 1:
            cuadro_comida[contador].config(state=NORMAL)
            if cuadro_comida[contador] == 0:
                cuadro_comida[contador].delete(0, END)
            cuadro_comida[contador].focus()
        else:
            cuadro_comida[contador].config(state=DISABLED)
            texto_comida[contador].set('0')
        contador += 1

        # Check bebidas
    contador = 0
    for c in cuadro_bebida:
        if variable_bebida[contador].get() == 1:
            cuadro_bebida[contador].config(state=NORMAL)
            if cuadro_bebida[contador] == 0:
                cuadro_bebida[contador].delete(0, END)
            cuadro_bebida[contador].focus()
        else:
            cuadro_bebida[contador].config(state=DISABLED)
            texto_bebida[contador].set('0')
        contador += 1

        # Check Postres
    contador = 0
    for c in cuadro_postre:
        if variable_postre[contador].get() == 1:
            cuadro_postre[contador].config(state=NORMAL)
            if cuadro_postre[contador] == 0:
                cuadro_postre[contador].delete(0, END)
            cuadro_postre[contador].focus()
        else:
            cuadro_postre[contador].config(state=DISABLED)
            texto_postre[contador].set('0')
        contador += 1


def resultado():
    global operador
    resultados = str(eval(operador))
    visor.delete(0, END)
    visor.insert(0, resultados)


def total():
    sub_total_comida = 0
    precio = 0
    for cantidad in texto_comida:
        sub_total_comida = sub_total_comida + (float(cantidad.get()) * precios_comida[precio])
        precio += 1

    sub_total_bebida = 0
    precio = 0
    for cantidad in texto_bebida:
        sub_total_bebida = sub_total_bebida + (float(cantidad.get()) * precios_bebida[precio])
        precio += 1

    sub_total_postre = 0
    precio = 0
    for cantidad in texto_postre:
        sub_total_postre = sub_total_postre + (float(cantidad.get()) * precios_postre[precio])
        precio += 1

    sub_total = sub_total_comida + sub_total_bebida + sub_total_postre
    impuesto = sub_total * 0.21
    total = sub_total + impuesto

    var_costo_comida.set(f'€ {round(sub_total_comida, 2)}')
    var_costo_bebida.set(f'€ {round(sub_total_bebida, 2)}')
    var_costo_postre.set(f'€ {round(sub_total_postre, 2)}')
    var_costo_subtotal.set(f'€ {round(sub_total, 2)}')
    var_costo_impuesto.set(f'€ {round(impuesto, 2)}')
    var_costo_total.set(f'€ {round(total, 2)}')


def recibo():
    texto_recibo.delete(1.0, END)
    num_recibo = f'N# - {random.randint(1000, 9999)}'
    fecha = datetime.datetime.now()
    fecha_recibo = f'{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}'
    texto_recibo.insert(END, f'Datos:\t{num_recibo}\t\t{fecha_recibo}\n')
    texto_recibo.insert(END, f'*' * 55 + '\n')
    texto_recibo.insert(END, f'Items\t\tCant.\tCosto Items\n')
    texto_recibo.insert(END, f'-' * 55 + '\n')

    contador = 0
    for c in texto_comida:
        if c.get() != '0':
            texto_recibo.insert(END,
                                f'{lista_comida[contador]}\t\t{c.get()}\t€ {int(c.get()) + precios_comida[contador]}\n')
        contador += 1

    contador = 0
    for c in texto_bebida:
        if c.get() != '0':
            texto_recibo.insert(END,
                                f'{lista_bebida[contador]}\t\t{c.get()}\t€ {int(c.get()) + precios_bebida[contador]}\n')
        contador += 1

    contador = 0
    for c in texto_postre:
        if c.get() != '0':
            texto_recibo.insert(END,
                                f'{lista_postre[contador]}\t\t{c.get()}\t€ {int(c.get()) + precios_postre[contador]}\n')
        contador += 1

    texto_recibo.insert(END, f'-' * 55 + '\n')
    texto_recibo.insert(END, f'Costo comida: \t\t\t{var_costo_comida.get()}\n')
    texto_recibo.insert(END, f'Costo bebida: \t\t\t{var_costo_bebida.get()}\n')
    texto_recibo.insert(END, f'Costo postre: \t\t\t{var_costo_postre.get()}\n')
    texto_recibo.insert(END, f'-' * 55 + '\n')
    texto_recibo.insert(END, f'Sub-total: \t\t\t{var_costo_subtotal.get()}\n')
    texto_recibo.insert(END, f'Impuesto: \t\t\t{var_costo_impuesto.get()}\n')
    texto_recibo.insert(END, f'Total: \t\t\t{var_costo_total.get()}\n')
    texto_recibo.insert(END, f'-' * 55 + '\n')
    texto_recibo.insert(END, f'Gracias!!')


def guardar():
    info_recibo = texto_recibo.get(1.0, END)
    archivo = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo('Información', 'Su recibo ha sido guardado')

def resetear():
    texto_recibo.delete(0.1, END)

    for texto in texto_comida:
        texto.set(0)

    for texto in texto_postre:
        texto.set(0)

    for texto in texto_bebida:
        texto.set(0)

    for cuadro in cuadro_comida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadro_bebida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadro_postre:
        cuadro.config(state=DISABLED)

    for v in variable_comida:
        v.set(0)
    for v in variable_bebida:
        v.set(0)
    for v in variable_postre:
        v.set(0)

    var_costo_comida.set('')
    var_costo_bebida.set('')
    var_costo_postre.set('')
    var_costo_subtotal.set('')
    var_costo_impuesto.set('')
    var_costo_total.set('')

# iniciar tkinter
aplicacion = Tk()

# Tamaño de la venta
aplicacion.geometry('1020x630+0+0')

# Evitar maximizar
aplicacion.resizable(0, 0)

# Titulo Venta
aplicacion.title('Restaurante - Sistema de facturación')

# Color de fondo
aplicacion.config(bg='burlywood')

# Panel superior
panel_superior = Frame(aplicacion, bd=1, relief=FLAT)
panel_superior.pack(side=TOP)

# Etiqueta Titulo
etiqueta_titulo = Label(panel_superior, text='Sistema de Facturación', fg='azure4',
                        font=('Dosis', 58), bg='burlywood', width=27)

etiqueta_titulo.grid(row=0, column=0)

# Panel izquierdo
panel_izquierdo = Frame(aplicacion, bd=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT)

# Panel costos
panel_costos = Frame(panel_izquierdo, bd=1, relief=FLAT, bg='azure4', padx=60)
panel_costos.pack(side=BOTTOM)

# Panel comida
panel_comida = LabelFrame(panel_izquierdo, text='Comida', font=('Dosis', 19, 'bold'),
                          bd=1, relief=FLAT, fg='azure4')
panel_comida.pack(side=LEFT)

# Panel bebidas
panel_bebidas = LabelFrame(panel_izquierdo, text='Bebidas', font=('Dosis', 19, 'bold'),
                           bd=1, relief=FLAT, fg='azure4')
panel_bebidas.pack(side=LEFT)

# Panel postres
panel_postres = LabelFrame(panel_izquierdo, text='Postres', font=('Dosis', 19, 'bold'),
                           bd=1, relief=FLAT, fg='azure4')
panel_postres.pack(side=LEFT)

# Panel derecha
panel_derecha = Frame(aplicacion, bd=1, relief=FLAT)
panel_derecha.pack(side=RIGHT)

# Panel calculadora
calculadora = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
calculadora.pack()

# Panel recibo
panel_recibo = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_recibo.pack()

# Panel botones
panel_botones = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_botones.pack()

# Lista productos
lista_comida = ['Pollo', 'Cordero', 'Salmon', 'Merluza', 'Comida5', 'Comida6', 'Comida7', 'Comida8']
lista_bebida = ['Bebida1', 'Bebida2', 'Bebida3', 'Bebida4', 'Bebida5', 'Bebida6', 'Bebida7', 'Bebida8']
lista_postre = ['Postre1', 'Postre2', 'Postre3', 'Postre4', 'Postre5', 'Postre6', 'Postre7', 'Postre8', ]

# Generar items comida
variable_comida = []
cuadro_comida = []
texto_comida = []
contador = 0
for comida in lista_comida:
    # Crear checkButton
    variable_comida.append('')
    variable_comida[contador] = IntVar()
    comida = Checkbutton(panel_comida,
                         text=comida.title(),
                         font=('Dosis', 19, 'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variable_comida[contador],
                         command=revisar_check)
    comida.grid(row=contador,
                column=0,
                sticky=W)

    # Crear cuadros de comida
    cuadro_comida.append('')
    texto_comida.append('')
    texto_comida[contador] = StringVar()
    texto_comida[contador].set(0)
    cuadro_comida[contador] = Entry(panel_comida,
                                    font=('Dosis', 18, 'bold'),
                                    bd=1,
                                    width=8,
                                    state=DISABLED,
                                    textvariable=texto_comida[contador],
                                    )
    cuadro_comida[contador].grid(row=contador,
                                 column=1)

    contador += 1

# Generar items bebida
variable_bebida = []
cuadro_bebida = []
texto_bebida = []
contador = 0
for bebida in lista_bebida:
    variable_bebida.append('')
    variable_bebida[contador] = IntVar()
    bebida = Checkbutton(panel_bebidas,
                         text=bebida.title(),
                         font=('Dosis', 19, 'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variable_bebida[contador],
                         command=revisar_check)
    bebida.grid(row=contador,
                column=0,
                sticky=W)

    # Crear cuadros de bebida
    cuadro_bebida.append('')
    texto_bebida.append('')
    texto_bebida[contador] = StringVar()
    texto_bebida[contador].set(0)
    cuadro_bebida[contador] = Entry(panel_bebidas,
                                    font=('Dosis', 18, 'bold'),
                                    bd=1,
                                    width=8,
                                    state=DISABLED,
                                    textvariable=texto_bebida[contador])
    cuadro_bebida[contador].grid(row=contador,
                                 column=1)

    contador += 1

# Generar items postrea
variable_postre = []
cuadro_postre = []
texto_postre = []
contador = 0
for postre in lista_postre:
    variable_postre.append('')
    variable_postre[contador] = IntVar()
    postre = Checkbutton(panel_postres,
                         text=postre.title(),
                         font=('Dosis', 19, 'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variable_postre[contador],
                         command=revisar_check)
    postre.grid(row=contador,
                column=0,
                sticky=W)

    # Crear cuadros de postre
    cuadro_postre.append('')
    texto_postre.append('')
    texto_postre[contador] = StringVar()
    texto_postre[contador].set(0)
    cuadro_postre[contador] = Entry(panel_postres,
                                    font=('Dosis', 18, 'bold'),
                                    bd=1,
                                    width=8,
                                    state=DISABLED,
                                    textvariable=texto_postre[contador])
    cuadro_postre[contador].grid(row=contador,
                                 column=1)
    contador += 1

# Variables
var_costo_bebida = StringVar()
var_costo_comida = StringVar()
var_costo_postre = StringVar()
var_costo_subtotal = StringVar()
var_costo_impuesto = StringVar()
var_costo_total = StringVar()

# Etiqueta costos y campos de entrada
etiqueta_costo_comida = Label(panel_costos,
                              text='Costo comida',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')

etiqueta_costo_comida.grid(row=0,
                           column=0)

texto_costo_comida = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_comida)

texto_costo_comida.grid(row=0,
                        column=1,
                        padx=41)

# Bebida
etiqueta_costo_bebida = Label(panel_costos,
                              text='Costo bebida',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')

etiqueta_costo_bebida.grid(row=1,
                           column=0)

texto_costo_bebida = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_bebida)

texto_costo_bebida.grid(row=1,
                        column=1,
                        padx=41)

# postre
etiqueta_costo_postre = Label(panel_costos,
                              text='Costo postre',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')

etiqueta_costo_postre.grid(row=2,
                           column=0)

texto_costo_postre = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_postre)

texto_costo_postre.grid(row=2,
                        column=1,
                        padx=41)

# subtotal
etiqueta_subtotal = Label(panel_costos,
                          text='Subtotal',
                          font=('Dosis', 12, 'bold'),
                          bg='azure4',
                          fg='white')

etiqueta_subtotal.grid(row=0,
                       column=2)

texto_subtotal = Entry(panel_costos,
                       font=('Dosis', 12, 'bold'),
                       bd=1,
                       width=10,
                       state='readonly',
                       textvariable=var_costo_subtotal)

texto_subtotal.grid(row=0,
                    column=3,
                    padx=41)

# impuesto
etiqueta_impuesto = Label(panel_costos,
                          text='Impuesto',
                          font=('Dosis', 12, 'bold'),
                          bg='azure4',
                          fg='white')

etiqueta_impuesto.grid(row=1,
                       column=2)

texto_impuesto = Entry(panel_costos,
                       font=('Dosis', 12, 'bold'),
                       bd=1,
                       width=10,
                       state='readonly',
                       textvariable=var_costo_impuesto)

texto_impuesto.grid(row=1,
                    column=3,
                    padx=41)

# total
etiqueta_total = Label(panel_costos,
                       text='Total',
                       font=('Dosis', 12, 'bold'),
                       bg='azure4',
                       fg='white')

etiqueta_total.grid(row=2,
                    column=2)

texto_total = Entry(panel_costos,
                    font=('Dosis', 12, 'bold'),
                    bd=1,
                    width=10,
                    state='readonly',
                    textvariable=var_costo_total)

texto_total.grid(row=2,
                 column=3,
                 padx=41)

# botones

botones = ['Total', 'Recibo', 'Guardar', 'Restear']
botones_creados = []
columna = 0
for boton in botones:
    boton = Button(panel_botones,
                   text=boton.title(),
                   font=('Dosis', 14, 'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1,
                   width=9)
    botones_creados.append(boton)
    boton.grid(row=0,
               column=columna)
    columna += 1

botones_creados[0].config(command=total)
botones_creados[1].config(command=recibo)
botones_creados[2].config(command=guardar)
botones_creados[3].config(command=resetear)

# Recibo
texto_recibo = Text(panel_recibo,
                    font=('Dosis', 12, 'bold'),
                    bd=1,
                    width=42,
                    height=10)

texto_recibo.grid(row=0,
                  column=0)

# Calculadora
visor = Entry(calculadora,
              font=('Dosis', 16, 'bold'),
              width=32,
              bd=1)

visor.grid(row=0,
           column=0,
           columnspan=4)

botones_calculadora = ['7', '8', '9', '+',
                       '4', '5', '6', '-',
                       '1', '2', '3', 'x',
                       'CE', 'B', '0', '/']

botones_guardados = []
fila = 1
columna_calculadora = 0

for boton in botones_calculadora:
    boton = Button(calculadora,
                   text=boton.title(),
                   font=('Dosis', 16, 'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1,
                   width=6)

    botones_guardados.append(boton)

    boton.grid(row=fila,
               column=columna_calculadora)
    if columna_calculadora == 3:
        fila += 1

    columna_calculadora += 1

    if columna_calculadora == 4:
        columna_calculadora = 0

botones_guardados[0].config(command=lambda: click_boton('7'))
botones_guardados[1].config(command=lambda: click_boton('8'))
botones_guardados[2].config(command=lambda: click_boton('9'))
botones_guardados[3].config(command=lambda: click_boton('+'))
botones_guardados[4].config(command=lambda: click_boton('4'))
botones_guardados[5].config(command=lambda: click_boton('5'))
botones_guardados[6].config(command=lambda: click_boton('6'))
botones_guardados[7].config(command=lambda: click_boton('-'))
botones_guardados[8].config(command=lambda: click_boton('1'))
botones_guardados[9].config(command=lambda: click_boton('2'))
botones_guardados[10].config(command=lambda: click_boton('3'))
botones_guardados[11].config(command=lambda: click_boton('*'))
botones_guardados[12].config(command=resultado)
botones_guardados[13].config(command=borrar)
botones_guardados[14].config(command=lambda: click_boton('0'))
botones_guardados[15].config(command=lambda: click_boton('/'))

# Evitar que la pantalla se cierre
aplicacion.mainloop()
