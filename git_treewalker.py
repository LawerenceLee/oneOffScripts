#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
import os


def treewalker(path):
    for root, dirs, files in os.walk(path):
        for directory in dirs:
            dir_path = os.path.join(root, directory)
            if '.git' in os.listdir(dir_path):
                print(dir_path)
                print('*'*60)
                os.system("cd {} && git pull github master".format(dir_path))
                os.system("cd {} && git push github master".format(dir_path))
                os.system("cd {} && git pull origin master".format(dir_path))
                os.system("cd {} && git push origin master".format(dir_path))
                print('*'*60, "\n\n")


if __name__ == "__main__":
    os.system('cls' if os.name == "nt" else "clear")
    path = input("Enter a full path: ")
    treewalker(path)
