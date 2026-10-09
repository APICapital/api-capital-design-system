---
titulo: "Catálogo de vetos visuais da API Capital (anti-slop)"
tipo: diretriz
status: em_construcao
dominio: design
zona: publica
bandeira: 06_marketing_api_capital
produto: api_capital
versao: 0.1
data: 2026-08-23
crivado_por: Marketing API
resumo: >-
  Os padrões que denunciam design feito por LLM, cada um com nome, o defeito, o certo e o teste.
relacionados:
  - DESIGN.md
---

# Catálogo de vetos visuais da API Capital

## Como ler

| Coluna | O que traz |
|---|---|
| **ID** | O nome do defeito. É o que o validador imprime, e o que se cita numa correção |
| **O defeito** | Como ele aparece na peça |
| **O certo** | O que fazer no lugar |
| **Teste** | O que a máquina procura. `olho` marca o que só o olho julga |

**Alcance:** `css` vale para peça em código (HTML, CSS, e-mail, tela). `pen` vale para arquivo do
Pencil e para peça montada por MCP de programa de design. `txt` vale para o texto de qualquer
peça.

---

## 1 · Cor

| ID | O defeito | O certo | Teste |
|---|---|---|---|
| `cor-fora-da-paleta` | Hex que não existe na paleta do `DESIGN.md` | Consumir token, nunca escrever hex | `css` `pen`: extrair todo hex e `rgb()` e cruzar com a paleta |
| `preto-puro` | `#000000` em texto ou fundo | Quase-preto `#171717` | `css` `pen`: procurar `#000`, `#000000`, `rgb(0,0,0)` |
| `bege-de-fundo` | Creme ou papel como fundo do documento, ou creme alternando as seções de uma peça longa | Branco puro `#FFFFFF` no `body`. O ritmo da peça longa é o cinza-claro `#F4F4F4`, nunca creme | `css`: fundo do `body` ou do container raiz em `#F1EAD8`, `#FBF9F3` ou similar; `#F1EAD8` em 2 ou mais blocos de seção irmãos |
| `parede-sem-divisao` | Peça longa com todas as seções em branco, sem nada que marque onde uma termina e a outra começa | Alternar a faixa da seção entre `#FFFFFF` e o cinza-claro `#F4F4F4` (`DESIGN.md` §Ritmo de superfície) | `css`: 4 ou mais blocos de seção irmãos, todos sem `background` próprio ou todos em `{colors.fundo}` |
| `superficie-arlequim` | A alternância vira festa: três ou mais superfícies claras na mesma peça, ou cada card com o seu fundo | Duas claras e só: branco e o cinza-claro; a faixa pinta a seção inteira, o card de dentro volta ao branco | `css`: mais de duas cores claras distintas em fundo de bloco na mesma peça |
| `vermelho-verde-livre` | Vermelho ou verde da marca usados por gosto | Vermelho só no `m` da tagline e em erro; verde só em confirmação | `css` `pen`: uso de `#B71313` ou `#0E7A47` fora de elemento de erro, alerta ou confirmação |
| `opacidade-em-vez-de-cor` | Cor sólida rebaixada com alpha para simular um tom mais claro. Não se aplica ao logo: logo com opacidade reduzida, como marca d'água, é permitido | A variação da cor, que já existe na paleta | `css` `pen`: preenchimento com `opacity` entre 0,05 e 0,6 em retângulo, célula ou fundo de bloco |
| `cinza-de-fabrica` | Cinza genérico de framework (`#F5F5F5`, `#EEE`, `#CCC`, `gray-100`) | `#E6E7E8` em bloco e borda; `#F4F4F4` em faixa de seção | `css`: cinza fora da paleta em fundo ou borda |
| `latao-segunda-cor` | Latão espalhado pela tela: botão, checkbox, texto de rótulo, borda, ícone corrente, e vira uma "segunda cor" forçada | Latão é detalhe: um número que importa, o fio do item ativo, no máximo uma caixa quente por página | `css` `pen`: `#AA7D41` ou `#9A7239` em 4 ou mais elementos distintos da mesma tela, ou em botão, checkbox, borda de campo ou rótulo |
| `checkbox-colorido` | Checkbox ou rádio em latão ou outra cor fora do sistema | Caixa branca com borda `#E6E7E8`, marca em `accent-color` azul `#0D2A54`, 8 px até o rótulo | `css`: `accent-color` diferente de `#0D2A54`; input de seleção com fundo ou borda latão |

## 2 · Sombra, brilho e profundidade

| ID | O defeito | O certo | Teste |
|---|---|---|---|
| `sombra` | Qualquer `box-shadow`, `text-shadow` ou `drop-shadow` | Separar por fundo sólido, cinza de quadro ou linha de alto contraste | `css`: propriedade presente. `pen`: nó com sombra |
| `glow` | Brilho colorido em volta de elemento | Nada. A marca não brilha | `css`: `box-shadow` com cor saturada e sem deslocamento |
| `glassmorphism` | Fundo borrado, vidro fosco, translucidez | Fundo sólido | `css`: `backdrop-filter`, `filter: blur` em container |
| `gradiente-em-elemento` | Degradê em botão, texto, ícone, caixa ou card | Gradiente só como véu de legibilidade de fundo, uma cor do transparente ao cheio | `css`: `linear-gradient` ou `radial-gradient` fora de fundo de peça; qualquer gradiente com duas cores diferentes |
| `gradiente-de-duas-cores` | Degradê entre duas cores diferentes | Uma cor só, do transparente ao cheio | `css` `pen`: contar cores distintas nas paradas |

## 3 · Forma

| ID | O defeito | O certo | Teste |
|---|---|---|---|
| `canto-fora-do-token` | `border-radius` diferente de 15 px em tela | 15 px em tela, canto vivo no impresso | `css`: todo `border-radius` que não seja 0 ou 15 |
| `pill` | Canto de `9999px`, botão ou tag em cápsula | Canto de 15 | `css`: raio acima de 40 px ou `9999px` |
| `contorno-cinza-1px` | Borda cinza clara de 1 px em volta de tudo | Fundo sólido ou fio de alto contraste | `css`: `border: 1px solid` em cinza claro, em mais de 3 elementos |
| `callout-faixa-lateral` | Caixa de destaque com faixa colorida na lateral ou no topo | Caixa do sistema: contorno, quadro, sólida, latão ou ocre | `css`: `border-left`, `border-right` ou `border-top` com espessura acima de 2 px e cor diferente das outras bordas do mesmo elemento |
| `fio-fora-da-escala` | Espessura de fio fora de 0,5 / 1 / 2 / 6 pt | As quatro espessuras do sistema | `css` `pen`: espessura de linha ou altura de retângulo divisor fora da escala |

## 4 · Tipografia

| ID | O defeito | O certo | Teste |
|---|---|---|---|
| `terceira-familia` | Uma terceira fonte além de Playfair Display e Inter | Duas famílias, e só duas | `css` `pen`: coletar `font-family` distintas |
| `antetitulo` | Rótulo miúdo em caixa alta acima do título | Subtítulo ou linha-fina, abaixo do título | `css` `pen`: texto curto, caixa alta, corpo menor que o do texto, posicionado acima de um título |
| `numero-em-serifada` | Dado apresentado em Playfair | Todo número apresentado em Inter 700 ou 800 | `css` `pen`: nó cujo conteúdo é só número, moeda ou percentual, com família serifada |
| `micro-label` | Rótulos do tipo `01 / BLOCO 03` | Nada, ou um rótulo de seção de verdade | `txt`: padrão de dois números separados por barra em caixa alta |
| `textinho` | Linha pequena e cinza carregando informação que deveria estar no texto | Subir a informação para o corpo ou virar elemento visual | `css`: corpo abaixo de 12 px com cor de baixo contraste e mais de 40 caracteres |
| `caixa-alta-em-corpo` | Parágrafo inteiro em caixa alta | Caixa alta só em rótulo de seção, com tracking | `css` `txt`: bloco de texto com mais de 30 caracteres todo em maiúscula |
| `medida-de-linha` | Linha longa demais para o olho voltar | De 6 a 8 colunas no retrato, 5 a 7 no paisagem | `css`: largura do bloco de texto acima de 90 caracteres na fonte declarada |

## 5 · Layout e ritmo

| ID | O defeito | O certo | Teste |
|---|---|---|---|
| `respiro-fora-da-escala` | Junta entre elementos que não é 60 nem 120 | Os dois valores da escala do `DESIGN.md` | `pen` `css`: medir as juntas verticais e classificar |
| `respiro-duplicado` | Duas juntas vizinhas com respiros muito diferentes | Consistência: mesma natureza de junta, mesma medida | `pen` `css`: comparar juntas do mesmo nível na mesma peça |
| `tres-colunas-identicas` | Três cards iguais no topo da página | Hierarquia de verdade, ou uma disposição própria | `css`: três irmãos de mesma largura e mesma estrutura no primeiro terço |
| `fora-da-coluna` | Elemento que começa ou termina no meio de uma coluna | Começar e terminar em coluna | `pen` `css`: cruzar as bordas com as posições da grade de 12 |
| `margem-fora-da-regua` | Margem que não é a do formato | 20 mm no A4, nas duas orientações; 4% em tela | `pen` `css`: medir a caixa útil |
| `elemento-esticado-para-tapar-buraco` | Elemento crescido para preencher o pé da página | Sobra branca no fim é aceitável | `olho` |
| `borda-serrilhada` | Elementos que declaram o mesmo alinhamento começando em verticais diferentes (logo a 40, menu a 24, texto a 56) | Uma borda de alinhamento é UMA linha: mesma vertical para todos, recuo só como degrau declarado de hierarquia | `css` `pen`: coletar a borda esquerda dos blocos de mesmo nível e acusar desvio maior que 2 px |
| `box-dentro-de-box` | Contêiner de fundo cinza agrupando campos dentro de um card que já tem fundo e borda | Campos direto sobre o fundo do card; grupo se marca com título e espaço, nunca com um segundo fundo | `css`: bloco com `background` de apoio contendo inputs, dentro de elemento que já tem borda ou fundo próprio |
| `passo-em-bolinha` | Número de passo dentro de disco ou bolinha colorida antes do título | Número no próprio título, Inter 700 tabular, na cor do título, seguido de ponto | `css`: elemento circular (`border-radius` ≥ 50%) de menos de 40 px contendo só um número |
| `botao-inventado` | Botão fora dos cinco declarados: fundo novo, texto latão, borda improvisada | Um dos cinco de §Botão; utilidade pequena é o secundário em 40 px | `css`: elemento clicável cuja combinação fundo/texto/borda não bate com nenhum dos cinco botões |
| `cabecalho-inventado` | Barra de topo de ferramenta ou página montada fora do componente | `barra-topo`: fundo azul-meia-noite, título Playfair, alturas 96/72/64 | `css`: header de página sem as propriedades do componente |

## 6 · Dado e gráfico

| ID | O defeito | O certo | Teste |
|---|---|---|---|
| `eixo-cortado` | Barra que não parte do zero | Barra do zero, sempre | `css` `pen`: valor mínimo do eixo diferente de zero em gráfico de barras |
| `grafico-sem-escala` | Gráfico sem eixo rotulado, sparkline decorativa | Eixo Y com valores | `css` `pen`: gráfico sem nó de rótulo de eixo |
| `percentual-sobre-fatia` | Número escrito em cima da fatia da rosca | Legenda ao lado, com o número | `pen`: texto centrado dentro de um setor |
| `fio-entre-linhas-de-tabela` | Linha divisória entre linhas de tabela | Zebra separa | `css` `pen`: borda horizontal repetida em linhas de tabela |
| `sem-fonte-e-data` | Tabela ou gráfico sem origem e data de apuração | Fonte e data no pé de cada um | `css` `pen`: bloco de dados sem nó de crédito abaixo |
| `rosca-sem-furo` | Gráfico de pizza cheio | Rosca, sempre com furo | `pen`: setor sem raio interno |

## 7 · Marca

| ID | O defeito | O certo | Teste |
|---|---|---|---|
| `simbolo-de-investimento` | Seta, candlestick ou gráfico como símbolo | O pelicano. A marca é o miolo | `olho` |
| `logo-remontada` | Logotipo montado à mão, letra por letra | Usar o componente oficial | `pen`: texto com o conteúdo `API` ou `CAPITAL` fora de um componente de logo |
| `logo-fora-do-oficial` | Variação de logo gerada na hora, cor trocada, proporção alterada | Só os arquivos oficiais | `css`: imagem de logo fora da pasta de assets |
| `mais-de-uma-caixa-quente` | Duas ou mais caixas latão ou ocre na mesma página | No máximo uma | `pen` `css`: contar caixas quentes por página |
| `botao-latao` | Ação em latão | Ação em azul-meia-noite ou azul-claro | `css` `pen`: elemento clicável com fundo `#AA7D41` |

## 8 · Texto da peça

| ID | O defeito | O certo | Teste |
|---|---|---|---|
| `travessao` | O símbolo `—` | Hífen, dois-pontos, ponto ou parênteses | `txt`: presença do caractere |
| `forma-nao-e-x-e-y` | A fôrma `não é X, é Y` | Reescrever no jeito falado | `txt`: expressão regular |
| `canonizar` | O verbo e suas variações | Aprovar, fechar, oficializar | `txt`: `canoniz`, `canônic` |
| `corporativês` | Mindset, disrupção, alavancar, sinergia | Palavra comum | `txt`: lista de termos |
| `emoji-decorativo` | Emoji em qualquer papel (decoração, ou no lugar de ícone, como 📎 num botão de anexo) | Nada, ou o ícone Lucide equivalente | `txt` `css`: caractere emoji em qualquer lugar da peça |
| `jargao-sem-traducao` | Termo técnico solto para quem não é do ramo | Traduzir antes de usar | `olho` |

## 9 · Acessibilidade

| ID | O defeito | O certo | Teste |
|---|---|---|---|
| `cor-sozinha-comunica` | Erro ou sucesso ditos só pela cor | Dizer em texto também | `css`: elemento de estado sem nó de texto |
| `foco-invisivel` | `outline: none` sem substituto | Anel de foco visível | `css`: `outline: none` ou `outline: 0` |
| `alvo-pequeno` | Área clicável abaixo de 44 px | 44 px de altura mínima em toque | `css`: altura declarada de botão e link em barra |

---

## O que a máquina não julga

Estes ficam com o Impeccable e com o passe humano antes da entrega. Estão listados aqui para
não sumirem, e **não** contam como veto do catálogo enquanto não tiverem teste:

- gosto de paleta e de tipografia
- ritmo de layout e cadência de leitura
- se a peça tem um momento próprio ou é montagem de blocos genéricos
- se a hierarquia diz o que importa primeiro
- se a imagem escolhida pertence ao mundo da marca

## Cobertura

O validador expõe os IDs que implementa. Um teste de cobertura confere que **todo ID deste
catálogo tem implementação, ou está declarado como `olho`**. Catálogo e validador que se descolam
viram documento passivo de novo, que é exatamente o que esta frente existe para evitar.

| Estado | Contagem |
|---|---|
| Vetos catalogados | 56 |
| Com teste declarado | 53 |
| Só olho humano (`olho`) | 3 |
| **Implementados no validador** | **0 (o validador ainda não existe)** |
