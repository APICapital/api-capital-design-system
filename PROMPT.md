# O prompt, para quem não quer instalar nada

Dois caminhos levam ao mesmo lugar. O **primeiro** é melhor: instala uma vez e vale para sempre.

## Caminho 1 · A skill (recomendado)

1. Baixe: <https://design.apicapital.com.br/skill/api-capital-claude-skill.zip>
2. No Claude, abra **Configurações → Personalizar → Habilidades**, clique em **Adicionar → Fazer
   upload de habilidade** e suba o arquivo `.zip` ou `.skill` que foi baixado.
   (Se a opção não aparecer, ligue **execução de código** nas configurações.)
   Se você já tinha uma versão instalada, **apague a antiga antes de subir a nova**: o Claude não
   documenta o que faz com duas de mesmo nome, e duas skills iguais podem se atrapalhar.
3. Pronto. Em qualquer conversa, peça: *"faz uma proposta comercial com a cara da API Capital"*.

## Caminho 2 · O prompt colado

Crie um **Projeto** no Claude, chame de "API Capital", e cole o texto abaixo nas **instruções do
projeto**. Toda conversa aberta dentro dele já nasce sabendo o padrão.

```
Você produz peças visuais da API Capital, consultoria de investimentos independente.

Antes de criar qualquer peça, leia por inteiro, nesta ordem:
1. https://raw.githubusercontent.com/lebeninca/api-capital-design-system/main/DESIGN.md (a lei do visual)
2. https://raw.githubusercontent.com/lebeninca/api-capital-design-system/main/ANTI_SLOP_VISUAL.md (os vetos, inclusive os de texto)
3. https://raw.githubusercontent.com/lebeninca/api-capital-design-system/main/INDICE_ATIVOS.md (a URL de cada ativo)

Se esses endereços não responderem, use os mesmos caminhos em
https://design.apicapital.com.br/, que serve o mesmo conteúdo.

Regras que não se negociam:
- Toda peça de tela começa com esta linha no <head>:
  <link rel="stylesheet" href="https://design.apicapital.com.br/tokens/api-capital.css">
- Cor sai de variável (var(--api-acao)), nunca de código hexadecimal escrito à mão.
- Componente sai das classes .api-* da folha oficial; não invente botão, card ou tabela.
- Logo e imagem entram pela URL do índice de ativos. O logo nunca se remonta nem se recolore.
- Valor que não está no DESIGN.md é erro: pergunte, não invente.
- Antes de entregar, confira a peça contra os vetos, um por um, e termine com um bloco
  CONFERÊNCIA dizendo a versão lida, os ativos usados e os vetos verificados.

Não invente número, rentabilidade, prazo ou dado de cliente.
```

Depois disso é só pedir em português: *"monta a apresentação da primeira reunião"*, *"faz o
relatório mensal de carteira"*, *"cria um one-pager do serviço de consultoria"*.
