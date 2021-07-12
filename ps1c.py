annual_salary = float(input("Enter the starting salary:​ "))
# annual_salary = 150000

total_cost = 1_000_000
semi_annual_raise = .07
portion_down_payment = 0.25
r = 0.04    # Return on investment
total_months = 0
current_savings = 0.0

def down_payment(annual_salary: int, portion_saved: float,  total_cost: int,
    portion_down_payment: float, r: float, semi_annual_raise: float,
    semi_annual_raise_after = 6
) -> int:
    total_months = 0
    current_savings = 0.0

    while total_cost * portion_down_payment > current_savings:
        if total_months != 0 and (total_months % semi_annual_raise_after) == 0:
            annual_salary *= 1 + semi_annual_raise

        return_on_investment = current_savings * (r / 12)
        investment = (annual_salary / 12) * portion_saved

        current_savings += return_on_investment + investment
        total_months += 1
    return total_months

moths = 36
bisections = 0
low = 0
high = 10_000
high_before = high
# ! Lower this value for a more accurate answer / more bisections !
# ! Must be positive !
epsilon = 1
savings_accuracy = 4 # In numbers after the decimal

while abs(low - high) >= epsilon:
    guess = (high + low) / 2.0
    payment_guess = down_payment(annual_salary, guess / high_before, total_cost, portion_down_payment, r, semi_annual_raise)

    # print(payment_guess)
    # print(guess, low, high)

    if moths < payment_guess: low = guess
    else: high = guess

    bisections += 1

if high == high_before:
    print(f"It is not possible to pay the down payment in {moths / 12} years.")
else:
    print(f"Best savings rate:​ {round(guess / high_before, savings_accuracy)}")
    print(f"Steps in bisection search:​ {bisections}")
