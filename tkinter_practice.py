import tkinter

# Set a constant (for the amount of time for the counter - 25min in seconds) which will be used in the tkinter app
DEFAULT_GAP = 60 * 25 

class Pymodoro:
    def __init__(self, master):
        self.master = master
        self.mainframe = tkinter.Frame(self.master, bg='white')
        self.mainframe.pack(fill=tkinter.BOTH, expand=True)

        self.timer_text = tkinter.StringVar() # Set a variable to hold the timer display number
        self.timer_text.trace('w', self.build_timer) # tells the text to go do something when it gets updated. 'w' tells it to take action when it's written to & the action it to call self.build_timer
        self.time_left = tkinter.IntVar() # Set an int var to hold the time left
        self.time_left.set(DEFAULT_GAP) # set the starting time left based on the external constant
        self.running = False # set the initial state of the timer to not be running

        # build all the parts of the apps display
        self.build_grid()
        self.build_banner()
        self.build_buttons()
        self.build_timer()

        # after everything is built, run the update function
        self.update()

    def build_grid(self):
        self.mainframe.columnconfigure(0, weight=1) #sets one column for the frame(mainframe) & lets it expand
        # sets 3 rows for mainframe. rows 0 & 2  don't expand, row 1 does
        self.mainframe.rowconfigure(0, weight=0) 
        self.mainframe.rowconfigure(1, weight=1)
        self.mainframe.rowconfigure(2, weight=0)

    def build_banner(self):
        # sets what the banner displays 
        banner = tkinter.Label(
            self.mainframe, # says the frame to which it belongs, the mainframe in this case
            bg='red',
            fg='white',
            text='Pymodoro',
            font=('Helvetica, 24')
        )
        # sets the location of the banner in the mainframe & how it is positioned. 
        banner.grid(
            row=0, column=0,
            sticky='ew', # Stuck to the east 'e' & west 'w' sides of the screen
            padx=3, pady=10 # sets the padding
        )

    def build_buttons(self):
        # adds a new frame for the buttons
        buttons_frame = tkinter.Frame(self.mainframe)
        # sets the location of where the new grid will go within the existing frame(mainframe)
        buttons_frame.grid(row=2, column=0, sticky='nsew', padx=3, pady=10)
        # configure the grid for the new frame - 2 columns in the 3rd row of the mainframe
        buttons_frame.columnconfigure(0, weight=1)
        buttons_frame.columnconfigure(1, weight=1)

        # make a start button
        self.start_button = tkinter.Button(
            buttons_frame, # belongs to button_frame
            text='Start',
            command=self.start_timer
        )
        # make a stop button
        self.stop_button = tkinter.Button(
            buttons_frame, # belongs to button_frame
            text='Stop',
            command=self.stop_timer
        )
        # set grid location (within button_frame) of buttons
        self.start_button.grid(row=0, column=0, sticky='ew')
        self.stop_button.grid(row=0, column=1, sticky='ew')

        # set the initial state of the stop button to be disabled
        self.stop_button.config(state=tkinter.DISABLED)

    # adding the ability to accept args is necessary since this will be called in different places & and, therefor Python requires it
    def build_timer(self, *args):
        timer = tkinter.Label(
            self.mainframe,
            text=self.timer_text.get(), # gets the stored value of the variable set in the __init__ function
            font=('Helvetica', 36)
        )
        timer.grid(row=1, column=0, sticky='nsew')

    # create method to give the timer a command to start
    def start_timer(self):
        self.time_left.set(DEFAULT_GAP) # Since this is set here, it can be removed from the __init__ function 
        self.running = True # set running to true once the start button is clicked
        # enable stop button & disable start button when the start button is pressed
        self.stop_button.config(state=tkinter.NORMAL)
        self.start_button.config(state=tkinter.DISABLED)

    # create method to give the timer a command to stop
    def stop_timer(self):
        self.running = False # set running to False once the stop button is clicked
        # enable start button & disable stop button when the stop button is pressed
        self.stop_button.config(state=tkinter.DISABLED)
        self.start_button.config(state=tkinter.NORMAL)

    def minutes_seconds(self, seconds):
        return int(seconds/60), int(seconds%60)
    
    def update(self):
        time_left = self.time_left.get()

        # checks if running is true & time_left isn't 0. If so, 1s is removed from time_left, else the stop_timer() is called
        # remaining time is shown with timer_text 
        if self.running and time_left:
            minutes, seconds = self.minutes_seconds(time_left)
            self.timer_text.set(
                '{:0>2}:{:0>2}'.format(minutes, seconds)
            )
            self.time_left.set(time_left-1)
        else:
            minutes, seconds = self.minutes_seconds(DEFAULT_GAP)
            self.timer_text.set(
                "{:0>2}:{:0>2}".format(minutes, seconds)
            )
            self.stop_timer()

        self.master.after(1000, self.update) # says to run the update function after every 1000ms(1 second)
    

if __name__ == '__main__':
    root = tkinter.Tk()
    Pymodoro(root)

    root.mainloop()