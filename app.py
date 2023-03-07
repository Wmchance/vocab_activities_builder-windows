import tkinter
from tkinter import *

from env_variable import OPENAI_API_KEY
from word_lists import *
from build_chosen_word_str import *

from fill_in_the_blank_individual_sentences import *
from fill_in_the_blank_short_story import *
from questions_with_vocab_answers import *
from scrambled_sentences import *
from words_to_picture import *

class WS_builder:
    def __init__(self, master):
        self.master = master
        self.mainframe = tkinter.Frame(self.master, bg='white')
        self.mainframe.pack(fill=tkinter.BOTH, expand=True)

        # build all the parts of the apps display
        self.build_grid()
        self.build_banner()
        self.build_instructions()
        self.build_listbox_labels()
        self.build_listboxes()
        self.build_file_name()
        self.build_create_section()
        self.vars()
        self.display_row()
    
    def build_grid(self):
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=0)
        self.mainframe.rowconfigure(1, weight=0)
        self.mainframe.rowconfigure(2, weight=0)
        self.mainframe.rowconfigure(3, weight=0)
        self.mainframe.rowconfigure(4, weight=0)
        self.mainframe.rowconfigure(5, weight=0)
        self.mainframe.rowconfigure(6, weight=0)

    # Not needed now, but will leave it incase vars are needed later
    def vars(self):
        self.unit_var = StringVar()
        self.lesson_var = StringVar()
        self.activity_var = StringVar()
    
    def build_banner(self):
        # sets what the banner displays 
        banner = tkinter.Label(
            self.mainframe, # says the frame to which it belongs, the mainframe in this case
            bg='blue',
            fg='white',
            text='STeP Worksheet Builder',
            font=('Helvetica, 24')
        )
        # sets the location of the banner in the mainframe & how it is positioned. 
        banner.grid(
            row=0, column=0,
            sticky='ew', # Stuck to the east 'e' & west 'w' sides of the screen
            padx=10, pady=5 # sets the padding
        )

    def build_instructions(self):
        # sets what the instructions area displays 
        instructions = tkinter.Label(
            self.mainframe, # says the frame to which it belongs, the mainframe in this case
            bg='white',
            fg='black',
            text='''
                1. Pick the vocab set you want to use by selecting the unit & lesson
                2. Pick the activity you want to create by selecting the name 
                3. Enter a name for the file you are creating 
                4. Click 'Create' to make your worksheet
                5. You can add additional activities to the worksheet by repeating these steps while keeping the file name the same.
            ''',
            font=('Helvetica, 15'),
            justify= 'left'
        )
        # sets the location of the instructions in the mainframe & how it is positioned. 
        instructions.grid(
            row=1, column=0,
            sticky='w', # Stuck to the east 'e' & west 'w' sides of the screen
            padx=5, pady=5 # sets the padding
        )

    def build_listbox_labels(self):
        # adds a new frame for the listbox labels
        listbox_labels_frame = tkinter.Frame(self.mainframe)
        # sets the location of where the new grid will go within the existing frame(mainframe)
        listbox_labels_frame.grid(row=2, column=0, sticky='nsew', padx=5, pady=5)
        # configure the grid for the new frame - 3 columns in the 3rd row of the mainframe
        listbox_labels_frame.columnconfigure(0, weight=1)
        listbox_labels_frame.columnconfigure(1, weight=1)
        listbox_labels_frame.columnconfigure(2, weight=1)

        # make a Unit-select listbox label
        self.unit_select_label = tkinter.Label(
            listbox_labels_frame, # says the frame to which it belongs, the listbox_labels_frame in this case
            bg='blue',
            fg='white',
            text='Unit',
            font=('Helvetica, 15')
        )

        # make a Lesson-select listbox label
        self.lesson_select_label = tkinter.Label(
            listbox_labels_frame, # says the frame to which it belongs, the listbox_labels_frame in this case
            bg='blue',
            fg='white',
            text='Lesson',
            font=('Helvetica, 15')
        )

        # make a Activity-select listbox label
        self.activity_select_label = tkinter.Label(
            listbox_labels_frame, # says the frame to which it belongs, the listbox_labels_frame in this case
            bg='blue',
            fg='white',
            text='Activity',
            font=('Helvetica, 15')
        )

        # set grid location (within listboxes_frame) of listboxes
        self.unit_select_label.grid(row=0, column=0, sticky='ew')
        self.lesson_select_label.grid(row=0, column=1, sticky='ew')
        self.activity_select_label.grid(row=0, column=2, sticky='ew')


    def build_listboxes(self):
        # adds a new frame for the listboxes
        listboxes_frame = tkinter.Frame(self.mainframe)
        # sets the location of where the new grid will go within the existing frame(mainframe)
        listboxes_frame.grid(row=3, column=0, sticky='nsew', padx=5, pady=5)
        # configure the grid for the new frame - 3 columns in the 3rd row of the mainframe
        listboxes_frame.columnconfigure(0, weight=1)
        listboxes_frame.columnconfigure(1, weight=1)
        listboxes_frame.columnconfigure(2, weight=1)

        # make a Unit-select listbox
        self.unit_listbox = tkinter.Listbox(
            listboxes_frame, # belongs to button_frame
            bg='white',
            fg='black',
            exportselection=False, # allows for 1 selection from each listbox to be highlighted
            height=5
        )
        self.unit_listbox.insert(1, " Unit 1")
        self.unit_listbox.insert(2, " Unit 2")
        self.unit_listbox.insert(3, " Unit 3")
        self.unit_listbox.insert(4, " Unit 4")
        self.unit_listbox.insert(5, " Unit 5")
        self.unit_listbox.insert(6, " Unit 6")
        self.unit_listbox.insert(7, " Unit 7")
        self.unit_listbox.insert(8, " Unit 8")
        self.unit_listbox.insert(9, " Unit 9")
        self.unit_listbox.insert(10, " Unit 10")
        self.unit_listbox.insert(11, " Unit 11")
        self.unit_listbox.insert(12, " Unit 12")

        # make a Lesson-select listbox
        self.lesson_listbox = tkinter.Listbox(
            listboxes_frame, # belongs to button_frame
            bg='white',
            fg='black',
            exportselection=False, # allows for 1 selection from each listbox to be highlighted
            height=5

        )
        self.lesson_listbox.insert(1, " Lesson 1")
        self.lesson_listbox.insert(2, " Lesson 2")
        self.lesson_listbox.insert(3, " Lesson 3")
        self.lesson_listbox.insert(4, " Lesson 4")

        # make a Activity-select listbox
        self.activity_listbox = tkinter.Listbox(
            listboxes_frame, # belongs to button_frame
            bg='white',
            fg='black',
            exportselection=False, # allows for 1 selection from each listbox to be highlighted
            height=5
        )
        self.activity_listbox.insert(1, " Fill-in-the-blank: Sentences")
        self.activity_listbox.insert(1, " Fill-in-the-blank: Short Story")
        self.activity_listbox.insert(1, " Answer Questions with Vocab")
        self.activity_listbox.insert(1, " Scrambled Sentences")
        self.activity_listbox.insert(1, " Draw pictures based on words")

        # set grid location (within listboxes_frame) of listboxes
        self.unit_listbox.grid(row=0, column=0, sticky='ew')
        self.lesson_listbox.grid(row=0, column=1, sticky='ew')
        self.activity_listbox.grid(row=0, column=2, sticky='ew')

    def build_file_name(self):
        # adds a new frame for the create labels
        file_name_frame = tkinter.Frame(self.mainframe)
        # sets the location of where the new grid will go within the existing frame(mainframe)
        file_name_frame.grid(row=4, column=0, sticky='nsew', padx=5, pady=5)
        # configure the grid for the new frame - 3 columns in the 3rd row of the mainframe
        file_name_frame.columnconfigure(0, weight=1)
        file_name_frame.columnconfigure(1, weight=1)

        # make a file name label
        self.file_name_label = tkinter.Label(
            file_name_frame, # says the frame to which it belongs, the listbox_labels_frame in this case
            text='File Name:',
            font=('Helvetica, 15')
        )

        # make an entry field for file name entry
        self.create_entry = tkinter.Entry(
            file_name_frame, # belongs to create_frame
            # textvariable : In order to be able to retrieve the current text from your entry widget, you must set this option to an instance of the StringVar class.
            # https://www.geeksforgeeks.org/python-tkinter-entry-widget/
        )

        # set grid location within create_labels_frame
        self.file_name_label.grid(row=0, column=0, sticky='ew')
        self.create_entry.grid(row=0, column=1, sticky='ew')

    
    def build_create_section(self):
        # adds a new frame for the create section
        create_frame = tkinter.Frame(self.mainframe)
        # sets the location of where the new grid will go within the existing frame(mainframe)
        create_frame.grid(row=5, column=0, sticky='nsew', padx=5, pady=5)
        # configure the grid for the new frame - 2 columns in the 4th row of the mainframe
        create_frame.columnconfigure(0, weight=1)
        create_frame.columnconfigure(1, weight=1)
        create_frame.columnconfigure(2, weight=1)
        
        # make a create button
        self.create_button = tkinter.Button(
            create_frame, # belongs to create_frame
            text='Create',
            font=('Helvetica, 20'),
            command= self.build_selected
            # command=self.call_creation_function
        )

        # set grid location (within create_frame) of button & entry
        self.create_button.grid(row=0, column=1, sticky='ew')
        # self.create_entry.grid(row=0, column=0, sticky='ew')

    # Temp row display to check vars are coming through correctly - TO BE DELETED
    def display_row(self):
        # sets what the display area displays 
        disp = tkinter.Label(
            self.mainframe, # says the frame to which it belongs, the mainframe in this case
            bg='white',
            fg='black',
            textvariable= self.lesson_var,
            font=('Helvetica, 15'),
            justify= 'left'
        )
        # sets the location of the instructions in the mainframe & how it is positioned. 
        disp.grid(
            row=6, column=0,
            sticky='w', # Stuck to the east 'e' & west 'w' sides of the screen
            padx=5, pady=5 # sets the padding
        )

    def build_selected(self):
        # Unit selection var
        unit_itm = self.unit_listbox.get(self.unit_listbox.curselection())
        unit_num = unit_itm.split(" ")[2]
        self.unit_var.set(unit_num)

        # Lesson selection var
        lesson_itm = self.lesson_listbox.get(self.lesson_listbox.curselection())
        lesson_num = lesson_itm.split(" ")[2]
        self.lesson_var.set(f'Lesson {lesson_num} activity created')

        # Activity selection var
        activity_itm = self.activity_listbox.get(self.activity_listbox.curselection())
        self.activity_var.set(activity_itm)

        # get word str for selected unit/lesson
        chosen_word_str = build_chosen_word_str(unit_num, lesson_num)

        # get function with prompt needed for chosen activity
        def selected_activity_build(activity_chosen):
            if activity_chosen == ' Fill-in-the-blank: Sentences':
                fill_in_the_blank_individual_sentences(OPENAI_API_KEY, chosen_word_str)
            elif activity_chosen == ' Fill-in-the-blank: Short Story':
                fill_in_the_blank_short_story(OPENAI_API_KEY, chosen_word_str)
            elif activity_chosen == ' Answer Questions with Vocab':
                questions_with_vocab_answers(OPENAI_API_KEY, chosen_word_str)
            elif activity_chosen == ' Scrambled Sentences':
                scrambled_sentences(OPENAI_API_KEY, chosen_word_str)
            elif activity_chosen == ' Draw pictures based on words':
                words_to_picture(OPENAI_API_KEY, chosen_word_str)

        # call function that makes API call with chosen word str & activity
        selected_activity_build(activity_itm)

    # def call_creation_function(self):
    #     fill_in_the_blank_individual_sentences(OPENAI_API_KEY, (', '.join(l2_u1_l1_list)))


if __name__ == '__main__':
    
    csv_from_book = 'SYM_2_WordList.csv'
    generate_word_lists(csv_from_book)

    # activity = fill_in_the_blank_individual_sentences(OPENAI_API_KEY, (', '.join(l2_u1_l1_list)))
    # print(l2_u1_l4_list) 

    root = tkinter.Tk()
    WS_builder(root)

    root.mainloop()