## Alunos: LUIZA E OTÁVIO

from neo4j import GraphDatabase

class App:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

uri = "neo4j+s://364def90.databases.neo4j.io:7687"
user = "neo4j"
password = "0p9xfrz83gJ10zC2AjqALlb_9ZsQ87y2OZ9d5PjGi3Q"
app = App(uri, user, password)

def menu():
    print('\n')
    print("|| Olá! Bem-vindo à galeria de arte ||")
    print('\n')
    print("Escolha uma opção para começar:")
    print('\n')
    print("1 - Consultar Dados")
    print("2 - Cadastrar Dados")
    print("3 - Excluir Dados")
    print("4 - Atualizar Dados")
    print("5 - Relatórios")
    print("0 - Sair")
    print('\n')

def menuTabela():    
    print('\n')
    print("Agora, escolha uma tabela para realizar a ação:")
    print('\n')
    print("1 - Artistas")
    print("2 - Obras")
    print("3 - Clientes")
    print("4 - Ordens")
    print("5 - Pagamentos")    
    print("6 - Exibições")
    print("0 - Voltar")
    print('\n')

def menuRelatorios():
    print('\n')
    print("Aqui estão alguns relatórios!")
    print('\n')
    print("Escolha o relatório que deseja acessar:")
    print('\n')
    print("1 - Compras por Cliente")
    print("2 - Exibição de Obras")
    print("3 - Obras por Artista")
    print("0 - Voltar")
    print('\n')

menu()
print('\n')
opcao = int(input("Escreva aqui sua opção: "))
print('\n')

while opcao != 0:
    if opcao == 1:
        print("Opção 1 - Consultar Dados")
        menuTabela()
        opcaoExibir = int(input("Escreva aqui sua opção de tabela: "))
        while opcaoExibir != 0:
            if opcaoExibir == 1:
                print('\n')
                print('Tabela de Artistas!')                
                print('\n')
                with app.driver.session() as session:
                    result = session.run("MATCH (a:Artista) RETURN a.nome_artista AS `Nome Artista`, a.id_artista AS `ID Artista`, a.email AS `E-mail`, a.pais AS `País`")
                    for record in result:
                        print(record)
            elif opcaoExibir == 2:
                print('\n')
                print('Tabela de Obras!')                
                print('\n')
                with app.driver.session() as session:
                    result = session.run("MATCH (o:Obra) RETURN o.nome_obra AS `Nome Obra`, o.id_obra AS `ID Obra`, o.nome_artista AS `Nome Artista`, o.id_artista AS `ID Artista`, o.tipo_arte AS `Tipo de Arte`, o.data_criacao AS `Data Criação`, o.preco AS`Preço`")
                    for record in result:
                        print(record)
            elif opcaoExibir == 3:
                print('\n')
                print('Tabela de Clientes!')                
                print('\n')
                with app.driver.session() as session:
                    result = session.run("MATCH (c:Cliente) RETURN c.id_cliente AS `ID Cliente`, c.cliente_nome AS `Nome Cliente`, c.telefone AS `Telefone`, c.preferencia_arte AS `Preferência Arte`, c.cliente_endereco AS `Endereço`, c.cliente_pais AS `País`")
                    for record in result:
                        print(record)
            elif opcaoExibir == 4:
                print('\n')
                print('Todas as Ordens')
                print('\n')
                with app.driver.session() as session:
                    result = session.run("MATCH (o:Obra)<-[r:ORDENOU]-(c:Cliente) RETURN o.nome_obra as `Nome Obra`, r.data_ordem as `Data Ordem`, c.cliente_nome as `Nome Cliente`")
                    for record in result:
                        print(record)
            elif opcaoExibir == 5:
                print('\n')
                print('Todos os Pagamentos')
                print('\n')
                with app.driver.session() as session:
                    result = session.run("MATCH (c:Cliente)-[p:PAGOU]->(o:Obra) RETURN c.id_cliente AS `ID Cliente`, c.cliente_nome AS `Nome Cliente`, o.nome_obra AS `Nome Obra`, p.valor_pago AS `Valor Pagamento`")
                    for record in result:
                        print(record)
            elif opcaoExibir == 6:
                print('\n')
                print('Tabela de Exibições!')                
                print('\n')
                with app.driver.session() as session:
                    result = session.run("MATCH (e:Exibicao) RETURN e.id_obra AS `ID Obra`, e.local_exibicao AS `Local Exibição`, e.data_exibicao AS `Data Exibição`")
                    for record in result:
                        print(record)
            else:
                print("Opção inválida!")
            
            menuTabela()
            opcaoExibir = int(input("Escreva aqui sua opção de tabela: "))

    if opcao == 2:
        print("Opção 2 - Cadastrar Dados")
        menuTabela()
        opcaoCadastrar = int(input("Escreva aqui sua opção de tabela: "))
        while opcaoCadastrar != 0:
            if opcaoCadastrar == 1:
                print('\n')
                print('Tabela de Artistas!')                
                print('\n')
                print('Exemplo: Leonardo Da Vinci, 1, email@example.com, Italy')                
                print('\n')
                nome_artista = input("Nome Artista: ")
                id_artista = input("ID Artista: ")
                email = input("E-mail: ")
                pais = input("País: ")
                query = """CREATE (a:Artista {nome_artista: $nome, id_artista: $id, email: $email, pais: $pais})"""
                with app.driver.session() as session:
                    session.run(query, nome=nome_artista, id=id_artista, email=email, pais=pais)
                print("Artista inserido com sucesso!")
            elif opcaoCadastrar == 2:
                print('\n')
                print('Tabela de Obras!')                
                print('\n')
                print('Exemplo: The Mona Lisa, mona002, Leonardo Da Vinci, 1, Portrait,10-jan-1517, 200000')                
                print('\n')
                nome_obra = input("Nome Obra: ")
                id_obra = input("ID Obra: ")
                nome_artista = input("Nome Artista: ")
                id_artista = input("ID Artista: ")
                tipo_arte = input("Tipo Arte: ")
                data_criacao = input("Data Criação: ")
                preco = int(input("Preço: "))              
                with app.driver.session() as session:
                    session.run("""MATCH (a:Artista {id_artista: $id_artista}) MERGE (o:Obra {id_obra: $id_obra}) SET o.nome_obra = $nome_obra, o.tipo_arte = $tipo_arte, o.data_criacao = $data_criacao, o.preco = $preco MERGE (a)-[:CRIADA_POR]->(o)""", id_artista=id_artista, id_obra=id_obra, nome_obra=nome_obra, tipo_arte=tipo_arte, data_criacao=data_criacao, preco=preco)
                print("Obra de arte inserida com sucesso!")
            elif opcaoCadastrar == 3:
                print('\n')
                print('Tabela de Clientes!')                
                print('\n')
                print('Exemplo: C01, Mr. Arif Hossain, 01724777840, Abstract, Gulshan 1, Bangladesh')                
                print('\n')
                id_cliente = input("ID Cliente: ")
                cliente_nome = input("Nome Cliente: ")
                telefone = input("Telefone: ")
                preferencia_arte = input("Preferência Arte: ")
                cliente_endereco = input("Endereço: ")
                cliente_pais = input("País: ")
                with app.driver.session() as session:
                    session.run("""CREATE (c:Cliente {id_cliente: $id_cliente, cliente_nome: $cliente_nome, telefone: $telefone, preferencia_arte: $preferencia_arte, cliente_endereco: $cliente_endereco, cliente_pais: $cliente_pais})""",
                id_cliente=id_cliente, cliente_nome=cliente_nome, telefone=telefone, preferencia_arte=preferencia_arte,
                cliente_endereco=cliente_endereco, cliente_pais=cliente_pais)
                print("Cliente cadastrado com sucesso!")
            elif opcaoCadastrar == 4:
                print('\n')
                print('Tabela de Ordens!')                
                print('\n')
                print('Exemplo: mona002, C01, 01-jan-2023, 05-jan-2023')                
                print('\n')
                id_obra = input("ID Obra: ")
                id_cliente = input("ID Cliente: ")
                data_ordem = input("Data Ordem: ")
                data_envio = input("Data Envio: ")
                with app.driver.session() as session:
                    session.run("MATCH (o:Obra {id_obra: $id_obra}), (c:Cliente {id_cliente: $id_cliente}) MERGE (o)-[:ORDENADO_POR]->(c) ON CREATE SET o.data_ordem = $data_ordem, o.data_envio = $data_envio", id_obra=id_obra, id_cliente=id_cliente, data_ordem=data_ordem, data_envio=data_envio)
                print("Ordem cadastrada com sucesso!")
            elif opcaoCadastrar == 5:
                print('\n')
                print('Tabela de Pagamentos!')                
                print('\n')
                print('Exemplo: mona002, C01, 200000')                
                print('\n')
                id_obra = input("ID Obra: ")
                id_cliente = input("ID Cliente: ")
                valor_obra = int(input("Valor Obra: "))
                with app.driver.session() as session:
                    session.run(
                        """
                        MATCH (o:Obra {id_obra: $id_obra}), (c:Cliente {id_cliente: $id_cliente})
                        CREATE (c)-[:REALIZOU_PAGAMENTO {valor_obra: $valor_obra}]->(o)
                        """,
                        id_obra=id_obra, id_cliente=id_cliente, valor_obra=valor_obra
                    )
                print("Pagamento cadastrado com sucesso!")
            elif opcaoCadastrar == 6:
                print('\n')
                print('Tabela de Exibições!')                
                print('\n')
                print('Exemplo: mona002, E01, Museum of Art, 01-jan-2023')                
                print('\n')
                id_obra = input("ID Obra: ")
                id_exibicao = input("ID Exibição: ")
                local_exibicao = input("Local Exibição: ")
                data_exibicao = input("Data Exibição: ")
                with app.driver.session() as session:
                    session.run(
                        """
                        MATCH (o:Obra {id_obra: $id_obra})
                        CREATE (o)-[:EXIBICAO {id_exibicao: $id_exibicao, local_exibicao: $local_exibicao, data_exibicao: $data_exibicao}]->(:EXIBE)
                        """,
                        id_obra=id_obra, id_exibicao=id_exibicao, local_exibicao=local_exibicao, data_exibicao=data_exibicao
                    )
                print("Exibição cadastrada com sucesso!")
            else:
                print("Opção inválida!")
            
            menuTabela()
            opcaoCadastrar = int(input("Escreva aqui sua opção de tabela: "))

    if opcao == 3:
        print("Opção 3 - Excluir Dados")
        menuTabela()
        opcaoExcluir = int(input("Escreva aqui sua opção de tabela: "))
        while opcaoExcluir != 0:
            if opcaoExcluir == 1:
                print('\n')
                print('Tabela de Artistas!')                
                print('\n')
                id_artista = input("ID Artista: ")
                with app.driver.session() as session:
                    session.run("MATCH (a:Artista {id_artista: $id_artista}) DETACH DELETE a", id_artista=id_artista)
                print("Artista excluído com sucesso!")
            elif opcaoExcluir == 2:
                print('\n')
                print('Tabela de Obras!')                
                print('\n')
                id_obra = input("ID Obra: ")
                with app.driver.session() as session:
                    session.run("MATCH (o:Obra {id_obra: $id_obra}) DETACH DELETE o", id_obra=id_obra)
                print("Obra excluída com sucesso!")
            elif opcaoExcluir == 3:
                print('\n')
                print('Tabela de Clientes!')                
                print('\n')
                id_cliente = input("ID Cliente: ")
                with app.driver.session() as session:
                    session.run("MATCH (c:Cliente {id_cliente: $id_cliente}) DETACH DELETE c", id_cliente=id_cliente)
                print("Cliente excluído com sucesso!")
            elif opcaoExcluir == 4:
                print('\n')
                print('Tabela de Ordens!')                
                print('\n')
                print('Exemplo: mona002, C01')                
                print('\n')
                id_obra = input("ID Obra: ")
                id_cliente = input("ID Cliente: ")
                with app.driver.session() as session:
                    session.run("MATCH (o:Obra {id_obra: $id_obra})-[r:ORDENADO_POR]->(c:Cliente {id_cliente: $id_cliente}) DELETE r", id_obra=id_obra, id_cliente=id_cliente)
                print("Ordem excluída com sucesso!")
            elif opcaoExcluir == 5:
                print('\n')
                print('Tabela de Pagamentos!')                
                print('\n')
                id_obra = input("ID Obra: ")
                id_cliente = input("ID Cliente: ")
                with app.driver.session() as session:
                    session.run("MATCH (o:Obra {id_obra: $id_obra})-[r:PAGO_POR]->(c:Cliente {id_cliente: $id_cliente}) DELETE r", id_obra=id_obra, id_cliente=id_cliente)
                print("Pagamento excluído com sucesso!")
            elif opcaoExcluir == 6:
                print('\n')
                print('Tabela de Exibições!')                
                print('\n')
                id_obra = input("ID Obra: ")
                with app.driver.session() as session:
                    session.run("MATCH (o:Obra {id_obra: $id_obra})-[r:EXIBIDO_EM]->(:Exibicao) DELETE r", id_obra=id_obra)
                print("Exibição excluída com sucesso!")
            else:
                print("Opção inválida!")
            
            menuTabela()
            opcaoExcluir = int(input("Escreva aqui sua opção de tabela: "))

    if opcao == 4:
        print("Opção 4 - Atualizar Dados")
        menuTabela()
        opcaoAtualizar = int(input("Escreva aqui sua opção de tabela: "))
        while opcaoAtualizar != 0:
            if opcaoAtualizar == 1:
                print('\n')
                print('Tabela de Artistas!')                
                print('\n')
                chave = input("Digite o ID do Artista a ser atualizado: ")
                id_artista = input("ID Artista: ")
                nome_artista = input("Nome Artista: ")
                email = input("E-mail: ")
                pais = input("País: ")
                with app.driver.session() as session:
                        session.run(
                        """
                        MATCH (a:Artista {id_artista: $chave})
                        SET a.nome_artista = $nome_artista, a.email = $email, a.pais = $pais
                        """,
                        chave=chave, nome_artista=nome_artista, email=email, pais=pais
                    )
                print("Artista atualizado com sucesso!")
            elif opcaoAtualizar == 2:
                print('\n')
                print('Tabela de Obras!')                
                print('\n')
                chave = input("Digite o ID da Obra a ser atualizada: ")
                id_obra = input("ID Obra: ")
                nome_obra = input("Nome Obra: ")
                nome_artista = input("Nome Artista: ")
                id_artista = input("ID Artista: ")
                tipo_arte = input("Tipo Arte: ")
                data_criacao = input("Data Criação: ")
                preco = int(input("Preço: "))
                with app.driver.session() as session:
                    session.run(
                        """
                        MATCH (o:Obra {id_obra: $chave})
                        SET o.nome_obra = $nome_obra, o.nome_artista = $nome_artista, o.id_artista = $id_artista, o.tipo_arte = $tipo_arte, o.data_criacao = $data_criacao, o.preco = $preco
                        """,
                        chave=chave, nome_obra=nome_obra, nome_artista=nome_artista, id_artista=id_artista, tipo_arte=tipo_arte, data_criacao=data_criacao, preco=preco
                    )
                print("Obra atualizada com sucesso!")
            elif opcaoAtualizar == 3:
                print('\n')
                print('Tabela de Clientes!')                
                print('\n')
                chave = input("Digite o ID do Cliente a ser atualizado: ")
                id_cliente = input("ID Cliente: ")
                cliente_nome = input("Nome Cliente: ")
                telefone = input("Telefone: ")
                preferencia_arte = input("Preferência Arte: ")
                cliente_endereco = input("Endereço: ")
                cliente_pais = input("País: ")
                with app.driver.session() as session:
                    session.run(
                        """
                        MATCH (c:Cliente {id_cliente: $chave})
                        SET c.cliente_nome = $cliente_nome, c.telefone = $telefone, c.preferencia_arte = $preferencia_arte, c.cliente_endereco = $cliente_endereco, c.cliente_pais = $cliente_pais
                        """,
                        chave=chave, cliente_nome=cliente_nome, telefone=telefone, preferencia_arte=preferencia_arte, cliente_endereco=cliente_endereco, cliente_pais=cliente_pais
                    )
                print("Cliente atualizado com sucesso!")
            elif opcaoAtualizar == 4:
                print('\n')
                print('Tabela de Ordens!')                
                print('\n')
                chave = input("Digite o ID da Obra a ser atualizada: ")
                id_cliente = input("ID Cliente: ")
                data_ordem = input("Data Ordem: ")
                data_envio = input("Data Envio: ")
                with app.driver.session() as session:
                    session.run(
                        """
                        MATCH (o:Obra {id_obra: $chave})<-[r:ORDENOU]-()
                        SET r.id_cliente = $id_cliente, r.data_ordem = $data_ordem, r.data_envio = $data_envio
                        """,
                        chave=chave, id_cliente=id_cliente, data_ordem=data_ordem, data_envio=data_envio
                    )
                print("Ordem atualizada com sucesso!")
            elif opcaoAtualizar == 5:
                print('\n')
                print('Tabela de Pagamentos!')                
                print('\n')
                id_obra = input("ID Obra: ")
                id_cliente = input("ID Cliente: ")
                valor_obra = int(input("Valor Obra: "))
                with app.driver.session() as session:
                    session.run("MATCH (o:Obra {id_obra: $id_obra})-[r:PAGO_POR]->(c:Cliente {id_cliente: $id_cliente}) SET o.valor_obra = $valor_obra", id_obra=id_obra, id_cliente=id_cliente, valor_obra=valor_obra)
                print("Pagamento atualizado com sucesso!")
            elif opcaoAtualizar == 6:
                print('\n')
                print('Tabela de Exibições!')                
                print('\n')
                id_obra = input("ID Obra: ")
                local_exibicao = input("Local Exibição: ")
                data_exibicao = input("Data Exibição: ")
                with app.driver.session() as session:
                    session.run("MATCH (o:Obra {id_obra: $idobra})-[r:EXIBIDO_EM]->(:Exibicao) SET r.local_exibicao = $local_exibicao, r.data_exibicao = $data_exibicao", id_obra=id_obra, local_exibicao=local_exibicao, data_exibicao=data_exibicao)
                print("Exibição atualizada com sucesso!")
            else:
                print("Opção inválida!")
            
            menuTabela()
            opcaoAtualizar = int(input("Escreva aqui sua opção de tabela: "))

    if opcao == 5:
        print("Opção 5 - Relatórios")
        menuRelatorios()
        opcaoRelatorio = int(input("Escreva aqui sua opção de relatório: "))
        while opcaoRelatorio != 0:
            if opcaoRelatorio == 1:
                print('\n')
                print('Relatório: Compras por Cliente')
                print('\n')
                id_cliente = input("ID Cliente: ")
                with app.driver.session() as session:
                    result = session.run("MATCH (c:Cliente {id_cliente: $id_cliente})-[:ORDENOU]->(o:Obra) RETURN c.cliente_nome AS `Nome Cliente`, o.nome_obra AS `Nome Obra`, o.preco AS `Preço`", id_cliente=id_cliente)
                    for record in result:
                        print(record)
            elif opcaoRelatorio == 2:
                print('\n')
                print('Relatório: Exibição de Obras')
                print('\n')
                local_exibicao = input("Local Exibição: ")
                with app.driver.session() as session:
                    result = session.run("MATCH (e:Exibicao)-[:EXIBE]->(o:Obra) WHERE e.local_exibicao = $local_exibicao RETURN o.nome_obra AS `Nome Obra`, o.nome_artista AS `Nome Artista`, e.data_exibicao AS `Data Exibição`", local_exibicao=local_exibicao)
                    for record in result:
                        print(record)
            elif opcaoRelatorio == 3:
                print('\n')
                print('Relatório: Obras de um Artista')
                print('\n')
                nome_artista = input("Nome do Artista: ")
                with app.driver.session() as session:
                    result = session.run("MATCH (a:Artista {nome_artista: $nome_artista})-[:CRIADA_POR]->(o:Obra) RETURN o.nome_obra AS `Nome Obra`, o.tipo_arte AS `Tipo Arte`, o.data_criacao AS `Data Criacao`, o.preco AS `Preco`", nome_artista=nome_artista)
                    for record in result:
                        print(record)
            else:
                print("Opção inválida!")
            
            menuRelatorios()
            opcaoRelatorio = int(input("Escreva aqui sua opção de relatório: "))

    menu()
    print('\n')
    opcao = int(input("Escreva aqui sua opção: "))
    print('\n')

app.close()
