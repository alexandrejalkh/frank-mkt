---
description: Convoca Perfilador de Mercado — sizing TAM/SAM/SOM + persona ICP + concorrencia + white-space + tendencias
argument-hint: <segmento> [foco] (ex: "FoodTech B2B Brasil" "TAM")
allowed-tools: Read, Write, WebSearch, Glob
---

# /frank-mkt:perfil

Convoca o **agente Perfilador de Mercado** para realizar analise estruturada de mercado em 5 frentes integradas: sizing TAM/SAM/SOM, persona ICP, analise de concorrencia, white-space e tendencias. Output salvo em `.frank-mkt/pesquisa/<segmento>-<data>.md`.

ASCII PT-BR sem acentos (compatibilidade com Windows/encoding).

Disclaimer: Este comando produz analise estruturada com base em pesquisa publica + frameworks. Numeros TAM/SAM/SOM sao estimativas triangulares para apoio a decisao estrategica. NAO substitui due-diligence formal, parecer juridico-tributario, ou estudo contratado de consultoria de mercado. Uso educacional e de planejamento.

---

## O que faz

Invoca o agente **perfilador-mercado** (`agents/perfilador-mercado.md`) para analise estruturada de mercado em 5 frentes:

### 1. Sizing (cross-skill: pesquisa-mercado-fundamentos)

- **TAM** (Total Addressable Market) — universo total se 100% dos compradores comprassem o produto
- **SAM** (Serviceable Addressable Market) — fatia atingivel pelo modelo de negocio (geografia + segmento + canal)
- **SOM** (Serviceable Obtainable Market) — fatia realisticamente capturavel em horizonte 3-5 anos
- **Top-down** — partir de relatorios setoriais (IBGE, Statista, Gartner, ABRAS, ABF, etc.) e segmentar
- **Bottom-up** — partir de unidade economica (ticket medio x clientes potenciais)
- **Triangulacao** — comparar top-down vs bottom-up, divergencia >30% acende alerta
- **Brasil specificity** — tropicalizar dados globais (Brasil != USA != Europa); inflacao, cambio, sazonalidade local

### 2. Persona ICP (cross-skill: persona-icp-deep)

- **Demographics** (B2C) — idade, renda, geografia, escolaridade, ocupacao
- **Firmographics** (B2B) — tamanho empresa, faturamento, vertical, geografia, maturidade digital
- **Psychographics** — valores, motivacoes, aspiracoes, medos
- **Jobs-to-be-Done (JTBD framework)** — funcional + social + emocional
- **Pain points** — dores atuais nao resolvidas
- **Gain points** — beneficios desejados (alem de "resolver dor")
- **Buyer journey** — awareness > consideration > decision > retention > advocacy
- **Buying committee** (B2B) — Forrester 2024 aponta media 22 stakeholders em deal enterprise; mapear champion + economic buyer + influenciadores + bloqueadores

### 3. Analise concorrencia (cross-skill: analise-concorrencia)

- **Direct competitors** — mesmo problema + mesmo target + mesma solucao
- **Indirect competitors** — mesmo problema, solucao diferente
- **Substitutes** — alternativa precaria (planilha Excel, "fazer manual", "nao fazer")
- **Porter 5 Forces** — rivalidade + poder comprador + poder fornecedor + ameaca novos entrantes + ameaca substitutos
- **SWOT** — strengths/weaknesses/opportunities/threats vs cada concorrente principal
- **Magic Quadrant / G2 / Capterra / Gartner** — benchmarks publicos quando disponivel
- **Brasil specifics** — concorrentes nacionais (geralmente menores mas com vantagem de tropicalizacao) + globais (geralmente maiores mas com gap de localizacao)

### 4. White-space analysis (cross-skill: white-space-analysis)

- **Underserved segments** — segmentos com demanda mas oferta insuficiente
- **Unmet needs (JTBD gap)** — jobs nao atendidos pelos players atuais
- **Geographic white-space** — regioes sub-atendidas (no Brasil: tipicamente Norte/Nordeste/Centro-Oeste)
- **Pricing white-space** — gaps entre tiers (ex: nada entre SMB R$500/mes e Enterprise R$10k/mes)
- **Vertical white-space** — sub-verticais sem solucao especializada
- **Disruption potential** — incumbentes vulneraveis (Christensen Innovator's Dilemma)

### 5. Trendwatching (cross-skill: trendwatching)

- **Macro trends (PEST/STEEP)** — Politico, Economico, Social, Tecnologico, Ambiental, Etico-legal
- **Micro trends** — segment-specific (delivery on-demand, ESG B2B, embedded finance, etc.)
- **Weak signals** — early indicators (Amy Webb futures framework) — pequenos sinais que podem virar onda
- **Trend amplifiers Brasil** — reforma tributaria 2026, Open Finance, Pix, LGPD enforcement, ESG SBT mandatory
- **Trend sources referencias** — WGSN, Trend Hunter, Mintel, Pinterest Predicts, Google Trends, Statista (quando aplicavel)

---

## Argumentos

`$ARGUMENTS` = `<segmento> [foco]`

- **segmento** (obrigatorio) — nicho/mercado a perfilar (ex: "FoodTech B2B Brasil", "SaaS legal mid-market", "Cosmetic clean beauty Brasil")
- **foco** (opcional) — uma das opcoes:
  - `TAM` — focar sizing (skip persona/concorrencia/white-space/trends superficiais)
  - `persona` — focar ICP deep (skip sizing detalhado)
  - `concorrentes` — focar mapeamento competitivo
  - `white-space` — focar gaps e oportunidades
  - `trends` — focar tendencias e weak signals
  - `full` (default) — todas as 5 frentes balanceadas

Exemplos:

- `/frank-mkt:perfil "FoodTech B2B Brasil"` → analise full
- `/frank-mkt:perfil "FoodTech B2B Brasil" "TAM"` → foco sizing
- `/frank-mkt:perfil "SaaS juridico mid-market" "persona"` → foco ICP deep
- `/frank-mkt:perfil "Cosmeticos clean beauty Brasil" "white-space"` → foco gaps
- `/frank-mkt:perfil "EdTech corporativo" "trends"` → foco tendencias

---

## Workflow do comando

### Passo 1 — Capturar entrada

- Parsear `$ARGUMENTS` em segmento + foco
- Se segmento vazio: pedir input ao usuario (segmento e obrigatorio)
- Se foco vazio: assumir `full`
- Validar foco contra lista permitida (TAM/persona/concorrentes/white-space/trends/full)

### Passo 2 — Garantir estrutura

```bash
mkdir -p .frank-mkt/pesquisa
```

### Passo 3 — Web search paralelo (3-6 queries)

Disparar pesquisas em paralelo conforme foco:

**full / TAM:**
- `<segmento> market size Brasil 2026`
- `<segmento> TAM SAM SOM Brasil`
- `<segmento> setor relatorio IBGE OR Statista`

**full / persona:**
- `<segmento> buyer persona ICP Brasil`
- `<segmento> jobs to be done framework`

**full / concorrentes:**
- `<segmento> principais concorrentes Brasil`
- `<segmento> G2 Capterra Gartner magic quadrant`

**full / white-space:**
- `<segmento> underserved segments Brasil`
- `<segmento> unmet needs market gap`

**full / trends:**
- `<segmento> trends 2026 Brasil`
- `<segmento> tendencias macro micro PEST`

### Passo 4 — Triangular dados + identificar gaps

- Cruzar dados de >=2 fontes para cada numero
- Marcar com `[fonte: X, ano: Y]` cada estimativa
- Se divergencia top-down vs bottom-up >30%: documentar como "alerta de incerteza"
- Se fonte unica: marcar como "estimativa baixa-confianca"

### Passo 5 — Estruturar output 5 frentes

Aplicar template abaixo. Preencher conforme foco:
- `full`: todas as 5 secoes
- `TAM`: secao SIZING extensa + outras resumidas em 3-5 linhas
- `persona`: secao PERSONA extensa + outras resumidas
- (analogo para concorrentes/white-space/trends)

### Passo 6 — Salvar arquivo

Path: `.frank-mkt/pesquisa/<segmento-slug>-<YYYY-MM-DD>.md`

Slug: lowercase + hifens + sem acentos + max 50 chars.

Se ja existe arquivo com mesmo nome (mesmo dia): sufixo `-v2`, `-v3`, etc.

### Passo 7 — Reportar resumo

No chat: imprimir resumo executivo + path do arquivo salvo + proximos passos sugeridos.

---

## Output formato (template)

```
=== FRANK-MKT PERFILADOR DE MERCADO ===
Segmento: <segmento>
Foco: <TAM | persona | concorrentes | white-space | trends | full>
Data: YYYY-MM-DD

[SIZING]
TAM Brasil 2026: R$ X bi
  Top-down: <metodologia + fontes>
  Bottom-up: <metodologia + fontes>
  Triangulacao: <converge / diverge X%>
SAM (<segmento serviceable>): R$ Y bi
  Filtro: <geografia + porte + canal>
SOM (3 anos atingivel): R$ Z mi
  Premissa: <market share alvo + ramp curve>
Sources: [...]

[PERSONA ICP]
Buyer principal: <titulo + segmento>
Demographics/Firmographics: <perfil>
JTBD funcional: <job pratico>
JTBD social: <imagem perante outros>
JTBD emocional: <sentimento desejado>
Pain points: <3-5 dores principais>
Gain points: <3-5 ganhos desejados>
Buyer journey: <awareness/consideration/decision/retention/advocacy>
Buying committee (B2B): <champion + economic buyer + influenciadores + bloqueadores>

[CONCORRENCIA]
Direct (3-5):
- Concorrente A — <ARR/share/posicionamento>
- Concorrente B — <ARR/share/posicionamento>
- Concorrente C — <ARR/share/posicionamento>

Indirect: <2-3 players adjacentes>
Substitutes: <alternativas precarias>

Porter 5 Forces:
- Rivalry: <ALTA/MEDIA/BAIXA + justificativa>
- Buyer power: <ALTA/MEDIA/BAIXA + justificativa>
- Supplier power: <ALTA/MEDIA/BAIXA + justificativa>
- Threat new entrants: <ALTA/MEDIA/BAIXA + justificativa>
- Substitutes: <ALTA/MEDIA/BAIXA + justificativa>

SWOT vs lider de mercado:
- S: <forca propria>
- W: <fraqueza propria>
- O: <oportunidade externa>
- T: <ameaca externa>

[WHITE-SPACE]
- Geografico: <regiao subatendida>
- Pricing: <gap de tier>
- Feature: <funcionalidade missing across competitors>
- Vertical: <sub-segmento subatendido>
- Disruption potential: <incumbente vulneravel + razao>

[TRENDS Brasil 2026+]
Macro (PEST/STEEP):
- <Politico/Economico/Social/Tecnologico/Ambiental/Etico-legal>
- <ex: Reforma tributaria 2026 mexe com inventory accounting>

Micro (segment-specific):
- <ex: ESG food waste reporting mandatory enterprises 2027>
- <ex: IA generativa demand forecasting popularizando>

Weak signals (Amy Webb framework):
- <pequeno sinal que pode virar onda>
- <ex: Restaurantes ghost-kitchens consolidando — B2B oportunidade>

Trend amplifiers Brasil:
- <ex: Pix B2B mid-market finance integration>
- <ex: Open Finance habilitando dados financeiros real-time>

[RECOMENDACOES estrategicas]
1. <recomendacao + justificativa baseada em evidencia>
2. <recomendacao + justificativa baseada em evidencia>
3. <recomendacao + justificativa baseada em evidencia>
4. <recomendacao + justificativa baseada em evidencia>
5. <recomendacao + justificativa baseada em evidencia>

[CONFIANCA / LIMITACOES]
- Numeros TAM/SAM/SOM: confianca <ALTA/MEDIA/BAIXA> (fontes: <N>)
- Persona ICP: confianca <ALTA/MEDIA/BAIXA> (sample: <publica/cliente/inferencia>)
- Concorrencia: confianca <ALTA/MEDIA/BAIXA> (data freshness: <data>)
- Trends: confianca <ALTA/MEDIA/BAIXA> (consenso vs contrarian)

[Proximos passos]
- /frank-mkt:save-session salvar analise
- skill `branding` para foundation
- skill `posicionamento-marca` para POV
- skill `big-idea` para nucleo criativo
- skill `go-to-market-strategy` para GTM motion
```

---

## Exemplo de chamada (segmento FoodTech B2B Brasil)

```
=== FRANK-MKT PERFILADOR DE MERCADO ===
Segmento: FoodTech B2B Brasil
Foco: full
Data: 2026-05-09

[SIZING]
TAM Brasil 2026: R$ 18 bi
  Top-down: ABRASEL faturamento food service R$ 350bi x 5% software penetracao
  Bottom-up: 1.2M estabelecimentos x R$ 15k ARR medio = R$ 18bi
  Triangulacao: converge (~5% diferenca)
SAM (mid-market 50-500 unidades): R$ 4 bi
  Filtro: redes nacionais + regionais + geografia SP/RJ/MG/RS/PR
SOM (3 anos atingivel): R$ 120 mi
  Premissa: 3% share mid-market em 36 meses
Sources: ABRASEL 2025, IBGE PIA 2024, Distrito FoodTech Report 2025

[PERSONA ICP]
Buyer principal: COO/Operations Manager rede restaurantes 50-500 unidades
Firmographics: faturamento R$ 50M-500M, MRR food, 3-15 anos mercado, SP/RJ/MG eixo
JTBD funcional: reduzir food waste + otimizar inventory
JTBD social: provar competencia operacional para CEO
JTBD emocional: confianca em decisoes data-driven
Pain points: planilhas Excel manuais + falta visibilidade tempo-real + integracoes ERP frageis
Gain points: dashboards BI + automacao + previsoes IA + WhatsApp Business native
Buyer journey: awareness LinkedIn/eventos > consideration RFP > decision pilot 90 dias
Buying committee: Champion COO + Economic CFO + Influencer CIO + Bloqueador Compras

[CONCORRENCIA]
Direct (3):
- Concorrente A — R$ 50M ARR Brasil, dominante TI grandes redes
- Concorrente B — R$ 20M ARR, foco delivery
- Concorrente C — R$ 8M ARR, mid-market

Indirect: SAP + Oracle (enterprise, overshoot mid-market)
Substitutes: planilhas Excel + ERP generico (Bling, Tiny, Omie)

Porter:
- Rivalry: ALTA (3 players ativos)
- Buyer power: MEDIA (mid-market disperso)
- Supplier power: BAIXA (cloud commoditizado AWS/GCP)
- Threat new entrants: ALTA (PLG facil + IA reduz CAC dev)
- Substitutes: BAIXA (ERP generico fail em food specifics)

SWOT vs lider A:
- S: tropicalizacao Pix nativo + WhatsApp
- W: marca menor + sales team enxuto
- O: gap mid-market 50-500 unidades
- T: lider A pode lancar SKU mid-market

[WHITE-SPACE]
- Geografico: Norte/Nordeste underserved (lider A foca SP/RJ)
- Pricing: nada entre R$ 500/mes (small) e R$ 8k/mes (enterprise) — gap mid-market
- Feature: integracao WhatsApp Business + Pix native missing across competitors
- Vertical: cafeterias 100-500 unidades subsegmentado
- Disruption: lider A locked-in legacy stack — IA-first new entrant pode disruptar

[TRENDS Brasil 2026]
Macro (PEST/STEEP):
- Inflacao alimentos pressionando margens (oportunidade automacao)
- Open Finance Brasil + Pix mid-market finance integration
- ESG mandatory food waste reporting enterprises 2027 (LGPD-style enforcement)

Micro:
- ESG food waste reporting mandatory enterprises 2027 (oportunidade compliance)
- IA generativa demand forecasting popularizando
- Reforma tributaria 2026 mexe com inventory accounting

Weak signals:
- Restaurantes ghost-kitchens consolidando (B2B oportunidade)
- Cooperativas regionais food service crescendo
- WhatsApp Business como ERP-light em SMB

[RECOMENDACOES estrategicas]
1. Foco mid-market 50-500 unidades (white-space pricing)
2. Diferencial: WhatsApp Business + Pix native
3. Geografia inicial: Sao Paulo + Rio (concentrar demanda)
4. Expansao Norte/Nordeste fase 2 (pos Series A)
5. ESG compliance reporting feature 2027 antecipar

[CONFIANCA / LIMITACOES]
- TAM/SAM/SOM: confianca MEDIA (3 fontes triangulando)
- Persona ICP: confianca MEDIA (inferencia + benchmarks publicos)
- Concorrencia: confianca ALTA (dados Distrito + LinkedIn 2025)
- Trends: confianca MEDIA-ALTA (consenso amplo)

[Proximos passos]
- /frank-mkt:save-session salvar analise
- branding skill para foundation
- posicionamento-marca para POV vs lider A
- big-idea para nucleo criativo
- go-to-market-strategy para GTM motion mid-market
```

---

## Cross-skill bridge

5 skills core do plugin frank-mkt acionadas:

| Skill | Onde aciona | Output que produz |
|-------|-------------|-------------------|
| `pesquisa-mercado-fundamentos` | Secao SIZING | TAM/SAM/SOM triangulados |
| `persona-icp-deep` | Secao PERSONA ICP | Persona + JTBD + buying committee |
| `analise-concorrencia` | Secao CONCORRENCIA | Direct/Indirect/Substitutes + Porter + SWOT |
| `white-space-analysis` | Secao WHITE-SPACE | Gaps geografico/pricing/feature/vertical |
| `trendwatching` | Secao TRENDS | Macro/Micro/Weak signals + amplifiers Brasil |

Skills auxiliares (referenciar quando relevante):
- `branding` — usar perfil como foundation para brand strategy
- `posicionamento-marca` — usar concorrencia + white-space para POV
- `big-idea` — usar JTBD emocional + insights persona
- `go-to-market-strategy` — usar SOM + buyer journey para motion
- `pricing-strategy` — usar pricing white-space para tier design

---

## Brasil specificity (sempre considerar)

Toda analise deve tropicalizar dados:

- **Geografia** — Brasil != USA != Europa. Mapear concentracao SP/RJ/MG vs interior vs Norte/Nordeste
- **Cambio** — converter dados USD para BRL na cotacao da data + mencionar volatilidade cambial
- **Inflacao** — IPCA acumulado relevante para sizing (R$ 1bi 2020 != R$ 1bi 2026)
- **Tributacao** — reforma tributaria 2026/2027 muda projecoes de tickets e margens
- **Pix + Open Finance** — diferencial competitivo em fintech/embedded finance
- **WhatsApp Business** — canal dominante Brasil B2B SMB+Mid (>90% penetracao)
- **LGPD enforcement** — barreira de entrada + custo compliance
- **ESG SBT mandatory** — empresas listadas + grandes corp. obrigadas reportar (oportunidade B2B compliance)
- **Reforma tributaria 2026** — IBS/CBS/IS muda inventory accounting + cross-border (oportunidade tax-tech)

---

## Disclaimer educacional

Este comando produz analise estruturada com base em pesquisa publica + frameworks academicos (Porter, Christensen, Forrester, Amy Webb, JTBD, etc.). Numeros TAM/SAM/SOM sao **estimativas triangulares** para apoio a decisao estrategica. **NAO substitui**:

- Due-diligence formal de investimento (M&A, VC, PE)
- Parecer juridico-tributario de operacao especifica
- Estudo contratado de consultoria de mercado (Gartner, Forrester, McKinsey, BCG, Bain, EY-Parthenon)
- Validacao primaria com clientes reais (entrevistas, surveys, pilots)

Uso: planejamento estrategico, pitch deck early-stage, alinhamento interno, hipotese para validacao primaria.

Confianca dos numeros: sempre marcar ALTA/MEDIA/BAIXA + fontes na secao `[CONFIANCA / LIMITACOES]`.

---

## Quando usar este comando

Use `/frank-mkt:perfil` quando:

- Inicio de projeto/cliente novo — entender mercado antes de qualquer entregavel
- Pitch deck Series A/B — slide market opportunity precisa de TAM/SAM/SOM rigoroso
- Lancamento de produto novo — validar white-space + persona antes de spec
- Analise concorrencial trimestral — atualizar mapa competitivo
- Trend report anual — atualizar weak signals + macro trends
- Briefing para skill `branding` ou `posicionamento-marca` — perfil e input

NAO usar para:
- Microdecisao tatica (use skill especifica direto)
- Copy ou criativo (use `big-idea`, `copy-writing`)
- Operacional (use `go-to-market-strategy`, `pricing-strategy`)

---

## Referencias frameworks aplicados

- **Porter 5 Forces** — Michael Porter, "Competitive Strategy" (1980)
- **JTBD** — Clayton Christensen, "Competing Against Luck" (2016)
- **Innovator's Dilemma** — Clayton Christensen (1997)
- **PEST/STEEP** — analise macro-ambiente classica (escola SWOT)
- **Buying committee 22 stakeholders** — Forrester B2B Buying Study 2024
- **Weak signals / futures framework** — Amy Webb, "The Signals Are Talking" (2016)
- **TAM/SAM/SOM** — Steve Blank, "The Four Steps to the Epiphany" (2005)
- **Magic Quadrant** — Gartner methodology
- **G2 / Capterra** — peer review B2B SaaS

---

## FIM /frank-mkt:perfil
