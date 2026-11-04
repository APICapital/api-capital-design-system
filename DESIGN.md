---
version: "3.9"
name: "API Capital"
description: "Consultoria de investimentos independente. Clássico moderno e autoridade tranquila: azul-meia-noite e latão sobre branco puro, Playfair Display em título e Inter em todo o resto, incluindo cada número apresentado. Zero sombra, canto de 15, grade de 12 colunas. O sistema atende impresso e tela com a mesma régua, e o padrão é sempre o registro mais sóbrio."

colors:
  # Marca
  azul: "#0D2A54"
  latao: "#AA7D41"
  azul-claro: "#418ECE"
  preto: "#171717"
  branco: "#FFFFFF"
  creme: "#F1EAD8"
  areia: "#E4CB8D"
  # Variações, para estado e sobreposição
  azul-var: "#152548"
  latao-var: "#9A7239"
  azul-claro-var: "#3E82B9"
  preto-var: "#020102"
  quadro: "#E6E7E8"
  cinza-claro: "#F4F4F4"
  creme-var: "#DBD4C5"
  areia-var: "#D0B980"
  parceiro: "#5E5E5E"
  # Escopo fechado
  erro: "#B71313"
  ok: "#0E7A47"
  # Papéis
  acao: "{colors.azul}"
  acao-hover: "{colors.azul-var}"
  acao-secundaria: "{colors.azul-claro}"
  acao-secundaria-hover: "{colors.azul-claro-var}"
  texto: "{colors.preto}"
  texto-fraco: "rgba(23,23,23,0.5)"
  sobre-escuro: "{colors.branco}"
  fundo: "{colors.branco}"
  fundo-bloco: "{colors.quadro}"
  fundo-quente: "{colors.creme}"
  fundo-secao: "{colors.cinza-claro}"
  fundo-escuro: "{colors.azul}"
  borda: "{colors.quadro}"
  fio: "{colors.azul}"
  destaque: "{colors.latao}"
  realce: "{colors.areia}"
  selecao: "{colors.azul}"

typography:
  display:
    fontFamily: "'Playfair Display', Georgia, serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.96px
  secao:
    fontFamily: "'Playfair Display', Georgia, serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.72px
  titulo:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  titulo-documento:
    fontFamily: "'Playfair Display', Georgia, serif"
    fontSize: 36px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: -0.4px
  titulo-de-secao:
    fontFamily: "'Playfair Display', Georgia, serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: -0.4px
  subtitulo:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 19px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  titulo-pagina:
    fontFamily: "'Playfair Display', Georgia, serif"
    fontSize: 26px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  citacao:
    fontFamily: "'Playfair Display', Georgia, serif"
    fontSize: 22px
    fontWeight: 400
    fontStyle: italic
    lineHeight: 1.45
    letterSpacing: 0
  corpo-grande:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 19px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  corpo:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 17px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  corpo-pequeno:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  rotulo:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 4px
    textTransform: uppercase
  numero-grande:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.4px
    fontFeature: tnum
  numero:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 17px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
    fontFeature: tnum
  botao:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 17px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0
  botao-utilidade:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: 0
  botao-pequeno:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0
  legenda:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0

rounded:
  canto-vivo: 0px
  canto: 15px
  canto-ferramenta: 10px

spacing:
  x1: 4px
  x2: 8px
  x4: 16px
  x6: 24px
  x10: 40px
  x16: 64px

components:
  botao-primario:
    backgroundColor: "{colors.acao}"
    textColor: "{colors.sobre-escuro}"
    typography: "{typography.botao}"
    rounded: "{rounded.canto}"
    padding: 0 24px
    height: 48px
  botao-primario-hover:
    backgroundColor: "{colors.acao-hover}"
    textColor: "{colors.sobre-escuro}"
    typography: "{typography.botao}"
    rounded: "{rounded.canto}"
    padding: 0 24px
    height: 48px
  botao-secundario:
    backgroundColor: "{colors.fundo}"
    textColor: "{colors.acao}"
    borderColor: "{colors.acao}"
    borderWidth: 1px
    typography: "{typography.botao}"
    rounded: "{rounded.canto}"
    padding: 0 24px
    height: 48px
  botao-azul-claro:
    backgroundColor: "{colors.acao-secundaria}"
    textColor: "{colors.sobre-escuro}"
    typography: "{typography.botao}"
    rounded: "{rounded.canto}"
    padding: 0 24px
    height: 48px
  botao-sobre-escuro:
    backgroundColor: "{colors.branco}"
    textColor: "{colors.azul}"
    typography: "{typography.botao}"
    rounded: "{rounded.canto}"
    padding: 0 24px
    height: 48px
  botao-texto:
    backgroundColor: transparent
    textColor: "{colors.acao}"
    typography: "{typography.botao}"
    rounded: "{rounded.canto-vivo}"
    padding: 0
    height: 48px
  botao-utilidade:
    backgroundColor: "{colors.fundo}"
    textColor: "{colors.acao}"
    borderColor: "{colors.acao}"
    borderWidth: 1px
    typography: "{typography.botao-utilidade}"
    rounded: "{rounded.canto-ferramenta}"
    padding: 0 12px
    height: 32px
  botao-utilidade-cheio:
    backgroundColor: "{colors.acao}"
    textColor: "{colors.sobre-escuro}"
    typography: "{typography.botao-utilidade}"
    rounded: "{rounded.canto-ferramenta}"
    padding: 0 12px
    height: 32px
  campo:
    backgroundColor: "{colors.fundo}"
    textColor: "{colors.texto}"
    borderColor: "{colors.borda}"
    borderWidth: 1px
    typography: "{typography.corpo}"
    rounded: "{rounded.canto}"
    padding: 0 16px
    height: 48px
  campo-ferramenta:
    backgroundColor: "{colors.fundo}"
    textColor: "{colors.texto}"
    borderColor: "{colors.borda}"
    borderWidth: 1px
    typography: "{typography.corpo-pequeno}"
    rounded: "{rounded.canto}"
    padding: 0 12px
    height: 40px
  campo-foco:
    backgroundColor: "{colors.fundo}"
    textColor: "{colors.texto}"
    borderColor: "{colors.acao}"
    borderWidth: 1px
    outline: "3px solid {colors.acao-secundaria}"
    outlineOffset: 2px
    typography: "{typography.corpo}"
    rounded: "{rounded.canto}"
    padding: 0 16px
    height: 48px
  campo-erro:
    backgroundColor: "{colors.fundo}"
    textColor: "{colors.texto}"
    borderColor: "{colors.erro}"
    borderWidth: 1px
    typography: "{typography.corpo}"
    rounded: "{rounded.canto}"
    padding: 0 16px
    height: 48px
  card-conteudo:
    backgroundColor: "{colors.fundo}"
    textColor: "{colors.texto}"
    borderColor: "{colors.fio}"
    borderWidth: 1px
    typography: "{typography.corpo}"
    rounded: "{rounded.canto}"
    padding: 40px
  card-dado:
    backgroundColor: "{colors.fundo-bloco}"
    textColor: "{colors.texto}"
    typography: "{typography.corpo}"
    rounded: "{rounded.canto}"
    padding: 40px
  card-destaque:
    backgroundColor: "{colors.fundo-escuro}"
    textColor: "{colors.sobre-escuro}"
    typography: "{typography.corpo}"
    rounded: "{rounded.canto}"
    padding: 40px
  card-quente:
    backgroundColor: "{colors.fundo-quente}"
    textColor: "{colors.azul}"
    typography: "{typography.corpo}"
    rounded: "{rounded.canto}"
    padding: 40px
  caixa-latao:
    backgroundColor: "{colors.destaque}"
    textColor: "{colors.sobre-escuro}"
    typography: "{typography.titulo}"
    rounded: "{rounded.canto}"
    padding: 24px
  caixa-ocre:
    backgroundColor: "{colors.realce}"
    textColor: "{colors.azul}"
    typography: "{typography.corpo}"
    rounded: "{rounded.canto}"
    padding: 24px
  nav-clara:
    backgroundColor: "{colors.fundo}"
    textColor: "{colors.texto}"
    typography: "{typography.corpo}"
    padding: 0 40px
    height: 96px
  nav-escura:
    backgroundColor: "{colors.fundo-escuro}"
    textColor: "{colors.sobre-escuro}"
    typography: "{typography.corpo}"
    padding: 0 40px
    height: 96px
  aviso-erro:
    backgroundColor: "{colors.fundo}"
    textColor: "{colors.texto}"
    borderColor: "{colors.erro}"
    borderWidth: 1px
    typography: "{typography.corpo-pequeno}"
    rounded: "{rounded.canto}"
    padding: 16px
  aviso-ok:
    backgroundColor: "{colors.fundo}"
    textColor: "{colors.texto}"
    borderColor: "{colors.ok}"
    borderWidth: 1px
    typography: "{typography.corpo-pequeno}"
    rounded: "{rounded.canto}"
    padding: 16px
  tabela-cabecalho:
    backgroundColor: "{colors.fundo-escuro}"
    textColor: "{colors.sobre-escuro}"
    typography: "{typography.rotulo}"
    rounded: "{rounded.canto-vivo}"
    padding: 16px
  tabela-linha:
    backgroundColor: "{colors.fundo}"
    textColor: "{colors.texto}"
    typography: "{typography.corpo-pequeno}"
    padding: 16px
  tabela-zebra:
    backgroundColor: "{colors.fundo-bloco}"
    textColor: "{colors.texto}"
    typography: "{typography.corpo-pequeno}"
    padding: 16px
  rodape:
    backgroundColor: "{colors.fundo}"
    textColor: "{colors.texto-fraco}"
    typography: "{typography.legenda}"
    padding: 64px 40px
  barra-topo:
    backgroundColor: "{colors.fundo}"
    textColor: "{colors.azul}"
    typography: "{typography.titulo-pagina}"
    padding: 0 24px
    height: 64px
  barra-topo-escura:
    backgroundColor: "{colors.fundo-escuro}"
    textColor: "{colors.sobre-escuro}"
    typography: "{typography.titulo-pagina}"
    padding: 0 24px
    height: 64px
  content-card:
    backgroundColor: "{colors.fundo}"
    textColor: "{colors.texto}"
    typography: "{typography.corpo}"
    rounded: "{rounded.canto}"
    padding: 40px
  content-card-numero:
    backgroundColor: "{colors.fundo}"
    textColor: "{colors.azul}"
    typography: "{typography.numero-grande}"
    rounded: "{rounded.canto}"
    padding: 40px
  numero-passo:
    backgroundColor: transparent
    textColor: "{colors.azul}"
    typography: "{typography.numero}"
  checkbox:
    backgroundColor: "{colors.fundo}"
    borderColor: "{colors.borda}"
    borderWidth: 1px
    accentColor: "{colors.acao}"
    rounded: 4px
    height: 16px
    width: 16px

tipo: diretriz
status: ativo
zona: publica
dominio: design
bandeira: 06_marketing_api_capital
produto: api_capital
versao: 3.9
resumo: >-
  Especificação de design da API Capital, no formato design.md: tokens de cor, tipografia,
  espaço, forma e componente, mais as regras de layout, logo, ícone, imagem, estado e veto.
  Atende impresso e tela.
---

## Visão geral

> **⬦ marca decisão pendente de aprovação.** O resto do documento é decisão já tomada.

A API Capital é uma consultoria de investimentos que não recebe comissão de produto. O sistema
visual traduz isso em sobriedade: **azul-meia-noite** (`{colors.azul}`) como cor de autoridade
e de ação, **latão** (`{colors.latao}`) como o único calor da paleta, e **branco puro**
(`{colors.branco}`) como fundo padrão. Em peça longa, a seção alterna com o cinza-claro para
marcar onde uma parte termina e a outra começa (§Ritmo de superfície).

A tipografia trabalha em par fixo: **Playfair Display** carrega título e abertura, com tracking
negativo nos tamanhos grandes; **Inter** carrega todo o resto, e **todo número apresentado**, com
figuras tabulares. Nenhuma terceira família entra no sistema.

O sistema atende dois territórios com a mesma régua. No impresso, grade de 12 colunas, margem de
20 mm e espaçamento de 60 ou 120 px a 300 dpi. Em tela, a mesma grade em proporção, canto de 15 px
e **zero sombra em qualquer nível**: o que separa um bloco do outro é fundo sólido ou linha.

### Assinatura

- **Zero sombra, em qualquer nível.** Profundidade se faz com fundo sólido, com `{colors.fundo-bloco}` ou com linha de alto contraste.
- **Uma só cor de ação.** `{colors.acao}` no botão cheio; `{colors.acao-secundaria}` no secundário. O latão nunca é clicável.
- **Playfair com tracking negativo** de -0,96 px em 48 px, escalando até 0 no corpo. O aperto no título grande é a assinatura tipográfica.
- **Figuras tabulares em todo número apresentado**, com Inter em peso 700. Coluna de número alinha à direita.
- **Canto de 15 px em tela, canto vivo no impresso.** Cápsula é vetada.
- **Estampa tom sobre tom**, sempre a variação da cor do fundo, em preenchimento sólido.
- **Gradiente só como véu de legibilidade**, de uma cor, do transparente ao cheio, e apenas sobre fundo complexo.
- **O padrão é sóbrio.** Peso regular, hierarquia conservadora, cor contida, zero efeito. Expressividade entra depois da primeira versão.

## Cores

### Marca

| Token | Hex | Papel |
|---|---|---|
| `{colors.azul}` | `#0D2A54` | Cor principal. Título, ação, fundo sólido, marca |
| `{colors.latao}` | `#AA7D41` | Único calor da paleta. Número que importa, marcação de item ativo |
| `{colors.azul-claro}` | `#418ECE` | Ação secundária, link, série de gráfico |
| `{colors.preto}` | `#171717` | Texto de leitura |
| `{colors.branco}` | `#FFFFFF` | Fundo padrão |
| `{colors.creme}` | `#F1EAD8` | Fundo de bloco, papel de peça impressa |
| `{colors.areia}` | `#E4CB8D` | Caixa de destaque suave, textura, série de gráfico |

### Variações

Uma por cor de marca. Servem para estado sobre, para fundo de bloco sobre o próprio fundo e para
a textura. Os valores são fixos.

| Cor | Variação |
|---|---|
| `{colors.azul}` | `{colors.azul-var}` `#152548` |
| `{colors.latao}` | `{colors.latao-var}` `#9A7239` |
| `{colors.azul-claro}` | `{colors.azul-claro-var}` `#3E82B9` |
| `{colors.preto}` | `{colors.preto-var}` `#020102` |
| `{colors.branco}` | `{colors.quadro}` `#E6E7E8` |
| `{colors.creme}` | `{colors.creme-var}` `#DBD4C5` |
| `{colors.areia}` | `{colors.areia-var}` `#D0B980` |

### ⬦ Papéis

Os nomes e a divisão em papéis são derivação. Use o token de papel na peça, não o de marca. Trocar uma cor da marca passa a ser uma linha.

| Token | Aponta para | Onde |
|---|---|---|
| `{colors.acao}` | `{colors.azul}` | Botão cheio, link em destaque |
| `{colors.acao-hover}` | `{colors.azul-var}` | O mesmo botão sob o cursor |
| `{colors.acao-secundaria}` | `{colors.azul-claro}` | Botão secundário, link em corpo de texto |
| `{colors.texto}` | `{colors.preto}` | Texto de leitura |
| `{colors.texto-fraco}` | `{colors.preto}` a 50% | Legenda, fonte, crédito, nota |
| `{colors.sobre-escuro}` | `{colors.branco}` | Texto sobre fundo escuro |
| `{colors.fundo}` | `{colors.branco}` | Fundo de página |
| `{colors.fundo-bloco}` | `{colors.quadro}` | Zebra de tabela, card de dado, campo, caixa de apoio |
| `{colors.fundo-quente}` | `{colors.creme}` | Bloco de respiro entre seções frias. **Nunca como faixa de seção em peça longa** |
| `{colors.fundo-secao}` | `{colors.cinza-claro}` | Faixa de seção em peça longa |
| `{colors.fundo-escuro}` | `{colors.azul}` | Card de destaque, cabeçalho de tabela, navegação escura |
| `{colors.borda}` | `{colors.quadro}` | Borda de campo e de bloco neutro |
| `{colors.fio}` | `{colors.azul}` | Fio de título, régua de seção, contorno de card |
| `{colors.destaque}` | `{colors.latao}` | Destaque quente. **Nunca em elemento clicável** |
| `{colors.selecao}` | `{colors.azul}` | Marca de checkbox e rádio (`accent-color`) |

🔴 **O latão é detalhe, não segunda cor.** Numa tela ele aparece **poucas vezes**: um número que
importa, o fio do item ativo, no máximo uma caixa quente. Latão em botão, checkbox, texto de
rótulo, borda de campo ou espalhado por vários elementos da mesma tela é veto
(`latao-segunda-cor`). Na dúvida, a cor é azul ou neutra, nunca latão.
| `{colors.realce}` | `{colors.areia}` | Caixa de destaque com texto de leitura |

### Alinhamento

🔴 **Toda borda de alinhamento é UMA linha só.** O que declara alinhamento à esquerda senta na
mesma vertical: logo da barra de topo, itens da navegação lateral, título da página e corpo do
conteúdo compartilham a mesma borda esquerda (a régua do respiro lateral, 40 px). O mesmo vale
à direita. **Elemento fora da vertical dos vizinhos é defeito, não variação**: se dois blocos
começam a 16 px de diferença, um dos dois está errado.

- Recuo de hierarquia (item de grupo, subitem) é degrau declarado da escala de espaço, nunca um
  valor solto.
- Fio de item ativo, borda e marcador não deslocam o texto: compensam a própria espessura.
- Antes de entregar qualquer tela, conferir as verticais: topo, lateral e conteúdo alinhados
  entre si.

### Ritmo de superfície em peça longa

Peça de rolagem longa (apresentação em seções, relatório, proposta, página de muitas dobras)
precisa que o leitor veja onde uma parte termina e a outra começa. Branco do topo ao pé apaga essa
divisão e entrega uma parede sem articulação.

**A régua:** a seção de uma peça longa alterna entre `{colors.fundo}` e `{colors.fundo-secao}`
(`{colors.cinza-claro}`, `#F4F4F4`), um cinza neutro puro, sem nenhum vermelho nem amarelo na
mistura. A faixa `{colors.fundo-escuro}` continua sendo o degrau de destaque, usada com
parcimônia.

🔴 **Creme não alterna seção.** `{colors.fundo-quente}` (`#F1EAD8`) é bloco de respiro pontual e
papel de peça impressa. Quem carrega o ritmo da peça longa é o cinza-claro.

Os limites, que são o que impede a válvula de virar carnaval:

- **Duas superfícies claras por peça:** branco e o cinza-claro. Não existe uma terceira.
- **A superfície pinta a FAIXA da seção inteira**, de borda a borda, nunca o card de dentro. Card sobre faixa de seção volta ao branco, ou se resolve por linha.
- **Zero cor nova.** A alternância consome token; hex escrito à mão segue vetado.
- **O padrão continua branco.** Peça curta (uma dobra, um card, um e-mail, uma folha A4) nasce branca e não alterna.
- **A troca de superfície basta.** Não se põe fio entre uma seção e a outra: o degrau de fundo já divide.
- **O documento inteiro nunca é de apoio.** A superfície é faixa dentro da peça; `body` e container raiz ficam em `{colors.fundo}`.

### Escopo fechado

| Token | Hex | Único uso |
|---|---|---|
| `{colors.erro}` | `#B71313` | Erro e alerta em interface. Na marca, o `m` da tagline |
| `{colors.ok}` | `#0E7A47` | Confirmação em interface |

### Gradiente

Três gradientes oficiais, em `{colors.branco}`, `{colors.azul}` e `{colors.preto}`, cada um de
uma cor só, do transparente ao cheio, na direção horizontal. Uso: sobre foto ou textura, para
abrir uma área limpa onde entra texto ou logo. Curva: branco 0 · 31% · 61% · 82% · 95% · cheio;
azul e preto 0 · 25% · 79% · cheio. Arquivos em `assets/gradiente/`.

## Tipografia

### Famílias

**Playfair Display** em título, abertura e citação. **Inter** em todo o resto, incluindo cada
número apresentado. As duas têm licença livre para uso comercial, e **os arquivos estão em
`assets/fonte/`**: `otf` e `ttf` para instalar, `woff2` para web.

⬦ Substituto, quando a família não carregar: Georgia no lugar da Playfair, e a fonte de sistema
no lugar da Inter. Nenhuma terceira família entra no sistema, nem como substituto permanente.

### Escala em tela

⬦ Quatro níveis vêm da folha de tokens do arquivo de desenho e estão aprovados: display 48,
título 28, corpo 17 e legenda 14. Os demais níveis e todo o tracking são derivação.

Em página de documentação, o título pesa MENOS: página e seção em Playfair **medium** (500).
**O `{typography.display}` bold é registro de CHAMADA: anúncio, hero de campanha, peça
gritante, e só isso.** Capa e abertura de peça editorial ficam no medium; o medium é a régua
de leitura, o bold é a exceção de impacto. A Playfair embarcada cobre os seis pesos (400 a 900) e os dois
itálicos; consuma o peso que o token declara, nunca um sintetizado.

| Token | Tamanho | Peso | Entrelinha | Tracking | Uso |
|---|---|---|---|---|---|
| `{typography.display}` | 48px | 700 | 1,15 | -0,96px | Título de abertura |
| `{typography.secao}` | 36px | 700 | 1,20 | -0,72px | Título de seção |
| `{typography.titulo}` | 28px | 600 | 1,30 | 0 | Título de bloco e de card. **Inter**, não Playfair |
| `{typography.titulo-documento}` | 36px | 500 | 1,20 | -0,4px | Título de página de documentação. Playfair medium |
| `{typography.titulo-de-secao}` | 28px | 500 | 1,25 | -0,4px | Título de seção em página de documentação. Playfair medium |
| `{typography.subtitulo}` | 19px | 500 | 1,35 | 0 | Subtítulo dentro de seção. Inter medium |
| `{typography.titulo-pagina}` | 26px | 400 | 1,20 | 0 | Título de página na barra de topo. Playfair regular |
| `{typography.citacao}` | 22px | 400 itálico | 1,45 | 0 | Citação, frase isolada |
| `{typography.corpo-grande}` | 19px | 400 | 1,60 | 0 | Parágrafo de abertura |
| `{typography.corpo}` | 17px | 400 | 1,60 | 0 | Leitura corrida |
| `{typography.corpo-pequeno}` | 15px | 400 | 1,50 | 0 | Célula de tabela, texto de apoio |
| `{typography.rotulo}` | 13px | 600 | 1,20 | 4px, caixa alta | Rótulo de seção, cabeçalho de tabela |
| `{typography.numero-grande}` | 40px | 700 | 1,10 | -0,4px | Número em destaque. Figuras tabulares |
| `{typography.numero}` | 17px | 700 | 1,30 | 0 | Número em tabela e em texto de dado. Figuras tabulares |
| `{typography.botao}` | 17px | 600 | 1,00 | 0 | Rótulo de botão |
| `{typography.botao-pequeno}` | 15px | 600 | 1,00 | 0 | Rótulo de botão compacto |
| `{typography.botao-utilidade}` | 14px | 600 | 1,00 | 0 | Rótulo do botão de ferramenta (§Densidade em ferramenta) |
| `{typography.legenda}` | 14px | 400 | 1,40 | 0 | Fonte, nota, crédito |

### Densidade em ferramenta

Ferramenta é toda tela de trabalho: formulário de geração, editor, painel de dados. Nela a
escala é um nível menor que a de página pública. Esta seção define **tamanho, peso, espaço e
cor** dos elementos em ferramenta; a disposição na página não é objeto do sistema.

| Elemento | Em ferramenta | Token |
|---|---|---|
| Título de seção ("1 · Dados", "Prévia") | Inter 17 px, **700**, `{colors.azul}` | `{typography.corpo}` em negrito |
| Rótulo de campo | 15 px, 600 | `{typography.corpo-pequeno}` |
| Dica ao lado do rótulo, texto de apoio, rótulo de caixa de marcar | 15 px, 400; dica e apoio em `{colors.texto-fraco}` | `{typography.corpo-pequeno}` |
| Texto dentro do campo | 15 px, campo de 40 px, respiro lateral 12 | `{components.campo-ferramenta}` |
| Botão, todos, inclusive a ação principal | 32 px, 14 px, respiro 12, canto 10 | `{components.botao-utilidade}` / `-cheio` |
| Caixa de marcar | 16 px, desenhada | `{components.checkbox}` |
| Etiqueta de grupo ("BÁSICOS") | 13 px, caixa alta | `{typography.rotulo}` |
| Tabela de dados, miúdos | 14 px | `{typography.legenda}` |

Em ferramenta não se usa Playfair nem `{typography.titulo}`: o título da página é o da barra
de topo, e o título de seção é `{typography.corpo}` em peso 700 e `{colors.azul}`. Seções
separadas por fio de 1 px em `{colors.borda}`, com respiro interno de 32 × 24 px. Rolagem
horizontal é veto em qualquer tela: `html, body` com `overflow-x: clip` (`hidden` cria
contêiner de rolagem e desativa `position: sticky`).

### Escala impressa (A4, 300 dpi)

| Nível | Tamanho e entrelinha |
|---|---|
| Título | Playfair Display **Medium** 130 |
| Chamada gritante | Playfair Display Bold, só em chamada e anúncio, nunca em capa ou miolo editorial |
| Linha-fina | Inter Regular 44 / 1,40 |
| Corpo | Inter Regular 34 / 1,62 |
| Citação | Playfair Display Italic 56 |
| Título de seção | Playfair Display **Regular** 84, com fio capilar sob o título |
| Rótulo de seção | Inter SemiBold 28, tracking 4 |
| Legenda | Inter Regular 24, em `{colors.texto-fraco}` |

Alinhamento à esquerda, sem justificar.

**Em peça editorial impressa (carta mensal, relatório), a capa e o título de abertura ficam em
Playfair MEDIUM (500) e o título de seção em Playfair REGULAR (400). Playfair Bold é SÓ para
chamada, anúncio e peça gritante**: não entra em capa nem em miolo editorial. O fio sob o
título e as linhas separadoras do miolo são **capilares** (0,5 pt · 2 px a 300 dpi).

### Princípios

- **Tracking negativo no título.** De -0,96 px em 48 px até 0 no corpo, proporcional ao tamanho.
  É o que dá acabamento ao título grande.
- **Figuras tabulares em número.** `font-feature-settings: "tnum"` em toda célula com dinheiro,
  contagem ou percentual. Sem isso, a coluna de número dança.
- **Número apresentado sai em Inter.** A exceção é o número dentro de uma frase que já esteja em
  Playfair, que pode continuar em Playfair.
- **Duas famílias.** Uma terceira família quebra o sistema.

### Número, moeda e data

| O que | Assim | Nunca |
|---|---|---|
| Decimal | `11,4%` | `11.4%` |
| Milhar | `1.250.000` | `1,250,000` |
| Moeda | `R$ 1.250,00` | `R$1250.00` |
| Percentual | `11,4%` | `11,4 %` |
| Variação | `+3,0 p.p.` | `+3,0pp` |
| Data | `31/07/2026` em tabela · `31 de julho de 2026` em texto | `07/31/2026` |

## Layout

### Escala de espaço

Base de 8 px, com 4 px para trabalho fino.

`{spacing.x1}` 4 · `{spacing.x2}` 8 · `{spacing.x4}` 16 · `{spacing.x6}` 24 · `{spacing.x10}` 40 ·
`{spacing.x16}` 64.

Respiro interno de card: `{spacing.x10}` 40 px. Respiro interno de caixa e de aviso:
`{spacing.x6}` 24 px. Respiro lateral de campo: `{spacing.x4}` 16 px.

### Utilitários de espaço

Cada degrau da escala existe como classe utilitária, gerada junto com os componentes. Três
famílias, nomeadas pelo que fazem:

| Família | O que faz | Classes |
|---|---|---|
| `vao` | O vão entre itens de um contêiner (gap) | `.api-vao-x6` · `.api-vao-col-x6` (só colunas) · `.api-vao-linha-x6` (só linhas) |
| `margem` | O espaço por fora do elemento | `.api-margem-x6` · por lado: `-topo` `-base` `-esq` `-dir` · por eixo: `-h` `-v` |
| `respiro` | O espaço por dentro do elemento | `.api-respiro-x10` · por lado: `-topo` `-base` `-esq` `-dir` · por eixo: `-h` `-v` |

O degrau entra no fim do nome: `.api-margem-topo-x6` é margem de 24 px no topo. Especial único:
`.api-margem-auto-h` centra o bloco na horizontal. **Valor de espaço escrito à mão em peça é o
mesmo erro que hex escrito à mão**: se a distância não é um degrau da escala, ela não existe.

### Grade e margem

Doze colunas nos dois territórios.

**Impresso:** página A4, retrato ou paisagem. Margem de 40 mm nas laterais e de 20 mm no topo e
na base.

**Tela:** doze colunas; a margem lateral é a da barra de topo, 24 px.

### Espaçamento entre blocos

Quando sobra espaço entre o último bloco e a margem, ele se distribui como respiro entre as
seções, mantendo a proporção entre elas. Os elementos não crescem para preencher.

### Coluna

Um bloco começa na borda de uma coluna e termina na borda de outra, ocupando de uma a doze
colunas inteiras. Se o conteúdo não couber, o bloco ganha uma coluna a mais; a medianiz não
muda e nada entra nela. Blocos de larguras diferentes convivem na mesma página. Divisões mais
usadas: uma coluna · duas em 50/50 · três em terços · duas em 7+5 · duas em 9+3.

## Profundidade

O sistema não usa sombra, em card, botão, painel flutuante ou logo sobre foto. Uma superfície
se separa da outra de duas formas:

| Como | Onde |
|---|---|
| Linha de 1 px em `{colors.borda}` | Campo, caixa, aviso, divisória |
| Linha de 1 px em `{colors.fio}` | Card de conteúdo em peça editorial |
| Fundo `{colors.fundo-bloco}` | Card de dado, zebra de tabela |
| Fundo `{colors.fundo-escuro}` | Card de destaque, cabeçalho de tabela |

Em página de ferramenta e painel, o fundo da página é `{colors.fundo-secao}` e o card é branco,
sem linha: o fundo separa.

## Forma

### Fio

| Nome | Espessura | Onde |
|---|---|---|
| Capilar | 0,5 pt | Fio de tabela, separador de linha |
| Fino | 1 pt | Divisória de bloco, contorno de caixa |
| Médio | 2 pt | Fio sob título, régua de seção |
| Grosso | 6 pt | Fio de abertura, marcação de capa |

### Canto

Em tela, card, botão, campo, aviso e amostra de cor têm `{rounded.canto}` (15 px); o botão de
utilidade tem `{rounded.canto-ferramenta}` (10 px). No impresso, `{rounded.canto-vivo}`. Cápsula
(canto igual à metade da altura) não se usa.

### Divisória

A divisória horizontal é o fio fino, na largura do bloco. Entre linhas de tabela não entra fio:
as linhas alternam fundo (zebra).

## Logo

Doze versões: oito montagens bicolores e quatro vazadas de uma cor. O logotipo nunca se remonta
à mão.

**Os arquivos estão em `assets/logo/`**, em `svg/`, `png/` (1x, 2x e 4x) e `pdf/`. Cada versão vem
em azul, branco e quase-preto. O nome diz tudo: `api_capital_logo03_branco.svg`.

### Arquivos justos

🔴 **Todo arquivo de logo é JUSTO: o canvas é a caixa exata da arte, sem margem embutida.**
`height: 42px` significa arte de 42 px. (Até 2026-08-26 os arquivos embutiam a área livre no
canvas e toda peça gerada saía com logo minúscula; eles foram substituídos, com os mesmos
nomes.) A área livre é régua de APLICAÇÃO (§Área livre): quem monta a peça deixa o respiro em
volta, ele não viaja dentro do arquivo.

**Régua de tamanho da arte em tela:**

- **Barra de topo e navegação:** a logo principal (`logo01`) com **56 px** na barra de 96;
  44 px na de 72; 36 px na de 64.
- **Rodapé:** 28 a 32 px.
- **Mínimo absoluto em tela: 24 px de altura.** Logo menor que isso não entra: na dúvida, a
  logo é MAIOR do que parece necessário, nunca menor.

### Área livre

Deixe uma faixa livre em volta do logo. A medida é **metade da altura da letra A** do logotipo
"API". No selo isolado, o disco com o pelicano, a medida é **um quarto do diâmetro do disco**.
Nenhum elemento entra nessa faixa: texto, fio, imagem ou borda de foto.

### Fundo

| Fundo | Versão |
|---|---|
| Branco e claro | Bicolor oficial, ou vazada em `{colors.azul}` |
| Escuro ou imagem escura | Vazada branca |
| Imagem clara ou textura | Vazada branca com véu por baixo |

### O que não se faz

- Remontar o logotipo com texto
- Trocar a cor de uma parte
- Esticar, inclinar, girar, aplicar efeito
- Pôr sombra ou contorno para separar do fundo
- Usar arquivo que não seja o oficial

### Opacidade

Reduzir a opacidade do logo é permitido, por exemplo para usá-lo como marca d'água. O arquivo
continua o oficial, inteiro e na cor dele. O veto de opacidade em §Vetos vale para cor de
preenchimento, não para o logo.

## Logos de parceiros

As plataformas onde a API opera e com quem tem convênio. **Os arquivos estão em
`assets/parceiros/`**, em `svg/` e `png/` (200 px de altura, fundo transparente). Nome:
`api_capital_parceiro_<nome>`.

No Pen, logo de parceiro entra como **vetor**, nunca como PNG: o script
`assets/parceiros/pen/logos_parceiros_api.js` desenha qualquer um deles (nó `script`, entrada
`logo` com o nome do arquivo e `color` com `{colors.parceiro}`).

Três regras, sem exceção:

1. **Ordem alfabética**, sempre. Nenhum parceiro vem antes por tamanho ou relevância.
2. **Mesma cor para todos:** `{colors.parceiro}` (`#5E5E5E`), cinza sólido. O logo
   nunca entra na cor da marca dele nem na cor da API. O arquivo já vem nessa cor.
3. **Mesmo peso visual entre todos.** Altura igual não basta: um logo quadrado e cheio pesa
   mais que um logo largo e fino. A altura de cada um vem da tabela abaixo, calculada para
   que todos ocupem a mesma área aparente, com correção óptica nos que pesam mais ou menos
   do que a área indica.

| Parceiro | Arquivo | Altura na linha de referência |
|---|---|---|
| Ágora | `api_capital_parceiro_agora` | 27 px |
| Avenue | `api_capital_parceiro_avenue` | 20 px |
| Brasilprev | `api_capital_parceiro_brasilprev` | 19 px |
| BTG Pactual | `api_capital_parceiro_btg_pactual` | 35 px |
| C6 Bank | `api_capital_parceiro_c6_bank` | 22 px |
| Genial | `api_capital_parceiro_genial` | 31 px |
| Inter | `api_capital_parceiro_inter` | 24 px |
| Morgan Stanley | `api_capital_parceiro_morgan_stanley` | 19 px |
| Nomad | `api_capital_parceiro_nomad` | 24 px |
| Safra | `api_capital_parceiro_safra` | 31 px |
| Stoa | `api_capital_parceiro_stoa` | 27 px |
| XP Investimentos | `api_capital_parceiro_xp_investimentos` | 40 px |

A linha de referência é a de uma peça A4 em tela (logo em grade de quatro colunas). Para
outro tamanho, multiplique todas as alturas pelo mesmo fator: a proporção entre elas não
muda. Em grade, cada logo se centra na própria célula.


## Ícone

A iconografia usa a biblioteca **Lucide**, de traço único e geometria simples.

**Os 24 ícones escolhidos para os usos recorrentes da marca estão em `assets/icone/`**, em
`svg/`, `png/` e `pdf/`. Use esses primeiro. Para um caso que eles não cobrem, escolha na
biblioteca completa da Lucide, em `assets/icone/lucide/`, mantendo traço de 2 px e sem
preenchimento.

Posição no card: canto inferior direito.

**Exceção: logo de rede social.** A Lucide não tem logo de marca. LinkedIn, Instagram, YouTube,
Facebook, X e WhatsApp usam a biblioteca **Phosphor**, peso regular, em `{colors.azul}` ou
`{colors.branco}`. A exceção vale só para logo de rede social; qualquer outro ícone segue na
Lucide. Os arquivos prontos, em PNG, estão em `assets/assinatura/`.

## Imagem

### Fotografia

**O acervo está em `assets/foto/`.**

```
Wide, quiet natural atmosphere in high key: open sky, mist, slow water or rippled sand.
Cool blue (hue 190-215) or warm sand (hue 29-39), never both in the same frame. Bright,
low saturation, low internal contrast: no deep blacks, no blown highlights, no drama.
No people, no sharp focal subject, no landmark. The image is background, not statement:
it must survive a text overlay without competing with it. Natural daylight, no artificial
colour grading, no lens flare, no HDR.
```

Fotografia de pessoa não está definida.

### Textura

Ladrilho que se repete para a direita e para baixo sem emenda, sempre tom sobre tom, em
preenchimento sólido. Nunca cor escura com opacidade por cima. **Os arquivos estão em
`assets/textura/`.**

| Fundo | Ladrilho |
|---|---|
| `{colors.preto}` | `{colors.preto-var}` |
| `{colors.azul}` | `{colors.azul-var}` |
| `{colors.azul-claro}` | `{colors.azul-claro-var}` |
| `{colors.latao}` | `{colors.latao-var}` |
| `{colors.areia}` | `{colors.areia-var}` |
| `{colors.creme}` | `{colors.creme-var}` |
| `{colors.branco}` | `{colors.quadro}` |

## Componentes

### Botão

**`{components.botao-primario}`** é a ação dominante. Fundo `{colors.acao}`, texto
`{colors.sobre-escuro}`, tipo `{typography.botao}`, canto `{rounded.canto}`, altura 48 px, respiro
lateral de `{spacing.x6}` 24 px. Sob o cursor vira `{components.botao-primario-hover}`, que troca
o fundo pela variação.

**`{components.botao-secundario}`** é a alternativa de contorno: fundo `{colors.fundo}`, texto e
borda de 1 px em `{colors.acao}`, mesma geometria.

**`{components.botao-azul-claro}`** carrega a ação secundária em `{colors.acao-secundaria}`.

**`{components.botao-sobre-escuro}`** é a ação sobre fundo escuro: fundo `{colors.branco}`, texto
`{colors.azul}`.

**`{components.botao-texto}`** é o botão sem caixa, em `{colors.acao}`.

**`{components.botao-utilidade}`** é o botão de ferramenta: contorno em `{colors.acao}`, tipo
`{typography.botao-utilidade}` (14 px), altura **32 px**, respiro lateral de 12 px e canto
`{rounded.canto-ferramenta}` (10 px: o canto de 15 num botão de 32 vira cápsula). A versão
cheia é `{components.botao-utilidade-cheio}`. **Em ferramenta, todo botão é de utilidade**,
inclusive a ação principal (exportar, salvar, gerar). Os botões de 48 e 56 px são de página
pública e de chamada (§Densidade em ferramenta).

Alturas: 48 px no padrão, 36 px na barra de topo, 32 px em ferramenta.

### Campo

**`{components.campo}`** tem fundo `{colors.fundo}`, borda de 1 px em `{colors.borda}`, canto
`{rounded.canto}`, altura 48 px e respiro lateral de `{spacing.x4}` 16 px.

**`{components.campo-ferramenta}`** é o campo de ferramenta: mesma anatomia, altura
**40 px**, respiro lateral de 12 px e o texto digitado em `{typography.corpo-pequeno}` (15 px):
texto dentro de campo fica um nível abaixo do corpo. Textarea segue a mesma régua (respiro de
10 × 12 px).

**O rótulo fica sempre acima do campo**, em `{typography.corpo-pequeno}` com peso 600; a dica
ao lado do rótulo e o texto de apoio ficam em `{typography.corpo-pequeno}` com peso 400 em
`{colors.texto-fraco}`. Em foco, `{components.campo-foco}` acrescenta anel de
3 px, afastado 2 px. Em erro, `{components.campo-erro}` troca a borda
por `{colors.erro}`, **com a mensagem escrita ao lado**.

**Formulário vive direto sobre o fundo do card ou da seção.** Não se cria contêiner de fundo
cinza para agrupar campos dentro de um card: caixa dentro de caixa é veto
(`box-dentro-de-box`). Grupo de campos se marca com título de grupo e espaço, nunca com um
segundo fundo.

**Botão dentro de formulário é um dos declarados em §Botão.** Botão ao lado de um campo
("Hoje", "Anexar arquivo", "Limpar") é `{components.botao-secundario}` em site e
`{components.botao-utilidade}` em ferramenta. Anexo de arquivo usa o ícone Lucide `paperclip`.

### Caixa de seleção

**`{components.checkbox}`** é a caixa de marcar: **16 × 16 px**, fundo `{colors.fundo}`, borda de
1 px em `{colors.borda}`, canto de 4 px, e a marca em `{colors.acao}`. **A caixa é desenhada
(`appearance: none`); o controle nativo do navegador não se usa**, porque a renderização varia
por sistema e não respeita a medida. Marcada: fundo `{colors.acao}` e tique branco de 2 px.
Rádio segue a mesma régua, redondo. **Checkbox nunca é latão,
nem qualquer outra cor fora de `{colors.acao}`.**

Entre a caixa e o rótulo entra respiro de `{spacing.x2}` 8 px, sempre: caixa colada no texto é
erro. O rótulo do checkbox fica em `{typography.corpo}` em site e em `{typography.corpo-pequeno}`
em ferramenta, sem caixa alta.

### Card

| Componente | Fundo | Texto | Quando |
|---|---|---|---|
| `{components.card-conteudo}` | `{colors.fundo}`, borda em `{colors.fio}` | `{colors.texto}` | Bloco de conteúdo com função estrutural |
| `{components.card-dado}` | `{colors.fundo-bloco}` | `{colors.texto}` | Número e dado apresentado |
| `{components.card-destaque}` | `{colors.fundo-escuro}` | `{colors.sobre-escuro}` | Destaque. **Um por tela** |
| `{components.card-quente}` | `{colors.fundo-quente}` | `{colors.azul}` | Respiro entre seções frias |

Respiro interno de 40 px em toda borda. Anatomia: título · fio · descrição · espaço · ícone no
canto inferior direito.

### Content card

A família de card de **ferramenta, painel e página interna** (formulário em etapas, dashboard,
gerador). É ela que se usa nesses territórios, nunca um bloco inventado.

**A regra de superfície que sustenta a família:** em página de ferramenta, o fundo da página é
`{colors.fundo-secao}` (`#F4F4F4`) e o content card é **branco, SEM borda**: é o degrau de fundo
que separa o card da página, não contorno. Contorno fino em volta de card de ferramenta é veto.
(O `{components.card-conteudo}` com borda no fio segue existindo para peça editorial sobre fundo
branco.)

Anatomia base, de cima para baixo: **título** em `{typography.titulo}` com `{colors.azul}` ·
**linha-fina** opcional em `{typography.corpo-pequeno}` com `{colors.texto-fraco}` · **corpo** em
`{typography.corpo}` · **ações**: `{components.botao-primario}` e, ao lado, link em
`{colors.acao-secundaria}` com o ícone Lucide `chevron-right`. Respiro interno de 40 px; entre os
elementos, a escala de `{spacing}`.

Três réguas de respiro que valem em toda a família:

- **A ação fica na base do card**, com espaço acima dela.
- **Entre o bloco de título (com linha-fina ou categoria) e o corpo entra espaço**, maior que o
  entrelinhas.

As variações, todas com a mesma base, mudando só o que está dito:

| Variação | O que muda | Quando |
|---|---|---|
| **`{components.content-card}`** | Nada. É a base | Bloco padrão de ferramenta e painel |
| **Com botões de utilidade** | Até dois `{components.botao-texto}` só-ícone (Lucide) no canto superior direito | Compartilhar, informação, fechar |
| **Clicável** | O card inteiro é o link: sem botão dentro, o título carrega o `chevron-right`. Sobre: fundo vai a `{colors.fundo-bloco}`. Foco: anel de 3 px | Atalho de navegação |
| **Desabilitado** | Texto a 40%, ícone Lucide `lock` ao lado do título, sem cursor de mão | Recurso indisponível |
| **Com categoria** | Linha-fina de categoria **abaixo do título**, com ícone Lucide de 16 px na frente, em `{typography.corpo-pequeno}` com `{colors.texto-fraco}` | Card em coleção com tipos |
| **Com ícone no alto** | Ícone Lucide de 40 px em `{colors.azul}` no canto superior esquerdo; o conteúdo desce | Card de recurso ou serviço |
| **Com ícone na base** | Ícone Lucide em `{colors.azul}` que **desrespeita a margem interna e senta no canto inferior direito do card** | Card de recurso ou serviço |
| **Com imagem** | Imagem no topo, na largura do card, cantos superiores de `{rounded.canto}` | Conteúdo editorial |
| **`{components.content-card-numero}`** | Título · corpo opcional · **número** em `{typography.numero-grande}` com `{colors.azul}` e, ao lado, a variação com seta Lucide (`arrow-up`/`arrow-down`) e rótulo em `{typography.legenda}` | Dado de dashboard |

Limites da família:

- **Card de ferramenta não tem borda, não tem sombra, não tem fundo cinza interno**: o grupo
  interno se marca com título e espaço (§Campo).
- **Não existe a variação com faixa indicadora na base.** Faixa colorida em borda de card é veto
  (`callout-faixa-lateral`), e aqui não há exceção.
- Na variação com número, a seta e a variação percentual podem usar `{colors.ok}` e
  `{colors.erro}` **porque comunicam dado, e sempre com o valor escrito ao lado**: a cor sozinha
  não comunica.
- Grade: os content cards de um painel assentam na grade de 12 colunas, com junta de
  `{spacing.x6}` 24 px entre cards.

### Caixa de destaque

**`{components.caixa-latao}`** tem fundo `{colors.destaque}` e carrega **só título grande ou
número**. **`{components.caixa-ocre}`** tem fundo `{colors.realce}` e carrega texto de
leitura em `{colors.azul}`.

Máximo de uma caixa quente por página.

### Navegação

A navegação de site é a barra de topo com itens de menu (configuração "site com navegação",
§Barra de topo): 64 px, respiro lateral de 24 px, itens em Inter 500 15 px, o ativo em 600 com
fio de 2 px (`{colors.acao}` no fundo claro, `{colors.destaque}` no escuro), uma ação à direita
de 36 px. No fundo escuro o logo entra na versão branca.

### Barra de topo

Todo site, painel, gerador e ferramenta abre com **`{components.barra-topo}`** (clara) ou
**`{components.barra-topo-escura}`**. Altura de 64 px, respiro lateral de 24 px.

🔴 **Toda a barra tem o mesmo alinhamento central:** cada elemento, da logo à lua, senta no
centro vertical da linha.

**A logo e o último elemento da direita respeitam a margem da página, quando ela existe:** o
respiro lateral da barra deixa de ser 24 px e passa a ser a própria margem do conteúdo. Não vale
para página de conteúdo central (como o gerador de carta), que fica nos 24 px.

**Medidas** (o desenho de referência é a folha `api_capital_ui_navegacao` do `.pen`; a página
navegável é `design.apicapital.com.br/componentes/barra-de-topo/`):

| Elemento | Medida | Observação |
| --- | --- | --- |
| Altura da barra | 64 px | uma só, em qualquer tela |
| Respiro lateral | 24 px | |
| Distância entre itens | 16 · 20 px | 16 em site, 20 em aplicação |
| Logo extensa (`logo03`) | 30 px | quando não há título de página |
| Selo isolado (`logo05`) | 31 px | quando há título de página |
| Título da página | Playfair regular 26 | alinha pelo "API Capital", ignorando o pelicano |
| Item de navegação | Inter 500 · 15 | ativo em 600, com fio de 2 px |
| Contexto | Inter 600 · 15 | nome do documento aberto |
| Ícone de ação | 21 px | Lucide, traço de 2 |
| Lua (claro/escuro) | 15 px | 70% do ícone comum |
| Avatar | 27 px | anel de 1 px a 3 px da foto |
| Campo de busca | 290 × 48 px | canto de 15 |
| Ação cheia | 36 px de altura | canto de 15, Inter 600 15 |

Em tela sensível ao toque, o alvo de cada ícone cresce para 44 px sem mudar o desenho.

**Qual logo entra:**

- **Logo extensa**: na esquerda ou no centro, quando a página não tem título.
- **Selo isolado** (círculo do pelicano): quando a página tem outro título.

**Na versão escura**, fundo `{colors.fundo-escuro}`, logo branca, ícone e texto em
`{colors.sobre-escuro}`, a ação cheia inverte (fundo branco, texto azul) e o campo de busca usa
`{colors.azul-var}`.

**Seis configurações prontas** (site simples, site com navegação, painel com busca, gerador de
documento, documentação e completa) em **Padrões · Barra de topo**, cada uma em clara e escura.
🔴 **Para montar uma barra, copie o código pronto de
`design.apicapital.com.br/componentes/barra-de-topo/codigo.html` e troque só textos, ícones e
logo. Não se desenha barra do zero.**

### Passo numerado

Formulário ou fluxo em etapas numera o passo **dentro do próprio título**, com
**`{components.numero-passo}`**: o número em `{typography.numero}` (Inter 700, figura tabular),
na cor do título `{colors.azul}`, seguido de ponto e do nome do passo, como `1. Cliente e consultor`.

**Sem círculo, sem bolinha, sem fundo, sem latão.** Número de passo dentro de disco colorido é
veto (`passo-em-bolinha`).

### Aviso

**`{components.aviso-erro}`** e **`{components.aviso-ok}`**: fundo branco, borda de 1 px na
cor do estado, canto `{rounded.canto}`, respiro de `{spacing.x4}` 16 px.

**Todo aviso tem ícone, título e o que fazer.** A cor sozinha não comunica.

### Tabela

**`{components.tabela-cabecalho}`** em `{colors.fundo-escuro}` com `{typography.rotulo}`.
Linhas alternam **`{components.tabela-linha}`** e **`{components.tabela-zebra}`**. Entre linhas
não entra fio.

Texto à esquerda, número à direita em `{typography.numero}`. A tabela fecha com fonte e data de
apuração em `{typography.legenda}`.

**Tabela curta de comparação** (duas ou três linhas, com as classes lado a lado): título de
coluna e valor ficam **centralizados**, o valor exatamente sob o seu título. O número à direita
é régua de tabela longa de dados; aplicado numa tabela curta, título e valor caem cada um num
canto e a peça desalinha.

### Gráfico

Cores de série, nesta ordem: `{colors.azul}` · `{colors.latao}` · `{colors.azul-claro}` ·
`{colors.preto}` · `{colors.areia}`.

**A paleta serve à mensagem.** A ordem acima é o padrão, não camisa de força: em gráfico denso
ou heatmap, cores de dado fora da marca (tons pastéis, verdes) entram quando melhoram a
leitura. A identidade da peça fica na tipografia, no layout e na moldura, não na cor de cada
série.

Eixo Y sempre com valores, barra partindo do zero (linha pode escalar: a régua é de barra),
rosca sempre com furo. Fecha com fonte e data de apuração.

**Moldura e rótulo:**

- **Título é o pedido, resumido.** Quem pediu "Selic nos últimos 5 anos" recebe o título "Taxa
  Selic Meta - 5 anos". **Nunca uma conclusão tirada do dado** ("A Selic subiu a 15%..."): o que
  o dado diz, quem pediu decide, e se quiser outro título pede para trocar. Em
  `{typography.titulo}` reduzido (20 px numa peça de 600 px, crescendo com a peça); subtítulo com
  a unidade e o período; **vão de 12 px entre os dois**.
- **Legenda de séries centrada** sobre o gráfico, com respiro generoso até o topo da área de
  dados (56 px numa peça de 600 px).
- **Rótulo de valor nunca tem contorno nem sombra.** Sobre fundo escuro (dentro de uma barra),
  só a cor muda para branco.
- **Rótulo nunca atravessa a borda de uma barra**: ou fica inteiro fora, em `{colors.texto}`,
  ou inteiro dentro, em branco. Rótulo de linha que colidiria com o rótulo da barra desce para
  baixo do ponto.
- **Marca d'água sempre.** Todo gráfico leva o logo principal da API (`api_capital_logo01_azul.svg`)
  no fundo, com 12% de opacidade, centrado na área dos dados na horizontal e na vertical, e grande:
  ocupa 85% dela, na largura ou na altura, o que encostar primeiro. Fica atrás das séries. A
  opacidade de 7% da primeira versão sumia em monitor de contraste baixo. Decisão de 4 de novembro de 2026, depois de um gráfico da API ser copiado e republicado
  sem permissão. **O tema do ECharts põe a marca sozinho** em todo gráfico iniciado com
  `'api-capital'`, e a repõe a cada atualização e redimensionamento: nenhuma ferramenta precisa
  lembrar dela, e nenhuma pode tirá-la. Gráfico feito fora do ECharts (planilha, imagem, outro
  motor) leva a mesma marca, nas mesmas medidas, posta à mão.
- **Animação desligada** em peça exportada.
- O tema do motor de gráficos (Apache ECharts) é `tokens/tema-echarts.js`, gerado deste
  arquivo; toda ferramenta que desenha gráfico carrega o tema pelo endereço, sem copiar valor.

## Estados

| Estado | Como se mostra |
|---|---|
| Normal | A cor do elemento |
| Sobre | A variação da cor (`{colors.acao-hover}` no botão). O cursor vira mão |
| Foco | Anel de 3 px em `{colors.acao-secundaria}`, afastado 2 px. Aparece na navegação por teclado |
| Desabilitado | Fundo `{colors.fundo-bloco}`, texto em `{colors.texto-fraco}`, sem cursor de mão |

## Acessibilidade

- **O anel de foco não se remove.** `outline: none` só com outro indicador de foco no lugar.
- **Erro, sucesso e alerta se dizem em texto**, não só em cor.
- **Texto alternativo em toda imagem que carrega informação.** Imagem decorativa entra com
  alternativo vazio.

## Comportamento responsivo

Em tela estreita, um bloco de três colunas passa a duas, depois a uma. Tabela larga rola na
horizontal dentro do próprio bloco. A barra de topo mantém 64 px em qualquer largura.

## Vetos

- Sombra, brilho, vidro fosco, translucidez
- Gradiente entre duas cores, ou em elemento de interface
- Cor sólida rebaixada com opacidade para simular tom mais claro (o logo com opacidade reduzida é permitido, §Logo)
- Cápsula (`9999px`)
- Contorno cinza claro de 1 px em volta de tudo
- Caixa de destaque com faixa colorida na lateral ou no topo
- Terceira família tipográfica
- Número apresentado em Playfair
- Número sem figura tabular em tabela
- Antetítulo: rótulo miúdo em caixa alta acima do título
- Rótulo do tipo `01 / BLOCO 03`
- Linha de fonte pequena e cinza com informação que deveria estar no texto
- Eixo de gráfico cortado, gráfico sem escala, minigráfico decorativo
- Gráfico sem a marca d'água da API
- Percentual escrito sobre a fatia da rosca
- Fio entre linhas de tabela
- Mais de uma caixa quente por página
- Emoji, em qualquer papel, inclusive no lugar de ícone. Ícone é Lucide
- Símbolo que remeta a mercado financeiro: gráfico, seta, candelabro japonês
- Latão como segunda cor da tela: em botão, checkbox, texto de rótulo, borda, ou repetido em vários elementos
- Botão fora dos cinco declarados em §Botão
- Contêiner de fundo cinza agrupando campos dentro de um card (box dentro de box)
- Número de passo dentro de círculo ou bolinha colorida
- Checkbox ou rádio em cor que não seja `{colors.selecao}`
- Cabeçalho de página inventado no lugar de `{components.barra-topo}`

## Guia de iteração

1. Trabalhe **um componente por vez**.
2. Referencie token, nunca valor: `{colors.acao}`, `{typography.corpo}`, `{rounded.canto}`.
3. Comece sóbrio. Expressividade entra na segunda versão.
4. Variante nova entra como entrada própria em `components`, não como exceção no texto.
5. Todo bloco começa e termina em coluna.
6. Espaçamento entre blocos: 120 px. Dentro do bloco: 60 px.
7. Número apresentado em Inter 700 com figura tabular.
8. Gráfico e tabela fecham com fonte e data de apuração.
9. Traduza o jargão. Quem lê não é do mercado financeiro.
10. Não acrescente ressalva regulatória, aviso legal ou nota de risco.

### Geração de imagem

```
Classic-modern brand system, sober and quiet authority, closer to Montblanc than to a fintech.
Deep navy (#0D2A54) and brass (#AA7D41) on pure white (#FFFFFF), neutral near-black text
(#171717). Playfair Display for headlines, Inter for everything else. Flat solid fills; the only
allowed gradient is a single-colour transparent-to-solid veil over a textured background, never
on type or UI. No shadow, no glow, no glassmorphism. Sharp editorial layout on a 12-column grid,
generous margins, 15px corner radius on screen elements. No stock-market iconography.
```

## Arquivos

Os ativos prontos para uso ficam neste pacote, em `assets/`:

| Grupo | Pasta | Formatos |
|---|---|---|
| Logo | `assets/logo/` | svg · png 1x 2x 4x · pdf |
| Tagline | `assets/tagline/` | svg · png 1x 2x 4x · pdf |
| Logos de parceiros | `assets/parceiros/` | svg · png |
| Ícone | `assets/icone/` | svg · png 1x 2x 4x · pdf |
| Gradiente | `assets/gradiente/` | svg · png 1x 2x 4x · pdf |
| Favicon | `assets/favicon/` | svg · png 1x 2x 4x · pdf |
| Paleta | `assets/paleta/` | svg · png · pdf · **ase** (Illustrator, Photoshop, InDesign) · **gpl** (Inkscape, Krita) · txt · json |
| Textura | `assets/textura/` | svg e pdf do ladrilho · png de todas |
| Wallpaper | `assets/wallpaper/` | png, no tamanho nativo |
| Social | `assets/social/` | png, no tamanho de cada plataforma |
| Splash | `assets/splash/` | png 1290 × 2796 |
| Foto | `assets/foto/` | png |
| Assinatura de e-mail | `assets/assinatura/` | png: logos de rede social (Phosphor) em azul e branco, ícones de contato e marcadores de foto |
| Exemplos | `exemplos/` | png e pdf das folhas do sistema |

| Biblioteca Lucide completa | `assets/icone/lucide/` | 1.767 svg |
| Fontes | `assets/fonte/` | Playfair Display em otf, Inter variável em ttf, e woff2 das duas para web |
