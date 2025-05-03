from tkinter import *

from tkinter.messagebox import *

import math as m 

font=('Verdana', 22, 'bold')


# FUNCTIONS FOR BINDING OF BUTTONS

def click_btn_function(event):
    print("btn clicked")
    b=event.widget
    text=b['text']
    print(text)
    if text=='X':
        text_field.insert(END, '*')
        return;
    if text=='÷':
        text_field.insert(END, '/')
        return;

    if text=='=':
        try:
            ex=text_field.get()
            answer=eval(ex)
            text_field.delete(0,END)
            text_field.insert(0,answer)
        except Exception as e:
            print("Error...", e)
            showerror("Error..",e)
            return
 
    text_field.insert(END, text)

# clear function

def all_clear():
    text_field.delete(0,END)    

def clear():
    ex=text_field.get()
    ex=ex[0:len(ex)-1]
    text_field.delete(0,END)
    text_field.insert(0,ex)

#creating  window

window = Tk()
window.title("Vicky's Calculator")
window.geometry('500x600')

# picture label 

headinglabel=Label(window, text="Vicky's",font=('ALGERIAN', 14))
headinglabel.pack(side=TOP,pady=5)

heading=Label(window, text="Calculator", font= ('ALGERIAN', 14), underline=0)
heading.pack(side=TOP)

#text field 
text_field= Entry(window, font=font, justify=CENTER)
text_field.pack(side=TOP,pady= 10, fill=X, padx=20 )

button_frame= Frame(window)
button_frame.pack(side=TOP)

#adding 0-9 keys
temp=1
for i in range (0,3):
    for j in range (0,3):
        btn1_9=Button(button_frame, font= font , text= str(temp), width=5, activebackground= 'green', activeforeground='white')
        btn1_9.grid(row=i,column=j, pady=5, padx=5)
        temp=temp+1
        btn1_9.bind('<Button-1>', click_btn_function)

#entring the 0,.,= keys 

dotbtn=Button(button_frame, font= font , text= ".", width=5, activebackground= 'green', activeforeground='white')
dotbtn.grid(row=3,column=0, pady=5, padx=5)

zerobtn=Button(button_frame, font= font , text= "0", width=5, activebackground= 'green', activeforeground='white')
zerobtn.grid(row=3,column=1, pady=5, padx=5)

equalbtn=Button(button_frame, font= font , text= "=", width=5, activebackground= 'green', activeforeground='white')
equalbtn.grid(row=3,column=2, pady=5, padx=5)

# Entring the function keys 

dividebtn=Button(button_frame, font= font , text= "÷", width=5, activebackground= 'green', activeforeground='white')
dividebtn.grid(row=0,column=3, pady=5, padx=5)

multiplybtn=Button(button_frame, font= font , text= "X", width=5, activebackground= 'green', activeforeground='white')
multiplybtn.grid(row=1,column=3, pady=5, padx=5)

plusbtn=Button(button_frame, font= font , text= "+", width=5, activebackground= 'green', activeforeground='white')
plusbtn.grid(row=2,column=3, pady=5, padx=5)

minusbtn=Button(button_frame, font= font , text= "-", width=5, activebackground= 'green', activeforeground='white')
minusbtn.grid(row=3,column=3, pady=5, padx=5)

clrbtn=Button(button_frame, font= font , text= "<--", width=10, activebackground= 'green', activeforeground='white', command=clear)
clrbtn.grid(row=4,column=0, columnspan= 2, pady=5, padx=5)

acbtn=Button(button_frame, font= font , text= "AC", width=10, activebackground= 'green', activeforeground='white', command=all_clear)
acbtn.grid(row=4,column=2, columnspan=2, pady=5, padx=5)

# BINDING ALL BUTTONS

dividebtn.bind('<Button-1>', click_btn_function)
multiplybtn.bind('<Button-1>', click_btn_function)
plusbtn.bind('<Button-1>', click_btn_function)
minusbtn.bind('<Button-1>', click_btn_function)

zerobtn.bind('<Button-1>', click_btn_function)
equalbtn.bind('<Button-1>', click_btn_function)
dotbtn.bind('<Button-1>', click_btn_function)
def enterclick(event):
    print('enter')
    e=Event()
    e.widget=equalbtn
    click_btn_function(e)

window.bind('<Return>', enterclick)

# start working for scientific calculator
#functions
scframe=Frame(window)
sqrtbtn=Button(scframe, font= font , text= "√", width=5, activebackground= 'green', activeforeground='white')
sqrtbtn.grid(row=0,column=0, pady=5, padx=5)

powbtn=Button(scframe, font= font , text= "^", width=5, activebackground= 'green', activeforeground='white')
powbtn.grid(row=0,column=1, pady=5, padx=5)

factbtn=Button(scframe, font= font , text= "x!", width=5, activebackground= 'green', activeforeground='white')
factbtn.grid(row=0,column=2, pady=5, padx=5)

radbtn=Button(scframe, font= font , text= "to Rad", width=5, activebackground= 'green', activeforeground='white')
radbtn.grid(row=0,column=3, pady=5, padx=5)

degbtn=Button(scframe, font= font , text= "to Deg", width=5, activebackground= 'green', activeforeground='white')
degbtn.grid(row=1,column=0, pady=5, padx=5)

sinbtn=Button(scframe, font= font , text= "sin Ɵ", width=5, activebackground= 'green', activeforeground='white')
sinbtn.grid(row=1,column=1, pady=5, padx=5)

cosbtn=Button(scframe, font= font , text= "cos Ɵ", width=5, activebackground= 'green', activeforeground='white')
cosbtn.grid(row=1,column=2, pady=5, padx=5)

tanbtn=Button(scframe, font= font , text= "tan Ɵ", width=5, activebackground= 'green', activeforeground='white')
tanbtn.grid(row=1,column=3, pady=5, padx=5)




normalcalc=True
def calculate_sc(event):
    print ('button clicked')
    btn=event.widget
    text=btn['text']
    ex=text_field.get()
    print(text)
    answer=''
    if text=='to Deg':
        print("Cal Degree")
        answer=str(m.degrees(float(ex)))
    elif text=='to Rad':
        print('Cal Radian')
        answer=str(m.radians(float(ex)))
    elif text=='x!':
        print('cal Factorial')
        answer=str(m.factorial(int(ex)))
    elif text=='sin Ɵ':
        print('cal sin Ɵ')    
        answer=str(m.sin(m.radians(int(ex))))        
    elif text=='cos Ɵ':
        print('cal cos Ɵ ')    
        answer=str(m.cos(m.radians(int(ex))))        
    elif text=='tan Ɵ':
        print('cal tan Ɵ')  
        answer=str(m.tan(m.radians(int(ex))))
    elif text=='√':
        print('cal sqaure root') 
        answer=str(m.sqrt(int(ex)))
    elif text=='^':
        print('cal power')  
        base,pow=ex.split(',')
        print(base)
        print(pow)
        answer=m.pow(int(base),int(pow))
    text_field.delete(0, END)             
    text_field.insert(0, answer)          

def sc_click():
    global normalcalc
    if normalcalc:
        button_frame.pack_forget()
        scframe.pack(side=TOP, pady=20)
        button_frame.pack(side=TOP)
        window.geometry('510x700')
        print("show Scientific")
        normalcalc=False
    else:
        print ("Show Normal")
        scframe.pack_forget()
        window.geometry('500x600')
        normalcalc=True    
    print('clicked')

sqrtbtn.bind("<Button-1>", calculate_sc) 
powbtn.bind("<Button-1>", calculate_sc)
factbtn.bind("<Button-1>", calculate_sc) 
radbtn.bind("<Button-1>", calculate_sc) 
degbtn.bind("<Button-1>", calculate_sc) 
sinbtn.bind("<Button-1>", calculate_sc) 
cosbtn.bind("<Button-1>", calculate_sc) 
tanbtn.bind("<Button-1>", calculate_sc) 


fontmenu=('', 15)
menubar=Menu(window, font=fontmenu)
mode=Menu(menubar, font=fontmenu, tearoff=0)
mode.add_checkbutton(label="Scientific Calculator", command=sc_click)
menubar.add_cascade(label="Mode",menu=mode)
window.config(menu=menubar)


window.mainloop()
