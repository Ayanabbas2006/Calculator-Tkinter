import tkinter as tk
root=tk.Tk()
root.geometry('375x500')
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
def button(text='(',font=('bold',18),fg='white',bg='black',relief='raised',command=None,row=2,column=1,sticky='nsew'):
	b=tk.Button(master=main_fr,text=text,font=font,fg=fg,bg=bg,relief=relief,command=command)
	b.grid(row=row,column=column,sticky=sticky)
lis=[['','(',')','/'],['7','8','9','x'],['4','5','6','-'],['1','2','3','+'],['','0','.','']]
row=2
for k in lis:
	col=0
	for l in k:
		if l!='':
			button(text=l,row=row,column=col,command=lambda val=l: set(val))
		col+=1
	row+=1
button(text="AC",bg='red',row=2,column=0,command=clear)
button(text="C",fg='red',row=6,column=0,command=erase)
button(text="=",bg='green',row=6,column=4,command=solve)
root.mainloop()
