# Na oferta de um produto de crédito aos clientes, três informações são muito importantes apresentar ao cliente:
# valor da dívida, a taxa de juros e o número de parcelas para pagamento do empréstimo contraído junto à Fintech.
# Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida,
# valor dos juros, quantidade de parcelas e valor da parcela.
#
# Os juros e a quantidade de parcelas seguem a tabela:
# +------------------------+----------------------------------+
# | Quantidade de Parcelas | % de juros sobre o valor inicial |
# | da dívida              | da dívida                        |
# +------------------------+----------------------------------+
# | 1                      | 0%                               |
# | 3                      | 10%                              |
# | 6                      | 15%                              |
# | 9                      | 20%                              |
# | 12                     | 25%                              |
# +------------------------+----------------------------------+
#
# Exemplo de saída do programa:
# Digite o valor da dívida: 1000
# Total: R$ 1000,00 Juros: R$ 0,00 Número de parcelas: 1 Valor da Parcela: R$ 1000,00
# Total: R$ 1100,00 Juros: R$ 100,00 Número de parcelas: 3 Valor da Parcela: R$ 366,67
# Total: R$ 1150,00 Juros: R$ 150,00 Número de parcelas: 6 Valor da Parcela: R$ 191,67
# Total: R$ 1200,00 Juros: R$ 200,00 Número de parcelas: 9 Valor da Parcela: R$ 133,33
# Total: R$ 1250,00 Juros: R$ 250,00 Número de parcelas: 12 Valor da Parcela: R$ 104,17

def get_user_input() -> float:
    while True:
        try:
            debt = float(input('Digite o valor da dívida: '))
            if debt <= 0:
                raise ValueError

            return debt
        except ValueError:
            print('Valor inválido. Por favor, digite um número válido.\n')


def format_currency_string(number: float) -> str:
    rounded_number = round(number, 2)
    number_string = str(rounded_number)

    whole, decimal = number_string.split('.')

    if len(decimal) < 2:
        decimal += '0'

    whole_with_separator = "{:,}".format(int(whole)).replace(',', '.')
    currency_string = "R$ " + whole_with_separator + ',' + decimal

    return currency_string


def debt_table():
    debt = get_user_input()
    installments_increase_factor = 3
    max_number_of_installments_options = 5
    interest_increase_factor = 0.05     # percent
    initial_installments_interest_rate = 0.1

    current_interest_rate = 0       # no interest in one installment payments
    total_debt_value = debt * (1 + current_interest_rate)
    total_interest_value = debt * current_interest_rate
    number_of_installments = 0

    for index in range(max_number_of_installments_options):
        if index == 0:
            current_installment = index + 1
            installment_price = total_debt_value / current_installment

            print(f'Total: {format_currency_string(total_debt_value)} '
                  f'Juros: {format_currency_string(total_interest_value)} '
                  f'Número de parcelas: {number_of_installments + 1} '
                  f'Valor da Parcela: {format_currency_string(installment_price)}')

            current_interest_rate = initial_installments_interest_rate
            number_of_installments += installments_increase_factor
        else:
            total_debt_value = debt * (1 + current_interest_rate)
            total_interest_value = debt * current_interest_rate
            installment_price = total_debt_value / number_of_installments

            print(f'Total: {format_currency_string(total_debt_value)} '
                  f'Juros: {format_currency_string(total_interest_value)} '
                  f'Número de parcelas: {number_of_installments} '
                  f'Valor da Parcela: {format_currency_string(installment_price)}')

            current_interest_rate += interest_increase_factor
            number_of_installments += installments_increase_factor


def main():
    debt_table()


if __name__ == '__main__':
    main()
