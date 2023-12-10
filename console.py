#!/usr/bin/python3
''' Console module definition '''
from models.base_model import BaseModel
from models import storage
import cmd


class HBNBCommand(cmd.Cmd):
    ''' console class definition '''
    prompt = "(hbnb) "

    def emptyline(self):
        ''' pass when empty line '''
        pass

    def do_EOF(self, arg):
        ''' exit feature definition'''
        return True

    def do_quit(self, arg):
        '''Quit command to exit the program '''
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
