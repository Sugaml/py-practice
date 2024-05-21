
"""
Jet company gives 5% commission to its sales man if their monthly sales are less than Rs. 10000
and a 10% commission if it is equal to or greater than Rs. 10000.
Write a program to calculate commission at the end of month.
"""
def calculate_commission(sales):
    if sales < 10000:
        commission = sales * 0.05
    else:
        commission = sales * 0.10
    return commission


monthly_sales = float(input("Enter the monthly sales amount: Rs. "))
commission = calculate_commission(monthly_sales)
print(f"The commission for sales of Rs. {monthly_sales} is Rs. {commission:.2f}")
