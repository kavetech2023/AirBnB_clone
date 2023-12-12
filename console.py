#!/usr/bin/python3
"""
defines the console module
"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ entry point of the command interpreter"""
    prompt = "(hbnb) "
    dict_classes = {"BaseModel": BaseModel,
                    "User": User,
                    "City": City,
                    "State": State,
                    "Amenity": Amenity,
                    "Place": Place,
                    "Review": Review
                    }

    def do_quit(self, line):
        """Quit command to exit program"""
        return True

    def do_EOF(self, line):
        """Eof command to exit program"""
        print("")
        return True

    def emptyline(self):
        """does nothing"""
        pass

    def do_create(self, args):
        """creates a new instance of the given class
        create class name
        create BaseModel
        """
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.dict_classes.keys():
            print("** class doesn't exist **")
            return
        new_object = eval(args[0])()
        storage.save()
        print(new_object.id)

    def do_show(self, args):
        """prints str representation of an obj
        based on claas name and id
        shows class name
        """
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.dict_classes.keys():
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        str_repre = "{}.{}".format(args[0], args[1])
        if str_repre in storage.all().keys():
            print(storage.all()[str_repre])
        else:
            print("** no instance found **")

    def do_destroy(self, args):
        """deletes objects based on id and class name
        destroys class name and id
        """
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.dict_classes.keys():
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        str_repre = "{}.{}".format(args[0], args[1])
        if str_repre in storage.all().keys():
            del storage.all()[str_repre]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, args):
        """prints str representation of all objects
        based on class or not
        all class names, doesnt matter
        """
        args = args.split()
        if not args:
            print([obj.__str__() for obj in storage.all().values()])
            return
        if args[0] not in HBNBCommand.dict_classes.keys():
            print("** class doesn't exist **")
            return
        list_objects = []
        for obj in storage.all().values():
            if obj.__class__.__name__ == args[0]:
                list_objects += [obj.__str__()]
        print(list_objects)

    def do_update(self, args):
        """updates objects
        by modifying an attribute
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.dict_classes.keys():
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        str_repre = "{}.{}".format(args[0], args[1])
        if str_repre not in storage.all().keys():
            print("** no instance found **")
            return
        obj = storage.all()[str_repre]
        setattr(obj, args[2], args[3])
        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
