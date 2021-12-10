import tkinter as tk
import aes


HEIGHT = 500
WIDTH = 500


is_pressed = 0


window = tk.Tk()

#create operating region + resize window
canvas = tk.Canvas(window, height = HEIGHT, width = WIDTH)
canvas.pack()


frame_key = tk.Frame(window, bd = 5)
frame_key.place(relwidth = 0.45, relheight = 0.1, relx = 0.25, rely = 0.1, anchor = 'n')

entry_key = tk.Entry(frame_key, font=('Calibri',12))
entry_key.place(relwidth=0.68, relheight = 1, relx = 0.32)

label_key = tk.Label(frame_key, font=('Calibri',13), anchor = 'nw', justify='left', bd=4, text = "Key")
label_key.place(relwidth=0.3, relheight = 1)


frame_M = tk.Frame(window, bd = 5)
frame_M.place(relwidth = 0.45, relheight = 0.1, relx = 0.25, rely = 0.25, anchor = 'n')

entry_M = tk.Entry(frame_M, font=('Calibri',12))
entry_M.place(relwidth=0.68, relheight = 1, relx = 0.32)

label_M = tk.Label(frame_M, font=('Calibri',13), anchor = 'nw', justify='left', bd=4, text = "Message")
label_M.place(relwidth=0.3, relheight = 1)

frame_E= tk.Frame(window, bd = 5)
frame_E.place(relwidth = 0.45, relheight = 0.1, relx = 0.25, rely = 0.5, anchor = 'n')

button_E = tk.Button(frame_E, text = "Encode ", font=('Calibri',18), command = lambda: AES_call(entry_key.get(), entry_M.get()))
button_E.place(relwidth=1, relheight = 1)

frame_D= tk.Frame(window, bd = 5)
frame_D.place(relwidth = 0.45, relheight = 0.1, relx = 0.25, rely = 0.7, anchor = 'n')

button_D = tk.Button(frame_D, text = "Decode ", font=('Calibri',18), command = lambda: AES_call(entry_key.get(), entry_M.get()))
button_D.place(relwidth=1, relheight = 1)



window.mainloop()
