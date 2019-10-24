from tkinter import *
from tkinter import ttk
from math import sqrt
from tkinter import messagebox
import sys

tk = Tk()

def solveEqn(a, b, cx):
    x1x = ((-1 * b) + sqrt(pow(b, 2) - (4 * a * cx))) / (2 * a)
    x2x = ((-1 * b) - sqrt(pow(b, 2) - (4 * a * cx))) / (2 * a)
    xA = [x1x, x2x]
    return xA

def get_dir(src):
    dir = sys.argv[0]
    dir = dir.split('/')
    dir.pop(-1)
    dir = '/'.join(dir)
    dir = dir+'/'+src
    return dir

def vectConvert(x, y):
   
    xOp = (30 * x) + 150
    yOp = (30 * x) + 105
    xAp = [xOp, yOp]
    return 

def vectConvertX(positions_list):
    ald = []
    for x in range(0, len(positions_list)):
        cys = positions_list[x]
        cys = (30 * cys) + 300
        ald.append(cys)
    return ald

global canvas1
#User input fraction
mega_frame = Frame(tk, bg="#F20530")
mega_frame.pack()
frame = Frame(mega_frame, bg="#F20530")
frame.grid()
frame2 = Frame(mega_frame)
frame2.grid()

OPTIONS = [
    "quadratic"
]
lbl2 = Label(frame, text="Co-efficient of X", bg="#A60303")
entry2 = Entry(frame)
lbl3 = Label(frame, text="Constant", bg="#A60303")
entry3 = Entry(frame)
lbl4 = Label(frame, text="Co-efficient of X2", bg="#A60303")
entry4 = Entry(frame)
lbl2.grid(row=2, column=0, sticky=E)
entry2.grid(row=2, column=1)
lbl3.grid(row=3, column=0, sticky=E)
entry3.grid(row=3, column=1)
lbl4.grid(row=4, column=0, sticky=E)
entry4.grid(row=4, column=1)

def labels(eqn_type):
    if eqn_type == "quadratic":
        #entry5.configure(state='disabled')
        entry2.configure(state='normal')
        entry3.configure(state='normal')
        entry6.configure(state='disabled')
  
def get_status():
    if variable.get() == "quadratic":
        labels("quadratic")
        
def create_graph():
    try:
        canvas1.delete("gd1")
        canvas1.delete("gd2")
    except:
        pass
    
    if variable.get() == "quadratic":
        a = int(entry4.get())
        b = int(entry2.get())
        cx = int(entry3.get())

        try:
            posy = solveEqn(a, b, cx)
        except:
            messagebox.showerror('Value Error', 'The values you entered are invalid')
            tk.destroy()
            
        print(posy)
        txt = "Pos1:", posy[0],',', 0, "Pos2:", 0,',', cx, "Pos3:", posy[1],',', 0
        poslbl.configure(text=txt)
        
        #Convert positions
        posy = vectConvertX(posy)

        #When y = 0
        x1 = posy[0]
        x2 = posy[1]
        
        #When x = 0
        y1 = (7 - (cx)) * 30

        i = canvas1.create_line(x1, 210, 300, y1, width=2, fill='black', tags="gd1")
        j = canvas1.create_line(300, y1, x2, 210, width=2, fill="black", tags="gd2")
        
variable = StringVar(frame)
variable.set(OPTIONS[0])

lbl1 = Label(frame, text="Equation Type", bg="#A60303")
lbl1.grid(row=0, sticky=E)
drop_menu1 = OptionMenu(frame, variable, *OPTIONS)
drop_menu1.grid(row=0, column=1)
btn1 = ttk.Button(frame, text="Re-run", command=get_status)
btn1.grid(column=0, row=5)
btn2 = ttk.Button(frame, text="Create Graph", command=create_graph)
btn2.grid(column=1, row=5)
btn3 = ttk.Button(frame, text="Exit App", command=tk.destroy)
btn3.grid(column=2, row=5)
poslbl = ttk.Label(frame, text='Vector location will appear here', background="yellow", font=("MS Sans Serif", 16))
poslbl.grid(columnspan=3, row=6)
canvas1 = Canvas(frame2, bg="white", width=600, height=450)
canvas1.grid()

y = 30
x = 30
canvas1.create_line(0, 0, 0, 450, fill='black')
canvas1.create_line(0, 0, 600, 0, fill='black')
canvas1.create_line(600, 0, 600, 450, fill='black')
canvas1.create_line(0, 210, 600, 210, fill='red', width=3)
canvas1.create_line(300, 0, 300, 450, fill='blue', width=3)

while(y <= 450):
    canvas1.create_line(0, y, 600, y, fill='black')
    y += 30
while(x < 600):
    canvas1.create_line(x, 0, x, 450, fill='black')
    x += 30


#lbl2 = Label(frame, text="")

tk.title("Quadratic Graph Presenter")
tk.resizable(False, False)
tk.iconbitmap("favicon.ico")
tk.mainloop()
