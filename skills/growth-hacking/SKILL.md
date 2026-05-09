---
name: growth-hacking
description: Growth Hacking + Growth Marketing 2026 (AARRR Pirate Metrics McClure 2007 + viral loops K-factor + ICE/RICE prioritization + Sean Ellis PMF survey 40% + growth experiments velocity + Reforge Brian Balfour 4-fits + Andrew Chen Cold Start Problem) para founders/CMO/PM/growth marketers/agencias, com cobertura AARRR Acquisition/Activation/Retention/Revenue/Referral + viral coefficient K>1 = self-sustaining + experiment cadence weekly + Brasil cases Nubank/iFood/Magalu/Mercado Livre. 2a SKILL Bloco Marketing & Estrategia 2o lote.
volatility: medium
last_review: 2026-05-09
next_review: 2026-11-09
languages: [pt-BR]
audience: [founders, CMO, PM, growth-marketers, agencias, performance-marketers]
ascii_only: true
---

# Skill: growth-hacking

Growth Hacking + Growth Marketing 2026 — disciplina sistematica de crescimento orientada por dados, experimentacao rapida e alavancas de produto/marketing/engenharia. Esta SKILL consolida 8 fundacoes (AARRR Pirate Metrics + PMF Sean Ellis + viral loops K-factor + experiments cadence + Reforge 4-Fits + Brasil cases + mensuracao + aplicacao MKT) com 18 anti-patterns + 18 regras de ouro + 4 personas + 50-70 referencias hyperlinks.

## Decaimento Temporal

- **Volatilidade**: medium — fundacoes (AARRR, PMF survey, K-factor) sao estaveis ha 15+ anos; tooling (Mixpanel, Amplitude, GrowthBook) e tactics (canais quentes) mudam trimestralmente.
- **Last review**: 2026-05-09
- **Next review**: 2026-11-09 (6 meses).
- **Triggers de re-review antecipado**:
  - Novo framework Reforge/Lenny/Andrew Chen com mais de 100k views.
  - Algoritmo de canal-chave (TikTok/Meta/Google) muda regras de attribution.
  - LGPD/cookies third-party deprecation no Brasil afeta tracking.
  - Caso Brasil de viral loop com K>1 documentado publicamente.
  - Mudanca em iOS ATT/Android Privacy Sandbox quebra MMM.
- **O que NAO decai**: AARRR (5 estagios), PMF 40% rule, K = i x c (formula), 4-Fits (market-product/product-channel/channel-model/model-market), ICE = Impact x Confidence x Ease.
- **O que decai rapido (< 6 meses)**: benchmarks por canal (CAC/LTV), tools recomendadas, algoritmos de attribution, tactics especificas (TikTok Shop, Reels, etc).

## Visao Geral

Growth Hacking foi cunhado por Sean Ellis em 2010 para descrever profissionais focados unicamente em crescimento, combinando marketing + produto + engenharia + dados. Em 2026 evoluiu para "Growth Marketing" como disciplina madura, com foco em:

1. **Sistemas, nao tacticas** — frameworks repetiveis (AARRR, 4-Fits) > hacks pontuais.
2. **Experimentos > opinioes** — cadencia semanal de testes A/B com hipoteses formais.
3. **Produto e canal sao inseparaveis** — Product-Channel Fit (Reforge) e nao-negociavel.
4. **Retencao precede aquisicao** — sem retencao, viralidade nao se sustenta (Andrew Chen).
5. **PMF antes de growth** — 40% Sean Ellis Test e gate antes de escalar gastos.

Pilares centrais (que esta SKILL cobre):

| Pilar | Foco | Owner tipico |
|-------|------|-------------|
| **AARRR (McClure 2007)** | 5 estagios: Acquisition, Activation, Retention, Revenue, Referral | Growth lead |
| **PMF (Sean Ellis)** | 40% survey + Quick Ratio | Founder/CEO |
| **Viral Loops (Chen)** | K-factor, cycle time, network effects | PM growth |
| **Experiments** | ICE/RICE, hypothesis-driven, weekly cadence | Growth team |
| **4-Fits (Balfour)** | Market-Product / Product-Channel / Channel-Model / Model-Market | CMO/CPO |
| **Brasil cases** | Nubank, iFood, Magalu, Mercado Livre | Growth Brasil |
| **Mensuracao** | Mixpanel, Amplitude, GA4, GrowthBook | Data + Growth |
| **Aplicacao MKT** | 5 audiencias (founders, CMO, PM, growth, agencias) | Todos |

Esta SKILL serve **founders pre-PMF**, **CMOs scaling growth**, **PMs growth-focused**, **growth marketers performance**, **agencias**.

## Fundacao 1 — AARRR Pirate Metrics McClure 2007

**Origem**. Dave McClure (entao 500 Startups, ex-PayPal) apresentou "Startup Metrics for Pirates: AARRR!" no Ignite Seattle em agosto de 2007 — palestra de 5 minutos que se tornou framework canonico de growth ([andrewchen.com](https://andrewchen.com), [500.co](https://500.co)).

**Os 5 estagios** (acronimo AARRR — "pirate" porque soa como "aaarrr"):

### 1. Acquisition (Aquisicao)

- **Pergunta**: De onde vem o usuario?
- **Metricas**: visitantes, signups, CAC (Customer Acquisition Cost), CAC payback period.
- **Canais 2026**: SEO/content, paid (Meta/Google/TikTok), referral, partnerships, PR, communities, podcasts, influencer, ABM.
- **Benchmark SaaS B2B**: CAC payback < 12 meses (mediana), < 6 meses (top quartil) — fonte SaaS Capital, OpenView.
- **Anti-pattern**: gastar em aquisicao antes de ter PMF (queima caixa em funil furado).

### 2. Activation (Ativacao)

- **Pergunta**: Usuario teve "first value moment" / "aha moment"?
- **Metricas**: % users que completam onboarding, time-to-value (TTV), activation rate.
- **Exemplos historicos**:
  - Facebook: "7 amigos em 10 dias" (correlacao forte com retencao).
  - Slack: "2.000 mensagens enviadas pelo time" (Bain analysis).
  - Dropbox: "1 arquivo salvo em 1 dispositivo" + "compartilhado com 1 pessoa".
- **Benchmark**: 20-40% activation em SaaS B2B self-serve (Mixpanel benchmarks).
- **Anti-pattern**: definir ativacao como "criou conta" (signup != activation).

### 3. Retention (Retencao)

- **Pergunta**: Usuario volta?
- **Metricas**: D1/D7/D30 retention, weekly/monthly active users (WAU/MAU), churn rate, cohort curves.
- **Curvas**:
  - **Smile curve** (sobe apos cair) — sinal de PMF forte (Sequoia).
  - **Flat curve** — usuarios voltam consistentemente (excelente).
  - **Curva de morte** (cai e nao volta) — sem PMF.
- **Benchmark consumer apps**: D30 retention 5-15% e mediano (Andrew Chen).
- **Benchmark SaaS B2B**: net revenue retention (NRR) > 110% e top quartil (Bessemer).
- **Anti-pattern**: focar em DAU sem olhar cohorts (vanity metric esconde churn).

### 4. Revenue (Receita)

- **Pergunta**: Usuario paga?
- **Metricas**: ARPU (Average Revenue Per User), LTV (Lifetime Value), MRR/ARR, conversion free-to-paid, expansion revenue.
- **Modelos**: subscription (SaaS), transactional (marketplace), ads (consumer), freemium-to-paid.
- **LTV:CAC ratio**: > 3:1 e saudavel (David Skok), > 5:1 e excelente.
- **Anti-pattern**: focar em MRR sem olhar CAC payback (crescimento que queima caixa).

### 5. Referral (Indicacao)

- **Pergunta**: Usuario traz outros usuarios?
- **Metricas**: K-factor (viral coefficient), Net Promoter Score (NPS), % users que indicam.
- **K-factor formula**: K = i x c (i = invites por usuario, c = conversion rate).
- **K > 1**: crescimento viral self-sustaining.
- **K < 1 mas > 0**: amplificacao (aquisicao paga gera mais usuarios via referral).
- **Cases**: Dropbox (2x storage por referral, K~0.6 + viral cycle 2 dias), PayPal (US$10 + US$10 inicial).
- **Anti-pattern**: programa de referral antes de ter retencao (usuarios que nao voltam nao indicam).

**Variante AAARRR** (com Awareness inicial): adiciona "Awareness" antes de Acquisition (top of funnel) — usado em CPG e brands com longo ciclo de consideracao ([userguiding.com](https://userguiding.com), [growwithward.com](https://growwithward.com)).

**Como aplicar (workflow)**:

1. **Mapear funnel** AARRR para seu produto especifico.
2. **Instrumentar** cada estagio (eventos em Mixpanel/Amplitude).
3. **Identificar gargalo** (estagio com pior conversao vs benchmark).
4. **Priorizar experimentos** no gargalo (ICE score).
5. **Iterar semanalmente** com hypothesis-driven experiments.

## Fundacao 2 — PMF Sean Ellis 40% Survey + ICE/RICE Prioritization

### Sean Ellis 40% Test

**Pergunta unica**: "How would you feel if you could no longer use [product]?"
- Very disappointed
- Somewhat disappointed
- Not disappointed
- N/A (no longer use)

**Threshold**: se >= 40% dos usuarios ativos respondem "very disappointed", o produto tem PMF ([pmfsurvey.com](https://pmfsurvey.com), [Sean Ellis Hacking Growth book](https://www.lennysnewsletter.com/p/the-original-growth-hacker-sean-ellis)).

**Origem**: Sean Ellis analisou 100+ startups (Dropbox, LogMeIn, Eventbrite) e identificou 40% como threshold empirico.

**Cases publicos**:
- **Slack**: > 50% very disappointed (PMF forte).
- **Superhuman**: 22% inicial -> 58% apos segmentacao por power users (Rahul Vohra "How Superhuman Built an Engine to Find Product/Market Fit").
- **Dropbox**: 47% inicial.

**2026 best practices**:
- **Quarterly testing** — PMF nao e estatico, decai com competicao/expansao.
- **Segmentacao** — testar por persona, plano, geografia (PMF varia por segmento).
- **Combinar com Quick Ratio** > 4 (new + expansion / churn + contraction MRR).
- **Combinar com retention curves** (smile curve confirma).
- **Sample size** >= 100 respostas para significancia.

**Anti-pattern**: rodar survey 1 vez e considerar resolvido (PMF e medicao continua).

### ICE Score (Sean Ellis)

**Formula**: ICE = Impact x Confidence x Ease (cada fator 1-10).

| Fator | Pergunta | Escala 1-10 |
|-------|----------|------------|
| **Impact** | Quanto move a metrica-alvo? | 1=marginal / 10=transformacional |
| **Confidence** | Quao seguro estou que vai funcionar? | 1=palpite / 10=evidencia forte |
| **Ease** | Quao rapido/barato e implementar? | 1=meses / 10=horas |

**Score range**: 1 a 1000.

**Uso**: priorizar 20-50 ideias semanalmente. Score > 200 e candidato forte; > 500 e prioridade.

**Limitacao**: nao considera Reach (publico afetado).

### RICE Score (Intercom)

**Formula**: RICE = (Reach x Impact x Confidence) / Effort.

| Fator | Definicao | Unidade |
|-------|-----------|---------|
| **Reach** | Pessoas afetadas em periodo | Numero absoluto (ex: 10k usuarios/mes) |
| **Impact** | Tamanho do efeito por usuario | 0.25 (minimal), 0.5 (low), 1 (medium), 2 (high), 3 (massive) |
| **Confidence** | Probabilidade de resultado esperado | 50-100% |
| **Effort** | Pessoa-meses | Numero absoluto |

**Quando usar RICE > ICE**:
- Produto maduro com user data.
- Multiplos canais com reach diferentes (mudanca em paginas com 100 vs 100k visitas).
- Decisoes que precisam de mais rigor (roadmap quarterly).

**Quando usar ICE > RICE**:
- Pre-PMF / startup early-stage.
- Cadencia semanal de growth experiments.
- Escassez de dados de reach.

**Workflow**: comecar com ICE (rapido), graduar para RICE quando tiver data ([growthmethod.com](https://growthmethod.com), [productplan.com](https://www.productplan.com)).

## Fundacao 3 — Viral Loops + K-factor + Network Effects

### K-factor (Viral Coefficient)

**Formula**: K = i x c
- **i** = numero medio de invites enviados por usuario.
- **c** = conversion rate dos invites em novos usuarios.

**Interpretacao**:
- **K > 1**: crescimento viral self-sustaining (cada usuario gera > 1 novo usuario).
- **K = 0.5-1**: amplificacao significativa (paid acquisition multiplica).
- **K < 0.5**: viralidade marginal (ainda util mas nao primario).

**Cycle time** (tempo entre invite e conversao): tao importante quanto K. Cycle de 2 dias com K=0.5 cresce mais rapido que cycle de 30 dias com K=1.5.

### Cases historicos de viral loops

| Empresa | Mecanica | K estimado |
|---------|----------|-----------|
| **Hotmail (1996)** | "PS: Get your free email at Hotmail" no rodape | ~1.5 (12M users em 18 meses) |
| **PayPal (2000)** | US$10 signup + US$10 referral | ~1.0 |
| **Dropbox (2008)** | 500MB extra por referral | ~0.6 (cycle 2-7 dias) |
| **LinkedIn (2003-2008)** | Address book import + connection invites | ~0.7 |
| **Tinder (2012)** | Word-of-mouth + Greek life sorority strategy | network effect (nao viral loop classico) |
| **Slack (2013-2014)** | Email-to-team-domain auto-join | viral dentro de empresa |
| **Notion (2018-2020)** | Public pages indexadas no Google | content viral + word-of-mouth |
| **Calendly (2013-2020)** | Booking link como CTA implicito | viral cycle ~7 dias |

### Andrew Chen — "Retention is King"

Chen (a16z, ex-Uber) escreveu serie classica em [andrewchen.com](https://andrewchen.com) e livro [The Cold Start Problem (2021)](https://www.amazon.com/Cold-Start-Problem-Andrew-Chen/dp/B08VL6Z1V3):

1. **Viralidade sem retencao = balde furado** — produtos virais que nao retem (FarmVille, Quibi) colapsam.
2. **Hard side / easy side** em marketplaces — focar em hard side (ex: motoristas no Uber, criadores no YouTube) inicialmente.
3. **Atomic network** — menor unidade que ja entrega valor (ex: 1 escritorio no Slack, 1 Greek house no Tinder, 1 cidade no Uber).
4. **Tipping point** — quando rede atinge densidade que se autossustenta.
5. **Saturation -> growth ceiling** — toda viralidade satura; planejar canais paid/content para vida pos-saturation.

**Tipos de viral loop** (Chen):
- **Word-of-mouth puro** (Tinder, Notion) — sem mecanica formal, depende de produto excepcional.
- **Incentivado** (Dropbox, PayPal) — recompensa explicita.
- **Built-in** (Hotmail, Calendly) — uso do produto = exposicao automatica.
- **Content viral** (YouTube, TikTok) — UGC indexado/compartilhado.
- **Network invitation** (Slack, LinkedIn) — convite necessario para usar.

**Anti-pattern 2026**: copiar viral mechanics sem entender drivers underlying (Dropbox referral funcionou porque storage era valor universal; copiar em produto onde recompensa nao tem utilidade fracassa).

### Network Effects

**Tipos** (NfX [nfx.com](https://www.nfx.com)):
1. **Direct network effects** — telefone, WhatsApp (mais users = mais valor).
2. **Indirect / two-sided** — Uber, Airbnb, marketplaces (oferta atrai demanda atrai oferta).
3. **Data network effects** — Google Search, Waze (mais uso = melhor produto).
4. **Social network effects** — Facebook, Instagram (status, FOMO).
5. **Tech performance** — Bitcoin, BitTorrent (mais nodes = melhor performance).

**Brasil**: Mercado Livre (marketplace com 16+ paises, 100M+ buyers — 2-sided), iFood (couriers + restaurantes + comensais — 3-sided), Nubank (sem network effect classico — viralidade word-of-mouth).

## Fundacao 4 — Growth Experiments Cadence + ICE Scoring + Velocity

### Princípios (Sean Ellis "Hacking Growth", Morgan Brown)

1. **Hypothesis-driven** — toda ideia vira hipotese formal (formato abaixo).
2. **Cadencia semanal** — Growth team meeting weekly + 2-5 experiments running.
3. **Volume > acertos individuais** — meta de 80% experimentos sem resultado positivo (top quartil), 20% wins compoem.
4. **Statistical significance** — p < 0.05, sample size adequado (calculadoras: Optimizely, GrowthBook).
5. **Single variable testing** — A/B; multivariate (MVT) so com volume alto.

### Formato de hipotese (Sean Ellis)

```
Acreditamos que [mudanca proposta]
Para [audiencia/segmento]
Resultara em [metrica + magnitude]
Saberemos disso quando observarmos [criterio mensuravel]
em [periodo].
```

**Exemplo**:
> "Acreditamos que adicionar social proof (logos de clientes) na landing page de pricing aumentara conversao free-to-paid em 15% para visitors organicos. Saberemos disso quando observarmos uplift estatisticamente significativo (p<0.05) em 4 semanas com sample minimo de 5.000 visitors por variante."

### Cadencia semanal (Growth Team Meeting — Sean Ellis)

**Agenda 60min**:
1. **Metricas (5 min)** — North Star + AARRR weekly review.
2. **Aprendizados (10 min)** — resultados de experimentos da semana anterior.
3. **Backlog (15 min)** — review de 20-50 ideias com ICE scores.
4. **Prioritizacao (10 min)** — selecionar 3-5 experimentos para proxima semana.
5. **Acao (15 min)** — atribuir owners, deadlines, tracking plans.
6. **Bloqueios (5 min)** — eng/design/data dependencies.

### Velocity benchmark

| Estagio empresa | Experimentos/semana |
|----------------|---------------------|
| Pre-PMF startup | 1-2 |
| Post-PMF startup | 3-7 |
| Scale-up | 10-20 |
| Booking.com (referencia) | 1.000+ ativos simultaneos |

**Booking.com** publicou em 2017 que rodava ~1.000 testes A/B simultaneos com plataforma proprietaria + ETP (Experimental Testing Platform).

### Tools 2026 (experimentation platforms)

| Tool | Uso | Pricing |
|------|-----|---------|
| **GrowthBook** | Open-source A/B testing + feature flags | Free / Pro |
| **Optimizely** | Enterprise A/B + personalization | Enterprise |
| **VWO** | A/B + heatmaps + session replay | Mid-market |
| **LaunchDarkly** | Feature flags + experimentation | Enterprise |
| **PostHog** | Product analytics + experiments + session replay | Free open-source |
| **Statsig** | A/B + holdouts + exposures | Startup-friendly |
| **Eppo** | Experimentation com warehouse-native (Snowflake/BigQuery) | Mid/Enterprise |

### Tipos de experimento

1. **A/B classico** — variant A vs B, traffic split 50/50.
2. **A/B/n** — 3+ variantes (ex: 4 headlines).
3. **MVT (multivariate)** — varias variaveis simultaneas (precisa volume alto).
4. **Holdout** — % usuarios nao recebe nenhuma mudanca (controle longo prazo).
5. **Switchback** — alternancia temporal (marketplaces 2-sided).
6. **CUPED** — controle de variancia com pre-experiment data (acelera signif).

**Anti-pattern 2026**:
- Parar experimento quando "ganha" (peeking — inflaciona false positives).
- Multiple testing sem correcao (Bonferroni / FDR).
- Sample ratio mismatch (SRM) sem investigar.
- Confundir significancia estatistica com relevancia pratica.

## Fundacao 5 — Reforge 4-Fits + Brian Balfour Growth Model

### Reforge

**Origem**: Brian Balfour (ex-VP Growth HubSpot) fundou Reforge em 2016 — escola executive education para growth/product/marketing leaders. Em 2026 lancou AI Growth Course (cohort outubro 2025) cobrindo "growth equation" para era AI ([brianbalfour.com](https://brianbalfour.com), [blog.brianbalfour.com](https://blog.brianbalfour.com)).

### Os 4 Fits (Brian Balfour 2017, atualizado 2026)

Para crescer alem de US$100M ARR, 4 fits precisam estar alinhados:

#### 1. Market-Product Fit

- Produto resolve problema real de mercado real.
- Sean Ellis 40% test confirma.
- Retention curve flat ou smile.
- **Pergunta**: o produto e necessario?

#### 2. Product-Channel Fit

- Forma do produto + comportamento do usuario = canal natural de aquisicao.
- **Exemplos**:
  - Notion (UGC publico) -> SEO/word-of-mouth fit.
  - Slack (workplace tool) -> bottoms-up enterprise via teams.
  - HubSpot (SMB content-rich) -> content/SEO fit.
  - Dropbox (file sharing) -> referral/viral fit.
- **Anti-fit**: produto self-serve B2B SaaS tentando vender via outbound enterprise sales.
- **Pergunta**: o canal escala com a forma do produto?

#### 3. Channel-Model Fit

- Canal compativel com modelo de receita / pricing / payback.
- **Exemplos**:
  - Paid ads + LTV alto (ecommerce, SaaS pricey) = fit.
  - Paid ads + freemium B2C low-LTV = anti-fit (queima caixa).
  - SEO + ARPU baixo = fit (custo marginal proximo zero).
  - Outbound enterprise + ACV > US$50k = fit.
- **Pergunta**: o CAC do canal cabe no LTV?

#### 4. Model-Market Fit

- Modelo de receita/pricing compativel com willingness-to-pay do mercado.
- **Exemplos**:
  - SMB Brasil + SaaS US$500/mes -> anti-fit (ticket alto).
  - Enterprise + SaaS US$50/mes -> anti-fit (subdimensionado).
  - Consumer + freemium -> fit se viral, anti-fit se LTV baixo.
- **Pergunta**: pricing/modelo casa com economic do segmento?

**Insight Reforge**: a maioria das startups falha por desalinhamento entre 2+ fits, nao por execucao ruim em 1 fit isolado.

### Atualizacao 2026 (AI era — Balfour)

**Growth equation 2026**: Growth = (Acquisition + Retention + Monetization) x Defensibility.

**Componentes amplificados por AI**:
- **Acquisition**: AI-generated content (caveat: commodity), AI ads (Google PMax, Meta Advantage+).
- **Retention**: AI-driven personalization, predictive churn, AI agents (Sierra, Decagon).
- **Monetization**: dynamic pricing (Uber-like), AI upsell.
- **Defensibility**: data moats, network effects, brand (AI nao substitui).

**Componentes transformados**:
- **Channel mix** — search via Perplexity/ChatGPT/Gemini muda SEO (GEO/AEO ja afeta CTR).
- **Pricing** — usage-based pricing acelera (cobrando por AI tokens consumidos).
- **Defensibility** — codigo nao e moat (AI codifica rapido); dados proprietarios + distribution + brand sao.

### Andrew Chen — Cold Start Problem (2021)

Framework complementar a Balfour:

1. **Cold start** — produto sem usuarios.
2. **Tipping point** — atomic network atinge massa critica.
3. **Escape velocity** — efeitos de rede dominam crescimento.
4. **Hitting the ceiling** — saturacao de mercado/canal.
5. **Moat** — defesa contra competicao (especialmente Big Tech copiando).

**Aplicacao Brasil**: iFood resolveu cold start via blitz cidade-por-cidade (atomic network = cidade), Uber via Sao Paulo primeiro, Mercado Livre via leilao (eBay-like) inicialmente.

## Fundacao 6 — Brasil 2026 (Nubank/iFood/Magalu/Mercado Livre cases)

### Nubank

**Crescimento**: 0 a 100M+ clientes (Brasil + Mexico + Colombia) em 12 anos.

**Mecanicas growth**:
1. **Word-of-mouth puro** — produto excepcional (sem taxas, app moderno, cartao roxo) gerou viralidade organica.
2. **Waitlist scarcity** (early days) — pessoas indicavam para furar fila.
3. **Friction-free signup** — onboarding 100% digital (CPF + selfie + RG).
4. **Content marketing** — blog "Fala Nu", series "Por dentro do Nu".
5. **PR + brand** — David Velez visivel, narrativa de "destruir bancos tradicionais".
6. **NPS > 80** consistentemente — drives referral organico.

**K-factor estimado**: 0.5-0.7 (sem programa formal de referral por anos; viralidade pura).

**Lesson**: produto excepcional + brand forte > programa de referral mecanico.

**Fonte**: [Mundo do Marketing](https://mundodomarketing.com.br), [insights.allidem.com](https://insights.allidem.com), Bloomberg Brasil, Brainvest.

### iFood

**Crescimento**: 0 a 80M+ pedidos/mes (estimado 2024-2025).

**Mecanicas growth**:
1. **3-sided marketplace** — entregadores + restaurantes + consumidores.
2. **Couriers as growth channel** — entregadores visiveis na rua = brand awareness perpetua.
3. **Cidade-por-cidade rollout** (cold start solution) — saturar atomic network antes de expandir.
4. **iFood Pedidos cashback** + cupons agressivos (CAC subsidio).
5. **Performance marketing** Meta/Google massivo.
6. **Brand investment** — Big Brother Brasil patrocinio, futebol.
7. **iFood Decola** — programa para pequenos restaurantes (long-tail supply).

**Lesson**: liquidez do marketplace (atomic network: cidade saturada) > expansao geografica acelerada.

### Magazine Luiza (Magalu)

**Crescimento**: digitalizacao de varejista tradicional (1957) em e-commerce + marketplace + super-app.

**Mecanicas growth**:
1. **Lu do Magalu** — avatar virtual (criada 2003) com 60M+ followers cross-platform — humanizacao da marca.
2. **Magalu como marketplace** — abriu plataforma para terceiros (iFood-like move).
3. **Aquisicoes estrategicas** — Netshoes, Estante Virtual, Hub Fintech, Steal the Look.
4. **Logistica integrada** — Magalu Entregas (1P + 3P).
5. **Magalu Cloud** + Magalu Pagamentos (super-app fintech).
6. **Loja fisica + digital** — omnichannel + retirada em loja.
7. **Lu narrativa** — "Lu, a vendedora do Magalu" tornou-se influenciadora digital.

**Lesson**: brand humanization (Lu) + omnichannel + marketplace = crescimento defensivel.

### Mercado Livre

**Crescimento**: 1999 (eBay clone Argentina) -> 100M+ users LATAM, lider e-commerce + Mercado Pago.

**Mecanicas growth**:
1. **2-sided marketplace** — sellers atraem buyers atraem sellers (network effect direto).
2. **Mercado Pago** — fintech wrapper + cross-sell (super-app Latam).
3. **Mercado Envios** — logistica propria (defensibilidade vs Amazon).
4. **Mercado Credito** — credit scoring proprietario para sellers.
5. **Mercado Ads** — retail media (vendendo ads para sellers).
6. **Free shipping subsidio** agressivo (acima de R$ 79 em geral) — drive de aquisicao.
7. **Brand Brasil** — patrocinios futebol, Olimpiadas.

**Lesson**: network effect 2-sided + fintech wrapper + logistica = moat profundo.

### Brasil 2026 — Tendencias growth

1. **Pix como ativador** — checkout 1-clique (Pix Automatico em 2025/2026).
2. **WhatsApp como canal primario** — conversational commerce (Meta API + Pix).
3. **Retail media** — Mercado Livre Ads, Magalu Ads, Amazon Ads BR.
4. **Creator economy** — micro-influencers (Tik Tok, Kwai) > celebs.
5. **AI adoption** — Globo, Itau, Bradesco com agentes (e-commerce + atendimento).
6. **LGPD maturity** — first-party data + consent management.
7. **Cross-border BR-EUA-China** — Shein, AliExpress, Temu pressionando margens.

**Fonte**: [businessofapps.com](https://www.businessofapps.com/data/brazil-app-market/), [globenewswire.com](https://www.globenewswire.com), [americasmi.com](https://americasmi.com).

## Fundacao 7 — Mensuracao + Tools 2026

### Stack growth analytics 2026

| Camada | Tools | Uso |
|--------|-------|-----|
| **Product analytics** | Mixpanel, Amplitude, Heap, PostHog | Funnels, cohorts, retention curves |
| **Web analytics** | GA4 + GTM, Plausible, Fathom | Top of funnel, channels |
| **Session replay** | Hotjar, FullStory, LogRocket, PostHog | Qualitative insights |
| **Heatmaps** | Hotjar, Microsoft Clarity (free), Crazy Egg | Click/scroll patterns |
| **A/B testing** | GrowthBook, Optimizely, VWO, Statsig | Experiments |
| **Feature flags** | LaunchDarkly, Statsig, ConfigCat | Gradual rollout |
| **CDP** | Segment, RudderStack, Hightouch | Pipe events para 50+ destinos |
| **Warehouse** | Snowflake, BigQuery, Redshift, Databricks | Source of truth |
| **Reverse ETL** | Hightouch, Census | Warehouse -> tools |
| **MMM (mkt mix)** | Robyn (Meta open-source), Recast, Lifesight | Multi-touch attribution |
| **Cohort tools** | Mixpanel/Amplitude nativo, Looker, Hex | Cohort analysis |
| **Survey** | Typeform, Refiner, Sprig (in-product), Hotjar | PMF + NPS + qual |

### North Star Metric (NSM)

**Definicao** (Amplitude / Sean Ellis): unica metrica que melhor representa valor entregue ao usuario.

**Criterios** (Lenny Rachitsky):
1. Lead indicator de revenue (nao trailing).
2. Reflete valor real (nao vanity).
3. Mensuravel weekly.
4. Acionavel (time pode mover).

**Exemplos publicos**:
- **Spotify**: time spent listening.
- **Airbnb**: nights booked.
- **Slack**: weekly active teams.
- **Facebook**: daily active users.
- **Netflix**: viewing hours.
- **WhatsApp**: messages sent.
- **iFood**: pedidos completos.
- **Nubank**: clientes ativos (NPS-weighted) — inferencia.

**L1/L2/L3 metrics tree** — NSM (L1) decomposto em inputs (L2) decompostos em sub-inputs (L3).

### Benchmarks AARRR 2026 por industry

| Industry | Activation | D30 retention | LTV:CAC | NPS |
|----------|-----------|--------------|---------|-----|
| **SaaS B2B self-serve** | 30-50% | 70-85% | 3-5x | 30-50 |
| **SaaS B2B sales-led** | 50-70% | 80-95% | 5-10x | 40-60 |
| **Consumer apps** | 20-40% | 5-15% | 1-3x | 20-40 |
| **Marketplaces 2-sided** | 15-30% | 40-60% | 3-7x | 30-50 |
| **Fintech BR** | 40-60% | 60-80% | 5-15x | 50-80 (Nubank) |
| **E-commerce** | 30-50% | 20-40% | 2-4x | 20-50 |

**Caveat**: benchmarks variam dramaticamente por sub-segmento; usar como referencia inicial.

### MMM + MTA + incrementality 2026

**Pos-iOS 14.5 ATT (2021)** + **third-party cookie deprecation (Chrome 2024)**: attribution multi-touch (MTA) ficou unreliable.

**Stack moderno** (Recast, Robyn — Meta open-source):
1. **MMM (Marketing Mix Modeling)** — modelo Bayesiano de regressao com saturacao + adstock.
2. **Geo experiments** (Google Causal Impact, GeoLift Meta open-source) — incrementality por regiao.
3. **Holdout tests** — % audiencia nao recebe canal (controle).
4. **Conversion lift studies** — Meta/Google nativo.
5. **First-party data + server-side tracking** (Conversions API, GA4 server-side).

**Anti-pattern**: confiar em last-click attribution em 2026 (subestima top of funnel).

## Fundacao 8 — Aplicacao em Content MKT

Como esta SKILL alimenta producao de content marketing pelas 5 audiencias frank-mkt:

### 1. Founders (pre-PMF)

**Conteudo**:
- Tutorial Sean Ellis 40% Test (template + analise).
- AARRR funnel canvas (template editavel).
- "5 sinais que voce nao tem PMF (e o que fazer)".
- Case Brasil: Nubank cold start.
- Toolkit: Mixpanel free + Hotjar + Typeform.

**Formato**: blog longo + video tutorial + planilha + Notion template.

### 2. CMOs (scaling growth)

**Conteudo**:
- 4-Fits Reforge applied (worksheet).
- Stack moderno: CDP + warehouse + experimentation platform.
- MMM vs MTA em era post-cookies.
- Benchmarks AARRR por industry.
- Case: como Magalu consolidou super-app.

**Formato**: whitepaper, webinar, framework downloadavel.

### 3. PMs (growth-focused)

**Conteudo**:
- ICE/RICE templates Notion + Airtable.
- Hypothesis-driven experiments framework.
- North Star Metric tree exercise.
- Activation milestones por industry.
- Case: Slack 2k messages activation insight.

**Formato**: tutorial step-by-step + templates.

### 4. Growth marketers / performance

**Conteudo**:
- Channel-Model Fit calculator (LTV:CAC payback).
- Holdout test setup (Meta + Google).
- Robyn MMM hands-on tutorial.
- Creative testing velocity (Meta Advantage+).
- Case: iFood couriers as channel.

**Formato**: hands-on tutorials + scripts + dashboards.

### 5. Agencias

**Conteudo**:
- Growth retainer pricing model.
- AARRR audit framework para clientes.
- Templates de hypothesis backlog.
- Reporting dashboard (Looker Studio + GA4).
- Case: como agencia ajudou e-commerce BR a 10x revenue.

**Formato**: kits + treinamentos + consultoria packages.

## Anti-Patterns 18

1. **"Growth hacking" como sinonimo de hacks pontuais** — confundir tactics com sistema.
2. **Aquisicao antes de PMF** — gastar em ads em produto com retencao plana.
3. **Vanity metrics** — total signups sem activation/retention.
4. **K-factor sem cycle time** — K=2 com cycle 60 dias < K=0.6 com cycle 2 dias (Dropbox).
5. **Copiar viral mechanics sem entender driver** — Dropbox referral funcionou porque storage era universal.
6. **Programa de referral antes de retencao** — usuarios que nao voltam nao indicam.
7. **Definir activation como signup** — signup != activation (signup e zero value).
8. **Focar em DAU sem cohorts** — DAU plano mascara churn alto.
9. **Last-click attribution em 2026** — ignora top of funnel (cookies + ATT quebraram).
10. **Peeking em A/B test** — parar ao "ganhar" inflaciona false positives.
11. **Multiple testing sem correcao** — 20 testes simultaneos = ~64% chance de >=1 falso positivo (5%).
12. **Confundir significancia estatistica com relevancia pratica** — uplift 0.5% pode ser p<0.05 mas irrelevante.
13. **Single test "definitivo"** — growth e cadencia de centenas/milhares de testes.
14. **PMF como evento unico** — PMF decai com competicao/expansao; medir quarterly.
15. **NSM mal escolhido (vanity)** — "registered users" > "weekly active users" e vanity.
16. **Channel concentration** — 80% trafico de 1 canal (algoritmo muda = morte).
17. **Ignorar Channel-Model Fit** — paid ads com LTV baixo + freemium = queima caixa.
18. **Growth team isolado de produto** — growth nao funciona sem product input nas alavancas core.

## 18 Regras de Ouro

1. **PMF antes de growth** — Sean Ellis 40% test + smile retention curve sao gates.
2. **AARRR e mapa, nao receita** — instrumentar 5 estagios + identificar gargalo.
3. **Activation > acquisition** — fix the leaky bucket primeiro.
4. **Retencao e o motor real** — sem retencao, viralidade e ads sao band-aid.
5. **Hypothesis-driven** — toda ideia vira hipotese formal antes de teste.
6. **Cadencia semanal** — Growth Team Meeting weekly, 3-5 experiments running.
7. **Volume > acertos** — 80% experimentos sem efeito e normal.
8. **ICE para velocidade, RICE para precisao** — escolher segundo estagio.
9. **Statistical rigor** — p<0.05, sample size, no peeking, correcao multiple testing.
10. **K = i x c (com cycle time)** — viralidade tem 3 dimensoes.
11. **Network effects > viral loops** — 2-sided marketplaces sao mais defensaveis.
12. **4-Fits alinhados** — Market-Product, Product-Channel, Channel-Model, Model-Market.
13. **NSM unico, decomposto em L2/L3** — clareza vertical do time.
14. **First-party data primeiro** — server-side tracking + CDP + consent.
15. **MMM + geo experiments + holdouts** — pos-cookies, attribution e estatistica.
16. **Brasil = cidade-por-cidade** (atomic network) — iFood, Uber playbook.
17. **Word-of-mouth > programa de referral** quando produto e excepcional (Nubank).
18. **Growth + product = mesma equipe** — alavancas core estao no produto, nao em ads.

## Exemplos Comportamentais

### Persona 1 — Mariana, founder pre-PMF (SaaS B2B brasileiro)

**Cenario**: 1.000 signups, 200 ativos D30 (20% retention), CAC R$ 80, LTV inferido R$ 240. Considera levantar Series A em 6 meses.

**Como esta SKILL ajuda**:
1. **Sean Ellis 40% Test** — survey aos 200 ativos. Resultado: 28% very disappointed -> NAO TEM PMF.
2. **Acao**: pausar gastos em ads, focar em entrevistas qualitativas com os 28% (super-fans).
3. **Insight**: super-fans sao agencias de marketing pequenas (5-15 pessoas), nao SMBs genericas. Pivot positioning.
4. **Re-test PMF em 90 dias** apos refinement: 47% very disappointed. PMF achieved.
5. **AARRR funnel** instrumentado em Mixpanel. Activation gargalo: 35% completam onboarding. Goal: 60%.
6. **3 experiments/semana** em activation (ICE prioritized).
7. **Series A com narrative de PMF + retention curve smile**.

**Output skill**: framework PMF survey + plano de pivot + AARRR canvas + ICE backlog.

### Persona 2 — Rafael, CMO de scale-up e-commerce BR

**Cenario**: e-commerce moda, R$ 200M GMV/ano, growing 30% YoY (slowing from 80%). Concentrado 70% Meta ads. CAC subindo, ROAS caindo.

**Como esta SKILL ajuda**:
1. **4-Fits audit** — identifica Channel-Model Fit risk (concentracao Meta + LTV plano = perigo).
2. **Diversificar canais** segundo 4-Fits: SEO (content + product pages), retail media (Mercado Livre Ads, Magalu Ads), creator economy (TikTok Shop, micro-influencers), CRM (email + WhatsApp).
3. **MMM com Robyn** — quantifica incrementalidade por canal (Meta saturado em > 60% de share).
4. **Holdout test** mensal por canal — incrementalidade real.
5. **Activation foco**: % first-time buyer que faz 2a compra em 30 dias (de 18% para 28%).
6. **Programa de fidelidade Lu-style** (humanizacao + gamificacao).
7. **Brasil cases**: Magalu omnichannel + Mercado Livre marketplace inspiram super-app moves.

**Output skill**: 4-Fits worksheet + MMM stack + Brasil benchmarks + diversification roadmap.

### Persona 3 — Camila, PM Growth em fintech BR (Nubank-like wannabe)

**Cenario**: app fintech early-stage, 50k users, K-factor 0.3, busca crescer self-sustaining.

**Como esta SKILL ajuda**:
1. **K = i x c decomposicao** — i (invites) = 0.8, c (conversion) = 0.37. Bottleneck: invites baixos.
2. **Hipotese**: aumentar i via in-app share + WhatsApp deep-link. ICE = 9 x 7 x 8 = 504 (high).
3. **Cycle time** atual = 18 dias. Reduzir para 7 dias via push notification reminder.
4. **Andrew Chen lessons** — focar em retention primeiro (D30 atual = 45%, target 70%) antes de escalar viral.
5. **Atomic network**: identifica que clusters universitarios sao high-K segmentos -> targeting.
6. **PMF survey** segmentado: gen Z 22+ tem 52% very disappointed, gen X tem 18%. Foco gen Z.
7. **Roadmap**: 12 weeks com goal K=0.7, cycle 7 days, D30 60%.

**Output skill**: K-factor calculator + Andrew Chen retention-first playbook + Brasil viral cases.

### Persona 4 — Lucas, dono de agencia growth (5-12 clientes B2B)

**Cenario**: agencia growth-focused, oferece performance + CRO + content. Quer subir ticket de R$ 8k/mes para R$ 25k/mes com pacote "Growth-as-a-Service".

**Como esta SKILL ajuda**:
1. **AARRR audit framework** vendido como engagement inicial (R$ 15k 1-time) -> identifica top 3 gargalos do cliente.
2. **Hypothesis backlog** mensal (30+ ideias com ICE) -> diferencial vs agencia tactical.
3. **Cadencia semanal** Growth Team Meeting para clientes -> "feel premium".
4. **Stack proprio**: GrowthBook + Hotjar Clarity + GA4 + Looker Studio (low cost, high signal).
5. **Pricing tiered**: Audit (1x R$15k), Implementation (3-6 meses R$ 25k/mes), Retainer (R$ 18k/mes manutencao).
6. **Cases Brasil** alimentam pitch (Nubank/iFood/Magalu) — credibilidade contextual.
7. **Treinamento interno time agencia** com SKILL frank-mkt (Lucas = scale).

**Output skill**: kit completo agencia (audit framework + pricing model + stack + case bank).

## Checklist Contraditorio Interno (10 perguntas)

Antes de aplicar growth tactics:

1. **Existe PMF?** Sean Ellis 40% test confirmado em segmento-alvo nas ultimas 12 semanas?
2. **Activation esta resolvido?** % activation > benchmark industry (consumer 20-40%, SaaS 30-70%)?
3. **Retention curve e smile/flat?** Cohort D30 estavel ou subindo, nao caindo?
4. **NSM esta correto?** E lead indicator de revenue, mensuravel weekly, acionavel?
5. **AARRR funnel esta instrumentado?** Cada estagio tem evento + dashboard?
6. **Backlog de experimentos > 20 ideias com ICE?** Ou time esta operando reativo?
7. **Cadencia weekly de experimentos?** Growth Team Meeting acontece?
8. **Channel-Model Fit ok?** LTV:CAC > 3:1 e CAC payback < 12 meses?
9. **Channel concentration < 60%** em qualquer canal unico (anti-fragility)?
10. **First-party data + consent** capturado pos-cookies/ATT (Conversions API + CDP)?

Se >= 7 sim: pronto para escalar. Se < 7: corrigir gaps antes de gastar.

## Referencias

### Canonical books

- Sean Ellis & Morgan Brown — [Hacking Growth (2017)](https://www.amazon.com/Hacking-Growth-Fastest-Growing-Companies-Breakout/dp/045149721X)
- Andrew Chen — [The Cold Start Problem (2021)](https://www.amazon.com/Cold-Start-Problem-Andrew-Chen/dp/B08VL6Z1V3)
- Eric Ries — [The Lean Startup (2011)](http://theleanstartup.com/)
- Alistair Croll & Benjamin Yoskovitz — [Lean Analytics (2013)](https://leananalyticsbook.com/)
- Hila Qu — [Growth Levers and How to Find Them (2024)](https://www.amazon.com/Growth-Levers-How-Find-Them/dp/B0CR5CWBYB)
- Elena Verna — [Reforge essays](https://www.elenaverna.com/)
- Brian Balfour — [Four Fits Growth Framework](https://brianbalfour.com/four-fits-growth-framework)
- Lenny Rachitsky — [Lenny's Newsletter](https://www.lennysnewsletter.com/)

### AARRR — Dave McClure

- [Slideshare original 2007 — Startup Metrics for Pirates](https://www.slideshare.net/dmc500hats/startup-metrics-for-pirates-long-version)
- [FourWeekMBA — AARRR Metrics 2026](https://fourweekmba.com/pirate-metrics/)
- [BuiltIn — What is AARRR](https://builtin.com/articles/aarrr)
- [GrowWithWard — AAARRR Pirate Funnel 5 steps](https://growwithward.com/aaarrr-pirate-funnel/)
- [DigitalLeadership — AAARRR Framework](https://digitalleadership.com/unite-articles/pirate-metrics-funnel-aaarrr/)
- [Dinmo — AARRR essential growth marketing framework](https://www.dinmo.com/marketing-strategy/data-driven-marketing/aarrr/)
- [UserGuiding — AAARRR Pirate Metrics & Funnel](https://userguiding.com/blog/pirate-metrics-aaarrr)
- [Trust — Dave McClure's AARRR](https://usetrust.io/blog/how-to-use-dave-mcclures-aarrr-growth-hacking/)
- [Growth Thinking — Pirate Funnel AARRR](https://mygrowththinking.com/the-pirate-funnel-aarrr-framework-explained/)

### Sean Ellis 40% Test + PMF

- [pmfsurvey.com (Sean Ellis + GoPractice)](https://pmfsurvey.com/about/)
- [Lenny — The Original Growth Hacker Sean Ellis](https://www.lennysnewsletter.com/p/the-original-growth-hacker-sean-ellis)
- [PMF Show — Sean Ellis growth at Dropbox](https://www.pmf.show/sean-ellis-led-growth-at-dropbox-invented-growth-hacking-heres-his-step-by-step-growth-guide/)
- [FitSignal — Sean Ellis 40% Test guide](https://www.fitsignal.com/blog/sean-ellis-40-percent-test)
- [LearningLoop — Sean Ellis Score](https://learningloop.io/glossary/sean-ellis-score)
- [Mapster — Sean Ellis PMF Survey](https://www.mapster.io/sean-ellis-pmf-survey)
- [Rahul Vohra — How Superhuman Built an Engine to Find PMF (FirstRound)](https://review.firstround.com/how-superhuman-built-an-engine-to-find-product-market-fit/)
- [IdeaProof — Sean Ellis Test 40% Rule 2026](https://ideaproof.io/questions/sean-ellis-test)
- [Product Coalition — Using Sean Ellis Test](https://medium.productcoalition.com/using-sean-ellis-test-for-measuring-your-product-market-fit-c8ac98053c2c)

### ICE / RICE Prioritization

- [GrowthMethod — ICE Framework](https://growthmethod.com/ice-framework/)
- [GrowWithWard — How NOT to Score ICE](https://growwithward.com/ice-prioritization-framework/)
- [ProductPlan — ICE Scoring Model](https://www.productplan.com/glossary/ice-scoring-model)
- [Intercom blog — RICE prioritization framework](https://www.intercom.com/blog/rice-simple-prioritization-for-product-managers/)
- [Kaizenko — Scoring Frameworks ICE/RICE](https://www.kaizenko.com/scoring-frameworks-ice-rice-and-weighted-scoring-for-product-prioritization/)
- [ProductLift — RICE vs ICE](https://www.productlift.dev/blog/rice-vs-ice)
- [Itamar Gilad — Confidence Meter](https://itamargilad.com/the-tool-that-will-help-you-choose-better-product-ideas/)
- [Zeda — ICE Scoring Prioritization](https://zeda.io/blog/ice-scoring-prioritisation-model)
- [IdeaPlan — RICE vs ICE vs MoSCoW 2026](https://www.ideaplan.io/compare/rice-vs-ice-vs-moscow)

### Viral loops + K-factor + Andrew Chen

- [Andrew Chen — andrewchen.com](https://andrewchen.com/)
- [Andrew Chen Substack — Braindump on Viral Loops](https://andrewchen.substack.com/p/braindump-on-viral-loops)
- [Andrew Chen — Retention is King](https://andrewchen.com/retention-is-king/)
- [Andrew Chen — Retention for Increase Viral Growth](https://viral-loops.com/blog/retention-for-viral-growth/)
- [Andrew Chen — More Retention More Viral Growth](https://andrewchen.com/more-retention-more-viral-growth/)
- [Speedrun Substack — Lost Art of Designing Viral Loops](https://speedrun.substack.com/p/the-lost-art-of-designing-viral-loops)
- [IdeaPlan — Viral Coefficient K-factor](https://www.ideaplan.io/metrics/viral-coefficient-k-factor)
- [Arfadia — K-Factor Complete Viral Growth Guide](https://www.arfadia.com/glossary/EN/k-factor)
- [Point Nine — Understanding Viral Growth in SaaS](https://medium.com/point-nine-news/understanding-viral-growth-in-saas-45eea50d8900)
- [StartupGTM — Andrew Chen Founder's Playbook](https://startupgtm.substack.com/p/the-andrew-chen-founders-playbook)

### Brian Balfour + Reforge

- [Brian Balfour — brianbalfour.com](https://brianbalfour.com/)
- [Brian Balfour — Four Fits Growth Framework](https://brianbalfour.com/four-fits-growth-framework)
- [Brian Balfour Blog — Four Fits in AI Era](https://blog.brianbalfour.com/p/the-four-fits-a-growth-framework)
- [Brian Balfour Blog — AI Growth Course](https://blog.brianbalfour.com/p/ai-growth-course)
- [Brian Balfour — $100M Frameworks Paid](https://brianbalfour.com/landing/p-100m-frameworks)
- [Reforge](https://www.reforge.com/)
- [Aakash Gupta — Reforge Growth Crash Course Brian Balfour](https://www.news.aakashg.com/p/reforge-growth-crash-course)
- [StartupAnatomy — How Brian Balfour Built Reforge](https://startupanatomy.substack.com/p/how-brian-balfour-built-reforge-and)

### Brasil cases

- [Mundo do Marketing — Nubank, Natura e iFood marcas mais influentes 2025](https://mundodomarketing.com.br/nubank-natura-e-ifood-sao-as-marcas-mais-influentes-do-brasil-em-2025)
- [insights.allidem.com — marcas brasileiras mais valiosas Nubank iFood Magalu](https://insights.allidem.com/como-lideram-as-marcas-brasileiras-mais-valiosas)
- [Unicep — Cases de Sucesso Empresas Brasileiras](https://www.unicep.edu.br/post/marketing-digital-cases-de-sucesso-de-empresas-brasileiras)
- [BusinessOfApps — Brazil App Market Statistics 2026](https://www.businessofapps.com/data/brazil-app-market/)
- [GlobeNewswire — Brazil Loyalty Business Report 2026](https://www.globenewswire.com/news-release/2026/02/10/3235128/28124/en/Brazil-Loyalty-Business-Report-2026.html)
- [GlobeNewswire — Brazil BNPL Report 2026](https://www.globenewswire.com/news-release/2026/02/04/3231847/28124/en/Brazil-Buy-Now-Pay-Later-Business-and-Investment-Opportunity-Report-2026.html)
- [AmericasMI — Retail Media Latin America](https://americasmi.com/insights/retail-media-latin-america/)
- [iCloud — Novas Formas de Empreender](https://icloud.com.br/blog/novas-formas-de-empreender/)

### Mensuracao / tools

- [Mixpanel](https://mixpanel.com/)
- [Amplitude](https://amplitude.com/)
- [PostHog](https://posthog.com/)
- [Heap](https://www.heap.io/)
- [GA4](https://marketingplatform.google.com/about/analytics/)
- [Hotjar](https://www.hotjar.com/)
- [Microsoft Clarity (free)](https://clarity.microsoft.com/)
- [GrowthBook](https://www.growthbook.io/)
- [Optimizely](https://www.optimizely.com/)
- [Statsig](https://statsig.com/)
- [Eppo](https://www.geteppo.com/)
- [LaunchDarkly](https://launchdarkly.com/)
- [Segment](https://segment.com/)
- [Robyn (Meta open-source MMM)](https://facebookexperimental.github.io/Robyn/)
- [Recast (MMM)](https://www.getrecast.com/)
- [GeoLift (Meta open-source)](https://github.com/facebookincubator/GeoLift)

### Network effects + marketplaces

- [NfX — Network Effects Bible](https://www.nfx.com/post/network-effects-bible)
- [a16z — All About Network Effects](https://a16z.com/all-about-network-effects/)
- [Sangeet Choudary — Platform Revolution](https://platformed.info/)
- [Bill Gurley — All Markets are Not Created Equal (10 factors of marketplaces)](https://abovethecrowd.com/2012/11/13/all-markets-are-not-created-equal-10-factors-to-consider-when-evaluating-digital-marketplaces/)

### Lenny Rachitsky / outras

- [Lenny's Newsletter](https://www.lennysnewsletter.com/)
- [Andrew Chen Twitter @andrewchen](https://x.com/andrewchen)
- [Sean Ellis Twitter @SeanEllis](https://x.com/SeanEllis)
- [Hiten Shah — Crazy Egg / KISSmetrics co-founder](https://hitenism.com/)
- [Hila Qu — Reforge instructor](https://www.elenaverna.com/p/hila-qu-on-growth-loops)
- [Casey Winters — Pinterest growth lead](https://caseyaccidental.com/)

## Cross-Skill References

Esta SKILL conecta com (ecossistema frank-mkt):

- **product-marketing** — go-to-market launches, positioning, lifecycle stages.
- **ABM** (account-based marketing) — variante para enterprise + ICP profundo.
- **pricing-strategy** — Channel-Model Fit (Balfour) + LTV:CAC.
- **GTM-strategy** — go-to-market frameworks (sister 2o lote).
- **funil-jornada** — AARRR funnel canonical + customer journey mapping.
- **metricas-marketing** — North Star Metric, NPS, MMM.
- **persona-icp-deep** — segmentation para PMF survey + Channel-Model Fit.
- **competitive-intelligence** — competitive moats + defensibility.
- **posicionamento-marca** — positioning antes de growth (April Dunford).
- **branding** — brand investment como growth long-term (Nubank/Magalu).
- **tecnicas-ia-claude-gemini-mkt** — AI para experiment ideation + content velocity.
- **conhecimento-ga4** — instrumentacao web analytics.
- **conhecimento-meta-ads** + **conhecimento-google-ads** + **conhecimento-linkedin-ads** — paid acquisition channels.
- **copywriting-conversao** — landing pages + creative testing.
- **conteudo-evergreen** — SEO/content como Channel.
- **big-idea** — narrativa de growth para investidores.
- **analise-concorrencia** — input para 4-Fits.
- **dominio-empreendedorismo-mkt** — founder-led growth.
- **dominio-financeiro-mkt** — unit economics, CAC payback, LTV.
- **dominio-ia-mkt** — AI growth equation (Balfour 2026).

## Integracao Ecossistema Frank-MKT

**Ordem de aplicacao recomendada para founder/CMO**:

1. **persona-icp-deep** — clarify ICP.
2. **posicionamento-marca** — April Dunford positioning.
3. **growth-hacking (esta SKILL)** — PMF test + AARRR mapping.
4. **funil-jornada** — customer journey detalhada.
5. **GTM-strategy** — go-to-market plan.
6. **product-marketing** — launches + lifecycle.
7. **pricing-strategy** — Channel-Model Fit pricing.
8. **metricas-marketing** — NSM + dashboards.
9. **conhecimento-ga4** + **conhecimento-meta-ads** + **conhecimento-google-ads** — instrumentar + paid.
10. **copywriting-conversao** — landing pages experimentation.
11. **conteudo-evergreen** — SEO/content channel.
12. **competitive-intelligence** — monitor competitive moves.

**Triggers de uso desta SKILL**:
- Founder pre-PMF -> Sean Ellis 40% test.
- CMO scaling -> 4-Fits audit + diversification.
- PM growth -> AARRR funnel + experiments cadence.
- Performance marketer -> Channel-Model Fit + MMM.
- Agencia -> AARRR audit framework para clientes.

**Output esperado**:
- AARRR funnel canvas instrumentado.
- PMF survey resultados + segmentation.
- ICE/RICE backlog (20+ experiments).
- Hypothesis-driven test cadence weekly.
- 4-Fits worksheet preenchida.
- NSM + L2/L3 metrics tree.
- Stack mensuracao operante (Mixpanel/Amplitude + GA4 + GrowthBook).

---

**Disclaimer educational**: esta SKILL e material educacional consolidando frameworks publicos (McClure, Sean Ellis, Andrew Chen, Brian Balfour) e analise de cases publicos brasileiros (Nubank, iFood, Magalu, Mercado Livre). Nao substitui aconselhamento estrategico personalizado. Benchmarks e estatisticas mudam com o tempo — verificar fontes originais. K-factors e LTV:CAC sao estimativas inferidas de fontes publicas, nao numeros oficiais das empresas. Cases brasileiros baseados em reportagens, palestras publicas e analise de marketing observavel — nao representam endorsement ou parceria. Sempre validar tactics com testes proprios em seu contexto antes de escalar investimento.
