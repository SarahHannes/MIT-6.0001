ori_annual_salary = int(input('Enter the starting salary: '))
annual_salary = ori_annual_salary
monthly_salary = annual_salary/12
semi_annual_increment = 0.07
total_cost = 1000000
down_payment = total_cost*0.25
r = 0.04
current_saving = 0
months = 0
months_inc = 0

precision = 25 #end savings need to be within $100 of the required down payment
low = 0
high = 10000
mid = ((low*10000)+high)/2/10000.0
num_guesses = 0

while current_saving < down_payment:
    while months != 36:
        if months_inc == 6:
            annual_salary = annual_salary + (annual_salary * semi_annual_increment)
            monthly_salary = annual_salary/12
            months_inc = 0

        total_roi = current_saving * r / 12
        current_saving += (monthly_salary * mid) + total_roi
        months_inc += 1
        months += 1

    if months == 36 and current_saving < down_payment:
        low = mid
        annual_salary = ori_annual_salary
        current_saving = 0
        months = 0
        months_inc = 0

    elif months == 36 and abs(current_saving-down_payment) >= precision:
        high = mid
        annual_salary = ori_annual_salary
        current_saving = 0
        months = 0
        months_inc = 0

    if high == 10000:
        mid = round(((low * 10000) + high) / 2 / 10000.0, 4)
    else:
        mid = round(((low * 10000) + (high * 10000)) / 2 / 10000.0, 4)

    num_guesses += 1
    if mid >= 0.9:
        print('It is not possible to pay the down payment in three years.')
        break
else:
    low = 0
    high = 1000
    print('Best saving rate:', mid)
    print('Steps in bisection search:', num_guesses)