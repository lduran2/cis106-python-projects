'''
./project12-miles-per-gallon-calculator/miles_per_gallon_calculator.py
An event-driven GUI program implementing a miles per gallon calculator
with a 'Calculate MPG' button.

By     : Leomar Duran <https://github.com/lduran2>
When   : 2020-12-05t20:54
Where  : Community College of Philadelphia
For    : CIS 106/Introduction to Programming
Version: 1.1

Changelog:
    v1.1 - 2020-12-05t20:54
        Added entries, buttons.
        Split creating frames and labels.
        Renamed to use underscores, instead of hyphens in names.
    
    v1.0 - 2020-12-05t16:39
        Created the GUI with just the labels.
'''

# libraries
import tkinter as tk    # for GUI

class MilesPerGallonGUI:
    '''
    A GUI of a Miles Per Gallon calculator.
    '''

    # tuple of keys for widgets in the main window
    ( \
        I_FRM_GALLONS, I_FRM_MILES, I_FRM_SUBMIT,\
        I_LBL_GALLONS, I_LBL_MILES,\
        I_ENT_GALLONS, I_ENT_MILES,\
        I_BTN_SUBMIT,\
        I_FINISH\
    ) = tuple(range(0,9))

    # index of first of each class of widget
    I_FRAME_START   = I_FRM_GALLONS
    I_LABEL_START   = I_LBL_GALLONS
    I_ENTRY_START   = I_ENT_GALLONS
    I_BUTTON_START  = I_BTN_SUBMIT

    # range of each class of widget
    RNG_FRAMES  = range(I_FRAME_START,  I_LABEL_START)
    RNG_LABELS  = range(I_LABEL_START,  I_ENTRY_START)
    RNG_ENTRIES = range(I_ENTRY_START,  I_BUTTON_START)
    RNG_BUTTONS = range(I_BUTTON_START, I_FINISH)

    # index of first of widget subclasses
    I_BUTTON_FRAME_START = I_FRM_SUBMIT

    # label strings used in GUI
    STR_LABELS = (
        'Size of gas tank [gal]:',\
        'Most one can drive [mi]:',\
    )

    # button strings used in GUI
    STR_BUTTONS = (
        'Calculate MPG!',
    )

    # entry width
    ENTRY_WIDTH = 4

    def __init__(self):
        '''
        Creates the GUI.
        '''

        # tuple of commands
        COMMANDS = ( self.calcMPG, )

        # list of widgets in the main window
        widgets = []
        # list of sides to pack widgets to
        sides = []

        # create the main window
        win_main = tk.Tk()

        # create the frames (stop at the labels)
        for k in self.RNG_FRAMES:
            # create the frame, and add it to widgets
            widgets.append(tk.Frame(win_main))
            # top pack all frames
            sides.append('top')
        # end for k in self.RNG_FRAMES

        # create the labels
        for k in self.RNG_LABELS:
            # choose the correct label
            i_label = (k - self.I_LABEL_START)
            # choose the correct frame
            i_frame = (i_label + self.I_FRAME_START)
            # get the label string
            str_label = self.STR_LABELS[i_label]
            # create the label
            label = tk.Label(widgets[i_frame], text=str_label)
            # add the label to widgets
            widgets.append(label)
            # left pack all labels
            sides.append('left')
        # end for k in self.RNG_LABELS

        # create the entries
        for k in self.RNG_ENTRIES:
            # choose the correct frame
            i_frame = (k - self.I_ENTRY_START + self.I_FRAME_START)
            # create the entry
            entry = tk.Entry(widgets[i_frame], width=self.ENTRY_WIDTH)
            # add the entry to widgets
            widgets.append(entry)
            # right pack all entries
            sides.append('right')
        # end for k in self.RNG_ENTRIES

        # create the buttons
        for k in self.RNG_BUTTONS:
            # choose the correct command and button string
            i_command = (k - self.I_BUTTON_START)
            # choose the correct frame
            i_frame = (i_command + self.I_BUTTON_FRAME_START)
            # create the button
            button = tk.Button(widgets[i_frame],\
                text=self.STR_BUTTONS[i_command],\
                command=COMMANDS[i_command]\
            )
            # add the button to widgets
            widgets.append(button)
            # left back the buttons
            sides.append('left')
        # end for k in self.RNG_BUTTONS

        # pack all widgets in the widgets list
        for k in range(len(widgets)):
            widgets[k].pack(side=sides[k])
        # end for widget in widgets

        # print status to the command line
        print('Running main window loop . . .')
        # run the main window loop
        win_main.mainloop();

        # finish
        print('Done.')
    # end def __init__(self)

    def calcMPG(self):
        return
    # end def calcMPG(self)
# end class MilesPerGallonGUI

# create the gui and run the main window loop
mpg_gui = MilesPerGallonGUI()
