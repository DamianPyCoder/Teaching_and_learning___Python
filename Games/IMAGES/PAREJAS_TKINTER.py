import random
import tkinter as tk

class JuegoDeParejas:
    def __init__(self, ventana, letras, filas=4, columnas=6):
        self.ventana = ventana
        self.letras = letras
        self.filas = filas
        self.columnas = columnas
        self.ancho = 8
        self.altura = 5
        
        self.botones = []
        self.parejas = []
        self.parejas_descubiertas = 0
        self.primer_boton = None
        
        # Crear los botones
        for fila in range(filas):
            fila_botones = []
            for columna in range(columnas):
                boton = tk.Button(ventana, width=self.ancho, height=self.altura,
                                  command=lambda fila=fila, columna=columna: self.seleccionar(fila, columna))
                fila_botones.append(boton)
                boton.grid(row=fila, column=columna)
            self.botones.append(fila_botones)
        
        # Crear las parejas de letras
        letras_duplicadas = list(letras * 2)
        random.shuffle(letras_duplicadas)
        for i in range(filas * columnas // 2):
            letra = letras_duplicadas[i]
            self.parejas.append(letra)
            self.parejas.append(letra)
        random.shuffle(self.parejas)
    
    def seleccionar(self, fila, columna):
        letra = self.parejas[fila * self.columnas + columna]
        self.botones[fila][columna].config(text=letra, state='disabled')
        if self.primer_boton is None:
            self.primer_boton = (fila, columna)
        else:
            fila1, columna1 = self.primer_boton
            if (fila, columna) != (fila1, columna1) and self.parejas[fila * self.columnas + columna] == self.parejas[fila1 * self.columnas + columna1]:
                self.parejas_descubiertas += 1
                if self.parejas_descubiertas == self.filas * self.columnas // 2:
                    self.reiniciar_juego()
            else:
                self.ventana.after(1000, lambda: self.ocultar(fila, columna, fila1, columna1))
                self.botones[fila][columna].config(state='active')
                self.botones[fila1][columna1].config(state='active')
            self.primer_boton = None
    
    def ocultar(self, fila1, columna1, fila2, columna2):
        self.botones[fila1][columna1].config(text='', state='active')
        self.botones[fila2][columna2].config(text='', state='active')
    
    def reiniciar_juego(self):
        if tk.messagebox.askyesno('¡Felicidades!', '¡Has encontrado todas las parejas! ¿Quieres jugar otra partida?'):
            self.ventana.destroy()
            juego = JuegoDeParejas(tk.Tk(), self.letras)
            juego.ventana.mainloop()
        else:
            self.ventana.destroy()

letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ventana = tk.Tk()
juego = JuegoDeParejas(ventana, letras)
ventana.mainloop()
