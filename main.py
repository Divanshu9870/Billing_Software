from cgitb import text
from multiprocessing.sharedctypes import Value
from tkinter import*
from tkinter import ttk
from turtle import right, title, width
from PIL import Image,ImageTk
from tkinter import messagebox
import random,os
import tempfile
from time import strftime

from click import command

class Billing_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x710+0+0")
        self.root.title("Billing software")

        #=======varaibles=====
        self.c_name=StringVar()
        self.c_phon=StringVar()
        self.bill_no=StringVar()
        z=random.randint(1000,9999)
        self.bill_no.set(z)
        self.c_email=StringVar()
        self.search_bill=StringVar()
        self.product=StringVar()
        self.prices=IntVar()
        self.qty=IntVar()
        self.sub_total=StringVar()
        self.tax_input=StringVar()
        self.total=StringVar()

        #product Categories list
        self.category=["Select Category","Clothing","Lifestyle","Grocery"]
        self.SubCatClothing=["Jeans","Shirt","T-Shirt"]
        self.Jeans=["Levis","Lee","Mufti","Spykar"]
        self.price_levis=5000
        self.price_lee=4000
        self.price_mufti=6000
        self.price_spykar=5500

        self.Shirt=["Peter England","Allen Solly","louis Phillipe"]
        self.price_peter=1500
        self.price_solly=1000
        self.price_louis=2000

        self.T_shirt=["Polo","Roadster","Jack&Jones"]
        self.price_polo=700
        self.price_roadster=1000
        self.price_jack=1500


        self.SubCatLifStyle=["Bath Soap","Shampoo","Hair Oil","Deodorant"]
        self.Bath_soap=["Lux","Dove","Dettol","Pearl"]
        self.price_lux=20
        self.price_dove=40
        self.price_dettol=30
        self.price_pearl=50

        self.Shampoo=["Head&Shoulder","Pantene","Tresmme"]
        self.price_head=450
        self.price_pantene=400
        self.price_tresmme=600

        self.Hair_oil=["Kesh King","Navratna","Hair&Care"]
        self.price_king=100
        self.price_nav=80
        self.price_hair=150

        self.deodorant=["Wild Stone","Fogg","Axe"]
        self.price_wildstone=250
        self.price_fogg=200
        self.price_axe=200





        self.SubCatGrocery=["Noodles","biscuit","Tea","Sauces"]
        self.noodles=["Maggies","yippee","Wai Wai"]
        self.price_maggie=15
        self.price_yippee=12
        self.price_wai=10

        self.biscuit=["Parle-G","Barbourn","Oreo","HideNseek"]
        self.price_parle=10
        self.price_barbourn=20
        self.price_oreo=25
        self.price_hide=30

        self.tea=["Red Label","Tata Agni","Tata Premium","Lipton"]
        self.price_red=400
        self.price_agni=350
        self.price_premium=450
        self.price_lipton=420

        self.sauce=["Tomato Sauce","Green Chilly Sauce","Soya Sauce"]
        self.price_tomato=200
        self.price_chilly=150
        self.price_soya=100
        




        
        img=Image.open(r"F:\billing software\images\img2.jpg")
        img=img.resize((480,150),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=480,height=150)

        img1=Image.open(r"F:\billing software\images\img1.jpg")
        img1=img1.resize((480,150),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=480,y=0,width=480,height=150)

        img2=Image.open(r"F:\billing software\images\img3.jpg")
        img2=img2.resize((480,150),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=960,y=0,width=480,height=150)

       

        title_lbl=Label(self.root,text="Billing Software System ", font=("times new roman",35,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=150,width=1530,height=45)

        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000, time)

        lbl= Label(title_lbl,font=('times new roman',20,'bold'),background='black',foreground='white')
        lbl.place(x=15,y=(-6),width=150,height=50)
        time()

        main_frame=Frame(self.root,bd=5,bg="white",relief=GROOVE)
        main_frame.place(x=0,y=195,width=1450,height=600)

        #customer Label Frame
        customer_frame=LabelFrame(main_frame,bd=3,bg="white",relief=RIDGE,text="Customer",font=("times new roman",14,"bold"),fg="red")
        customer_frame.place(x=5,y=1,width=350,height=150)

        self.lbl_mob=Label(customer_frame,text="Mobile no:",font=("times new roman",12,"bold"),bg="white")
        self.lbl_mob.grid(row=0,column=0,padx=5,sticky=W)
        self.entry_mob=ttk.Entry(customer_frame,textvariable=self.c_phon,font=("times new roman",12,"bold"),width=24)
        self.entry_mob.grid(row=0,column=1,padx=5,pady=5,sticky=W)

        self.cust_name=Label(customer_frame,text="Customer Name:",font=("times new roman",12,"bold"),bg="white")
        self.cust_name.grid(row=1,column=0,padx=5,sticky=W)
        self.entry_name=ttk.Entry(customer_frame,textvariable=self.c_name,font=("times new roman",12,"bold"),width=24)
        self.entry_name.grid(row=1,column=1,padx=5,pady=5,sticky=W)

        self.lbl_email=Label(customer_frame,text="Email:",font=("times new roman",12,"bold"),bg="white")
        self.lbl_email.grid(row=2,column=0,padx=5,sticky=W)
        self.entry_email=ttk.Entry(customer_frame,textvariable=self.c_email,font=("times new roman",12,"bold"),width=24)
        self.entry_email.grid(row=2,column=1,padx=5,pady=5,sticky=W)

        #product
        product_frame=LabelFrame(main_frame,bd=3,bg="white",relief=RIDGE,text="Product",font=("times new roman",14,"bold"),fg="red")
        product_frame.place(x=360,y=1,width=500,height=150)

        self.lbl_category=Label(product_frame,text="Select Categories:",font=("times new roman",12,"bold"),bg="white")
        self.lbl_category.grid(row=0,column=0,padx=5,sticky=W)
        self.combo_category=ttk.Combobox(product_frame,value=self.category,width=15,font=("times new roman",12,"bold"),state="read only")
        #semester_combo["values"]=("select Semester","Ist","2nd","3rd","4th","5th","6th","7th","8th")
        self.combo_category.current(0)
        self.combo_category.grid(row=0,column=1,padx=2,pady=5,sticky=W)
        self.combo_category.bind("<<ComboboxSelected>>",self.Categories)
        
        #sub category
        self.lbl_subcategory=Label(product_frame,text="Sub Category:",font=("times new roman",12,"bold"),bg="white")
        self.lbl_subcategory.grid(row=1,column=0,padx=5,sticky=W)
        self.combo_subcategory=ttk.Combobox(product_frame,value=[" "],width=15,font=("times new roman",12,"bold"),state="read only")
        self.combo_subcategory.grid(row=1,column=1,padx=2,pady=5,sticky=W)
        self.combo_subcategory.bind("<<ComboboxSelected>>",self.Product_add)

        #product name
        self.lblproduct=Label(product_frame,text="Product:",font=("times new roman",12,"bold"),bg="white")
        self.lblproduct.grid(row=3,column=0,padx=5,sticky=W)
        self.combo_product=ttk.Combobox(product_frame,textvariable=self.product,width=15,font=("times new roman",12,"bold"),state="read only")
        #semester_combo["values"]=("select Semester","Ist","2nd","3rd","4th","5th","6th","7th","8th")
        #semester_combo.current(0)
        self.combo_product.grid(row=3,column=1,padx=2,pady=5,sticky=W)
        self.combo_product.bind("<<ComboboxSelected>>",self.Price)

        self.lblprice=Label(product_frame,text="Price:",font=("times new roman",12,"bold"),bg="white")
        self.lblprice.grid(row=0,column=2,padx=5,sticky=W)
        self.combo_price=ttk.Combobox(product_frame,width=15,textvariable=self.prices,font=("times new roman",12,"bold"),state="read only")
        #semester_combo["values"]=("select Semester","Ist","2nd","3rd","4th","5th","6th","7th","8th")
        #semester_combo.current(0)
        self.combo_price.grid(row=0,column=3,padx=2,pady=5,sticky=W)


        self.lblQty=Label(product_frame,text="Qty:",font=("times new roman",12,"bold"),bg="white")
        self.lblQty.grid(row=1,column=2,padx=5,sticky=W)
        self_combo_qty=ttk.Combobox(product_frame,textvariable=self.qty,width=15,font=("times new roman",12,"bold"),state="read only")
        self_combo_qty.grid(row=1,column=3,padx=2,pady=5,sticky=W)

        #middle Frame
        MiddleFrame=Frame(self.root,bd=10)
        MiddleFrame.place(x=6,y=357,width=860,height=205)

        img3=Image.open(r"F:\billing software\images\img1.jpg")
        img3=img3.resize((427,220),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        f_lbl=Label(MiddleFrame,image=self.photoimg3)
        f_lbl.place(x=0,y=0,width=427,height=220)

        img4=Image.open(r"F:\billing software\images\img2.jpg")
        img4=img4.resize((427,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        f_lbl=Label(MiddleFrame,image=self.photoimg4)
        f_lbl.place(x=425,y=0,width=427,height=220)

        #search frame
        Search_Frame=Frame(main_frame,bd=2,bg="white")
        Search_Frame.place(x=890,y=10,width=400,height=40)
        self.lblBill=Label(Search_Frame,text="Bill number",font=("times new roman",12,"bold"),fg="white",bg="red")
        self.lblBill.grid(row=0,column=0,sticky=W,padx=1)

        self.txt_Entry_Search=ttk.Entry(Search_Frame,textvariable=self.search_bill,font=("times new roman",12,"bold"),width=20)
        self.txt_Entry_Search.grid(row=0,column=1,padx=2,pady=2,sticky=W)

        self.BtnSearch=Button(Search_Frame,command=self.find_bill,text="Search",width=10,font=("times new roman",10,"bold"),bg="orangered",fg="white",cursor="hand2")
        self.BtnSearch.grid(row=0,column=2)


        #right bill frame

        rightlabel_frame=LabelFrame(main_frame,bd=3,bg="white",relief=RIDGE,text="Bill Area",font=("times new roman",14,"bold"),fg="red")
        rightlabel_frame.place(x=865,y=40,width=480,height=320)

        scroll_y=ttk.Scrollbar(rightlabel_frame,orient=VERTICAL)
        self.textarea=Text(rightlabel_frame,yscrollcommand=scroll_y.set,bg="white",fg="blue",font=("times new roman",12,"bold"))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        #bill counter label frame
        Bottomlabel_frame=LabelFrame(main_frame,bd=3,bg="white",relief=RIDGE,text="Product",font=("times new roman",14,"bold"),fg="red")
        Bottomlabel_frame.place(x=0,y=360,width=1350,height=135)

        self.lblSubTotal=Label(Bottomlabel_frame,text=" Sub Total:",font=("times new roman",12,"bold"),bg="white")
        self.lblSubTotal.grid(row=0,column=0,padx=5,sticky=W)
        self.entrySubTotal=ttk.Entry(Bottomlabel_frame,textvariable=self.sub_total,font=("times new roman",12,"bold"),width=20)
        self.entrySubTotal.grid(row=0,column=1,padx=5,pady=5,sticky=W)


        self.lbl_Tax=Label(Bottomlabel_frame,text="Total:",font=("times new roman",12,"bold"),bg="white")
        self.lbl_Tax.grid(row=2,column=0,padx=5,sticky=W)
        self.txt_tax=ttk.Entry(Bottomlabel_frame,textvariable=self.total,font=("times new roman",12,"bold"),width=20)
        self.txt_tax.grid(row=2,column=1,padx=5,pady=5,sticky=W)

        self.lblAmountTotal=Label(Bottomlabel_frame,text="Gov Tax:",font=("times new roman",12,"bold"),bg="white")
        self.lblAmountTotal.grid(row=1,column=0,padx=5,sticky=W)
        self.textAmountTotal=ttk.Entry(Bottomlabel_frame,textvariable=self.tax_input,font=("times new roman",12,"bold"),width=20)
        self.textAmountTotal.grid(row=1,column=1,padx=5,pady=5,sticky=W)

        #button frame
        btn_frame=Frame(Bottomlabel_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=320,y=0)

        self.BtnAddToCart=Button( btn_frame,command=self.AddItem,text="Add To Cart",height=2,width=13,font=("times new roman",15,"bold"),bg="orangered",fg="white",cursor="hand2")
        self.BtnAddToCart.grid(row=0,column=0)

        self.Btngenerate_Bill=Button( btn_frame,command=self.gen_bill,text="Generate Bill",height=2,width=13,font=("times new roman",15,"bold"),bg="orangered",fg="white",cursor="hand2")
        self.Btngenerate_Bill.grid(row=0,column=1)

        self.BtnSave=Button( btn_frame,text="Save Bill",command=self.save_bill,height=2,width=13,font=("times new roman",15,"bold"),bg="orangered",fg="white",cursor="hand2")
        self.BtnSave.grid(row=0,column=2)

        self.BtnPrint=Button( btn_frame,command=self.iprint, text="Print",height=2,width=13,font=("times new roman",15,"bold"),bg="orangered",fg="white",cursor="hand2")
        self.BtnPrint.grid(row=0,column=3)

        self.BtnClear=Button( btn_frame,command=self.clear,text="Clear",height=2,width=13,font=("times new roman",15,"bold"),bg="orangered",fg="white",cursor="hand2")
        self.BtnClear.grid(row=0,column=4)

        self.BtnExit=Button( btn_frame,command=self.root.destroy,text="Exit",height=2,width=13,font=("times new roman",15,"bold"),bg="orangered",fg="white",cursor="hand2")
        self.BtnExit.grid(row=0,column=5)
        self.welcome()

        self.l=[]
    #==========function declaration
    def AddItem(self):
        Tax=1
        self.n=self.prices.get()
        self.m=self.qty.get()*self.n
        self.l.append(self.m)
        if self.product.get()=="":
            messagebox.showerror("Error","Please select the Product")
        else:
            self.textarea.insert(END,f"\n  {self.product.get()}\t\t{self.qty.get()}\t\t{self.m}")
            self.sub_total.set(str('Rs.%.2f'%(sum(self.l))))
            self.tax_input.set(str('Rs.%.2f'%((((sum(self.l)) - (self.prices.get()))*Tax)/100)))
           
            self.total.set(str('Rs.%.2f'%(((sum(self.l)) + ((((sum(self.l)) - (self.prices.get()))*Tax)/100)))))

    def gen_bill(self):
        if self.product.get()=="":
            messagebox.showerror("Error","Please Add to Cart")
        else:
            text=self.textarea.get(10.0,(10.0+float(len(self.l))))
            self.welcome()
            self.textarea.insert(END,text)
            self.textarea.insert(END,f"\n  ============================================")
            self.textarea.insert(END,f"\n Sub Amount:\t\t\t{self.sub_total.get()}")
            self.textarea.insert(END,f"\n Tax Amount:\t\t\t{self.tax_input.get()}")
            self.textarea.insert(END,f"\n Total Amount:\t\t\t{self.total.get()}")
            self.textarea.insert(END,f"\n============================================")

    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do You Want to save the bill")
        if op>0:
            self.bill_data=self.textarea.get(1.0,END)
            f1=open('bills/'+str(self.bill_no.get())+".txt",'w')
            f1.write(self.bill_data)
            op=messagebox.showinfo("saved",f"Bill No:{self.bill_no.get()} Saved successfully")
            f1.close()

    def iprint(self):
        q=self.textarea.get(1.0,"end-1c")
        filename=tempfile.mktemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename,"print")

    def find_bill(self):
        found="no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f'bills/{i}','r')
                self.textarea.delete(1.0,END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                found="yes"
        if found=='no':
            messagebox.showerror("Error","Invalid Bill")

    def clear(self):
        self.textarea.delete(1.0,END)
        self.c_name.set("")
        self.c_phon.set("")
        self.c_email.set("")
        z=random.randint(1000,9999)
        self.bill_no.set(str(z))
        self.search_bill.set("")
        self.product.set("")
        self.prices.set(0)
        self.qty.set(0)
        self.l=[0]
        self.sub_total.set("")
        self.tax_input.set("")
        self.total.set("")
        self.welcome()





    def welcome(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,"\t Welcome to dev Mini Mall")
        self.textarea.insert(END,f"\n Bill Number:{self.bill_no.get()}")
        self.textarea.insert(END,f"\n Customer Name:{self.c_name.get()}")
        self.textarea.insert(END,f"\n Phone Number:{self.c_phon.get()}")
        self.textarea.insert(END,f"\n Customer Email:{self.c_email.get()}")

        self.textarea.insert(END,f"\n ================================================")
        self.textarea.insert(END,f"\n Products\t\t\tQTY\t\tPrice")
        self.textarea.insert(END,f"\n ================================================\n")










    
    def Categories(self,event=""):
        if self.combo_category.get()=="Clothing":
            self.combo_subcategory.config(value=self.SubCatClothing)
            self.combo_subcategory.current(0)

        if self.combo_category.get()=="Lifestyle":
            self.combo_subcategory.config(value=self.SubCatLifStyle)
            self.combo_subcategory.current(0)

        if self.combo_category.get()=="Grocery":
            self.combo_subcategory.config(value=self.SubCatGrocery)
            self.combo_subcategory.current(0)
    
    def Product_add(self,event=""):
        if self.combo_subcategory.get()=="Jeans":
            self.combo_product.config(value=self.Jeans)
            self.combo_product.current(0)

        if self.combo_subcategory.get()=="Shirt":
            self.combo_product.config(value=self.Shirt)
            self.combo_product.current(0)

        if self.combo_subcategory.get()=="T-Shirt":
            self.combo_product.config(value=self.T_shirt)
            self.combo_product.current(0)

        
        if self.combo_subcategory.get()=="Bath Soap":
            self.combo_product.config(value=self.Bath_soap)
            self.combo_product.current(0)

        if self.combo_subcategory.get()=="Shampoo":
            self.combo_product.config(value=self.Shampoo)
            self.combo_product.current(0)

        if self.combo_subcategory.get()=="Hair Oil":
            self.combo_product.config(value=self.Hair_oil)
            self.combo_product.current(0)
        
        if self.combo_subcategory.get()=="Deodorant":
            self.combo_product.config(value=self.deodorant)
            self.combo_product.current(0)

        #grocery
        if self.combo_subcategory.get()=="Noodles":
            self.combo_product.config(value=self.noodles)
            self.combo_product.current(0)

        if self.combo_subcategory.get()=="biscuit":
            self.combo_product.config(value=self.biscuit)
            self.combo_product.current(0)
        
        if self.combo_subcategory.get()=="Tea":
            self.combo_product.config(value=self.tea)
            self.combo_product.current(0)
        
        if self.combo_subcategory.get()=="Sauces":
            self.combo_product.config(value=self.sauce)
            self.combo_product.current(0)

    def Price(self,event=""):
        if self.combo_product.get()=="Levis":
            self.combo_price.config(value=self.price_levis)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_product.get()=="Lee":
            self.combo_price.config(value=self.price_lee)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_product.get()=="Mufti":
            self.combo_price.config(value=self.price_mufti)
            self.combo_price.current(0)
            self.qty.set(1)
        
        if self.combo_product.get()=="Spykar":
            self.combo_price.config(value=self.price_spykar)
            self.combo_price.current(0)
            self.qty.set(1)

        #Shirts
        if self.combo_product.get()=="Peter England":
            self.combo_price.config(value=self.price_peter)
            self.combo_price.current(0)
            self.qty.set(1)
        
        if self.combo_product.get()=="louis Phillipe":
            self.combo_price.config(value=self.price_louis)
            self.combo_price.current(0)
            self.qty.set(1)

        #T-shirts
        if self.combo_product.get()=="Polo":
            self.combo_price.config(value=self.price_polo)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_product.get()=="Roadster":
            self.combo_price.config(value=self.price_roadster)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_product.get()=="Jack&Jones":
            self.combo_price.config(value=self.price_jack)
            self.combo_price.current(0)
            self.qty.set(1)
        #bath soap
        if self.combo_product.get()=="Lux":
            self.combo_price.config(value=self.price_lux)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_product.get()=="Dove":
            self.combo_price.config(value=self.price_dove)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_product.get()=="Dettol":
            self.combo_price.config(value=self.price_dettol)
            self.combo_price.current(0)
            self.qty.set(1)
        
        if self.combo_product.get()=="Pearl":
            self.combo_price.config(value=self.price_pearl)
            self.combo_price.current(0)
            self.qty.set(1)
        #Shampoo
        if self.combo_product.get()=="Head&Shoulder":
            self.combo_price.config(value=self.price_head)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_product.get()=="Pantene":
            self.combo_price.config(value=self.price_pantene)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_product.get()=="Tresmme":
            self.combo_price.config(value=self.price_tresmme)
            self.combo_price.current(0)
            self.qty.set(1)

        #hair oil
        if self.combo_product.get()=="Kesh King":
            self.combo_price.config(value=self.price_king)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_product.get()=="Navratna":
            self.combo_price.config(value=self.price_nav)
            self.combo_price.current(0)
            self.qty.set(1)
        
        if self.combo_product.get()=="Hair&Care":
            self.combo_price.config(value=self.price_head)
            self.combo_price.current(0)
            self.qty.set(1)

        #deo
        if self.combo_product.get()=="Wild Stone":
            self.combo_price.config(value=self.price_wildstone)
            self.combo_price.current(0)
            self.qty.set(1)
        
        if self.combo_product.get()=="Fogg":
            self.combo_price.config(value=self.price_fogg)
            self.combo_price.current(0)
            self.qty.set(1)
        
        if self.combo_product.get()=="Axe":
            self.combo_price.config(value=self.price_axe)
            self.combo_price.current(0)
            self.qty.set(1)

        #noodles
        if self.combo_product.get()=="Maggies":
            self.combo_price.config(value=self.price_maggie)
            self.combo_price.current(0)
            self.qty.set(1)
        
        if self.combo_product.get()=="yippee":
            self.combo_price.config(value=self.price_yippee)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_product.get()=="Wai Wai":
            self.combo_price.config(value=self.price_wai)
            self.combo_price.current(0)
            self.qty.set(1)

        #biscuit
        if self.combo_product.get()=="Parle-G":
            self.combo_price.config(value=self.price_parle)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_product.get()=="Barbourn":
            self.combo_price.config(value=self.price_barbourn)
            self.combo_price.current(0)
            self.qty.set(1)
        
        if self.combo_product.get()=="Oreo":
            self.combo_price.config(value=self.price_oreo)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_product.get()=="HideNseek":
            self.combo_price.config(value=self.price_hide)
            self.combo_price.current(0)
            self.qty.set(1)

        #tea
        if self.combo_product.get()=="Red Label":
            self.combo_price.config(value=self.price_red)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_product.get()=="Tata Agni":
            self.combo_price.config(value=self.price_agni)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_product.get()=="Tata Premium":
            self.combo_price.config(value=self.price_premium)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_product.get()=="Lipton":
            self.combo_price.config(value=self.price_lipton)
            self.combo_price.current(0)
            self.qty.set(1)

        #sauces

        if self.combo_product.get()=="Tomato Sauce":
            self.combo_price.config(value=self.price_tomato)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_product.get()=="Green Chilly Sauce":
            self.combo_price.config(value=self.price_chilly)
            self.combo_price.current(0)
            self.qty.set(1)

        if self.combo_product.get()=="Soya Sauce":
            self.combo_price.config(value=self.price_head)
            self.combo_price.current(0)
            self.qty.set(1)
        
        
        









if __name__=="__main__":

    root=Tk()
    obj=Billing_App(root)
    root.mainloop()