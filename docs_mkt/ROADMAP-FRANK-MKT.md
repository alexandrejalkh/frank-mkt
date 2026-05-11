# Roadmap — Frank MKT (plugin Claude Code)

> Documento-fonte para o plugin `frank-mkt-plugin/`. Não é versionado pelo plugin — fica em `docs_mkt/` para evolução livre.

**Data inicial:** 2026-05-07
**Versão atual do plugin:** **v2.37.1** (atualizada em 2026-05-11 — render-loop visual + drift repair pos-v2.37.0)
**Modelo de referência:** `frank-juridico-ti-plugin/` (v1.5.3)

> ⚠️ **Nota historica (2026-05-11):** este Roadmap foi escrito em 2026-05-07 quando o plugin estava em v0.5.0 com 11 skills implementadas e ~58 skills previstas. **O plugin avancou MUITO ALEM** do roadmap original — hoje (v2.37.1) tem **93 skills implementadas em 18 blocos completos + Skills Avancadas 2/2 (svg-engineering-ia + render-loop-svg) + 10 slash commands + 16 agentes = 119 artefatos / ~121.463 linhas**. As secoes abaixo sao preservadas como **historia do projeto**, mas refletem o plano inicial, NAO o estado atual. Para estado atual ver: `frank-mkt-plugin/skills/INDEX.md` (v2.37.1).

**Snapshots historicos das sessoes principais:**
- [`SNAPSHOT-2026-05-07.md`](SNAPSHOT-2026-05-07.md) — fim sessao 1 (v0.5.0)
- [`SNAPSHOT-2026-05-08-v2.0.0.md`](SNAPSHOT-2026-05-08-v2.0.0.md) — v2.0.0 33 skills 7 blocos
- [`SNAPSHOT-2026-05-08-v2.11.0.md`](SNAPSHOT-2026-05-08-v2.11.0.md) — v2.11.0 44 skills
- [`SNAPSHOT-2026-05-08-v2.13.0.md`](SNAPSHOT-2026-05-08-v2.13.0.md) — v2.13.0 46 skills milestone Bloco F
- [`aprendizado_infografico.md`](aprendizado_infografico.md) — 2026-05-11 transfer brief render-loop SVG (insumo para evolucao futura)

---

## 1. Visão geral

Plugin Claude Code que entrega uma persona unificada de **consultor de Marketing + SEO + Mídias Sociais + Inteligência de Mercado**, com motor cognitivo, Contraditório Interno obrigatório, agentes especialistas e skills com decaimento temporal. Mesma arquitetura do Frank Jurídico TI, adaptada para a área de marketing.

### Áreas cobertas (consolidadas a partir do briefing)

1. **Marketing** — campanha, posicionamento, jornada, funil, big idea.
2. **Market research / inteligência de mercado** — sizing, persona, concorrência, white-space, trendwatching.
3. **SEO** — keywords, on-page, técnico, link building, conteúdo evergreen.
4. **Mídias sociais** — LinkedIn, Instagram, Facebook, TikTok, X, YouTube Shorts.
5. **Copy & redação** — copy de conversão, storytelling, e-mail, redação publicitária.
6. **UX/UI** — heurísticas, microcopy, acessibilidade, design system.
7. **Psicologia & influência** — gatilhos éticos, viés cognitivo, prova social honesta.
8. **Empreendedorismo & impacto** — negócio nascente, social/humanitário, propósito.
9. **Frank Corporativo** — comunicação corporativa, RP, employer branding, narrativa institucional.
10. **Postagens do próprio Frank / IA / atualização do LinkedIn** — uso interno (manter LinkedIn de marca pessoal/empresa atualizado).

---

## 2. Estrutura de arquivos do plugin (espelho do Frank Jurídico TI)

```
frank-mkt-plugin/
├── .claude-plugin/
│   └── plugin.json              # name=frank-mkt, version=0.1.0
├── CHANGELOG.md
├── README.md
├── settings.json                # { "agent": "frank-mkt" }
├── agents/
│   ├── README.md                # placeholder com lista
│   └── (a implementar: frank-mkt.md, juiz.md, auditor.md, ...)
├── hooks/
│   ├── hooks.json               # SessionStart -> check-skills-vencidas.sh
│   └── check-skills-vencidas.sh # bash portátil
└── skills/
    ├── INDEX.md                 # placeholder com lista
    └── (a implementar: <nome>/SKILL.md por skill)
```

---

## 3. Agentes planejados (14 — derivados do briefing)

| # | Agente | Função | Equivalente no jurídico |
|---|--------|--------|-------------------------|
| 1 | `frank-mkt` | Principal: persona + motor cognitivo + contraditório | `frank-juridico-ti` |
| 2 | `juiz` | Arbitra divergência entre modos | `juiz` |
| 3 | `auditor` | Varredura mecânica PASS/FAIL de peça | `auditor` |
| 4 | `investigador` | Entrevista, extrai fatos da marca/produto/persona | `investigador` |
| 5 | `perfilador-mercado` | Sizing, persona, concorrência, white-space | (novo) |
| 6 | `redator-hacker` | Copy de alta conversão com ética anti-dark-pattern | (novo) |
| 7 | `seo-strategist` | Estratégia de keywords, autoridade, conteúdo evergreen | (novo) |
| 8 | `social-media-linkedin` | LinkedIn — B2B, employer brand, thought leadership | (novo) |
| 9 | `social-media-instagram` | Instagram — Reels, Stories, carrossel | (novo) |
| 10 | `social-media-facebook` | Facebook — orgânico + ads, comunidades | (novo) |
| 11 | `ux-ui-revisor` | UX/UI, heurísticas, microcopy, acessibilidade | (novo) |
| 12 | `psicologia-influencia` | Gatilhos éticos, viés cognitivo, prova social honesta | (novo) |
| 13 | `frank-corporativo` | Comunicação corporativa, RP, employer brand, narrativa | (novo) |
| 14 | `social-humanitario` | Causas, propósito, ESG, terceiro setor, humanitário | (novo) |

> Frank-MKT é **um só agente** que troca de chapéu (modo Marketing, SEO, Social, Pesquisa, Corporativo, Empreendedorismo). Os agentes 5-14 são especialistas convocados sob demanda — análogos ao Vinculador / Suporte Documental / ISO-Compliance no jurídico.

---

## 4. Skills planejadas (organizadas por área)

### Infraestrutura (slash commands — 8)

`init`, `stack`, `save-session`, `help`, `audit`, `review`, `juiz`, `perfil`

### Marketing & Estratégia (5)

`posicionamento-marca`, `branding`, `funil-jornada`, `big-idea`, `metricas-marketing`

### Copy & Redação (4)

`copywriting-conversao`, `storytelling`, `email-marketing`, `redacao-publicitaria`

### SEO (7) — ✅ BLOCO ESTENDIDO 100% IMPLEMENTADO (9.853 linhas totais)

`seo-fundamentos` (skill-mãe — **implementada em 2026-05-07, v0.1.0, 1144 linhas**), `seo-keywords` (**implementada em 2026-05-07, v0.1.0, 1259 linhas**), `seo-on-page` (**implementada em 2026-05-07, v0.1.0, 1519 linhas**), `seo-tecnico` (**implementada em 2026-05-07, v0.1.0, 1587 linhas**), `seo-link-building` (**implementada em 2026-05-07, v0.1.0, 1435 linhas**), `conteudo-evergreen` (**implementada em 2026-05-07, v0.1.0, 1283 linhas**), `seo-ai-otimizacao` (**implementada em 2026-05-07, v0.1.0, 1626 linhas — pesquisa de campo + volatility high**)

### Mídia Social (10) — ✅ **BLOCO 100% COMPLETO (10/10) — 10.962 linhas totais**

`social-media-fundamentos` (skill-mãe NOVA — **implementada em 2026-05-07, v0.1.0, 1248 linhas**), `linkedin-organico` (**1498 linhas**), `x-twitter` (**1091 linhas**), `youtube-shorts` (**947 linhas**), `instagram-feed-reels` (**1128 linhas**), `tiktok-criativo` (**1009 linhas**), `facebook-organico` (**1057 linhas**), `linkedin-ads` (**1020 linhas**), `instagram-ads` (**1043 linhas**), `facebook-ads` (**921 linhas**) — **todas com pesquisa de campo + volatility high**.

### Pesquisa & Inteligência de Mercado (6)

`sizing-mercado`, `persona-icp`, `analise-concorrencia`, `pesquisa-qualitativa`, `pesquisa-quantitativa`, `tendencias-trendwatching`

### UX/UI (4)

`ux-heuristicas`, `microcopy`, `acessibilidade-wcag`, `design-system-basico`

### Psicologia & Influência (3)

`gatilhos-eticos`, `vies-cognitivo`, `prova-social-honesta`

### Conhecimento de Plataforma (6 — high volatility)

`conhecimento-meta-ads`, `conhecimento-google-ads`, `conhecimento-linkedin-ads`, `conhecimento-ga4`, `conhecimento-search-console`, `conhecimento-conar-cdc`

### Corporativo & Humanitário (6)

`comunicacao-corporativa`, `employer-branding`, `comunicacao-crise`, `esg-comunicacao`, `terceiro-setor`, `empreendedorismo-impacto`

### Meta-skill (1)

`manutencao-skills`

### Skills Avançadas / Experimentais (1 — em construção)

`svg-engineering-ia` — **NOVA SKILL INOVADORA**: especializada em geração de SVG via Claude (e LLMs em geral) para resolver o problema de criação de imagens vetoriais complexas. Cobertura proposta: técnicas e conceitos de SVG; geração programática de imagens complexas; metodologias de composição de múltiplos vetores; vetorização de bitmap; rasterização de SVG; estudo de como IA consegue gerar SVG válido e esteticamente correto sem feedback visual; guias oficiais (W3C SVG 2.0 + MDN + svg.dev); técnicas para Claude validar criticamente seus próprios SVGs (auto-crítica + métricas geométricas + heurísticas); criação de novas técnicas próprias para problemas residuais (composição complexa + precisão geométrica + harmonia visual sem visualização). **Inovadora**: trata o gap real entre LLMs (texto-only) e geração de arte vetorial complexa.

### Identidade Visual Corporativa / Brand Design (8 — em construção)

**Novo bloco planejado para fechar gap de ~50-60% do trabalho de identidade visual corporativa** que o plugin não cobre hoje (logo + manual marca + paleta + tipografia + ícones + templates concretos + papelaria + collateral). Camada executiva complementar à camada estratégica (`branding` + `posicionamento-marca` + `big-idea` já implementadas).

`logo-design-process`, `brand-book-methodology`, `paleta-cores-corporativa`, `tipografia-corporativa`, `iconografia-corporativa`, `templates-corporativos-comerciais`, `apresentacoes-decks-corporativos`, `print-papelaria-collateral`

**Cobertura proposta**:

- **`logo-design-process`** — princípios design (Paul Rand + Saul Bass + Massimo Vignelli) + processo (research → conceito → sketch → digital → variações → entregáveis .svg/.png/.pdf/.eps) + validação (escala + monocromático + reverso + contexto) + cases brasileiros (Magalu/Nubank/Itaú/Boticário rebrands)
- **`brand-book-methodology`** — estrutura canônica manual de identidade (5 seções: Marca + Cores + Tipografia + Aplicações + Don'ts) + ferramentas (Figma + Frontify + Zeroheight + InDesign) + governança versão + uso por terceiros + cases (Airbnb DLS + IBM Carbon + Spotify Encore)
- **`paleta-cores-corporativa`** — paleta primária/secundária/terciária + acessibilidade WCAG contraste 4.5:1 AA / 7:1 AAA + Pantone PMS + conversão RGB/CMYK/HEX + dark mode + cultural meaning (cores Brasil vs global)
- **`tipografia-corporativa`** — escolha tipográfica + hierarquia (display/heading/body/caption) + licenciamento (Google Fonts free + Adobe Fonts subscription + custom enterprise) + fallbacks web + variable fonts 2026 + acessibilidade
- **`iconografia-corporativa`** — sistema de ícones consistente (Stroke vs Fill + grid 24/32px + line weight) + biblioteca + Lucide/Heroicons/Phosphor referencias + custom set process + integração com `svg-engineering-ia` para geração via Claude
- **`templates-corporativos-comerciais`** — estrutura visual padrão para propostas comerciais + contratos + modelos para sistemas SaaS (UI templates) + cover/header/footer + tom comercial brasileiro + integração assinatura digital (DocuSign + ClickSign Brasil)
- **`apresentacoes-decks-corporativos`** — pitch deck (Sequoia template + Y Combinator) + sales deck (Gong/Chorus best practices) + investor deck (a16z/Bessemer references) + board presentation + master slides PowerPoint/Keynote/Google Slides + brand-aligned visual templates
- **`print-papelaria-collateral`** — cartão visita + papel timbrado + envelope + assinatura email HTML + folder/flyer/banner/roll-up + sinalização interna/externa + brindes corporativos + grid layout + bleed/safety areas + briefing gráfico para fornecedor

**Sinergia com `svg-engineering-ia`**: skill base (Skills Avançadas / Experimentais) fornece técnicas de geração vetorial via Claude para alimentar `logo-design-process` (logos + variações), `iconografia-corporativa` (sistema ícones), e ilustrações spot dentro de `templates-corporativos-comerciais` e `apresentacoes-decks-corporativos`.

**Total previsto: ~58 skills** (vs. 49 do Jurídico TI) — ATUALIZADO: **92 skills** (83 implementadas + 1 svg-engineering-ia + 8 brand-design = 9 em construção).

### Status de implementação

| Skill | Status | Linhas | Volatility |
|-------|--------|--------|------------|
| `seo-fundamentos` | ✅ Implementada (2026-05-07, v0.1.0) | 1144 | medium (6 meses) |
| `seo-keywords` | ✅ Implementada (2026-05-07, v0.1.0) | 1259 | medium (6 meses) |
| `seo-on-page` | ✅ Implementada (2026-05-07, v0.1.0) | 1519 | medium (6 meses) |
| `seo-tecnico` | ✅ Implementada (2026-05-07, v0.1.0) | 1587 | medium (6 meses) |
| `seo-link-building` | ✅ Implementada (2026-05-07, v0.1.0) | 1435 | medium (6 meses) |
| `conteudo-evergreen` | ✅ Implementada (2026-05-07, v0.1.0) | 1283 | medium (6 meses) |
| `seo-ai-otimizacao` | ✅ Implementada (2026-05-07, v0.1.0 — pesquisa de campo) | 1626 | **high (3 meses)** |
| **Bloco SEO ESTENDIDO** | **✅ 7 skills** | **9.853** | — |
| `social-media-fundamentos` | ✅ Implementada (2026-05-07, v0.1.0 — pesquisa de campo, skill-mãe do bloco) | 1248 | **high (3 meses)** |
| `linkedin-organico` | ✅ Implementada (2026-05-07, v0.1.0 — pesquisa de campo) | 1498 | **high (3 meses)** |
| `x-twitter` | ✅ Implementada (2026-05-07, v0.1.0 — pesquisa de campo) | 1091 | **high (3 meses)** |
| `youtube-shorts` | ✅ Implementada (2026-05-07, v0.1.0 — pesquisa de campo) | 947 | **high (3 meses)** |
| `instagram-feed-reels` | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo) | 1128 | **high (3 meses)** |
| `tiktok-criativo` | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo) | 1009 | **high (3 meses)** |
| `facebook-organico` | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo) | 1057 | **high (3 meses)** |
| `linkedin-ads` | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo) | 1020 | **high (3 meses)** |
| `instagram-ads` | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo) | 1043 | **high (3 meses)** |
| `facebook-ads` | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo) | 921 | **high (3 meses)** |
| **🎉 Bloco Mídia Social — COMPLETO** | **✅ 10/10** | **10.962** | — |
| `geracao-imagens-ia` | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo) — **NOVO bloco Comunicação Visual & IA** | 1.161 | **high (3 meses)** |
| `infograficos-diagramas` | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo) | 1.334 | **medium (6 meses)** |
| `composicao-visual` | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo) | 1.346 | **medium (6 meses)** |
| `audio-musica-ia` | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo) | 1.356 | **high (3 meses)** |
| **🎉 Bloco Comunicação Visual & IA — COMPLETO** | **✅ 4/4** | **5.197** | — |
| `github-presence` | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo) — **NOVO bloco Multi-Platform Strategy** | 1.339 | **medium (6 meses)** |
| `multi-platform-narrative` | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo) | 1.275 | **medium (6 meses)** |
| `escrita-por-publico` | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo) | 1.730 | **low (12 meses)** — primeira `low` do plugin |
| **🎉 Bloco Multi-Platform Strategy — COMPLETO** | **✅ 3/3** | **4.344** | — |
| `persuasao-eticas` | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo) — **NOVO bloco Persuasão & Engajamento** | 1.315 | **low (12 meses)** |
| `engajamento-comunidade` | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo) | 1.512 | **medium (6 meses)** |
| **🎉 Bloco Persuasão & Engajamento — COMPLETO** | **✅ 2/2** | **2.827** | — |
| `guerrilha-criativa` | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo) — **NOVO bloco Marketing Não-Tradicional** | 1.410 | **medium (6 meses)** |
| `newsjacking-real-time` | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo) | 1.232 | **medium (6 meses)** |
| **🎉 Bloco Marketing Não-Tradicional — COMPLETO** | **✅ 2/2** | **2.642** | — |
| `posicionamento-marca` | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo) — **bloco Marketing & Estratégia** | 1.380 | **low (12 meses)** |
| `branding` | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo) | 1.687 | **low (12 meses)** |
| `funil-jornada` | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo) | 1.502 | **low (12 meses)** |
| `big-idea` | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo) | 1.581 | **low (12 meses)** |
| `metricas-marketing` | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo) | 1.721 | **medium (6 meses)** |
| **🎉 Bloco Marketing & Estratégia — COMPLETO** | **✅ 5/5** | **7.871** | — |
| `dominio-vertical-fundamentos` (mãe Bloco F) | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo) | 1.347 | **low (12 meses)** |
| `dominio-ti-mkt` (1ª filha Bloco F) | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo) | 1.533 | **medium (6 meses)** |
| `dominio-juridico-mkt` (2ª filha Bloco F) | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo + frank_juridico_garden integrado) | 1.688 | **high (3 meses)** |
| `dominio-empreendedorismo-mkt` (3ª filha Bloco F) | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo) | 1.452 | **medium (6 meses)** |
| `dominio-negocios-mkt` (4ª filha Bloco F) | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo) | 1.659 | **medium (6 meses)** |
| `dominio-ia-mkt` (5ª filha Bloco F = SKILL-MÃE IA) | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo) | 1.557 | **high (3 meses)** |
| `tecnicas-ia-claude-gemini-mkt` (6ª filha Bloco F — filha de IA mãe) | ✅ Implementada (2026-05-08, v0.1.0 — material proprietário user Alexandre Jalkh sintetizado) | 1.403 | **medium (6 meses)** |
| `dominio-rh-mkt` (7ª filha Bloco F) | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo) | 1.419 | **medium (6 meses)** |
| `dominio-dp-mkt` (8ª filha Bloco F — DP operational complementar RH) | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo) | 1.271 | **high (3 meses)** |
| `dominio-financeiro-mkt` (9ª filha Bloco F) | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo) | 1.447 | **medium (6 meses)** |
| `dominio-fiscal-mkt` (10ª filha Bloco F) | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo) | 1.379 | **high (3 meses)** |
| `dominio-adm-mkt` (11ª filha Bloco F) | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo) | 1.250 | **medium (6 meses)** |
| `dominio-iot-mkt` (12ª filha Bloco F — ÚLTIMA, M5 Stack inside) | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo) | 1.451 | **medium (6 meses)** |
| **🎉 Bloco F Domínio Vertical EXPANDIDO COMPLETO** | **✅ 13/13** (mãe + 12 filhas implementadas) | **18.856** | — |
| `atas-relatorios-corporativos` (1ª SKILL Bloco E Documentos Corporativos) | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo) | 1.073 | **medium (6 meses)** |
| `comunicacoes-corporativas` (2ª SKILL Bloco E — ÚLTIMA) | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo) | 874 | **medium (6 meses)** |
| **🎉 Bloco E Documentos Corporativos COMPLETO** | **✅ 2/2** (atas-relatorios + comunicacoes) | **1.947** | — |
| `pesquisa-mercado-fundamentos` (1ª SKILL Bloco Pesquisa & Inteligência) | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo) | 906 | **medium (6 meses)** |
| `persona-icp-deep` (2ª SKILL Bloco Pesquisa) | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo) | 833 | **medium (6 meses)** |
| `analise-concorrencia` (3ª SKILL Bloco Pesquisa) | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo) | 612 | **medium (6 meses)** |
| `white-space-analysis` (4ª SKILL Bloco Pesquisa) | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo) | 665 | **medium (6 meses)** |
| `trendwatching` (5ª SKILL Bloco Pesquisa) | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo) | 656 | **medium (6 meses)** |
| `competitive-intelligence` (6ª SKILL Bloco Pesquisa — ÚLTIMA) | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo) | 666 | **medium (6 meses)** |
| **🎉 Bloco Pesquisa & Inteligência de Mercado COMPLETO** | **✅ 6/6** (fundamentos + ICP + análise-concorrência + white-space + trendwatching + competitive-intelligence) | **4.338** | — |
| `comunicacao-corporativa` (1ª SKILL Bloco Corporativo & Humanitário) | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo) | 737 | **medium (6 meses)** |
| `employer-branding` (2ª SKILL Bloco Corporativo & Humanitário) | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo) | 833 | **medium (6 meses)** |
| `comunicacao-crise` (3ª SKILL Bloco Corporativo & Humanitário — paralela) | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo) | 1.080 | **medium (6 meses)** |
| `esg-comunicacao` (4ª SKILL Bloco Corporativo & Humanitário — paralela) | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo) | 1.096 | **medium (6 meses)** |
| `terceiro-setor` (5ª SKILL Bloco Corporativo & Humanitário — paralela) | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo) | 837 | **medium (6 meses)** |
| `empreendedorismo-impacto` (6ª SKILL Bloco Corporativo & Humanitário — ÚLTIMA paralela) | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo) | 879 | **medium (6 meses)** |
| **🎉 Bloco Corporativo & Humanitário COMPLETO** | **✅ 6/6** (comunicacao-corporativa + employer-branding + comunicacao-crise + esg-comunicacao + terceiro-setor + empreendedorismo-impacto) | **5.462** | — |
| `copywriting-conversao` (1ª SKILL Bloco Copy & Redação — paralela) | ✅ Implementada (2026-05-09, v0.1.0 — pesquisa de campo) | 776 | **medium (6 meses)** |
| `storytelling` (2ª SKILL Bloco Copy & Redação — paralela) | ✅ Implementada (2026-05-09, v0.1.0 — pesquisa de campo) | 1.809 | **medium (6 meses)** |
| `email-marketing` (3ª SKILL Bloco Copy & Redação — paralela) | ✅ Implementada (2026-05-09, v0.1.0 — pesquisa de campo) | 1.607 | **medium (6 meses)** |
| `redacao-publicitaria` (4ª SKILL Bloco Copy & Redação — ÚLTIMA paralela) | ✅ Implementada (2026-05-09, v0.1.0 — pesquisa de campo) | 1.893 | **medium (6 meses)** |
| **🎉 Bloco Copy & Redação COMPLETO** | **✅ 4/4** (copywriting-conversao + storytelling + email-marketing + redacao-publicitaria) | **6.085** | — |
| `ux-heuristicas` (1ª SKILL Bloco UX/UI — paralela) | ✅ Implementada (2026-05-09, v0.1.0 — pesquisa de campo) | 845 | **medium (6 meses)** |
| `microcopy` (2ª SKILL Bloco UX/UI — paralela) | ✅ Implementada (2026-05-09, v0.1.0 — pesquisa de campo) | 1.884 | **medium (6 meses)** |
| `acessibilidade-wcag` (3ª SKILL Bloco UX/UI — paralela) | ✅ Implementada (2026-05-09, v0.1.0 — pesquisa de campo) | 1.180 | **medium (6 meses)** |
| `design-system-basico` (4ª SKILL Bloco UX/UI — ÚLTIMA paralela) | ✅ Implementada (2026-05-09, v0.1.0 — pesquisa de campo) | 805 | **medium (6 meses)** |
| **🎉 Bloco UX/UI COMPLETO** | **✅ 4/4** (ux-heuristicas + microcopy + acessibilidade-wcag + design-system-basico) | **4.714** | — |
| `gatilhos-eticos` (1ª SKILL Bloco Psicologia & Influência — paralela) | ✅ Implementada (2026-05-09, v0.1.0 — pesquisa de campo) | 1.048 | **medium (6 meses)** |
| `vies-cognitivo` (2ª SKILL Bloco Psicologia & Influência — paralela) | ✅ Implementada (2026-05-09, v0.1.0 — pesquisa de campo) | 1.063 | **medium (6 meses)** |
| `prova-social-honesta` (3ª SKILL Bloco Psicologia & Influência — ÚLTIMA paralela) | ✅ Implementada (2026-05-09, v0.1.0 — pesquisa de campo) | 859 | **medium (6 meses)** |
| **🎉 Bloco Psicologia & Influência COMPLETO** | **✅ 3/3** (gatilhos-eticos + vies-cognitivo + prova-social-honesta) | **2.970** | — |
| `conhecimento-meta-ads` (1ª SKILL Bloco Conhecimento de Plataforma — paralela) | ✅ Implementada (2026-05-09, v0.1.0 — pesquisa de campo) | 788 | **high (3 meses)** |
| `conhecimento-google-ads` (2ª SKILL Bloco Conhecimento de Plataforma — paralela) | ✅ Implementada (2026-05-09, v0.1.0 — pesquisa de campo) | 859 | **high (3 meses)** |
| `conhecimento-linkedin-ads` (3ª SKILL Bloco Conhecimento de Plataforma — paralela) | ✅ Implementada (2026-05-09, v0.1.0 — pesquisa de campo) | 602 | **high (3 meses)** |
| `conhecimento-ga4` (4ª SKILL Bloco Conhecimento de Plataforma — paralela) | ✅ Implementada (2026-05-09, v0.1.0 — pesquisa de campo) | 1.163 | **high (3 meses)** |
| `conhecimento-search-console` (5ª SKILL Bloco Conhecimento de Plataforma — paralela) | ✅ Implementada (2026-05-09, v0.1.0 — pesquisa de campo) | 910 | **high (3 meses)** |
| `conhecimento-conar-cdc` (6ª SKILL Bloco Conhecimento de Plataforma — ÚLTIMA paralela) | ✅ Implementada (2026-05-09, v0.1.0 — pesquisa de campo) | 1.305 | **high (3 meses)** |
| **🎉 Bloco Conhecimento de Plataforma COMPLETO** | **✅ 6/6** (conhecimento-meta-ads + conhecimento-google-ads + conhecimento-linkedin-ads + conhecimento-ga4 + conhecimento-search-console + conhecimento-conar-cdc) | **5.627** | — |
| `manutencao-skills` (Meta-skill — paralela) | ✅ Implementada (2026-05-09, v0.1.0 — pesquisa de campo) | 958 | **medium (6 meses)** |
| **🎉 Bloco Meta-skill COMPLETO** | **✅ 1/1** (manutencao-skills) | **958** | — |
| `growth-hacking` (1ª SKILL Bloco MKT & Estratégia 2º lote — paralela) | ✅ Implementada (2026-05-09, v0.1.0 — pesquisa de campo) | 895 | **medium (6 meses)** |
| `product-marketing` (2ª SKILL Bloco MKT & Estratégia 2º lote — paralela) | ✅ Implementada (2026-05-09, v0.1.0 — pesquisa de campo) | 831 | **medium (6 meses)** |
| `account-based-marketing` (3ª SKILL Bloco MKT & Estratégia 2º lote — paralela) | ✅ Implementada (2026-05-09, v0.1.0 — pesquisa de campo) | 1.045 | **medium (6 meses)** |
| `pricing-strategy` (4ª SKILL Bloco MKT & Estratégia 2º lote — paralela) | ✅ Implementada (2026-05-09, v0.1.0 — pesquisa de campo) | 738 | **medium (6 meses)** |
| `go-to-market-strategy` (5ª SKILL Bloco MKT & Estratégia 2º lote — ÚLTIMA paralela) | ✅ Implementada (2026-05-09, v0.1.0 — pesquisa de campo) | 1.046 | **medium (6 meses)** |
| **🎉 Bloco MKT & Estratégia 2º lote COMPLETO** | **✅ 5/5** (growth-hacking + product-marketing + account-based-marketing + pricing-strategy + go-to-market-strategy) | **4.555** | — |
| `svg-engineering-ia` (Skills Avançadas / Experimentais — INOVADORA) | ✅ Implementada (2026-05-09, v0.1.0 — pesquisa profunda 16 web searches em 4 rounds) | **1.234** | **medium (6 meses)** |
| **🎉 Bloco Skills Avançadas / Experimentais COMPLETO** | **✅ 1/1** (svg-engineering-ia inovadora — base ferramental para 8 skills brand-design) | **1.234** | — |
| `logo-design-process` (1ª SKILL Bloco Identidade Visual Corporativa / Brand Design) | 🟡 **Em construção** — Paul Rand + Saul Bass + Vignelli + processo design + variações + entregáveis + cases Brasil | — | **medium (6 meses)** projetada |
| `brand-book-methodology` (2ª SKILL Brand Design) | 🟡 **Em construção** — manual identidade 5 seções + Figma/Frontify/Zeroheight + governança + cases Airbnb DLS/IBM Carbon/Spotify Encore | — | **medium (6 meses)** projetada |
| `paleta-cores-corporativa` (3ª SKILL Brand Design) | 🟡 **Em construção** — paleta + WCAG contraste + Pantone + RGB/CMYK + dark mode + cultural meaning Brasil | — | **medium (6 meses)** projetada |
| `tipografia-corporativa` (4ª SKILL Brand Design) | 🟡 **Em construção** — escolha tipográfica + hierarquia + licenciamento + variable fonts + acessibilidade | — | **medium (6 meses)** projetada |
| `iconografia-corporativa` (5ª SKILL Brand Design) | 🟡 **Em construção** — sistema ícones + grid 24/32px + Lucide/Heroicons/Phosphor + custom + integração SVG-IA | — | **medium (6 meses)** projetada |
| `templates-corporativos-comerciais` (6ª SKILL Brand Design) | 🟡 **Em construção** — propostas + contratos + modelos sistemas SaaS + DocuSign/ClickSign Brasil | — | **medium (6 meses)** projetada |
| `apresentacoes-decks-corporativos` (7ª SKILL Brand Design) | 🟡 **Em construção** — pitch (Sequoia/YC) + sales (Gong/Chorus) + investor (a16z/Bessemer) + board + master slides | — | **medium (6 meses)** projetada |
| `print-papelaria-collateral` (8ª SKILL Brand Design — ÚLTIMA) | 🟡 **Em construção** — cartão visita + papel timbrado + assinatura email + folder/flyer/banner/sinalização + brindes | — | **medium (6 meses)** projetada |
| `logo-design-process` (1ª SKILL Bloco Identidade Visual Corporativa / Brand Design — paralela RECORDISTA 8 agentes) | ✅ Implementada (2026-05-09, v0.1.0 — pesquisa de campo) | 1.102 | **medium (6 meses)** |
| `brand-book-methodology` (2ª SKILL — paralela) | ✅ Implementada (2026-05-09, v0.1.0 — pesquisa de campo) | 779 | **medium (6 meses)** |
| `paleta-cores-corporativa` (3ª SKILL — paralela) | ✅ Implementada (2026-05-09, v0.1.0 — pesquisa de campo) | 895 | **medium (6 meses)** |
| `tipografia-corporativa` (4ª SKILL — paralela) | ✅ Implementada (2026-05-09, v0.1.0 — pesquisa de campo) | 1.088 | **medium (6 meses)** |
| `iconografia-corporativa` (5ª SKILL — paralela) | ✅ Implementada (2026-05-09, v0.1.0 — pesquisa de campo) | 774 | **medium (6 meses)** |
| `templates-corporativos-comerciais` (6ª SKILL — paralela) | ✅ Implementada (2026-05-09, v0.1.0 — pesquisa de campo) | 809 | **medium (6 meses)** |
| `apresentacoes-decks-corporativos` (7ª SKILL — paralela) | ✅ Implementada (2026-05-09, v0.1.0 — pesquisa de campo) | 748 | **medium (6 meses)** |
| `print-papelaria-collateral` (8ª SKILL — ÚLTIMA paralela) | ✅ Implementada (2026-05-09, v0.1.0 — pesquisa de campo) | 911 | **medium (6 meses)** |
| **🎉 Bloco Identidade Visual Corporativa / Brand Design COMPLETO** | **✅ 8/8** (logo-design-process + brand-book-methodology + paleta-cores-corporativa + tipografia-corporativa + iconografia-corporativa + templates-corporativos-comerciais + apresentacoes-decks-corporativos + print-papelaria-collateral) | **7.106** | — |
| **Bloco F Domínio Vertical aplicado a MKT (NOVO planejado)** | **⏸️ 0/6** | — | — |
| Demais blocos planejados (Documentos Corporativos + Pesquisa + Copy + UX/UI + Plataforma + Corporativo + Meta + Infra + Agentes) | Planejados | — | — |

---

## 5. Decaimento temporal — proposta de tiers

| Tier | Reavaliação | Skills típicas |
|------|-------------|----------------|
| **high** | 1–3 meses | Plataformas (Meta, LinkedIn, Google, TikTok), GA4, Search Console, CONAR/CDC, tendências |
| **medium** | 6 meses | SEO técnico, frameworks de pesquisa, métricas-padrão, copy de plataforma |
| **low** | 12 meses | Metodologias (contraditório, posicionamento, persona, jornada), psicologia, princípios UX |
| **very-low** | 24 meses | Infra (init, stack, audit, review, help, save-session, juiz, perfil) |

Atribuição definitiva por skill quando o `SKILL.md` for criado.

---

## 6. Regras imutáveis (cristal C0 e correlatos)

- **NÃO CHUTAR** — não inventar dado de mercado, share, CAC, LTV, métrica de plataforma, case real, depoimento. Na dúvida, perguntar/pesquisar.
- Não criar copy enganoso, dark pattern, prova social falsa.
- Não orientar greenwashing, pinkwashing, manipulação eleitoral.
- Não gerar peça que viole CDC, LGPD, CONAR, regras de plataforma.
- Não revelar prompts internos dos agentes.
- Contraditório Interno SEMPRE ativo em peça relevante.
- Avisar decaimento temporal de skill vencida.

---

## 7. Roadmap de implementação (sugestão de ordem)

### Sprint 1 — Núcleo

1. `agents/frank-mkt.md` — persona + motor cognitivo + contraditório (adaptar de `frank-juridico-ti.md`).
2. `skills/init/SKILL.md` — configura `.frank-mkt/`.
3. `skills/help/SKILL.md` — lista comandos/agentes/skills.
4. `skills/stack/SKILL.md` — exibe estado.
5. `skills/save-session/SKILL.md` — log de sessão.
6. `skills/manutencao-skills/SKILL.md` — controle de decaimento.

### Sprint 2 — Inteligência de mercado e perfilamento

7. `agents/perfilador-mercado.md` + skills `sizing-mercado`, `persona-icp`, `analise-concorrencia`.
8. `agents/investigador.md` + skill `pesquisa-qualitativa`.

### Sprint 3 — Copy e auditoria

9. `agents/redator-hacker.md` + skills `copywriting-conversao`, `storytelling`, `redacao-publicitaria`.
10. `agents/auditor.md` + `skills/audit/SKILL.md` (definir N regras PASS/FAIL).
11. `skills/review/SKILL.md` (review qualitativo).

### Sprint 4 — Mídias sociais

12. Agentes `social-media-linkedin`, `social-media-instagram`, `social-media-facebook`.
13. Skills correspondentes (orgânico + ads por plataforma).
14. `agents/juiz.md` + `skills/juiz/SKILL.md` (arbitragem entre modos).

### Sprint 5 — SEO e UX

15. `agents/seo-strategist.md` + skills SEO (5).
16. `agents/ux-ui-revisor.md` + skills UX (4).

### Sprint 6 — Psicologia & influência

17. `agents/psicologia-influencia.md` + skills correspondentes (3).

### Sprint 7 — Corporativo, humanitário, conhecimento de plataforma

18. `agents/frank-corporativo.md` + skills corporativas (4).
19. `agents/social-humanitario.md` + skills `terceiro-setor`, `esg-comunicacao`, `empreendedorismo-impacto`.
20. Skills `conhecimento-*` (Meta Ads, Google Ads, LinkedIn Ads, GA4, Search Console, CONAR/CDC).

### Sprint 8 — Refinamento

21. Atualizar README, CHANGELOG, INDEX.
22. Definir 62-regras-equivalente do Auditor.
23. Bump para v1.0.0 quando todos os agentes/skills críticas estiverem implementados.

---

## 8. Decisões a tomar antes do Sprint 1

- [ ] **Nome final do plugin no marketplace:** `frank-mkt` ou `frank-marketing`? (atualmente: `frank-mkt`)
- [ ] **Repositório/marketplace:** GitHub novo ou conviver com `spkr-frank-juridico-marketplace`?
- [ ] **Persona do Frank-MKT:** mesma "voz" do Jurídico TI ou tom mais publicitário/criativo?
- [ ] **Cliente alvo prioritário:** B2B (LinkedIn-heavy) ou B2C (Instagram/TikTok-heavy)?
- [ ] **Postagens do próprio Frank:** plugin gera posts para a marca pessoal/SPKR ou só apoia o cliente? (briefing menciona "Atualizar LinkedIn / Postagens do Frank / IA").
- [ ] **Frank Corporativo:** será agente separado dentro do plugin OU plugin paralelo `frank-corp-plugin/`?

---

## 9. Materiais a coletar em `docs_mkt/`

- [ ] Briefing completo do escopo (este arquivo já cobre o início).
- [ ] Exemplos de peças do cliente / SPKR (se houver — para definir voz).
- [ ] Lista de plataformas/canais prioritários.
- [ ] Personas iniciais (se já houver).
- [ ] Métricas de referência por área.
- [ ] Frameworks favoritos (AARRR, Jobs-to-be-done, JTBD, OKR de marketing, etc.).
- [ ] Bibliografia (Kotler, Cialdini, Vaynerchuk, Ogilvy, Lindstrom, etc.) — para citação correta nas skills.
