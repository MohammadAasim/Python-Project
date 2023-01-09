
#What is Qr Code
#A QR code is a type of matrix barcode invented in 1994
#by the Japanese automotive company Denso Wave


from tkinter import*
import qrcode
from PIL import Image, ImageTk
from resizeimage import resizeimage
class Qr_Generator:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1000x560+100+100")
        self.root.title("Fastag QR Code Generator ")
        self.root.bd=2
        self.root.resizable(False,False)
        #self.root.resizable(True,True)
        
        #mainloop()      
        # Create Details
        # variable
        self.var_Name=StringVar()
        self.var_Number=StringVar()
        self.var_company=StringVar()
        self.var_color=StringVar()
        self.var_Recharge=StringVar()
        self.var_Mobile=StringVar()

        emp_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")    
        emp_Frame.place(x=20,y=90,width=600,height=450)

        emp_title=Label(emp_Frame,text="Vehicle Details",font=("goudy old style",22),bg='#151B54',fg='white').place(x=0,y=0,relwidth=1)

        lbl_Name_code=Label(emp_Frame,text="Vehicle Owner Name:",font=("times new roman",17,'bold'),bg='white').place(x=20,y=70)
        lbl_Number_code=Label(emp_Frame,text="Vehicle Number:",font=("times new roman",17,'bold'),bg='white').place(x=20,y=110)
        lbl_company_code=Label(emp_Frame,text="Vehicle Company:",font=("times new roman",17,'bold'),bg='white').place(x=20,y=150)
        lbl_color_code=Label(emp_Frame,text="Vehicle Colour:",font=("times new roman",17,'bold'),bg='white').place(x=20,y=190)
        lbl_Recharge_code=Label(emp_Frame,text="Recharge Amount:",font=("times new roman",17,'bold'),bg='white').place(x=20,y=230)
        lbl_Mobile_code=Label(emp_Frame,text="Mobile No.:",font=("times new roman",17,'bold'),bg='white').place(x=20,y=270)

        text_Name_code=Entry(emp_Frame,font=("times new roman",16,),textvariable=self.var_Name,bg='lightyellow').place(x=270,y=70,width=300)
        text_Name_code=Entry(emp_Frame,font=("times new roman",16,),textvariable=self.var_Name,bg='lightyellow').place(x=270,y=70,width=300)
        text_Number_code=Entry(emp_Frame,font=("times new roman",16,),textvariable=self.var_Number,bg='lightyellow').place(x=270,y=110,width=300)
        text_company_code=Entry(emp_Frame,font=("times new roman",16,),textvariable=self.var_company,bg='lightyellow').place(x=270,y=150,width=300)
        text_color_code=Entry(emp_Frame,font=("times new roman",16,),textvariable=self.var_color,bg='lightyellow').place(x=270,y=190,width=300)
        text_Recharge_code=Entry(emp_Frame,font=("times new roman",16,),textvariable=self.var_Recharge,bg='lightyellow').place(x=270,y=230,width=300)
        text_Mobile_code=Entry(emp_Frame,font=("times new roman",16,),textvariable=self.var_Mobile,bg='lightyellow').place(x=270,y=270,width=300)

        btn_generate=Button(emp_Frame,text="Generate UPI QR Code",command=self.generate,font=("times new roman",15),bg="#151B54",fg='White').place(x=270,y=330,width=210,height=30)
        btn_clear=Button(emp_Frame,text="Clear",command=self.clear,font=("times new roman",15),bg="#151B54",fg='White').place(x=130,y=330,width=100,height=30)

        self.msg=''
        self.lbl_msg=Label(emp_Frame,text=self.msg,font=("times new roman",20,'bold'),bg='white',fg='green')
        self.lbl_msg.place(x=0,y=370,relwidth=1)

        qr_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")    
        qr_Frame.place(x=640,y=90,width=335,height=450)
        emp_title=Label(qr_Frame,text="UPI QR Code",font=("goudy old style",22),bg='#151B54',fg='white').place(x=0,y=0,relwidth=1)
        self.qr_code=Label(qr_Frame,text="UPI QR Code \nNot Generate",font=("times new roman",15),bg='#151B54',fg='white',bd=1,relief=RIDGE)
        self.qr_code.place(x=40,y=120,height=250,width=250)
    
    def clear(self):
        self.var_Name.set('')
        self.var_Number.set('')
        self.var_company.set('')
        self.var_color.set('')
        self.var_Recharge.set('')
        self.var_Mobile.set('')
        self.msg=''
        self.lbl_msg.config(text=self.msg)
        self.qr_code.config(image='')
    def generate(self):
        if self.var_Name.get()=='' or self.var_Number.get()==''or self.var_company.get()==''or self.var_color.get()==''or self.var_Recharge.get()==''or self.var_Mobile.get()=='':
            self.msg='All Fields are Required !!!'
            self.lbl_msg.config(text=self.msg,fg='red')
        else:
            qr_data=(f'Vehicle Owner Name:{self.var_Name.get()}\nVehicle Number:{self.var_Number.get()}\nVehicle Company:{self.var_company.get()}\nVehicle Colour:{ self.var_color.get()}\nRecharge Amount:{self.var_Recharge.get()}\nMobile No.:{self.var_Mobile.get()}')
            qr_code=qrcode.make(qr_data)
            #print(qr_code)
            qr_code=resizeimage.resize_cover(qr_code,[230,230])
            qr_code.save("Project/emp_"+str(self.var_Name.get())+'.png')
            #qr code image update
            self.im=ImageTk.PhotoImage(file="Project/emp_"+str(self.var_Name.get())+'.png')
            self.qr_code.config(image=self.im)
            #update
            self.msg='Successfully Generate UPI QR Code !!!'
            self.lbl_msg.config(text=self.msg,fg='green')


        
root=Tk()
obj=Qr_Generator(root)
canvas = Canvas(root, width = 1000, height =80)      
canvas.pack()
img = ImageTk.PhotoImage(Image.open("fastag.png"))      
#img = PhotoImage(file="fastag.png")      
canvas.create_image(45,-17, anchor=NW, image=img)
root.mainloop()
