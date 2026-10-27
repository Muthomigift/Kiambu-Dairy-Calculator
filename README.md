Kiambu Dairy Co-op Payment Calculator:

A simple command-line tool that tells a farmer how much they are owed for the milk they supplied, based on the current buying price.

Features:
1. Asks for the farmer's name and litres supplied.
2. Reads the current buying price from price.txt
3. Falls back to a default price of KES 55 litres if price.txt is missing.
4. Validates inputs.
5. Prints a clear summary with the total owed.

Setup instructions:
1. Clone this project.
2. Create a file named price.txt in the same folder as dairy_calculator.py, containing only the current price per litre.
3. To update the weekly rate, edit the number in price.txt. No code changes are needed.

Example of the output:
Kiambu Dairy Co-op Payment Calculator
-------------------------------------
Current buying price: KES 55.00 per litre

Farmer name: Chokera Gift
Litres supplied today: 100

Farmer  : Chokera Gift
Litres  : 100.0
Price   : KES 55.00/litre
Total   : KES 5,500.00