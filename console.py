#!/usr/bin/python3
"""
ontains the entry point of the command interpreter

"""
import cmd
import shlex
import models
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models import storage

class_type = {'BaseModel': BaseModel,
              'User': User,
              'Place': Place,
              'State': State,
              'City': City,
              'Amenity': Amenity,
              'Review': Review}


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

    def do_update(self, args):
        """Update command load new info at the instances"""
        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
        elif not args[0] in class_type:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif ("{}.{}".format(args[0], args[1]) not in storage.all().keys()):
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            new_dict = storage.all()
            tmp = "{}.{}".format(args[0], args[1])
            if tmp in new_dict.keys():
                attr = getattr(new_dict[tmp], args[2], "")
                setattr(new_dict[tmp], args[2], type(attr)(args[3]))
                new_dict[tmp].save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
