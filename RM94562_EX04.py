# Toda vez que um cliente realiza um resgate de uma aplicação financeira, o sistema deve calcular a alíquota
# de imposto de renda (IR) que deve ser aplicada sobre aquele resgate, considerando o número de dias que
# o valor permaneceu aplicado, conforme a tabela abaixo:
#
# Até 180 dias = alíquota de 22,5% de IR.
# De 181 a 360 dias = alíquota de 20% de IR.
# De 361 a 720 dias = alíquota de 17,5% de IR.
# Acima de 720 dias = alíquota de 15% de IR.
#
# É o que acontece, por exemplo, com o CDB - Certificado de Depósito Bancário, uma aplicação de renda fixa
# comumente oferecida pelas Fintechs. Outros investimentos em renda fixa, como LCI e LCA, respectivamente,
# Letra de Crédito Imobiliário e Letra de Crédito do Agronegócio são isentos de imposto de renda.
# Escreva um programa que receba o tipo de investimento do qual se deseja realizar
# um resgate (1 para CDB, 2 para LCI e 3 para LCA), o valor a ser resgatado e o número de dias que esse
# valor permaneceu investido e, se for o caso, calcule o valor referente ao imposto de renda.
#
# Atenção! O programa deve consistir se o investimento fornecido é válido, ou seja, 1, 2 o 3.

def get_user_investment_type_input() -> int:
    while True:
        try:
            selected_investment = int(input('Qual investimento você deseja realizar o resgate? '
                                            '(1 para CDB, 2 para LCI e 3 para LCA) '))
            if selected_investment <= 0 or selected_investment >= 4:
                raise ValueError

            return selected_investment
        except ValueError:
            print('Valor inválido. Por favor, digite um número válido.\n')


def get_user_redemption_amount() -> float:
    while True:
        try:
            redemption_amount = float(input('Qual o valor do resgate? '))
            if redemption_amount <= 0:
                raise ValueError

            return redemption_amount
        except ValueError:
            print('Valor inválido. Por favor, digite um número válido.\n')


def get_user_investment_duration() -> int:
    while True:
        try:
            investment_duration = int(input('Quantos dias esse valor permaneceu investido? '))
            if investment_duration <= 0:
                raise ValueError

            return investment_duration
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


def calculate_income_tax(selected_investment, redemption_amount, investment_duration):
    taxed_amount = 0.0
    has_income_tax = False

    if selected_investment == 1:
        has_income_tax = True

    # Até 180 dias = alíquota de 22,5% de IR.
    if investment_duration <= 180 and has_income_tax:
        income_tax = 0.225
        taxed_amount = redemption_amount * income_tax
    # De 181 a 360 dias = alíquota de 20% de IR.
    elif 181 <= investment_duration <= 360 and has_income_tax:
        income_tax = 0.20
        taxed_amount = redemption_amount * income_tax
    # De 361 a 720 dias = alíquota de 17,5% de IR.
    elif 361 <= investment_duration <= 720 and has_income_tax:
        income_tax = 0.175
        taxed_amount = redemption_amount * income_tax
    # Acima de 720 dias = alíquota de 15% de IR.
    elif investment_duration >= 721 and has_income_tax:
        income_tax = 0.15
        taxed_amount = redemption_amount * income_tax

    return taxed_amount


def main():
    selected_investment = get_user_investment_type_input()
    redemption_amount = get_user_redemption_amount()
    investment_duration = get_user_investment_duration()

    taxed_amount = calculate_income_tax(selected_investment, redemption_amount, investment_duration)

    print(f'\nO valor referente ao imposto de renda desse resgate é de {format_currency_string(taxed_amount)}.')


if __name__ == '__main__':
    main()
