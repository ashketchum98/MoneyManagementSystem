import tkinter as tk

class Application():

	def __init__(self, root):

		root.config(bg="cadet blue")

		#StringVars for all Inputs...
		self.name = tk.StringVar()
		self.address = tk.StringVar()
		self.mobile = tk.StringVar()
		self.date = tk.StringVar()
		self.time = tk.StringVar()
		self.amount = tk.StringVar()

		#Main Frame
		self.main_frame = tk.Frame(root, bg="cadet blue")
		self.main_frame.grid()

		#Frame for Title
		self.title_frame = tk.Frame(self.main_frame, bd=2, padx=54, pady=8, bg="ghost white", relief="ridge")
		self.title_frame.pack(side="top")

		#Label for title
		self.title_label = tk.Label(self.title_frame, font=('arial', 47, 'bold'), text="Money Database Management System", bg="ghost white")
		self.title_label.grid()

		#Frame for buttons
		self.button_frame = tk.Frame(self.main_frame,bd=2, width=1350, height=70, padx=18, pady=10, bg="ghost white")
		self.button_frame.pack(side="bottom")

		self.data_frame = tk.Frame(self.main_frame,bd=1, width=1300, height=400, padx=20, pady=20, bg="cadet blue")
		self.data_frame.pack(side="bottom")

		self.left_data_frame = tk.LabelFrame(self.data_frame, bd=1, width=1000, height=600, padx=20, font=('arial', 20, 'bold'), bg="ghost white", text="Person Info")
		self.left_data_frame.pack(side="left")

		self.right_data_frame = tk.LabelFrame(self.data_frame, bd=1, width=450, height=300, padx=31, pady=3, font=('arial', 20, 'bold'), bg="ghost white", text="Person Details")
		self.right_data_frame.pack(side="right")

		#Labels and Input Fields for Person Info...
		self.name_label = tk.Label(self.left_data_frame, font=('arial',20,'bold'), text="Name: ",padx=2,pady=2,bg="ghost white")
		self.name_label.grid(row=0,column=0,sticky="w")
		self.name_input = tk.Entry(self.left_data_frame, font=('arial',20,'bold'), textvariable=self.name, width=39)
		self.name_input.grid(row=0,column=1)

		self.address_label = tk.Label(self.left_data_frame, font=('arial',20,'bold'), text="Address: ",padx=2,pady=2,bg="ghost white")
		self.address_label.grid(row=1,column=0,sticky="w")
		self.address_input = tk.Entry(self.left_data_frame, font=('arial',20,'bold'), textvariable=self.address, width=39)
		self.address_input.grid(row=1,column=1)

		self.mobile_label = tk.Label(self.left_data_frame, font=('arial',20,'bold'), text="Mobile No: ",padx=2,pady=2,bg="ghost white")
		self.mobile_label.grid(row=2,column=0,sticky="w")
		self.mobile_input = tk.Entry(self.left_data_frame, font=('arial',20,'bold'), textvariable=self.mobile, width=39)
		self.mobile_input.grid(row=2,column=1)

		self.date_label = tk.Label(self.left_data_frame, font=('arial',20,'bold'), text="Date: ",padx=2,pady=2,bg="ghost white")
		self.date_label.grid(row=3,column=0,sticky="w")
		self.date_input = tk.Entry(self.left_data_frame, font=('arial',20,'bold'), textvariable=self.date, width=39)
		self.date_input.grid(row=3,column=1)

		self.time_label = tk.Label(self.left_data_frame, font=('arial',20,'bold'), text="Time: ",padx=2,pady=2,bg="ghost white")
		self.time_label.grid(row=4,column=0,sticky="w")
		self.time_input = tk.Entry(self.left_data_frame, font=('arial',20,'bold'), textvariable=self.time, width=39)
		self.time_input.grid(row=4,column=1)

		self.amount_label = tk.Label(self.left_data_frame, font=('arial',20,'bold'), text="Amount: ",padx=2,pady=2,bg="ghost white")
		self.amount_label.grid(row=5,column=0,sticky="w")
		self.amount_input = tk.Entry(self.left_data_frame, font=('arial',20,'bold'), textvariable=self.amount, width=39)
		self.amount_input.grid(row=5,column=1)

		#ScrollBar and ListBox for all details...
		self.scrollbar = tk.Scrollbar(self.right_data_frame)
		self.scrollbar.grid(row=0, column=1, sticky="ns")

		self.person_list = tk.Listbox(self.right_data_frame, width=41, height=16, font=('arial',12,'bold'), yscrollcommand=self.scrollbar.set)
		self.person_list.grid(row=0,column=0,padx=8)
		self.scrollbar.config(command=self.person_list.yview)





if __name__=="__main__":
	root = tk.Tk()
	root.title("Money Management System")
	root.geometry("1350x750+0+0")
	#root.resizable(0,0)
	app = Application(root)
	root.mainloop()
