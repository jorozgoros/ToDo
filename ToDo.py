from datetime import datetime
from datetime import date


today = date.today()
dateFormated = today.strftime("%d %B, %Y")

print("Welcome to the To Do app\nActions: \n 1-Check entries\n 2-New entrie\n 3-Delete entrie\n 4-Exit")
entries = {}

def printEntries():
    print(entries)
    for x in entries:
        print(f"{x}:\n {entries[x][0]}, {entries[x][1]}")

def newEntrie():
    entrie = "hola" #input("Type the desired entrie: ")
    date = today
    deadline = "02-04-2025" #input("Enter the deadline in dd-mm-yyyy format. For no deadline type 0:")
    date_deadline = datetime.strptime(deadline, '%d-%m-%Y').date()
    deadlineFormated = date_deadline.strftime("%d %B, %Y")
    entries[deadlineFormated]=(dateFormated, entrie)

while True:
    action = int(input("Please, choose an action:"))
    if action == 1:
        printEntries()
    elif action == 2:
        newEntrie()
    elif action == 4:
        break

