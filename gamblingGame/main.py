import random

# slot machine, 3 in a row matches, 3x3

# constant value of lines in slot machine/
# or rows of char that cycle in slot machine
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

SLOT_ROWS = 3
SLOT_COLS = 3

symbol_count = {"🍑": 2, "🃏": 3, "💣": 6, "🍒": 8}

symbol_value = {"🍑": 5, "🃏": 4, "💣": 3, "🍒": 2}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    # if one line is betted, each row will be checked dynamically per number of lines being betted on
    for line in range(lines):
        # going down the first column, then second, then third, and so on until the number of lines being betted on is reached
        symbol = columns[0][line]
        # loops through each column to check symbol is matching
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            """
            bet on each line, so individual lines can give a loss or win, so winnings is added to the total winnings,
            and not multiplied by the number of lines betted on
            """
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


# GENERATE  what symbols will be in cols
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        # _ key words when you are iterating, and it doesn't matter we use a anonymous value
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    # adds a copy to this variable instead of a reference to prevent overwriting of either variables
    columns = []
    for _ in range(cols):
        # what values go into columns vertically, per rows
        column = []
        # : is there to make a reference not a copy
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            # remove selected symbols, from finding first instance in the list
            current_symbols.remove(value)
            column.append(value)
            # add value of symbol to column
        columns.append(column)

    return columns


def print_slots_machine(columns):
    """
    columns displayed and function as row as the data structure
    we need to transpose the matrix 90 so its vertical instead of horizontal
    if crash its because the index is out of range
    """
    for row in range(len(columns[0])):
        """
        loop through all columns and only print first value of index of current row
        enumeration gives index as well as the item in the loop
        """
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()  # new line after each row


def deposit():
    while True:
        amount = input("What is your deposit? \n$: ")
        # input query check, convert string to int
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("amount must be greater than 0.")
        else:
            print("Please enter a number.")
    return amount


# collect bet
def get_num_of_lines():
    while True:
        lines = input(
            "enter number of lines to bet on [1 -> " + str(MAX_LINES) + "]? \n: "
        )
        # input query check, convert string to int
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("enter valid number of lines")
        else:
            print("Please enter a number.")
    return lines


def get_bet():
    while True:
        amount = input("What is your bet, on each line? \n $: ")
        # input query check, convert string to int
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"amount must be between ${MIN_BET} <-> ${MAX_BET}.")
        else:
            print("Please enter a number.")
    return amount

def play_round(balance):

    lines = get_num_of_lines()
    # check if bet balance fit bet lines
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(
                f"You do not have enough to bet that amount, your current balance is: ${balance}"
            )
        else:
            break

    print(
        f"You're betting ${bet} on {lines} lines.\n Total bet is equal to: ${total_bet}"
    )

    print("Balance:", balance, "Bet lines:", lines)

    slots = get_slot_machine_spin(SLOT_ROWS, SLOT_COLS, symbol_count)
    print_slots_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"| You earn |  \n     $ {winnings}")
    print(f"You won on lines\n    ", *winning_lines)

    return winnings - total_bet

def main():
    
    balance = deposit()
    while True:
        print(f"Current Balance: $ {balance}")
        spin = input("Press enter to bet \n(q to quit).")
        if spin == "q":
            break
        balance += play_round(balance)
    print(f"You plundered a total of \n     ${balance} \n thank you for playing!\n GAMBLE RESPONSIBLY! ")

main()
