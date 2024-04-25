from ModulesAndImports import add
# Exercise 1.1: Variables and Basic Data Types

name = "Ante"
age = 27
color = "black"

print("My name is {}, I am {} years old, and my favorite color is {}.".format(name, age, color))



# Exercise 1.2: Control Flow - If-Else Statements
num = int(input("\nPlease enter a number: "))
if (num % 2 == 0):
    print("Even")
else: print("Odd")

# Exercise 1.3: Loops - Creating a Multiplication Table
print(f"\nMultiplication table for {num}:")
for i in range(1, 11):
    mTable = num * i
    print(f"{num} x {i} = {mTable}")
    
# Exercise 1.4: Functions - Fibonacci Series
def fibonacci(num):
    a, b = 0, 1
    print("\nFibonacci sequence: ")
    for i in range(num):
        print(a, end=" ")
        a, b = b, a + b
fibonacci(num)

# Exercise 2.1 Lists and List Comprehension
def filterPosNumbers(nums):
    posNumbers = [number for number in nums if number > 0]
    return posNumbers

nums = [3, -9, 0, 35, -2, 11, -28, 10]

posNums = filterPosNumbers(nums)
print("\n\nList of positive numbers: ", posNums)

# Exercise 2.2 Dictionaries - Word Frequencies
def count_words(text):
    words = text.lower().split()
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

text = input("Please enter a string(Sentences): ")
word_counts = count_words(text)
print("\nWord counts:")
for word, count in word_counts.items():
    print(f"{word}: {count}")
    
# Exercise 2.3 File I/O - Reading and Writing
def reverse_text_file(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            content = file.read()
        print("\nContents of the input file:")
        print(content)
        reversed_content = content[::-1]
        with open(output_file, 'w') as file:
            file.write(reversed_content)
        print(f"\nReversed content written to {output_file}\n")
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    
input_file = 'input.txt'
output_file = 'output.txt'
reverse_text_file(input_file, output_file)

# Exercise 2.4: Error Handling - Dividing Numbers
def divide_numbers():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 / num2
        print(f"The result of dividing {num1} by {num2} is: {result}")
    except ValueError:
        print("Error: Please enter valid numbers.")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.\n")
divide_numbers()

# Exercise 3.1: Classes and Objects - Simple Bank Account
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"\nDeposited ${amount:.2f}. New balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Error: Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")

    def print_balance(self):
        print(f"Account balance for account number {self.account_number}: ${self.balance:.2f}\n")

# Example for the BankAccount class
account = BankAccount("123456")
account.deposit(500)
account.withdraw(100)
account.print_balance()

# Exercise 3.2 Modules and Imports
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

result = add(a, b)
print(f"The sum if {a} and {b} is: {result}")