# Design System da API Capital

Tudo que é preciso para produzir uma peça da marca: a especificação, os vetos, os tokens e os
ativos.

## Como usar com o Claude

Clone a pasta e trabalhe de dentro dela:

```
git clone git@github.com:<conta>/api-capital-design-system.git
cd api-capital-design-system
claude
```

O `CLAUDE.md` da raiz é lido sozinho no começo da sessão, e ele manda o Claude ler a
especificação e os vetos antes de produzir qualquer coisa. Daí é só pedir a peça: *"monta uma
apresentação de primeira reunião"*, *"faz a proposta de trabalho em HTML"*.

Peça montada fora desta pasta não herda nada disso. Se for produzir em outro projeto, copie
`DESIGN.md`, `ANTI_SLOP_VISUAL.md`, `CLAUDE.md` e `tokens/` para lá.

## O pacote está publicado

| Onde | Endereço |
|---|---|
| Portal, com a skill e o prompt | <https://design.apicapital.com.br/> |
| Endereço reserva (redireciona) | <https://apicapital.github.io/api-capital-design-system/> |
| Repositório | <https://github.com/APICapital/api-capital-design-system> |

**É deste endereço que as peças bebem.** Peça de tela importa
`tokens/api-capital.css` por link e referencia logo, ícone e imagem pela URL do
`INDICE_ATIVOS.md`: atualizou aqui, atualizou em toda peça já entregue.

Para publicar o que mudou:

```
/Users/leandrobeninca/Developer/second-brain/engenharia/infra/scripts/publicar_design_system_api.sh "o que mudou"
```

Antes disso, se mexeu nos tokens rode `python3 tokens/gerar_tokens.py`; se acrescentou ou
renomeou ativo, `python3 gerar_indice_ativos.py`.

**A skill do Claude é um ponteiro** (`skill/api-capital/SKILL.md`): nenhum pedaço do design system
viaja dentro dela: o material é lido deste endereço a cada trabalho. Por isso quem instalou uma
vez nunca fica com a régua velha, e o `.zip` só precisa ser refeito (`./empacotar_skill.sh`) quando
o protocolo dela ou o endereço mudarem.

## Por onde começar

| Você quer | Abra |
|---|---|
| Saber as regras: cor, tipografia, layout, componentes | `DESIGN.md` |
| Saber o que **não** fazer | `ANTI_SLOP_VISUAL.md` |
| Usar em código | `tokens/api-capital.css` (importa os três abaixo) |
| Pegar um logo, ícone, fonte, cor ou textura | `assets/` |
| Ver uma página montada na régua | `exemplos/` |

## Estrutura

```
DESIGN.md              a lei: tokens, regras e componentes
ANTI_SLOP_VISUAL.md    o catálogo de vetos, com o teste de cada um
tokens/
  api-capital.css      folha única: importa as três abaixo
  fontes.css           @font-face de Playfair Display e Inter
  tokens.css           variáveis e classes de tipografia
  componentes.css      as 23 classes de componente
  tokens.json          os mesmos tokens em JSON
  gerar_tokens.py      gera tokens.css, componentes.css e tokens.json
assets/
  logo/                svg · png 1x 2x 4x · pdf
  tagline/             svg · png 1x 2x 4x · pdf
  icone/               svg · png 1x 2x 4x · pdf · lucide/ (biblioteca completa)
  gradiente/           svg · png 1x 2x 4x · pdf
  favicon/             svg · png 1x 2x 4x · pdf
  paleta/              svg · png · pdf · ase · gpl · txt · json
  fonte/               playfair-display/ e inter/, para instalar e para web
  textura/             svg e pdf do ladrilho · png de todas
  wallpaper/           png, no tamanho nativo
  social/              png, no tamanho de cada plataforma
  splash/              png 1290 × 2796
  foto/                png
exemplos/              png e pdf das folhas do sistema
```

## Regra de ouro dos tokens

**O `DESIGN.md` é a fonte única.** `tokens.css` e `tokens.json` são gerados, não editados. Mexeu
nos tokens do `DESIGN.md`, rode:

```
python3 tokens/gerar_tokens.py
```

