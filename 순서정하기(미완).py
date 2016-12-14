from tkinter import *
import time 
class App(Frame):
	def __init__(self,master):
		super().__init__(master)
		self.pack(padx=10, pady=10)
		self.button1_clicks = 0
		self.button2_clicks = 0
		self.create_widgets()
	
	def create_widgets(self):
		Label(self, text='순서방향을 정해주십시오').grid(row=0, column=1)
		Label(self, text=' ').grid(row=1,column=1)
		self.button1 = Button(self)
		self.button1["text"] = "순방향"
		self.button1["command"] = self.update_count1
		self.button1.grid(row=3, column=0)
		self.button2 = Button(self)
		self.button2['text'] = '역방향'
		self.button2['command'] = self.update_count2
		self.button2.grid(row=3, column=2)
		Button(self, text="quit", command=self.quit).grid(row=4, column=2)
	
	def update_count1(self):
		self.button1_clicks += 1

	def update_count2(self):
		self.button2_clicks += 1

root = Tk()
root.title('ckeck')
root.geometry("400x300")
app = App(root)
root.mainloop()

