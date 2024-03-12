import cmd
class HBNBCommand(cmd.Cmd):
    """class for HBNB command"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit the program."""
        return True
    def do_EOF(self, arg):
        """Quit the program."""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()