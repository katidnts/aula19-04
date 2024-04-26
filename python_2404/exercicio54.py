from tabulate import tabulate

def verificarDispnibilidade(listaFuncionario, nome, salario, cargo):

    if len(listaFuncionario) < 5:

        if cargo != 'Professor':
            funcionario = Funcionario(nome, salario, cargo)
            listaFuncionario.append(funcionario)
            print('Funcionário cadastrado')
        else:
            controleProfessores = 0
            for funcionario in listaFuncionario:
                if funcionario.cargo == 'Professor':
                    controleProfessores += 1
                    
            if controleProfessores < 2:
                funcionario = Funcionario(nome, salario, cargo)
                listaFuncionario.append(funcionario)
            else:
                print('Não há disponibilidade para cadastrar mais professores')
    else:
        print('Não há vagas')


class Funcionario():

    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo
        self.disciplinas = []


    #def mudarNome(self, nome):
     #   self.nome = nome

    def cadastrarDisciplina(self, disciplinas):
        if self.cargo == 'Professor':
            self.disciplinas.append(disciplinas)
        else:
            print('Só professores podem lecionar')


lista = []
funcionario1 = Funcionario('Renan', 1000, 'Professor')
funcionorio2 = Funcionario('Wll', 1000, 'Professor')

lista.append(funcionario1)
lista.append(funcionorio2)
verificarDispnibilidade(lista, 'Ana', 1000, 'Porteiro')
verificarDispnibilidade(lista, 'Bruno', 1000, 'Secretária')
verificarDispnibilidade(lista, 'Fernanda', 1000, 'Bibliotecária')

funcionario1.cadastrarDisciplina('Português')
lista[2].cadastrarDisciplina('Português')
#print(funcionario1.disciplinas)


data = [[funcionario.nome, funcionario.salario, funcionario.cargo]for funcionario in lista]


print(tabulate(data, headers=["Nome", "Salário", "Cargo"]))

