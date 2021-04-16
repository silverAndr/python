import json
profit_dict = {}
pr = {}
profit = 0
profit_average = 0
i = 0
with open('companies.txt', 'r') as file:
    for line in file:
        company, form, income, outlay = line.split()
        company_name = form + ' ' + company
        profit_dict[company_name] = int(income) - int(outlay)
        if profit_dict.setdefault(company_name) >= 0:
            profit = profit + profit_dict.setdefault(company_name)
            i += 1
    if i != 0:
        profit_average = profit / i
        print(f'Средняя прибыль - {profit_average:.2f}')
    else:
        print(f'Все работают в убыток')
    pr = {'средняя прибыль': round(profit_average)}
    profit_dict.update(pr)
    print(f'Прибыль по компаниям - {profit_dict}')

with open('companies.json', 'w') as write_js:
    json.dump(profit_dict, write_js)
    js_file = json.dumps(profit_dict)
    print(f'записано в файл.')
