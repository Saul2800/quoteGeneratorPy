import tkinter as tk
import requests
from threading import Thread

api="http://api.quotable.io/random" #API of quotes
quotes=[]                           #empty
quote_number=0                      #star count

#---------------------------------------------------
#TKINTER
window=tk.Tk()
window.geometry("900x260")
window.title("Quote Generator")
window.grid_columnconfigure(0,weight=1)
window.resizable(False,False)
window.configure(bg="grey")
#---------------------------------------------------

#Load the quothes from the API to our computer
def preload_quotes():
    global quotes
    
    print("LOADING...")
    for x in range(10):
        random_quote=requests.get(api).json()
        content=random_quote["content"]
        author=random_quote["author"]
        quote=content+"\n\n"+" By " + author
        print(content)

        quotes.append(quote)
    print("Finished loading...")

preload_quotes() 

#count the quotes and show on the screen if you need more make the preload
def get_random_quote():
    global quote_label
    global quotes
    global quote_number

    quote_label.configure(text=quotes[quote_number])
    quote_number=quote_number+1
    print(quote_number)

    if quotes[quote_number]==quotes[-3]:
        thread=Thread(target=preload_quotes)
        thread.start()


#UI---------------------------------------------------
#Label to show the QUOTES
quote_label=tk.Label(window,text="Click to Quote",height=6,pady=10,wraplength=800,font=("Helvetica",14))
quote_label.grid(row=0,column=0,stick="WE",padx=20,pady=10)

#Button to activate and show quotes
button=tk.Button(text="Generate",command=get_random_quote,bg='#0052cc',fg='#ffffff',activebackground="grey",font=("Helvetica",14))
button.grid(row=1,column=0,stick="WE",padx=20,pady=10)



#Execute the main program
if __name__ == "__main__":
    window.mainloop()
