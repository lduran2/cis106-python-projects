'''
./final-project/password_checking_gui.py
An event-driven GUI program implementing password validator.

By     : Leomar Duran <https://github.com/lduran2>
When   : 2020-12-11t16:15
Where  : Community College of Philadelphia
For    : CIS 106/Introduction to Programming
Version: 1.0

Changelog:
    v1.0 - 2020-12-12t01:05
        Implemented GUI.
        Added support for frame sets.
        Removed fields because this GUI does not have them.
        Added indices for all label strings.
'''

# libraries
import password_checking as pwch    # for the password validator
import tkinter as tk                # for GUI

class PasswordCheckingGui:
    '''
    A GUI of a password validator.
    '''

    def __init__(self):
        '''
        Creates the GUI.
        '''

        # tuple of commands for the buttons
        COMMANDS = ( self.checkPassword, )

        # list of widgets in the main window
        widgets = []
        # list of sides to pack widgets to
        sides = []

        # lists of methods to export
        # accessors for passwords
        get_passwords   = ([None] * self.__N_FIELD_SETS)
        # mutators for the error messages
        set_messages    = ([None] * self.__N_FIELD_SETS)
        # mutators for the success messages
        set_successes   = ([None] * self.__N_FIELD_SETS)

        # create the main window
        win_main = tk.Tk()
        # provide width to the window
        widgets.append(tk.Canvas(win_main,
            width=self.__MAIN_WINDOW_WIDTH, height=0))
        # pack to the top
        sides.append('top')

        # for every fieldset
        for j in range(self.__N_FIELD_SETS):

            # set up the frames (stop at the labels)
            for k in self.__RNG_FRAMES[j]:
                # create the frame, and add it to widgets
                widgets.append(tk.Frame(win_main))
                # top pack all frames
                sides.append('top')
            # end for k in self.__RNG_FRAMES[j]

            # set up the list for StringVar objects
            stvs = []
            # set up the labels
            for k in range(len(self.__RNG_LABELS[j])):
                # choose the correct frame
                i_frame = self.__RNG_FRAMES[j][k]
                # get the label string
                str_label = self.__STR_LABELS[j][k]
                # create its StringVar
                stvs.append(tk.StringVar())
                stvs[k].set(str_label)
                # create the label
                label = tk.Label(widgets[i_frame], textvariable=stvs[k])
                # add the label to widgets
                widgets.append(label)
                # left pack all labels
                sides.append('left')
            # end for k in range(len(self.__RNG_LABELS[j]))

            # set up the entries
            for k in range(len(self.__RNG_ENTRIES[j])):
                # choose the correct frame
                i_frame = self.__RNG_FRAMES[j][k]
                # create the entry
                entry = tk.Entry(widgets[i_frame], width=self.__ENTRY_WIDTH)
                # add the entry to widgets
                widgets.append(entry)
                # right pack all entries
                sides.append('right')
            # end for k in self.__RNG_ENTRIES[j]

            # colors, accessors, mutators
            widgets[self.__I_LBL_MESSAGE[j]]['fg'] = 'red'
            widgets[self.__I_LBL_SUCCESS[j]]['fg'] = 'green'
            get_passwords[j] = widgets[self.__I_ENT_PASSWORD[j]].get
            set_messages[j] = stvs[self.__I_STR_MESSAGE].set
            set_successes[j] = stvs[self.__I_STR_SUCCESS].set
        # end for j in range(self.__N_FIELD_SETS)

        # add the get methods for passwords to self
        self.__get_passwords    = get_passwords
        # add the set methods for error and success messages to self
        self.__set_messages     = set_messages
        self.__set_successes    = set_successes

        # set up the buttons
        for k in range(len(self.__RNG_BUTTONS)):
            # create the button
            button = tk.Button(widgets[self.__I_BUTTON_FRAME_START],
                text=self.__STR_BUTTONS[k], command=COMMANDS[k]
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
        print('Password Checking: Running main window loop . . .')
        # run the main window loop
        win_main.mainloop();

        # finish
        print('Done.')
    # end def __init__(self)

    def checkPassword(self):
        '''
        Runs the password validator and displays the result on the GUI.
        '''
        # get the passwords
        passwords = (self.__get_passwords[0](), self.__get_passwords[1]())
        # check for the same password
        are_same_passwords = (passwords[0] == passwords[1])
        # validate the first password
        password_validation = pwch.validate_password(passwords[0])
        n_errors = len(password_validation)

        # clear all messages
        for j in range(self.__N_FIELD_SETS):
            self.__set_messages[j](
                self.__STR_LABELS[j][self.__I_STR_MESSAGE])
            self.__set_successes[j](
                self.__STR_LABELS[j][self.__I_STR_SUCCESS])
        # end for k in range(self.__N_FIELD_SETS)

        # if not the same password, notify message[1]
        if (not(are_same_passwords)):
            self.__set_messages[1]('✖ The two passwords must be the same.')
        # otherwise, but the password is invalid, notify
        elif (n_errors != 0):
            self.__set_messages[1]('✖ The password is not a proper password.')
        else:
        # otherwise, accept the password
            self.__set_successes[1]('✔ Password accepted!')
        # if (not(are_same_passwords)) elif (n_errors != 0) else

        # if there are any validation errors
        if (n_errors != 0):
            # add the header and complete the lines
            password_validation = ('The password:',) + password_validation
            password_validation += ('',) * (pwch.N_ERRORS - n_errors)
            # notify message[0]
            self.__set_messages[0]('\n'.join(password_validation))
        # end if (len(password_validation) != 0)
        # otherwise, the password is proper
        else:
            self.__set_successes[0]('✔ The password is a proper password!')
        # end if (len(password_validation) != 0) else
    # end def convertToFahrenheit(self)


    ##################################################################
    # CONSTANTS

    # width of the main window
    __MAIN_WINDOW_WIDTH = 500

    # number of field sets
    __N_FIELD_SETS = 2

    # index lists for each fieldset
    __I_FRM_PASSWORD    = ([0] * __N_FIELD_SETS)
    __I_FRM_MESSAGE     = ([0] * __N_FIELD_SETS)
    __I_FRM_SUCCESS     = ([0] * __N_FIELD_SETS)
    __I_LBL_PASSWORD    = ([0] * __N_FIELD_SETS)
    __I_LBL_MESSAGE     = ([0] * __N_FIELD_SETS)
    __I_LBL_SUCCESS     = ([0] * __N_FIELD_SETS)
    __I_ENT_PASSWORD    = ([0] * __N_FIELD_SETS)

    # tuple of keys for widgets in the main window
    ( 
        __I_CANVAS,
        __I_FRM_PASSWORD[0], __I_FRM_MESSAGE[0], __I_FRM_SUCCESS[0],
        __I_LBL_PASSWORD[0], __I_LBL_MESSAGE[0], __I_LBL_SUCCESS[0],
        __I_ENT_PASSWORD[0],
        __I_FRM_PASSWORD[1], __I_FRM_MESSAGE[1], __I_FRM_SUCCESS[1],
            __I_FRM_SUBMIT,
        __I_LBL_PASSWORD[1], __I_LBL_MESSAGE[1], __I_LBL_SUCCESS[1],
        __I_ENT_PASSWORD[1],
        __I_BTN_CHECK_PASSWORD,
        __I_FINISH
    ) = tuple(range(18))

    # index of first of each class of widget
    __I_FRAME_START   = ( __I_FRM_PASSWORD[0], __I_FRM_PASSWORD[1] )
    __I_LABEL_START   = ( __I_LBL_PASSWORD[0], __I_LBL_PASSWORD[1] )
    __I_ENTRY_START   = ( __I_ENT_PASSWORD[0], __I_ENT_PASSWORD[1] )
    __I_BUTTON_START  = __I_BTN_CHECK_PASSWORD

    # index of first of widget subclasses
    __I_BUTTON_FRAME_START  = __I_FRM_SUBMIT

    # range of each class of widget
    __RNG_FRAMES  = (
        range(__I_FRAME_START[0], __I_LABEL_START[0]),
        range(__I_FRAME_START[1], __I_LABEL_START[1]) )
    __RNG_LABELS  = (
        range(__I_LABEL_START[0], __I_ENTRY_START[0]),
        range(__I_LABEL_START[1], __I_ENTRY_START[1]) )
    __RNG_ENTRIES = (
        range(__I_ENTRY_START[0], __I_FRAME_START[1]),
        range(__I_ENTRY_START[1], __I_BUTTON_START) )
    __RNG_BUTTONS = range(__I_BUTTON_START, __I_FINISH)

    # label strings used in GUI
    __STR_LABELS = (
        (
            'Enter password:',
            ('\n' * (pwch.N_ERRORS + 1 - 1)),
            ''
        ),
        (
            'Confirm password:',
            '',
            ''
        )
    )

    # indices for string labels
    (__I_STR_PASSWORD, __I_STR_MESSAGE, __I_STR_SUCCESS) =\
        range(len(__RNG_LABELS[0]))

    # button strings used in GUI
    __STR_BUTTONS = (
        'Check password!',
    )

    # number of characters in each entry widgets
    __ENTRY_WIDTH = 20

# end class PasswordCheckingGui

# create the gui and run the main window loop
pwch_gui = PasswordCheckingGui()
