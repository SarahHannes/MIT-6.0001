def get_month_salary(annual_salary):
    # get monthly salary
    """ Returns monthly salary = annual salary / 12"""
    return annual_salary / 12


def get_month_portion(m_salary, portion_saved):
    # calc percentage of portion saved each month
    """ Returns monthly portion saved = monthly salary * (% portion saved)"""
    return m_salary * portion_saved


def get_monthly_roi(m_portion):
    # return on investment each month
    """ Returns monthly roi = (monthly salary * portion saved) * (r/12)
    where r/12 is the percent roi per month"""
    r = 0.04
    return m_portion * (r/12)


def goal_saving(total_cost):
    # calc goal saving = total cost * portion down payment
    """ Returns goal saving = total cost of dream home * (% down payment)"""
    portion_down_payment = 0.25
    return total_cost * portion_down_payment


def total_saving(m_portion, m_roi):
    # total of current saving = monthly portion saved + monthly return on investment
    """ Return total saving = monthly portion saved + monthly roi"""
    return m_portion + m_roi


user_annual_salary = int(input("Enter your annual salary:"))
user_portion_saved = float(input("Enter the percent of your salary to save, as a decimal:"))
user_total_cost = int(input("Enter the cost of your dream home:"))

goal_down_payment = goal_saving(user_total_cost)
monthly_salary = get_month_salary(user_annual_salary)
monthly_portion = get_month_portion(monthly_salary, user_portion_saved)
monthly_roi = get_monthly_roi(monthly_portion)
total_saved = total_saving(monthly_portion, monthly_roi)

months = 1
while total_saved < goal_down_payment:
    cumulative_monthly_portion = total_saved + monthly_portion
    cumulative_monthly_roi = get_monthly_roi(cumulative_monthly_portion)
    total_saved = total_saving(cumulative_monthly_portion, cumulative_monthly_roi)
    months += 1

print('Number of months:', months)