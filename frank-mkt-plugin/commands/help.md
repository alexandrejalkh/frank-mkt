---
description: Lista comandos slash + agentes + skills do plugin frank-mkt agrupados por categoria
argument-hint: [filtro] (opcional - ex skills, agentes, commands, seo, social, branding, pesquisa, copy, ux, psicologia, dominio, ads, corporativo)
allowed-tools: Read, Glob
---

# /frank-mkt:help

Voce e o frank-mkt apresentando o catalogo completo do plugin. O usuario digitou /frank-mkt:help e quer descobrir o que esta disponivel. Use $ARGUMENTS como filtro opcional. Resposta em ASCII PT-BR (sem acentos), markdown limpo, listagem fiel ao estado atual do plugin.

---

## O que faz

Apresenta menu navegavel de TUDO disponivel no plugin frank-mkt:

- 10 slash commands (operacionais + analiticos + criativo + render-loop)
- 16 agentes (persona principal + 13 especialistas + atelier-criativo + renderer-visual)
- 93 skills agrupadas em 18 blocos tematicos

Filtro $ARGUMENTS afunila a listagem por categoria ou tema. Sem filtro = visao geral compacta + sugestao de proxima leitura.

---

## Workflow

1. Se $ARGUMENTS vazio: imprimir secao "Visao geral" + "Por onde comecar".
2. Se $ARGUMENTS = "commands" ou "comandos" ou "slash": imprimir bloco "10 Slash Commands" completo.
3. Se $ARGUMENTS = "agentes" ou "agents": imprimir bloco "16 Agentes" completo.
4. Se $ARGUMENTS = "skills": imprimir bloco "93 Skills" completo (todos os 18 sub-blocos).
5. Se $ARGUMENTS for tema (seo, social, branding, pesquisa, copy, ux, psicologia, dominio, ads, corporativo, identidade, ia, persuasao, guerrilha, estrategia): imprimir somente recortes relevantes (skills + agentes + commands daquele tema).
6. Sempre fechar com "Cross-references" sugerindo ordem de leitura.

---

## Visao geral

Plugin frank-mkt v2.38.1 - marketing + comunicacao + branding + render-loop visual + hardening operacional sob arquitetura Claude Code.

```
10 slash commands  -> operacao do plugin (inclui /frank-mkt:atelier + /frank-mkt:gerar-infografico)
16 agentes         -> personas especialistas (inclui atelier-criativo + renderer-visual)
93 skills (18 blocos) -> conhecimento ativavel (inclui render-loop-svg)
```

Filtros aceitos: commands | agentes | skills | seo | social | branding | pesquisa | copy | ux | psicologia | dominio | ads | corporativo | identidade | ia | persuasao | guerrilha | estrategia | arte | sinestesia

Exemplos:
- `/frank-mkt:help` -> visao geral
- `/frank-mkt:help skills` -> 92 skills agrupadas
- `/frank-mkt:help seo` -> recorte SEO (skills + agentes + commands)
- `/frank-mkt:help branding` -> recorte branding/identidade visual

---

## 10 Slash Commands

Comandos operacionais do plugin frank-mkt.

| Comando                       | Funcao                                            |
|-------------------------------|---------------------------------------------------|
| `/frank-mkt:init`             | Configura estrutura `.frank-mkt/` no projeto      |
| `/frank-mkt:stack`            | Mostra estado atual: stack, decisoes, roadmap     |
| `/frank-mkt:save-session`     | Salva log estruturado da sessao em `.frank-mkt/sessions/` |
| `/frank-mkt:help`             | Este comando - lista catalogo completo            |
| `/frank-mkt:audit`            | Varredura mecanica do auditor (PASS/FAIL por regra) |
| `/frank-mkt:review`           | Review qualitativo do trabalho de marketing       |
| `/frank-mkt:juiz`             | Arbitra divergencia entre modos/agentes (parecer imparcial) |
| `/frank-mkt:perfil`           | Perfilador de mercado: sizing + persona + concorrencia |
| `/frank-mkt:atelier`          | Atelier criativo: artista digital generalista (visao estetica + sinestesia entre dominios + anti-AI-slop) |
| `/frank-mkt:gerar-infografico` | Orquestra geracao infografico SVG denso end-to-end: atelier (visao) -> svg-engineering-ia (markup) -> renderer-visual (validacao visual real via render-loop) |

Ordem tipica:
```
/frank-mkt:init -> /frank-mkt:perfil -> [trabalho] -> /frank-mkt:audit -> /frank-mkt:review -> /frank-mkt:save-session
```

Em caso de conflito entre dois agentes ou modos: `/frank-mkt:juiz` arbitra.

---

## 16 Agentes

Personas especializadas com System Prompt proprio.

| Agente                       | Papel                                              |
|------------------------------|----------------------------------------------------|
| `frank-mkt`                  | Persona principal - estrategista marketing senior   |
| `juiz`                       | Arbitrador imparcial entre modos divergentes       |
| `auditor`                    | Varredura mecanica PASS/FAIL contra regras         |
| `investigador`               | Entrevista estruturada com interlocutor (briefing) |
| `perfilador-mercado`         | Sizing TAM/SAM/SOM + persona + concorrencia        |
| `redator-hacker`             | Copy alta conversao (etico - sem dark patterns)    |
| `seo-strategist`             | Keywords + autoridade + arquitetura de conteudo    |
| `social-media-linkedin`      | LinkedIn B2B + employer brand                      |
| `social-media-instagram`     | Instagram - Reels + Stories + Feed                 |
| `social-media-facebook`      | Facebook organico + ads                            |
| `ux-ui-revisor`              | Heuristicas Nielsen + microcopy + acessibilidade   |
| `psicologia-influencia`      | Gatilhos eticos + viesses cognitivos               |
| `frank-corporativo`          | Comunicacao corporativa (atas, releases, internas) |
| `social-humanitario`         | Causas + ESG + terceiro setor                      |
| `atelier-criativo`           | Artista digital generalista - visao estetica + sinestesia + anti-AI-slop |
| `renderer-visual`            | Agente operacional - render-loop SVG/HTML via Bash + headless browser + Read multimodal |

Convocacao tipica: persona principal `frank-mkt` orquestra, agentes especialistas executam, `auditor` valida, `juiz` arbitra divergencias. `atelier-criativo` invocado quando brief tem ambiguidade estetica; `renderer-visual` invocado para fechar loop visual em SVG/HTML gerado (Write -> Bash render -> Read PNG -> avaliar).

---

## 93 Skills (18 BLOCOS COMPLETOS)

### Bloco 1 - SEO Estendido (7 skills)
- `seo-fundamentos` - principios basicos SEO 2026
- `seo-keywords` - pesquisa + clusterizacao + intencao
- `seo-on-page` - title, H1-H6, meta, schema, links internos
- `seo-tecnico` - core web vitals, crawl, indexacao, robots
- `seo-link-building` - autoridade etica + outreach
- `conteudo-evergreen` - artigos perenes + atualizacao
- `seo-ai-otimizacao` - LLM-friendly content + AI Overviews

### Bloco 2 - Midia Social Organica + Ads (10 skills)
- `social-media-fundamentos` - estrategia geral cross-platform
- `linkedin-organico` - posts + carrosseis + thought leadership B2B
- `x-twitter` - threads + tom + viralizacao etica
- `youtube-shorts` - hook + retencao + CTA
- `instagram-feed-reels` - estetica + Reels + carrosseis
- `tiktok-criativo` - trends + audio + nativo
- `facebook-organico` - grupos + comunidade + alcance
- `linkedin-ads` - Sponsored Content + Conversation + Lead Gen
- `instagram-ads` - Stories + Reels Ads + criativos
- `facebook-ads` - CBO + Advantage+ + retargeting

### Bloco 3 - Comunicacao Visual & IA (4 skills)
- `geracao-imagens-ia` - Midjourney, DALLE, SD, Flux, prompts
- `infograficos-diagramas` - hierarquia visual + fluxos
- `composicao-visual` - layout, grid, contraste, hierarquia
- `audio-musica-ia` - Suno, Udio, ElevenLabs, jingles

### Bloco 4 - Multi-Platform & Audiencia (3 skills)
- `github-presence` - README, perfil, awesome-lists, autoridade tecnica
- `multi-platform-narrative` - mesma historia adaptada por canal
- `escrita-por-publico` - tom para CEO vs dev vs juridico vs leigo

### Bloco 5 - Persuasao & Comunidade (2 skills)
- `persuasao-eticas` - principios Cialdini aplicados eticamente
- `engajamento-comunidade` - construir base + UGC + advocacy

### Bloco 6 - MKT Nao-Tradicional (2 skills)
- `guerrilha-criativa` - acoes baixo custo alto impacto
- `newsjacking-real-time` - aproveitar pauta com responsabilidade

### Bloco 7 - MKT & Estrategia 1o lote (5 skills)
- `posicionamento-marca` - point-of-view + categoria + diferenciacao
- `branding` - identidade narrativa + valores + arquetipos
- `funil-jornada` - awareness -> conversao -> retencao
- `big-idea` - conceito unificador da campanha
- `metricas-marketing` - CAC, LTV, ROAS, atribuicao

### Bloco 8 - Dominio Vertical (13 skills)
- `dominio-vertical-fundamentos` - como ganhar fluencia setorial
- `dominio-ti-mkt` - marketing para empresas de TI/SaaS
- `dominio-juridico-mkt` - publicidade adv (OAB compliance)
- `dominio-empreendedorismo-mkt` - founder-led + bootstrap
- `dominio-negocios-mkt` - PMEs + B2B classico
- `dominio-ia-mkt` - mkt para AI startups + posicionamento
- `tecnicas-ia-claude-gemini-mkt` - usar LLMs para mkt produtivo
- `dominio-rh-mkt` - employer branding + recruitment marketing
- `dominio-dp-mkt` - departamento pessoal e mkt interno
- `dominio-financeiro-mkt` - mkt para fintechs + finance B2B
- `dominio-fiscal-mkt` - contabil + tributario + compliance comms
- `dominio-adm-mkt` - administracao + gestao
- `dominio-iot-mkt` - IoT/embarcados + indl 4.0

### Bloco 9 - Documentos Corporativos (2 skills)
- `atas-relatorios-corporativos` - atas, relatorios, MOM
- `comunicacoes-corporativas` - releases, comunicados internos, FAQs

### Bloco 10 - Pesquisa & Inteligencia (6 skills - BLOCO FECHADO)
- `pesquisa-mercado-fundamentos` - desk research + survey + qualitativa
- `persona-icp-deep` - ICP profundo + jobs-to-be-done
- `analise-concorrencia` - SWOT + benchmarking + share of voice
- `white-space-analysis` - territorios nao-ocupados
- `trendwatching` - sinais fracos + tendencias emergentes
- `competitive-intelligence` - inteligencia competitiva continua

### Bloco 11 - Corporativo & Humanitario (6 skills)
- `comunicacao-corporativa` - estrategia institucional integrada
- `employer-branding` - marca empregadora + EVP
- `comunicacao-crise` - playbook + dark site + porta-voz
- `esg-comunicacao` - environment, social, governance reporting
- `terceiro-setor` - ONG + captacao + voluntariado
- `empreendedorismo-impacto` - negocio social + B Corp

### Bloco 12 - Copy & Redacao (4 skills)
- `copywriting-conversao` - frameworks AIDA, PAS, BAB, FAB
- `storytelling` - hero journey + StoryBrand + 3 atos
- `email-marketing` - sequencias, deliverability, segmentacao
- `redacao-publicitaria` - claims, slogans, manifestos

### Bloco 13 - UX/UI (4 skills)
- `ux-heuristicas` - 10 heuristicas Nielsen aplicadas
- `microcopy` - botoes, tooltips, mensagens de erro
- `acessibilidade-wcag` - WCAG 2.2 AA + leis BR
- `design-system-basico` - tokens, componentes, governanca

### Bloco 14 - Psicologia & Influencia (3 skills)
- `gatilhos-eticos` - reciprocidade, autoridade, prova social, etc
- `vies-cognitivo` - ancoragem, framing, loss aversion (uso etico)
- `prova-social-honesta` - depoimentos reais + cases verificaveis

### Bloco 15 - Conhecimento de Plataforma (6 skills high vol)
- `conhecimento-meta-ads` - Meta Ads Manager profundo
- `conhecimento-google-ads` - Google Ads + Performance Max
- `conhecimento-linkedin-ads` - Campaign Manager LinkedIn
- `conhecimento-ga4` - Google Analytics 4 + GTM
- `conhecimento-search-console` - GSC + indexacao + queries
- `conhecimento-conar-cdc` - CONAR + CDC + LGPD aplicados

### Bloco 16 - Meta-skill (1 skill)
- `manutencao-skills` - como criar/atualizar/podar skills do plugin

### Bloco 17 - MKT & Estrategia 2o lote (5 skills)
- `growth-hacking` - experimentation + AARRR + viral loops
- `product-marketing` - PMF + posicionamento + GTM tatico
- `account-based-marketing` - ABM 1:1 / 1:few / 1:many
- `pricing-strategy` - modelos, psicologia, value-based
- `go-to-market-strategy` - GTM end-to-end + checklist lancamento

### Bloco 18 - Skills Avancadas / Experimentais (2 skills)
- `svg-engineering-ia` - gerar SVG via prompt LLM (inovadora)
- `render-loop-svg` - operacionalizacao de feedback visual real (Write SVG -> Bash render -> Read PNG multimodal -> Edit) — resolve output cego em SVG denso (v2.37.0)

### Bloco 19 - Identidade Visual Corporativa / Brand Design (8 skills)
- `logo-design-process` - briefing -> exploracao -> refinamento -> entrega
- `brand-book-methodology` - manual de marca completo
- `paleta-cores-corporativa` - sistema de cor + acessibilidade
- `tipografia-corporativa` - sistema tipografico + pareamento
- `iconografia-corporativa` - icon set coerente + grid
- `templates-corporativos-comerciais` - propostas, decks, fichas
- `apresentacoes-decks-corporativos` - storytelling em slides
- `print-papelaria-collateral` - cartoes, papel timbrado, envelopes

---

## Recortes tematicos (filtros)

### Filtro `seo`
- Skills: `seo-fundamentos`, `seo-keywords`, `seo-on-page`, `seo-tecnico`, `seo-link-building`, `conteudo-evergreen`, `seo-ai-otimizacao`, `conhecimento-search-console`
- Agente: `seo-strategist`
- Comandos: `/frank-mkt:audit`, `/frank-mkt:review`

### Filtro `social`
- Skills: `social-media-fundamentos`, `linkedin-organico`, `instagram-feed-reels`, `tiktok-criativo`, `youtube-shorts`, `x-twitter`, `facebook-organico`, `linkedin-ads`, `instagram-ads`, `facebook-ads`, `engajamento-comunidade`
- Agentes: `social-media-linkedin`, `social-media-instagram`, `social-media-facebook`
- Comandos: `/frank-mkt:perfil`, `/frank-mkt:audit`

### Filtro `branding`
- Skills: `branding`, `posicionamento-marca`, `big-idea`, `logo-design-process`, `brand-book-methodology`, `paleta-cores-corporativa`, `tipografia-corporativa`, `iconografia-corporativa`
- Agente: `frank-mkt` (orquestra)
- Comandos: `/frank-mkt:perfil`, `/frank-mkt:review`

### Filtro `pesquisa`
- Skills: `pesquisa-mercado-fundamentos`, `persona-icp-deep`, `analise-concorrencia`, `white-space-analysis`, `trendwatching`, `competitive-intelligence`
- Agentes: `perfilador-mercado`, `investigador`
- Comando: `/frank-mkt:perfil`

### Filtro `copy`
- Skills: `copywriting-conversao`, `storytelling`, `email-marketing`, `redacao-publicitaria`, `microcopy`, `escrita-por-publico`
- Agente: `redator-hacker`
- Comandos: `/frank-mkt:audit`, `/frank-mkt:review`

### Filtro `ux`
- Skills: `ux-heuristicas`, `microcopy`, `acessibilidade-wcag`, `design-system-basico`
- Agente: `ux-ui-revisor`
- Comando: `/frank-mkt:review`

### Filtro `psicologia`
- Skills: `gatilhos-eticos`, `vies-cognitivo`, `prova-social-honesta`, `persuasao-eticas`
- Agente: `psicologia-influencia`
- Comando: `/frank-mkt:review`

### Filtro `dominio`
- Skills: 13 skills do bloco Dominio Vertical (`dominio-ti-mkt`, `dominio-juridico-mkt`, etc)
- Agente: `frank-mkt`
- Comando: `/frank-mkt:perfil`

### Filtro `ads`
- Skills: `linkedin-ads`, `instagram-ads`, `facebook-ads`, `conhecimento-meta-ads`, `conhecimento-google-ads`, `conhecimento-linkedin-ads`, `conhecimento-ga4`, `pricing-strategy`
- Agentes: `social-media-linkedin`, `social-media-instagram`, `social-media-facebook`, `redator-hacker`
- Comando: `/frank-mkt:audit`

### Filtro `corporativo`
- Skills: `comunicacao-corporativa`, `employer-branding`, `comunicacao-crise`, `esg-comunicacao`, `atas-relatorios-corporativos`, `comunicacoes-corporativas`, `apresentacoes-decks-corporativos`, `templates-corporativos-comerciais`
- Agente: `frank-corporativo`
- Comando: `/frank-mkt:review`

### Filtro `identidade`
- Skills: 8 skills do Bloco 19 (Identidade Visual Corporativa / Brand Design)
- Agente: `atelier-criativo` (visao estetica) + `frank-mkt` (orquestracao)
- Comandos: `/frank-mkt:atelier`, `/frank-mkt:review`

### Filtro `arte`
- Skills: `svg-engineering-ia`, `render-loop-svg`, `logo-design-process`, `brand-book-methodology`, `paleta-cores-corporativa`, `tipografia-corporativa`, `iconografia-corporativa`, `composicao-visual`, `geracao-imagens-ia`, `audio-musica-ia`
- Agentes: `atelier-criativo` (visao) + `renderer-visual` (validacao)
- Comandos: `/frank-mkt:atelier`, `/frank-mkt:gerar-infografico`

### Filtro `infografico`
- Skills: `infograficos-diagramas`, `svg-engineering-ia`, `render-loop-svg`, `composicao-visual`, `paleta-cores-corporativa`, `tipografia-corporativa`
- Agentes: `atelier-criativo` (visao) + `renderer-visual` (validacao operacional)
- Comando: `/frank-mkt:gerar-infografico` (workflow end-to-end com render-loop obrigatorio)

### Filtro `sinestesia`
- Skills: `audio-musica-ia`, `geracao-imagens-ia`, `composicao-visual`, `svg-engineering-ia`, `storytelling`, `big-idea`
- Agente: `atelier-criativo` (laboratorio sinestesia cross-domain)
- Comando: `/frank-mkt:atelier "<brief>" sinestesia`

### Filtro `ia`
- Skills: `dominio-ia-mkt`, `tecnicas-ia-claude-gemini-mkt`, `geracao-imagens-ia`, `audio-musica-ia`, `svg-engineering-ia`, `seo-ai-otimizacao`
- Agente: `frank-mkt`
- Comando: `/frank-mkt:review`

### Filtro `persuasao`
- Skills: `persuasao-eticas`, `gatilhos-eticos`, `vies-cognitivo`, `prova-social-honesta`, `copywriting-conversao`, `storytelling`
- Agentes: `psicologia-influencia`, `redator-hacker`
- Comando: `/frank-mkt:audit`

### Filtro `guerrilha`
- Skills: `guerrilha-criativa`, `newsjacking-real-time`, `engajamento-comunidade`
- Agente: `frank-mkt`
- Comando: `/frank-mkt:review`

### Filtro `estrategia`
- Skills: `posicionamento-marca`, `branding`, `funil-jornada`, `big-idea`, `metricas-marketing`, `growth-hacking`, `product-marketing`, `account-based-marketing`, `pricing-strategy`, `go-to-market-strategy`
- Agentes: `frank-mkt`, `perfilador-mercado`
- Comandos: `/frank-mkt:perfil`, `/frank-mkt:review`

---

## Cross-references (ordem tipica de uso)

### Lancamento de produto/marca novo
```
/frank-mkt:init
  -> /frank-mkt:perfil (perfilador-mercado + investigador)
  -> pesquisa-mercado-fundamentos + persona-icp-deep + analise-concorrencia
  -> white-space-analysis + trendwatching
  -> posicionamento-marca + branding + big-idea
  -> logo-design-process + brand-book-methodology
  -> go-to-market-strategy + pricing-strategy
  -> funil-jornada + metricas-marketing
  -> [execucao por canal]
  -> /frank-mkt:audit + /frank-mkt:review
  -> /frank-mkt:save-session
```

### Campanha de conteudo organico
```
/frank-mkt:perfil
  -> seo-keywords + seo-fundamentos
  -> conteudo-evergreen + storytelling
  -> seo-on-page + seo-ai-otimizacao
  -> multi-platform-narrative + escrita-por-publico
  -> linkedin-organico / instagram-feed-reels / etc
  -> engajamento-comunidade
  -> /frank-mkt:audit
```

### Campanha paga (Ads)
```
/frank-mkt:perfil
  -> persona-icp-deep
  -> copywriting-conversao + redacao-publicitaria
  -> conhecimento-meta-ads OU conhecimento-google-ads OU conhecimento-linkedin-ads
  -> facebook-ads / instagram-ads / linkedin-ads
  -> conhecimento-ga4 + metricas-marketing
  -> /frank-mkt:audit + /frank-mkt:review
```

### Comunicacao corporativa / crise
```
/frank-mkt:init
  -> comunicacao-corporativa + comunicacao-crise
  -> atas-relatorios-corporativos + comunicacoes-corporativas
  -> employer-branding (se interno)
  -> esg-comunicacao (se sustentabilidade)
  -> /frank-mkt:review (frank-corporativo)
```

### Identidade visual / brand design
```
/frank-mkt:perfil
  -> branding + posicionamento-marca
  -> logo-design-process
  -> paleta-cores-corporativa + tipografia-corporativa + iconografia-corporativa
  -> brand-book-methodology
  -> templates-corporativos-comerciais + print-papelaria-collateral
  -> apresentacoes-decks-corporativos
  -> /frank-mkt:review
```

### Resolucao de divergencia
```
[debate entre dois agentes] -> /frank-mkt:juiz -> parecer imparcial
```

---

## Disclaimer educacional

Este catalogo e meio de referencia, nao prescricao. As skills, agentes e comandos sao ferramentas - o trabalho de marketing requer julgamento humano sobre contexto, etica e estrategia. O plugin frank-mkt apoia a decisao mas nao substitui:

- Briefing real do cliente
- Pesquisa primaria com usuarios reais
- Auditoria juridica em comunicacao regulada (saude, financeiro, juridico, infantil)
- Compliance LGPD / CDC / CONAR / OAB / CFC conforme setor
- Decisao executiva de orcamento, posicionamento e risco

Sempre que a skill citar "use eticamente", isso e um pre-requisito, nao um adendo. Frank-mkt rejeita dark patterns, manipulacao de viesses contra o interlocutor e claims sem prova.

---

## Resposta esperada

Devolver ao usuario o(s) bloco(s) selecionado(s) por $ARGUMENTS + secao "Cross-references" + disclaimer compacto. Sem inventar skills/agentes/comandos que nao estao listados aqui. Se $ARGUMENTS nao bater com nenhum filtro conhecido, mostrar visao geral + lista de filtros validos.
