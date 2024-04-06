from src.gui.start import start
from src.lib.rdb.model import Database

database = Database()

def main():

    start(database)

if __name__ == '__main__':

    main()