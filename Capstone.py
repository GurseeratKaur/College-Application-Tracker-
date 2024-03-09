import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import time
import sqlite3 
from sqlite3 import Error

# Creating a tkinter GUI Application with 3 pages - 
#	1.) profile
#	2.) college application deadlines
#	3.) extracurricular activities

root = tk.Tk()
root.title("College Application Tracker")
root.resizable(True,True)
nb = ttk.Notebook(root, width = 1380, height = 730)
nb.grid(row = 1, column = 0)

page1 = ttk.Frame(nb)
page2 = ttk.Frame(nb)
page3 = ttk.Frame(nb)
nb.add(page1, text="Profile")
nb.add(page2, text ="College Application Deadlines")
nb.add(page3, text="Extracurricular Activities")

# Class for rendering animated gifs successfully

class AnimatedGif(tk.Label):
	"""
	Class to show animated GIF file in a label
	Use start() method to begin animation, and set the stop flag to stop it
	"""
	def __init__(self, root, gif_file, delay):
		"""
		:param root: tk.parent
		:param gif_file: filename (and path) of animated gif
		:param delay: delay between frames in the gif animation (float)
		"""
		tk.Label.__init__(self, root)
		self.root = root
		self.gif_file = gif_file
		self.delay = delay  # Animation delay - try low floats, like 0.04 (depends on the gif in question)
		self.stop = False  # Thread exit request flag

		self._num = 0

	def start(self):
		""" Starts non-threaded version that we need to manually update() """
		self.start_time = time.time()  # Starting timer
		self._animate()

	def stop(self):
		""" This stops the after loop that runs the animation, if we are using the after() approach """
		self.stop = True

	def _animate(self):
		try:
			self.gif = tk.PhotoImage(file=self.gif_file, format='gif -index {}'.format(self._num))  # Looping through the frames
			self.configure(image=self.gif)
			self._num += 1
		except tk.TclError:  # When we try a frame that doesn't exist, we know we have to start over from zero
			self._num = 0
			#self.stop = True  - to stop the animated gif after it has completed one cycle
		if not self.stop:    # If the stop flag is set, we don't repeat
			self.root.after(int(self.delay*1000), self._animate)

def animation(frame, gif_file):
	lbl_with_my_gif = AnimatedGif(frame,gif_file,0.01) 
	lbl_with_my_gif.grid(row = 0, column = 0)
    # Shows gif at first frame and we are ready to go
	lbl_with_my_gif.start()	

#PAGE 1: Profile Page
			
lblfr_profile = ttk.LabelFrame(page1, text = "MY PROFILE")
lbl_name = ttk.Label(lblfr_profile, text=" Full name:")
lbl_age = ttk.Label(lblfr_profile, text="Age:")
lbl_dob = ttk.Label(lblfr_profile, text="DOB:\n*(dd/mm/yyyy)")
lbl_gender = ttk.Label(lblfr_profile, text="Gender:")
lbl_hobbies = ttk.Label(lblfr_profile, text = "Hobbies:")
lbl_career = ttk.Label(lblfr_profile, text = "What are your career aspirations:")

flower_image = PhotoImage(file="flower.gif")
picture = ttk.Label(lblfr_profile, image = flower_image)
txt_profile_name = ttk.Entry(lblfr_profile)
txt_age = ttk.Entry(lblfr_profile)
txt_dob = ttk.Entry(lblfr_profile)
var_chk = IntVar()
rdl_1 = ttk.Radiobutton(lblfr_profile,text = "Male", variable = var_chk, value = 1)
rdl_2 = ttk.Radiobutton(lblfr_profile,text = "Female", variable = var_chk, value = 2)
rdl_3 = ttk.Radiobutton(lblfr_profile,text = "Other", variable = var_chk, value = 3)
hobbies = tk.Text(lblfr_profile, width = 40, height = 5, wrap = "word")
career = tk.Text(lblfr_profile, width = 40, height = 5, wrap = "word")


lblfr_profile.grid(row = 4, column = 1,sticky = "nw", ipadx= 50) 
picture.grid(row = 0, column = 0, rowspan = 2)
lbl_name.grid(row = 0, column = 1 )
lbl_age.grid(row = 1, column = 1)
lbl_dob.grid(row =2 , column = 1)
lbl_gender.grid(row = 3, column = 1)
lbl_hobbies.grid(row = 4, column = 1)
lbl_career.grid(row = 9, column = 1) #

txt_profile_name.grid(row = 0, column = 2)
txt_age.grid(row = 1, column = 2)
txt_dob.grid(row = 2, column =2)
rdl_1.grid(row =3, column = 2, sticky = "w")
rdl_2.grid(row =3, column = 2, sticky = "")
rdl_3.grid(row =3, column = 2, sticky = "e")
hobbies.grid(row = 4, column = 2, rowspan = 4)
career.grid(row = 9, column = 2, rowspan = 4) 

#PAGE 2: College applicaion deadlines Page

lblfr_college = ttk.LabelFrame(page2, text = "College Information") 
frame =tk.Frame(page2,width=200, height=200,colormap="new")
frame.grid(row = 0, column = 0,sticky = "ne")

# help button 
def helping_instructions(filename):
	top = Toplevel()
	top.title("Help")
	
	photo = PhotoImage(file= filename)
	w = Label(top, image=photo)
	w.photo = photo
	w.grid(row = 0, column = 3)

animation(frame, 'iconic.gif')
btn_help = tk.Button(frame,text = "HELP",command = lambda: helping_instructions("college.gif"),bg = "blue",width = 7, height = 1)
btn_help.grid(row = 1, column = 0)

# widgets
lbl_name = ttk.Label(lblfr_college, text = "Name of College: *", font = ("Arial", 15))
lbl_tuition_fees = ttk.Label(lblfr_college, text = "Tuition fees: *", font = ("Arial",15))
lbl_accomodation_cost = ttk.Label(lblfr_college, text = "Accomodation cost: ", font = ("Arial",15))
lbl_program = ttk.Label(lblfr_college, text = "Program applied:*", font = ("Arial",15))
lbl_rank_sw = ttk.Label(lblfr_college, text = "Competitiveness(out of 10): ", font = ("Arial",15))
lbl_location = ttk.Label(lblfr_college, text = "Location:* ", font = ("Arial",15))
lbl_requirements = ttk.Label(lblfr_college, text = "Requirements:*",font =("Arial",15))
lbl_doc_deadline = ttk.Label(lblfr_college, text = "Documents submission deadline:(mm/dd/yyyy)*",font =("Arial",15))
lbl_application_deadline = ttk.Label(lblfr_college, text = "Application submission deadline:(mm/dd/yyyy)*",font =("Arial",15))

txt_name = ttk.Entry(lblfr_college)
txt_tuition_fees = ttk.Entry(lblfr_college)
txt_accomodation_cost = ttk.Entry(lblfr_college)
txt_rank_sw = ttk.Entry(lblfr_college)
txt_program = ttk.Entry(lblfr_college)
txt_location = ttk.Entry(lblfr_college)
txt_requirements = ttk.Entry(lblfr_college)
txt_doc = ttk.Entry(lblfr_college)
txt_app = ttk.Entry(lblfr_college)

lblfr_college.grid(row = 0, column = 0, sticky = "nw")
lbl_name.grid(row = 0, column = 0)
lbl_tuition_fees.grid(row = 1, column = 0)
lbl_accomodation_cost.grid(row = 2, column = 0)
lbl_rank_sw.grid(row = 3, column = 0)
lbl_program.grid(row = 4, column = 0)
lbl_location.grid(row = 5, column = 0)
lbl_requirements.grid(row = 6, column = 0)
lbl_doc_deadline.grid(row =7, column = 0)
lbl_application_deadline.grid(row = 8, column = 0)

txt_name.grid(row = 0, column = 1)
txt_tuition_fees.grid(row = 1, column = 1)
txt_accomodation_cost.grid(row = 2, column = 1) 
txt_rank_sw.grid(row = 3, column = 1)
txt_program.grid(row = 4, column = 1) 
txt_location.grid(row = 5, column = 1)
txt_requirements.grid(row = 6, column = 1)
txt_doc.grid(row =7, column = 1)
txt_app.grid(row = 8, column = 1)

#Treeview 
tree = ttk.Treeview(page2, selectmode ="browse",columns = ("College","Fees","Accomo.","Program","Rank","Location","Requirements","doc","app"))
tree.heading("#0", text="IDX")
tree.column("#0",width=50)
tree.heading("College",text = "College")
tree.heading("Fees", text="Tuition fees")
tree.column("Fees",width = 100)
tree.column("Accomo.",width = 150)
tree.heading("Accomo.", text="Accomodation cost")
tree.heading("Program", text = "Program")
tree.heading("Rank", text="Competitiveness")
tree.column("Rank",width = 100)
tree.heading("Location", text = "Location")
tree.column("Location",width =150)
tree.heading("Requirements", text = "Requirements")
tree.heading("doc",text="Doc deadline")
tree.column("doc",width =100)
tree.heading("app",text="App deadline")
tree.column("app",width =100)
tree.grid(row = 1, column = 0, rowspan = 10)

#PAGE 3: Extracurricular activities page

# function to count text in descripton field
def length_of_text(event):
	text = general_description.get("1.0", "end-1c").split(" ")
	txt_word_count.delete(0,"end")
	txt_word_count.insert(0, "{}".format(len(text)))
	lbl_word_alert = ttk.Label(lblfr_text,text = "                                                                                                                                      ", font = ("Arial",15) ,foreground = "red", justify = "left")
	lbl_word_alert.grid(row = 1, column = 0)
	
	if len(text)>100:		
		lbl_word_alert["text"] = " You have exceeded the maximum word length by {}. Please shorten your response.".format(len(text)-100)
		
	if len(text) <= 100:
		lbl_word_alert["text"] =  "                                                                                                                                      "

#frame
lblfr_activity = ttk.LabelFrame(page3, text = "Extracurricular Inforamtion")
lblfr_text = ttk.LabelFrame(page3, text = "Description(in less than 100 words):") #
frame_1 =tk.Frame(page3,width=200, height=200,colormap="new")
frame_1.grid(row = 0, column = 1,sticky = "ne")

#help button
animation(frame_1,'iconic.gif')
btn_help = tk.Button(frame_1,text = "HELP",command = lambda: helping_instructions("activity.gif"),width = 7, height = 1)
btn_help.grid(row = 1, column = 0)

# widgets
lbl_activity = ttk.Label(lblfr_activity, text = "Extracurricular Activity: *", font = ("Arial", 15))
lbl_type = ttk.Label(lblfr_activity, text = "Type: *", font = ("Arial",15))
lbl_sch_years = ttk.Label(lblfr_activity, text = "School years involved in activity: *", font = ("Arial",15))
lbl_years = ttk.Label(lblfr_activity, text = "No. of years involved in activity: *", font = ("Arial",15))
lbl_hrs_per_wk = ttk.Label(lblfr_activity, text = "Time spent per week (in hours): *", font = ("Arial",15))
lbl_wks_per_yr = ttk.Label(lblfr_activity, text = "Weeks spent per year *: ", font = ("Arial",15))
lbl_status = ttk.Label(lblfr_activity,text = "Status([A]ctive/[U]nactive):*",font = ("Arial",15))

txt_activity = ttk.Entry(lblfr_activity)
txt_type = ttk.Entry(lblfr_activity)
txt_sch_years = ttk.Entry(lblfr_activity)
txt_years = ttk.Entry(lblfr_activity)
txt_hrs_per_wk= ttk.Entry(lblfr_activity)
txt_wks_per_yr= ttk.Entry(lblfr_activity)
txt_status = ttk.Entry(lblfr_activity)

lblfr_activity.grid(row = 0, column = 0, sticky = "w", padx=(0,5))
lblfr_text.grid(row = 0, column = 0, sticky = 'e') 
page3.grid_columnconfigure(0, weight=1)
lbl_activity.grid(row = 0, column = 0)
lbl_type.grid(row = 1, column = 0)
lbl_sch_years.grid(row = 2, column = 0)
lbl_years.grid(row = 3, column = 0)
lbl_hrs_per_wk.grid(row = 4, column = 0)
lbl_wks_per_yr.grid(row = 5, column = 0)
lbl_status.grid(row = 6, column = 0)

txt_activity.grid(row = 0, column = 1)
txt_type.grid(row = 1, column = 1)
txt_sch_years.grid(row = 2, column = 1) 
txt_years.grid(row = 3, column = 1)
txt_hrs_per_wk.grid(row = 4, column = 1) 
txt_wks_per_yr.grid(row = 5, column = 1)
txt_status.grid(row = 6, column = 1)


general_description = tk.Text(lblfr_text, width = 70, height = 10, bg = "black", fg = "white", wrap = "word") #
general_description.configure(insertbackground= "white") #to make the cursor white so that we can keep track of it
general_description.bind("<Key>", length_of_text) #
general_description.grid(row = 0, column = 0)

txt_word_count = ttk.Entry(lblfr_text, width = 10)
txt_word_count.grid(row = 2, column = 0)
lbl_word_alert = ttk.Label(lblfr_text,text = "                                                                                                                                      ", font = ("Arial",15) ,foreground = "red", justify = "left")
lbl_word_alert.grid(row = 1, column = 0)

#Treeview
tree_2 = ttk.Treeview(page3, columns = ("activity","type","sch_years","years","hrs_per_wk","wk_per_yr","status","description"))
tree_2.heading("#0", text="IDX")
tree_2.heading("activity", text="Activity")
tree_2.heading("type", text="Type")
tree_2.heading("sch_years", text = "School years")
tree_2.heading("years", text = "No. of years")
tree_2.heading("hrs_per_wk", text="hrs/wk")
tree_2.heading("wk_per_yr",text = "wks/yr")
tree_2.heading("status",text = "Status (Active/Unactive)")
tree_2.column("#0",width = 50)
tree_2.column("sch_years",width = 100)
tree_2.column("years",width = 100)
tree_2.column("hrs_per_wk",width = 100)
tree_2.column("wk_per_yr",width = 100)
tree_2.column("status",width = 150)
tree_2.heading("description",text = "Description")
tree_2.column("description",width = 350)

tree_2.grid(row = 1, column = 0, rowspan = 10)

#FUNCTIONS for SQLite Database handling 

#creating connection to pythonsqlite3 database
def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    finally:
        conn.close()

# if __name__ == '__main__':
#     create_connection("pythonsqlite3.db")
# creating tables in pythonsqlite3 database
def return_conn(db_file):
    
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None
    
def create_table(conn, create_table_sql):
    
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
        
def main_to_create_table():
    database = "pythonsqlite3.db"
    
    sql_create_profile = """ CREATE TABLE IF NOT EXISTS profile (
                                        "name" text NOT NULL,
                                        "age" INTEGER,
                                        "dob" text,
                                        "career" text,
                                        "hobbies" text,
                                        "gender" text
                                    ); """
    
    sql_create_college_info_table = """ CREATE TABLE IF NOT EXISTS college_info (
                                        "IDX" INTEGER PRIMARY KEY,
                                        "name" text NOT NULL,
                                        "tuition fees" text,
                                        "accomodation cost" text,
                                        "program" text,
                                        "competitiveness" INTEGER,
                                        "location" text,
                                        "requirements" text,
                                        "document submission deadline" text,
                                        "application deadline" text
                                    ); """
 
    sql_create_activity_table = """CREATE TABLE IF NOT EXISTS extracurricular_activities (
                                   "IDX" INTEGER PRIMARY KEY,
                                    "activity" text NOT NULL,
                                    "type" text,
                                    "school years" numeric,
                                    "years" integer NOT NULL,
                                    "hours per week" integer NOT NULL,
                                    "weeks per year" integer NOT NULL,
                                    "status" text NOT NULL,
                                    "description" text 
                                );"""
 
    # create a database connection
    conn = return_conn(database)
    if conn is not None:
        # create college_info table
        create_table(conn, sql_create_college_info_table)
        # create profile database to store data
        create_table(conn,sql_create_profile)
        # create activity table
        create_table(conn, sql_create_activity_table)
    else:
        print("Error! cannot create the database connection.")

# if __name__ == '__main__':
#     main_to_create_table()

#creating entries for the tables in the database

def create_college_info(conn, college_entry):
    sql = " INSERT INTO college_info('name','tuition fees','accomodation cost','program','competitiveness','location','requirements','document submission deadline','application deadline') VALUES(?,?,?,?,?,?,?,?,?)"
    cur = conn.cursor()
    cur.execute(sql, college_entry)
    conn.commit()
    return cur.lastrowid

def create_activity(conn, activity_entry):
    sql = " INSERT INTO extracurricular_activities('activity','type','school years','years','hours per week','weeks per year','status','description') VALUES(?,?,?,?,?,?,?,?)"
    cur = conn.cursor()
    cur.execute(sql, activity_entry)
    conn.commit()
    return cur.lastrowid # to return the index

#reading entries from tables and displaying them on the GUI
def read_profile():
	database = "pythonsqlite3.db"
  # create a database connection
	conn = return_conn(database)
	cur = conn.cursor()
	cur.execute("SELECT * FROM profile")
	rows = cur.fetchall()
	for row in rows:
		if row[0] != "":
			txt_profile_name.insert(0,row[0])
			txt_age.insert(0,row[1])
			txt_dob.insert(0,row[2])
			career.insert(1.0,row[3])
			hobbies.insert(1.0,row[4])
			var_chk.set(row[5])


def read_from_college_database():
	database = "pythonsqlite3.db"
	conn = return_conn(database)
	cur = conn.cursor()
	cur.execute("SELECT * FROM college_info")
	rows = cur.fetchall()
	for row in rows:
		tree.insert("", "end", text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9]))


def read_from_activity_database():
	database = "pythonsqlite3.db"
	conn = return_conn(database)
	cur = conn.cursor()
	cur.execute("SELECT * FROM extracurricular_activities")
	rows = cur.fetchall()
	for row in rows:
		tree_2.insert("", "end", text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]))


# Inserting new entries into the database and displaying them on the GUI
def main_to_insert_in_table():
	database = "pythonsqlite3.db"
	conn = return_conn(database)
 # create a database connection
	with conn:
		if  txt_name.get() == "" or txt_tuition_fees.get() == "" or txt_program.get() == "" or txt_location.get() == "" or txt_requirements.get() == "" or txt_doc.get() == "" or txt_app.get() == "":
			messagebox.showinfo("Error","Please fill in necessary entries(marked by *)")
		else:
			college_1 =(txt_name.get(),txt_tuition_fees.get(),txt_accomodation_cost.get(),txt_program.get(),txt_rank_sw.get(),txt_location.get(),txt_requirements.get(),txt_doc.get(),txt_app.get())
			index = create_college_info(conn, college_1) #to create a college application info entry in the database
			tree.insert("", "end", text=index, values=(txt_name.get(),txt_tuition_fees.get(),txt_accomodation_cost.get(),txt_program.get(),txt_rank_sw.get(),txt_location.get(),txt_requirements.get(),txt_doc.get(),txt_app.get()))
			messagebox.showinfo("Update", "Successfully added to database.")

def main_to_insert_in_table_2():
	database = "pythonsqlite3.db"
 
    # create a database connection
	conn = return_conn(database)
	with conn:
		
		if txt_activity.get() == "" or txt_type.get() == "" or txt_sch_years.get() == "" or txt_years == "" or txt_hrs_per_wk.get() == "" or txt_wks_per_yr.get() == "" or txt_status.get() == "": #txt_index_2.get() == "" or 
			messagebox.showinfo("Error","Please fill in necessary entries(marked by *)")
		else:
			activity_1 = (txt_activity.get(),txt_type.get(),txt_sch_years.get(),txt_years.get(),txt_hrs_per_wk.get(),txt_wks_per_yr.get(),txt_status.get(),general_description.get("1.0", "end-1c"))#,description.get("1.0", "end-1c"))
			index = create_activity(conn, activity_1) # to create an activity entry in the database
			tree_2.insert("","end",text = index,values =(txt_activity.get(),txt_type.get(),txt_sch_years.get(),txt_years.get(),txt_hrs_per_wk.get(),txt_wks_per_yr.get(),txt_status.get(),general_description.get("1.0", "end-1c")))
			messagebox.showinfo("Update","Successfully added to the database.")
 		

	
#Code to display values in the form based on the entry selected in the TreeView.
def selected_college_entry(a): 
	database = "pythonsqlite3.db"
	conn = return_conn(database)
	cur = conn.cursor()
	idx =  tree.item(tree.focus())['text']
	sql = cur.execute("SELECT * FROM college_info WHERE IDX=?",(idx,)).fetchall()
	for item in sql:
		name = item[1]
		tuition_fees = item[2]
		accomodation_cost= item[3]
		program= item[4]
		competitiveness=item[5]
		location= item[6]
		requirements= item[7]
		doc = item[8]
		app = item[9]
	conn.commit()
	txt_name.delete(0,"end")
	txt_tuition_fees.delete(0,"end")
	txt_accomodation_cost.delete(0,"end")
	txt_program.delete(0,"end")
	txt_rank_sw.delete(0,"end")
	txt_location.delete(0,"end")
	txt_requirements.delete(0,"end")
	txt_doc.delete(0,"end")
	txt_app.delete(0,"end")
	txt_tuition_fees.insert(0,tuition_fees)
	txt_name.insert(0,name)
	txt_accomodation_cost.insert(0,accomodation_cost)
	txt_program.insert(0,program)
	txt_rank_sw.insert(0,competitiveness)
	txt_location.insert(0,location)
	txt_requirements.insert(0,requirements)
	txt_doc.insert(0,doc)
	txt_app.insert(0,app)

def selected_activty_entry(a):
	database = "pythonsqlite3.db"
	conn = return_conn(database)
	cur = conn.cursor()
	idx_2 =  tree_2.item(tree_2.focus())['text']
	sql = cur.execute("SELECT * FROM extracurricular_activities where IDX=?",(idx_2,))
	for item in sql:
		activity = item[1]
		type = item[2]
		sch_years= item[3]
		years= item[4]
		hrs_per_wk=item[5]
		wks_per_year= item[6]
		status= item[7]
		description = item[8]
	conn.commit()
	
	txt_activity.delete(0,"end")
	txt_type.delete(0,"end")
	txt_sch_years.delete(0,"end")
	txt_years.delete(0,"end")
	txt_hrs_per_wk.delete(0,"end")
	txt_wks_per_yr.delete(0,"end")
	txt_status.delete(0,"end")
	general_description.delete(1.0,"end") 
	txt_word_count.delete(0,"end")
	txt_activity.insert(0,activity)
	txt_type.insert(0,type)
	txt_sch_years.insert(0,sch_years)
	txt_years.insert(0,years)
	txt_hrs_per_wk.insert(0,hrs_per_wk)
	txt_wks_per_yr.insert(0,wks_per_year)
	txt_status.insert(0,status)
	general_description.insert("end",description) # insert into decription
	text = general_description.get("1.0", "end-1c").split(" ")
	txt_word_count.insert(0, "{}".format(len(text)))


#deletion of entries from the database
def delete_entry(conn, IDX, table_name):
	sql = f"DELETE FROM {table_name} WHERE IDX=?"
	cur = conn.cursor()
	cur.execute(sql, (IDX,))

def delete_all_entries(conn, table_name):
    sql = f"DELETE FROM {table_name}"
    cur = conn.cursor()
    cur.execute(sql)

def main_to_delete(tree, table_name):
	database = "pythonsqlite3.db"
    # create a database connection
	conn = return_conn(database)
	with conn:
		confirmation = messagebox.askokcancel("Confirmation","Are you sure you want to delete the selected entry.Press ok to confirm")
		if confirmation == True:
			idx =  tree.item(tree.focus())['text']
			tree.delete(tree.selection())
			delete_entry(conn,idx, table_name)

def main_to_delete_all(tree, table_name):
	database = "pythonsqlite3.db"
    # create a database connection
	conn = return_conn(database)
	with conn:
		confirm = messagebox.askokcancel("Confirmation","Are you sure you want to delete all entries. Press ok to confirm")
		if confirm == True:		
			database = "pythonsqlite3.db"
			for i in tree.get_children():
				tree.delete(i)
			delete_all_entries(conn, table_name)

# updating entries in the database		
def update_profile(conn, profile_data):
	sql = '''UPDATE profile
              SET 'name' = ? ,
                  'age' = ? ,
                  'dob' = ?,
                  'gender' = ?,
                  'hobbies'=?,
                  'career'=?
              '''
	
	cur = conn.cursor()
	cur.execute(sql, profile_data)
	# Check if the update affected any rows
	if (cur.rowcount == 0):
        # If no rows were updated, use INSERT statement
		cur.execute('''
            INSERT INTO profile ('name', 'age', 'dob', 'gender', 'hobbies', 'career')
            VALUES (?, ?, ?, ?, ?, ?)
        ''', profile_data)

	conn.commit()
    		
def update_college(conn, college_entry):
	sql = '''UPDATE college_info
              SET 'name' = ? ,
                  'tuition fees' = ? ,
                  'accomodation cost' = ?,
                  'program' = ?,
                  'competitiveness'=?,
                  'location'=?,
                  'requirements'=?,
                  'document submission deadline'=?,
                  'application deadline'=?
				WHERE IDX = ?
               '''
    
	try:
		cur = conn.cursor()
		idx =  tree.item(tree.focus())['text']
		college_entry += (idx,)
		cur.execute(sql, college_entry)
		tree.item(tree.selection(), text=idx, values=(txt_name.get(),txt_tuition_fees.get(),txt_accomodation_cost.get(),txt_program.get(),txt_rank_sw.get(),txt_location.get(),txt_requirements.get(),txt_doc.get(),txt_app.get()))
	except sqlite3.IntegrityError as e:
		print(f"Error during update: {e}")

def update_activity(conn, activity_entry):

	sql = '''UPDATE extracurricular_activities
              SET 'activity' = ? ,
                  'type' = ? ,
                  'school years' = ?,
                  'years' = ?,
                  'hours per week'=?,
                  'weeks per year'=?,
                  'status'=?,
                  'description'=?
			  WHERE IDX = ?
              '''
	try:	  
		cur = conn.cursor()
		idx_2 =  tree_2.item(tree_2.focus())['text']
		activity_entry += (idx_2,)
		cur.execute(sql, activity_entry)
		tree_2.item(tree_2.selection(),text = idx_2,values =(txt_activity.get(),txt_type.get(),txt_sch_years.get(),txt_years.get(),txt_hrs_per_wk.get(),txt_wks_per_yr.get(),txt_status.get(),general_description.get("1.0","end-1c")))#,description.get("1.0", "end-1c")))
	except sqlite3.IntegrityError as e:
		print(f"Error during update: {e}")

def main_update_profile():
	database = "pythonsqlite3.db"
 
    # create a database connection
	conn = return_conn(database)
	
	with conn:
    # create a database connection    		
		confirm = messagebox.askokcancel("Update","Press ok if you want to make the following changes to your profile.")
		if confirm == True:
			update_profile(conn,(txt_profile_name.get(),txt_age.get(),txt_dob.get(),var_chk.get(),hobbies.get("1.0", "end-1c"),career.get("1.0", "end-1c")))
			messagebox.showinfo("Update","Saved")
		if confirm == False:
			txt_profile_name.delete(0,"end")
			txt_dob.delete(0,"end")
			txt_age.delete(0,"end")
			hobbies.delete(1.0,"end")
			career.delete(1.0,"end")
			read_profile()
					
def main_update_college_info():
	database = "pythonsqlite3.db"
    # create a database connection
	conn = return_conn(database)
	with conn:
		if txt_name.get() == "" or txt_tuition_fees.get() == "" or txt_accomodation_cost.get() == "" or txt_program.get() == "" or txt_rank_sw == "" or txt_location.get() == "" or txt_requirements.get() == "" or txt_doc.get() == "" or txt_app.get() == "":
			messagebox.showerror("Error","Please fill in necessary entries(marked by *)")
		else:
			confirm = messagebox.askokcancel("Update","Press OK to update the entry into the database otherwise press cancel to return.")
			if confirm == True:
				update_college(conn,(txt_name.get(),txt_tuition_fees.get(),txt_accomodation_cost.get(),txt_program.get(),txt_rank_sw.get(),txt_location.get(),txt_requirements.get(),txt_doc.get(),txt_app.get()))
				messagebox.showinfo("Update","Successful")
        
def main_update_activtiy():
	database = "pythonsqlite3.db"
    # create a database connection
	conn = return_conn(database)
	with conn:
		if txt_activity.get() == "" or txt_type.get() == "" or txt_sch_years.get() == "" or txt_years == "" or txt_hrs_per_wk.get() == "" or txt_wks_per_yr.get() == "" or txt_status.get() == "":
			messagebox.showinfo("Error","Please fill in necessary entries(marked by *)")
		else:
			confirm = messagebox.askokcancel("Update","Press OK to update the entry into the database otherwise press cancel to return.")			
			if confirm == True:
				update_activity(conn,(txt_activity.get(),txt_type.get(),txt_sch_years.get(),txt_years.get(),txt_hrs_per_wk.get(),txt_wks_per_yr.get(),txt_status.get(),general_description.get("1.0", "end-1c")))#,description.get("1.0", "end-1c")))
				messagebox.showinfo("Update","Successful")

# Save button for Profile page 1
btn_save = ttk.Button(page1, text = "Save", command = main_update_profile)
btn_save.grid(row =13, column = 1)

# Buttons for college applicatons deadline page 2
btn_insertion = ttk.Button(lblfr_college,text = "Add to Database",command =main_to_insert_in_table)
btn_insertion.grid(row = 10, column = 0)
btn_delete_all = ttk.Button(lblfr_college,text ="Delete All",command = lambda: main_to_delete_all(tree, "college_info"))
btn_delete_all.grid(row = 10, column = 1)
btn_delete = ttk.Button(lblfr_college,text ="Delete",command = lambda: main_to_delete(tree, "college_info"))
btn_delete.grid(row = 10, column = 2)
btn_update = ttk.Button(lblfr_college,text = "Update",command = main_update_college_info)
btn_update.grid(row = 10, column = 3)

# Buttons for extracurricular activities page 3
btn_insertion_2 = ttk.Button(lblfr_activity,text = "Add to Database",command =main_to_insert_in_table_2)
btn_insertion_2.grid(row = 8, column = 0)
btn_delete_all_2 = ttk.Button(lblfr_activity,text ="Delete All",command = lambda: main_to_delete_all(tree_2, "extracurricular_activities"))
btn_delete_all_2.grid(row = 8, column = 5)
btn_delete_2 = ttk.Button(lblfr_activity,text ="Delete",command = lambda: main_to_delete(tree_2, "extracurricular_activities"))
btn_delete_2.grid(row = 8, column = 6)
btn_update_2 = ttk.Button(lblfr_activity,text = "Update",command = main_update_activtiy)
btn_update_2.grid(row = 8, column = 7)
    

if __name__ == '__main__':
	create_connection("pythonsqlite3.db")
	main_to_create_table()
	read_profile()
	read_from_college_database()
	read_from_activity_database()
	tree.bind('<<TreeviewSelect>>', selected_college_entry)
	tree_2.bind('<<TreeviewSelect>>', selected_activty_entry)

	root.mainloop()
