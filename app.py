def calculate_simple_interest(principal, rate, time):
    """
    Calculate the simple interest.

    Parameters:
    principal (float): The principal amount.
    rate (float): The annual interest rate (in percentage).
    time (float): The time period in years.

    Returns:
    float: The simple interest.
    """
    simple_interest = (principal * rate * time) / 100
    return simple_interest

# Example usage
principal_amount = float(input("Enter the principal amount: "))
annual_rate = float(input("Enter the annual interest rate (in percentage): "))
time_period = float(input("Enter the time period in years: "))

simple_interest = calculate_simple_interest(principal_amount, annual_rate, time_period)
print(f"The simple interest is: {simple_interest}")
