def display_mailing_label(name, address, city, state, zip_code):
    print(name)
    print(address)
    print(f"{city}, {state} {zip_code}")

display_mailing_label(
    "Alondra Martinez",
    "1234 Main St",
    "Charlotte",
    "NC",
    "28202"
)

display_mailing_label(
    "John Smith",
    "456 Oak Ave",
    "Atlanta",
    "GA",
    "30303"
)
# add numbers
def add_numbers(*numbers):
    total = sum(numbers)
    expression = " + ".join(str(num) for num in numbers)
    print(f"{expression} = {total}")

add_numbers(1, 2, 3)
add_numbers(10, 20, 30, 40)

# Receipt

def display_reciept(total_due, amount_paid):
    
    print(f"Total Due: ${total_due}")
    print(f"Amount paid: ${amount_paid}")

    if amount_paid >= total_due:
        
        change_due = amount_paid - total_due

        print(f"\nChange Due: ${change_due}")

    else: 
        remaining_balance = total_due - amount_paid

        print(f"\nRemaining Balance: ${remaining_balance}")

display_reciept(20, 30)
display_reciept(50, 25)
