#!/usr/bin/python3
"""
ontains the entry point of the command interpreter

"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Class Console """
    prompt = "(hbnb)"

    def emptyline(self):
        """empty line execution"""
        pass

    def do_EOF(self, line):
        """EOF command to exit the interpreter"""
        print("")
        return True

    def do_quit(self, line):
        """Quit command to exit the interpreter"""
        return True

    do_EOF = do_quit

if __name__ == '__main__':
    HBNBCommand().cmdloop()
