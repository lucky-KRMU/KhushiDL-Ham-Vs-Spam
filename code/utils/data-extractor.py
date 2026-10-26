import pathlib as pl

# creating the directories (folders)
pl.Path('../../data').mkdir(exist_ok=True)
pl.Path('../../data/ham').mkdir(exist_ok=True)
pl.Path('../../data/spam').mkdir(exist_ok=True)

# variables to keep file count
ham_count = 1
spam_count = 1

# getting the data
with open('../../raw data/SMSSpamCollection') as file:
    lines = file.readlines()

# creating files
for line in lines:
    line = line.strip()
    if line[0:3] == 'ham':
        with open(f'../../data/ham/{ham_count}.txt', "w") as file:
            file.write(line[4:])
        ham_count += 1
    else:
        with open(f'../../data/spam/{spam_count}.txt', "w") as file:
            file.write(line[5:])
        spam_count += 1

print("Data Created")
print(f"Total ham: {ham_count - 1}")
print(f"Total spam: {spam_count - 1}")