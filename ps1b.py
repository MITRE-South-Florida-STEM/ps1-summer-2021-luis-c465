annual_salary = float(input("Enter your annual salary:​ "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home:​ "))
semi_annual_raise = float(input("Enter the semi­annual raise, as a decimal:​ "))

semi_annual_raise_after = 6
portion_down_payment = 0.25
r = 0.04    # Return on investment
total_months = 0
current_savings = 0.0

while total_cost * portion_down_payment > current_savings:
    if total_months != 0 and (total_months % semi_annual_raise_after) == 0:
        annual_salary *= 1 + semi_annual_raise

    return_on_investment = current_savings * (r / 12)
    investment = (annual_salary / 12) * portion_saved

    current_savings += return_on_investment + investment
    total_months += 1

print(f"Number of months:​ {total_months}")
