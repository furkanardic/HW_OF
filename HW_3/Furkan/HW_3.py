import tkinter as tk

pencere = tk.Tk()
pencere.geometry('1280x768')
#Baslik boyutu ve basligi çalistirma
headline= tk.Label(text='MARKETS')
headline.config(width=200)
headline.config(font=("Courier", 44))
headline.pack()
#buton calistirma
button_market_1 = tk.Button(text='Tamam', command=pencere.destroy)
button_market_1.config(width=10)
button_market_1.config(font=("Courier",30))
button_market_1.pack()
pencere.mainloop()
print(dir(tk.Label))