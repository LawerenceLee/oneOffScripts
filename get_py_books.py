import os

if __name__ == "__main__":
    username = os.getlogin()
    os.chdir('/Users/{}/Desktop'.format(username))
    os.system('git clone https://LawerenceLee@bitbucket.org/LawerenceLee/python_books.git')