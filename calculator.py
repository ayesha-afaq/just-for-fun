import customtkinter as ctk 
from customtkinter import CTkFrame,CTkButton,CTkEntry,CTkLabel

class calculator:
   def __init__(self,root):
      self.root=root
      self.root.title('Calculator')
      self.root.geometry('700x700')
      header=CTkLabel(master=self.root,text='HAPPY CALCULATING :)',font=("Arial", 16)).pack(pady=20)
   
      self.display =CTkEntry(self.root, font=("Arial", 24), justify="right")
      self.display.pack(pady=10)
      self.layout()
      

   def layout(self):
      self.button_frame =CTkFrame(self.root)
      self.button_frame.pack()
      buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]
        
        # Create buttons
      for i, text in enumerate(buttons):
            row = i // 4
            col = i % 4
            btn =CTkButton(
                self.button_frame,
                text=text,
                command=lambda t=text: self.on_button_click(t),
                font=("Arial", 18),
                height=50
            )
            btn.grid(row=row, column=col, padx=5, pady=5)

   def on_button_click(self,text):
      if text=='=':
         self.calculate()
      elif text=='C':
         self.display.delete(0,'end')
      else:
         self.display.insert('end',text)

   def calculate(self):
      try:
         expression=self.display.get()
         result=eval(expression)
         self.display.delete(0,'end')
         self.display.insert(0,str(result))
      except:
         self.display.delete(0,'end')
         self.display.insert(0,'Error')

      

app=ctk.CTk()
cal=calculator(app)

ctk.set_default_color_theme('blue')
ctk.set_appearance_mode('dark')

app.mainloop()