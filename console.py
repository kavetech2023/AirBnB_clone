#!/usr/bin/python3
"""Contains the entry point of the command interpreter.
"""

import cmd
import models
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import shlex


class HBNBCommand(cmd.Cmd):
    """class for command processor.

    Args:
        cmd (_type_): _description_
    """
    prompt = "(hbnb) "
    classes_list = ["BaseModel", "User", "State", "City", "Amenity",
                    "Place", "Review"]
    commands_list = ["create", "show", "all", "destroy", "update", "count"]

    def do_quit(self, args):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, args):
        """EOF command to exit the program
        """
        return True

    def emptyline(self):
        """Empty line shouldn't execute anything
        """
        pass

    def do_create(self, inp):
        """Creates a new instance of BaseModel, saves it (to the JSON
        file) and prints the id.

        Args:
            class_name (class): name of current class.
        """
        args = inp.split()
        if not self.class_verification(args):
            return

        inst = eval(str(args[0]) + '()')
        if not isinstance(inst, BaseModel):
            return
        inst.save()
        print(inst.id)

    def do_show(self, inp):
        """Prints the string representation of an instance based on the
        class name and id.
        """
        args = inp.split()

        if not self.class_verification(args):
            return

        if not self.id_verification(args):
            return

        string_key = str(args[0]) + '.' + str(args[1])
        objects = models.storage.all()
        print(objects[string_key])

    @classmethod
    def class_verification(cls, args):
        """Verifies class and checks if it is in the class list.

        Returns:
            bool: True or false depending on status of class.
        """
        if len(args) == 0:
            print("** class name missing **")
            return False

        if args[0] not in cls.classes_list:
            print("** class doesn't exist **")
            return False

        return True

    @staticmethod
    def id_verification(args):
        """Verifies id of class.

        Returns:
            bool: True or False depending on status of id.
        """
        if len(args) < 2:
            print("** instance id missing **")
            return False

        objects = models.storage.all()
        string_key = str(args[0]) + '.' + str(args[1])
        if string_key not in objects.keys():
            print("** no instance found **")
            return False

        return True

    def do_destroy(self, inp):
        """Deletes an instance based on the class name and id (save the
        change into the JSON file).
        """
        args = inp.split()
        if not self.class_verification(args):
            return
        if not self.id_verification(args):
            return
        string_key = str(args[0]) + '.' + str(args[1])
        objects = models.storage.all()
        models.storage.delete(objects[string_key])
        models.storage.save()

    def do_all(self, inp):
        """Prints all string representation of all instances based or not
        on the class name.
        """
        args = inp.split()
        all_objects = models.storage.all()
        list_ = []
        if len(args) == 0:
            # print all classes
            for value in all_objects.values():
                list_.append(str(value))
        elif args[0] in self.classes_list:
            # print just arg[0] class instances
            for (key, value) in all_objects.items():
                if args[0] in key:
                    list_.append(str(value))
        else:
            print("** class doesn't exist **")
            return False
        print(list_)

    def do_update(self, line):
        """ Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file).
        """
        act = ""
        for argv in line.split(','):
            act = act + argv
        args = shlex.split(act)
        if not self.class_verification(args):
            return
        if not self.id_verification(args):
            return
        if not self.attribute_verification(args):
            return
        all_objects = models.storage.all()
        for key, value in all_objects.items():
            object_name = value.__class__.__name__
            object_id = value.id
            if object_name == args[0] and object_id == args[1].strip('"'):
                if len(args) == 2:
                    print("** attribute name missing **")
                elif len(args) == 3:
                    print("** value missing **")
                else:
                    setattr(value, args[2], args[3])
                    models.storage.save()
                return

    def precmd(self, arg):
        """Hook before the command is run.
        If the self.block_command returns True, the command is not run.
        Otherwise, it is run.
        """
        if '.' in arg and '(' in arg and ')' in arg:
            cls = arg.split('.')
            command = cls[1].split('(')
            args = command[1].split(')')
            if cls[0] in HBNBCommand.classes_list and command[0] \
                    in HBNBCommand.commands_list:
                arg = command[0] + ' ' + cls[0] + ' ' + args[0]
        return arg

    def do_count(self, class_name):
        """Retrieve the number of instances of a class.
        """
        count = 0
        all_objects = models.storage.all()
        for key, value in all_objects.items():
            keys_split = key.split('.')
            if keys_split[0] == class_name:
                count += 1
        print(count)

    @staticmethod
    def attribute_verification(args):
        """Verifies attributes.
        """
        if len(args) < 3:
            print("** attribute name missing **")
            return False
        if len(args) < 4:
            print("** value missing **")
            return False
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
