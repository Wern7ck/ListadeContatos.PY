def adicionar_contato(contatos, nome_contato, telefone_contato, email_contato):
    contato = {"contato": nome_contato, "telefone_contato": telefone_contato, "email_contato": email_contato, "favorito": False}
    contatos.append(contato)
    print(f"Contato {nome_contato} foi adicionado com sucesso!")
    return
def ver_contatos(contatos):
    print("\nLista de Contatos:")
    for indice, contato in enumerate(contatos, start=1):
        status = "✯" if contato["favorito"] else ""
        nome_contato = contato["contato"]
        telefone_contato = contato["telefone_contato"]
        email_contato = contato["email_contato"]
        print(f"{indice}. [{status}] {nome_contato} {telefone_contato} {email_contato}")
        return
        
def atualizar_contato(contatos, indice_contato, novo_nome_contato, novo_telefone_contato, novo_email_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        contatos[indice_contato_ajustado]["contato"] = novo_nome_contato, novo_telefone_contato, novo_email_contato
        print(f"Contato {indice_contato} atualizado para {novo_nome_contato} {novo_telefone_contato} {novo_email_contato}")
    else:
        print("Este contato não existe!")
    return
    
def favoritar_contato(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    contatos[indice_contato_ajustado]["favorito"] = True
    print(f"O Contato {indice_contato} foi marcado como favorito.")
    return
    
def apagar_contato(contatos):
    for contato in contatos:
        contatos.remove(contato)
        print("Contatos foram deletados.")
        return
        
contatos = []
while True:
  print("\nMenu do Gerenciador de Lista de contatos:")
  print("1. Adicionar contatos")
  print("2. Ver contatos")
  print("3. Atualizar contatos")
  print("4. Favoritar contatos")
  print("5. Deletar contatos")
  print("6. Sair")
  escolha = input("Digite sua escolha: ")
  if escolha =="1":
      nome_contato = input("Digite o nome do contato que deseja adicionar:")
      telefone_contato = input("Digite o telefone do contato que deseja adicionar:")
      email_contato = input("Digite o email do contato que deseja adicionar:")
      adicionar_contato(contatos, nome_contato, telefone_contato, email_contato)
  elif escolha == "2":
      ver_contatos(contatos)
  elif escolha == "3":
      ver_contatos(contatos)
      indice_contato = input("Digite o número do contato que deseja atualizar:")
      novo_nome = input("Digite o novo nome do contato:")
      novo_telefone = input("Digite o novo nome do contato:")
      novo_email = input("Digite o novo nome do contato:")
      atualizar_contato(contatos, indice_contato, novo_nome, novo_telefone, novo_email)
  elif escolha == "4":
        ver_contatos(contatos)
        indice_contato = input("Digite o número do contato que deseja favoritar:")
        favoritar_contato(contatos, indice_contato)
  elif escolha == "5":
        apagar_contato(contatos)
        ver_contatos(contatos)
  elif escolha == "6":
      break
print("Programa Finalizado.")
