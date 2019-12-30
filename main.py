import tkinter as tk
from tkinter import messagebox
import database

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

		#Actions for Buttons.....
		def exitAction():
			exitdisp = messagebox.askyesno("Money Database Management System", "Are you sure you want to exit!")
			if exitdisp > 0:
				root.destroy()
			return

		def clearData():
			self.name_input.delete(0,"end")
			self.address_input.delete(0,"end")
			self.mobile_input.delete(0,"end")
			self.date_input.delete(0,"end")
			self.time_input.delete(0,"end")
			self.amount_input.delete(0,"end")

		def addPerson():
			name = self.name_input.get()
			address = self.address_input.get()
			mobile_no = self.mobile_input.get()
			date = self.date_input.get()
			time = self.time_input.get()
			amount = self.amount.get()
			self.person_list.delete(0,"end")
			status = database.addData(name,address,mobile_no,date,time,amount)
			if status:
				self.person_list.insert("end",(name,address,mobile_no,date,time,amount))
			else:
				self.person_list.insert("end","Not Added Something went wrong!!!")

		def personRec(event):
			global pd
			search_person = self.person_list.curselection()[0]
			pd = self.person_list.get(search_person)

			clearData()
			self.name_input.insert("end",pd[1])
			self.address_input.insert("end",pd[2])
			self.mobile_input.insert("end",pd[3])
			self.date_input.insert("end",pd[4])
			self.time_input.insert("end",pd[5])
			self.amount_input.insert("end",pd[6])



		def deletePerson():
			database.deleteData(pd[0])
			clearData()
			displayAll()

		def searchPerson():
			name = self.name_input.get()
			address = self.address_input.get()
			mobile_no = self.mobile_input.get()
			date = self.date_input.get()
			time = self.time_input.get()
			amount = self.amount.get()
			clearData()
			self.person_list.delete(0,"end")
			for row in database.searchData(name, address, mobile_no, date, time, amount):
				self.person_list.insert("end", row, str("\n"))

		def displayAll():
			self.person_list.delete(0,"end")
			for row in database.displayData():
				self.person_list.insert("end",row,str("\n"))

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
		self.person_list.bind("<<ListboxSelect>>", personRec)
		self.person_list.grid(row=0,column=0,padx=8)
		self.scrollbar.config(command=self.person_list.yview)

		#Buttons for interacting...
		self.addbtn = tk.Button(self.button_frame, text="Add New", font=('arial',20,'bold'), height=1, width=10, bd=4, command=addPerson)
		self.addbtn.grid(row=0, column=0)

		self.displaybtn = tk.Button(self.button_frame, text="Display", font=('arial',20,'bold'), height=1, width=10, bd=4, command=displayAll)
		self.displaybtn.grid(row=0, column=1)

		self.clearbtn = tk.Button(self.button_frame, text="Clear", font=('arial',20,'bold'), height=1, width=10, bd=4, command=clearData)
		self.clearbtn.grid(row=0, column=2)

		self.deletebtn = tk.Button(self.button_frame, text="Delete", font=('arial',20,'bold'), height=1, width=10, bd=4, command=deletePerson)
		self.deletebtn.grid(row=0, column=3)

		self.searchbtn = tk.Button(self.button_frame, text="Search", font=('arial',20,'bold'), height=1, width=10, bd=4, command=searchPerson)
		self.searchbtn.grid(row=0, column=4)

		self.exitbtn = tk.Button(self.button_frame, text="Exit", font=('arial',20,'bold'), height=1, width=10, bd=4, command=exitAction)
		self.exitbtn.grid(row=0, column=5)







if __name__=="__main__":
	root = tk.Tk()
	root.title("Money Management System")
	root.geometry("1350x750+0+0")
	#root.resizable(0,0)
	app = Application(root)
	root.mainloop()
