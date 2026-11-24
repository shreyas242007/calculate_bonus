import sys

def CalculateBonus(salary):
    if salary < 20000:
        bonus_rate = 0.05
    elif salary >= 20000 and salary <= 40000:
        bonus_rate = 0.10
    else:
        bonus_rate = 0.15

    bonus = salary * bonus_rate
    total_salary = salary + bonus
    return bonus_rate * 100, bonus, total_salary

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            basic_salary = float(sys.argv)
            rate, bonus, final_salary = CalculateBonus(basic_salary)
            print(f"Basic Salary: Rs. {basic_salary}")
            print(f"Total Payout: Rs. {final_salary}")
        except ValueError:
            pass
