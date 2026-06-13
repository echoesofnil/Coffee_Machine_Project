# ☕ Coffee Machine Project

A simple Python-based Coffee Machine simulation that allows users to order coffee, process payments, manage resources, and generate reports.

## Features

* Order different types of coffee:

  * Espresso
  * Latte
  * Cappuccino
* Checks if enough ingredients are available before preparing a drink.
* Accepts coin payments (quarters, dimes, nickels, and pennies).
* Calculates and returns change.
* Tracks profit earned.
* Displays available resources and profit through a report command.
* Supports turning off the machine using the `off` command.

## Technologies Used

* Python 3
* Dictionaries
* Functions
* Loops and Conditional Statements

## Project Structure

```python
MENU        # Coffee menu with ingredients and cost
resources   # Available ingredients

check_resources()  # Checks ingredient availability
process_coins()    # Calculates inserted money
make_coffee()      # Deducts ingredients and serves coffee
coffee_machine()   # Main program loop
```

## How to Run

1. Clone this repository:

```bash
git clone https://github.com/your-username/coffee-machine.git
```

2. Navigate to the project folder:

```bash
cd coffee-machine
```

3. Run the program:

```bash
python coffee_machine.py
```

## Example Usage

```text
What would you like? (espresso/latte/cappuccino): latte
Please insert coins.
How many quarters?: 10
How many dimes?: 0
How many nickles?: 0
How many pennies?: 0

Here is your latte. Enjoy! ☕
```

## Commands

| Command    | Description                       |
| ---------- | --------------------------------- |
| espresso   | Order Espresso                    |
| latte      | Order Latte                       |
| cappuccino | Order Cappuccino                  |
| report     | Show current resources and profit |
| off        | Turn off the machine              |

## Learning Outcomes

This project helped me practice:

* Python Functions
* Dictionaries and Nested Dictionaries
* Loops
* Conditional Logic
* Resource Management
* User Input Handling

## Future Improvements

* Add more drink options.
* Save profit and resources in a file.
* Create a graphical user interface (GUI).
* Add inventory refill functionality.

## Author

Developed by Nilakshi as part of Python learning and project practice.
