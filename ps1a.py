annual_salary = float(input("Enter your annual salary:​ "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home:​ "))

portion_down_payment = 0.25
r = 0.04    # Return on investment
total_months = 0
current_savings = 0.0

while total_cost * portion_down_payment > current_savings:
    total_months += 1
    return_on_investment = current_savings * (r / 12)
    investment = (annual_salary / 12) * portion_saved

    current_savings += return_on_investment + investment

print(f"Number of months:​ {total_months}")
