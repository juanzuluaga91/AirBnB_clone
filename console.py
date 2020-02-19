#!/usr/bin/python3
"""
ontains the entry point of the command interpreter

"""
import cmd
import shlex
import models
from models.base_model import BaseModel
from models import storage

class_type = {"BaseModel": BaseModel, "User" : User}


class HBNBCommand(cmd.Cmd):
    """Class Console """
    prompt = "(hbnb) "

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

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in class_type:
            new_inst = class_type[args[0]]()
        else:
            print("** class doesn't exist **")
            return False
        print(new_inst.id)
        new_inst.save()

    def do_show(self, arg):
        """
        Prints the string representation
        of an instance based on the class name and id
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in class_type:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in class_type:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    models.storage.all().pop(key)
                    models.storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints string representations of instances"""
        args = shlex.split(arg)
        obj_all = []
        if len(args) == 0:
            for value in models.storage.all().values():
                obj_all.append(str(value))
            print("[", end="")
            print(", ".join(obj_all), end="")
            print("]")
        elif args[0] in class_type:
            for key in models.storage.all():
                if args[0] in key:
                    obj_all.append(str(models.storage.all()[key]))
            print("[", end="")
            print(", ".join(obj_all), end="")
            print("]")
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
