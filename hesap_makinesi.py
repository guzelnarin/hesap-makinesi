import tkinter as tk
from ttkthemes import ThemedTk
import math

root = tk.Tk()

expression = ""
equation = tk.StringVar()


def press(ifade):
    global expression
    expression = expression + str(ifade)
    equation.set(expression)

def mat_islem():
    global expression
    expression = expression.replace(',', '.')
    total = str(eval(expression))
    equation.set(f"{total}")
    expression=""


def clear():
    global expression
    expression = ""
    equation.set("") 



def kok_alma():
    try:
        global expression
        expression = float(expression.replace(',', '.'))
        kok = math.sqrt(expression)
        equation.set(f"{kok:.2f}")
    except:
        equation.set("Hata")
    expression = ""




def faktoriyel_alma():
    try:
        global expression
        sayi = int(expression)
        faktoriyel = 1
        if sayi >= 0:
            for i in range(1, sayi + 1):
                faktoriyel *= i
            equation.set(str(faktoriyel))
        else:
            equation.set("Sayı 0'dan kucuk")
    except:
        equation.set("Hata")



def log_alma():
    try:
      global expression
      expression=float(expression.replace(',','.'))
      taban=10
      log =logaritma = math.log(expression, taban)
      equation.set(f"{log:.4f}")

    except:
        equation.set("Hata")   

def us_alma():
    try:
       global expression
       parts = expression.split(',')
       if len(parts) == 2:
            taban = float(parts[0].replace(',', '.'))
            us = float(parts[1].replace(',', '.'))
            sonuc = math.pow(taban, us)
            equation.set(sonuc)

       else:
           equation.set("Hatalı deger")    
    except:
        equation.set("Hata")        

    
        
    
root.configure(background="white") 
root.title("Hesap Makinesi") 

expression_field = tk.Entry(root, textvariable=equation, font=("Verdana", 10, "bold")) 
expression_field.grid(columnspan=4)

button9 = tk.Button(root, bg='light blue',command= lambda:press(9), activebackground='light blue', borderwidth=0, text='9', relief='flat',font=("Verdana"),width=5)
button9.grid(row='2',column='3',padx='2',pady='1')

button8= tk.Button(root, bg='light blue',command= lambda:press(8), activebackground='light blue',borderwidth=0, text='8', relief='flat', font=("Verdana"),width=5)
button8.grid(row='2',column='2',padx='1',pady='1')

button7= tk.Button(root, bg='light blue',command= lambda:press(7), activebackground='light blue',borderwidth=0, text='7', relief='flat', font=("Verdana"),width=5)
button7.grid(row='2',column='1',padx='1',pady='1')

button6=tk.Button(root, bg='light blue',command= lambda:press(6), activebackground='light blue',borderwidth=0, text='6', relief='flat', font=("Verdana"),width=5)
button6.grid(row='3',column='3',padx='1',pady='1')

button5= tk.Button(root, bg='light blue',command= lambda:press(5), activebackground='light blue',borderwidth=0, text='5', relief='flat', font=("Verdana"),width=5)
button5.grid(row='3',column='2',padx='1',pady='1')

button4= tk.Button(root, bg='light blue',command= lambda:press(4), activebackground='light blue',borderwidth=0, text='4', relief='flat', font=("Verdana"),width=5)
button4.grid(row='3',column='1',padx='1',pady='1')

button3= tk.Button(root, bg='light blue',command= lambda:press(3), activebackground='light blue',borderwidth=0, text='3', relief='flat', font=("Verdana"),width=5)
button3.grid(row='4',column='3',padx='1',pady='1')

button2= tk.Button(root,bg='light blue',command= lambda:press(2), activebackground='light blue',borderwidth=0, text='2', relief='flat', font=("Verdana"),width=5)
button2.grid(row='4',column='2',padx='1',pady='1')

button1= tk.Button(root, bg='light blue',command= lambda:press(1), activebackground='light blue',borderwidth=0, text='1', relief='flat', font=("Verdana"),width=5)
button1.grid(row='4',column='1',padx='1',pady='1')

button0= tk.Button(root, bg='light blue',command= lambda:press(0), activebackground='light blue',borderwidth=0, text='0', relief='flat', font=("Verdana"),width=5)
button0.grid(row='5',column='1',padx='1',pady='1')

button_virgul= tk.Button(root,bg='gray',command= lambda:press(","), activebackground='gray', text=',',borderwidth=0, relief='flat', font=("Verdana"),width=5)
button_virgul.grid(row='5',column='2',padx='1',pady='1')

button_carpi= tk.Button(root,bg='gray', command= lambda:press("*"),activebackground='gray', text='x',borderwidth=0, relief='flat', font=("Verdana"),width=5)
button_carpi.grid(row='3',column='4',padx='1',pady='1')

button_bolu= tk.Button(root,bg='gray',command= lambda:press("/"),activebackground='gray', text='/',borderwidth=0, relief='flat', font=("Verdana"),width=5)
button_bolu.grid(row='2',column='4',padx='1',pady='1')

button_eksi= tk.Button(root, bg='gray',command= lambda:press("-"), activebackground='gray', text='-',borderwidth=0, relief='flat', font=("Verdana"),width=5)
button_eksi.grid(row='4',column='4',padx='1',pady='1')

button_toplama= tk.Button(root, bg='gray',command= lambda:press("+"), activebackground='gray',borderwidth=0, text='+', relief='flat', font=("Verdana"),width=5)
button_toplama.grid(row='5',column='4',padx='1',pady='1')

button_esittir= tk.Button(root, bg='gray',command=mat_islem, activebackground='gray',borderwidth=0, text='=', relief='flat', font=("Verdana"),width=5)
button_esittir.grid(row='5',column='3',padx='1',pady='1')

button_sil = tk.Button(root, text='Clear', bg='red',activebackground='red',command=clear, borderwidth=0, relief='flat',  width=5,font=("Verdana")) 
button_sil.grid(row=1, column='5',padx='1',pady='1') 

button_koklusayi = tk.Button(root, text=" √", bg="gray", command=kok_alma, borderwidth=0, activebackground='gray', relief='flat',width=5, font=('Verdana') )
button_koklusayi.grid(row='3', column='5')

button_uslusayi = tk.Button(root, text="x!", bg="gray", command=faktoriyel_alma, borderwidth=0, activebackground='gray', relief='flat',width=5, font=('Verdana') )
button_uslusayi.grid(row='2', column='5')

button_uslusayi = tk.Button(root, text="log", bg="gray", command=log_alma, borderwidth=0, activebackground='gray', relief='flat',width=5, font=('Verdana') )
button_uslusayi.grid(row='4', column='5')

button_uslusayi = tk.Button(root, text="x^y", bg="gray", command=us_alma, borderwidth=0, activebackground='gray', relief='flat',width=5, font=('Verdana') )
button_uslusayi.grid(row='5', column='5')




root.mainloop()