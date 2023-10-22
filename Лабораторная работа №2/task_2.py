salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

money_capital = 0

for _ in range(months):
    cheak = spend - salary  # тратим ежемесячеую зарплату (остается "долг")
    spend = spend * increase + spend  # начисляются проценты
    money_capital += cheak  # считаем сколько нужно денег, чтобы выплатить "долг"

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital, 2))
