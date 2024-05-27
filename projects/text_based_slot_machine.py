#the user can deposit a certain amount of money that will 
#allow to bet btwn 1 , 2 , 3 lines
#with a 3 by 3 slot machine
import random


MAX_LINES = 3
MIN_BET = 5
MAX_BET = 1000

ROWS = 3
COLS = 3

symbol_count={
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:#you can also do that if you dont use a break statement you can use an else to be ran after the for loop
            winnings += values[symbol] + bet
            winning_lines.append(line + 1)
    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column=[]
        current_symbols = all_symbols[:]#making a copy
        for _ in range(rows):
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns

def print_slot_machine(columns):
    #transposing
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):#gives you the index plus the item in the indexed place in list
            if i != len(columns) -1:
                print(column[row],end = "|")
            else:
                print(column[row], end = "")
            
        print()#empty print statement  prints newline character or space

def deposit():
    while True:
        amount = input("What would you like to deposit?? $$")
        if amount.isdigit():
            amount=int(amount) 
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("please enter a number.")

    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines you wanna bet on(1 -" + str(MAX_LINES)+ ")? " )
        if lines.isdigit():
            lines=int(lines) 
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("please enter a number.")

    return lines

def get_bet():
    while True:
        bet = input("What would you like to bet on each line?" )
        if bet.isdigit():
            bet=int(bet) 
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET}- ${MAX_BET}")
                #Embedding numbers in sentenses will be converted to string by pythom
        else:
            print("please enter a number.")

    return bet

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"you don't have enough money to bet that amount, you current balance is: {balance}")
        else:
            break
    print(f"You are betting ${bet} Lines {lines}. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines ,bet , symbol_value)
    print(f"You won ${winnings}.")
    print(f"you won on", *winning_lines)#will pass all the lines and pass them to the print statement
    return  winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("press enter to spin (q to quit) .")
        if answer == "q":
            break
        balance += spin(balance)
    print(f"You left with {balance}")

main()