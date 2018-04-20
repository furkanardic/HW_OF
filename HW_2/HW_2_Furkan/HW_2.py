import tkinter as tk

pencere = tk.Tk()
pencere.geometry('1280x768')

etiket = tk.Label(text='Merhaba Zalim Dünya')
etiket.pack()
düğme = tk.Button(text='Tamam', command=pencere.destroy)
düğme.pack()
pencere.mainloop()
