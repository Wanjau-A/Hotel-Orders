**Python POS System: Local Cuisine Menu**
A lightweight, command-line interface (CLI) application designed to process food orders from a pre-defined menu. This script handles user input, validates items against available stock, and calculates the total bill dynamically.

**The Menu**
The system supports a variety of local and international dishes, including:
Starters & Snacks: Samosa, Smocha, Taco
Main Meals: Kienyeji Fry and Ugali, Pilau Beef, Mukimo and Beef
Combos: Fries Masala and Sausage, Chapati Quarter Chicken
Beverages: Smoothies

**Features**
Input Validation: Automatically formats user input to match menu keys (e.g., "smocha" becomes "Smocha").
Error Handling: Gracefully handles invalid items and "End of File" (EOF) interruptions.
Real-time Logic: Continuously accepts orders until the user signals they are finished.
Summary Report: Provides a full list of ordered items and a total price in KES.

**Installation & Usage**
Prerequisites
Python 3.x installed on your machine.

**Running the App**
Clone or Copy the script to your local machine:

    Bash
    git clone https://github.com/yourusername/pos-system-python.git
    cd pos-system-python
Run the script using your terminal:

    Bash
    python pos_script.py
Follow the prompts:

Type the name of the dish you want.

Press Enter to add it.
When finished, press Ctrl + D (Linux/Mac) or Ctrl + Z then Enter (Windows) to generate your bill.

**Code Structure**
The project is built using a clean, functional approach:
MENU: A dictionary constant containing item names as keys and prices as values.
compute_total(): A helper function that iterates through the order list to calculate the sum.
main(): The entry point that manages the user interaction loop and exception handling.

Example Session
Plaintext
Place an order: smocha
Added Smocha to your list.
Place an order: pilau beef
Added Pilau Beef to your list.
Place an order: [Ctrl+D]

Finalizing Order
Your order: Smocha, Pilau Beef
Your total bill is ksh.650

This project is open-source and available under the MIT License.

Would you like me to help you add a feature that allows users to specify quantities (e.g., "2 Samosas")?
