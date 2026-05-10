---
name: conhecimento-google-ads
description: Conhecimento Google Ads 2026 (Search + Display + YouTube + Performance Max + Demand Gen + Discovery + Shopping + App + Smart Bidding tROAS/tCPA + Quality Score + audiences + creative + Enhanced Conversions + Consent Mode v2) para performance marketers/CMO/founders/agencias, com cobertura Performance Max default 2024-2026 + Smart Bidding AI mandatory + Enhanced Conversions first-party data + Consent Mode v2 EU/Brasil + Quality Score 1-10 lift CPC -50% se 10. 2a SKILL Bloco Conhecimento de Plataforma.
volatility: high
last_review: 2026-05-09
next_review: 2026-08-09
languages: [pt-BR]
audience: [performance-marketers, CMO, founders, agencias, growth-marketers, media-buyers]
ascii_only: true
---

# Skill: conhecimento-google-ads

## Decaimento Temporal

> Ultima verificacao: 2026-05-09 | Proxima revisao: 2026-08-09 | Volatility: **HIGH** (3 meses)
>
> Google Ads opera em ciclo de release continuo, com mudancas estruturais a cada 6-12 semanas. Em 2026, a plataforma vive 4 forcas de instabilidade simultaneas que exigem reground frequente:
>
> 1. **AI mandatory shift** — Smart Bidding ja responde por ~88% do gasto em 2026 (vs 71% em 2024); manual CPC virou exotico. Performance Max e default para e-commerce e domina ~62% dos cliques. Mudancas de modelo em tROAS/tCPA acontecem sem changelog publico.
> 2. **Privacy/Consent Mode v2** — virada de 15-jun-2026 reorganiza completamente quem controla dados (ad_storage no Google Ads vira autoridade unica, Google Signals deixa de co-controlar). Anunciante que nao tem Consent Mode v2 + Enhanced Conversions perde 20-40% de conversoes mensuraveis.
> 3. **3rd-party cookies + Chrome user-choice** — apos abandono da deprecation forcada (jul-2024), Chrome migrou para "user-choice in privacy settings". Cookies 3p ainda existem em 2026 mas dependem de consentimento ativo, derrubando match rate de Customer Match e remarketing.
> 4. **AI Max + RSA evolution** — RSA virou padrao de Search desde 2022; em 2026 Google testa AI Max (camada de IA generativa sobre RSA) que reescreve titulos em runtime. Quality Score, Ad Strength e Relative CTR ganharam fatores semanticos novos.
>
> **Reground antes de qualquer peca formal:**
> - Google Ads Help Center — https://support.google.com/google-ads
> - Google Ads & Commerce Blog — https://blog.google/products/ads-commerce/
> - Think with Google — https://www.thinkwithgoogle.com
> - Google Ads Liaison (X/@adsliaison) — atualizacoes informais
> - Google Search Status Dashboard — https://status.search.google.com
> - PPC Land — https://ppc.land
> - Search Engine Land (PPC channel) — https://searchengineland.com/library/channel/ppc
>
> **Acionamento:** planejamento de campanha Google Ads, auditoria de conta, escolha de tipo de campanha (Search/Pmax/YouTube/Demand Gen/Shopping/App), definicao de bidding (tROAS/tCPA/Maximize), Quality Score baixo, Ad Strength Poor, mensuracao GA4 + Enhanced Conversions, Consent Mode v2, Customer Match, debug de Performance Max, briefing de criativo de video, benchmarks por industria, ROAS abaixo da meta.
>
> **Skills relacionadas:** `conhecimento-meta-ads` (sister no bloco), `conhecimento-linkedin-ads` (sister), `conhecimento-ga4` (mensuracao downstream), `conhecimento-search-console` (organico complementar), `conhecimento-conar-cdc` (compliance publicidade BR), `seo-tecnico` (landing page Quality Score), `metricas-marketing` (ROAS/CAC/LTV), `funil-jornada` (mapping campanha por estagio), `copywriting-conversao` (RSA headlines/descriptions), `dominio-juridico-mkt` (LGPD/CDC para anuncios juridicos).

---

## Visao Geral

Google Ads em 2026 nao e mais "leilao de palavras-chave + lance manual". E uma **plataforma de IA com 9 tipos de campanha**, onde o anunciante terceiriza decisoes operacionais (lance, criativo, segmentacao) para modelos de Smart Bidding e cede sinais (signals, conversoes valoradas, first-party data) para o sistema otimizar.

Quem entra esperando rodar tudo no manual perde dinheiro. Quem entra entregando os sinais errados (proxy conversions, valores estimados ruins, audiencias contaminadas) treina o algoritmo contra si.

Esta skill e um **mapa operacional** para que o marketer/CMO/founder/agencia tome decisoes corretas em 9 dimensoes:

1. **Tipo de campanha** — Search vs Display vs YouTube vs Performance Max vs Demand Gen vs Discovery (deprecating) vs Shopping vs App vs Local.
2. **Estrutura de conta** — campaign / ad group / keyword / asset group / ad — e quando consolidar vs quando segmentar.
3. **Bidding** — Maximize Conversions vs tCPA vs Maximize Conversion Value vs tROAS vs Manual CPC (legado) — e quando trocar.
4. **Audiencias** — Custom Segments + Affinity + In-Market + Life Events + Customer Match + Remarketing + Similar Audiences (deprecating).
5. **Criativo** — RSA (15 headlines + 4 descriptions), video YouTube/Shorts, asset groups Pmax, image/text/logo/video.
6. **Quality Score / Ad Strength** — relevance + landing page + expected CTR + Ad Strength + relative CTR.
7. **Mensuracao** — Google Ads tag + GA4 + Enhanced Conversions + offline conversions + cross-device + Consent Mode v2.
8. **Privacy** — LGPD (BR) + GDPR (EU) + Consent Mode v2 + first-party data + Customer Match hashing.
9. **Aplicacao por audiencia** — performance marketer / CMO / founder / agencia / growth / media buyer.

A skill cobre 8 fundacoes, 18 anti-patterns, 18 regras de ouro, 4 personas, checklist contraditorio e ~60 referencias.

> **Cristal C0 — Google Ads em 2026 e AI-first ou nao e Google Ads.** Manual CPC virou exotico, RSA virou unico formato de Search, Performance Max virou default. Quem briga com a IA da plataforma esta brigando com o motor que move 88% do gasto global.

---

## Fundacao 1 — Google Ads Foundations (campaign types, estrutura, match types)

### 1.1 Os 9 tipos de campanha em 2026

| Tipo | Inventario | Uso primario | Status 2026 |
|------|-----------|--------------|-------------|
| **Search** | Google Search + parceiros de busca | Demanda existente, intencao alta | Padrao consolidado |
| **Performance Max (Pmax)** | Search + Display + YouTube + Gmail + Maps + Discover | Conversao multi-canal automatica | Default 2024-2026 |
| **Display** | GDN (Google Display Network) — sites/apps parceiros | Awareness + remarketing | Em declinio frente a Pmax |
| **YouTube (Video)** | YouTube + parceiros video | Awareness, consideration, action (TrueView for Action) | Crescendo via Shorts |
| **Demand Gen** | YouTube + Shorts + Discover + Gmail | Awareness/consideration visual | Substituiu Discovery em 2024 |
| **Discovery** | Discover + YouTube + Gmail | (legado) | Migrado para Demand Gen |
| **Shopping (Standard)** | Google Shopping + SERP | E-commerce com feed | Coexiste com Pmax para retail |
| **App** | Search + Play + YouTube + Display | Install/in-app action | Default mobile-first |
| **Local / Smart** | Maps + Search + Display | Pequenos negocios fisicos | Em transicao para Pmax |

> **Regra de selecao 2026:**
> - E-commerce com feed -> Performance Max (default) + Shopping (controle)
> - Demanda de busca clara (B2B, juridico, servicos) -> Search
> - Awareness puro vertical/Shorts -> YouTube + Demand Gen
> - App install -> App campaigns
> - Negocio local fisico -> Local/Pmax for store goals
> - Brand defense -> Search com brand keywords (NAO Pmax — canibaliza)

### 1.2 Estrutura hierarquica

```
ACCOUNT (MCC/Manager opcional)
  +-- CAMPAIGN (objetivo, orcamento, bidding, geo, idioma, tipo)
       +-- AD GROUP (tema/intencao) — apenas Search/Display/Video
       |    +-- KEYWORD (Search) ou PLACEMENT (Display) ou TARGETING
       |    +-- AD (RSA, Display, Video)
       +-- ASSET GROUP (Performance Max) — equivalente moderno do ad group
            +-- ASSETS (headlines, descriptions, images, logos, videos)
            +-- AUDIENCE SIGNALS (custom segments, customer match, in-market)
            +-- LISTING GROUPS (se tem feed)
```

> Em 2026, Pmax nao tem ad group classico — tem **asset groups** com signals.

### 1.3 Match types em Search (2026)

| Match | Sintaxe | Comportamento 2026 |
|-------|---------|---------------------|
| **Broad** | `aluguel apartamento` | Padrao recomendado pelo Google quando combinado com Smart Bidding. Inclui sinonimos, queries relacionadas, intent semantico. |
| **Phrase** | `"aluguel apartamento"` | Frase precisa ou variacoes proximas; perdeu rigidez em 2021. |
| **Exact** | `[aluguel apartamento]` | Intent exato + variacoes proximas (close variants). Nao e mais "literal". |
| **Negative** | `-gratis` (broad neg), `"-gratis"` (phrase neg), `[-gratis]` (exact neg) | Critico para limpar trafego. |

> **Mudanca 2021-2026:** Google unificou close variants em todos os match types. Hoje Broad + Smart Bidding tem performance equivalente ou superior a Exact + Manual em ~70% dos cenarios com volume suficiente.

### 1.4 Sinais de qualidade da estrutura

- Campanha por **objetivo + tipo + geo + idioma** (nao por produto).
- Ad group por **tema/intencao** (nao por keyword unica — SKAGs morreram em 2021).
- Pelo menos **3 RSAs por ad group** com Ad Strength Good/Excellent.
- Negative keyword list compartilhada entre campanhas.
- Conversion actions bem definidas com **valor monetario** (nao so flag boolean).

---

## Fundacao 2 — Performance Max + Smart Bidding (Pmax + tROAS/tCPA)

### 2.1 Performance Max — o que e

Pmax e o tipo de campanha lancado em 2021 que **unifica todos os inventarios Google em uma so campanha** (Search, Display, YouTube, Gmail, Maps, Discover) e deixa o algoritmo decidir onde aparecer, com qual criativo e quanto pagar — o anunciante define apenas:

- **Objetivo** (conversoes ou valor de conversao)
- **Orcamento**
- **Bidding** (Maximize Conversions, Maximize Conversion Value, tCPA, tROAS)
- **Asset group** (assets criativos)
- **Audience signals** (sinais — NAO targeting estrito; o algoritmo usa como hint)
- **Geo + idioma**

### 2.2 Posicao em 2026

- **62% de todos os cliques Google Ads** em 2026 vem de Pmax (Google Ads Blog, fev/2026).
- **82% das contas** ativas rodam ao menos 1 Pmax (vs 8% em 2022).
- E-commerce com feed -> Pmax e **default** desde 2024.

### 2.3 Smart Bidding — estrategias

| Estrategia | Otimiza para | Quando usar | Conversoes/mes minimas |
|------------|--------------|-------------|------------------------|
| **Maximize Clicks** | Volume de cliques | Cold start, sem dado de conversao | 0 |
| **Maximize Conversions** | Volume de conversoes (sem CPA fixo) | Inicio com pixel ativo | 15+ |
| **tCPA (Target CPA)** | Custo por acao alvo | CPA estavel, conversoes binarias | 30-50+ |
| **Maximize Conversion Value** | Valor total de conversao | Tem valores diferentes por conversao | 30+ |
| **tROAS (Target ROAS)** | Retorno sobre investimento alvo | E-commerce com revenue tracking | 50-100+ |
| **Manual CPC** | Lance manual | Legado / brand defense / teste | (qualquer) |

### 2.4 tROAS vs tCPA — a virada de 2026

> **2024 -> 2026: a virada de default.**
> Em 2024, tCPA era a estrategia recomendada para a maioria das contas. Em 2026, **tROAS virou preferida** para qualquer conta com dados de valor de conversao (revenue, order value, lead score).

- **tCPA** otimiza para encontrar conversoes a um **custo fixo** — nao distingue entre conversao de R$ 50 e R$ 5.000.
- **tROAS** otimiza para **retorno sobre investimento** — prioriza conversoes de alto valor mesmo que custem mais por clique.

> **Performance:** advertisers em tROAS ganharam ~38% mais ROAS vs Manual CPC em benchmarks Q1/2026 cross-industria.

### 2.5 Learning period — regras de ouro

- **Runway minimo:** 3 semanas (21 dias) sem mudancas estruturais antes de avaliar Smart Bidding.
- **Threshold de conversoes:** 30 conversoes em 30 dias para tCPA, 50+ para tROAS.
- **Mudanca de target:** maximo +/-15% por vez. Mudanca brusca reseta o learning.
- **Pausa = reset.** Nao pausar campanha em learning.

### 2.6 Audience signals em Pmax

Signals **NAO sao targeting** — sao hints para acelerar o learning. O algoritmo pode (e vai) sair desses signals se encontrar conversao melhor fora.

| Signal type | Como criar |
|-------------|-----------|
| **Custom segments** | Search terms + URLs de concorrentes + apps |
| **Your data** | Customer Match (lista de clientes hashed) + remarketing |
| **Interests & detailed demographics** | In-market + affinity + life events |
| **Demographics** | Idade + genero + parental + income |

> **Cristal C2 — Pmax sem signals e cego.** Lancar Pmax sem signals em conta nova (sem historico) custa 4-8 semanas de learning e ate 60% mais CPA.

### 2.7 Anti-patterns Pmax

- Brand keywords dentro de Pmax — canibaliza Search brand. Use **brand exclusion list** ou rode Search brand separada.
- Asset group unico para 50 produtos diferentes — perde granularidade. Crie asset groups por categoria.
- Conversion actions nao valoradas — Pmax otimiza para "qualquer conversao" e busca a mais barata (geralmente proxy ruim).
- Pausar Pmax durante learning — reset.

---

## Fundacao 3 — Search Ads + RSA + Quality Score

### 3.1 Responsive Search Ads (RSA) — unico formato Search desde 2022

RSA e o formato unico de Search desde junho/2022 (ETAs foram descontinuados). O anunciante fornece:

- **Ate 15 headlines** (30 caracteres cada)
- **Ate 4 descriptions** (90 caracteres cada)
- Google **mistura e combina** em runtime conforme a query, dispositivo e contexto.

### 3.2 Anatomia RSA otima

```
HEADLINES (15)
  - 3 contendo a keyword principal (pinned position 1 opcional)
  - 3 contendo USP/diferencial
  - 3 contendo prova social/numero
  - 3 contendo CTA verbal
  - 3 contendo objecao/medo respondido
DESCRIPTIONS (4)
  - 1 problema/dor
  - 1 solucao/beneficio
  - 1 prova/garantia
  - 1 CTA + urgencia
```

### 3.3 Pinning — quando usar

Pin (fixar posicao 1, 2 ou 3) reduz combinacoes possiveis e geralmente **piora Ad Strength**. Use apenas para:

- Compliance (juridico, financeiro, saude — texto obrigatorio)
- Brand consistency (sempre comecar com nome da marca)
- Disclaimer regulatorio

### 3.4 Quality Score 1-10

Quality Score (QS) e calculado por keyword e tem 3 componentes visiveis:

| Componente | Peso aproximado | Como melhorar |
|-----------|-----------------|---------------|
| **Expected CTR** | ~40% | Headlines relevantes, USP, CTA forte |
| **Ad Relevance** | ~30% | Keyword no headline + description, semantica |
| **Landing Page Experience** | ~30% | Velocidade (Core Web Vitals), conteudo da query, mobile, HTTPS |

### 3.5 Impacto economico do QS

- **QS 10/10:** CPC ate **-50%** vs media do leilao
- **QS 7-9:** CPC neutro a -25%
- **QS 5-6:** CPC neutro a +25%
- **QS 1-4:** CPC ate **+400%**

> **Cristal C3 — QS e multiplicador de orcamento.** Subir QS de 5 -> 8 nao melhora 60% — pode dobrar volume com mesmo orcamento.

### 3.6 Ad Strength

Ad Strength (Poor / Average / Good / Excellent) e o **score do RSA** (nao da keyword). Subir de Poor para Excellent traz **~15% mais cliques e conversoes** em media.

> Atencao: Ad Strength nao tem correlacao direta 1:1 com CTR/CVR/QS — e **hint de variedade**, nao de qualidade absoluta. RSAs Excellent nem sempre vencem.

### 3.7 Relative CTR (novidade 2026)

Em 2026 Google introduziu **Relative CTR** como sinal de QS — compara seu CTR ao CTR medio das outras posicoes na mesma SERP. Se a media e 2% e voce tem 4%, sua eCTR fica "Above Average".

### 3.8 Landing Page Experience + Core Web Vitals

Em 2026, **Core Web Vitals (LCP, INP, CLS)** sao input direto no Landing Page Experience. Site lento (LCP > 2.5s, INP > 200ms) **nao consegue QS 10**.

> Cruzar com `seo-tecnico` para tuning CWV.

---

## Fundacao 4 — YouTube Ads + Demand Gen

### 4.1 Formatos de video em 2026

| Formato | Duracao | Skip | Inventario | Uso |
|---------|---------|------|-----------|-----|
| **Skippable in-stream (TrueView)** | 15-180s | Sim (apos 5s) | Pre/mid/post-roll | Action + consideration |
| **Non-skippable in-stream** | ate 15s | Nao | Pre-roll | Awareness |
| **Bumper** | ate 6s | Nao | Pre-roll | Reach + frequencia |
| **In-feed (antes Discovery)** | qualquer | n/a | Home/search YouTube | Consideration |
| **Masthead** | ate 30s | Nao | Home YouTube (premium) | Awareness brand |
| **Shorts ads** | 9:16 vertical, < 60s | Nao (no feed) | Shorts feed | Action + reach jovem |

### 4.2 Demand Gen — substituto de Discovery (2024+)

Demand Gen (lancado 2024) substituiu Discovery Ads e agrega:

- YouTube in-feed
- YouTube Shorts feed
- Google Discover
- Gmail promocoes

Otimiza para **conversoes ou cliques no site**, nao apenas views. Default visual (image + video).

### 4.3 ABCDs do criativo (Google framework)

- **A** — Attract: capturar atencao em 5s (face, movimento, cor, audio)
- **B** — Brand: marca presente desde inicio (logo, nome, voiceover)
- **C** — Connect: emocao + storytelling
- **D** — Direct: CTA claro (visite, compre, cadastre)

### 4.4 Best practices Shorts ads (2026)

- **Aspect ratio 9:16 nativo** — vertical, nao landscape com black bars.
- **Hook em 2-3 segundos** — Shorts viewers decidem swipe em <3s.
- **Som ativo** — som (musica, voiceover) aumenta conversao em 20%+ vs muted.
- **UGC-style** — handheld, first-person, edicao minima — outperforma producao polida.
- **< 60s** — alinha com comportamento Shorts.
- **Brand presente cedo** — nao deixar para o ultimo segundo.
- **20-30% do orcamento YouTube em Shorts** se publico < 35 anos.

### 4.5 Performance comparativa

- Vertical 9:16 nativo: **+10-20% conversoes/dolar** vs landscape em Shorts.
- Native-feel UGC: ate **3x completion rate** vs repurposed ads tradicionais.

### 4.6 TrueView for Action / Video Action Campaigns (VAC)

VAC sao campanhas YouTube otimizadas para conversao (nao views). Em 2026 a maioria de VAC esta sendo absorvida por **Demand Gen** ou **Performance Max**.

### 4.7 Targeting YouTube

| Tipo | Exemplo |
|------|---------|
| **Demographic** | Idade, genero, parental, household income |
| **Interests** | Affinity, custom affinity, in-market, life events |
| **Topics** | Categorias YouTube |
| **Placements** | Canais, videos, apps especificos |
| **Custom segments** | Search history + URLs + apps |
| **Remarketing** | Visitantes site, viewers anteriores, customer list |

### 4.8 Frequencia + brand lift

Frequencia ideal: **3-5 impressoes/usuario/semana** para awareness; **1-2/semana** para action. Acima disso, ad fatigue + waste.

---

## Fundacao 5 — Audiences + Targeting (incluindo Customer Match + Similar Audiences)

### 5.1 Tipos de audiencia em 2026

| Categoria | Tipo | Como funciona |
|-----------|------|---------------|
| **Demographics** | Idade/genero/parental/income | Declarativo Google + inferido |
| **Affinity** | Categorias de interesse de longo prazo | Esportes, gastronomia, viagens |
| **In-Market** | Pesquisando ativamente comprar (curto prazo) | Carro, escola, software |
| **Life Events** | Mudanca, casamento, formatura, novo trabalho | YouTube + Search + Gmail |
| **Custom Segments** | Voce define keywords + URLs + apps que descrevem o publico | Custom flexivel |
| **Customer Match** | Lista de clientes hashed (email/telefone/endereco) | First-party data |
| **Remarketing (Google Ads)** | Visitantes site, app users, video viewers | Pixel + Customer Match |
| **Similar Audiences** | Lookalike de seed audience | **DEPRECATED em mai/2023** |
| **Detailed Demographics** | Educacao, parental status, casa propria, marital | Inferido |
| **Combined Audiences** | AND/OR/NOT entre as acima | Refinamento |

### 5.2 Similar Audiences — fim em 2023

> **Atencao:** Similar Audiences foi descontinuado em **maio/2023**. O substituto e **Optimized Targeting** (em Display/Video) e **audience signals** em Pmax — ambos automatizados.

### 5.3 Customer Match — first-party data

Customer Match e a **arma de privacy-first 2026**. Voce sobe lista de clientes (hashed via SHA-256: email, telefone, endereco) e Google matcha com usuarios logados.

**Match rates tipicos 2026:**
- Email: 40-60% (caia para 30% sem Consent Mode v2)
- Telefone: 30-50%
- Combo: 50-70%

**Casos de uso:**
- Targeting clientes ativos (upsell/cross-sell)
- Exclusao de clientes (acquisition only)
- Suppression de churn em remarketing
- Seed para custom segments

**LGPD/GDPR:** lista deve ter **base legal** (consentimento ou legitimo interesse documentado). Sem base legal -> infracao.

### 5.4 Optimized Targeting (substituto de Similar)

Em Display/Video/Demand Gen/Pmax, **Optimized Targeting** expande automaticamente alem da audience selecionada para encontrar conversoes similares. E AI-driven, nao exige seed audience explicita.

> **Anti-pattern:** desligar Optimized Targeting "para ter controle" geralmente reduz volume em 30-50% sem ganho proporcional de qualidade.

### 5.5 Anti-patterns de audience

- Audiencias muito estreitas (< 100k usuarios) em Display/YouTube — algoritmo nao tem espaco para learn.
- Sobrepor Affinity + In-Market + Custom + Demographic em AND — colapsa volume.
- Customer Match sem refresh > 90 dias — match rate cai 40%+.
- Customer Match sem Consent Mode v2 -> match rate cai 30-50% em 2026.
- Remarketing list sem segmentacao por funil (visitantes home + carrinho abandonado + clientes na mesma lista).

---

## Fundacao 6 — Brasil 2026 (LGPD + Consent Mode v2 + GA4 + cases)

### 6.1 LGPD em Google Ads

LGPD (Lei 13.709/2018) entrou em vigor em **16-ago-2020** e regula tratamento de dados pessoais de residentes no Brasil. Para Google Ads:

- **Bases legais:** consentimento, legitimo interesse, execucao de contrato, etc.
- **Direitos do titular:** acesso, correcao, exclusao, portabilidade, oposicao.
- **Encarregado (DPO):** obrigatorio para empresas que tratam dados em escala.
- **ANPD (Autoridade Nacional):** reguladora.
- **Multas:** ate 2% do faturamento, limitado a R$ 50 milhoes por infracao.

### 6.2 Consent Mode v2 — virada de 15-jun-2026

A maior mudanca de governance de dados em 2026 acontece em **15-jun-2026**:

- **ad_storage** (Consent Mode v2 dentro do Google Ads) vira **autoridade unica** sobre coleta de dados publicitarios.
- **Google Signals** (em GA4) **deixa de co-controlar** ads collection.
- Quando `ad_storage = denied`: Google Ads tags nao leem/escrevem cookies de ads (`_gcl_au`), nao coletam device IDs, nao linkam sessao a Google account, nao passam visitor-level data para Ads.

### 6.3 Estado dos cookies 3p em 2026

- **jul/2024:** Google **abandonou** a deprecation forcada de 3p cookies em Chrome.
- **2025-2026:** Chrome migrou para **user-choice** (Privacy & Security settings) — usuario decide individualmente.
- **Tendencia:** ~30-40% dos usuarios Chrome optam por bloquear 3p cookies em 2026.
- **Safari/Firefox:** ja bloqueiam 3p cookies por default ha anos.

### 6.4 Enhanced Conversions — first-party + hashing

Enhanced Conversions e a **maior mudanca de mensuracao 2024-2026**. Funciona assim:

1. Usuario converte no site (preenche email + telefone no checkout/lead form).
2. Google Ads tag captura esses campos no client-side, **hash SHA-256 antes de enviar**.
3. Hash e enviado para Google junto com o evento de conversao.
4. Google matcha com sua user base logada e atribui conversoes que seriam perdidas (cross-device, cookies bloqueados, ITP).

**Resultado tipico:** **+5% a +15% de conversoes reportadas** apos implementacao.

> **Cristal C6 — sem Enhanced Conversions, voce esta cego em 2026.** Match rate de Customer Match + atribuicao Smart Bidding caem 20-40% sem Enhanced Conversions.

### 6.5 Implementacao Enhanced Conversions

Tres opcoes:
1. **Google Tag Manager + Variable Enhanced Conversions** — recomendado, manutenivel.
2. **gtag.js manual** — direto no codigo, mais controle.
3. **Google Ads API** — server-side, ideal para offline conversions.

### 6.6 GA4 + Google Ads — integracao em 2026

- **Recomendacao 2026:** usar **Google Ads native tag** como fonte primaria de conversao para Smart Bidding; **GA4 key events** para analytics, audience building e cross-channel reporting.
- Conversoes importadas de GA4 sao validas, mas tem **latencia 24-48h** e podem perder conversoes em Consent Mode denied.
- **Atribution model:** GA4 default 2026 e **data-driven** (DDA); ultimo clique e legado.

### 6.7 Cases Brasil 2026

> Cases publicos disponiveis em Think with Google Brasil + Google Ads case studies. Nao reproduzimos numeros sem fonte primaria. Categorias com cases publicados:

- **E-commerce:** Magazine Luiza, Americanas, Mercado Livre, Amaro, Riachuelo.
- **Bancos/fintech:** Nubank, Itau, Inter, C6.
- **Telecom:** Vivo, TIM, Claro.
- **Educacao:** Ambev, Hotmart, Kroton.
- **Mobilidade:** iFood, 99, Uber Eats.
- **Streaming:** Globoplay, Netflix BR.

> Para citar case, **sempre referenciar fonte primaria** (Think with Google). Numeros sem fonte = nao usar.

### 6.8 CPC Brasil tipico (BRL) — disclaimer

Benchmarks Brasil em BRL variam fortemente por:
- Industria (juridico R$ 8-25 vs e-commerce R$ 0.50-3)
- Geo (SP/RJ premium vs interior)
- Sazonalidade (Black Friday +60%, jul-ago baixa)
- Quality Score do anunciante

> **Nao publicar benchmark BR especifico nesta skill** — varia demais e desatualiza rapido. Linkar fontes vivas: [WordStream Google Ads Benchmarks](https://www.wordstream.com/blog/2025-google-ads-benchmarks), [Triple Whale](https://www.triplewhale.com/blog/google-ads-benchmarks).

### 6.9 Portugues + keywords

- **Acentuacao:** Google Search trata "ADVOGADO" e "ADVOGADO" com acento como variantes proximas (close variants); ambos cobertos por exact match em 2026.
- **Stopwords:** "de", "para", "em" sao removidas de match logic; nao perder espaco em headline com elas.
- **Regional:** "celular" (BR) vs "telemovel" (PT) — separar campanhas por mercado.
- **Genero:** "advogado" e "advogada" sao matches proximos mas anuncio gendered tem CTR diferente — A/B testar.

---

## Fundacao 7 — Mensuracao + Tools 2026

### 7.1 Stack de mensuracao

| Camada | Ferramenta | Funcao |
|--------|-----------|--------|
| **Tag mgmt** | Google Tag Manager (GTM) | Deploy de tags |
| **Conversion tracking** | Google Ads tag + Enhanced Conversions | Smart Bidding fuel |
| **Analytics** | GA4 | Cross-channel, audiences, attribution |
| **Search organic** | Google Search Console | Query data, indexabilidade |
| **Reporting** | Looker Studio (ex-Data Studio) | Dashboards |
| **Server-side** | GA4 server-side + Tag Manager Server-side | First-party + privacy |
| **Offline** | Google Ads API (offline conversion import) | Lead -> venda fechada |

### 7.2 Atribuicao em 2026

GA4 padrao **data-driven attribution (DDA)** desde 2023. Modelos legados (last click, first click, linear, time decay, position-based) ainda existem em **comparison tools** mas nao em reports default.

> Em Google Ads, modelo de atribuicao usado por Smart Bidding e DDA. Nao tente forcar last-click em 2026.

### 7.3 Cross-device + Consent Mode

Cross-device tracking depende de:
1. Usuario logado em conta Google
2. Consent Mode v2 com `ad_storage = granted`
3. Enhanced Conversions ativos

Sem 1+2+3, atribuicao cross-device cai a praticamente zero.

### 7.4 Benchmarks 2026 (cross-industry)

> **Disclaimer:** numeros abaixo sao agregados de fontes publicas (WordStream, Triple Whale, Store Growers, AGrowth) e variam por industria/geo/conta. Usar como ordem de grandeza, nao como meta absoluta.

| Metrica | Search avg 2026 | Display avg 2026 | YouTube avg 2026 |
|---------|----------------|-------------------|-------------------|
| **CTR** | ~3.17% | ~0.5-0.8% | ~0.65% (in-stream skip) |
| **CPC** | USD 2.96 (Q1/26, +12% YoY) | USD 0.50-1 | n/a (CPV) |
| **CPM** | n/a | USD 12.79 (med, +10% YoY) | USD 5-15 |
| **CVR** | 3-7% (B2C), 1-3% (B2B) | 0.5-1% | 1-3% (action) |
| **CPA** | USD 53.89 (avg cross-industry, +6% YoY) | varia muito | varia |

**Por industria (Search CPC USD 2026):**
- Legal services: ~USD 6.75 (mais caro)
- Insurance, B2B services: USD 4-6
- Tech: CPA medio USD 133 (mais alto)
- E-commerce: ~USD 1.16
- Auto: CPA medio ~USD 33 (mais baixo)

**ROAS targets tipicos 2026:**
- E-commerce mass: 4-6x
- E-commerce premium: 6-10x
- B2B SaaS: 2-3x (LTV maior compensa)
- D2C: 3-5x
- Servicos local: 3-5x

### 7.5 KPIs operacionais (alem de CPA/ROAS)

- **Search Impression Share (IS)** — % de impressoes capturadas vs disponivel.
- **IS lost to budget** — quanto orcamento te impediu de aparecer.
- **IS lost to rank** — quanto Quality Score + lance te impediram.
- **Top IS** — share entre top 3 posicoes.
- **Absolute top IS** — share da posicao 1.
- **Auction insights** — concorrentes no leilao + share deles.
- **Search terms report** — queries reais que dispararam seu anuncio.

### 7.6 AI-powered bidding adoption

Em 2026, **78% do gasto Google Ads** flui via AI bidding (Smart Bidding completo). Anunciantes em AI bidding reportam **22% lower CPA** vs Manual CPC em media.

### 7.7 Looker Studio + reporting

- Conector nativo Google Ads + GA4.
- Templates publicos: Google Ads Overview, Performance Max Insights, Search Term Mining.
- Custom para CMO: ROAS / CPA / blended CAC / LTV / payback period.

---

## Fundacao 8 — Aplicacao em Content MKT (5 audiencias x Google Ads)

### 8.1 Performance marketers (in-house ou agencia)

- **Foco:** ROAS, CPA, IS, learning periods, budget pacing.
- **Stack diaria:** Google Ads UI + Editor + Search Terms report + Auction Insights + Looker Studio.
- **Decisoes recorrentes:** consolidacao de campanha (HSA -> menos campanhas, mais sinal), troca de bidding, asset rotation Pmax.
- **Conteudo:** SOPs internos, audit checklists, dashboard semanal.

### 8.2 CMO

- **Foco:** marketing-driven revenue, blended ROAS/CAC, payback period, share-of-search.
- **Decisoes recorrentes:** budget split Google vs Meta vs LinkedIn vs YouTube; aprovacao de Pmax (que tem menos transparencia); compliance LGPD.
- **Conteudo:** narrativa para board (eficiencia + brand), benchmarks vs concorrencia, plan vs actual.

### 8.3 Founders (early-stage SaaS / D2C)

- **Foco:** primeiros R$ a serem investidos em Google Ads, payback, learning curve.
- **Decisoes recorrentes:** Search vs Pmax como primeira campanha; quanto investir antes de pedir help de agencia.
- **Conteudo:** runbook de "primeiros 90 dias em Google Ads", milestones, red flags.

### 8.4 Agencias

- **Foco:** retainer client, escalabilidade, white-label reporting, processo replicavel.
- **Decisoes recorrentes:** estrutura MCC, naming convention, templates de RSA/asset group, escalation tree.
- **Conteudo:** case studies, propostas comerciais com benchmarks de industria, briefings de criativo padronizados.

### 8.5 Growth marketers / media buyers

- **Foco:** experimentation, holdouts, incrementality testing, MMM (marketing mix modeling).
- **Decisoes recorrentes:** geo holdout test para medir incrementalidade, conversion lift studies, brand lift YouTube.
- **Conteudo:** experiment logs, statistical readouts, incrementality reports.

---

## Anti-Patterns 18

1. **Lancar Pmax sem audience signals** em conta nova — 4-8 semanas de learning desperdicado, CPA +60%.
2. **Brand keywords dentro de Pmax** — canibaliza Search brand. Use brand exclusion.
3. **Pmax + Search brand simultaneos sem exclusao** — Pmax come o trafego barato e infla ROAS aparente.
4. **Manual CPC em 2026** — perde 22-38% de eficiencia vs Smart Bidding em conta com >30 conversoes/mes.
5. **tCPA em conta com revenue tracking** — deveria ser tROAS. tCPA otimiza para conversao barata, nao valiosa.
6. **Mudar target tCPA/tROAS em > 15% por vez** — reseta learning, 21 dias para reestabilizar.
7. **Pausar campanha em learning** — reset completo do modelo.
8. **Conversion actions sem valor monetario** — Smart Bidding otimiza para conversao errada (proxy barato).
9. **RSA com pinning agressivo** (3+ pins) — reduz combinacoes, derruba Ad Strength, reduz volume.
10. **Skipping Enhanced Conversions** em 2026 — perde 5-15% de conversoes reportadas, match rate Customer Match cai 30%.
11. **Customer Match sem refresh** > 90 dias — match rate cai 40%+.
12. **Similar Audiences em new build** — descontinuado mai/2023.
13. **Ignorar Consent Mode v2** apos 15-jun-2026 — cookies de ads bloqueados, atribuicao colapsa.
14. **Quality Score 1-4 sem audit** — CPC ate +400% acima da media.
15. **Landing page com LCP > 2.5s** — Quality Score teto 7-8, nunca 10.
16. **Match type Exact + Manual CPC obsessivo** — fluxo de 2018; perde ~30% de volume vs Broad + Smart Bidding em 2026.
17. **YouTube Shorts em 16:9 com black bars** — completion rate ate 3x menor vs 9:16 nativo.
18. **Asset group Pmax cobrindo 50 produtos heterogeneos** — algoritmo nao consegue inferir signal de qualidade; segmente por categoria.

---

## 18 Regras de Ouro

1. **Smart Bidding default em 2026.** Manual CPC apenas para brand defense ou teste A/B controlado.
2. **Pmax e default para e-commerce com feed.** Search ainda e default para B2B com demanda explicita.
3. **Sempre dar audience signals em Pmax.** Mesmo sendo "hint", aceleram learning em 4-8 semanas.
4. **tROAS > tCPA quando ha revenue tracking.** Otimize para valor, nao volume.
5. **Espere 3 semanas + 30-50 conversoes antes de avaliar Smart Bidding.** Learning periods sao reais.
6. **Mude target em incrementos < 15%.** Mudancas bruscas resetam learning.
7. **RSA: 15 headlines, 4 descriptions, Ad Strength Good/Excellent.** Sem pinning agressivo.
8. **Quality Score 8+ e meta operacional.** Subir QS 5 -> 8 dobra volume com mesmo budget.
9. **Landing page CWV LCP < 2.5s, INP < 200ms, CLS < 0.1.** Sem isso, QS teto = 7.
10. **Enhanced Conversions e nao-negociavel em 2026.** Match rate + Smart Bidding dependem disso.
11. **Consent Mode v2 implementado antes de 15-jun-2026.** Apos a virada, sem v2 = cego.
12. **Customer Match com refresh < 90 dias.** Match rate degrada rapido.
13. **YouTube Shorts em 9:16 nativo, hook em 2-3s, som ativo.** UGC-style outperforma producao polida.
14. **Brand exclusion list em Pmax.** Nao deixe Pmax canibalizar Search brand.
15. **Conversion actions com valor monetario sempre.** Mesmo que estimado.
16. **Atribuicao data-driven (DDA) e default.** Last-click e legado.
17. **Search terms report semanal.** Negative keywords sao manutencao continua, nao setup unico.
18. **LGPD + base legal documentada para Customer Match e remarketing.** Sem base legal -> infracao.

---

## Exemplos Comportamentais (4 personas)

### Persona 1 — Performance marketer in-house e-commerce moda

**Contexto:** moda D2C, R$ 250k/mes em Google Ads, ROAS atual 3.8x, meta 5x. Conta 80% Pmax + 20% Search brand.

**Diagnostico via skill:**
- Pmax sem brand exclusion -> canibaliza Search brand, infla ROAS Pmax aparente. Adicionar `brand exclusion list`.
- Bidding em Maximize Conversion Value sem target -> migrar para tROAS 5x com runway 3 semanas.
- Asset group unico cobrindo 12 categorias -> segmentar em 4 asset groups (vestidos, calcas, calcados, acessorios).
- Enhanced Conversions nao implementado -> ganho esperado +8-12% conversoes, +20-30% match rate.
- Audience signals em Pmax: customer match (clientes ativos 12 meses) + custom segment (concorrentes + categorias).

**Output esperado:** plano 30 dias com baseline atual, mudancas estruturais, runway de learning, KPIs semanais.

### Persona 2 — CMO SaaS B2B (mid-market)

**Contexto:** SaaS HR Tech, ticket medio R$ 8k/mes, ciclo 60 dias, R$ 180k/mes em ads (Google + LinkedIn + Meta), CAC blended R$ 14k, payback 9 meses.

**Diagnostico via skill:**
- Google Ads = 60% do budget, gerando 70% dos demos qualificados — eficiencia OK.
- Smart Bidding em tCPA R$ 800 — deveria migrar para Maximize Conversion Value com lead scoring (lead score x ticket projetado).
- Search Brand vs Search Generic split: 70/30. Meta deveria ser 50/50 com expansao em generic + concorrente.
- YouTube ausente — testar Demand Gen + bumper ads para topo de funil + remarketing -> Search.
- Atribuicao: cross-device + offline conversions (CRM Salesforce) integrar via Google Ads API offline import.
- Compliance LGPD: Customer Match com leads de fundo de funil (MQL/SQL) requer revisao de base legal.

**Output esperado:** narrativa board com plan de expansao topo de funil + integracao CRM + compliance LGPD revisada.

### Persona 3 — Founder early-stage D2C beleza

**Contexto:** marca de skincare clean, 8 meses de operacao, MRR R$ 80k, investe R$ 12k/mes em ads (50% Meta, 50% Google), ROAS 2.5x, sem agencia.

**Diagnostico via skill:**
- Conta nova com R$ 12k/mes -> 30-40 conversoes/mes -> Pmax sustentavel mas no limite. Search brand + Pmax e a estrutura ideal para early-stage.
- Bidding: comecar com Maximize Conversion Value (sem target) por 3 semanas para acumular dado, depois migrar para tROAS 3x.
- RSA: 2 RSAs por ad group, 15 headlines com 5 angulos diferentes (clean, eficacia, prova social, dermatologista-aprovado, sustentabilidade).
- Landing page: CWV LCP 3.2s -> meta 2.0s; rodar com `seo-tecnico` para tuning.
- Enhanced Conversions: prioridade 1 — implementar via GTM em 1 semana.
- YouTube Shorts: budget R$ 1k/mes em Demand Gen com criativo UGC (cliente real, vertical, 30s).

**Output esperado:** runbook 90 dias com milestones de gasto/aprendizado, red flags, momentos de chamar agencia.

### Persona 4 — Agencia gerenciando 30 clientes

**Contexto:** agencia mid-size, 30 clientes ativos em Google Ads, retainer R$ 6k-25k/mes, time de 8 paid media specialists.

**Diagnostico via skill:**
- Estrutura MCC com naming convention: `[CLIENTE]_[OBJETIVO]_[TIPO]_[GEO]_[IDIOMA]_[VARIANT]`.
- Templates padronizados: RSA template (15 headlines + 4 descriptions com placeholders), asset group Pmax template, negative keyword master list.
- Audit checklist quinzenal por conta: QS distribution, Ad Strength, search terms, IS, learning status, conversion accuracy.
- Reporting white-label Looker Studio com 4 vistas: Executive (CMO), Operational (paid media), Creative (designer), Compliance (LGPD/legal).
- Escalation tree: paid media -> account manager -> head paid -> CSO conforme severidade.
- Capacitacao continua: skill `conhecimento-google-ads` re-grounding mensal (volatility HIGH).

**Output esperado:** SOP completo + templates + reporting + onboarding novos analistas.

---

## Checklist Contraditorio Interno (10 perguntas)

Antes de fechar pecas formais, responder:

1. **Estou usando dado proprio ou estimando?** Pmax "62% dos cliques" tem fonte (Google Ads Blog fev/2026) — checei? Se nao, removo numero ou linko fonte primaria.
2. **Smart Bidding ou Manual CPC esta sendo recomendado por inercia ou por dado?** A conta tem >30 conversoes/mes para sustentar tCPA? > 50 para tROAS?
3. **Pmax esta canibalizando Search brand?** Brand exclusion configurada? Auction Insights confirma?
4. **Quality Score esta sendo medido por keyword (componente Search) ou estou misturando com Ad Strength (componente RSA)?** Sao coisas diferentes.
5. **Estou recomendando Similar Audiences?** Foi descontinuada mai/2023. Substituir por Optimized Targeting + audience signals.
6. **Enhanced Conversions esta na lista de prioridades?** Em 2026, sem isso, conta perde 5-15% de mensuracao + 20-40% de match rate Customer Match.
7. **Consent Mode v2 esta antes ou depois de 15-jun-2026?** A virada muda quem controla ad data — recomendacao deve refletir.
8. **Estou citando benchmark sem fonte?** WordStream/Triple Whale/Store Growers sao publicos; numeros sem link = nao publicar.
9. **Meu plano respeita learning periods (3 semanas, 30-50 conversoes)?** Mudancas semanais agressivas resetam Smart Bidding.
10. **Compliance LGPD esta no escopo?** Customer Match + remarketing exigem base legal. Anuncio de saude/financeiro tem regras CONAR/CDC adicionais — cruzar com `dominio-juridico-mkt` e `conhecimento-conar-cdc`.

---

## Referencias

### Documentacao oficial Google

- [Google Ads Help Center](https://support.google.com/google-ads)
- [Google Ads & Commerce Blog](https://blog.google/products/ads-commerce/)
- [Think with Google](https://www.thinkwithgoogle.com)
- [Think with Google Brasil](https://www.thinkwithgoogle.com/intl/pt-br/)
- [Google Ads Liaison (X)](https://x.com/adsliaison)
- [Google Search Status Dashboard](https://status.search.google.com)
- [Google Marketing Live](https://marketingplatform.google.com/about/marketing-live/)
- [About Target ROAS bidding](https://support.google.com/google-ads/answer/6268637)
- [Search Partner Network announcements](https://support.google.com/google-ads/answer/16286960)
- [About Responsive Search Ads](https://support.google.com/google-ads/answer/7684791)
- [YouTube Shorts ads specs and best practices](https://support.google.com/google-ads/answer/16041697)
- [Helping users comply with LGPD (Google Ads)](https://support.google.com/google-ads/answer/9943919)
- [Helping users comply with LGPD (Ad Manager)](https://support.google.com/admanager/answer/9894744)
- [Third-party cookie deprecation FAQ](https://support.google.com/google-ads/answer/14762010)
- [How brands use YouTube Shorts ads (Google Blog)](https://blog.google/products/ads-commerce/youtube-shorts-ads-select-lineups-abcds/)

### Performance Max + Smart Bidding

- [Google Ads in 2026: AI Max, Performance Max & Smart Bidding Changes](https://www.yellowjackmedia.com/google-ads-in-2026-how-ai-max-performance-max-and-smart-bidding-are-changing-ppc-forever/)
- [Smart Bidding 2026: Value Based Bidding Playbook (Brainmine)](https://www.brainminetech.com/blog/how-value-based-bidding-is-changing-the-way-google-ads-scales-profit-in-2026/)
- [tCPA and tROAS methodology (Dotidot)](https://www.dotidot.io/post/tcpa-troas-smarter-bidding-explained)
- [AI Google Ads Bidding: PMax Automation Strategy 2026 (Digital Applied)](https://www.digitalapplied.com/blog/ai-google-ads-bidding-automation-pmax-2026)
- [How Google Ads Auction Works: Complete 2026 Breakdown](https://www.digitalapplied.com/blog/how-google-ads-auction-works-complete-breakdown)
- [Google Ads Statistics 2026 (Pace Ads)](https://paceads.com/research/google-ads-statistics-2026)
- [Pros & Cons of Every Automated Bidding Strategy (WordStream)](https://www.wordstream.com/blog/google-ads-automated-bidding)
- [Google Ads Smart Bidding Delivers Results at Scale (Playhouse Digital)](https://playhouse.digital/resources/what-is-google-ads-smart-bidding)

### Search Ads + RSA + Quality Score

- [Responsive Search Ads (RSAs): 2026 Guide + 6 Best Practices (Growth Minded)](https://growthmindedmarketing.com/blog/responsive-search-ads/)
- [Google Ads Quality Score Guide 2026: Master the 1-10 Scale (Two Squares)](https://twosquares.co.uk/blog/google-ads-quality-score)
- [Google RSAs in 2024: Everything you need to know (Search Engine Land)](https://searchengineland.com/google-rsas-everything-you-need-to-know-440449)
- [Responsive Search Ads: The Ultimate Guide 2026 (Seize Marketing)](https://seizemarketingagency.com/responsive-search-ads/)
- [What Actually Drives RSA Performance (Optmyzr)](https://www.optmyzr.com/blog/google-rsa-performance-study/)
- [The Ultimate Guide to Responsive Search Ads (Optmyzr)](https://www.optmyzr.com/guide/responsive-search-ads/)
- [Does Ad Strength Impact Responsive Search Ads? (Optmyzr)](https://www.optmyzr.com/blog/ad-strength-responsive-search-ads/)
- [Responsive Search Ads Best Practices Guide 2026 (Scalix AI)](https://scalixai.com/blog/responsive-search-ads)

### YouTube + Demand Gen

- [YouTube Ads 2026: Video Advertising Strategy Guide (Digital Applied)](https://www.digitalapplied.com/blog/youtube-ads-2026-video-advertising-strategy-guide)
- [YouTube Ads in 2026: Complete Strategy Guide (Groas)](https://groas.ai/post/youtube-ads-strategy-2026-complete-guide-formats-targeting-rules)
- [Innovative YouTube Ad Formats for 2026 (Marketing Agent)](https://marketingagent.blog/2026/02/24/innovative-youtube-ad-formats-for-2026-beyond-skippable-ads-new-business-opportunities/)
- [YouTube Ads: How to Create Video Ads That Convert in 2026 (Creatify)](https://creatify.ai/blog/youtube-ads-how-to-create-video-ads-that-convert-in-2026)
- [YouTube Ads Best Practices for SaaS & B2B in 2026 (Aimers)](https://aimers.io/blog/youtube-ads-best-practices)
- [YouTube Ads in 2026: Formats, Targeting (Tiberius Digital)](https://www.tiberius.co.nz/wiki/youtube-advertising-video-ads-strategy)
- [YouTube AI Video Ads Guide 2026 (VirVid)](https://virvid.ai/blog/youtube-ai-video-ads-guide-2026-shorts-instream-formats)
- [YouTube Video Ad Specs & Placements Guide 2026 (QuickFrame)](https://quickframe.mountain.com/blog/youtube-video-ad-specs/)

### Benchmarks + Industria

- [Google Ads Benchmarks by Industry (Triple Whale)](https://www.triplewhale.com/blog/google-ads-benchmarks)
- [Google Ads Performance Benchmarks 2026 (White Label Agency)](https://www.whitelabelagency.co/post/google-ads-benchmarks-in-2026-ctr-cpc-conversion-rates-by-industry)
- [Google Ads Benchmarks 2026: CPC, CTR, CVR by Industry (Digital Applied)](https://www.digitalapplied.com/blog/google-ads-benchmarks-2026-cpc-ctr-cvr-industry)
- [2026 Google Ads Benchmarks: Average CPC, CTR, CPA & CVR (UpRoas)](https://www.uproas.io/blog/google-ads-benchmarks)
- [Google Ads Cost Benchmarks by Industry 2026 (Get-Ryze)](https://www.get-ryze.ai/blog/google-ads-cost-benchmarks-by-industry-2026)
- [27 Google Ads Benchmarks 2026 (Store Growers)](https://www.storegrowers.com/google-ads-benchmarks/)
- [Google Ads Benchmarks 2026: Key Metrics (AGrowth)](https://agrowth.io/blogs/google-ads/google-ads-benchmarks)
- [Google Ads benchmarks by industry in 2026 (Usermaven)](https://usermaven.com/blog/google-ads-benchmarks)
- [Google Ads Benchmarks 2025 (WordStream)](https://www.wordstream.com/blog/2025-google-ads-benchmarks)

### LGPD + GA4 + Enhanced Conversions

- [Google Ads Conversion Tracking Setup 2026 (Groas)](https://groas.ai/post/google-ads-conversion-tracking-setup-2026-the-complete-guide-ga4-enhanced-conversions-consent-mode)
- [Google Data Transmission Controls Guide 2026 (ALM Corp)](https://almcorp.com/blog/google-data-transmission-controls-complete-guide/)
- [Google Ads Conversion Tracking 2026: GA4 + Enhanced (Groas)](https://groas.ai/post/google-ads-conversion-tracking-ga4-enhanced-conversions-audit-guide-2026)
- [How to track conversions with Google Ads and GA4 2026 (Amrudin Catic)](https://www.amrudincatic.com/google-ads-ga4-conversion-tracking-2026/)
- [Complete Guide to Enhanced Conversions in Google Ads 2026 (Lever Digital)](https://www.leverdigital.co.uk/guides/the-complete-guide-to-enhanced-conversions-in-google-ads)
- [Guide to Enhanced Conversions Google Ads 2026 (Trackingplan)](https://webflow.trackingplan.com/blog/enhanced-conversions-google-ads)
- [Google Ads Trends 2026 (Sharp Innovations)](https://www.sharpinnovations.com/blog/2025/11/google-ads-trends-and-technologies-2026/)
- [GA4 Update April 2026 — What Changed (Groas)](https://groas.ai/post/ga4-update-april-2026-what-changed-google-ads-conversion-tracking-fix)

### Consent Mode v2 + Cookies

- [Google Consent Mode June 2026 Update (UniConsent)](https://www.uniconsent.com/blog/google-ads-consent-mode-change-2026)
- [Global Cookie Consent Trends 2026 (Secure Privacy)](https://secureprivacy.ai/blog/global-cookie-consent-trends-2026)
- [Third-Party Cookie Deprecation: 2026 Guide (Ethyca)](https://www.ethyca.com/guides/third-party-cookie-deprecation-here-s-what-privacy-teams-need-to-know)
- [Google strips Analytics of ad data authority June 2026 (PPC Land)](https://ppc.land/google-strips-analytics-of-ad-data-authority-in-june-2026-consent-overhaul/)
- [The New Future of Cookies (Cookie-Script)](https://cookie-script.com/news/new-future-of-cookies-user-choice-vs-browser-deprecation)
- [Third-Party Cookies in 2026 (Studio Stray)](https://studiostray.com/insights/third-party-cookies-2026-what-changed)
- [Google Ads Tracking After Consent Mode V2 (Dataslayer)](https://www.dataslayer.ai/blog/track-google-ads-after-consent-mode-v2-2025-guide)
- [Google's keeps Third-Party Cookies alive (Jentis)](https://www.jentis.com/blog/google-will-not-deprecate-third-party-cookies)
- [GA4 and Google Ads Consent Controls Split June 2026 (ALM Corp)](https://almcorp.com/blog/ga4-google-ads-consent-controls-split-june-2026/)

### Brasil — regulatorio

- [ANPD — Autoridade Nacional de Protecao de Dados](https://www.gov.br/anpd/pt-br)
- [LGPD — Lei 13.709/2018](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm)
- [CONAR — Conselho de Auto-Regulamentacao Publicitaria](https://www.conar.org.br)
- [Codigo de Defesa do Consumidor (CDC)](https://www.planalto.gov.br/ccivil_03/leis/l8078compilado.htm)

### Comunidade + Imprensa especializada

- [Search Engine Land — PPC channel](https://searchengineland.com/library/channel/ppc)
- [Search Engine Journal — PPC](https://www.searchenginejournal.com/category/pay-per-click/)
- [PPC Land](https://ppc.land)
- [PPC Hero](https://www.ppchero.com)
- [WordStream Blog](https://www.wordstream.com/blog)

---

## Cross-Skill References

- **`conhecimento-meta-ads`** (sister no bloco Conhecimento de Plataforma) — para split de orcamento Google vs Meta + atribuicao incremental.
- **`conhecimento-linkedin-ads`** (sister) — B2B mid-funnel + ABM complementar a Google Search B2B.
- **`conhecimento-ga4`** — mensuracao downstream de tudo que Google Ads gera; integracao tag + DDA + audience export.
- **`conhecimento-search-console`** — organic search complementar; queries do Search Console alimentam negative keywords + custom segments.
- **`conhecimento-conar-cdc`** (sister) — compliance publicidade BR; obrigatorio para anuncios em saude, financeiro, juridico, infanto-juvenil, alcool, alimentos.
- **`seo-tecnico`** — Quality Score depende de Core Web Vitals + landing page experience; tuning CWV reduz CPC ate 50%.
- **`seo-fundamentos`** — pipeline crawl/render/index/rank afeta landing page indexada + Brand SERP.
- **`seo-keywords`** — keyword research compartilhado entre SEO e Search Ads (negative kw mining + intent mapping).
- **`metricas-marketing`** — ROAS, CAC, LTV, payback period; framework para meta de tROAS.
- **`funil-jornada`** — mapping campanha por estagio (awareness/consideration/conversion/retention -> Demand Gen/YouTube/Search/Customer Match).
- **`copywriting-conversao`** — RSA headlines/descriptions, USP, CTA, prova social, gatilhos eticos.
- **`persona-icp-deep`** — definicao de Custom Segments + Customer Match + audience signals Pmax.
- **`dominio-juridico-mkt`** — base legal LGPD para Customer Match e remarketing; compliance publicidade juridica (OAB).
- **`dominio-financeiro-mkt`** — orcamento, payback period, modelagem ROAS x CAC x LTV.

---

## Integracao Ecossistema Frank-MKT

A skill `conhecimento-google-ads` ocupa a 2a posicao do **Bloco Conhecimento de Plataforma** (apos `conhecimento-meta-ads`). Ela e:

- **Pre-requisito** para qualquer peca formal envolvendo Google Ads (planejamento de campanha, audit, briefing de criativo, plano de mensuracao).
- **Pos-requisito** de skills de funil e estrategia: `funil-jornada`, `persona-icp-deep`, `metricas-marketing`, `posicionamento-marca` definem o "porque", esta skill define o "como" em Google Ads.
- **Cross-skill obrigatorio** em projetos B2B (com `conhecimento-linkedin-ads`), em projetos com KPIs de revenue (com `conhecimento-ga4`), em projetos brasileiros (com `conhecimento-conar-cdc` + `dominio-juridico-mkt` para LGPD).

**Posicao no fluxo Frank-MKT:**

```
[Estrategia] persona-icp-deep + posicionamento-marca + funil-jornada + metricas-marketing
                                    |
                                    V
[Conhecimento Plataforma] conhecimento-meta-ads + conhecimento-google-ads + conhecimento-linkedin-ads + ...
                                    |
                                    V
[Execucao] copywriting-conversao + redacao-publicitaria + composicao-visual + criativo
                                    |
                                    V
[Mensuracao] conhecimento-ga4 + conhecimento-search-console + metricas-marketing
                                    |
                                    V
[Compliance] conhecimento-conar-cdc + dominio-juridico-mkt + dominio-financeiro-mkt
```

**Reground HIGH (3m):** dado o volatility, esta skill deve ser re-grounded a cada 90 dias com fontes vivas listadas em `regrounding_sources` e Referencias.

---

> **Disclaimer educational.** Esta skill e material educacional e operacional, nao parecer juridico nem consultoria contabil. Decisoes sobre LGPD, base legal, contratos com Google e demais terceiros, e regulamentacao setorial (CONAR, ANATEL, BACEN, ANVISA, OAB, CFM) devem passar por profissionais habilitados. Numeros, benchmarks e politicas de produto Google citados aqui derivam de fontes publicas datadas em 2026 e mudam sem aviso. Re-grounding obrigatorio antes de pecas formais. ASCII PT-BR, sem acentos. Pertence ao plugin frank-mkt (Claude Code).
