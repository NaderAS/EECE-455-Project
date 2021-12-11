import tkinter as tk
import aes



def table(root,encr):
    encryptmatrix = [["Round","Encrypted Message"]]
    roundnumb = 0
    for u in range(len(encr[0])):
        encryptmatrix.append([roundnumb,encr[0][u]])
        roundnumb = roundnumb + 1
    i = 0
    q = 0
    while(i < 9):
        j = 0
        k = 0
        while(j < 5):
            if (i == 0):
                if (j == 0):
                    e = tk.Entry(root, width=15,font=('Calibri',12))
                    e.grid(row=q, column=j)
                    e.insert(tk.END, encryptmatrix[i][j])
                    j = j + 1
                else:
                    e = tk.Entry(root, width=80,font=('Calibri',12))
                    e.grid(row=q, column=j)
                    e.insert(tk.END, encryptmatrix[i][j])
                    j = 5
                    i = i + 1
                    q = q + 1
            else:
                if (j == 0):
                    e = tk.Entry(root, width=15,font=('Calibri',12))
                    e.grid(row=q, column=j)
                    e.insert(tk.END, encryptmatrix[i][j])
                    j = j + 1
                else:
                    e = tk.Entry(root, width=80,font=('Calibri',12))
                    e.grid(row=q, column=1)
                    e.insert(tk.END, encryptmatrix[i][1][k])
                    if (q%4 != 1):
                        v = tk.Entry(root, width=15,font=('Calibri',12))
                        v.grid(row=q, column=0)
                    k = k + 1
                    j = j + 1
                    q = q + 1
                if (j == 5):
                    i = i + 1
    frame_B= tk.Frame(window, bd = 5)
    frame_B.place(relwidth = 0.17, relheight = 0.1, relx = 0.80, rely = 0.92, anchor = 'n')
    button_E = tk.Button(frame_B, text = "Next Page", font=('Calibri',18), command = lambda: changetable(root, encryptmatrix))
    button_E.place(relwidth=1, relheight = 1)
            
def changetable(root, encryptmatrix):
    i = 9
    q = 1
    empty = 0
    while(i < 18):
        j = 0
        k = 0
        while(j < 5):
            if (j == 0):
                if (empty == 0):
                    e = tk.Entry(root, width=15,font=('Calibri',12))
                    e.grid(row=q, column=j)
                    e.insert(tk.END, encryptmatrix[i][j])
                    j = j + 1
                else:
                    e = tk.Entry(root, width=15,font=('Calibri',12))
                    e.grid(row=q, column=j)
                    j = j + 1
            else:
                if (empty == 0):
                    e = tk.Entry(root, width=80,font=('Calibri',12))
                    e.grid(row=q, column=1)
                    e.insert(tk.END, encryptmatrix[i][1][k])
                    if (q%4 != 1):
                        v = tk.Entry(root, width=15,font=('Calibri',12))
                        v.grid(row=q, column=0)
                    k = k + 1
                    j = j + 1
                    q = q + 1
                else:
                    e = tk.Entry(root, width=80,font=('Calibri',12))
                    e.grid(row=q, column=1)
                    if (q%4 != 1):
                        v = tk.Entry(root, width=15,font=('Calibri',12))
                        v.grid(row=q, column=0)
                    k = k + 1
                    j = j + 1
                    q = q + 1
            if (j == 5):
                i = i + 1
            if (i == len(encryptmatrix)):
                        empty = 1

def encrypt(root, master_key, plaintext, type):
    encr = aes.AES_call(master_key, plaintext, type)
    print(encr[0])
    print(encr[1])
    t = table(root, encr)
    
    

    
def makewindow():
    
    OPTIONS = [
    "128",
    "192",
    "256"
    ]
    
    frame_type = tk.Frame(window, bd = 5)
    frame_type.place(relwidth = 0.45, relheight = 0.1, relx = 0.25, rely = 0.03, anchor = 'n')
    
    variable = tk.StringVar(window)
    variable.set(OPTIONS[0])
    
    dropdown_type = tk.OptionMenu(frame_type, variable, *OPTIONS, command=callback, variable=n)
    dropdown_type.place(relwidth=0.68, relheight = 1, relx = 0.32)
    
    label_type = tk.Label(frame_type, font=('Calibri',13), anchor = 'nw', justify='left', bd=4, text = "Type")
    label_type.place(relwidth=0.3, relheight = 1)
    
    frame_key = tk.Frame(window, bd = 5)
    frame_key.place(relwidth = 0.45, relheight = 0.1, relx = 0.25, rely = 0.15, anchor = 'n')
    
    entry_key = tk.Entry(frame_key, font=('Calibri',12))
    entry_key.place(relwidth=0.68, relheight = 1, relx = 0.32)
    
    label_key = tk.Label(frame_key, font=('Calibri',13), anchor = 'nw', justify='left', bd=4, text = "Key")
    label_key.place(relwidth=0.3, relheight = 1)
    
    
    frame_M = tk.Frame(window, bd = 5)
    frame_M.place(relwidth = 0.45, relheight = 0.1, relx = 0.25, rely = 0.3, anchor = 'n')
    
    entry_M = tk.Entry(frame_M, font=('Calibri',12))
    entry_M.place(relwidth=0.68, relheight = 1, relx = 0.32)
    
    label_M = tk.Label(frame_M, font=('Calibri',13), anchor = 'nw', justify='left', bd=4, text = "Message/Cypher")
    label_M.place(relwidth=0.3, relheight = 1)
    
    frame_E= tk.Frame(window, bd = 5)
    frame_E.place(relwidth = 0.45, relheight = 0.1, relx = 0.25, rely = 0.5, anchor = 'n')
    
    button_E = tk.Button(frame_E, text = "Encode ", font=('Calibri',18), command = lambda: encrypt(frame_table, int(entry_key.get(),16), int(entry_M.get(),16), n))
    button_E.place(relwidth=1, relheight = 1)
    
    frame_D= tk.Frame(window, bd = 5)
    frame_D.place(relwidth = 0.45, relheight = 0.1, relx = 0.25, rely = 0.7, anchor = 'n')
    
    button_D = tk.Button(frame_D, text = "Decode ", font=('Calibri',18), command = lambda: aes.AES_call_decrypt(int(entry_key.get(),16), int(entry_M.get(),16), n))
    button_D.place(relwidth=1, relheight = 1)
    
    frame_C= tk.Frame(window, bd = 5)
    frame_C.place(relwidth = 0.45, relheight = 0.1, relx = 0.25, rely = 0.9, anchor = 'n')
    
    button_D = tk.Button(frame_C, text = "Clear", font=('Calibri',18), command = lambda: clear())
    button_D.place(relwidth=1, relheight = 1)
    window.mainloop()

def clear():
    canvas.delete("all")
    makewindow()
    
    
HEIGHT = 1000
WIDTH = 1000


is_pressed = 0


window = tk.Tk()
#create operating region + resize window
canvas = tk.Canvas(window, height = HEIGHT, width = WIDTH)
#canvas.pack()
frame_table = tk.Frame(window, bd = 5)
frame_table.place(relx = 0.4)
makewindow()