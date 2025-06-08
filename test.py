import subprocess
import logging

logging.basicConfig(filename = 'Logs.log', level = logging.INFO, format = ('%(asctime)s - %(levelname)s - %(message)s'))

logger = logging.getLogger(__name__)

while(True):
    print("Welcome to the terminal, choose a command: ")
    print("1-see current directory")
    print("2-see the files")
    print("3-make a new file")
    print("4-delete a file")
    print("5-quit")
    choice = int(input())

    if(choice == 1):
        result = subprocess.run(["pwd"], capture_output=True, text=True, check=True)
        print(f"The current directory is: {result.stdout}")
        try:
            logging.info("the current direcroty was seen")
        except subprocess.CalledProcessError as e:
            logger.error("No permission", exc_info= True)

    elif(choice == 2):
        result = subprocess.run(["ls"], capture_output = True, text=True)
        print(f"The files are: {result.stdout}")
        try:
            logging.info("The files were seen")
        except PermissionError as e:
            logger.error("No permission", exc_info=True)
    
    elif(choice == 3):
        name = input("Enter the file name you want to make: ")
        try:
            subprocess.run(['touch', name])
            print(f"{name} file was made")
            logging.info(f"a new file was made by name: {name}")
        except PermissionError as e:
            logger.error("No permission,, the file was not made", exc_info=True)

    elif(choice == 4):
        name = input("Enter the name of the file you want to delete: ")
        try:
            subprocess.run(['rm', name], check= True)
            print(f"The file {name} was deleted")
            logging.warning(f"file {name} was deleted")
        except subprocess.CalledProcessError:
            print("No such file or directory")
            logger.exception("No file was found to delete")

    elif(choice == 5):
        choice1 = input("Do you want to delete the logs? y/n: ")
        if(choice1 == 'y'):
            subprocess.run(['rm', 'Logs.log'])
            print("Goodbye!")
            break
        elif(choice1 == 'n'):
            print("goodbye")
            logging.info("The program was quit")
            break

    else:
        print("Invalid input")


    
