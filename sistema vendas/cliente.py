from database import conectar

conexao, cursor = conectar()

def formatar_telefone(telefone):
    telefone = telefone.strip()

    if not telefone.isdigit():
        return None

    if len(telefone) != 11:
        return None

    return f"({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}"

class Cliente:
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone


    def cadastrar_cliente(self):
        cursor.execute("""INSERT INTO clientes(nome, email, telefone)
                        VALUES(%s, %s, %s)""",(self.nome, self.email, self.telefone))

        conexao.commit()


    def listar_clientes(self):
        cursor.execute("SELECT * FROM clientes")

        clientes = cursor.fetchall()

        for cliente in clientes:
            id_cliente, nome, email, telefone_formatado = cliente

            print('-' * 30)
            print(f"""
ID: {id_cliente}
Nome: {nome}
E-mail: {email}
Telefone: {telefone_formatado}""")
            

    def buscar_cliente(self, nome):
        cursor.execute("""SELECT * FROM clientes
                WHERE nome LIKE %s """, (f"%{nome}%",))

        clientes = cursor.fetchall()

        if not clientes:
            print('Erro, esse cliente não consta em nossos registros.')
        else:
            for cliente in clientes:
                id_cliente, nome, email, telefone_formatado = cliente
            
                print('-' * 30)
                print(f"""
ID: {id_cliente}
Nome: {nome}
E-mail: {email}
Telefone: {telefone_formatado}""")            


    def atualizar_cliente(self, id_cliente):
        cursor.execute("""UPDATE clientes
                    SET nome = %s,
                    email = %s,
                    telefone = %s
                    WHERE id = %s""", (self.nome, self.email, self.telefone, id_cliente))
        
        conexao.commit()  

        return cursor.rowcount 

    def excluir_cliente(self, id_cliente):
        cursor.execute("""DELETE FROM clientes
                        WHERE id = %s""", (id_cliente,))
        
        conexao.commit()

        return cursor.rowcount                                     
        

while True:
    print('===== SISTEMA DE VENDAS =====\n')
    print("""
[ 1 ] - Cadastrar cliente
[ 2 ] - Listar clientes
[ 3 ] - Buscar cliente
[ 4 ] - Atualizar cliente
[ 5 ] - Excluir cliente
[ 6 ] - Sair""")

    try:
        opcao = int(input('\nEscolha: '))
    except ValueError:
        print('Erro, por favor digite um valor válido.')
        continue

    if opcao == 1:
        nome = input('\nNome do cliente: ').strip().title()

        if not nome:
            print('Inválido! Esse campo não pode ficar em branco, por preencher!')
            continue

        email = input('Email: ')

        if not '@' in email or not "." in email:
            print('email inválido, por favor, preencha novamente!')
            continue

        telefone = input('Telefone: ')

        telefone_formatado = formatar_telefone(telefone)

        if telefone_formatado is None:
            print('Telefone inválido! Digite 11 números.')
            continue

        cadastro = Cliente(nome, email, telefone_formatado)
        cadastro.cadastrar_cliente()

        print('\nCliente cadastrado com sucesso!')

    elif opcao == 2:
        listagem = Cliente('', '', '')
        listagem.listar_clientes()

    elif opcao == 3:
        nome = input('Digite o nome do cliente para a busca: ').strip().title()

        if not nome:
            print('Inválido! Esse campo não pode ficar em branco, por preencher!')
            continue

        busca = Cliente('', '', '')
        busca.buscar_cliente(nome)

    elif opcao == 4:
        try:
            id_cliente = int(input('Digite o ID do cliente para atualizar: '))
        except ValueError:
            print('inválido! Digite um valor válido!')
            continue

        novo_nome = input('Novo nome: ').strip().title()
        
        if not novo_nome:
            print('Inválido! Esse campo não pode ficar em branco, por preencher!')
            continue
        
        novo_email = input('Novo Email: ')
        
        if not '@' in novo_email or not "." in novo_email:
            print('email inválido, por favor, preencha novamente!')
            continue
        
        novo_telefone = input('Novo telefone: ')
        
        novo_telefone_formatado = formatar_telefone(novo_telefone)
        
        if novo_telefone_formatado is None:
            print('Telefone inválido! Digite 11 números.')
            continue

        atualizacao = Cliente(novo_nome, novo_email, novo_telefone_formatado)
        resultado = atualizacao.atualizar_cliente(id_cliente)

        if resultado == 0:
            print("ID não encontrado.")
        else:
            print("Cliente atualizado com sucesso!")

    elif opcao == 5:
        try:
            id_cliente = int(input('Digite o ID do cliente para excluir: '))
        except ValueError:
            print('inválido! Digite um valor válido!')
            continue

        escolha = input('Deseja mesmo excluir cliente[s/n]?  ').strip().lower()[0]

        if escolha == 'n':
            print('Ação cancelada!')
            continue

        else:
            deletar = Cliente('', '', '')
            resultado = deletar.excluir_cliente(id_cliente)

            if resultado == 0:
                print("ID não encontrado.")
            else:
                print("Cliente apagado com sucesso!")

    elif opcao == 6:
        print('Sistema encerrado!')
        break

    else:
        print('Ação inexistente! Tente novamente.')

    