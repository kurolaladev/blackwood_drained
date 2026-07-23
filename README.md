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

### Jogar Direto no Navegador (Itch.io)
Se preferir jogar de forma instantânea sem baixar nada, você pode acessar a versão web hospedada na plataforma:
👉 **[Jogue Blackwood: Drained no Itch.io](https://kurolaladev.itch.io/blackwood-drained)**

---

### Pré-requisitos (Versão Local)
Para rodar o jogo localmente, você precisa apenas do **Python 3.x** instalado em sua máquina ou dispositivo (sem necessidade de instalar dependências externas, utilizando estritamente a *Standard Library*).

---

### No Computador (Windows / Linux / macOS) ☆☆☆

1. **Baixar o código:** Clone este repositório ou baixe o arquivo `main.py`.
2. **Abrir o Terminal:** Acesse a pasta onde o arquivo foi salvo no seu Terminal (Linux/macOS) ou Prompt de Comando / PowerShell (Windows).
3. **Executar o script:**
   * **Windows:**
     ```bash
     python main.py
     ```
   * **Linux / macOS:**
     ```bash
     python3 main.py
     
