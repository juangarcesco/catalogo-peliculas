import tkinter as tk
from client.gui_app import Frame

def main():
    root = tk.Tk()
    root.title("Catalogo de peliculas")
    root.iconbitmap('img/cp-logo.ico') 
    root.resizable(0,0)
    

    app = Frame(root = root)
    
    root.mainloop()

if __name__ == '__main__':
    
    main()