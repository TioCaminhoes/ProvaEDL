from collections import deque

class botaoavancarvoltarvisitar:
    def __init__(self):
        self.historico = deque()
        self.pagina_atual = None

    def visitar(self, pagina):
        if self.pagina_atual is not None:
            self.historico.append(self.pagina_atual)
        self.pagina_atual = pagina
        print(f"Visitando: {self.pagina_atual}")

    def avancar(self):
        if self.historico:
            self.pagina_atual = self.historico.pop()
            print(f"Avançando para: {self.pagina_atual}")
        else:
            print("Não há páginas para avançar.")

    def voltar(self):
        if self.historico:
            self.historico.append(self.pagina_atual)
            self.pagina_atual = self.historico.pop()
            print(f"Voltando para: {self.pagina_atual}")
        else:
            print("Não há páginas para voltar.")

botao = botaoavancarvoltarvisitar()
botao.visitar("Página 3")
botao.visitar("Página 2")
botao.visitar("Página 1")
botao.voltar()
botao.avancar()
botao.avancar()

### provavelmente era apenas um vetor que adicionava. Por exemplo, em um vetor 1,2,3,4 <- Estou no 4 e quero voltar uma casa, assim quando volto, faço outra ação 5. Então o vetor estaria 1,2,3,5,4.
### nesse código, utilizo uma variável para armazenar a pagina atual, e uma pilha para armazenar as paginas visitadas. Assim, quando eu quero voltar, eu apenas desempilho a pagina atual, e quando eu quero avançar, eu apenas empilho a pagina atual.

class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class FilaPacientes:
    def __init__(self):
        self.cabeca = None

    def registrarchegadapaciente(self, paciente):
        no = No(paciente)
        if not self.cabeca:
            self.cabeca = no
        else:
            atual = self.cabeca
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = no
        print(f"Paciente {paciente} registrado na fila.")

    def chamaroproximo(self):
        if not self.cabeca:
            print("Não há pacientes na fila.")
            return None
        paciente = self.cabeca.valor
        self.cabeca = self.cabeca.proximo
        print(f"Chamando paciente: {paciente}")
        return paciente

    def removerpaciente(self, paciente):
        atual = self.cabeca
        anterior = None
        while atual:
            if atual.valor == paciente:
                if anterior:
                    anterior.proximo = atual.proximo
                else:
                    self.cabeca = atual.proximo
                print(f"Paciente {paciente} removido da fila.")
                return True
            anterior = atual
            atual = atual.proximo
        print(f"Paciente {paciente} não encontrado na fila.")
        return False

    def exibirpacientes(self):
        atual = self.cabeca
        while atual:
            print(atual.valor)
            atual = atual.proximo

fila = FilaPacientes()
fila.registrarchegadapaciente("A")
fila.registrarchegadapaciente("B")
fila.registrarchegadapaciente("C")
fila.removerpaciente("A")
fila.exibirpacientes()
fila.removerpaciente("C")
fila.exibirpacientes()

### nessa lista, o ultimo não é O(1) porque a remoção de um paciente específico exige percorrer a lista até encontrar o paciente, o que pode levar um tempo maior de acordo com o tamanho da lista.
### a desistencia se torna difícil caso a fila seja muito grande, pois é necessário percorrer a lista para encontrar o paciente a ser removido.
### complexidade de tempo: O(n) para remoção de um paciente específico, O(1) para registrar chegada e chamar próximo paciente.

class Pilha:
    def __init__(self):
        self.itens = []

    def empilhar(self, item):
        self.itens.append(item)
        print(f"Empilhando: {item}")

    def desempilhar(self):
        if not self.esta_vazia():
            item = self.itens.pop()
            print(f"Desempilhando {item}")
            return item
        else:
            print("A pilha está vazia.")
            return None

    def esta_vazia(self):
        return len(self.itens) == 0

    def correcaocolchetes(self, expressao):
        pares = {'(': ')', '{': '}', '[': ']'}
        pilha = Pilha()
        for x in expressao:
            if x in pares:
                pilha.empilhar(x)
            elif x in pares.values():
                if pilha.esta_vazia() or pares[pilha.desempilhar()] != x:
                    return False
        return pilha.esta_vazia()

    def exibirfaltando(self):
        if self.correcaocolchetes(expressao):
            print("Todos os colchetes estão corretos.")
        else:
            print(f"Colchetes faltando: {expressao}") ###precisa retornar qual colchete está faltando, mas não sei como fazer isso
            while not self.esta_vazia():
                print(self.desempilhar())
pilha = Pilha()
expressao = "{[()()]"
print(pilha.correcaocolchetes(expressao))
pilha.exibirfaltando()

### o código vai empilhando assim que encontra um colchete de abertura e vai desempilhando quando encontra um colchete de fechamento. Se no final a pilha estiver vazia, significa que todos os colchetes estão corretos. Caso contrário, significa que há colchetes faltando. A função `exibirfaltando` tenta mostrar quais colchetes estão faltando, mas atualmente apenas imprime os colchetes que ainda estão na pilha. A busca é O(n) porque percorre a expressão e adiciona na pilha, mas assim que encontra o par, sua remoção é O(1). A complexidade de tempo total é O(n) para percorrer a expressão e O(1) para empilhar e desempilhar.

class Playlist:
    def __init__(self):
        self.cabeca = None

    def adicionar_musica(self, musica):
        no = No(musica)
        if not self.cabeca:
            self.cabeca = no
        else:
            atual = self.cabeca
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = no
        print(f"Música '{musica}' adicionada à playlist.")

    def remover_musica_consecutiva(self):
        atual = self.cabeca
        while atual and atual.proximo:
            if atual.valor == atual.proximo.valor:
                atual.proximo = atual.proximo.proximo
            else:
                atual = atual.proximo

    def exibir_playlist(self):
        if not self.cabeca:
            print("A playlist está vazia.")
            return
        atual = self.cabeca
        while atual:
            print(atual.valor)
            atual = atual.proximo

    def reverter_playlist(self):
        anterior = None
        atual = self.cabeca
        while atual:
            proximo = atual.proximo
            atual.proximo = anterior
            anterior = atual
            atual = proximo
        self.cabeca = anterior

playlist = Playlist()
playlist.exibir_playlist()
playlist.remover_musica_consecutiva()
playlist.exibir_playlist()
playlist.reverter_playlist()
playlist.exibir_playlist()


class ListaEncadeadaCircular:
    def __init__(self):
        self.ultimo = None

    def adicionar_servidor(self, servidor):
        no = No(servidor)
        if not self.ultimo:
            self.ultimo = no
            self.ultimo.proximo = self.ultimo
        else:
            no.proximo = self.ultimo.proximo
            self.ultimo.proximo = no
        self.ultimo = no
        print(f"Servidor '{servidor}' adicionado.")

    def obter_servidor_da_proxima_requisicao(self):
        if not self.ultimo:
            print("A lista está vazia.")
            return None
        servidor = self.ultimo.proximo.valor
        self.ultimo.proximo = self.ultimo.proximo.proximo
        return servidor
    def remover_servidor(self, servidor):
        atual = self.ultimo
        anterior = None
        while atual:
            if atual.valor == servidor:
                if anterior:
                    anterior.proximo = atual.proximo
                else:
                    self.ultimo = atual.proximo
                print(f"Servidor '{servidor}' removido da lista.")
                return True
            anterior = atual
            atual = atual.proximo
        print(f"Servidor '{servidor}' não encontrado na lista.")
        return False

    def exibir_servidores(self):
        if not self.ultimo:
            print("A lista está vazia.")
            return
        atual = self.ultimo.proximo
        while atual != self.ultimo:
            print(atual.valor)
            atual = atual.proximo

    def remover_servidor_ultimo(self):
        if not self.ultimo:
            print("A lista está vazia.")
            return None
        servidor = self.ultimo.proximo.valor
        self.ultimo.proximo = self.ultimo.proximo.proximo
        print(f"Servidor '{servidor}' removido da lista.")
        return servidor



lista = ListaEncadeadaCircular()
lista.adicionar_servidor("A")
lista.adicionar_servidor("B")
lista.adicionar_servidor("C")
lista.adicionar_servidor("D")
lista.exibir_servidores()
lista.remover_servidor("A")
lista.exibir_servidores()
lista.remover_servidor("C")
lista.exibir_servidores()
lista.remover_servidor_ultimo()
lista.exibir_servidores()

class DequePilha:
    def __init__(self):
        self.deque = deque()
        self.pilhas = deque()

    def adicionar_fim(self, item):
        self.deque.append(item)
        print(f"Realizando ação: {item}")

    def vazio(self):
        return len(self.deque) == 0

    def remover_inicio(self):
        if self.vazio() == False:
            item = self.deque.popleft()
            print(f"Removendo ação temporária: {item}")
            return item
        else:
            print("O deque está vazio.")
            return None

    def remover_fim(self):
        if self.vazio() == False:
            item = self.deque.pop()
            self.pilhas.append(item)
            print(f"Desfazendo ação: {item}")
            return item
        else:
            print("O deque está vazio.")
            return None

    def remover_pilha(self):
        if self.pilhas:
            item = self.pilhas.pop()
            self.deque.append(item)
            print(f"Refazendo ação: {item}")
            return item
        else:
            print("A pilha está vazia.")
            return None

    def exibir(self):
        print("Deque:", self.deque)
        print("Pilha:", self.pilhas)

    def menu(self):
        while True:
            print("\nMenu:")
            print("1. Fazer ação")
            print("2. Remover ação temporária")
            print("3. Desfazer ação")
            print("4. Refazer ação")
            print("5. Exibir deque e pilha")
            print("6. Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                item = input("Digite a ação a ser realizada: ")
                self.adicionar_fim(item)
            elif opcao == "2":
                self.remover_inicio()
            elif opcao == "3":
                self.remover_fim()
            elif opcao == "4":
                self.remover_pilha()
            elif opcao == "5":
                self.exibir()
            elif opcao == "6":
                print("Saindo...")
                break
            else:
                print("Opção inválida. Tente novamente.")

##deque_pilha = DequePilha()
##deque_pilha.menu()

### se utilizasse um vetor comum, a remoção de um elemento do início exigiria deslocar todos os elementos para a esquerda, resultando em uma complexidade de tempo O(n).
