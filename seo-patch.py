#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SEO oprava pro tetianakotolup.com

Co skript udělá:
  1) do každé stránky projektu doplní <meta name="description"> a <link rel="canonical">
     a základní Open Graph (pokud tam ještě nejsou)
  2) v index.html opraví JSON-LD: doplní LinkedIn do "sameAs", upraví "worksFor"
     a doplní "seeks" (hledá hlavní pracovní poměr) vedle stávajícího "worksFor" (OSVČ)

Spuštění ve složce repozitáře:
    python3 seo-patch.py

Skript nic nemaže, jen doplňuje. Před spuštěním si udělej `git status`,
po spuštění `git diff`, ať vidíš, co se změnilo.
"""

import re
import pathlib

DOMAIN = "https://tetianakotolup.com"

# stránka -> popis pro Google (max ~155 znaků)
PAGES = {
    "15.html": "GrowthLab AI – tři propojená n8n workflow: AI kvalifikace poptávek, Zoho CRM, analýza dialogu a reporting do Telegramu. Projekt Tetiany Kotolup.",
    "12.html": "WealthMirror AI – produkční SaaS aplikace v Telegramu: Node.js, TypeScript, OpenAI API, PostgreSQL, Supabase. Projekt Tetiany Kotolup.",
    "13.html": "AI CRM – správa klientů a schůzek přirozeným jazykem: React, Node.js, Express, OpenAI, PostgreSQL, Prisma. Projekt Tetiany Kotolup.",
    "14.html": "LegisFlow – automatizovaná analýza rizik v právních dokumentech: PDF, GPT-4o, strukturovaný report. Projekt Tetiany Kotolup.",
    "16.html": "Apulia Olive Oil CZ – vícejazyčný e-shop: produktová data, platební brána, Google Ads, GDPR Consent Mode v2. Projekt Tetiany Kotolup.",
    "1.html":  "Generátor ukrajinských měsíců – n8n workflow pro automatické zpracování dat. Projekt Tetiany Kotolup.",
    "2.html":  "Denní měnový report – automatizovaný sběr kurzů a doručení reportu. n8n. Projekt Tetiany Kotolup.",
    "3.html":  "Měsíční prodejní analytika – automatizovaný report z dat o prodejích. n8n. Projekt Tetiany Kotolup.",
    "4.html":  "Generování textů více modely a AI výběr kvality – n8n workflow. Projekt Tetiany Kotolup.",
    "5.html":  "Upozornění na cenu BTC do Telegramu – n8n workflow s API a webhooky. Projekt Tetiany Kotolup.",
    "6.html":  "Denní motivace do Telegramu – naplánované n8n workflow s Telegram Bot API. Projekt Tetiany Kotolup.",
    "7.html":  "Denní report počasí – n8n workflow s napojením na externí API. Projekt Tetiany Kotolup.",
    "8.html":  "Ukládání obrázků na Google Drive – automatizace přes Google API. n8n. Projekt Tetiany Kotolup.",
    "9.html":  "Telegram → Google Calendar – vytváření událostí z chatu. n8n, Google API. Projekt Tetiany Kotolup.",
    "10.html": "Monitoring dostupnosti webu – automatické kontroly a upozornění. n8n. Projekt Tetiany Kotolup.",
    "v.html":  "Voice to Image Generator – převod hlasu na obrázek přes AI API. Projekt Tetiany Kotolup.",
}

root = pathlib.Path(".")
changed = []

for name, desc in PAGES.items():
    p = root / name
    if not p.exists():
        print(f"  přeskočeno (soubor nenalezen): {name}")
        continue
    html = p.read_text(encoding="utf-8")

    # z <title> vytáhneme název pro og:title
    m = re.search(r"<title>(.*?)</title>", html, re.S)
    title = m.group(1).strip() if m else name

    add = []
    if 'name="description"' not in html:
        add.append(f'<meta name="description" content="{desc}">')
    if 'rel="canonical"' not in html:
        add.append(f'<link rel="canonical" href="{DOMAIN}/{name}">')
    if 'property="og:title"' not in html:
        add.append(f'<meta property="og:title" content="{title}">')
        add.append(f'<meta property="og:description" content="{desc}">')
        add.append(f'<meta property="og:url" content="{DOMAIN}/{name}">')
        add.append(f'<meta property="og:image" content="{DOMAIN}/foto.jpeg">')
        add.append('<meta property="og:type" content="article">')
    if 'name="robots"' not in html:
        add.append('<meta name="robots" content="index, follow, max-image-preview:large">')

    if not add:
        print(f"  beze změny: {name}")
        continue

    block = "\n" + "\n".join(add) + "\n"
    html = html.replace("</title>", "</title>" + block, 1)
    p.write_text(html, encoding="utf-8")
    changed.append(name)
    print(f"  opraveno: {name} (+{len(add)} tagů)")

# ---- index.html: JSON-LD ----
idx = root / "index.html"
if idx.exists():
    html = idx.read_text(encoding="utf-8")
    before = html

    # LinkedIn do sameAs
    if "linkedin.com/in/tetiana-kotolup" not in html:
        html = html.replace(
            '"sameAs": [\n    "https://github.com/tetiana-a"',
            '"sameAs": [\n    "https://www.linkedin.com/in/tetiana-kotolup/",\n    "https://github.com/tetiana-a"',
            1,
        )

    # worksFor zůstává (OSVČ) + přidáme seeks (hlavní pracovní poměr)
    if '"seeks"' not in html:
        html = html.replace(
            '"worksFor": {\n    "@type": "Organization",\n    "name": "Self-employed (OSVČ)"\n  }',
            '"seeks": {\n    "@type": "Demand",\n    "name": "Full-time position in IT support, customer support or process automation (Brno / Prague)"\n  },\n  "worksFor": {\n    "@type": "Organization",\n    "name": "Self-employed (OSVČ), Brno"\n  }',
            1,
        )

    if html != before:
        idx.write_text(html, encoding="utf-8")
        changed.append("index.html")
        print("  opraveno: index.html (JSON-LD)")
    else:
        print("  beze změny: index.html")

print()
print(f"Hotovo. Změněno souborů: {len(changed)}")
if changed:
    print("Zkontroluj `git diff`, pak:")
    print('  git add -A && git commit -m "SEO: descriptions, canonical, OG, sitemap" && git push')
