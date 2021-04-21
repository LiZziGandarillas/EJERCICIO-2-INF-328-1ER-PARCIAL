# INTERFAZ DE LA CALCULADORA
import CalculadoraLib
from tkinter import *
expresion = "0"
def botonPresionado(num):
    global expresion
    if expresion == "0":
        expresion = ""
    expresion = expresion + str(num)
    ecuacion.set(expresion)
def botonIgual():
    try:
        global expresion
        total = CalculadoraLib.Calcular(expresion)
        ecuacion.set(CalculadoraLib.formato1(total))
        expresion = CalculadoraLib.formato2(total)
    except:
        ecuacion.set(" error ")
        expresion = "error"

def ac():
	global expresion
	expresion = ""
	ecuacion.set("")
def delete():
    global expresion
    if expresion == "error" or expresion == "" or len(expresion) == 1:
        expresion = ""
    else:
        expresion = expresion[:-1]
    ecuacion.set(expresion)

if __name__ == "__main__":
    ventana = Tk()
    ventana.configure(background="cyan")
    ventana.title("CALCULADORA")
    ventana.geometry("272x340")
    ecuacion = StringVar()
    ecuacion.set("")
    Label(text="", background="cyan").grid(row=0, column=0, ipadx=5)
    expresion_campo = Entry(ventana, textvariable=ecuacion, justify='right')
    expresion_campo.grid(row=1, column=1, columnspan=4, ipadx=58, ipady=7)
    Label(text="  ", background="cyan").grid(row=2, column=0, ipadx=2)

    botonAbrirParentesis = Button(ventana, text=' ( ', fg='white', bg='DodgerBlue4', command=lambda: botonPresionado("("), height=2, width=7)
    botonAbrirParentesis.grid(row=3, column=1)
    botonCerrarParentesis = Button(ventana, text=' ) ', fg='white', bg='DodgerBlue4', command=lambda: botonPresionado(")"), height=2, width=7)
    botonCerrarParentesis.grid(row=3, column=2)
    botonDel = Button(ventana, text='DEL', fg='black', bg='pink', command=delete, height=2, width=7)
    botonDel.grid(row=3, column=3)
    botonAc = Button(ventana, text='AC', fg='black', bg='pink', command=ac, width=7)
    botonAc.grid(row=3, column=4, rowspan=2,ipady=27)

    boton7 = Button(ventana, text=' 7 ', fg='white', bg='turquoise4', command=lambda: botonPresionado(7), height=2, width=7)
    boton7.grid(row=4, column=1)
    boton8 = Button(ventana, text=' 8 ', fg='white', bg='turquoise4', command=lambda: botonPresionado(8), height=2, width=7)
    boton8.grid(row=4, column=2)
    boton9 = Button(ventana, text=' 9 ', fg='white', bg='turquoise4', command=lambda: botonPresionado(9), height=2, width=7)
    boton9.grid(row=4, column=3)

    boton4 = Button(ventana, text=' 4 ', fg='white', bg='turquoise4', command=lambda: botonPresionado(4), height=2, width=7)
    boton4.grid(row=5, column=1)
    boton5 = Button(ventana, text=' 5 ', fg='white', bg='turquoise4', command=lambda: botonPresionado(5), height=2, width=7)
    boton5.grid(row=5, column=2)
    boton6 = Button(ventana, text=' 6 ', fg='white', bg='turquoise4', command=lambda: botonPresionado(6), height=2, width=7)
    boton6.grid(row=5, column=3)
    botonDividir = Button(ventana, text=' / ', fg='black', bg='white', command=lambda: botonPresionado("/"), height=2, width=7)
    botonDividir.grid(row=5, column=4)

    boton1 = Button(ventana, text=' 1 ', fg='white', bg='turquoise4', command=lambda: botonPresionado(1), height=2, width=7)
    boton1.grid(row=6, column=1)
    boton2 = Button(ventana, text=' 2 ', fg='white', bg='turquoise4', command=lambda: botonPresionado(2), height=2, width=7)
    boton2.grid(row=6, column=2)
    boton3 = Button(ventana, text=' 3 ', fg='white', bg='turquoise4', command=lambda: botonPresionado(3), height=2, width=7)
    boton3.grid(row=6, column=3)
    botonMultiplicar = Button(ventana, text=' * ', fg='black', bg='white', command=lambda: botonPresionado("*"), height=2, width=7)
    botonMultiplicar.grid(row=6, column=4)

    boton0 = Button(ventana, text=' 0 ', fg='white', bg='turquoise4', command=lambda: botonPresionado(0), height=2, width=7)
    boton0.grid(row=7, column=1)
    botonPunto= Button(ventana, text='.', fg='white', bg='turquoise4', command=lambda: botonPresionado('.'), height=2, width=7)
    botonPunto.grid(row=7, column=2)
    botonSumar = Button(ventana, text=' + ', fg='black', bg='white', command=lambda: botonPresionado("+"), height=2, width=7)
    botonSumar.grid(row=7, column=3)
    botonRestar = Button(ventana, text=' - ', fg='black', bg='white', command=lambda: botonPresionado("-"), height=2, width=7)
    botonRestar.grid(row=7, column=4)
    botonIgual = Button(ventana, text=' = ', fg='black', bg='white', command=botonIgual, height=2)
    botonIgual.grid(row=8, column=1, columnspan=4, ipadx=108)
    
    
    ventana.mainloop()    
