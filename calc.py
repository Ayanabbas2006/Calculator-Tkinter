import tkinter as tk
root=tk.Tk()
root.geometry('375x500')
root.resizable(True,True)
main_fr=tk.Frame(root,bd=5,relief='sunken')
main_fr.grid(row=0,column=0,sticky='nsew')
root.title('Calculator')
logo=tk.PhotoImage(file='calc.png')
root.iconphoto(True,logo)
result=tk.StringVar()
res=tk.Entry(main_fr,textvariable=result,font=('bold',24),fg='white',bg='black',justify='right')
res.grid(row=0,column=0,rowspan=2,columnspan=4,sticky='nsew')
res.focus_set()
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

for i in range(4):
    main_fr.columnconfigure(i, weight=1)
for j in range(7):
    main_fr.rowconfigure(j, weight=1)

def normal_color(*args):
	if res.cget('fg')!='red' or res.get()=='':
		res.config(fg='white')

def clear():
	global result
	result.set('')
	res.config(fg='white')

def erase(*args):
	global result
	s=result.get()
	l=list(s)
	l.pop(-1)
	g=''.join(l)
	result.set(g)
def solve(*args):
	global result
	s=result.get()
	d=s.replace('x','*')
	try:
		r=eval(d)
		res.config(fg='green')
		result.set(r)
	except Exception:
		res.config(fg='red')
		result.set('Error')
def set(st):
	global result
	res.config(fg='white')
	s=result.get()
	s+=st
	result.set(s)


res.bind('<Return>',solve)
res.bind('<KeyPress>',normal_color)


b13=tk.Button(main_fr,text='AC',font=('bold',18),fg='white',bg='red',relief='raised',command=lambda: clear())
b13.grid(row=2,column=0,sticky='nsew')
b14=tk.Button(main_fr,text='(',font=('bold',18),fg='white',bg='black',relief='raised',command=lambda: set('('))
b14.grid(row=2,column=1,sticky='nsew')
b15=tk.Button(main_fr,text=')',font=('bold',18),fg='white',bg='black',relief='raised',command=lambda: set(')'))
b15.grid(row=2,column=2,sticky='nsew')
b16=tk.Button(main_fr,text='/',font=('bold',18),fg='white',bg='black',relief='raised',command=lambda: set('/'))
b16.grid(row=2,column=3,sticky='nsew')

b9=tk.Button(main_fr,text='7',font=('bold',18),fg='white',bg='black',relief='raised',command=lambda: set('7'))
b9.grid(row=3,column=0,sticky='nsew')
b10=tk.Button(main_fr,text='8',font=('bold',18),fg='white',bg='black',relief='raised',command=lambda: set('8'))
b10.grid(row=3,column=1,sticky='nsew')
b11=tk.Button(main_fr,text='9',font=('bold',18),fg='white',bg='black',relief='raised',command=lambda: set('9'))
b11.grid(row=3,column=2,sticky='nsew')
b12=tk.Button(main_fr,text='x',font=('bold',18),fg='white',bg='black',relief='raised',command=lambda: set('x'))
b12.grid(row=3,column=3,sticky='nsew')

b5=tk.Button(main_fr,text='4',font=('bold',18),fg='white',bg='black',relief='raised',command=lambda: set('4'))
b5.grid(row=4,column=0,sticky='nsew')
b6=tk.Button(main_fr,text='5',font=('bold',18),fg='white',bg='black',relief='raised',command=lambda: set('5'))
b6.grid(row=4,column=1,sticky='nsew')
b7=tk.Button(main_fr,text='6',font=('bold',18),fg='white',bg='black',relief='raised',command=lambda: set('6'))
b7.grid(row=4,column=2,sticky='nsew')
b8=tk.Button(main_fr,text='-',font=('bold',18),fg='white',bg='black',relief='raised',command=lambda: set('-'))
b8.grid(row=4,column=3,sticky='nsew')

b1=tk.Button(main_fr,text='1',font=('bold',18),fg='white',bg='black',relief='raised',command=lambda: set('1'))
b1.grid(row=5,column=0,sticky='nsew')
b2=tk.Button(main_fr,text='2',font=('bold',18),fg='white',bg='black',relief='raised',command=lambda: set('2'))
b2.grid(row=5,column=1,sticky='nsew')
b3=tk.Button(main_fr,text='3',font=('bold',18),fg='white',bg='black',relief='raised',command=lambda: set('3'))
b3.grid(row=5,column=2,sticky='nsew')
b4=tk.Button(main_fr,text='+',font=('bold',18),fg='white',bg='black',relief='raised',command=lambda: set('+'))
b4.grid(row=5,column=3,sticky='nsew')


bk=tk.Button(main_fr,text='C',font=('bold',18),fg='red',bg='black',relief='raised',command=lambda: erase())
bk.grid(row=6,column=0,sticky='nsew')
b0=tk.Button(main_fr,text='0',font=('bold',18),fg='white',bg='black',relief='raised',command=lambda: set('0'))
b0.grid(row=6,column=1,sticky='nsew')
b_=tk.Button(main_fr,text='.',font=('bold',18),fg='white',bg='black',relief='raised',command=lambda: set('.'))
b_.grid(row=6,column=2,sticky='nsew')
be=tk.Button(main_fr,text='=',font=('bold',18),fg='white',bg='green',relief='raised',command=lambda: solve())
be.grid(row=6,column=3,sticky='nsew')

root.mainloop()
