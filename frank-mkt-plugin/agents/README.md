# Agents — Frank MKT

> 16 agentes implementados. Cada agente é arquivo `.md` com frontmatter YAML + persona + skills consultadas + frameworks + workflow + cross-skill + disclaimer.

## Agentes implementados (16/16 — v2.38.1)

| Arquivo | Agente | Função | Acionamento |
|---------|--------|--------|-------------|
| `frank-mkt.md` | `frank-mkt` | **Principal** — persona + motor cognitivo + contraditório, orquestra 93 skills + 16 agentes (incluindo este principal) + 10 commands | Default |
| `atelier-criativo.md` | `atelier-criativo` | **Artista digital generalista** — visão estética + sinestesia entre domínios + síntese de mestres em voz própria. Não é desenvolvedor; SVG é apenas um pincel | Brief tem ambiguidade criativa real ou cruza domínios (visual + textual + musical + conceitual) |
| `renderer-visual.md` | `renderer-visual` | **Agente operacional** — render-loop visual via Bash + headless browser + Read multimodal. Fecha o loop "Write SVG -> Render PNG -> Read multimodal -> Edit" que outros agentes visuais (atelier-criativo, ux-ui-revisor) não conseguem sozinhos. NÃO toma decisões estéticas | SVG/HTML denso (>200 linhas, ilustrações, formulas, infograficos) requer validação visual antes de entregar |
| `juiz.md` | `juiz` | Arbitrador imparcial — decide divergência entre agentes (6 critérios hierárquicos) | Sob demanda qualificada |
| `auditor.md` | `auditor` | Varredura mecânica PASS/FAIL (7 checklists, 3 níveis severidade) | Antes de entregar peça |
| `investigador.md` | `investigador` | Entrevista interlocutor (5 blocos), extrai fatos marca/produto/persona | Início do caso |
| `perfilador-mercado.md` | `perfilador-mercado` | Sizing TAM/SAM/SOM + persona + concorrência + white-space + trends | Quando tese depende de leitura de mercado |
| `redator-hacker.md` | `redator-hacker` | Copy alta conversão **ANTI-dark-pattern** + frameworks Schwartz/Cialdini/Brasil | Briefing copy/landing/anúncio |
| `seo-strategist.md` | `seo-strategist` | SEO + GEO 2026 + Core Web Vitals INP + autoridade + evergreen | Conteúdo orgânico |
| `social-media-linkedin.md` | `social-media-linkedin` | LinkedIn — B2B, employer brand, TLAs, Buying Group Targeting | Conteúdo/ads LinkedIn |
| `social-media-instagram.md` | `social-media-instagram` | Instagram — Reels-first, Brasil micro-influência #1, CTWA | Conteúdo/ads Instagram |
| `social-media-facebook.md` | `social-media-facebook` | Facebook — 35-65, Groups, Marketplace, CAPI | Conteúdo/ads Facebook |
| `ux-ui-revisor.md` | `ux-ui-revisor` | Nielsen 10 + WCAG 2.2 + Core Web Vitals + LBI Brasil | Revisão landing/app/produto |
| `psicologia-influencia.md` | `psicologia-influencia` | Cialdini + Kahneman + Top 20 vieses + ANTI-dark-pattern firme | Mensagem persuasiva ou audit ético |
| `frank-corporativo.md` | `frank-corporativo` | PESO + IR + ESG + Crisis + Employer Branding + ABERJE/ABRACOM | Peça corporativa |
| `social-humanitario.md` | `social-humanitario` | Causas + ESG + AA1000 + SROI + ANTI-greenwashing | Marca de propósito / ONGs |

## Diferenças importantes entre agentes

### `atelier-criativo` vs skill `svg-engineering-ia`

| Aspecto | `atelier-criativo` (agente) | `svg-engineering-ia` (skill) |
|---------|-----------------------------|------------------------------|
| Natureza | Persona com visão estética | Ferramenta técnica |
| Decide | O QUE criar | COMO criar (técnico) |
| Domínios | Site + proposta + SVG + naming + manifesto + sinestesia | SVG vetorial específico |
| Tom | Voz própria defendida | Metodológico neutro |
| Output | Proposta autoral com filosofia | Código SVG validado |
| Quando | Brief criativo aberto | Execução técnica vetorial |

### `atelier-criativo` vs `redator-hacker`

| Aspecto | `atelier-criativo` | `redator-hacker` |
|---------|---------------------|-------------------|
| Foco | Visão poética/estética cross-domain | Copy de conversão tática |
| Frameworks | Síntese arte (Bauhaus + Tarsila + Wong Kar-wai) | Schwartz + Cialdini + Maccedo |
| Tensão | Defende visão artística contra performance | Conversão ética sem dark-pattern |
| Colaboração | Yin (visão) | Yang (tática) |

### `atelier-criativo` vs `frank-corporativo`

| Aspecto | `atelier-criativo` | `frank-corporativo` |
|---------|---------------------|---------------------|
| Foco | Manifesto + visão poética | PESO + IR + governança institucional |
| Tom | Posição estética defendida | Compliance + stakeholders múltiplos |
| Colaboração | Visão | Estrutura |

> Ordem de implementação e roadmap em [`../../docs_mkt/ROADMAP-FRANK-MKT.md`](../../docs_mkt/ROADMAP-FRANK-MKT.md).
