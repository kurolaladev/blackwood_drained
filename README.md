# Blackwood: Drained ☆☆☆

**Blackwood: Drained** é um jogo de ficção interativa no formato *Text Adventure* (RPG textual de terminal) desenvolvido em Python. A aplicação coloca o jogador na pele de um caçador investigando eventos nefastos na fictícia e sufocante cidade de Blackwood, Louisiana, combinando elementos de suspense noir, investigação forense e terror sobrenatural.

O projeto foi construído com foco na **experiência do usuário (UX) em CLI**, aplicando conceitos sólidos de **mecanismos de controle de fluxo**, manipulação de tempo de execução, tratamento rígido de *inputs* e arquitetura modular de código segundo as diretrizes da **PEP 8**.

---

## Funcionalidades e Mecânicas ☆☆☆

- **Efeito de Imersão Textual:** Renderização de texto estilo *typewriter* (máquina de escrever) com pauses calculados para construção de atmosfera narrativa.
- **Árvore de Decisões e Múltiplos Finais:** Escolhas com peso narrativo real que alteram o estado do jogo (inventário implícito) e ramificam a história para 3 finais distintos (*Bom*, *Neutro* e *Ruim*).
- **Tratamento Rigoroso de Inputs:** Sistema de validação contra entradas inválidas no terminal via *loops* de checagem e limpeza de buffer ANSI, impedindo a quebra do fluxo da partida.
- **Interface Limpa em Terminal:** Manipulação de chamadas de sistema para limpeza de tela (`clear`/`cls`), garantindo foco e clareza visual a cada cena.

---

## Estrutura e Modularidade do Código ☆☆☆

O script `main.py` foi projetado com foco em **modularidade e legibilidade**, separando a engine do jogo do conteúdo narrativo propriamente dito:

* `narrar(texto)`: Responsável por controlar a cadência de exibição do texto no terminal, gerenciar o tempo de pausa e validar a progressão por meio de confirmação do usuário (tecla Enter).
* `fazer_escolha(opcoes)`: Função de interface genérica que renderiza menus numerados dinamicamente e valida se a resposta do usuário está dentro do intervalo de opções permitidas.
* **Gerenciamento de Estado:** Utilização de flags de inventário (`tem_poeira`, `tem_endereco`, `tem_instinto`) que determinam caminhos lógicos nas estruturas condicionais do jogo.

> **Nota técnica:** Todas as funções possuem *Docstrings* detalhadas no padrão PEP 257 e o código atende às convenções estéticas de legibilidade da PEP 8.

---

## Como Executar o Projeto ☆☆☆

### Pré-requisitos
Para rodar o jogo, você precisa apenas do **Python 3.x** instalado em sua máquina (sem necessidade de instalação de dependências externas, utilizando estritamente a *Standard Library*).

### Passo a Passo
1. Clone este repositório ou baixe o arquivo `main.py`.
2. Abra o terminal (ou prompt de comando) na pasta onde o arquivo foi salvo.
3. Execute o programa com o seguinte comando:
   ```bash
   python main.py

(Compatível também com o ambiente Pydroid 3 em dispositivos Android).
Guia de Testes dos Finais ☆☆☆

Para validar o funcionamento da árvore de decisões e testar a integridade de todos os textos, siga as rotas abaixo durante a execução:

    Final Ruim (Derrota): Escolha [1] Consultar contatos na investigação ➔ Escolha [2] Ignorar e seguir viagem na estrada.

    Final Neutro (O Abismo): Escolha [1] Consultar contatos na investigação ➔ Escolha [1] Frear bruscamente na estrada.

    Final Bom (Sucesso): Escolha [2] Investigar a vida da vítima na investigação ➔ Siga a rota da Igreja.

Autoria ☆☆☆

    Desenvolvido por: Lya
