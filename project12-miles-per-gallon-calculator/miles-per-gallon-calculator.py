'''
./project12-miles-per-gallon-calculator/miles-per-gallon-calculator.py
An event-driven GUI program implementing a miles per gallon calculator
with a 'Calculate MPG' button.

By     : Leomar Duran <https://github.com/lduran2>
When   : 2020-12-05t16:39
Where  : Community College of Philadelphia
For    : CIS 106/Introduction to Programming
Version: 1.0

Changelog:
    v1.0 - 2020-12-05t16:39
        Created the GUI with just the labels.
'''

# libraries
import tkinter as tk    # for GUI

class MilesPerGallonGUI:
    '''
    A GUI of a Miles Per Gallon calculator.
    '''

    def __init__(self):
        '''
        Creates the GUI.
        '''

        # tuple of keys for widgets in the main window
        ( \
            I_FRM_GALLONS,    I_LBL_GALLONS,\
            I_FRM_MILES,      I_LBL_MILES,\
            I_FRM_SUBMIT,     I_LBL_SUBMIT, \
            I_FINISH\
        ) = tuple(range(0,7))

        LABELS = (
            'Size of gas tank [gal]:',\
            'Most one can drive [mi]:',\
        )

        # list of widgets in the main window
        widgets = []

        # create the main window
        win_main = tk.Tk()

        # create the frames that have labels (stop at the submit frame)
        for k in range(I_FRM_GALLONS, I_FRM_SUBMIT, 2):
            # create the frame
            frame = tk.Frame(win_main)
            # choose the correct label
            i_label = ((k - I_FRM_GALLONS) >> 1)
            # add it to widgets
            widgets.append(frame)
            # create and add to widgets, the label
            widgets.append(tk.Label(frame, text=LABELS[i_label]))
        # end for k in range(I_FRM_GALLONS, I_LBL_GALLONS)

        # reverse the order of the widgets
        # pack all widgets in the reverse widgets list
        for widget in widgets:
            widget.pack()
        # end for k in range(len(widgets))

        # run the main window loop
        win_main.mainloop();
    # end def __init__(self)
# end class MilesPerGallonGUI

mpg_gui = MilesPerGallonGUI()