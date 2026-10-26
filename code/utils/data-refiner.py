import pathlib as pl

pl.Path('../../data').mkdir(exist_ok=True)
pl.Path('../../data/ham').mkdir(exist_ok=True)
pl.Path('../../data/spam').mkdir(exist_ok=True)
ham_count = 1
spam_count = 1

with open('../../raw data/SMSSpamCollection') as file:
    lines = file.readlines()

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