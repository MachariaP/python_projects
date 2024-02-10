#!/usr/bin/python3
"""Command interpreter for the AirBnB clone project"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program gracefully at End Of File (EOF)"""
        print("")  # Print a new line before exiting
        return True

    def emptyline(self):
        """Called when an empty line is entered"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
