#!/usr/bin/env python3
"""Varre assets/ e escreve o indice que o Claude consulta para achar cada ativo por URL.

Gera:
  ativos.json        todos os caminhos, por categoria, com a URL publica montada
  INDICE_ATIVOS.md   a versao legivel: como montar a URL e quais sao os ativos essenciais

Rode depois de acrescentar ou renomear ativo:  python3 gerar_indice_ativos.py
"""
import json, pathlib, collections

RAIZ = pathlib.Path(__file__).parent
BASE = "https://design.apicapital.com.br"
EXT_OK = {".svg", ".png", ".jpg", ".jpeg", ".pdf", ".woff2", ".otf", ".ttf", ".ase", ".gpl", ".json", ".txt", ".css"}

arquivos = sorted(
    p for p in (RAIZ / "assets").rglob("*")
    if p.is_file() and p.suffix.lower() in EXT_OK and not p.name.startswith(".")
)

por_cat = collections.defaultdict(list)
for p in arquivos:
    rel = p.relative_to(RAIZ).as_posix()
    por_cat[p.relative_to(RAIZ / "assets").parts[0]].append(rel)

(RAIZ / "ativos.json").write_text(json.dumps({
    "base": BASE,
    "total": len(arquivos),
    "categorias": {c: sorted(v) for c, v in sorted(por_cat.items())},
}, ensure_ascii=False, indent=1), encoding="utf-8")

ESSENCIAIS = [
    ("Logo principal, azul, para fundo claro", "assets/logo/svg/api_capital_logo01_azul.svg"),
    ("Logo principal, branco, para fundo escuro", "assets/logo/svg/api_capital_logo01_branco.svg"),
    ("Selo do pelicano, azul (todas as versões do pássaro em assets/logo/pelicano/)",
     "assets/logo/pelicano/svg/api_capital_logo05_azul.svg"),
    ("Ícone temático da API (24 deles em assets/icone/svg/)", "assets/icone/svg/api_capital_icone_carteira.svg"),
    ("Favicon", "assets/favicon/svg/api_capital_favicon.svg"),
    ("Ladrilho do ninho, azul", "assets/textura/svg/api_capital_textura_ninho_azul.svg"),
    ("Gradiente azul", "assets/gradiente/svg/api_capital_gradiente_azul.svg"),
    ("Foto de céu com rastro de avião", "assets/foto/png/api_capital_foto_ceu_aviao_rastro.png"),
]
linhas = [
    "# Índice de ativos da API Capital",
    "",
    "Todo ativo deste pacote tem endereço público e estável. A URL se monta assim:",
    "",
    f"```\n{BASE}/<caminho do arquivo>\n```",
    "",
    f"Exemplo: `{BASE}/assets/logo/svg/api_capital_logo01_azul.svg`",
    "",
    "**A lista completa, com os "
    f"{len(arquivos)} arquivos, está em `ativos.json`**, no mesmo padrão de URL.",
    "",
    "## O que existe, por categoria",
    "",
    "| Categoria | Arquivos |",
    "|---|---|",
]
for cat, itens in sorted(por_cat.items()):
    linhas.append(f"| `assets/{cat}/` | {len(itens)} |")
linhas += [
    "",
    "## Para escolher vendo",
    "",
    f"A galeria com prévia de cada ativo, os formatos e a URL pronta para copiar está em",
    f"**{BASE}/ativos/**. Ela lê este mesmo `ativos.json`, então nunca fica defasada.",
    "",
    "## Os essenciais, com a URL pronta", "", "| O que é | URL |", "|---|---|",
]
for nome, rel in ESSENCIAIS:
    existe = (RAIZ / rel).exists()
    linhas.append(f"| {nome} | `{BASE}/{rel}`{'' if existe else ' ⚠️ não encontrado'} |")
linhas += [
    "",
    "## Regra de uso",
    "",
    "Em peça de tela, referencie o ativo pela URL: não copie o arquivo e não redesenhe nada.",
    "O logo nunca se remonta com texto, e ícone se pega em `assets/icone/lucide/`, que traz a",
    "biblioteca Lucide completa em SVG.",
    "",
]
(RAIZ / "INDICE_ATIVOS.md").write_text("\n".join(linhas), encoding="utf-8")
# versao.json: o carimbo que a skill compara para saber se esta lendo material velho
import re
fm = (RAIZ / "DESIGN.md").read_text(encoding="utf-8")[:400]
versao = re.search(r'version:\s*"([^"]+)"', fm).group(1)
(RAIZ / "versao.json").write_text(json.dumps({
    "design_system": versao,
    "ativos": len(arquivos),
    "base": BASE,
}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

print(f"ativos.json e INDICE_ATIVOS.md: {len(arquivos)} arquivos em {len(por_cat)} categorias")
