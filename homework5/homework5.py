d# 3.1 --- Vocab Review ----
'''
1. Git is a software that allows you to navigate through your computer from within the terminal. Github is an online repository for files stored in your computer that allows you to save things outside your computer and share them. 
2. The terminal is where you interact with files on your computer and run code. The command line is the specific line where you type and run commands. 
3. A local repository is where files are stored on your computer. A remote repository stores files outside of your computer and allows anyone to acces them. 
4. Version control is a service provided by online softwares that tracks changes to go between saved versions. 
5. The staging area is the screen git gives you before you push your changes to be saved in a remote repository. You can edit any changes you have made and tell git to only commit certain changes. 
6. Git add tells git to search the directory you are currently in for new changes. 
7. Git commit saves all changes specified after git add to your local repository's memory. 
8. Git push sends the file saved by git commit to the remote repository. 
9. Git status shows informations about your current repository, any changes you have made to your file since your last commit, and information about your staging area. 
10. Git pull brings changes from a remote directory to your computer.  
11.pwd prints the location of your current working directory
12. ls lists the files and directories within your current directory
13. cd changes current directory to the specified directory
14. nano allows you to edit the specified file
15. touch creates a file with the given name
16. mv moves the specified file to a new location
17. rm removes the specified file
18. cat combines files 
'''

# 3.2 --- Directory Tree ---
'''
1. pwd
2. ls
3. cd python_decal/brianna_repo, pull homework.py
4. mv homework.py homework/
5. cd python_decal/judy_decal/homework/
6. nano homework.py
7. git add ., git commit -m "Homework done", git push origin main
8. git pull judy_decal, git add ., git commit -m "some commit message", git push origin main
9. ~/recents/
'''
# 4.1 --- Data Types ---

def data_type(input_string):
    print(type(input_string))

data_type(3.14)
data_type(True)

# 4.2 --- Conditionals ---

def even_or_odd(num):
    if num % 2 == 1:
        print(str(num) + " is odd")
    else: 
        print(str(num) + " is even")

even_or_odd(7)
even_or_odd(10)

# 5 --- Loops ---
def sumWithLoop(numbers):
    sum_of_numbers = 0
    for number in numbers:
        sum_of_numbers += number
    print(sum_of_numbers)

sumWithLoop([1, 2, 3, 4, 5])

# 6.1 --- Lists --- 
def duplicateList(list1):
    second_list = []
    for word in list1:
        second_list.append(word)
        second_list.append(word)
    print(second_list)

duplicateList(['a', 'b', 'c'])
               
# 6.2 --- Debugging --- 
def square(num):
    return(num * num)

even_or_odd(89)