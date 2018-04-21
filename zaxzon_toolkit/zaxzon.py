import os
import sys


def make_toolbox(toolbox_name, flag="--local"):
    toolbox_path = "{}/.zaxzon_toolboxes/{}_toolbox/".format(
                                    os.environ['HOME'], toolbox_name)
    if toolbox_name != "":
        try:
            os.makedirs(toolbox_path)
            os.chdir(toolbox_path)
            os.system("cd {} && git init".format(toolbox_path))
        except OSError:
            print("This toolbox already exists")
    if flag == '--web':
        remote_name = input("Remote Repository Name: ")
        remote_address = input("Remote Repository Path: ")
        os.system("cd {} && git remote add {} {} ".format(
                                                toolbox_path,
                                                remote_name,
                                                remote_address))


def main():
    action = sys.argv[1]
    if action == 'make_toolbox':
        if len(sys.argv) == 4:
            make_toolbox(sys.argv[2], sys.argv[3])
        elif len(sys.argv) == 3:
            make_toolbox(sys.argv[2])
        else:
            print("You've passed too many arguments to 'make_toolbox")


if __name__ == "__main__":
    main()
