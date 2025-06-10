
def factorial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Factorial is only defined for non-negative integers.")
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Example usage:
try:
    num = int(input("Enter a non-negative integer: "))
    result = factorial(num)
    print(f"The factorial of {num} is {result}")
except ValueError as e:
    print(e)



# Define a function to calculate final bill with GST
def calculate_final_bill(bill_amount, gst_percent):
    """
    This function takes the original bill amount and GST percentage,
    then returns the total payable amount.
    """
    gst_amount = (gst_percent / 100) * bill_amount  # Calculate GST
    total = bill_amount + gst_amount  # Final amount
    return total  # Send back the final value

# Let's use this function
original_amount = 1000  # in INR
gst = 18  # 18% GST

final_amount = calculate_final_bill(original_amount, gst)
print(f" Final amount after {gst}% GST on ₹{original_amount} is ₹{final_amount}")
