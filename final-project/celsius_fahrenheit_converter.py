'''
./final-project/celsius_fahrenheit_converter.py
A GUI program implementing a calculator that converts between Celsius
and Fahrenheit.

By     : Leomar Duran <https://github.com/lduran2>
When   : 2020-12-10t21:43
Where  : Community College of Philadelphia
For    : CIS 106/Introduction to Programming
Version: 1.1

Changelog:
    v1.1 - 2020-12-10t21:43
        Implemented 'Convert to Celsius!'

    v1.0 - 2020-12-10t19:40
        Implemented 'Convert to Fahrenheit!'
'''

# libraries
import tkinter as tk                # for GUI

class CelsiusFahrenheitConverter:
    '''
    A GUI of a Celsius/Fahrenheit Temperature Converter.
    '''

    def __init__(self):
        '''
        Creates the GUI.
        '''

        # tuple of commands for the buttons
        COMMANDS = ( self.convertToFahrenheit, self.convertToCelsius )

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

        # add the get method for input temperature to self
        self.__get_temp_in  = widgets[self.__I_ENT_TEMP_IN].get
        # add the set methods for message, output temperature to self
        self.__set_message  = stv_message.set
        self.__set_temp_in      = string_vars[
            self.__I_FLD_TEMP_OUT - self.__I_FIELD_START].set

        # set up the buttons
        for k in self.__RNG_BUTTONS:
            # choose the correct command and button string
            i_command = (k - self.__I_BUTTON_START)
            # create the button
            button = tk.Button(widgets[self.__I_BUTTON_FRAME_START],
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
        print('Celsius/Fahrenheit Converter:', end=' ')
        print('Running main window loop . . .')
        # run the main window loop
        win_main.mainloop();

        # finish
        print('Done.')
    # end def __init__(self)

    def convertToFahrenheit(self):
        '''
        Converts the temperature to Fahrenheit.
        '''
        # get the input temperature
        temp_in = self.validateTemp()
        if (temp_in == None):
            return
        #

        # empty the message
        self.__set_message('')
        # calculate the fahrenheit temperature
        C = temp_in
        F = (((9.0 * C)/5.0) + 32.0)
        # display the result message
        self.__set_temp_in(self.__FAHRENHEIT_FORMAT%(F))
        #msg.showinfo('Response', message)
    # end def convertToFahrenheit(self)


    def convertToCelsius(self):
        '''
        Converts the temperature to Celsius.
        '''
        # get the input temperature
        temp_in = self.validateTemp()
        if (temp_in == None):
            return
        #

        # empty the message
        self.__set_message('')
        # calculate the celsius temperature
        F = temp_in
        C = ((5.0*(F - 32.0))/9.0)
        # display the result message
        self.__set_temp_in(self.__CELSIUS_FORMAT%(C))
        #msg.showinfo('Response', message)
    # end def convertToCelsius(self)

    def validateTemp(self):
        '''
        Validates the input temperature.
        @returns
            the input temperature if valid
            `None` otherwise
        '''
        try:
            temp_in = float(self.__get_temp_in())
        except ValueError: # handle not floatable
            self.__set_message(
                '️✖ The input temperature must be a number.')
            return None
        # end except ValueError
        return temp_in
    # end def validate_temp(self)


    ##################################################################
    # CONSTANTS

    # width of the main window
    __MAIN_WINDOW_WIDTH = 300

    # tuple of keys for widgets in the main window
    ( 
        __I_CANVAS,
        __I_FRM_TEMP_IN, __I_FRM_MESSAGE, __I_FRM_TEMP_OUT, __I_FRM_SUBMIT,
        __I_LBL_TEMP_IN, __I_LBL_MESSAGE, __I_LBL_TEMP_OUT,
        __I_ENT_TEMP_IN, 
                                          __I_FLD_TEMP_OUT,
            __I_BTN_FAHRENHEIT, __I_BTN_CELSIUS,
        __I_FINISH
    ) = tuple(range(0,13))

    # index of first of each class of widget
    __I_FRAME_START   = __I_FRM_TEMP_IN
    __I_LABEL_START   = __I_LBL_TEMP_IN
    __I_ENTRY_START   = __I_ENT_TEMP_IN
    __I_FIELD_START   = __I_FLD_TEMP_OUT
    __I_BUTTON_START  = __I_BTN_FAHRENHEIT

    # index of first of widget subclasses
    __I_FIELD_FRAME_START   = __I_FRM_TEMP_OUT
    __I_BUTTON_FRAME_START  = __I_FRM_SUBMIT

    # range of each class of widget
    __RNG_FRAMES  = range(__I_FRAME_START,  __I_LABEL_START)
    __RNG_LABELS  = range(__I_LABEL_START,  __I_ENTRY_START)
    __RNG_ENTRIES = range(__I_ENTRY_START,  __I_FIELD_START)
    __RNG_FIELDS  = range(__I_FIELD_START,  __I_BUTTON_START)
    __RNG_BUTTONS = range(__I_BUTTON_START, __I_FINISH)

    # label strings used in GUI
    __STR_LABELS = (
        'Input temperature:',
        '',
        'Output temperature:'
    )

    # button strings used in GUI
    __STR_BUTTONS = (
        'Convert to Fahrenheit!',
        'Convert to Celsius!'
    )

    # number of characters in each entry widgets
    __ENTRY_WIDTH = 6

    # result formats
    __FAHRENHEIT_FORMAT = '%.1f °F'
    __CELSIUS_FORMAT = '%.1f °C'

# end class CelsiusFahrenheitConverter

# create the gui and run the main window loop
cf_conv_gui = CelsiusFahrenheitConverter()
