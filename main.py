import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import smtplib
import re
#import mail

win = Tk()
win.configure(background='light blue')
win.geometry("1100x700+100+100")
win.title("Event Registration page")

firstname = StringVar()
lastname = StringVar()
contact = StringVar()
email = StringVar()
gender = IntVar()
Age = StringVar()
select_category = StringVar()
select_event = StringVar()
agree = IntVar()
event_ = ['Cultural', 'Sport', 'Academic']
Cultural = ['Singing Competition', 'Dancing Competition', 'Drawing Competition', 'Mehendi Competition',
            'Rangoli Competition']
Sport = ['Cricket', 'Volleyball', 'Badminton', 'Football', 'Basketball']
Academic = ['Microcontroller based quiz', 'GK quiz', 'Coding quiz']


def validateAllFields():
    fname= firstname.get()
    lname = lastname.get()
    con = contact.get()
    emailId = email.get()
    gen = gender.get()
    age = Age.get()
    category = select_category.get()
    event = select_event.get()
    if firstname.get() == "":
        messagebox.showinfo('Information', 'Please Enter firstname To Proceed')
    elif lastname.get() == "":
        messagebox.showinfo('Information', 'Please Enter lastname To Proceed')
    elif contact.get() == "":
        messagebox.showinfo('Information', 'Please Enter Contact To Proceed')
    elif len(contact.get()) != 10:
        messagebox.showinfo('Information', 'Please Enter 10 digit phone number  To Proceed')
    elif email.get() == "":
        messagebox.showinfo('Information', 'Please Enter Email To Proceed')
    elif gender.get() == 0:
        messagebox.showinfo('Information', 'Please Select Gender To Proceed')
    elif Age.get() == "":
        messagebox.showinfo('Information', 'Please Enter Age To Proceed')
    elif select_category.get() == "" :
        messagebox.showinfo('Information', 'Please Enter Event To Proceed')
    elif select_event.get() == "" :
        messagebox.showinfo('Information', 'Please Enter Event To Proceed')
    elif agree.get() == 1:
        if re.match("^[a-zA-Z0-9_+&*-]+(?:\\.[a-zA-Z0-9_+&*-]+)*@(?:[a-zA-Z0-9-]+\\.)+[a-zA-Z]{2,7}$", email.get()):
            conn=sqlite3.connect('Form.db', timeout=10)
            with conn:
                cursor=conn.cursor()
                cursor.execute(
                    'CREATE TABLE IF NOT EXISTS student_info(firstName TEXT,lastName TEXT,Contact INTEGER,email TEXT ,gender INTEGER,Age INTEGER,select_category TEXT,select_event TEXT)')
                cursor.execute(
                    'INSERT INTO student_info(firstName,lastName,Contact,email,gender,Age,select_category,select_event)'
                    'VALUES(?,?,?,?,?,?,?,?)',(fname.capitalize(),lname.capitalize(),con,emailId, gen, age, category, event))
            conn.commit()
            messagebox.showinfo('Congratulation','Registered Successfully')

            # receiver=email.get()
            # message="Subject: Registered Event Details" +'\n'+"Hello ," +'\n'+(str(fname.capitalize())+' '+str(lname.capitalize()))+'\n'+'Participated Event:'+str(category.capitalize())+'-'+str(event.capitalize())+'\n'+'Date of the Event: 28th Feb,2021'+'\n'+'Venue:Datta Meghe College of Engineering,Auditorium'+'\n'+"Thankyou"
            # s = smtplib.SMTP('smtp.gmail.com',587)
            # s.starttls()
            # s.login(mail.sender, mail.password)
            # s.sendmail(mail.sender,receiver,message)
            # s.quit()

        else:
            messagebox.showwarning('Invalid entry','Please entry a valid email')
    else:
        messagebox.showwarning('Error','Please agree the terms and conditions')


final = StringVar()
def query():
        conn = sqlite3.connect('Form.db')
        with conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM student_info')
            result = cursor.fetchall()
            final = ''
            for tup in result:
              final += str(tup)
              final += '\n'
            list1.insert(END, final)
        conn.commit()

def pick_event(e):
    if entry_category.get() == 'Cultural':
        entry_event.config(value=Cultural)
        entry_event.current()
    if entry_category.get() == 'Sport':
        entry_event.config(value=Sport)
        entry_event.current()
    if entry_category.get() == 'Academic':
        entry_event.config(value=Academic)
        entry_event.current()


def clear():
    firstname.delete(0, END)
    lastname.delete(0, END)
    contact.delete(0, END)
    email.delete(0, END)
    gender.set(0)
    Age.delete(0, END)
    select_category.set(0)
    select_event.set(0)
    agree.set(0)

def reset():
    list1.delete(1.0, END)


label_heading = Label(win, text="Registration", width=15, font=("bold", 15), bg="light blue")
label_heading.place(x=250, y=20)

label1 = Label(win, text="First name", fg='black')
label1.pack()
label1.place(x=40, y=90)

firstname = Entry(win, width=30, textvariable='firstname')
firstname.pack()
firstname.place(x=110, y=90)

label2 = Label(win, text="Last name", fg='black')
label2.pack()
label2.place(x=350, y=90)

lastname = Entry(win, width=30, textvariable='lastname')
lastname.pack()
lastname.place(x=430, y=90)

label3 = Label(win, text="Contact", fg='black')
label3.pack()
label3.place(x=40, y=170)

contact = Entry(win, width=30, textvariable='contact')
contact.pack(pady=5)
contact.place(x=110, y=170)


label4 = Label(win, text="Email", fg='black')
label4.pack(pady=5)
label4.place(x=370, y=170)

email = Entry(win, width=30, textvariable=email)
email.pack(pady=5)
email.place(x=430, y=170)

label5 = Label(win, text="Gender", fg='black')
label5.pack(pady=5)
label5.place(x=40, y=250)

male_gender = Radiobutton(win, text='Male', variable=gender, value=1)
male_gender.pack()
male_gender.place(x=100, y=250)

female_gender = Radiobutton(win, text='female', variable=gender, value=2)
female_gender.pack()
female_gender.place(x=180, y=250)

other_gender = Radiobutton(win, text='other', variable=gender, value=3)
other_gender.pack()
other_gender.place(x=260, y=250)

label6 = Label(win, text="Age", fg='black')
label6.pack(pady=5)
label6.place(x=400, y=250)

Age = Entry(win, width=30, textvariable=Age)
Age.pack(pady=5)
Age.place(x=430, y=250)

#label7 = Label(win, text="Select event - ", fg='black')
#label7.pack()
#label7.place(x=55, y=355)
#list_label7 = ['Dancing', 'Singing', 'Drama', 'Fashion Show', 'Cooking']

#drop1 = OptionMenu(win, select_event, *list_label7)
#drop1.pack()
#select_event.set("choose")
#drop1.place(x=160, y=355)


label_category = Label(win, text='Select the category of event:').place(x=20, y=400)
entry_category = ttk.Combobox(win, width=20, value=event_, textvariable=select_category)
entry_category.place(x=200, y=400)
entry_category.current()
entry_category.bind("<<ComboboxSelected>>", pick_event)
label_event = Label(win, text='Select event:').place(x=50, y=500)
entry_event = ttk.Combobox(win, width=20, value='', textvariable=select_event)
entry_event.place(x=200, y=500)
entry_event.current()


agree_button = Checkbutton(win, text='I agree with terms and conditions', variable=agree, onvalue=1, offvalue=2)
agree_button.pack()
agree_button.place(x=40, y=550)

register_button = Button(win, text='Register', width=20, fg='white', bg ='blue', command=validateAllFields)
register_button.pack(pady=5)
register_button.place(x=100, y=600)

reset_button = Button(win, text='Reset', width=20, fg='white', bg ='blue', command=clear)
reset_button.pack(pady=5)
reset_button.place(x=350, y=600)

list1 = Text(win, height=40, width=70)
list1.place(x=650, y=50)

b1 = Button(win, text='View all entries', width=20, fg='white', bg ='blue', command=query)
b1.place(x=100, y=650)

b2 = Button(win, text='clear', width=20, fg='white', bg ='blue', command=reset)
b2.place(x=350, y=650)
win.mainloop()