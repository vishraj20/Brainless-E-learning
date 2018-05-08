from tkinter import *
import log

def main():
    def close():
        window.destroy()    
    def open1():
        window = Tk()
        window.wm_title("Brainless E-learning")
        list1=Listbox(window, height=40,width=150)
        list1.grid(row=2,column=0,rowspan=16,columnspan=20)
        sb1=Scrollbar(window)
        sb1.grid(row=2,column=21,rowspan=16)
        list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=list1.yview)
        file = open('C programming_tutorial.txt','r')
        lines = file.readlines()
        file.close()
        for line in lines:
            line = line.strip()
            list1.insert(END,line)
        window.mainloop()
    def open2():
        window = Tk()
        window.wm_title("Brainless E-learning")
        list1=Listbox(window, height=40,width=150)
        list1.grid(row=2,column=0,rowspan=16,columnspan=20)
        sb1=Scrollbar(window)
        sb1.grid(row=2,column=21,rowspan=16)
        list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=list1.yview)
        file = open('cpp1.txt','r')
        lines = file.readlines()
        file.close()
        for line in lines:
            line = line.strip()
            list1.insert(END,line)
        window.mainloop()
    def open3():
        window = Tk()
        window.wm_title("Brainless E-learning")
        list1=Listbox(window, height=40,width=150)
        list1.grid(row=2,column=0,rowspan=16,columnspan=20)
        sb1=Scrollbar(window)
        sb1.grid(row=2,column=21,rowspan=16)
        list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=list1.yview)
        file = open('css.txt','r')
        lines = file.readlines()
        file.close()
        for line in lines:
            line = line.strip()
            list1.insert(END,line)
        window.mainloop()
    def open4():
        window = Tk()
        window.wm_title("Brainless E-learning")
        list1=Listbox(window, height=40,width=150)
        list1.grid(row=2,column=0,rowspan=16,columnspan=20)
        sb1=Scrollbar(window)
        sb1.grid(row=2,column=21,rowspan=16)
        list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=list1.yview)
        file = open('html.txt','r')
        lines = file.readlines()
        file.close()
        for line in lines:
            line = line.strip()
            list1.insert(END,line) 
        window.mainloop()
    def open5():
        window = Tk()
        window.wm_title("Brainless E-learning")
        list1=Listbox(window, height=40,width=150)
        list1.grid(row=2,column=0,rowspan=16,columnspan=20)
        sb1=Scrollbar(window)
        sb1.grid(row=2,column=21,rowspan=16)
        list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=list1.yview)
        file = open('java.txt','r')
        lines = file.readlines()
        file.close()
        for line in lines:
            line = line.strip()
            list1.insert(END,line)  
        window.mainloop()
    def open6():
        window = Tk()
        window.wm_title("Brainless E-learning")
        list1=Listbox(window, height=40,width=150)
        list1.grid(row=2,column=0,rowspan=16,columnspan=20)
        sb1=Scrollbar(window)
        sb1.grid(row=2,column=21,rowspan=16)
        list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=list1.yview)
        file = open('jquery.txt','r')
        lines = file.readlines()
        file.close()
        for line in lines:
            line = line.strip()
            list1.insert(END,line)  
        window.mainloop()
    
    def open7():
        window = Tk()
        window.wm_title("Brainless E-learning")
        list1=Listbox(window, height=40,width=150)
        list1.grid(row=2,column=0,rowspan=16,columnspan=20)
        sb1=Scrollbar(window)
        sb1.grid(row=2,column=21,rowspan=16)
        list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=list1.yview)
        file = open('jquery.txt','r')
        lines = file.readlines()
        file.close()
        for line in lines:
            line = line.strip()
            list1.insert(END,line)  
        window.mainloop()
    def open8():
        window = Tk()
        window.wm_title("Brainless E-learning")
        list1=Listbox(window, height=40,width=150)
        list1.grid(row=2,column=0,rowspan=16,columnspan=20)
        sb1=Scrollbar(window)
        sb1.grid(row=2,column=21,rowspan=16)
        list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=list1.yview)
        file = open('python.txt','r')
        lines = file.readlines()
        file.close()
        for line in lines:
            line = line.strip()
            list1.insert(END,line)  
        window.mainloop()
    def open9():
        window = Tk()
        window.wm_title("Brainless E-learning")
        list1=Listbox(window, height=40,width=150)
        list1.grid(row=2,column=0,rowspan=16,columnspan=20)
        sb1=Scrollbar(window)
        sb1.grid(row=2,column=21,rowspan=16)
        list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=list1.yview)
        file = open('php.txt','r')
        lines = file.readlines()
        file.close()
        for line in lines:
            line = line.strip()
            list1.insert(END,line)
        window.mainloop()
    def open10():
        window = Tk()
        window.wm_title("Brainless E-learning")
        list1=Listbox(window, height=40,width=150)
        list1.grid(row=2,column=0,rowspan=16,columnspan=20)
        sb1=Scrollbar(window)
        sb1.grid(row=2,column=21,rowspan=16)
        list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=list1.yview)
        file = open('sql.txt','r')
        lines = file.readlines()
        file.close()
        for line in lines:
            line = line.strip()
            list1.insert(END,line)  
        window.mainloop()
    def data():
        def c():
            open1()
        def cpp():
            open2()
        def css():
            open3()
        def html():
            open4()
        def java():
            open5()
        def jscript():
            open6()
        def jquery():
            open7()
        def python():
            open8()
        def php():
            open9()
        def sql():
            open10()
        
        window=Tk()
        window.wm_title("Brainless E-learning")
        l=Label(window,text="Welcome To Brainless Group")
        l.grid(row=0,column=0)
        l1=Label(window,text="C programming")
        l1.grid(row=3,column=0)
        b11=Button(window,text="Open",command=c)
        b11.grid(row=3,column=3)
        l1=Label(window,text="C++")
        l1.grid(row=5,column=0)
        b12=Button(window,text="Open",command=cpp)
        b12.grid(row=5,column=3)
        l1=Label(window,text="CSS")
        l1.grid(row=7,column=0)
        b13=Button(window,text="Open",command=css)
        b13.grid(row=7,column=3)
        l1=Label(window,text="HTML")
        l1.grid(row=9,column=0)
        b14=Button(window,text="Open",command=html)
        b14.grid(row=9,column=3)
        l1=Label(window,text="JAVA")
        l1.grid(row=11,column=0)
        b15=Button(window,text="Open",command=java)
        b15.grid(row=11,column=3)
        l1=Label(window,text="Java Script")
        l1.grid(row=13,column=0)
        b16=Button(window,text="Open",command=jscript)
        b16.grid(row=13,column=3)
        l1=Label(window,text="Jquery")
        l1.grid(row=15,column=0)
        b17=Button(window,text="Open",command=jquery)
        b17.grid(row=15,column=3)
        l1=Label(window,text="Python")
        l1.grid(row=17,column=0)
        b18=Button(window,text="Open",command=python)
        b18.grid(row=17,column=3)
        l1=Label(window,text="PHP")
        l1.grid(row=19,column=0)
        b19=Button(window,text="Open",command=php)
        b19.grid(row=19,column=3)
        l1=Label(window,text="SQL")
        l1.grid(row=21,column=0)
        b20=Button(window,text="Open",command=sql)
        b20.grid(row=21,column=3)
        
       
        sb1=Scrollbar(window)
        sb1.grid(row=2,column=2,rowspan=9)

        
        window.mainloop()

    def new():
        close()
        def add():
        
            log.insert(user_name_text.get(), password_text.get(),email_text.get(),mobile_text.get())
            
            main()
            
        
            
        window=Tk()
        window.wm_title("BrainLess E-learning")

        l1=Label(window,text="User Name")
        l1.grid(row=0,column=0)

        l2=Label(window,text="Password")
        l2.grid(row=0,column=2)
    
        l3=Label(window,text="Email_id")
        l3.grid(row=1,column=0)

        l4=Label(window,text="Mobile_no")
        l4.grid(row=1,column=2)

        user_name_text=StringVar()
        e1=Entry(window,textvariable=user_name_text)
        e1.grid(row=0,column=1)

        password_text=StringVar()
        e2=Entry(window,textvariable=password_text)
        e2.grid(row=0,column=3)

        email_text=StringVar()
        e3=Entry(window,textvariable=email_text)
        e3.grid(row=1,column=1)

        mobile_text=StringVar()
        e4=Entry(window,textvariable=mobile_text)
        e4.grid(row=1,column=3)

        b1=Button(window,text="Register",command=add)
        b1.grid(row=2,column=3)

        b1=Button(window,text="Login",command=main)
        b1.grid(row=2,column=1)

        window.mainloop()

    def log_in():
        for row in log.search(user_name_text.get(),password_text.get()):
                        
            if(str1 == user_name_text):
                if(password_text == str2):                
                    close()
                    data()
            
            
    window=Tk()

    window.wm_title("BrainLess E-learning")

    l1=Label(window,text="User Name")
    l1.grid(row=0,column=1)

    l2=Label(window,text="Password")
    l2.grid(row=0,column=5)

    user_name_text=StringVar()
    e1=Entry(window,textvariable=user_name_text)
    e1.grid(row=0,column=3)
    str1=StringVar()
    str1=user_name_text

    password_text=StringVar()
    e2=Entry(window,textvariable=password_text)
    e2.grid(row=0,column=8)
    str2=StringVar()
    str2=password_text

    b1=Button(window,text="Submit",command=log_in)
    b1.grid(row=5,column=3)

    b1=Button(window,text="Register New",command=new)
    b1.grid(row=5,column=8)


    window.mainloop()

main()

