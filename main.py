'''
NOTE: This Project is done by Ranukesh Raj Sah (SID: 210280)
'''


import tkinter
from tkinter import *
import tkinter.messagebox
import os
import sys
from subprocess import call
from PIL import Image, ImageTk
from PIL import ImageTk, Image
import tkinter as tk
from playsound import playsound
import mainBackEnd
from tkinter import ttk




soy=tkinter.Tk()
soy.geometry("1150x800")
soy.title("Project By Ranukesh Raj Sah(SID 210280) ")
soy.config(bg="#ccefff")
soy.resizable(False, False)



#>>>>>>>>Making a function >link>main2.py
def main6():
  frame6=Frame(soy,bg="#ccefff")
  frame6.place(width=1150,height=800,x=0,y=0)

  #>>>>>adding  image5
  img5 = tk.PhotoImage(file="image21.png")
  label5 = tk.Label(frame6, image=img5,bg="#ccefff")
  label5.pack(side="top",pady=10)
  #>>>>>adding  image6
  img6 = tk.PhotoImage(file="image22.png")
  label6 = tk.Button(frame6, image=img6,bg="#ccefff",cursor="hand2",command=click_sound)
  label6.place(x=90,y=320)
  
  img66 = tk.PhotoImage(file="image23.png")
  label66 = tk.Button(frame6, image=img66,bg="#ccefff",cursor="hand2",command=click_sound)
  label66.place(x=600,y=320)

  #>>>>>Adding a button >but1 >an image7
  img7 = tk.PhotoImage(file="image7.png")
  but7=tkinter.Button(frame6, image=img7,bg="#ccefff",command=lambda:[information()],cursor="hand2")
  but7.place(x=572,y=716)
  
  img01 = tk.PhotoImage(file="image8.png")
  label01 = tk.Button(frame6, image=img01,bg="#ccefff",command=main2,cursor="hand2")
  label01.place(x=500,y=716)
  
  
  #>>>>>>>REVIEW(error-part)
  img8 = tk.PhotoImage(file="image3.png")
  but8=tkinter.Button(frame6, image=img8,bg="#ccefff",cursor="hand2")
  but8.place(side="top", fill="none",pady=5)
  #>>>>>>>REVIEW(error-part)
 





img900= tk.PhotoImage(file="image8.png")
def information():
  frame5=Frame(soy,bg="#ccefff")
  frame5.place(width=1150,height=800,x=0,y=0)
#========================================================Variables=====================================================================
  soy.name = StringVar()
  soy.fname = StringVar()
  soy.mname = StringVar()
  soy.address = StringVar()
  soy.mobno = StringVar()
  soy.email = StringVar()
  soy.dob = StringVar()
  soy.gender = StringVar()



  #==========================================================Functions====================================================================
  def StudentRec(event):
   try: 
    global selected_tuple
    
    index = soy.listbox.curselection()[0]
    selected_tuple = soy.listbox.get(index)

    soy.Entry_name.delete(0, END)
    soy.Entry_name.insert(END, selected_tuple[1])
    soy.Entry_fname.delete(0, END)
    soy.Entry_fname.insert(END, selected_tuple[2])
    soy.Entry_mname.delete(0, END)
    soy.Entry_mname.insert(END, selected_tuple[3])
    soy.Entry_address.delete(0, END)
    soy.Entry_address.insert(END, selected_tuple[4])
    soy.Entry_mobno.delete(0, END)
    soy.Entry_mobno.insert(END, selected_tuple[5])
    soy.Entry_emailID.delete(0, END)
    soy.Entry_emailID.insert(END, selected_tuple[6])
    soy.Entry_dob.delete(0, END)
    soy.Entry_dob.insert(END, selected_tuple[7])
    soy.Entry_gender.delete(0, END)
    soy.Entry_gender.insert(END, selected_tuple[8])
   except IndexError:
    pass


  def Add():
    if(len(soy.name.get()) != 0):
      mainBackEnd.insert(soy.name.get(), soy.fname.get(), soy.mname.get(), soy.address.get(), soy.mobno.get(), soy.email.get(), soy.dob.get(),soy.gender.get()),soy.listbox.delete(0, END),soy.listbox.insert(END, (soy.name.get(), soy.fname.get(), soy.mname.get(), soy.address.get(), soy.mobno.get(), soy.email.get(), soy.dob.get(),soy.gender.get())),soy.fname.get(), soy.mname.get(), soy.address.get(), soy.mobno.get(), soy.email.get(), soy.dob.get(),soy.gender.get(), soy.listbox.delete(0, END),soy.listbox.insert(END, (soy.name.get(), soy.fname.get(), soy.mname.get(), soy.address.get(), soy.mobno.get(), soy.email.get(), soy.dob.get(),soy.gender.get()))

  def Display():
   soy.listbox.delete(0, END)
   for row in mainBackEnd.view():
    soy.listbox.insert(END, row, str(' '))


  def Exit():
    Exit = tkinter.messagebox.askyesno("Login System", "Confirm if you want to Exit")
    if Exit > 0:
      soy.destroy()
      return 
          

  def Reset():
    soy.name.set('')
    soy.fname.set('')
    soy.mname.set('')
    soy.address.set('')
    soy.mobno.set('')
    soy.email.set('')
    soy.dob.set('')
    soy.gender.set('')
    soy.listbox.delete(0, END)



  def Delete():
    if(len(soy.name.get()) != 0):
      mainBackEnd.delete(selected_tuple[0])
      Reset()
      Display()


  def Search():
    soy.listbox.delete(0, END)
    for row in mainBackEnd.search(soy.name.get(), soy.fname.get(), soy.mname.get(), soy.address.get(), soy.mobno.get(), soy.email.get(), soy.dob.get(),soy.gender.get()):
      soy.listbox.insert(END, row, str(' '))
                

  def Update():
    if(len(soy.name.get()) != 0):
      mainBackEnd.delete(selected_tuple[0])
    if(len(soy.name.get()) != 0):
      mainBackEnd.insert(soy.name.get(), soy.fname.get(), soy.mname.get(), soy.address.get(), soy.mobno.get(), soy.email.get(), soy.dob.get(),soy.gender.get())

      soy.listbox.delete(0, END)
      soy.listbox.insert(END, (soy.name.get(), soy.fname.get(), soy.mname.get(), soy.address.get(), soy.mobno.get(), soy.email.get(), soy.dob.get(), soy.gender.get()))



  #============================================================Frames=====================================================================

  soy.Main_Frame = LabelFrame(frame5, width = 1150, height = 800, font = ('arial',20,'bold'), \
                                bg = 'lightblue',bd = 5, relief = 'ridge')
  soy.Main_Frame.grid(row = 0, column = 0, padx = 49, pady = 20)

  soy.Frame_1 = LabelFrame(soy.Main_Frame, width = 600, height = 400, font = ('arial',15,'bold'), \
                            relief = 'ridge', bd = 10, bg = 'lightblue', text = 'STUDENT INFORMATION ')
  soy.Frame_1.grid(row = 1, column = 0, padx = 10)

  soy.Frame_2 = LabelFrame(soy.Main_Frame, width = 750, height = 400, font = ('arial',15,'bold'), \
                            relief = 'ridge', bd = 10, bg = 'lightblue', text = 'STUDENT DATABASE')
  soy.Frame_2.grid(row = 1, column = 1, padx = 5)                  

  soy.Frame_3 = LabelFrame(frame5, width = 1200, height = 100, font = ('arial',10,'bold'), \
                            bg = 'lightblue', relief = 'ridge', bd = 13)
  soy.Frame_3.grid(row = 2, column = 0, pady = 10)



  #========================================================Labels of Frame_1========================================================
  soy.Label_name = Label(soy.Frame_1, text = 'Name', font = ('arial',20,'bold'),  bg = 'lightblue')
  soy.Label_name.grid(row = 0, column = 0, sticky = W, padx = 20, pady = 10)
  soy.Label_fname = Label(soy.Frame_1, text = 'Father Name', font = ('arial',20,'bold'),  bg = 'lightblue')
  soy.Label_fname.grid(row = 1, column = 0, sticky = W, padx = 20)
  soy.Label_mname = Label(soy.Frame_1, text = 'Mother Name', font = ('arial',20,'bold'),  bg = 'lightblue')
  soy.Label_mname.grid(row = 2, column = 0, sticky = W, padx = 20)
  soy.Label_address = Label(soy.Frame_1, text = 'Address', font = ('arial',20,'bold'),  bg = 'lightblue')
  soy.Label_address.grid(row = 3, column = 0, sticky = W, padx = 20)
  soy.Label_mobno = Label(soy.Frame_1, text = 'Mobile Number', font = ('arial',20,'bold'),  bg = 'lightblue')
  soy.Label_mobno.grid(row = 4, column = 0, sticky = W, padx = 20)
  soy.Label_emailID = Label(soy.Frame_1, text = 'Email ID', font = ('arial',20,'bold'),  bg = 'lightblue')
  soy.Label_emailID.grid(row = 5, column = 0, sticky = W, padx = 20)
  soy.Label_dob = Label(soy.Frame_1, text = 'Date of Birth', font = ('arial',20,'bold'),  bg = 'lightblue')
  soy.Label_dob.grid(row = 6, column = 0, sticky = W, padx = 20)
  soy.Label_gender = Label(soy.Frame_1, text = 'Gender', font = ('arial',20,'bold'),  bg = 'lightblue')
  soy.Label_gender.grid(row = 7, column = 0, sticky = W, padx = 20, pady = 10)


  #========================================================Entries of Frame_1========================================================
  soy.Entry_name = Entry(soy.Frame_1, font = ('arial',17,'bold'), textvariable = soy.name)
  soy.Entry_name.grid(row = 0, column = 1, padx = 10, pady = 5)
  soy.Entry_fname = Entry(soy.Frame_1, font = ('arial',17,'bold'), textvariable = soy.fname)
  soy.Entry_fname.grid(row = 1, column = 1, padx = 10, pady = 5)
  soy.Entry_mname = Entry(soy.Frame_1, font = ('arial',17,'bold'), textvariable = soy.mname)
  soy.Entry_mname.grid(row = 2, column = 1, padx = 10, pady = 5)
  soy.Entry_address = Entry(soy.Frame_1, font = ('arial',17,'bold'), textvariable = soy.address)
  soy.Entry_address.grid(row = 3, column = 1, padx = 10, pady = 5)
  soy.Entry_mobno = Entry(soy.Frame_1, font = ('arial',17,'bold'), textvariable = soy.mobno)
  soy.Entry_mobno.grid(row = 4, column = 1, padx = 10, pady = 5)
  soy.Entry_emailID = Entry(soy.Frame_1, font = ('arial',17,'bold'), textvariable = soy.email)
  soy.Entry_emailID.grid(row = 5, column = 1, padx = 10, pady = 5)
  soy.Entry_dob = Entry(soy.Frame_1, font = ('arial',17,'bold'), textvariable = soy.dob)
  soy.Entry_dob.grid(row = 6, column = 1, padx = 10, pady = 5)
  soy.Entry_gender = ttk.Combobox(soy.Frame_1, values = (' ','Male','Female','Others'),\
                                    font = ('arial',17,'bold'), textvariable = soy.gender, width = 19)
  soy.Entry_gender.grid(row = 7, column = 1, padx = 10, pady = 5)




  #========================================================Buttons of soy.Frame_3=========================================================
  soy.btnSave = Button(soy.Frame_3, text = 'SAVE', font = ('arial',17,'bold'), width = 8, command = Add)
  soy.btnSave.grid(row = 0, column = 0, padx = 10, pady = 10)
  soy.btnDisplay = Button(soy.Frame_3, text = 'DISPLAY', font = ('arial',17,'bold'), width = 8, command = Display)
  soy.btnDisplay.grid(row = 0, column = 1, padx = 10, pady = 10)
  soy.btnReset = Button(soy.Frame_3, text = 'RESET', font = ('arial',17,'bold'), width = 8, command = Reset)
  soy.btnReset.grid(row = 0, column = 2, padx = 10, pady = 10)
  soy.btnUpdate = Button(soy.Frame_3, text = 'UPDATE', font = ('arial',17,'bold'), width = 8, command = Update)
  soy.btnUpdate.grid(row = 0, column = 3, padx = 10, pady = 10)
  soy.btnDelete = Button(soy.Frame_3, text = 'DELETE', font = ('arial',17,'bold'), width = 8, command = Delete)
  soy.btnDelete.grid(row = 0, column = 4, padx = 10, pady = 10)
  soy.btnSearch = Button(soy.Frame_3, text = 'SEARCH', font = ('arial',17,'bold'), width = 8, command = Search )
  soy.btnSearch.grid(row = 0, column = 5, padx = 10, pady = 10)
  soy.btnExit = Button(soy.Frame_3, text = 'EXIT', font = ('arial',17,'bold'), width = 8, command = Exit)
  soy.btnExit.grid(row = 0, column = 6, padx = 10, pady = 10)



  #===============================================List Box and soy.scrollbar========================================================
  soy.scrollbar = Scrollbar(soy.Frame_2)
  soy.scrollbar.grid(row = 0, column = 1, sticky = 'ns')

  soy.listbox = Listbox(soy.Frame_2, width = 75, height = 20 , font = ('arial',12,'bold'))
  soy.listbox.bind('<<ListboxSelect>>', StudentRec)
  soy.listbox.grid(row = 0, column = 0)
  soy.scrollbar.config(command = soy.listbox.yview)
  
  label900 = tk.Button(frame5, image = img900,bg="#ccefff",cursor="hand2",command=main6,font = ('arial',26,'bold'),bd=50)
  label900.place(x=500,y=716)
  
  
 
              
information()













#>>>>>>>> doing a sound effect
def click_sound():
  playsound("sound.wav")


#>>>>>>>>Making a function >link>main2.py
def main4():
  frame4=Frame(soy,bg="#ccefff")
  frame4.place(width=1150,height=800,x=0,y=0)

  #>>>>>adding  image5
  img5 = tk.PhotoImage(file="image44.png")
  label5 = tk.Label(frame4, image=img5,bg="#ccefff")
  label5.pack(side="top",pady=10)
  #>>>>>adding  image6

  label6 = tk.Button(frame4, text="Play",bg="#ccefff",cursor="hand2",command=click_sound,bd=15,font = ('arial',26,'bold'),relief=GROOVE,repeatdelay=1)
  label6.place(x=1000,y=10)
  


  #>>>>>Adding a button >but1 >an image7
  img7 = tk.PhotoImage(file="image7.png")
  but7=tkinter.Button(frame4, image=img7,bg="#ccefff",command=lambda:[information()],cursor="hand2")
  but7.place(x=572,y=716)
  
  img01 = tk.PhotoImage(file="image8.png")
  label01 = tk.Button(frame4, image=img01,bg="#ccefff",command=main2,cursor="hand2")
  label01.place(x=500,y=716)
  
  
  #>>>>>>>REVIEW(error-part)
  img8 = tk.PhotoImage(file="image3.png")
  but8=tkinter.Button(frame4, image=img8,bg="#ccefff",cursor="hand2")
  but8.place(side="top", fill="none",pady=5)
  #>>>>>>>REVIEW(error-part)
 





#>>>>>>>>Making a function >link>main2.py
def main2():
  frame2=Frame(soy,bg="#ccefff")
  frame2.place(width=1150,height=800,x=0,y=0)

  #>>>>>adding  image5
  img5 = tk.PhotoImage(file="image5.png")
  label5 = tk.Label(frame2, image=img5,bg="#ccefff")
  label5.pack(side="top",pady=10)
  #>>>>>adding  image6
  img6 = tk.PhotoImage(file="image6.png")
  label6 = tk.Label(frame2, image=img6,bg="#ccefff")
  label6.pack(side="top", fill="none",pady=13)

  #>>>>>Adding a button >but1 >an image7
  img7 = tk.PhotoImage(file="image7.png")
  but7=tkinter.Button(frame2, image=img7,bg="#ccefff",command=main4,cursor="hand2")
  but7.place(x=572,y=716)
  
  img01 = tk.PhotoImage(file="image8.png")
  label01 = tk.Button(frame2, image=img01,bg="#ccefff",command=main3,cursor="hand2")
  label01.place(x=500,y=716)
  
  
  #>>>>>>>REVIEW(error-part)
  img8 = tk.PhotoImage(file="image3.png")
  but8=tkinter.Button(frame2, image=img8,bg="#ccefff",cursor="hand2")
  but8.place(side="top", fill="none",pady=5)
  #>>>>>>>REVIEW(error-part)
  
  
  
  
  
  
  #>>>>>>>>Making a function >link>main1.py
def main3():
  frame3=Frame(soy,bg="#ccefff")
  frame3.place(width=1150,height=800,x=0,y=0)
  #>>>>>adding  image1
  im1 = tk.PhotoImage(file="image1.png")
  label21 = tk.Label(frame3, image=im1,bg="lightblue")
  label21.pack(side="top", fill="none",pady=10)

  #>>>>>adding  image2
  img22 = tk.PhotoImage(file="image2.png")
  label22 = tk.Label(frame3, image=img22,bg="lightblue")
  label22.pack(side="top", fill="none",pady=5)


  #>>>>>Adding a button >but1 >an image
  img33= tk.PhotoImage(file="image3.png")
  but33=tkinter.Button(frame3, image=img33,bg="#ccefff",command=main2,cursor="hand2")
  but33.pack(side="top", fill="none",pady=5)
  
  
  #>>>>>>>REVIEW(error-part)
  img88 = tk.PhotoImage(file="image3.png")
  but88=tkinter.Button(frame3, image=img88,bg="#ccefff",cursor="hand2")
  but88.place(side="top", fill="none",pady=5)
  #>>>>>>>REVIEW(error-part)



  
  


#>>>>> >Frame 1 >start
frame1=Frame(soy,bg="#ccefff")
frame1.place(width=1150,height=800,x=0,y=0)
#>>>>>adding  image1
img = tk.PhotoImage(file="image1.png")
label1 = tk.Label(frame1, image=img,bg="lightblue")
label1.pack(side="top", fill="none",pady=10)

#>>>>>adding  image2
img2 = tk.PhotoImage(file="image2.png")
label2 = tk.Label(frame1, image=img2,bg="lightblue")
label2.pack(side="top", fill="none",pady=5)


#>>>>>Adding a button >but1 >an image
img3 = tk.PhotoImage(file="image3.png")
but1=tkinter.Button(frame1, image=img3,bg="#ccefff",command=lambda:[main2()],cursor="hand2")
but1.pack(side="top", fill="none",pady=5)


#>>>>> >Frame 1 >end






soy.mainloop()



