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
# colaborador informa um dia da semana. Formato: (xxxx)-(feira)
# verificar e exibir qual o dia escolhido

mensagem_boas_vindas = 'boas vindas'
mensagem_informe_dia = 'informe dia: '
mensagem_informe_quantidade_colaboradores = 'colaboradores: '
mensagem_erro_informe_dia = 'erro dia'
mensagem_erro_quantidade_colaboradores = 'erro colaboradores'
dias_da_semana_validos = ['seg', 'ter', 'qua']
dias_da_semana_informados = []


def main():
    verificar_melhor_dia_da_semana()
    # check_best_week_day()


def verificar_melhor_dia_da_semana():
    numero_de_colaboradores = input(mensagem_informe_quantidade_colaboradores)

    if numero_de_colaboradores.isdigit():
        if int(numero_de_colaboradores) == 0:
            print(mensagem_erro_quantidade_colaboradores)
            verificar_melhor_dia_da_semana()

        else:
            print('numero_de_colaboradores: ', numero_de_colaboradores)

            for colaborador in range(int(numero_de_colaboradores)):
                dia_informado = ''
                while dia_informado not in dias_da_semana_validos:
                    dia_informado = input(f'colaborador {colaborador + 1}, ' + mensagem_informe_dia)
                    print('dia_informado: ', dia_informado)

                dias_da_semana_informados.append(dia_informado)
            else:
                print(f'dias_da_semana_informados: {dias_da_semana_informados}')

            maior_numero_de_ocorrencias = 0
            dia_da_semana_selecionado = ''
            dias_da_semana_verificados = []
            for dia in dias_da_semana_informados:
                print('dia: ', dia)
                if dia in dias_da_semana_verificados:
                    continue

                dias_da_semana_verificados.append(dia)
                ocorrencias = dias_da_semana_informados.count(dia)
                print('ocorrencias: ', ocorrencias)
                if ocorrencias > maior_numero_de_ocorrencias:
                    maior_numero_de_ocorrencias = ocorrencias
                    dia_da_semana_selecionado = dia
                    print('maior_numero_de_ocorrencias: ', maior_numero_de_ocorrencias)
                    print('dia_da_semana_selecionado: ', dia_da_semana_selecionado)

            else:
                print('dias_da_semana_verificados: ', dias_da_semana_verificados)
                print('dia_da_semana_selecionado: ', dia_da_semana_selecionado)

    else:
        print(mensagem_erro_quantidade_colaboradores)
        verificar_melhor_dia_da_semana()


def check_best_week_day():
    # Create an empty dictionary to store the votes
    votes = {'segunda-feira': 0, 'terça-feira': 0, 'quarta-feira': 0, 'quinta-feira': 0, 'sexta-feira': 0}

    # Ask the user for the number of collaborators who will participate in the vote
    num_collaborators = int(input('How many collaborators will participate in the vote? '))

    # Use a for loop to iterate through each collaborator and ask for their preferred day
    for i in range(num_collaborators):
        preferred_day = input('Collaborator {}: Which day of the week do you prefer for the live event? '.format(i + 1))

        # Check if the preferred day is valid, and if so, add a vote for that day
        if preferred_day in votes:
            votes[preferred_day] += 1
        else:
            print(
                'Invalid day of the week. Please enter one of the following: segunda-feira, terça-feira, '
                'quarta-feira, quinta-feira, sexta-feira')

    # Find the day with the most votes
    max_votes = max(votes.values())
    best_day = [day for day, votes in votes.items() if votes == max_votes]

    # Print the results
    print('The best day(s) for the live event, according to the collaborators, is/are: {}'.format(', '.join(best_day)))


if __name__ == '__main__':
    main()
