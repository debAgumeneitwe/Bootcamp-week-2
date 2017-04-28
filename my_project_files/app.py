""""
Usage:
    create_room <room_name> <room_type>...
    add person <full_name> <position>
    -h | --help

Options:
  -h --help     Show this screen.    
"""

from docopt import docopt, DocoptExit
import cmd # helps to activate modules of the interactive and the program dependencies
from Dojo_room_allocation import Dojo

def docopt_decorator(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """

    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class DojoInteractive(cmd.Cmd):
    intro = 'Welcome to the Room Allocation System!' + ' (Type help for a list of commands.)'
    prompt = '(The Dojo) '
    file = None
    
    
    @docopt_decorator
    def do_create_room(self, arg):
        """Usage: create_room <room_name> <room_type>..."""
        room_name = arg['<room_name>']
        room_type = arg['<room_type>']
        for name in room_name:
            print(room_type, " called ", room_name, " has been successfully created")
        
        
    @docopt_decorator
    def do_add_person(self,arg):
        """Usage: add_person <full_name> <position>"""
        full_name = arg["<full_name>"]
        position = arg["<position>"]
        print(full_name, "has been successfully added")
        
        
    
    
    
DojoInteractive().cmdloop()
    
    
    





