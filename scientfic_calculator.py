from Tkinter import*
from numpy import*
from visual import*


win = Tk()

win.title('Faltu ladka')

e = Entry(win,width=90,borderwidth=5)
e.grid(row=0,column=0,padx=10,pady=10,columnspan=10)

#Intergration start-----------------------------------------------------------------------------------------------------------------

def intergration():
    
    win2=Tk()
    win2.title("Intergration")

    dia_ask = Label(win2,text="Choose the mode of Intergration").grid(row=0,column=0,pady=5,padx=30)
            
    
        
    def sin_int():
        
        fun = Label(win2,text="Enter the function:").grid(row=3,column=0,padx=50,pady=5,columnspan=1)
        fun_e = Entry(win2,width=40,borderwidth=5).grid(row=4,column=0,padx=50,pady=5)

        up_lim = Label(win2,text="Enter the lower limit:").grid(row=5,column=0,padx=50,pady=5)
        up_lim_e = Entry(win2,width=20,borderwidth=5).grid(row=6,column=0,padx=50,pady=5)

        lo_lim = Label(win2,text="Enter the upper limit:").grid(row=7,column=0,padx=50,pady=5)
        lo_lim_e = Entry(win2,width=20,borderwidth=5).grid(row=8,column=0,padx=50,pady=5)
        
        btn_result = Button(win2,padx=30,pady=5,text="Result",command=result1).grid(row=9,column=0,pady=5,padx=30)

        #btn_dou_int = Button(win2,padx=10,pady=5,text="Double Intergration",command=dob_int,state=DISABLED).grid(row=2,column=0,pady=5,padx=30)
    

    def dob_int():
        
        
        fun = Label(win2,text="Enter the function:").grid(row=3,column=0,padx=50,pady=5,columnspan=1)
        fun_e = Entry(win2,width=40,borderwidth=5).grid(row=4,column=0,padx=50,pady=5)

        up_lim_x = Label(win2,text="Enter the lower limit of x:").grid(row=5,column=0,padx=50,pady=5)
        up_lim_e_x = Entry(win2,width=20,borderwidth=5).grid(row=6,column=0,padx=50,pady=5)

        lo_lim_x = Label(win2,text="Enter the upper limit of x:").grid(row=7,column=0,padx=50,pady=5)
        lo_lim_e_x = Entry(win2,width=20,borderwidth=5).grid(row=8,column=0,padx=50,pady=5)
        
        up_lim_y = Label(win2,text="Enter the lower limit of y:").grid(row=9,column=0,padx=50,pady=5)
        up_lim_e_y = Entry(win2,width=20,borderwidth=5).grid(row=10,column=0,padx=50,pady=5)

        lo_lim_y = Label(win2,text="Enter the upper limit of y:").grid(row=11,column=0,padx=50,pady=5)
        lo_lim_e_y = Entry(win2,width=20,borderwidth=5).grid(row=12,column=0,padx=50,pady=5)
        
        
        btn_result = Button(win2,padx=30,pady=5,text="Result",command=result2).grid(row=13,column=0,pady=5,padx=30)

        #btn_sin_int = Button(win2,padx=10,pady=5,text="Single Intergration",command=sin_int,state=DISABLED).grid(row=1,column=0,pady=5,padx=30)

    
    
    def result1():
            fun_res = Label(win2,text="The Intergal value is:").grid(row=10,column=0,pady=5,padx=30)
            
    def result2():
            fun_res = Label(win2,text="The Intergal value is:").grid(row=14,column=0,pady=5,padx=30)
    
        
    btn_dou_int = Button(win2,padx=10,pady=5,text="Double Intergration",command=dob_int).grid(row=2,column=0,pady=5,padx=30)
    btn_sin_int = Button(win2,padx=10,pady=5,text="Single Intergration",command=sin_int).grid(row=1,column=0,pady=5,padx=30)

#intergration end----------------------------------------------------------------------------------------------------------------

def complex_():
    
    win3=Tk()
    win3.title("Complex")

    
    
    
def diff_eq():
    
    win4=Tk()
    win4.title("Differential Equation")
    
def about():
    
    win5=Tk()
    win5.title("About")
    mylabel=Label(win5,text="""********************************

                          This software is devolped by Niranjan Gupta in python.
                          this software will solve most comman problem in math and physics.         




                            """)

    mylabel.grid(row=0,column=0)
    
def ske_graph():
    
    win6=Tk()
    win6.title("Skecth Graph")
    
def Help():
    
    win7=Tk()
    win7.title("Help")

        


#numeric calculater-----------------------------------------

def button_1_x():
    num = e.get()
    e.delete(0,END)
    e.insert(0,1.0/(int(num)))
    
def button_1_x2():
    num = e.get()
    e.delete(0,END)
    e.insert(0,1.0/(float(num))**2)
    
def button_1_x3():
    num = e.get()
    e.delete(0,END)
    e.insert(0,1.0/(float(num))**3)

def button_1_xn():
    first_num=e.get()
    global f_num
    global math
    math="1xn"
    f_num=float(first_num)
    e.delete(0,END)

    
   
            
def button_x_2():
    num=e.get()
    e.delete(0,END)
    e.insert(0,(float(num))**2)

def button_x_3():
    num = e.get()
    e.delete(0,END)
    e.insert(0,(float(num))**3)
   
def button_xn():
    first_num=e.get()
    global f_num
    global math
    math="xn"
    f_num=float(first_num)
    e.delete(0,END)
       
    
def button_click(number):
    curent = e.get()
    e.delete(0,END)
    e.insert(0,str(curent) + str(number))
    
def button_add():
    first_num=e.get()
    global f_num
    global math
    math="add"
    f_num=float(first_num)
    e.delete(0,END)


def button_sub():
    
    first_num=e.get()
    global f_num
    global math
    math="sub"
    f_num=float(first_num)
    e.delete(0,END)

def button_mul():
    first_num=e.get()
    global f_num 
    global math
    math="mul"
    f_num=float(first_num)
    e.delete(0,END)

def button_div():
    first_num=e.get()
    global f_num
    global math
    math="div"
    f_num=float(first_num)
    e.delete(0,END)
    




def button_equal():   
    second_number=e.get()
    e.delete(0,END)
    if math=="add":
        e.insert(0,f_num + float(second_number))
        
    if math=="sub":
        e.insert(0,f_num - float(second_number))
        
    if math=="mul":
        e.insert(0,f_num * float(second_number))

    if math=="div":
        e.insert(0,f_num / float(second_number))
    
    if math=="1xn":
        e.insert(0,1.0/f_num**(float(second_number)))
        
    if math=="xn":
        e.insert(0,f_num**(float(second_number)))
    
    
def button_clear():
    e.delete(0,END)
    
def sine():
    m=e.get()
    e.delete(0,END)
    e.insert(0,sin(float(m)))
  
def cose():
    m=e.get()
    e.delete(0,END)
    e.insert(0,cos(float(m)))

def tane():
    m=e.get()
    e.delete(0,END)
    e.insert(0,tan(float(m)))

def ex():
    m=e.get()
    e.delete(0,END)
    e.insert(0,exp(float(m)))

def sqrte():
    m=e.get()
    e.delete(0,END)
    e.insert(0,(float(m))**0.5)

def e_x():
    m=e.get()
    e.delete(0,END)
    e.insert(0,exp(-(float(m))))

def facte():
    m=e.get()
    e.delete(0,END)
    num=int(m)
    fact=1
    for i in range(1,num+1):
        fact *= i
    e.insert(0,fact)

def loge():
    m=e.get()
    e.delete(0,END)
    e.insert(0,log(float(m))/log(10))

def lne():
    m=e.get()
    e.delete(0,END)
    e.insert(0,log(float(m)))

def arcsine():
    m=e.get()
    e.delete(0,END)
    e.insert(0,arcsin(float(m)))

def arccose():
    m=e.get()
    e.delete(0,END)
    e.insert(0,arccos(float(m)))



    
# End numeric calculaetr--------------------------------------------------------    


btn_sin = Button(win,text="sin(x)",padx=27,pady=10,command = sine).grid(row=2,column=0,pady=10,padx=5)
btn_cos = Button(win,text="cos(x)",padx=27,pady=10,command = cose).grid(row=2,column=1,padx=5)
btn_tan = Button(win,text="tan(x)",padx=27,pady=10,command = tane).grid(row=2,column=2,padx=5)

btn_log = Button(win,text="ln(x)",padx=30,pady=10,command = lne).grid(row=3,column=0,pady=5)
btn_ln = Button(win,text="log(x)",padx=27,pady=10,command = loge).grid(row=3,column=1)
btn_ex = Button(win,text="e^x",padx=32,pady=10,command = ex).grid(row=3,column=2)

btn_e_x = Button(win,text="e^-x",padx=30,pady=10,command = e_x).grid(row=4,column=0,pady=5)
btn_sqrt = Button(win,text="sqrt(x)",padx=25,pady=10,command = sqrte).grid(row=4,column=1)
btn_fact = Button(win,text="fact(n)",padx=25,pady=10,command = facte).grid(row=4,column=2)

btn_add = Button(win,text="+",padx=26,pady=10,command = button_add).grid(row=2,column=3)
btn_sub = Button(win,text="-",padx=27,pady=10,command = button_sub).grid(row=3,column=3)
btn_mul = Button(win,text="*",padx=27,pady=10,command = button_mul).grid(row=4,column=3)
btn_div = Button(win,text="/",padx=27,pady=10,command = button_div).grid(row=5,column=3)

btn_arccos = Button(win,text="arccos(x)",padx=19,pady=10,command = arccose).grid(row=5,column=2)
btn_equal = Button(win,text="=",padx=38,pady=10,command = button_equal).grid(row=5,column=0,pady=5)
btn_clear = Button(win,text="clear",padx=30,pady=10,command=button_clear).grid(row=1,column=0)

btn_x2 = Button(win,text="x^2",padx=32,pady=10,command=button_x_2).grid(row=1,column=1)
btn_x3 = Button(win,text="x^3",padx=32,pady=10,command=button_x_3).grid(row=1,column=2)
btn_x_n = Button(win,text="x^n",padx=21.4,pady=10,command=button_xn).grid(row=1,column=3)

btn_arcsin = Button(win,text="arcsin(x)",padx=19,pady=10,command = arcsine).grid(row=5,column=1)

btn_int = Button(win,text="Intergration",padx=14,pady=10,command=intergration).grid(row=1,column=6,padx=5)
btn_complex = Button(win,text="Complex",padx=20,pady=10,command=complex_).grid(row=2,column=6)
btn_skecth = Button(win,text="Skecth graph",padx=10,pady=10,command=ske_graph).grid(row=3,column=6)
btn_about = Button(win,text="About",padx=28,pady=10,command=about).grid(row=5,column=6)
btn_diff_eq = Button(win,text="Diff-eqation",padx=12,pady=10,command=diff_eq).grid(row=4,column=6)

btn_1_x = Button(win,text="1/x",padx=26.5,pady=10,command=button_1_x).grid(row=1,column=5,padx=5)
btn_1_x2 = Button(win,text="1/x^2",padx=20.5,pady=10,command=button_1_x2).grid(row=2,column=5)
btn_1_x3 = Button(win,text="1/x^3",padx=20.5,pady=10,command=button_1_x3).grid(row=3,column=5)
btn_1_xn = Button(win,text="1/x^n",padx=20.5,pady=10,command=button_1_xn).grid(row=4,column=5)
btn_help = Button(win,text="Help",padx=25,pady=10,command=Help).grid(row=5,column=5)

#btn_1 = Button(win,padx=10,pady=10).grid(row=1,column=0)
#btn_1 = Button(win,padx=10,pady=10).grid(row=1,column=0)
#btn_1 = Button(win,padx=10,pady=10).grid(row=1,column=0)
#btn_1 = Button(win,padx=10,pady=10).grid(row=1,column=0)
#btn_1 = Button(win,padx=10,pady=10).grid(row=1,column=0)









win.mainloop()
