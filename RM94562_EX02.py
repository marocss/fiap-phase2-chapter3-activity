# A compra de um veículo pode ser realizada parcelada. Crie um programa que receba o valor de
# um carro e mostre uma tabela com os seguintes dados: preço final, quantidade de parcelas e
# valor da parcela. Considere o seguinte:
# a) O preço final para compra à vista tem um desconto de 20%:
# b) A quantidade de parcelas pode ser 6, 12, 18, 24, 30, 36, 42, 48, 54 e 60:

# Os percentuais de acréscimo seguem na tabela abaixo:

# +------------------------+----------------------------------+
# | Quantidade de Parcelas | Percentual de Acréscimo sobre o  |
# |                        | preço final                      |
# +------------------------+----------------------------------+
# | 6                      | 3%                               |
# | 12                     | 6%                               |
# | 18                     | 9%                               |
# | 24                     | 12%                              |
# | 30                     | 15%                              |
# | 36                     | 18%                              |
# | 42                     | 21%                              |
# | 48                     | 24%                              |
# | 54                     | 27%                              |
# | 60                     | 30%                              |
# +------------------------+----------------------------------+

# Modelo de saída:

# Digite o preço do carro: 20000
# O preço final à vista com desconto 20% é: 16000.0
# O preço final parcelado em 6 X é de R$ 20600,00 com parcelas de R$ 3433,33
# O preço final parcelado em 12 X é de R$ 21200,00 com parcelas de R$ 1766,67
# O preço final parcelado em 18 X é de R$ 21800,00 com parcelas de R$ 1211,11
# O preço final parcelado em 24 X é de R$ 22400,00 com parcelas de R$ 933,33
# O preço final parcelado em 30 X é de R$ 23000,00 com parcelas de R$ 766,67
# O preço final parcelado em 36 X é de R$ 23600,00 com parcelas de R$ 655,56
# O preço final parcelado em 42 X é de R$ 24200,00 com parcelas de R$ 576,19
# O preço final parcelado em 48 X é de R$ 24800,00 com parcelas de R$ 516,67
# O preço final parcelado em 54 X é de R$ 25400,00 com parcelas de R$ 470,37
# O preço final parcelado em 60 X é de R$ 26000,00 com parcelas de R$ 433,33

def get_user_input() -> float:
    while True:
        try:
            car_price = float(input('Digite o preço do carro: '))
            if car_price <= 0:
                raise ValueError

            return car_price
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


def calculate_car_price():
    in_cash_discount = 0.2
    interest_increase_per_installments_options = 0.03
    installments_increase_per_option = 6
    number_of_payment_options = 11  # à vista, 6, 12, 18,...

    car_price = get_user_input()

    for index in range(number_of_payment_options):
        current_number_of_installments = index * installments_increase_per_option
        current_interest = index * interest_increase_per_installments_options

        if current_number_of_installments == 0:
            in_cash_car_price = car_price * (1 - in_cash_discount)
            formatted_in_cash_discount = f'{in_cash_discount * 100:.0f}%'
            print(f'O preço final à vista com desconto {formatted_in_cash_discount} é '
                  f'{format_currency_string(in_cash_car_price)}')
        else:
            car_price_with_interest = car_price * (1 + current_interest)
            installment_price = car_price_with_interest / current_number_of_installments

            formatted_car_price_with_interest = format_currency_string(car_price_with_interest)
            formatted_installment_price = format_currency_string(installment_price)
            print(
                f'O preço final parcelado em {current_number_of_installments} X é de '
                f'{formatted_car_price_with_interest} com parcelas de {formatted_installment_price}')


def main():
    calculate_car_price()


if __name__ == '__main__':
    main()
