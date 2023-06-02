from cProfile import label
import string
from tkinter import *
import random
import time
from tkinter import messagebox
from tkinter import filedialog
from turtle import clear; 

#Membuat Frame aplikasi
root = Tk()
root.geometry("1275x720+0+0") # menentukan ukuran window aplikasi
root.resizable(0,0)
root.title("fluffyeaaq coffee & eatery") # nama aplikasi
topFrame=Frame(root,bd=10,relief=RIDGE,bg='brown3') # frame judul
topFrame.pack(side=TOP)

labelTitle=Label(topFrame,text='fluffyeaaq coffee & eatery',font=('Berlin Sans FB',30,'bold'),fg='#d28b41',bg='#ecc7a2', bd=10,width=20) #judul aplikasi
labelTitle.grid(row=0,column=10)

root.config(bg='#bd8c5a') # warna dasar / background
# batas Frame aplikasi


# VARIABLE
# Menentukan variables
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()

# variabel menu brunch
e_pancake=StringVar()
e_croissant=StringVar()
e_waffle = StringVar()
e_cinnamonroll = StringVar()
e_burger = StringVar()

# variabel menu minuman
e_applejuice=StringVar()
e_lemontea = StringVar()
e_milktea = StringVar()
e_espresso = StringVar()
e_vanillalatte = StringVar()

# variabel menu dessert
e_onionring=StringVar()
e_frenchfries = StringVar()
e_friedicecream = StringVar()
e_cheesecake = StringVar()
e_icecream = StringVar()

# variabel Harga dalam struk
hargadaribrunchvar=StringVar()
hargadariminumanvar=StringVar()
hargadaridessertvar=StringVar()
subtotalvar=StringVar()
servicetaxvar=StringVar()
totalcostvar=StringVar()
taxvaluevar=StringVar()

e_pancake.set('0')
e_croissant.set('0')
e_waffle.set('0')
e_cinnamonroll.set('0')
e_burger.set('0')

e_applejuice.set('0')
e_lemontea.set('0')
e_milktea.set('0')
e_espresso.set('0')
e_vanillalatte.set('0')

e_onionring.set('0')
e_frenchfries.set('0')
e_friedicecream.set('0')
e_cheesecake.set('0')
e_icecream.set('0')


# FUNGSI
# Awal fungsi perhitungan harga total
tax=(10/100)
def totalcost():
    # mengglobalkan beberapa variable terlebih dahulu
    global hargadaribrunch,hargadariminuman,hargadaridessert,subtotalItems,totaltax
    if var1.get() != 0 or var2.get() != 0 or var3.get() != 0 or var4.get() != 0 or var5.get() != 0 or \
        var6.get() != 0 or var7.get() != 0 or var8.get() != 0 or var9.get() != 0 or var10.get() != 0 or\
        var11.get() != 0 or var12.get() != 0 or var13.get() != 0 or var14.get() != 0 or var15.get() != 0:

        item1=int(e_pancake.get())
        item2=int(e_croissant.get())
        item3=int(e_waffle.get())
        item4=int(e_cinnamonroll.get())
        item5=int(e_burger.get())
        
        item6=int(e_applejuice.get())
        item7=int(e_lemontea.get())
        item8 =int(e_milktea.get())
        item9=int(e_espresso.get())
        item10=int(e_vanillalatte.get())
        
        item11=int(e_onionring.get())
        item12=int(e_frenchfries.get())
        item13=int(e_friedicecream.get())
        item14=int(e_cheesecake.get())
        item15=int(e_icecream.get())
    

        hargadaribrunch=(item1*28000) + (item2*32000) + (item3*29000) + (item4*28000) + (item5*31000) 
        hargadariminuman=(item6*20000) + (item7*15000) + (item8*15000) + (item9*22000) + (item10*18000)
        hargadaridessert=(item11*18000) + (item12*25000) + (item13*25000) + (item14*28000) + (item15*16000) 

        hargadaribrunchvar.set(str(hargadaribrunch))
        hargadariminumanvar.set(str(hargadariminuman))
        hargadaridessertvar.set(str(hargadaridessert))

        subtotalItems=hargadaribrunch+hargadariminuman+hargadaridessert
        subtotalvar.set(str(subtotalItems))
       #tax=(10/100)
        taxvaluevar.set(str(tax))
        totaltax= subtotalItems*tax
        
        
        servicetaxvar.set(totaltax)
        
        totalcost=subtotalItems+totaltax
        totalcostvar.set(str(totalcost))

    else:
        messagebox.showerror('Error','Tidak ada item yang dipilih')
# Batas fungsi perhitungan harga total
last_billnumber = 00000
# awal fungsi cetak struk
def struk():
    global billnumber,date, last_billnumber 
    if hargadaribrunchvar.get() != '' or hargadaridessertvar.get() != '' or hargadariminumanvar.get() != '':
        textStruk.delete(1.0,END)
        last_billnumber += 1
        billnumber ='BILL'+str(last_billnumber)
        date=time.strftime('%d/%m/%Y')
        textStruk.insert(END,'Resep Ref:\t        '+billnumber+'\t         '+date+'\n')
        textStruk.insert(END,'******************\n')
        textStruk.insert(END,'Items:\t\t          Harga Total (Rp)\n')
        textStruk.insert(END,'******************\n')
        if e_pancake.get()!='0':
            textStruk.insert(END,f'pancake\t\t\tRp. {int(e_pancake.get())*27000}\n\n')

        if e_croissant.get()!='0':
            textStruk.insert(END,f'croissant\t\t\tRp. {int(e_croissant.get())*33000}\n\n')

        if e_waffle.get()!='0':
            textStruk.insert(END,f'waffle\t\t\tRp. {int(e_waffle.get())*25000}\n\n')

        if e_cinnamonroll.get() != '0':
            textStruk.insert(END, f'cinnamonroll:\t\t\tRp. {int(e_cinnamonroll.get()) * 22000}\n\n')

        if e_burger.get() != '0':
            textStruk.insert(END, f'burger:\t\t\tRp. {int(e_burger.get()) * 33000}\n\n')

        if e_applejuice.get() != '0':
            textStruk.insert(END, f'apple juice:\t\t\tRp. {int(e_applejuice.get()) * 20000}\n\n')

        if e_lemontea.get() != '0':
            textStruk.insert(END, f'lemon tea:\t\t\tRp. {int(e_lemontea.get()) * 15000}\n\n')

        if e_milktea.get() != '0':
            textStruk.insert(END, f'milktea:\t\t\tRp. {int(e_milktea.get()) * 15000}\n\n')

        if e_espresso.get() != '0':
            textStruk.insert(END, f'espresso:\t\t\tRp. {int(e_espresso.get()) * 22000}\n\n')

        if e_vanillalatte.get() != '0':
            textStruk.insert(END, f'vanilla latte :\t\t\tRp. {int(e_vanillalatte.get()) * 18000}\n\n')

        if e_onionring.get() != '0':
            textStruk.insert(END, f'onionring:\t\t\tRp. {int(e_onionring.get()) * 18000}\n\n')

        if e_frenchfries.get() != '0':
            textStruk.insert(END, f'frenchfries:\t\t\tRp. {int(e_frenchfries.get()) * 36000}\n\n')

        if e_friedicecream.get() != '0':
            textStruk.insert(END, f'fried ice cream:\t\t\tRp. {int(e_friedicecream.get()) * 15000}\n\n')

        if e_cheesecake.get() != '0':
            textStruk.insert(END, f'cheese cake:\t\t\tRp. {int(e_cheesecake.get()) * 1500}\n\n')

        if e_icecream.get() != '0':
            textStruk.insert(END, f'icecream:\t\t\tRp. {int(e_icecream.get()) * 16000}\n\n')

        textStruk.insert(END,'******************\n')
        if hargadaribrunchvar.get()!='Rp 0':
            textStruk.insert(END,f'Harga dari makanan\t\t\tRp. {hargadaribrunch}\n\n')
        if hargadariminumanvar.get() != 'Rp 0':
            textStruk.insert(END,f'Harga dari minuman\t\t\tRp. {hargadariminuman}\n\n')
        if hargadaridessertvar.get() != 'Rp 0':
            textStruk.insert(END,f'Harga dari jajanan\t\t\tRp. {hargadaridessert}\n\n')

        textStruk.insert(END, f'Sub Total\t\t\tRp. {subtotalItems}\n\n')
        textStruk.insert(END, f'Service Tax\t\t\tRp. {totaltax}\n\n')
        textStruk.insert(END, f'Harga total\t\t\tRP. {subtotalItems+totaltax}\n\n')
        textStruk.insert(END,'******************\n')

    else:
        messagebox.showerror('Error','Tidak ada item yang dipilih')
# batas fungsi cetak struk

# awal fungsi simpan dalam perangkat
def save():
    if textStruk.get(1.0,END)=='\n':
        pass
    else:
        # HANYA DALAM EXTENSION FILE .txt
        url=filedialog.asksaveasfile(mode='w',defaultextension='.txt') 
        if url==None:
            pass
        else:

            bill_data=textStruk.get(1.0,END)
            url.write(bill_data)
            url.close()
            messagebox.showinfo('Informasi','Struk Anda berhasil disimpan')
# Batas fungsi simpan dalam perangkat 

# awal fungsi reset
def reset():
    textStruk.delete(1.0,END)
    e_pancake.set('0')
    e_croissant.set('0')
    e_waffle.set('0')
    e_cinnamonroll.set('0')
    e_burger.set('0')
    
    e_applejuice.set('0')
    e_lemontea.set('0')
    e_milktea.set('0')
    e_espresso.set('0')
    e_vanillalatte.set('0')

    e_onionring.set('0')
    e_frenchfries.set('0')
    e_friedicecream.set('0')
    e_cheesecake.set('0')
    e_icecream.set('0')
    # batas untuk variables

    textpancake.config(state=DISABLED)
    textcroissant.config(state=DISABLED)
    textwaffle.config(state=DISABLED)
    textcinnamonroll.config(state=DISABLED)
    textburger.config(state=DISABLED)

    textapplejuice.config(state=DISABLED)
    textlemontea.config(state=DISABLED)
    textmilktea.config(state=DISABLED)
    textespresso.config(state=DISABLED)
    textvanillalatte.config(state=DISABLED)

    textonionring.config(state=DISABLED)
    textfrenchfries.config(state=DISABLED)
    textfriedicecream.config(state=DISABLED)
    textcheesecake.config(state=DISABLED)
    texticecream.config(state=DISABLED)


    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)

    hargadariminumanvar.set('')
    hargadaribrunchvar.set('')
    hargadaridessertvar.set('')
    subtotalvar.set('')
    servicetaxvar.set('')
    totalcostvar.set('')
    taxvaluevar.set('')

# batas fungsi reset

# mengaktifkan fungsi entry menu makanan
def pancake():
    if var1.get()==1:
        textpancake.config(state=NORMAL)
        textpancake.delete(0,END)
        textpancake.focus()
    else:
        textpancake.config(state=DISABLED)
        e_pancake.set('0')

def croissant():
    if var2.get()==1:
        textcroissant.config(state=NORMAL)
        textcroissant.delete(0,END)
        textcroissant.focus()
    else:
        textcroissant.config(state=DISABLED)
        e_croissant.set('0')

def waffle():
    if var3.get()==1:
        textwaffle.config(state=NORMAL)
        textwaffle.delete(0,END)
        textwaffle.focus()
    else:
        textwaffle.config(state=DISABLED)
        e_waffle.set('0')

def cinnamonroll():
    if var4.get()==1:
        textcinnamonroll.config(state=NORMAL)
        textcinnamonroll.delete(0,END)
        textcinnamonroll.focus()

    else:
        textcinnamonroll.config(state=DISABLED)
        e_cinnamonroll.set('0')

def burger ():
    if var5.get()==1:
        textburger.config(state=NORMAL)
        textburger.delete(0,END)
        textburger.focus()
    else:
        textburger.config(state=DISABLED)
        e_burger.set('0')

# batas mengaktifkan entry menu makanan

# mengaktifkan entry menu minuman
def applejuice():
    if var6.get()==1:
        textapplejuice.config(state=NORMAL)
        textapplejuice.delete(0,END)
        textapplejuice.focus()
    else:
        textapplejuice.config(state=DISABLED)
        e_applejuice.set('0')

def lemontea():
    if var7.get()==1:
        textlemontea.config(state=NORMAL)
        textlemontea.focus()
        textlemontea.delete(0, END)
    else:
        textlemontea.config(state=DISABLED)
        e_lemontea.set('0')

def milktea():
    if var8.get()==1:
        textmilktea.config(state=NORMAL)
        textmilktea.delete(0,END)
        textmilktea.focus()
    else:
        textmilktea.config(state=DISABLED)
        e_milktea.set('0')

def espresso():
    if var9.get()==1:
        textespresso.config(state=NORMAL)
        textespresso.delete(0,END)
        textespresso.focus()
    else:
        textespresso.config(state=DISABLED)
        e_espresso.set('0')

def vanillalatte():
    if var10.get()==1:
        textvanillalatte.config(state=NORMAL)
        textvanillalatte.delete(0,END)
        textvanillalatte.focus()
    else:
        textvanillalatte.config(state=DISABLED)
        e_vanillalatte.set('0')
# batas mengaktifkan entry minuman

# mengaktifkan entry menu jajanan
def onionring():
    if var11.get()==1:
        textonionring.config(state=NORMAL)
        textonionring.focus()
        textonionring.delete(0,END)
    else:
        textonionring.config(state=DISABLED)
        e_onionring.set('0')

def frenchfries():
    if var12.get()==1:
        textfrenchfries.config(state=NORMAL)
        textfrenchfries.delete(0,END)
        textfrenchfries.focus()
    else:
        textfrenchfries.config(state=DISABLED)
        e_frenchfries.set('0')

def friedicecream():
    if var13.get()==1:
        textfriedicecream.config(state=NORMAL)
        textfriedicecream.delete(0,END)
        textfriedicecream.focus()
    else:
        textfriedicecream.config(state=DISABLED)
        e_friedicecream.set('0')

def cheesecake():
    if var14.get()==1:
        textcheesecake.config(state=NORMAL)
        textcheesecake.delete(0,END)
        textcheesecake.focus()
    else:
        textcheesecake.config(state=DISABLED)
        e_cheesecake.set('0')

def icecream():
    if var15.get()==1:
        texticecream.config(state=NORMAL)
        texticecream.delete(0,END)
        texticecream.focus()
    else:
        texticecream.config(state=DISABLED)
        e_icecream.set('0')
# FRAME KIRI

# Membuat frame kiri untuk menu cafe
menuFrame=Frame(root,bd=10,relief=RIDGE,bg='black')
menuFrame.pack(side=LEFT)

hargaFrame=Frame(menuFrame,bd=9,relief=RIDGE,bg='#050206',pady=12)
hargaFrame.pack(side=BOTTOM)

brunchFrame=LabelFrame(menuFrame,text=' Brunch ',font=('Edwardian Script ITC',19,'bold'),bd=10,relief=RIDGE,fg='#2f2f2f', bg='#f6f6f6')
brunchFrame.pack(side=LEFT)

minumanFrame=LabelFrame(menuFrame,text=' Minuman ',font=('Edwardian Script ITC',19,'bold'),bd=10,relief=RIDGE,fg='#2f2f2f', bg='#f6f6f6')
minumanFrame.pack(side=LEFT)

dessertFrame=LabelFrame(menuFrame,text=' Dessert ',font=('Edwardian Script ITC',19,'bold'),bd=10,relief=RIDGE,fg='#2f2f2f', bg='#f6f6f6')
dessertFrame.pack(side=LEFT)
# batas frame kiri (menu cafe)


# membuat tampilan daftar menu makanan
pancake=Checkbutton(brunchFrame,text=' Pancake ',font=('High Tower Text',16,'bold'),onvalue=1,offvalue=0,variable=var1,
                        command=pancake, bg='#f6f6f6')
pancake.grid(row=0,column=0,sticky=W)

croissant=Checkbutton(brunchFrame,text=' Croissant ',font=('High Tower Text',16,'bold'),onvalue=1,offvalue=0,variable=var2,
                        command=croissant, bg='#f6f6f6')
croissant.grid(row=1,column=0,sticky=W)

waffle=Checkbutton(brunchFrame,text=' Waffle ',font=('High Tower Text',16,'bold'),onvalue=1,offvalue=0,variable=var3,
                        command=waffle, bg='#f6f6f6')
waffle.grid(row=2,column=0,sticky=W)

cinnamonroll=Checkbutton(brunchFrame,text=' Cinnamonroll ',font=('High Tower Text',16,'bold'),onvalue=1,offvalue=0,variable=var4,
                        command=cinnamonroll, bg='#f6f6f6')
cinnamonroll.grid(row=3,column=0,sticky=W)

burger=Checkbutton(brunchFrame,text=' Burger ',font=('High Tower Text',16,'bold'),onvalue=1,offvalue=0,variable=var5,
                        command=burger, bg='#f6f6f6')
burger.grid(row=4,column=0,sticky=W)


# menambahkan fields entri untuk item brunch
textpancake=Entry(brunchFrame,font=('High Tower Text','16','bold'),bd=7,width=8,state=DISABLED,textvar=e_pancake)
textpancake.grid(row=0,column=1)

textcroissant=Entry(brunchFrame,font=('High Tower Text','16','bold'),bd=7,width=8,state=DISABLED,textvar=e_croissant)
textcroissant.grid(row=1,column=1)

textwaffle=Entry(brunchFrame,font=('High Tower Text','16','bold'),bd=7,width=8,state=DISABLED,textvar=e_waffle)
textwaffle.grid(row=2,column=1)

textcinnamonroll=Entry(brunchFrame,font=('High Tower Text','16','bold'),bd=7,width=8,state=DISABLED,textvar=e_cinnamonroll)
textcinnamonroll.grid(row=3,column=1)

textburger=Entry(brunchFrame,font=('High Tower Text','16','bold'),bd=7,width=8,state=DISABLED,textvar=e_burger)
textburger.grid(row=4,column=1)

# membuat tampilan daftar menu minuman
applejuice=Checkbutton(minumanFrame,text='Apple Juice',font=('High Tower Text',16,'bold'),onvalue=1,offvalue=0,variable=var6,
                        command=applejuice, bg='#f6f6f6')
applejuice.grid(row=0,column=0,sticky=W)

lemontea=Checkbutton(minumanFrame,text='Lemon Tea',font=('High Tower Text',16,'bold'),onvalue=1,offvalue=0,variable=var7,
                        command=lemontea, bg='#f6f6f6')
lemontea.grid(row=1,column=0,sticky=W)

milktea=Checkbutton(minumanFrame,text='Milk Tea',font=('High Tower Text',16,'bold'),onvalue=1,offvalue=0,variable=var8,
                        command=milktea, bg='#f6f6f6')
milktea.grid(row=2,column=0,sticky=W)

espresso=Checkbutton(minumanFrame,text='Espresso',font=('High Tower Text',16,'bold'),onvalue=1,offvalue=0,variable=var9,
                        command=espresso, bg='#f6f6f6')
espresso.grid(row=3,column=0,sticky=W)

vanillalatte=Checkbutton(minumanFrame,text='Vanilla Latte',font=('High Tower Text',16,'bold'),onvalue=1,offvalue=0,variable=var10,
                        command=vanillalatte, bg='#f6f6f6')
vanillalatte.grid(row=4,column=0,sticky=W)

# menambahkan fields entri untuk item minuman
textapplejuice=Entry(minumanFrame,font=('High Tower Text','16','bold'),bd=7,width=7,state=DISABLED,textvar=e_applejuice)
textapplejuice.grid(row=0,column=1)

textlemontea=Entry(minumanFrame,font=('High Tower Text','16','bold'),bd=7,width=7,state=DISABLED,textvar=e_lemontea)
textlemontea.grid(row=1,column=1)

textmilktea=Entry(minumanFrame,font=('High Tower Text','16','bold'),bd=7,width=7,state=DISABLED,textvar=e_milktea)
textmilktea.grid(row=2,column=1)

textespresso=Entry(minumanFrame,font=('High Tower Text','16','bold'),bd=7,width=7,state=DISABLED,textvar=e_espresso)
textespresso.grid(row=3,column=1)

textvanillalatte=Entry(minumanFrame,font=('High Tower Text','16','bold'),bd=7,width=7,state=DISABLED,textvar=e_vanillalatte)
textvanillalatte.grid(row=4,column=1)

# membuat tampilan daftar menu dessert
onionring=Checkbutton(dessertFrame,text='Onion Ring',font=('High Tower Text',16,'bold'),onvalue=1,offvalue=0,variable=var11,
            command=onionring, bg='#f6f6f6')
onionring.grid(row=0,column=0,sticky=W)

frenchfries=Checkbutton(dessertFrame,text='French Fries',font=('High Tower Text',16,'bold'),onvalue=1,offvalue=0,variable=var12,
            command=frenchfries, bg='#f6f6f6')  
frenchfries.grid(row=1,column=0,sticky=W)

friedicecream=Checkbutton(dessertFrame,text='Fried Ice Cream',font=('High Tower Text',16,'bold'),onvalue=1,offvalue=0,variable=var13,
            command=friedicecream, bg='#f6f6f6')
friedicecream.grid(row=2,column=0,sticky=W)

cheesecake=Checkbutton(dessertFrame,text='Cheese Cake',font=('High Tower Text',16,'bold'),onvalue=1,offvalue=0,variable=var14,
            command=cheesecake, bg='#f6f6f6')
cheesecake.grid(row=3,column=0,sticky=W)

icecream=Checkbutton(dessertFrame,text='Ice Cream',font=('High Tower Text',16,'bold'),onvalue=1,offvalue=0,variable=var15,
            command=icecream, bg='#f6f6f6')
icecream.grid(row=4,column=0,sticky=W)


# menambahkan fields entri untuk item dessert
textonionring = Entry(dessertFrame, font=('High Tower Text','16','bold'),bd=7,width=7, state=DISABLED, textvar=e_onionring)
textonionring.grid(row=0, column=1)

textfrenchfries = Entry(dessertFrame, font=('High Tower Text','16','bold'),bd=7,width=7, state=DISABLED, textvar=e_frenchfries)
textfrenchfries.grid(row=1, column=1)

textfriedicecream = Entry(dessertFrame, font=('High Tower Text','16','bold'),bd=7,width=7, state=DISABLED, textvar=e_friedicecream)
textfriedicecream.grid(row=2, column=1)

textcheesecake = Entry(dessertFrame, font=('High Tower Text','16','bold'),bd=7,width=7, state=DISABLED, textvar=e_cheesecake)
textcheesecake.grid(row=3, column=1)

texticecream = Entry(dessertFrame, font=('High Tower Text','16','bold'),bd=7,width=7, state=DISABLED, textvar=e_icecream)
texticecream.grid(row=4, column=1)

# FRAME KANAN

# Membuat frame kanan untuk (Struk)
rightFrame=Frame(root,bd=15,relief=RIDGE)
rightFrame.pack(side=RIGHT)

strukFrame=Frame(rightFrame,bd=1,relief=RIDGE, bg='#f0f0f0')
strukFrame.pack()

buttonFrame=Frame(rightFrame,bd=3,relief=RIDGE)
buttonFrame.pack()
# Batas frame kanan (Struk)


# membuat label harga dan kolom entrinya
LabelHargadariBrunch=Label(hargaFrame,text='    HARGA DARI BRUNCH', font=('Constantia',12,'bold'),bg='#050206',fg='#fde4c3')
LabelHargadariBrunch.grid(row=0,column=0)

textHargadariBrunch=Entry(hargaFrame,font=('Calibri',14,'bold'),bd=6,width=16,state='readonly',textvariable=hargadaribrunchvar)
textHargadariBrunch.grid(row=0,column=1,padx=41)

LabelHargadariMinuman=Label(hargaFrame,text='    HARGA DARI MINUMAN', font=('Constantia',12,'bold'),bg='#050206',fg='#fde4c3')
LabelHargadariMinuman.grid(row=1,column=0)

textHargadariMinuman=Entry(hargaFrame,font=('Calibri',14,'bold'),bd=6,width=16,state='readonly',textvariable=hargadariminumanvar)
textHargadariMinuman.grid(row=1,column=1,padx=41)

LabelHargadariDessert=Label(hargaFrame,text='  HARGA DARI DESSERT', font=('Constantia',12,'bold'),bg='#050206',fg='#fde4c3')
LabelHargadariDessert.grid(row=2,column=0)

textHargadariDessert=Entry(hargaFrame,font=('Calibri',14,'bold'),bd=6,width=16,state='readonly',textvariable=hargadaridessertvar)
textHargadariDessert.grid(row=2,column=1,padx=41)

LabelSubTotal=Label(hargaFrame,text='SUB TOTAL', font=('Constantia',12,'bold'),bg='#050206',fg='#fde4c3')
LabelSubTotal.grid(row=0,column=2)

textSubTotal=Entry(hargaFrame,font=('Calibri',14,'bold'),bd=6,width=16,state='readonly',textvariable=subtotalvar)
textSubTotal.grid(row=0,column=3,padx=41)

LabelTax=Label(hargaFrame,text='Pajak'+' '+str(tax*100)+'%', font=('Constantia',12,'bold'),bg='#050206',fg='#fde4c3')
LabelTax.grid(row=1,column=2)

textTax=Entry(hargaFrame,font=('Calibri',14,'bold'),bd=6,width=16,state='readonly',textvariable=servicetaxvar)
textTax.grid(row=1,column=3,padx=41)

LabelHargaTotal=Label(hargaFrame,text='HARGA TOTAL', font=('Constantia',12,'bold'),bg='#050206',fg='#fde4c3')
LabelHargaTotal.grid(row=2,column=2)

textHargaTotal=Entry(hargaFrame,font=('Calibri',14,'bold'),bd=6,width=16,state='readonly',textvariable=totalcostvar)
textHargaTotal.grid(row=2,column=3,padx=41)


# Membuat tampilan Buttons struk (Tombol-tombol pada frame kanan)
buttonTotal= Button(buttonFrame,text='Total',font=('arial',12,'bold'),fg='#fefefe',bg='#b38b59',bd=3,padx=12,
                    command=totalcost)
buttonTotal.grid(row=0,column=0)

buttonStruk= Button(buttonFrame,text='Struk',font=('arial',12,'bold'),fg='#fefefe',bg='#b38b59',bd=3,padx=12,
                    command=struk)
buttonStruk.grid(row=0,column=1)

buttonSimpan= Button(buttonFrame,text='Simpan',font=('arial',12,'bold'),fg='#fefefe',bg='#b38b59',bd=3,padx=12,
                    command=save)
buttonSimpan.grid(row=0,column=2)

buttonReset= Button(buttonFrame,text='Reset',font=('arial',12,'bold'),fg='#fefefe',bg='red',bd=3,padx=12,
            command=reset)
buttonReset.grid(row=0,column=4)

# menentukan teks pada frame struk
textStruk=Text(strukFrame,font=('arial',12,'bold'),bd=3,width=36,height=26)
textStruk.grid(row=0,column=0)

# perulangan agar aplikasi tetap berjalan
while True:
    try:
        root.mainloop()
        break
    except UnicodeDecodeError:
        pass