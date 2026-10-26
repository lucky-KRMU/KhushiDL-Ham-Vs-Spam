'''
This is the program to refine and equate the count of spam and ham messages
'''

# importing the necessary module
import pathlib as pl
from random import sample

root_path = pl.Path('../../data') # defining the root path

ham_dir = [file for file in (root_path/"ham").iterdir()] # getting the ham messages
spam_dir = [file for file in (root_path/"spam").iterdir()] # getting the spam messages

# counting message numbers and creating sorted directories
ham_count = len(ham_dir)
spam_count = len(spam_dir)
del_count = 0

# deleting the exccess data
if ham_count > spam_count:
    to_del = sample(ham_count, k=(ham_count-spam_count))
else:
    to_del = sample(spam_count, k=(spam_count-ham_count))

# deleting the files
for file in to_del:
    file.unlink(missing_ok=True)


ham_dir = [file for file in (root_path/"ham").iterdir()] # getting the ham messages
spam_dir = [file for file in (root_path/"spam").iterdir()] # getting the spam messages

# counting message numbers and creating sorted directories
ham_count = len(ham_dir)
spam_count = len(spam_dir)

print("Total Files deleted: {}".format(del_count))
print("Total Ham files remaining: {}".format(ham_count))
print("Total Spam files remaining: {}".format(spam_count))
    