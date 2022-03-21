import math
import sys


def addition_to_whole(number):
    if number * 10 % 10 != 0:
        return int((number * 10 // 10)) + 1
    return int(number)


def calc_number_of_monthly_payment():
    print('Enter the loan principal:')
    loan_principal = int(input())
    print('enter monthly payment:')
    month_payment = int(input())
    print('enter the loan interest:')
    loan_interest = float(input())
    i = loan_interest / (12 * 100)
    month_number = math.log(month_payment / (month_payment - i * loan_principal), 1 + i)
    month_number = addition_to_whole(month_number)
    year_number = month_number // 12
    month_number = month_number % 12
    result_text = f"it will take "
    if year_number > 0:
        result_text = result_text + f"{year_number} years" if year_number > 1 else f"{year_number} year"
    if month_number > 0:
        result_text = result_text + f' {month_number} months' if (month_number > 1) else f'{month_number} month'
    result_text = result_text + f' to repay the loan'
    print(result_text)


def calc_annuity_monthly_payment():
    print('Enter the loan principal:')
    loan_principal = int(input())
    print('Enter the number of periods:')
    periods_count = int(input())
    print('Enter the loan interest:')
    interest_rate = float(input())
    i = interest_rate / (12 * 100)
    a = loan_principal * (i * pow((1 + i), periods_count))
    a = -(-a // (pow((1 + i), periods_count) - 1))
    print(f'Your monthly payment = {a}!')


def calc_loan_principal():
    print('enter the annuity payment:')
    annuity_payment = float(input())
    print('enter the number of periods:')
    month_number = int(input())
    print('enter the loan interest:')
    loan_interest = float(input())
    i = loan_interest / (12 * 100)
    loan_principal = annuity_payment / ((i * pow(1 + i, month_number)) / (pow(1 + i, month_number) - 1))
    print(f'your loan principal = {loan_principal}!')


def main():
    print('''what do you want to calculate?
            type "n" - for number of monthly payments,
            type "a" for annuity monthly payment amount,
            type "p" - for the monthly payment:''')
    calc_type = input()
    if calc_type == 'n':
        calc_number_of_monthly_payment()
    if calc_type == 'a':
        calc_annuity_monthly_payment()
    if calc_type == 'p':
        calc_loan_principal()


def calc_payments(**kwargs):
    calc_type = kwargs['type']
    interest = 0
    if 'interest' in kwargs.keys():
        interest = kwargs['interest']

    periods = 0
    if 'periods' in kwargs.keys():
        periods = kwargs['periods']

    principal = 0
    if 'principal' in kwargs.keys():
        principal = kwargs['principal']

    payment = 0
    if 'payment' in kwargs.keys():
        payment = kwargs['payment']

    i = interest / (12 * 100)
    if calc_type == 'diff':
        month_principal = principal / periods
        total_payment = 0
        for month in range(periods):
            payment = month_principal + i * (principal - (principal * month) / periods)
            payment = addition_to_whole(payment)
            total_payment += payment
            print(f'Month {month + 1}: payment is {payment}')
        print(f'Overpayment = {total_payment - principal}')
    else:
        if principal != 0 and periods != 0 and interest != 0:
            a = principal * (i * pow((1 + i), periods))
            a = -(-a // (pow((1 + i), periods) - 1))
            print(f'Your annuity payment = {a}!')
            print(f'Overpayment = {a * periods - principal}')
        elif payment != 0 and periods != 0 and interest != 0:
            loan_principal = payment / ((i * pow(1 + i, periods)) / (pow(1 + i, periods) - 1))
            print(f'Your loan principal = {loan_principal}!')
            print(f'Overpayment = {payment * periods - loan_principal}')
        elif principal != 0 and payment != 0 and interest != 0:
            month_number = math.log(payment / (payment - i * principal), 1 + i)
            month_number = addition_to_whole(month_number)
            overpayment = payment * month_number - principal
            year_number = month_number // 12
            month_number = month_number % 12
            result_text = f"it will take "
            if year_number > 0:
                result_text = result_text + f"{year_number} years" if year_number > 1 else f"{year_number} year"
            if month_number > 0:
                result_text = result_text + f' {month_number} months' if (month_number > 1) else f'{month_number} month'
            result_text = result_text + f' to repay the loan'
            print(result_text)
            print(f'Overpayment = {overpayment}')


if __name__ == '__main__':
    param_list = sys.argv[1:]
    params_dict = {}
    if len(param_list) == 4:

        calc_type_name, calc_type = param_list[0].split('=')
        params_dict[calc_type_name.strip('--')] = calc_type
        principal_name, principal = param_list[1].split('=')
        params_dict[principal_name.strip('--')] = float(principal)
        periods_name, periods = param_list[2].split('=')
        params_dict[periods_name.strip('--')] = int(periods)
        interest_name, interest = param_list[3].split('=')
        params_dict[interest_name.strip('--')] = float(interest)
        if 'interest' not in params_dict.keys():
            print('Incorrect parameters.')
        else:
            calc_payments(**params_dict)
    elif len(param_list) == 0:
        main()
    else:
        print('Incorrect parameters.')
