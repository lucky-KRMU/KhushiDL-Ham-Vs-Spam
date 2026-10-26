'''
This is the program to refine and equate the count of spam and ham messages
'''

# importing the necessary module
import pathlib as pl
from random import sample, shuffle
from shutil import move

root_path = pl.Path('../../data') # defining the root path

ham_dir = [file for file in (root_path/"ham").iterdir()] # getting the ham messages
spam_dir = [file for file in (root_path/"spam").iterdir()] # getting the spam messages

# counting message numbers and creating sorted directories
ham_count = len(ham_dir)
spam_count = len(spam_dir)
del_count = 0
data_count = 0

# deleting the exccess data
if ham_count > spam_count:
    data_count = (ham_count-spam_count) # getting the data count ( to be deleted )
else:
    data_count = (spam_count-ham_count)

to_del = sample(ham_dir, k=data_count) # getting the files to be deleted

# deleting the files
for file in to_del:
    file.unlink(missing_ok=True)
    del_count += 1


ham_dir = [file for file in (root_path/"ham").iterdir()] # getting the ham messages
spam_dir = [file for file in (root_path/"spam").iterdir()] # getting the spam messages

# counting message numbers and creating sorted directories
ham_count = len(ham_dir)
spam_count = len(spam_dir)

# printing the final report
print("Total Files deleted: {}".format(del_count))
print("Total Ham files remaining: {}".format(ham_count))
print("Total Spam files remaining: {}".format(spam_count))


# Splitting the data into test and train

# making the directories (train and test)
train = (root_path / "train").mkdir(exist_ok=True)
test = (root_path / "test").mkdir(exist_ok=True)

train = (root_path/"train")
test = (root_path/"test")

# creating train folder subfolders
train_ham = (train / "ham").mkdir(exist_ok=True) 
train_spam = (train / "spam").mkdir(exist_ok=True) 

# creating test folder subfolders
test_ham = (test / "ham").mkdir(exist_ok=True) 
test_spam = (test / "spam").mkdir(exist_ok=True) 

# we will split the data into 3:1 ratio (train:test)

# shuffling the data
ham_shuffle = [file for file in (root_path/"ham").iterdir()]
spam_shuffle = [file for file in (root_path/"spam").iterdir()]

shuffle(ham_shuffle)
shuffle(spam_shuffle)

k = int(data_count * .75)
file_move = 0

# for train data
for file in ham_shuffle[:k]:
    move(file, (train/"ham"))
    file_move += 1
    
for file in spam_shuffle[:k]:
    move(file, (train/"spam"))
    file_move += 1

# for test data
for file in ham_shuffle[k:]:
    move(file, (test/"ham"))
    file_move += 1
    
for file in spam_shuffle[k:]:
    move(file, (test/"spam"))
    file_move += 1

# removing the ham and spam directories
(root_path/"ham").rmdir()
(root_path/"spam").rmdir()

# printing the final statistics
print("-"*10)
print("Files Moved: {}".format(file_move))
print(f"Total Train Ham: {len([file for file in (train/ "ham").iterdir()])}")
print(f"Total Train Ham: {len([file for file in (train/ "spam").iterdir()])}")
print(f"Total Test Ham: {len([file for file in (test/ "ham").iterdir()])}")
print(f"Total Test Ham: {len([file for file in (test/ "spam").iterdir()])}")