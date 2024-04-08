# 1 – A Bidu é uma startup na área de Fintech fundada em 2011 que ajuda os usuários a controlar suas fontes de
# receitas, gastos, dívidas e investimentos. Ela precisa realizar uma votação para escolher qual dia da semana é o
# melhor para a realização das lives com o time da mentoria financeira. Desenvolva um programa em que os
# colaboradores informem um dos 5 dias da semana (segunda-feira, terça-feira, quarta-feira, quinta-feira e
# sexta-feira) da sua preferência para participar da live. Verifique e exiba ao final, qual dia foi o escolhido pelos
# colaboradores.
# Observação: Verifique o número de colaboradores que irão participar da votação para programar sua
# estrutura de repetição.

# Bidu
# fundada em 2011
# qual dia da semana é o melhor para realizar live
#
# verificar número de colaboradores
# colaborador informa um dia da semana. Formato: (xxxx)-feira
# verificar e exibir qual o dia escolhido

welcome_message = ('Bem-vindo(a) à votação da Bidu para escolher o melhor dia da semana para a realização '
                   'das lives com o time da mentoria financeira!\n')
message_inform_number_of_collaborators = 'Quantos colaboradores vão participar da votação? '
message_error_number_of_collaborators = 'Valor inválido. Por favor, informe um número inteiro positivo.\n'
valid_week_days = ['segunda-feira', 'terça-feira', 'quarta-feira', 'quinta-feira', 'sexta-feira']


def get_user_input(message: str) -> int:
    while True:
        number_of_collaborators = input(message)
        if number_of_collaborators.isdigit():
            is_zero = int(number_of_collaborators) == 0

            if not is_zero:
                return int(number_of_collaborators)
            else:
                print(message_error_number_of_collaborators)
                continue
        else:
            print(message_error_number_of_collaborators)
            continue


def get_collaborators_votes(number_of_collaborators: int) -> list:
    preferred_week_days_selected = []

    for index in range(number_of_collaborators):
        preferred_week_day = ''
        collaborator_number = index + 1
        while preferred_week_day not in valid_week_days:
            preferred_week_day = input(f'\nColaborador {collaborator_number}, por favor informe seu dia preferido da '
                                       f'semana para a live ({', '.join(valid_week_days)}): ').strip().lower()
            if preferred_week_day not in valid_week_days:
                print(f'Dia inválido. Por favor insira um dos seguintes dias: {', '.join(valid_week_days)}.')
            else:
                print('Obrigado pelo seu voto.')
                if collaborator_number < number_of_collaborators:
                    print('Próximo colaborador!')

        preferred_week_days_selected.append(preferred_week_day)
    else:
        print('\nFim da votação. Realizando a contagem...\n')

    return preferred_week_days_selected


def get_preferred_week_day_or_days(preferred_week_days_selected: list) -> list:
    greatest_number_of_occurrences = 0
    already_verified_week_days = []
    most_voted_week_days = []

    for week_day in preferred_week_days_selected:
        if week_day in already_verified_week_days:
            continue

        already_verified_week_days.append(week_day)
        occurrences = preferred_week_days_selected.count(week_day)

        if occurrences >= greatest_number_of_occurrences:
            previous_greatest_number_of_occurrences = greatest_number_of_occurrences
            greatest_number_of_occurrences = occurrences

            if greatest_number_of_occurrences > previous_greatest_number_of_occurrences:
                most_voted_week_days[:] = []
                most_voted_week_days.append(week_day)
            else:
                most_voted_week_days.append(week_day)

    return most_voted_week_days


# Note: liked this solution because you can find out the vote for each collaborator. don't like it because
# it takes too much time and has unnecessary complexity, like two for loops for example
def check_best_week_day():
    print(welcome_message)

    number_of_collaborators = get_user_input(message_inform_number_of_collaborators)
    print(f'Ok. A votação será realizada com {number_of_collaborators} colaboradores. '
          f'Preparando para coletar os votos...')

    preferred_week_days_selected = get_collaborators_votes(number_of_collaborators)

    most_voted_week_day_or_days = get_preferred_week_day_or_days(preferred_week_days_selected)

    if len(most_voted_week_day_or_days) == 1:
        print(f'O melhor dia para a live, de acordo com os colaboradores, é {most_voted_week_day_or_days[0]}.')
    else:
        print(f'Houve um empate para o melhor dia para a live, de acordo com os colaboradores. Os seguintes '
              f'dias receberam mais votos: {', '.join(most_voted_week_day_or_days)}.')


def main():
    check_best_week_day()


if __name__ == '__main__':
    main()
