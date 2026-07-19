import os

# Nomes dos arquivos de armazenamento
ARQUIVO_USUARIOS = "usuarios.txt"
ARQUIVO_PRODUTOS = "produtos.txt"

# ==============================================================================
# FUNÇÕES DE GERENCIAMENTO DE ARQUIVOS (PERSISTÊNCIA)
# ==============================================================================

def carregar_usuarios():
    """Lê o arquivo de usuários e retorna uma lista de dicionários."""
    usuarios = []
    # Se o arquivo não existir, cria um usuário admin padrão para teste
    if not os.path.exists(ARQUIVO_USUARIOS):
        with open(ARQUIVO_USUARIOS, "w", encoding="utf-8") as f:
            f.write("admin,admin123,gerente\n")
            f.write("user,user123,funcionario\n")
            
    with open(ARQUIVO_USUARIOS, "r", encoding="utf-8") as f:
        for linha in f:
            linha = linha.strip()
            if linha:
                dados = linha.split(",")
                if len(dados) == 3:
                    usuarios.append({
                        "username": dados[0],
                        "password": dados[1],
                        "permissao": dados[2]
                    })
    return usuarios

def salvar_usuarios(usuarios):
    """Grava a lista de usuários atualizada no arquivo."""
    with open(ARQUIVO_USUARIOS, "w", encoding="utf-8") as f:
        for u in usuarios:
            f.write(f"{u['username']},{u['password']},{u['permissao']}\n")

def carregar_produtos():
    """Lê o arquivo de produtos e retorna uma lista de dicionários."""
    produtos = []
    if not os.path.exists(ARQUIVO_PRODUTOS):
        # Cria alguns produtos iniciais de exemplo
        with open(ARQUIVO_PRODUTOS, "w", encoding="utf-8") as f:
            f.write("101,Placa de Video RTX 4060,2100.00,15\n")
            f.write("102,Processador Core i5,1150.00,20\n")
            f.write("103,Memoria RAM 16GB,350.00,50\n")

    with open(ARQUIVO_PRODUTOS, "r", encoding="utf-8") as f:
        for linha in f:
            linha = linha.strip()
            if linha:
                dados = linha.split(",")
                if len(dados) == 4:
                    produtos.append({
                        "codigo": dados[0],
                        "nome": dados[1],
                        "preco": float(dados[2]),
                        "quantidade": int(dados[3])
                    })
    return produtos

def salvar_produtos(produtos):
    """Grava a lista de produtos atualizada no arquivo."""
    with open(ARQUIVO_PRODUTOS, "w", encoding="utf-8") as f:
        for p in produtos:
            f.write(f"{p['codigo']},{p['nome']},{p['preco']},{p['quantidade']}\n")

# ==============================================================================
# CRUD DE USUÁRIOS (Apenas Gerente acessa por completo)
# ==============================================================================

def criar_usuario(usuarios):
    print("\n--- Cadastrar Novo Usuário ---")
    username = input("Digite o nome de usuário (login): ").strip()
    
    # Verifica se já existe
    for u in usuarios:
        if u['username'] == username:
            print("Erro: Este usuário já existe!")
            return
            
    password = input("Digite a senha: ").strip()
    permissao = input("Digite a permissão (gerente/funcionario): ").strip().lower()
    
    if permissao not in ['gerente', 'funcionario']:
        print("Permissão inválida! Escolha 'gerente' ou 'funcionario'.")
        return
        
    usuarios.append({"username": username, "password": password, "permissao": permissao})
    salvar_usuarios(usuarios)
    print(f"Usuário '{username}' cadastrado com sucesso!")

def listar_usuarios(usuarios):
    print("\n--- Lista de Usuários do Sistema ---")
    for u in usuarios:
        print(f"Usuário: {u['username']} | Permissão: {u['permissao']}")

def atualizar_usuario(usuarios):
    print("\n--- Atualizar Senha/Permissão ---")
    username = input("Digite o nome do usuário que deseja atualizar: ").strip()
    for u in usuarios:
        if u['username'] == username:
            u['password'] = input("Digite a nova senha: ").strip()
            nova_perm = input("Digite a nova permissão (gerente/funcionario): ").strip().lower()
            if nova_perm in ['gerente', 'funcionario']:
                u['permissao'] = nova_perm
                salvar_usuarios(usuarios)
                print("Usuário atualizado com sucesso!")
            else:
                print("Permissão inválida. Alterações descartadas.")
            return
    print("Usuário não encontrado.")

def deletar_usuario(usuarios, usuario_logado):
    print("\n--- Deletar Usuário ---")
    username = input("Digite o nome do usuário a ser removido: ").strip()
    if username == usuario_logado:
        print("Erro: Você não pode deletar a si mesmo!")
        return
        
    for u in usuarios:
        if u['username'] == username:
            usuarios.remove(u)
            salvar_usuarios(usuarios)
            print(f"Usuário {username} removido com sucesso.")
            return
    print("Usuário não encontrado.")

# ==============================================================================
# CRUD DE PRODUTOS OU SERVIÇOS
# ==============================================================================

def criar_produto(produtos):
    print("\n--- Cadastrar Novo Produto ---")
    codigo = input("Código do produto: ").strip()
    for p in produtos:
        if p['codigo'] == codigo:
            print("Erro: Já existe um produto com este código!")
            return
            
    nome = input("Nome do produto: ").strip()
    try:
        preco = float(input("Preço: R$ "))
        quantidade = int(input("Quantidade em estoque: "))
    except ValueError:
        print("Erro: Preço ou Quantidade inválidos!")
        return
        
    produtos.append({"codigo": codigo, "nome": nome, "preco": preco, "quantidade": quantidade})
    salvar_produtos(produtos)
    print("Produto cadastrado com sucesso!")

def buscar_produto(produtos):
    print("\n--- Buscar Produto ---")
    opcao = input("Buscar por (1) Código ou (2) Nome? ")
    termo = input("Digite o termo de busca: ").strip().lower()
    
    encontrado = False
    for p in produtos:
        if (opcao == "1" and p['codigo'] == termo) or (opcao == "2" and termo in p['nome'].lower()):
            print(f"\n[Encontrado] Cód: {p['codigo']} | Nome: {p['nome']} | Preço: R${p['preco']:.2f} | Estoque: {p['quantidade']}")
            encontrado = True
            
    if not encontrado:
        print("Nenhum produto encontrado com esse critério.")

def listar_produtos_ordenados(produtos, critério):
    print(f"\n--- Produtos Ordenados por {critério.upper()} ---")
    if critério == "nome":
        lista_ordenada = sorted(produtos, key=lambda x: x['nome'].lower())
    elif critério == "preco":
        lista_ordenada = sorted(produtos, key=lambda x: x['preco'])
    else:
        lista_ordenada = produtos

    for p in lista_ordenada:
        print(f"Cód: {p['codigo']} | Nome: {p['nome']} | Preço: R${p['preco']:.2f} | Qtd: {p['quantidade']}")

def atualizar_produto(produtos):
    print("\n--- Atualizar Produto ---")
    codigo = input("Digite o código do produto que deseja editar: ").strip()
    for p in produtos:
        if p['codigo'] == codigo:
            print(f"Produto selecionado: {p['nome']}")
            p['nome'] = input("Novo Nome: ").strip()
            try:
                p['preco'] = float(input("Novo Preço: R$ "))
                p['quantidade'] = int(input("Nova Quantidade: "))
                salvar_produtos(produtos)
                print("Produto atualizado com sucesso!")
            except ValueError:
                print("Erro: Valores inválidos fornecidos.")
            return
    print("Produto não encontrado.")

def deletar_produto(produtos):
    print("\n--- Excluir Produto ---")
    codigo = input("Digite o código do produto que deseja deletar: ").strip()
    for p in produtos:
        if p['codigo'] == codigo:
            produtos.remove(p)
            salvar_produtos(produtos)
            print("Produto removido com sucesso!")
            return
    print("Produto não encontrado.")

# ==============================================================================
# PAINÉIS DE ACESSO (MENUS ESPECÍFICOS)
# ==============================================================================

def painel_gerente(usuario_logado, usuarios, produtos):
    while True:
        print(f"\n======================================")
        print(f" TECHNEXUS - PAINEL DO GERENTE ({usuario_logado})")
        print(f"======================================")
        print("1. Cadastrar Usuário")
        print("2. Listar Usuários")
        print("3. Atualizar Usuário")
        print("4. Deletar Usuário")
        print("--------------------------------------")
        print("5. Cadastrar Produto")
        print("6. Listar Produtos por Nome")
        print("7. Listar Produtos por Preço")
        print("8. Buscar Produto")
        print("9. Atualizar Produto")
        print("10. Deletar Produto")
        print("0. Fazer Logout")
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1": criar_usuario(usuarios)
        elif opcao == "2": listar_usuarios(usuarios)
        elif opcao == "3": atualizar_usuario(usuarios)
        elif opcao == "4": deletar_usuario(usuarios, usuario_logado)
        elif opcao == "5": criar_produto(produtos)
        elif opcao == "6": listar_produtos_ordenados(produtos, "nome")
        elif opcao == "7": listar_produtos_ordenados(produtos, "preco")
        elif opcao == "8": buscar_produto(produtos)
        elif opcao == "9": atualizar_produto(produtos)
        elif opcao == "10": deletar_produto(produtos)
        elif opcao == "0": break
        else: print("Opção inválida!")

def painel_funcionario(usuario_logado, produtos):
    while True:
        print(f"\n======================================")
        print(f" TECHNEXUS - PAINEL DO FUNCIONÁRIO ({usuario_logado})")
        print(f"======================================")
        print("1. Listar Produtos por Nome")
        print("2. Listar Produtos por Preço")
        print("3. Buscar Produto")
        print("0. Fazer Logout")
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1": listar_produtos_ordenados(produtos, "nome")
        elif opcao == "2": listar_produtos_ordenados(produtos, "preco")
        elif opcao == "3": buscar_produto(produtos)
        elif opcao == "0": break
        else: print("Opção inválida!")

# ==============================================================================
# FLUXO PRINCIPAL DO SISTEMA
# ==============================================================================

def main():
    while True:
        # Recarrega a memória sempre que volta ao menu inicial
        usuarios = carregar_usuarios()
        produtos = carregar_produtos()
        
        print("\n=== BEM-VINDO À TECHNEXUS ===")
        print("1. Fazer Login")
        print("2. Sair do Sistema")
        opcao_inicial = input("Escolha uma opção: ").strip()
        
        if opcao_inicial == "1":
            print("\n--- Tela de Login ---")
            login_user = input("Nome de Usuário: ").strip()
            login_pass = input("Senha: ").strip()
            
            autenticado = False
            for u in usuarios:
                if u['username'] == login_user and u['password'] == login_pass:
                    autenticado = True
                    print(f"\nLogin bem-sucedido! Bem-vindo(a) {login_user}.")
                    
                    if u['permissao'] == 'gerente':
                        painel_gerente(login_user, usuarios, produtos)
                    else:
                        painel_funcionario(login_user, produtos)
                    break
            
            if not autenticado:
                print("Usuário ou senha incorretos!")
                
        elif opcao_inicial == "2":
            print("Encerrando o sistema da TechNexus. Até logo!")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()