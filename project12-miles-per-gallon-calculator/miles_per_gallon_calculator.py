'''
./project12-miles-per-gallon-calculator/miles_per_gallon_calculator.py
An event-driven GUI program implementing a miles per gallon calculator
with a 'Calculate MPG' button.

By     : Leomar Duran <https://github.com/lduran2>
When   : 2020-12-06t04:11
Where  : Community College of Philadelphia
For    : CIS 106/Introduction to Programming
Version: 1.4

Changelog:
    v1.4 - 2020-12-06t04:11
        Changed to use labels for output.

    v1.3 - 2020-12-05t22:29
        Implemented `calcMPG` assuming good input.

    v1.2 - 2020-12-05t21:02
        Made class constants private and moved to bottom of class.

    v1.1 - 2020-12-05t20:54
        Added entries, buttons.
        Split creating frames and labels.
        Renamed to use underscores, instead of hyphens.
    
    v1.0 - 2020-12-05t16:39
        Created the GUI with just the labels.
'''

# libraries
import tkinter as tk                # for GUI
import tkinter.messagebox as msg    # for information dialog boxes

class MilesPerGallonGUI:
    '''
    A GUI of a Miles Per Gallon calculator.
    '''

    def __init__(self):
        '''
        Creates the GUI.
        '''

        # tuple of commands for the buttons
        COMMANDS = ( self.calcMPG, )

        # list of widgets in the main window
        widgets = []
        # list of sides to pack widgets to
        sides = []
        # list of StringVar objects
        string_vars = []

        # create the main window
        win_main = tk.Tk()
        # provide width to the window
        widgets.append(tk.Canvas(win_main,
            width=self.__MAIN_WINDOW_WIDTH, height=0))
        # pack to the top
        sides.append('top')

        # set up the frames (stop at the labels)
        for k in self.__RNG_FRAMES:
            # create the frame, and add it to widgets
            widgets.append(tk.Frame(win_main))
            # top pack all frames
            sides.append('top')
        # end for k in self.__RNG_FRAMES

        # set up the labels
        for k in self.__RNG_LABELS:
            # choose the correct label
            i_label = (k - self.__I_LABEL_START)
            # choose the correct frame
            i_frame = (i_label + self.__I_FRAME_START)

            # get the label string
            str_label = self.__STR_LABELS[i_label]
            # create the label
            label = tk.Label(widgets[i_frame], text=str_label)
            # add the label to widgets
            widgets.append(label)
            # left pack all labels
            sides.append('left')
        # end for k in self.__RNG_LABELS

        # set up the message label
        # create its StringVar
        stv_message = tk.StringVar()
        widgets[self.__I_LBL_MESSAGE]['textvariable'] = stv_message

        # set up the entries
        for k in self.__RNG_ENTRIES:
            # choose the correct frame
            i_frame = (k - self.__I_ENTRY_START + self.__I_FRAME_START)
            # create the entry
            entry = tk.Entry(widgets[i_frame], width=self.__ENTRY_WIDTH)
            # add the entry to widgets
            widgets.append(entry)
            # right pack all entries
            sides.append('right')
        # end for k in self.__RNG_ENTRIES

        # set up the output fields
        for k in self.__RNG_FIELDS:
            i_frame = (k
                - self.__I_FIELD_START + self.__I_FIELD_FRAME_START)
            # create the related StringVar
            string_var = tk.StringVar()
            # create the output field
            field = tk.Label(widgets[i_frame],
                textvariable=string_var,
                borderwidth=widgets[self.__I_ENTRY_START]['borderwidth'],
                relief=widgets[self.__I_ENTRY_START]['relief']
            )
            # add the StringVar to its list
            string_vars.append(string_var)
            # add the output field to widgets
            widgets.append(field)
            # left pack all output fields
            sides.append('left')
        # end for k in self.__RNG_FIELDS

        # add the get methods for gallons, miles to self
        self.__get_gallons  = widgets[self.__I_ENT_GALLONS].get
        self.__get_miles    = widgets[self.__I_ENT_MILES].get
        # add the set methods for message, MPG to self
        self.__set_message  = stv_message.set
        self.__set_mpg      = string_vars[
            self.__I_FLD_MPG - self.__I_FIELD_START].set

        # set up the buttons
        for k in self.__RNG_BUTTONS:
            # choose the correct command and button string
            i_command = (k - self.__I_BUTTON_START)
            # choose the correct frame
            i_frame = (i_command + self.__I_BUTTON_FRAME_START)
            # create the button
            button = tk.Button(widgets[i_frame],
                text=self.__STR_BUTTONS[i_command],
                command=COMMANDS[i_command]
            )
            # add the button to widgets
            widgets.append(button)
            # left back the buttons
            sides.append('left')
        # end for k in self.__RNG_BUTTONS

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
        '''
        Calculates the miles per gallon.
        '''
        # get the gallons
        try:
            gallons = float(self.__get_gallons())
        except ValueError: # handle not floatable
            #msg.showinfo('Response',
            #    'The size of the gas tank must be a number.', icon='error'
            #)
            self.__set_message(
                '️✖ The size of the gas tank must be a number.')
            return
        # end except ValueError

        # get the miles
        try:
            miles = float(self.__get_miles())
        except ValueError: # handle not floatable
            #msg.showinfo('Response',
            #    'The most one can drive must be a number.', icon='error'
            #)
            self.__set_message(
                '✖️ The most one can drive must be a number.')
            return
        # end except ValueError

        # gallons must be positive,
        # but reject < 0.001 to avoid equality comparison of floats
        if (gallons < 0.001):
            #msg.showinfo('Response',
            #    'The size of the gas tank must be positive.', icon='error'
            #)
            self.__set_message(
                '✖ The size of the gas tank must be positive.')
            return
        # end if (gallons < 0.001)

        # miles must be nonnegative
        elif (miles < 0.0):
            #msg.showinfo('Response',
            #    'The most one can drive must be nonnegative.', icon='error'
            #)
            self.__set_message(
                '✖ The most one can drive must be nonnegative.')
            return
        # end if (miles < 0.0)

        # empty the message
        self.__set_message('')
        # calculate the miles per gallon
        mpg = (miles / gallons)
        # set up the result message
        #message = ('Miles per gallon: ' + format(mpg, self.__MPG_FORMAT))
        # display the result message
        self.__set_mpg(format(mpg, self.__MPG_FORMAT))
        #msg.showinfo('Response', message)
    # end def calcMPG(self)


    ##################################################################
    # CONSTANTS

    # width of the main window
    __MAIN_WINDOW_WIDTH = 350

    # tuple of keys for widgets in the main window
    ( 
        __I_CANVAS,
        __I_FRM_GALLONS, __I_FRM_MILES, __I_FRM_MESSAGE, __I_FRM_MPG,
            __I_FRM_SUBMIT,
        __I_LBL_GALLONS, __I_LBL_MILES, __I_LBL_MESSAGE, __I_LBL_MPG,
        __I_ENT_GALLONS, __I_ENT_MILES,
                                                         __I_FLD_MPG,
            __I_BTN_SUBMIT,
        __I_FINISH
    ) = tuple(range(0,15))

    # index of first of each class of widget
    __I_FRAME_START   = __I_FRM_GALLONS
    __I_LABEL_START   = __I_LBL_GALLONS
    __I_ENTRY_START   = __I_ENT_GALLONS
    __I_FIELD_START   = __I_FLD_MPG
    __I_BUTTON_START  = __I_BTN_SUBMIT

    # index of first of widget subclasses
    __I_FIELD_FRAME_START   = __I_FRM_MPG
    __I_BUTTON_FRAME_START  = __I_FRM_SUBMIT

    # range of each class of widget
    __RNG_FRAMES  = range(__I_FRAME_START,  __I_LABEL_START)
    __RNG_LABELS  = range(__I_LABEL_START,  __I_ENTRY_START)
    __RNG_ENTRIES = range(__I_ENTRY_START,  __I_FIELD_START)
    __RNG_FIELDS  = range(__I_FIELD_START,  __I_BUTTON_START)
    __RNG_BUTTONS = range(__I_BUTTON_START, __I_FINISH)

    # label strings used in GUI
    __STR_LABELS = (
        'Size of gas tank [gal]:',
        'Most one can drive [mi]:',
        '',
        'Miles per gallon:'
    )

    # button strings used in GUI
    __STR_BUTTONS = (
        'Calculate MPG!',
    )

    # number of characters in each entry widgets
    __ENTRY_WIDTH = 4

    # result format
    __MPG_FORMAT = '.1f'

# end class MilesPerGallonGUI

# create the gui and run the main window loop
mpg_gui = MilesPerGallonGUI()
