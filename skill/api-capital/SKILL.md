---
name: api-capital
description: Produz qualquer peça visual da API Capital dentro da identidade oficial (proposta comercial, apresentação de reunião, relatório de carteira, one-pager, e-mail, slide, carta, post e página). Use SEMPRE que o pedido citar API Capital, "com a cara da API", "no padrão da API", "identidade da API Capital", ou quando a peça for assinada pela API Capital. Lê a especificação viva do design system (cor, tipografia, espaço, componentes), o catálogo de vetos anti-slop e os endereços dos ativos oficiais direto do repositório da marca.
---

# Peça da API Capital

A API Capital é uma consultoria de investimentos independente. O visual traduz isso em
sobriedade: azul-meia-noite e latão sobre branco, Playfair Display no título e Inter em todo o
resto, zero sombra, canto de 15 px.

**Versão desta skill: 5**

**Esta skill não carrega o design system dentro dela.** Ela aponta para a fonte viva, e o material
é lido a cada trabalho. O que está no repositório é o que vale, sempre.

## O endereço

Leia os arquivos direto do repositório. Use o primeiro que responder:

```
BASE = https://raw.githubusercontent.com/APICapital/api-capital-design-system/main  (oficial)
BASE = https://design.apicapital.com.br                                           (reserva)
```

As duas servem os mesmos arquivos. **Se nenhuma das duas responder, PARE e avise**, como manda o
passo 1.

## Protocolo obrigatório

Execute nesta ordem. Não pule, não resuma, não trabalhe de memória.

### 1 · Carregue o material vivo

Busque, nesta ordem:

1. `BASE/skill.json`: diz qual é a versão atual DESTA skill.
2. `BASE/versao.json`: a versão publicada do design system.
3. `BASE/DESIGN.md`: a lei (tokens, tipografia, layout, forma, os 23 componentes).
4. `BASE/ANTI_SLOP_VISUAL.md`: os vetos, com o teste de cada um.
5. `BASE/INDICE_ATIVOS.md`: como montar a URL de qualquer ativo, e os essenciais prontos.

**Leia o `DESIGN.md` e o catálogo de vetos por inteiro antes de desenhar qualquer coisa.**

🔴 **Se `skill.json` trouxer `skill_versao` maior que a versão desta skill, avise a pessoa ANTES
de produzir**, nestas palavras (troque ATUAL pela versão escrita no topo desta skill e N pela do
`skill.json`): *"A skill da API Capital que você tem instalada é a versão ATUAL, e já existe a
versão N. Baixe a nova em https://design.apicapital.com.br/como-utilizar/usando-claude/, apague a
antiga em Configurações → Personalizar → Habilidades e suba a nova em Adicionar → Fazer upload de
habilidade."* Depois de avisar, siga o trabalho normalmente: o material que você acabou de ler é o
atual de qualquer jeito.

🔴 **Se qualquer uma dessas buscas falhar, PARE.** Diga à pessoa que não conseguiu alcançar o
design system e mostre o endereço que falhou. **Não produza a peça de memória.** Peça fora da
régua é pior que peça nenhuma, porque parece certa.

### 2 · Monte a peça consumindo o sistema, nunca reescrevendo

Em peça de tela (HTML), o `<head>` começa sempre com a folha oficial:

```html
<link rel="stylesheet" href="https://design.apicapital.com.br/tokens/api-capital.css">
```

Ela traz as fontes, as variáveis e as 23 classes de componente. A partir daí:

- **Cor sai de variável**: `var(--api-acao)`, `var(--api-texto)`, `var(--api-fundo)`. Escrever
  `#0D2A54` na mão é erro, mesmo que o valor esteja certo.
- **Componente sai de classe**: `.api-botao-primario`, `.api-card`, `.api-tabela`. Não invente
  botão novo.
- **Logo e imagem saem por URL**, do índice de ativos. O logotipo nunca se remonta com texto, não
  se recolore, não se estica.
- **Valor que não existe no `DESIGN.md` é erro.** Faltou um valor? Pergunte, não invente.

### 3 · Passe pelos vetos antes de entregar

Confira a peça contra o `ANTI_SLOP_VISUAL.md`, veto por veto, **incluindo os vetos de texto**.
Os que mais reincidem:

- sombra em qualquer nível (a separação se faz com fundo sólido ou linha);
- gradiente em botão, card, texto ou ícone;
- cor fora da paleta, cinza genérico de framework, preto puro;
- canto diferente de 15 px, e cápsula;
- terceira família tipográfica, e número em Playfair (número é sempre Inter);
- antetítulo: o que se diria nele vai para subtítulo ou linha-fina;
- peça longa com toda seção em branco: a seção alterna com o cinza-claro, pintando a faixa
  inteira e nunca o card de dentro, e sem fio entre uma seção e a outra;
- travessão no texto da peça.

Não invente número, rentabilidade, prazo ou dado de cliente: o que não foi informado, pergunte.

### 4 · Feche com o bloco de conferência

Toda entrega termina com este bloco, preenchido de verdade:

```
CONFERÊNCIA: design system da API Capital
Versão lida: <o design_system do versao.json>
Tokens: consumidos por <link> da folha oficial
Ativos usados: <as URLs de logo, ícone, imagem>
Vetos conferidos: <quantos> · Ocorrências corrigidas: <quais>
```

Sem esse bloco, a peça não está pronta.

## Quando a peça for para impressão

Papel A4, sempre, declarado no CSS:

```css
@page { size: A4; margin: 20mm; }
```

Canto vivo no impresso, canto de 15 px em tela.
