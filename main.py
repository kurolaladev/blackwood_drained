"""
BLACKWOOD: DRAINED
------------------
Jogo de ficção interativa via terminal no estilo Text Adventure.
Linguagem: Python 3
Estilo de código: PEP 8
"""

import os
import sys
import time

# =============================================================================
# CONSTANTES E CONFIGURAÇÕES DO SISTEMA
# =============================================================================

VELOCIDADE_TEXTO = 0.02
PAUSA_SISTEMA = 1.0


# =============================================================================
# FUNÇÕES UTILITÁRIAS / INTERFACE
# =============================================================================

def narrar(texto: str) -> None:
    """Exibe o texto com efeito de máquina de escrever e aguarda confirmação.

    Itera sobre os caracteres da string aplicando um delay definido e
    exige a tecla Enter para avançar. Limpa entradas inválidas da tela.

    Args:
        texto (str): O trecho narrativo a ser exibido no terminal.
    """
    for letra in texto:
        print(letra, end='', flush=True)
        time.sleep(VELOCIDADE_TEXTO)

    while True:
        entrada = input(" ➔ ").strip()
        if entrada == "":
            break
        # Apaga a linha anterior no terminal caso o usuário digite algo além do Enter
        sys.stdout.write("\033[F\033[K")
    print()


def fazer_escolha(opcoes: list[str]) -> str:
    """Apresenta um menu de escolhas numeradas e valida a entrada do jogador.

    Garante que o jogador digite apenas o número correspondente a uma
    das opções válidas fornecidas.

    Args:
        opcoes (list[str]): Lista de strings contendo os textos das opções.

    Returns:
        str: O número escolhido pelo jogador como string (ex: '1', '2').
    """
    while True:
        print("\nEscolha uma opção:")
        for i, opcao in enumerate(opcoes, 1):
            print(f"[{i}] {opcao}")

        res = input("\n> ").strip()
        opcoes_validas = [str(i) for i in range(1, len(opcoes) + 1)]

        if res in opcoes_validas:
            return res

        os.system('clear')
        print("⚠️  Opção inválida! Digite apenas o número da sua escolha.\n")


# =============================================================================
# ESTADO DO JOGO / INVENTÁRIO
# =============================================================================

tem_poeira = False
tem_endereco = False
tem_instinto = False


# =============================================================================
# FLUXO PRINCIPAL DO JOGO
# =============================================================================

os.system('clear')

print("BLACKWOOD: DRAINED\n")
time.sleep(PAUSA_SISTEMA)

# -----------------------------------------------------------------------------
# CENA 1: INTRODUÇÃO E A IGREJA
# -----------------------------------------------------------------------------

narrar("O ar em Blackwood é espesso; ele gruda nas entranhas como um parasita.")
narrar("Você estaciona o carro em frente à antiga Igreja de São Judas Tadeu. "
       "A cruz de madeira imponente, cravada na parede descascada, te observa "
       "como um sentinela silencioso sob a tarde acinzentada.")
narrar("Há um trilho de sangue: ele corta o solo e morre nos fundos da construção. "
       "Você segue o rastro escarlate até a porta do almoxarifado.")
narrar("Uma fita amarela de contenção policial atravessa o batente, mas o plástico "
       "está enfraquecido, cedendo ao tempo. Você o retira sem esforço. Gira a maçaneta "
       "lentamente. Está trancada.")

print("[SISTEMA]: Digite o número da opção desejada e pressione Enter.")

escolha_porta = fazer_escolha([
    "Arrombar a porta com um chute.",
    "Usar clips resistentes e abrir furtivamente."
])

os.system('clear')

if escolha_porta == "1":
    narrar("O silêncio da igreja quase abandonada não te intimida. Você se posiciona, "
           "respira fundo e dá um chute certeiro na porta. O impacto ecoa como um trovão.")
else:
    narrar("Com paciência, você cria uma chave improvisada e consegue destrancar a porta "
           "sem fazer barulho. O silêncio permanece intacto.")

narrar("​Dentro da sala, o odor metálico invade suas narinas, brigando com o cheiro "
       "persistente de mofo. Teias de aranha cobrem os cantos das paredes. Você está "
       "totalmente sozinho na escuridão.")
narrar("​Tateia os bolsos e acende sua lanterna. O clique ecoa e uma luz trêmula e "
       "amarelada corta o quarto empoeirado. No chão, uma mancha escura - era o que havia "
       "restado de uma enorme poça de sangue.")
narrar("​Você aponta o feixe de luz para a parede em ruínas. A silhueta de um relógio "
       "de madeira escura surge diante dos seus olhos. Os ponteiros estão parados "
       "exatamente às 2h45 da manhã.")
narrar("​Ao se aproximar, você nota algo impossível: o vidro está condensado por dentro; "
       "cristais de gelo cobrem os números. Você toca a madeira e sente um frio cortante "
       "atingir as pontas de seus dedos – uma heresia térmica diante do mormaço "
       "sufocante da Louisiana lá fora.")
narrar("​Você conhece esse sinal.")
narrar("O sobrenatural não pertence a este lugar e a natureza reage tentando congelar "
       "a ferida aberta na realidade. Onde o profano caminha, o mundo se manifesta em rejeição.")
narrar("​O que passou por aqui não era humano.")
narrar("​Você deixa a sala gélida e hostil. A mancha de sangue fica para trás como uma "
       "promessa de trazer justiça. Ao chegar no carro, nota que seus sapatos estão mais "
       "sujos do que deveriam.")

# Escolha da Sujeira
escolha_sujeira = fazer_escolha([
    "Ignorar a sujeira.",
    "Bater a poeira com as mãos."
])

os.system('clear')

if escolha_sujeira == "1":
    narrar("Você entra no carro e dá partida no motor com um suspiro longo; um pouco de "
           "pó não te incomodaria.")
elif escolha_sujeira == "2":
    tem_poeira = True
    narrar("Você nota uma coloração amarelada e um odor acre. Ao esfregar o pó entre "
           "os dedos, a textura é peculiar – não parece sujeira comum.")
    narrar("Você limpa as mãos nas calças e dá partida no motor, perdido em pensamentos.")
    print("[SISTEMA: Você obteve 'Poeira Estranha']\n")
    time.sleep(PAUSA_SISTEMA)
else:
    narrar("Você decide não perder tempo com isso e dá partida no motor.")

# -----------------------------------------------------------------------------
# CENA 2: O NECROTÉRIO
# -----------------------------------------------------------------------------

narrar("Cada rua de Blackwood que passa diante de seus olhos parece um presságio. "
       "O céu acinzentada reflete no painel do carro, uma luz pálida e quase nauseante.")
narrar("Em poucos minutos, você estaciona diante do necrotério: uma construção de "
       "concreto branco, indiferente e comum demais para o horror que guarda.")
narrar("Você desce do carro e entra. Seus passos ecoam pesados no piso de linóleo.")
narrar("Para diante do balcão, soltando a respiração lentamente enquanto o cheiro "
       "de antisséptico invade seus pulmões.")
narrar("A recepcionista te encara com um sorriso intenso, exagerado – quase como se "
       "aquele lugar precisasse forçar uma normalidade que não existe.")

# Escolha da Abordagem
escolha_abordagem = fazer_escolha([
    "Sustenta o olhar e saca o distintivo falso.",
    "Acena brevemente e mostra o distintivo por dentro do casaco."
])

os.system('clear')

if escolha_abordagem == "1":
    narrar("Sem hesitar, você o exibe com autoridade e anuncia que está ali para uma "
           "perícia federal no cadáver da Igreja de São Judas.")
    narrar("Você não pede – ordena confiantemente.")
elif escolha_abordagem == "2":
    narrar("Com um tom de voz baixo e controlado, você evita o sorriso da mulher.")
    narrar("Pede acesso ao corpo do incidente na São Judas, mantendo uma postura "
           "discreta para não atrair olhares indesejados.")
else:
    narrar("Você mostra o distintivo de qualquer jeito, querendo apenas acabar logo com aquilo.")

narrar("Ela assente com hesitação e levanta-se, saindo detrás do balcão. O som dos saltos "
       "contra o linóleo é irritante de tão rítmico.")
narrar("Você a segue até uma gaveta metálica e fria. Quando ela a puxa, o cheiro "
       "metálico misturado ao formol faz suas narinas arderem instantaneamente.")
narrar("Após expor o corpo mutilado, a mulher estende a mão enluvada em sua direção, "
       "um gesto silencioso de 'está por sua conta'.")
narrar("Ela se retira com passos calculados, deixando você para trás com o silêncio "
       "denso e opressor da morte.")

# Exame do Corpo
narrar("Você puxa as luvas de látex, o estalo do elástico soando como um tiro no "
       "quarto vazio.")
narrar("Não foi uma morte rápida. Os ferimentos são agressivos, profundos, mas "
       "estranhamente precisos. Há uma intenção ali; parece ter sido quase pessoal, "
       "ou pelo menos muito cruel.")
narrar("Você pega a prancheta com o relatório preliminar. Seus olhos correm pelas notas: "
       "Hipovolemia severa. Ausência de 85% do volume sanguíneo total.")
narrar("Com olhar confuso, franze a testa. O relatório deixa claro: o sangue não foi "
       "drenado ali, e a poça da igreja não era tão massiva quanto deveria ser.")
narrar("Isso porque ele foi levado ou consumido.")
narrar("No pescoço e braços, a luz amarelada revela o que você temia: marcas de "
       "furos profundos e cortes irregulares. Algo se alimentou e rasgou a carne ao "
       "mesmo tempo.")
narrar("A brutalidade sugere algo animalesco, mas a eficiência do dreno aponta "
       "para um predador clássico.")
narrar("A ideia de um vampiro — algo cruel, insaciável — cruza sua mente como uma "
       "sombra indesejada.")

# Checagem condicional de item
if tem_poeira:
    print("[SISTEMA: Sua mente faz uma conexão...]\n")
    time.sleep(PAUSA_SISTEMA)
    narrar("Mas então, você se lembra do que viu na igreja. O vidro condensado, a poeira "
           "amarela no seu sapato.")
    narrar("Algo causa um ruído na sua linha de raciocínio; vampiros são predadores de "
           "sangue, mas o que você encontrou antes parecia... diferente.")
    narrar("Quase como se o cenário e o corpo estivessem contando histórias distintas.")
else:
    narrar("Você encara o corpo em silêncio, tentando processar a sede daquela criatura.")

narrar("Seu longo suspiro ecoa pela sala melancólica, vívido demais para um lugar que "
       "deveria ser o fim de tudo.")
narrar("Você desliza o cadáver de volta para o descanso frio da gaveta metálica. O som "
       "do metal batendo é seco, final.")
narrar("Sem pressa, dobra o relatório forense e o enfia no bolso do casaco, sentindo o "
       "peso do papel contra o peito. Ao sair, a recepcionista esquisita continua lá. O "
       "sorriso desconfortável ainda engole o rosto dela – estático, como se tivesse sido "
       "esculpido em cera.")
narrar("Você não diz nada. Apenas assente curtamente com a cabeça e atravessa a porta "
       "de vidro. A brisa úmida da rua te atinge como um soco, mas você entra no carro "
       "em silêncio e fecha a porta, deixando Blackwood do lado de fora por um instante "
       "enquanto o motor ruge para um horizonte incerto e distante.")
narrar("O carro jaz estacionado no acostamento de uma estrada deserta — a parada "
       "perfeita para sua mente inquieta. Acima de você, a sombra de um carvalho "
       "antigo se projeta como mãos retorcidas, tentando agarrar quem quer que se "
       "atreva a passar por ali.")

# -----------------------------------------------------------------------------
# CENA 3: A DECISÃO DE INVESTIGAÇÃO
# -----------------------------------------------------------------------------

narrar("No silêncio que se segue, você retira o relatório do bolso e o abre sobre o volante.")
narrar("A luz do crepúsculo é ruim, mas as palavras 'Ausência de Volume Sanguíneo' "
       "saltam do papel como um aviso silencioso.")

escolha_investigacao = fazer_escolha([
    "Consultar seus contatos.",
    "Investigar a vida da vítima."
])

os.system('clear')

if escolha_investigacao == "1":
    narrar("Você pega o celular e disca um número que não está na sua agenda, mas "
           "que você decorou há anos.")
    narrar("Precisa de alguém que entenda do assunto para confirmar sua teoria.")
    narrar("O estalo do celular fechando ecoa na cabine como um ponto final.")
    narrar("Depois de alguns minutos de conversa com seu contato, as evidências parecem "
           "apontar para o óbvio: um ninho de vampiros atuando nas redondezas.")
    narrar("O rastro de corpos drenados nos últimos dias não deixa muita margem para erro.")
    narrar("Você guarda o aparelho e encara a estrada escura, sentindo que o alvo "
           "finalmente ganhou um nome.")
    narrar("Sem hesitação, enfia uma longa e afiada faca de prata e uma garrafa de água "
           "benta dentro de sua maleta: está na hora de acabar com o mal pela raíz – "
           "ou pelo pescoço.")
    narrar("Dá dois tapas no coldre de sua pistola carregada de balas sagradas e assente "
           "com a cabeça.")

elif escolha_investigacao == "2":
    tem_endereco = True
    narrar("Você ignora o próprio cansaço e percorre cada linha do relatório, forçando "
           "os olhos contra a luz fraca do painel.")
    narrar("No rodapé de uma das páginas amassadas, você encontra o que buscava: um "
           "nome com o mesmo sobrenome da vítima e um número de contato.")
    narrar("Apanha o celular e disca sem hesitar; a conversa com o familiar é breve, "
           "mas as informações trocadas pesam no ar.")
    narrar("Você encerra a ligação com um clique seco, sentindo que o rumo da "
           "investigação acaba de mudar.")
    print("[SISTEMA: Você obteve 'Endereço do Familiar']\n")
    time.sleep(PAUSA_SISTEMA)

narrar("Então arremessa o relatório no banco do passageiro e dá partida no motor.")
narrar("A noite nessas redondezas não costuma perdoar quem fica parado por muito tempo.")
narrar("Agora, você corta o asfalto rumo à parte mais isolada da cidade.")

# =============================================================================
# RAMIFICAÇÃO A: JOGADOR NÃO POSSUI O ENDEREÇO DO FAMILIAR
# =============================================================================

if not tem_endereco:
    narrar("Você corta as ruas solitárias de Blackwood quando um calafrio súbito "
           "percorre sua espinha, travando sua respiração por um segundo longo demais.")
    narrar("Há algo de errado. O rastro das casas antigas e decrépitas que passam pela "
           "janela parece um mau presságio, uma dissonância que grita mais alto que a "
           "localização do ninho.")
    narrar("O ar ali parece mais pesado.")

    escolha_estrada = fazer_escolha([
        "Frear bruscamente (Confiar no instinto).",
        "Ignorar e seguir viagem."
    ])

    os.system('clear')

    if escolha_estrada == "1":
        tem_instinto = True
        narrar("Você confia no seu instinto. O faro de caçador diz que o perigo pode "
               "estar escondido naquelas paredes descascadas do outro lado da rua.")
        print("[SISTEMA: Você obteve 'Instinto de Caçador']\n")
        time.sleep(PAUSA_SISTEMA)
    else:
        narrar("Você aperta os olhos contra a estrada e suspira fundo.")
        narrar("O tempo é curto, a manhã se aproxima e você não pode se dar ao luxo "
               "de deixar o rastro dos vampiros esfriar por causa de um palpite.")

    os.system('clear')

    # -------------------------------------------------------------------------
    # FINAL 1: NEUTRO
    # -------------------------------------------------------------------------
    if tem_instinto:
        narrar("Você desce do carro e chuta a porta da casa. O cheiro de enxofre e gelo "
               "seco é tão forte que queima suas narinas.")
        narrar("No centro da sala, você vê um homem sendo despedaçado por algo que veste "
               "pele humana, mas é pálido demais e possui olhos que são apenas dois "
               "buracos negros.")
        narrar("A vítima se contorce no chão, tentando escapar de garras que se fincam "
               "profundamente em sua carne.")
        narrar("Por um milésimo de segundo, você jura ver o reflexo de asas celestiais sob "
               "o corpo dele — uma sombra impossível que pisca junto com a lâmpada falha "
               "do teto.")
        narrar("Em um pânico controlado, você descarrega a arma nas costas da criatura.")
        narrar("Sem parar para recarregar, chuta um galão de querosene sobre os sigilos de "
               "sangue no chão. As chamas sobem, azuis e erráticas, reagindo violentamente "
               "ao sangue celestial.")
        narrar("O demônio solta um guincho que rasga o ar. Ele recua, mas antes de sumir "
               "pela fresta que se fecha no espaço-tempo, vira o rosto — uma máscara de "
               "carne derretida — e fixa os olhos em você. Uma promessa silenciosa.")
        narrar("O rapaz no chão solta um suspiro final. A cabeça pende para o lado. Sem vida.")
        narrar("Você encara o assoalho, aterrorizado pelos símbolos desconhecidos desenhados "
               "em sangue. Logo abaixo do cadáver do anjo, uma mancha esbranquiçada começa "
               "a se espalhar.")
        narrar("Gelo.")
        narrar("Um calafrio percorre sua espinha enquanto as peças do quebra-cabeça se "
               "encaixam à força na sua mente.")
        narrar("Você vira as costas para aquele antro de profanação. Seja lá o que tenha "
               "presenciado, é muito maior do que uma simples caçada; você não erradicou o mal, "
               "apenas o interrompeu.")
        narrar("Você pisa fundo, decidido a se afastar o máximo possível de Blackwood. Sua "
               "única chance é tentar despistar o Abismo, que agora sabe seu nome.")
        narrar("Por alguns minutos, o vento morno e úmido da estrada te traz um falso senso "
               "de segurança.")
        narrar("No entanto… seu sangue congela nas veias quando o relógio do painel trava "
               "em números específicos.")
        narrar("2h45 da madrugada.")
        print("\n--- [FINAL 1: NEUTRO - O ABISMOS SABE SEU NOME] ---\n")

    # -------------------------------------------------------------------------
    # FINAL 2: RUIM
    # -------------------------------------------------------------------------
    else:
        narrar("Você segue até um galpão abandonado.")
        narrar("Ao se aproximar da porta, o cheiro metálico que emana lá de dentro confirma "
               "sua intuição; você já espera encontrar um mar de sangue, o banquete perfeito "
               "para um ninho de vampiros.")
        narrar("Ao chutar a porta, vê um homem parado bem no meio da sala insalubre e "
               "mal iluminada. Ele parece em transe. Sob seus pés, há uma poça de sangue "
               "muito menor do que o esperado.")
        narrar("Sem hesitar, você dispara uma bala de prata, confiante. Ele cai com um "
               "baque surdo e pesado, sem emitir um único som. O silêncio te faz hesitar por "
               "um instante; aquilo é incomum.")
        narrar("Você se aproxima a passos lentos, em guarda. Quando está perto o suficiente, "
               "saca sua faca de prata e corta o pescoço da criatura em um golpe veloz "
               "e agressivo.")
        narrar("O sangue jorra, mas é espesso, negro e queima sua pele como ácido ao tocar sua mão.")
        narrar("Subitamente, uma mão quente e impossivelmente forte agarra seu pescoço.")
        narrar("Num piscar de olhos, a criatura se levanta e te joga no chão sem esforço. "
               "A cabeça dela se conecta ao tronco novamente, como se o seu golpe tivesse "
               "sido apenas um incômodo.")
        narrar("Ela sorri — um rasgo macabro que vai de orelha a orelha. Sua consciência "
               "se esvai enquanto a criatura aperta sua garganta com uma força sobre-humana.")
        narrar("O cheiro insuportável de enxofre invade seus pulmões no lugar do ar e é "
               "a única coisa que te mantém consciente.")
        narrar("Os olhos dela tornam-se dois abismos inteiramente negros. Você a encara "
               "por um último segundo antes de sentir uma dor lancinante: as garras da "
               "criatura mergulham no seu abdômen, revirando suas entranhas.")
        narrar("Num último suspiro vão, você tenta soltar um urro de agonia, mas sua "
               "voz morre junto com a esperança…")
        narrar("Você falhou na caçada.")
        narrar("Trouxeste estacas para o apocalipse. O que está diante de si não teme a "
               "sede; ele teme apenas a luz que você não soube encontrar.")
        print("\n--- [FINAL RUIM: DERROTA ABSOLUTA] ---\n")

# =============================================================================
# RAMIFICAÇÃO B: JOGADOR POSSUI O ENDEREÇO DO FAMILIAR (FINAL BOM)
# =============================================================================

else:
    narrar("Você estaciona o carro diante de uma casa de madeira acinzentada, o jardim "
           "crescido parece ter desistido de lutar contra a própria natureza selvagem.")
    narrar("Ao bater na porta, é recebido por uma mulher de olhar cansado; a irmã mais "
           "velha da vítima.")
    narrar("Lá dentro, o cheiro de café velho e incenso preenche a sala. Ela fala do "
           "rapaz com uma reverência dolorosa.")
    narrar("Diz que era a alma da São Judas – um homem que dedicou cada segundo à comunidade "
           "e à fé. Alguém que todos amavam, mas que poucos realmente conheciam.")
    narrar("Com a permissão da mulher, você sobe até o quarto dele. O ambiente é simples, "
           "quase espartano, mas exala uma paz que não combina com a brutalidade que você "
           "viu no necrotério.")
    narrar("Enquanto você vasculha uma cômoda de carvalho, ouve o ranger dos degraus.")
    narrar("A jovem entra no quarto segurando um livro de capa de couro desgastada, "
           "apertando-o contra o peito antes de estendê-lo em sua direção.")
    narrar("— Acho que deveria ver isto… Pode ser que te ajude na investigação. Era importante "
           "para ele.")
    narrar("Você assente em silêncio e guarda o volume sob o braço. Ao se despedir, o "
           "peso do livro parece aumentar a cada passo.")
    narrar("De volta ao carro, sob a luz fraca do painel, você o abre.")
    narrar("Não é um diário comum. As páginas estão repletas de uma caligrafia elegante, "
           "descrevendo uma existência que remete às lendas que percorrem as rodas de "
           "conversa dos caçadores.")
    narrar("A vítima não era apenas um homem religioso; era um Principado. Um sentinela "
           "celestial que vigiava a cidade pacata há muito tempo.")
    narrar("Você guarda o diário no banco do passageiro. O peso daquelas palavras é "
           "quase físico.")
    narrar("Então engata a marcha e faz o caminho de volta; está na hora de retornar "
           "ao lugar onde tudo começou.")

    # Retorno à Igreja
    os.system('clear')
    narrar("A Igreja de São Judas Tadeu parece ainda mais fúnebre sob o manto da noite.")
    narrar("As janelas coloridas de vidro fosco não deixam a luz sair, mas você sente a "
           "pulsação do que está acontecendo lá dentro.")
    narrar("Desta vez, não vai pelos fundos. Você caminha até a entrada principal e "
           "empurra as portas duplas de carvalho. O ranger da madeira ecoa pelo altar "
           "como um desafio.")
    narrar("Lá dentro, o ar é denso, carregado com o cheiro de ozônio e enxofre.")
    narrar("No centro do corredor principal, onde antes ficavam os bancos de oração, "
           "agora existe um selo complexo e grotesco, desenhado com um sangue que ainda "
           "pulsa em um tom dourado-doentio: o sangue do Principado.")
    narrar("Três figuras estão paradas ao redor do círculo. À primeira vista, parecem homens "
           "comuns, mas a forma como a luz falha reflete em seus olhos totalmente negros "
           "revela a verdade.")
    narrar("Eles param o que estão fazendo e cravam olhares predatórios em você, os "
           "rostos distorcidos em sorrisos famintos.")
    narrar("Você para no início do corredor. O destino de Blackwood está a poucos metros "
           "de distância.")

    escolha_final = fazer_escolha([
        "Sacar a arma com munição abençoada com sangue angelical.",
        "Chacoalhar a cabeça em negação e usar o papel do diário do Principado."
    ])

    os.system('clear')

    if escolha_final == "1":
        narrar("Você sente o peso extra do carregador. Cada bala ali foi mergulhada na "
               "água benta e encharcada com o sangue angelical que você coletou na cena "
               "do crime, seguindo as instruções do diário.")
        narrar("Se eles querem sangue, você vai entregar o tipo que queima. Dispara tiros "
               "rápidos contra os demônios disfarçados, que se contorcem de dor ao sangrarem "
               "e partem rapidamente em sua direção, irados. Seus olhos parecem faiscar de ódio.")
    else:
        narrar("Você encara os abismos negros nos olhos daquelas coisas com um desprezo frio.")
        narrar("— Que Deus tenha misericórdia de vocês — você murmura, com a mão já tateando "
               "o papel dobrado no bolso.")
        narrar("Seu objetivo é claro, você quer encerrar aquele ciclo de heresia e morte "
               "que está assombrando a cidadezinha.")

    # Clímax do Final Bom
    narrar("Então você arremessa uma página amarelada no centro do círculo.")
    narrar("É um pedaço arrancado do diário, coberto por uma caligrafia em sangue que "
           "parece vibrar no papel.")
    narrar("As palavras são escritas em uma linguagem que fere os olhos; uma geometria "
           "impossível que não deveria existir na realidade.")
    narrar("Os demônios rugem em uníssono, um som de metal retorcido, e avançam. Mas você "
           "não recua.")
    narrar("Com os pés firmes sobre o solo profanado, começa a falar. Palavras em "
           "enoquiano antigo escapam de seus lábios com dificuldade — uma língua que "
           "você nunca estudou, mas que flui com a autoridade de um trovão, guiada pela "
           "vontade do Principado.")
    narrar("As criaturas travam. Elas tremem, os corpos possuídos entrando em convulsão "
           "enquanto tentam romper a barreira invisível que sua voz está erguendo.")
    narrar("O ar ao redor se torna subitamente gélido, cristalizando o mormaço típico de "
           "Louisiana em questão de segundos.")
    narrar("Você tateia o bolso e retira o item final: uma pedra preciosa que pulsa com "
           "as cores de um arco-íris preso em cristal.")
    narrar("Ela queima sua palma com um calor sagrado, quase macia ao toque, como se "
           "estivesse viva. É a Graça do anjo — a essência que ele destilou de si mesmo "
           "antes do fim.")
    narrar("Sem hesitar, você a arremessa no coração do ritual, fecha os olhos e se encolhe.")

    os.system('clear')
    narrar("Uma explosão de luz branca, pura e absoluta, devora a escuridão da igreja.")
    narrar("O som que se segue não é de fogo, mas um zumbido ensurdecedor misturado aos "
           "gritos agônicos dos demônios sendo arrancados a força de seus corpos.")
    narrar("O impacto te joga contra o chão frio.")
    narrar("Quando você finalmente abre os olhos, o silêncio é absoluto.")
    narrar("Onde a luz tocou, símbolos antigos daquela mesma linguagem ficaram marked "
           "como cicatrizes de sombra permanente.")
    narrar("No lugar dos demônios, jazem apenas cadáveres humanos mutilados – Seus olhos "
           "foram reduzidos a buracos negros e profundos, que ainda soltam uma leve "
           "fumaça acre e cinzenta.")
    narrar("Você se levanta com dificuldade, o mundo ainda girando. Bate a poeira da "
           "roupa com gestos mecânicos, sentindo o zumbido nos ouvidos diminuir aos poucos.")
    narrar("Diante do altar, você faz o sinal da cruz. Quase sente como se o próprio "
           "Senhor estivesse te encarando através das gravuras detalhadas de anjos "
           "pintadas nas paredes e no teto.")
    narrar("Ao atravessar as portas da igreja, o peso em sua alma é quase palpável.")
    narrar("A pequena cidadezinha de Blackwood finalmente desfrutará de uma noite "
           "tranquila; sua caçada foi um sucesso.")
    narrar("O mormaço da Louisiana voltou, mas o seu sangue continua frio.")
    narrar("Você salvou a cidade, mas agora carrega uma certeza amarga: o que tentou "
           "entrar pela igreja de São Judas foi apenas a primeira batida de uma porta "
           "que o Inferno pretende derrubar por inteiro.")
    print("\n--- [FINAL BOM: A CAÇADA FOI UM SUCESSO] ---\n")

# ==================================================================================================
# fim do script :D
# ==================================================================================================
