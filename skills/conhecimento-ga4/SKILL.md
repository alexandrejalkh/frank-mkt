---
name: conhecimento-ga4
description: Conhecimento Google Analytics 4 (GA4) 2026 (event-based model substituindo session-based UA Jul-2023 + Engagement metrics + Explorations + Audiences + Conversions Key Events + BigQuery export gratis + Looker Studio + Consent Mode v2 + first-party data + GTM Tag Manager + sGTM server-side) para analysts/CMO/founders/devs/agencias, com cobertura migracao mandatory UA->GA4 Jul-2023 + 14 meses retention default + 4 default channels modelo + Conversions agora "Key Events" + cross-domain tracking + LGPD compliance Brasil. 4a SKILL Bloco Conhecimento de Plataforma.
volatility: high
last_review: 2026-05-09
next_review: 2026-08-09
languages: [pt-BR]
audience: [data-analysts, CMO, founders, devs, agencias, growth-marketers, performance-marketers]
ascii_only: true
regrounding_sources:
  - "https://support.google.com/analytics"
  - "https://developers.google.com/analytics"
  - "https://developers.google.com/analytics/devguides/collection/ga4"
  - "https://support.google.com/analytics/answer/9304153"
  - "https://support.google.com/analytics/answer/10089681"
  - "https://developers.google.com/tag-platform/tag-manager/server-side"
  - "https://support.google.com/tagmanager"
  - "https://lookerstudio.google.com"
  - "https://cloud.google.com/bigquery"
  - "https://developers.google.com/tag-platform/security/guides/consent"
---

# Skill: conhecimento-ga4

> **Decaimento Temporal**
> Ultima verificacao: 2026-05-09 | Proxima revisao: 2026-08-09 | Volatility: **high** (3 meses)
> Google ajusta GA4 silenciosamente: novos events recomendados, deprecation de campos, mudancas em retention default, mudancas em Consent Mode (v2 mandatory desde Mar-2024 + TCF v2.3 mandatory 28-Fev-2026), Conversions->Key Events rename (2024), evolucao de Explorations, novos limites de BigQuery export. Re-validar TUDO antes de publicar peca formal:
> - Google Analytics Help Center — https://support.google.com/analytics
> - Google Analytics Developers — https://developers.google.com/analytics
> - GA4 Changelog — https://developers.google.com/analytics/devguides/collection/protocol/ga4/changelog
> - Google Tag Manager — https://support.google.com/tagmanager
> - Looker Studio — https://lookerstudio.google.com
> - Simo Ahava blog (ground-truth GTM/GA4) — https://www.simoahava.com
> - Google Analytics Blog — https://blog.google/products/marketingplatform/analytics
>
> **Acionamento:** auditoria GA4, migracao UA->GA4 (raros remanescentes), debug events, configurar Key Events, criar Audiences, planejar Explorations (funnel/path/segment overlap), exportar para BigQuery, montar Looker Studio dashboard, implantar Consent Mode v2 (LGPD/GDPR/TCF v2.3), evangelizar sGTM, ecommerce events tracking (view_item->purchase), benchmarks engagement rate, decisao "GA4 native vs Mixpanel/Amplitude vs Hotjar/FullStory".
> **Skills relacionadas:** `conhecimento-meta-ads` (sister), `conhecimento-google-ads` (sister, integracao Key Events->Google Ads import), `conhecimento-linkedin-ads` (sister), `conhecimento-search-console` (sister, GSC + GA4 integration), `conhecimento-conar-cdc` (sister, LGPD compliance contexto BR), `seo-tecnico` (CWV + render budget impacto em GA4 page_view), `metricas-marketing` (KPIs upstream que entram em GA4), `funil-jornada` (AARRR mapeado em events GA4), `dominio-juridico-mkt` (LGPD em consent mode).
> **Pre-requisito:** ter nocao basica de "evento", "parametro", "dimensao", "metrica", "amostragem" e diferenca conceitual entre session-based (UA) e event-based (GA4). Esta skill aprofunda execucao + nuances + armadilhas + Brasil 2026.

---

## 1. Visao Geral

Google Analytics 4 (GA4) e a plataforma de analytics web + app do Google que **substituiu Universal Analytics (UA)** em **01-Jul-2023** (UA Standard sunset; UA 360 propriedades padronizadas em 01-Jul-2024). GA4 nao e "UA versao 4" — e **um produto novo, com modelo de dados radicalmente diferente** (event-based) e ergonomia distinta. Times que migraram esperando "UA com cara nova" geralmente subutilizam GA4 (estatistica de mercado: implementacoes medias usam apenas 12 dos 40+ event types disponiveis).

Esta skill cobre o **conhecimento estrutural de GA4** para analysts, CMO, founders, devs e agencias atuando no Brasil em 2026 — ano em que **87% das ex-propriedades UA ja migraram**, mas apenas **32% rodaram audit pos-migracao**, com auditadas encontrando em media **4.7 discrepancias de tracking** que precisaram correcao.

A skill cobre 8 fundacoes:

1. **GA4 Foundations + Migration** — modelo event-based, sunset UA, 14 meses retention default, 4 default channels, Engagement vs Bounce Rate.
2. **Events** — auto-collected, enhanced measurement, recommended, custom; limites 500 distinct standard / 50M premium.
3. **Explorations** — Free Form, Funnel, Path, Segment Overlap, Cohort, User Lifetime; sample 10M default.
4. **Conversions / Key Events** — rename 2024; import para Google Ads; cross-platform attribution.
5. **BigQuery Export** — free tier 2023+, raw event data, retention 1 ano default, SQL queries cost-efficient.
6. **Brasil 2026** — LGPD, Consent Mode v2 (TCF v2.3 mandatory 28-Fev-2026), GTM, sGTM, Looker Studio, padroes Magalu/Mercado Livre/Nubank/iFood.
7. **Mensuracao + Tools** — Looker Studio, Mixpanel/Amplitude (alternativas product analytics), Hotjar/FullStory (complemento qualitativo), benchmarks engagement rate >=50%.
8. **Aplicacao MKT** — 5 audiencias canonicas (analyst, CMO, founder/dev, agencia, growth/performance).

### 1.1 Acionamento — quando esta skill carrega

| Gatilho | Exemplo |
|---------|---------|
| Auditoria de GA4 | "tracking confiavel? rodar audit nas 50+ propriedades do cliente" |
| Migracao UA->GA4 (raros) | "ainda em UA legado export — como migrar agora?" |
| Debug events | "purchase event nao chega; veio com items vazio" |
| Setup Key Events | "marcar form_submit como Key Event para Google Ads pegar" |
| Audiences | "audience 'engaged + nao convertidos' para remarketing" |
| Explorations | "funnel 4 steps view_item->add_to_cart->begin_checkout->purchase" |
| BigQuery export | "ligar export, projetar custos, montar Looker Studio em cima" |
| Consent Mode v2 | "implantar consent_mode + CMP TCF v2.3 antes de 28-Fev-2026" |
| sGTM server-side | "migrar GTM web -> sGTM Cloud Run / Stape; vale o custo?" |
| Ecommerce | "Shopify/VTEX/Magento dataLayer correto para GA4 ecommerce" |
| Benchmark | "engagement rate 32% — esta ruim?" |
| Mixpanel vs GA4 | "produto SaaS B2B precisa product analytics, GA4 chega?" |

### 1.2 Pre-requisitos

- [ ] **Acessos**: GA4 (admin Editor minimo), GTM (web e/ou server), Google Ads (linker), Search Console (linker), BigQuery (caso export), Looker Studio.
- [ ] **Stack documentada**: CMS/framework, render mode (CSR/SSR/SSG/ISR — afeta page_view), CDN, CMP (Cookiebot, OneTrust, Iubenda, CookieFirst, etc.), provider de pagamento.
- [ ] **dataLayer plan**: spec documentado de eventos (nome + parametros + items array para ecommerce).
- [ ] **Consent Mode v2 status** (Basic vs Advanced + TCF v2.3 string atualizada).
- [ ] **Google Ads + GA4 linker** + **GSC + GA4 linker** verificados.
- [ ] **Conhecimento dos KPIs upstream do negocio** — sem isso, GA4 vira "vanity dashboard". Vide `metricas-marketing`.

> **Cristal C0 — NAO CHUTAR.** Nenhuma decisao em GA4 (deletar evento, recriar Key Event, ativar attribution model novo, mudar retention, ligar BigQuery export) e tomada sem (i) data dump real do DebugView/RealTime, (ii) cross-check com GSC/Google Ads/CRM, (iii) revisao do dataLayer no GTM. "Achismo" em analytics custa decisoes erradas multiplicadas por todo o budget.

---

## 2. Modelo mental — UA session-based vs GA4 event-based

A diferenca-chave (sem entender, nada faz sentido):

```
UA (Universal Analytics) — Jul-2005 a Jul-2023 — modelo session-based
==============================================================================
SESSION
  |-- pageview
  |-- pageview
  |-- event (ga('send','event',...))
  |-- transaction (ecommerce)
  |-- ...
SESSION
  |-- pageview
  ...

Conceitos: "session", "bounce" (1 hit), "page", "screen". Hits sao tipados.


GA4 — Jul-2023 (sunset UA) ate hoje — modelo event-based
==============================================================================
EVENT (sempre evento; pageview e screen_view sao tipos de evento)
  parametros: page_location, page_title, ga_session_id, engagement_time_msec, ...
EVENT
  parametros: items[], value, currency, transaction_id, ...
EVENT
  parametros: ...

Conceitos: "event", "engagement" (>=10s OU >=2 pageviews OU >=1 conversion),
"engagement rate" (sessoes engajadas / sessoes), nao ha "bounce rate" classico
(bounce rate em GA4 = inverso de engagement rate; saiu do core report).
```

### 2.1 Implicacoes praticas

- **Tudo e evento.** Pageview e `page_view` event. Click e click event. Scroll e scroll event. Cada evento carrega ate ~25 parametros (configuravel).
- **Sessoes ainda existem em GA4** (`ga_session_id`, `ga_session_number`, `session_start` event), MAS:
  - Bounce rate "1 hit" sumiu. Substituido por **Engagement Rate**.
  - Session timeout default = 30 min (configuravel 5 min - 7h45 em Property Settings).
  - Cross-device tracking via Google Signals (opt-in, requer LGPD/GDPR consent).
- **Nao ha "view" pre-UA-360.** GA4 tem **DataStreams** (Web Stream, Android Stream, iOS Stream — multiplos por property) + **Properties** + **Accounts**.
- **Sample 10M default** em Explorations (dataset >10M hits/sessoes em janela vira amostra). GA4 360 sobe para 1B+.
- **Retention default = 14 meses** (era 26 em UA). Settable em Admin > Data Settings > Data Retention; max **38 meses** (GA4 360) ou **14 meses** (GA4 Standard) para event-level data.

### 2.2 Dimensoes vs Metricas — terminologia GA4

- **Dimensao** — atributo qualitativo (ex.: `page_path`, `country`, `source`, `medium`, `device_category`).
- **Metrica** — quantitativo (ex.: `eventCount`, `sessions`, `engagedSessions`, `totalUsers`, `conversions`, `purchaseRevenue`).
- **Dimensao customizada** — registro de parametro de evento como dimensao explorable. Limite: 50 event-scoped + 25 user-scoped (GA4 Standard); 125 + 100 (GA4 360).
- **Metrica customizada** — agregacao de parametro numerico. Limite: 50 (Standard); 125 (360).

> **Pegadinha:** parametro de evento NAO aparece automatico em relatorios. Precisa ser **registrado como Custom Dimension** em Admin > Custom Definitions. So apos o registro, dados FUTUROS aparecem em explorations/reports. Dados passados sem registro sao perdidos (ficam apenas em BigQuery se export ativo).

---

## 3. Migracao UA->GA4 + 4 default channels

### 3.1 Sunset oficial UA

- **01-Jul-2023** — UA Standard parou de processar hits.
- **01-Jul-2024** — UA 360 parou de processar hits.
- **01-Jul-2024** — propriedades UA deletadas; export historico encerrado para a maioria.
- **Status 2026:** 87% das organizacoes ja migraram. Cauda longa (13%) sao casos de legado nao-mais-monitorado, properties dormentes ou stacks customizadas (Snowplow, Heap, Plausible, Matomo).

### 3.2 Framework migracao 12 etapas (resumo)

1. Criar **GA4 Property** + **Web Data Stream** + **App Streams** (se aplicavel).
2. Instalar **gtag.js** (codigo direto) OU **GTM** com tag GA4 Configuration.
3. **Enhanced Measurement** ON (default): captura page_view, scrolls 90%, outbound clicks, site search, video engagement YouTube embed, file downloads.
4. Mapear **events UA -> GA4** (vide tabela 3.4 abaixo).
5. Configurar **Custom Events** (eventos especificos do negocio).
6. Registrar **Custom Dimensions/Metrics** (parametros que viram dimensao/metrica).
7. Marcar **Key Events** (ex-Conversions; Google Ads import).
8. Configurar **Audiences** (incluindo audiencias dinamicas).
9. **Linker accounts**: Google Ads, Search Console, BigQuery, Merchant Center, Display & Video 360, Search Ads 360.
10. Configurar **Consent Mode v2** + CMP (TCF v2.3).
11. **Validar** com DebugView + Tag Assistant + GA4 Realtime + GTM Preview + (se sGTM) Server Container Preview.
12. **Audit pos-migracao** (90 dias depois): comparar volumes vs UA backup, identificar discrepancias, corrigir.

### 3.3 14 meses retention default (vs UA 26 meses) — armadilha

- GA4 Standard default = **14 meses** (tinha 2 meses ate 2023; subiu para 14 default).
- Aumentar para **38 meses** so GA4 360.
- **Implicacao critica:** Explorations com janela maior que 14 meses retornam dados truncados ou ausentes. Para historico maior, **BigQuery export e a unica saida** (custo-beneficio gigante; vide Sec 5).
- **Acao recomendada (dia 1 de qualquer setup novo):** ligar BigQuery export imediatamente. Cada dia perdido sem export = dado bruto perdido para sempre (so agregados ficam em GA4 UI).

### 3.4 Mapping UA -> GA4 (sintese)

| UA | GA4 |
|----|-----|
| Sessions | Sessions (definicao similar; `session_start` event) |
| Users | Total Users / Active Users |
| Pageviews | `page_view` event |
| Bounce Rate | (deprecado) — usar **Engagement Rate** (inverso) |
| Avg. Session Duration | Average Engagement Time per Session |
| Goals (4 tipos: Destination, Duration, Pages/Session, Event) | **Key Events** (todos sao baseados em event) |
| Events (Cat/Action/Label/Value) | Events (parametros nomeados; sem hierarquia rigida) |
| Ecommerce + Enhanced Ecommerce | Recommended ecommerce events (view_item, add_to_cart, ... purchase) |
| Site Search | Enhanced Measurement view_search_results |
| Custom Dimensions (hit/session/user) | Event-scoped + User-scoped Custom Dimensions |
| Views (UA only) | (nao existe; usar Filters em DataStream + Property) |
| Filters (Include/Exclude IP) | Internal Traffic + Developer Traffic + Unwanted Referrals |
| Channel Grouping (UA: 8 default) | **Default Channel Group** (4 grupos canonicos + ~17 sub) — Sec 3.5 |
| `(direct) / (none)` | Direct (mesmo) |
| Demographics | Audiences + Demographics (requer Google Signals + consent) |

### 3.5 Default Channel Group GA4 — 4 grupos canonicos modelo

GA4 simplifica para **Default Channel Group** com regras hardcoded baseadas em source/medium/campaign:

1. **Direct** — `source=direct AND medium=(not set|none)`.
2. **Cross-network** — `campaign=cross-network` (Performance Max etc.).
3. **Paid Search / Paid Social / Paid Shopping / Paid Video / Paid Other** — `medium = cpc|ppc|paid|...` + matching de domains.
4. **Organic Search / Organic Social / Organic Shopping / Organic Video** — matching de domains (google.com, facebook.com, instagram.com, youtube.com, etc.) + medium=`organic`.
- **Email** — medium=`email|e-mail|e_mail`.
- **Affiliates**, **Referral**, **Audio**, **SMS**, **Mobile Push Notifications**, **Display**, **Unassigned**.

**Diferenca crucial vs UA:** GA4 usa **Data-Driven Attribution (DDA)** como default em Key Events (era Last Click em UA), com fallback para Last Click se DDA insuficiente. Cross-channel reports usam DDA; Acquisition reports usam Last Non-Direct Click.

### 3.6 Engagement Rate vs Bounce Rate — KPI mental shift

- **Engaged Session** (GA4) = sessao que cumpre **>= 1 dos criterios**:
  - Durou **>= 10 segundos**, OU
  - Teve **>= 2 page_views/screen_views**, OU
  - Teve **>= 1 conversion event**.
- **Engagement Rate** = engaged sessions / total sessions.
- **Bounce Rate (GA4)** = 1 - Engagement Rate. Voltou em Aug-2022 a pedido publico, MAS tem semantica diferente do UA.

**Benchmark 2026 (Sec 14):** engagement rate **>= 50%** para sites de conteudo saudavel; **>= 60%** para SaaS landing pages com bom fit; **30-40%** comum em sites de noticias rasos.

---

## 4. Events — auto-collected + enhanced + recommended + custom

### 4.1 4 categorias de events

| Categoria | Quem dispara | Exemplos |
|-----------|--------------|----------|
| **Auto-collected** | gtag.js / Firebase SDK automatico | `first_visit`, `session_start`, `user_engagement`, `app_remove`, `app_update`, `app_clear_data`, `os_update`, `app_exception` |
| **Enhanced Measurement** | toggle no Web Stream | `page_view`, `scroll` (90% threshold), `click` (outbound), `view_search_results`, `video_start/progress/complete` (YouTube embed), `file_download` |
| **Recommended** | dev implementa com NOMES PADRAO | ecommerce: `view_item`, `select_item`, `add_to_cart`, `remove_from_cart`, `view_cart`, `begin_checkout`, `add_payment_info`, `add_shipping_info`, `purchase`, `refund`. Tambem: `login`, `sign_up`, `share`, `search`, `select_content`, `tutorial_begin/complete`, `level_up`, `unlock_achievement`, `earn_virtual_currency`, `spend_virtual_currency`, `generate_lead`, `join_group`, `post_score`, `app_open` |
| **Custom** | dev cria com qualquer nome | `whitepaper_download`, `pricing_calculator_used`, `cnpj_validated`, `pix_qr_generated`, etc. |

> **Regra:** SEMPRE preferir **Recommended** sobre Custom quando o caso bate. Recommended events tem dimensoes/metricas pre-cabladas em reports e enriquecimento automatico (ex.: `purchase` aciona Revenue automatico em todos os Acquisition reports).

### 4.2 Limites criticos

- **500 distinct event names** por property (GA4 Standard). Acima disso, eventos extras viram `(other)` e sao perdidos (apenas agregados).
- **GA4 360**: 50 milhoes distinct (na pratica, ilimitado).
- **25 parametros por evento** (alem dos automaticos). User properties: 25 user-scoped.
- **40 caracteres** event name max; **40 caracteres** parameter name max; **100 caracteres** parameter value (text) max.
- **Reservados**: prefixos `_` (underscore), `firebase_`, `google_`, `ga_` proibidos para custom.

### 4.3 Items array (ecommerce)

Para `view_item`, `add_to_cart`, `purchase`, etc., o parametro `items` e um **array de objetos** com ate 27 parametros padrao por item (mais customs):

```javascript
gtag('event', 'purchase', {
  transaction_id: 'T_12345',
  value: 199.90,
  currency: 'BRL',
  tax: 19.99,
  shipping: 9.90,
  coupon: 'BLACKFRIDAY10',
  items: [{
    item_id: 'SKU_001',
    item_name: 'Camiseta Frank',
    affiliation: 'Loja Frank',
    coupon: 'BLACKFRIDAY10',
    discount: 10,
    index: 0,
    item_brand: 'Frank',
    item_category: 'Vestuario',
    item_category2: 'Camisetas',
    item_category3: 'Manga curta',
    item_list_id: 'related_products',
    item_list_name: 'Produtos Relacionados',
    item_variant: 'Preto P',
    location_id: 'ChIJ...',  // Place ID Google
    price: 99.90,
    quantity: 2
  }]
});
```

> **Pegadinha 1:** `currency` em **ISO 4217** (`BRL`, `USD`, `EUR`). Sem currency, GA4 dropa `value` em alguns reports.
> **Pegadinha 2:** `value` deve ser numerico (sem aspas), com ponto decimal (nao virgula).
> **Pegadinha 3:** `transaction_id` UNICO. Se mesmo ID dispara 2x (refresh, double-click), GA4 deduplica em alguns reports MAS BigQuery export grava ambos.

### 4.4 dataLayer pattern (GTM)

```javascript
// GTM dataLayer push pattern canonico (ecommerce)
window.dataLayer = window.dataLayer || [];
dataLayer.push({ ecommerce: null });  // limpa anterior
dataLayer.push({
  event: 'purchase',
  ecommerce: {
    transaction_id: 'T_12345',
    value: 199.90,
    currency: 'BRL',
    items: [/* ... */]
  }
});
```

Em GTM, criar **Variable** tipo `Data Layer Variable` apontando para `ecommerce`, e **Trigger** Custom Event = `purchase`. Tag GA4 Event recebe ecommerce data via `Send Ecommerce Data` toggle.

### 4.5 Modify + Create + Audit events (admin)

- **Create event** — criar novo event a partir de outro existente com filtros (ex.: criar `purchase_high_value` a partir de `purchase` com `value >= 500`).
- **Modify event** — sobrescrever parametros de event existente (ex.: normalizar `page_path` removendo query strings).
- **Mark as Key Event** — vide Sec 6.

> **Cristal C1 — Audit antes de criar custom.** Antes de inventar custom event, conferir se existe Recommended event que cobre o caso. Inventar `cart_add` em vez de `add_to_cart` quebra todos os reports de ecommerce. Vide Sec 14 anti-patterns.

---

## 5. Explorations — Free Form, Funnel, Path, Segment Overlap, Cohort, User Lifetime

Explorations e o **modulo "Explore"** em GA4 — substituto direto de "Custom Reports" UA + algumas analyses inexistentes em UA. Acessivel via menu lateral "Explore".

### 5.1 6 templates oficiais

| Template | Pergunta que responde | Quando usar |
|----------|----------------------|-------------|
| **Free Form** | "como filtro/cruzo/visualizo dimensoes x metricas?" | report tabular custom, similar a UA Custom Report |
| **Funnel exploration** | "que % dos users avanca step a step ate conversao?" | ate 10 steps, com ate 4 segments simultaneos |
| **Path exploration** | "que paginas/eventos vem antes/depois de X?" | reverse engineering jornada (forward + backward) |
| **Segment overlap** | "audiencias se intersectam? quao?" | Venn de ate 3 segments |
| **Cohort exploration** | "users adquiridos em jan retem em fev/mar/abr?" | retention curves, decay, % cohort |
| **User lifetime** | "qual revenue/sessions total per user lifetime?" | LTV simplificado |

### 5.2 Funnel exploration — masterclass

- **Open vs Closed funnel:**
  - **Closed** (default) — usuario PRECISA passar pelos steps em ordem. Quem entra direto no step 3 nao conta no funnel.
  - **Open** — usuario entra em qualquer step e os subsequentes contam normalmente. Util para analise multi-touchpoint.
- **Make open funnel:** toggle dentro da config.
- **Trended funnel:** linha do tempo das conversoes step a step (vs tabela estatica).
- **Elapsed time** — tempo entre steps (mediano + max).
- **Next action** — que evento ocorre depois de cada step (drop-off destination).
- **Segments comparados** — ate 4 (ex.: Mobile vs Desktop, Brazil vs Argentina, Paid vs Organic).

### 5.3 Path exploration

- **Forward path** — start node = evento/page X, ver o que vem depois.
- **Backward path** — end node = evento/page X, ver o que vem antes (uso classico: "o que precede `purchase`?").
- **Node types**: `Event name`, `Page title`, `Page title + screen class`.
- **Limitacoes:** path nao mostra "loops infinitos". Aninha ate ~5 niveis. Para analise mais profunda, BigQuery + SQL.

### 5.4 Segment overlap

- Ate **3 segmentos** simultaneos.
- Diagrama de Venn + tabela de counts.
- Caso clasico: segmento "Engaged users" + "Mobile" + "Brazil" — ver quantos sao todos os 3.

### 5.5 Cohort exploration

- **Acquisition cohort** (ex.: users adquiridos na semana X).
- **Cohort criteria** (ex.: First Touch, Any Event, Firebase install).
- **Return criteria** (ex.: Any Event, ou specific event como `purchase`).
- **Granularidade**: Daily, Weekly, Monthly.
- **Calculation**: Standard (% do cohort), Cumulative (acumulado), Rolling (deslizante).

### 5.6 Sample 10M default — limitacao critica

- GA4 Standard amostra explorations com **>= 10M events** na janela analisada.
- GA4 360 sobe para **>= 1B events**.
- **Ouro: BigQuery export elimina sample** — Looker Studio em cima de BQ direct query nao amostra (custa $5/TB queried, mas free tier de 1TB/mes cobre maioria das PMEs).

### 5.7 Tabela "explorations templates" — quick reference

| Caso | Template | Steps/Configs criticos |
|------|----------|------------------------|
| Drop-off checkout | Funnel (closed) | 4 steps: view_item, add_to_cart, begin_checkout, purchase + segment Mobile/Desktop |
| Onboarding SaaS | Funnel (open) | sign_up, tutorial_begin, tutorial_complete, first_value_event |
| O que precede churn | Path (backward) | end node = event "subscription_cancel" |
| O que vem apos blog post | Path (forward) | start node = page_path = /blog/* |
| Ad-paid + remarketing audiencia | Segment overlap | Acquired: Paid, Behavior: Engaged, Geo: Brazil |
| Retention 12 weeks | Cohort | Weekly + cumulative + return = any event |
| LTV per channel | User lifetime | breakdown por First User Source |

---

## 6. Conversions / Key Events — rename 2024 + integracao Google Ads

### 6.1 Rename Conversions -> Key Events (2024)

- Em **2024**, Google renomeou **"Conversions"** para **"Key Events"** dentro de GA4 (UI + Reporting).
- **"Conversions"** continua existindo, mas agora se refere a **conversoes importadas no Google Ads** (eventos GA4 marcados como Key Event + importados em Google Ads viram "GA4 conversions" no Google Ads).
- **Implicacao:** comunicacao com stakeholders precisa de cuidado. "Conversao" significa coisas diferentes em GA4 (Key Event) vs Google Ads (GA4 Conversion importada).

### 6.2 Como marcar Key Event

1. Admin > Events > localizar event (ex.: `generate_lead`, `purchase`, `form_submit`).
2. Toggle **"Mark as key event"** = ON.
3. Aguardar 24-48h para historico processar.
4. (Opcional, recomendado) Importar para Google Ads: linker GA4-Google Ads + selecionar Key Event no Google Ads > Tools > Conversions > Import.

### 6.3 30 Key Events max

- Limite GA4 Standard = **30 Key Events** por property.
- Limite GA4 360 = mesmos 30 (a Google nao subiu nesse).
- **Estrategia:** marcar so o que IMPORTA para Google Ads bidding e Audiences. Nao marcar todo click.

### 6.4 Counting method

- **Once per session** (default) — conta 1x mesmo se evento dispara 3x na sessao.
- **Every event** — conta cada disparo.
- **Recomendado:** `purchase` = Every event (cada compra conta); `form_submit` = Once per session (evita duplicacao por refresh).

### 6.5 Cross-platform attribution

- GA4 unifica web + app em uma property (Web Stream + App Streams na mesma Property).
- Key Events sao agregados cross-stream.
- **Atencao Brasil:** muitos clientes ainda tem property separada para web e para app (legado pre-GA4). Migrar para single-property + multi-stream.

### 6.6 Attribution model (DDA default)

GA4 default = **Data-Driven Attribution (DDA)** desde Out-2023 (substituiu Last Click default).

- **Position-based, Time-decay, Linear, First-click** ainda disponiveis em Admin > Attribution Settings.
- **DDA requer >= 3000 path interactions + 300 conversions / 30 dias** para o modelo treinar; abaixo disso GA4 fallback Last Click.

---

## 7. BigQuery Export — gratis + raw data + cost-efficient

### 7.1 Por que ligar (resposta curta: "ligue ontem")

- **Free tier desde 2023:** GA4 Standard property pode exportar gratuitamente (era exclusivo GA4 360 ate 2023). Ainda existe limite **1 milhao de events/dia** para daily export GA4 Standard.
- **Raw event-level data** sem amostragem, sem agregacao, sem limites de cardinalidade (alem do 500 distinct names).
- **Schema canonico** com tabelas `events_YYYYMMDD` (daily, particionada) + `events_intraday_YYYYMMDD` (streaming).
- **SQL queries arbitrarias** — joins com CRM, ERP, custom dim tables, etc.
- **Looker Studio direct query** = Looker dashboards no dado bruto, sem sample.
- **Retention configuravel** ate forever (BigQuery storage e barato).

### 7.2 Setup em 5 etapas

1. **Google Cloud Project** com billing ativado (mesmo que use free tier).
2. GA4 > Admin > **Product Links > BigQuery Links > Link**.
3. Selecionar **dataset region** (saoluo1, southamerica-east1 = Sao Paulo, recomendado para BR).
4. Frequencia: **Daily** (1x/dia, batch) + **Streaming** (continuous, ~minutos delay) — ambas podem ligar.
5. Aguardar 24-48h primeira tabela aparecer.

### 7.3 Custos reais 2026

| Recurso | Free tier mensal | Custo apos free tier |
|---------|------------------|----------------------|
| **BigQuery Storage** | 10 GB | ~$0.02/GB/mes (active); $0.01/GB/mes (long-term, >90 dias sem modificacao) |
| **BigQuery Queries (analise)** | 1 TB queried | $5/TB queried (on-demand) |
| **Streaming insert** | nenhum | $0.05/GB inserted (sGTM streaming export incorre) |
| **Looker Studio** | gratis (UI) | gratis (queries em BQ entram no balde de 1TB) |

**Estimativa pratica BR PME:** site com **1M page_views/mes** + ecommerce moderado gera ~3-5GB de events/mes. Storage cabe em free tier por anos. Queries variam:
- Looker Studio "leve" (cards agregados, 1 partition por vez): **~50-200 GB/mes queried** — dentro do free tier.
- Looker Studio "pesado" (sem `_TABLE_SUFFIX`, sem WHERE em date): **>1TB facil**, $5+/mes.

> **Otimizacao essencial:** sempre filtrar por `_TABLE_SUFFIX` (sufixo `events_20260501`) e usar `PARTITIONS` em queries de Looker. Queries sem partition pruning escaneiam dataset inteiro.

### 7.4 Schema canonico (essencial)

```sql
-- Tabela: <project>.<dataset>.events_YYYYMMDD
-- Particionada por _TABLE_SUFFIX

SELECT
  event_date,
  event_timestamp,
  event_name,
  event_params,         -- ARRAY<STRUCT<key STRING, value STRUCT<...>>>
  user_id,
  user_pseudo_id,       -- Client ID (cookie _ga)
  user_first_touch_timestamp,
  user_properties,      -- ARRAY<STRUCT>
  device,               -- STRUCT (category, mobile_brand_name, OS, browser)
  geo,                  -- STRUCT (country, region, city, continent)
  app_info,             -- STRUCT (id, version, install_source) -- so apps
  traffic_source,       -- STRUCT (name, medium, source) -- first-touch
  collected_traffic_source, -- session-level traffic
  session_traffic_source_last_click, -- last-click (Out-2023+)
  ecommerce,            -- STRUCT (transaction_id, total_item_quantity, ...)
  items,                -- ARRAY<STRUCT> (items array do evento ecommerce)
  privacy_info,         -- STRUCT (analytics_storage, ads_storage, uses_transient_token)
  stream_id,
  platform              -- WEB / IOS / ANDROID
FROM `myproject.analytics_123456.events_20260509`
WHERE event_name = 'purchase'
  AND geo.country = 'Brazil';
```

### 7.5 Queries canonicas (cookbook)

```sql
-- 1. Receita diaria
SELECT
  event_date,
  COUNT(DISTINCT user_pseudo_id) AS users,
  SUM(ecommerce.purchase_revenue) AS revenue
FROM `proj.ds.events_*`
WHERE _TABLE_SUFFIX BETWEEN '20260401' AND '20260430'
  AND event_name = 'purchase'
GROUP BY event_date
ORDER BY event_date;

-- 2. Funnel ecommerce 4 steps
WITH step1 AS (
  SELECT user_pseudo_id FROM `proj.ds.events_*`
  WHERE _TABLE_SUFFIX BETWEEN '20260401' AND '20260430'
    AND event_name = 'view_item'
),
step2 AS (
  SELECT user_pseudo_id FROM `proj.ds.events_*`
  WHERE _TABLE_SUFFIX BETWEEN '20260401' AND '20260430'
    AND event_name = 'add_to_cart'
),
-- ... etc
SELECT
  (SELECT COUNT(DISTINCT user_pseudo_id) FROM step1) AS s1,
  (SELECT COUNT(DISTINCT user_pseudo_id) FROM step2) AS s2;

-- 3. Cohort retention semanal
-- (longa; ver ga4bigquery.com cookbook)
```

### 7.6 Retention BigQuery vs GA4 UI

- **GA4 UI**: 14 meses (Standard) / 38 meses (360) max.
- **BigQuery**: configuravel no dataset (default 60 dias, settable a forever). Storage cost negligivel.
- **Compromisso:** raw data BigQuery + dashboards Looker Studio = retention efetiva ilimitada por preco baixo.

---

## 8. Looker Studio + alternativas Mixpanel/Amplitude/Hotjar/FullStory

### 8.1 Looker Studio (ex-Data Studio)

- **Gratis** com unlimited reports, users, sharing.
- **Native GA4 connector** (gratis).
- **Native BigQuery connector** (gratis em UI; queries entram no balde de 1TB free).
- **3rd-party connectors:** Supermetrics, Funnel.io, Windsor.ai (pagos, conectam dezenas de fontes alem GA4).

### 8.2 GA4 connector vs BigQuery connector — diferenca critica

| Criterio | GA4 connector | BigQuery connector |
|----------|---------------|---------------------|
| Sample | Sim (>10M events) | Nao |
| Speed | Lento (vai na API GA4) | Rapido (queries SQL) |
| Cardinalidade | Truncada (top 50k rows) | Total |
| Joins com CRM/dados externos | Nao | Sim |
| Custo | Gratis | Free tier 1TB/mes; depois $5/TB |
| Setup | 1 click | Requer ativar BQ export + SQL skill |

**Recomendacao 2026:** dashboards executivos = GA4 connector (rapido para construir). Dashboards profundos / cohort / multi-source = BigQuery connector.

### 8.3 Mixpanel + Amplitude (product analytics — alternativas/complemento)

- **GA4 e otimo em web + ecommerce**, MAS deficiente em **product analytics** (eventos de feature-usage em SaaS B2B/B2C app, retention curves complexas, A/B test analysis).
- **Mixpanel** (~$0-25/mo free; pago a partir de ~$833/mo enterprise) — funnel + retention + cohort + JIT analytics.
- **Amplitude** (free ate 10M events/mo; pago a partir de ~$995/mo) — similar; melhor em behavioral cohorts + ML insights.
- **Heap** (auto-track all DOM events) — alternativa "no-code" mais cara.
- **Padrao 2026 SaaS B2B BR:** GA4 (web ads attribution) + Amplitude/Mixpanel (in-app product analytics) coexistem.

### 8.4 Hotjar + FullStory (qualitativo — complemento)

- **Hotjar** ($0-99+/mo) — heatmaps + session recordings + surveys + feedback widgets + funnels.
- **FullStory** (enterprise; $0 free trial) — session replay + Frustration Signals (rage clicks, dead clicks, errors) + heatmaps.
- **Quando usar:** depois do "que" (GA4 quantitativo), entender o "por que" (Hotjar/FullStory qualitativo). Casos: drop-off em form, abandonment de checkout, micro UX issues.
- **Privacidade:** ambos suportam mascaramento de PII (CPF, cartao). LGPD requer anonymization + consent.

### 8.5 Stack 2026 canonical PME BR

```
Layer 1 (web ads attribution): GA4 + GTM + sGTM (opcional) + BigQuery export + Looker Studio
Layer 2 (product analytics in-app, se SaaS): Amplitude OU Mixpanel
Layer 3 (qualitativo UX): Hotjar OU FullStory (mais raro em PME)
Layer 4 (CRM): RD Station / HubSpot / Pipedrive — integrado com GA4 via measurement protocol/CAPI
Layer 5 (data warehouse, se enterprise): BigQuery (ja temos via export GA4) OU Snowflake/Redshift se outro stack
Layer 6 (BI): Looker Studio (free) OU Power BI / Tableau / Looker (enterprise)
```

---

## 9. Brasil 2026 — LGPD, Consent Mode v2, GTM, sGTM, padroes

### 9.1 LGPD (Lei 13.709/2018) + GA4

- **Base legal recomendada para GA4:** consentimento (Art. 7 I) ou legitimo interesse (Art. 7 IX) — depende do uso. **Recomendacao consolidada 2026:** consentimento explicito via CMP banner para qualquer cookie de medicao/marketing (alinhado a CNIL/GDPR + ANPD orientacao tecnica).
- **Direitos do titular** (Cap III LGPD): acesso, correcao, eliminacao, portabilidade, oposicao. GA4 oferece **User Deletion API** (Section 9.5).
- **DPO obrigatorio** se processamento em larga escala (regra ANPD).
- **Encarregado:** documentar contato em politica de privacidade.

### 9.2 Consent Mode v2 — mandatory desde Mar-2024 + TCF v2.3 mandatory 28-Fev-2026

- **Consent Mode v2** — sinal de Google que ajusta comportamento de Google tags (GA4, Google Ads, Floodlight) baseado em consent state.
- **2 modos:**
  - **Basic** — Google tags **NAO disparam** ate consent. Sem consent = zero data.
  - **Advanced** — Google tags **disparam SEMPRE**, mas em modo "cookieless ping" se sem consent. Google usa **modeling** para extrapolar conversoes nao consentidas (data-driven, behavioral modeling).
- **TCF v2.3** (IAB Transparency & Consent Framework) — mandatory 28-Fev-2026 para CMPs operando na EU. CMP precisa gerar consent string TCF v2.3.
- **Brasil:** TCF nao e mandatory por lei BR, mas **Google Ads + GA4** exigem Consent Mode v2 para servir EEA users + recomendam para todos os mercados (modeling so funciona com Consent Mode v2 implantado). **Default 2026 BR**: implantar Consent Mode v2 Advanced + CMP com TCF v2.3 (cobre LGPD + GDPR via mesma infra).

### 9.3 4 consent signals canonicos

| Signal | Significado | GA4 impact |
|--------|-------------|------------|
| `ad_storage` | cookies de Ads | sem consent = sem cookies de remarketing |
| `analytics_storage` | cookies de Analytics | sem consent = sem _ga cookie -> Client ID por session-only |
| `ad_user_data` | enviar user data para Ads (Customer Match) | sem consent = nao envia |
| `ad_personalization` | personalizacao em Ads | sem consent = ads contextuais apenas |

### 9.4 CMPs comuns BR 2026

- **Cookiebot** (gratis ate 100 paginas; pago)
- **OneTrust** (enterprise, pago, top-tier)
- **CookieFirst** (pago, simples)
- **Iubenda** (pago, BR-popular, footer "by Iubenda")
- **TrustArc** (enterprise)
- **Usercentrics** (enterprise, GDPR-strong)
- **Quantcast** (gratis basico)
- **Custom CMP** (build interno; risco compliance se mal feita)

> **Pegadinha BR:** muitos sites legados ainda usam "barra de cookies aceita-tudo" sem opt-in granular. **NAO compliant LGPD nem GDPR**. Migrar para CMP com escolha granular (analytics yes/no, ads yes/no, etc.).

### 9.5 User Deletion API + retention controls

- **User Deletion API** GA4 — endpoint POST que apaga eventos associados a User ID ou Client ID. Necessario para atender requisicao LGPD Art. 18 V (eliminacao).
- Documentacao: https://developers.google.com/analytics/devguides/config/userdeletion/v1
- Tambem: Admin > Data Settings > **Reset User Data on New Activity** (toggle).

### 9.6 GTM (Google Tag Manager) — basico

- **GTM web container** = JavaScript hospedado no Google que carrega tags (GA4, Meta Pixel, LinkedIn Insight, etc.) baseado em **triggers** (eventos no site) e **variables** (dataLayer, JS vars, custom).
- **Estrutura:** Tags + Triggers + Variables + Folders.
- **GA4 Configuration tag** (1x por site) + **GA4 Event tags** (N, conforme events).
- **Preview Mode** (Tag Assistant) para debug ANTES de publicar.

### 9.7 sGTM (Server-side GTM) — quando vale a pena

**sGTM = container GTM rodando em servidor (Cloud Run / App Engine / Stape / Self-hosted).** Em vez de browser disparar pixels para Google/Meta/LinkedIn, browser dispara para SEU servidor, que reencaminha para destinos.

**Beneficios:**
- **Bypass de adblockers** (ITP Safari, uBlock Origin) — recupera 10-30% de tracking perdido.
- **First-party context** — cookies servidos do seu domain (vs 3rd-party sub-rejected).
- **Enriquecimento server-side** — append de loyalty tier, LTV, customer status antes de mandar p/ Meta CAPI / GA4.
- **PII strip** — remover CPF/email antes de enviar para Meta/Google.
- **Compliance** — center de governanca; um lugar so para reduzir/remover dados.
- **Performance** — menos JS no browser = LCP/INP melhores.

**Custos 2026:**
- **Stape.io** (managed sGTM) — $20-100/mo (PME) ate $500+/mo (enterprise); inclui hosting + presets.
- **Cloud Run self-hosted** — $0-20/mo (low traffic) ate $100-500/mo (high traffic).
- **Self-hosted VM** — depende; mais barato mas mais ops.

**Trade-off:** sGTM **NAO e plug-and-play**. Requer dev/devops + monitoramento + governanca + 2-4 semanas de migracao. Para PME com <100k page_views/mo, custo-beneficio fraco. Para >500k page_views/mo + ecommerce + LGPD-strict, **default arquitetural 2026**.

### 9.8 Padroes Brasil 2026 — empresas referencia

- **Magalu (Magazine Luiza)** — GA4 + sGTM + BigQuery + Looker Studio + product analytics customizado. Public case: data-driven ranking de produtos.
- **Mercado Livre** — Snowplow + GA4 (paralelo) + DW propria. Heap event capture estilo "track-everything".
- **Nubank** — Amplitude (product analytics) + GA4 (marketing site) + DW propria. Paper publico sobre cohort modeling.
- **iFood** — Amplitude + GTM/sGTM + segment.com style + DW propria.
- **Localiza** — GA4 + Adobe Analytics (legado) + Salesforce CDP.

> **Observacao:** os patterns acima exigem time de data eng dedicado. PME BR 2026 default = GA4 + GTM + sGTM (Stape) + BigQuery + Looker Studio. Stack acima cobre 90% dos casos.

### 9.9 Cross-domain tracking BR (multi-dominio)

GA4 suporta cross-domain nativamente via Admin > Data Stream > **Configure tag settings > Configure your domains**.

```
Lista domains (separados por ;):
loja.frank.com.br; checkout.frank.com.br; pagamento.frank.com.br
```

GA4 propaga `_ga` cookie via **GET param `_gl` (linker)** entre domains listados. **NAO funciona com iframes externos** — estes precisam tratamento dedicado (postMessage + manual ID propagation).

---

## 10. Audiences + first-party data + remarketing GA4

### 10.1 GA4 Audiences

- Admin > Audiences > **New audience**.
- Definidas por: **Conditions** (events + parametros + sequences + scope) + **Membership duration** (1-540 dias) + **Trigger** (opcional).
- Limite **GA4 Standard:** 100 audiences ativas.
- Audiences sao usadas em: **Google Ads remarketing** (linker), **Display & Video 360**, **Search Ads 360**, **Audience-based reports** em Explorations, **Audience triggers** (cria event quando user entra na audience).

### 10.2 Predictive audiences (smart audiences)

GA4 oferece **3 predictive metrics** (com modelo ML proprio):

- `purchase_probability` — prob de compra em 7 dias.
- `churn_probability` — prob de churn em 7 dias.
- `predicted_revenue` — receita prevista em 28 dias.

**Pre-requisitos:** **>= 1000 returning users com purchase_probability + 1000 sem purchase em 28 dias** + Key Event marcado como `purchase` ou `in_app_purchase`. Sem volume, GA4 nao serve predictive metric.

**Audiences predictive ja prontas:**
- Likely 7-day purchasers
- Likely 7-day churning users
- Predicted 28-day top spenders

### 10.3 First-party data + Customer Match

- **GA4 nao expoe email/CPF/User ID** em UI/connector — privacidade.
- **Customer Match Google Ads** — upload de email lists para targeting; alimentado fora de GA4 (CRM -> Google Ads direto OU via Google Cloud Customer Match API).
- **Enhanced Conversions** — GA4 (e Google Ads) suportam envio de hashed email/phone para enriquecer attribution. Configuravel via gtag/GTM.

### 10.4 Custom Audiences criativas

- **Engaged + nao convertidos** — `engaged_session = true AND key_event_count = 0` em 30d.
- **High-LTV cohort** — `predicted_revenue > X` (predictive).
- **Cart abandoners** — `add_to_cart fired BUT purchase NOT fired in 7d` (sequence + lookback).
- **Power users SaaS** — `feature_X_used >= 5 in 14d`.

---

## 11. Ecommerce — implementacao e armadilhas

### 11.1 10 events ecommerce essenciais (em ordem do funnel)

1. `view_item_list` — listou produtos (categoria, search, recommended).
2. `select_item` — clicou em produto da lista.
3. `view_item` — abriu PDP (product detail page).
4. `add_to_cart` — adicionou ao carrinho.
5. `view_cart` — abriu carrinho.
6. `remove_from_cart` — removeu do carrinho.
7. `begin_checkout` — comecou checkout.
8. `add_shipping_info` — informou endereco/frete.
9. `add_payment_info` — informou metodo pagamento.
10. `purchase` — concluiu compra.

Complementares: `refund` (estorno), `view_promotion` + `select_promotion` (banner promocional), `add_to_wishlist`.

### 11.2 Implementacoes por plataforma BR

- **Shopify** — app oficial Google & YouTube (GA4 + Google Ads + Google Merchant). Nem sempre dispara `view_item_list`, `select_item` corretamente; auditar com Tag Assistant.
- **VTEX** — modulo nativo "VTEX Pixel Manager" + `dataLayer push` + GTM. Mais flexivel; auditar items array.
- **Magento (Adobe Commerce)** — extensoes nativas + customizacao via dataLayer.
- **WordPress + WooCommerce** — plugins GA4 (Site Kit, MonsterInsights, GTM4WP) + dataLayer.
- **Loja Integrada** — limitado, custom dataLayer dificil; muitas vezes "purchase only" trackado.
- **Nuvemshop** — integracao nativa GA4 + Meta Pixel; auditar items.
- **Nuvemshop, Shopify** comum: `purchase` dispara mas `transaction_id` muda em refresh = duplicate counting.

### 11.3 5 armadilhas ecommerce comuns

1. **transaction_id duplicado** — refresh da thank-you page dispara `purchase` 2x. **Fix:** server-side trigger + idempotency check.
2. **items array vazio** — `purchase` chega sem items (so totals). Reports "Top products" ficam vazios.
3. **currency missing** — `purchase` sem `currency: 'BRL'`. GA4 dropa `value` em alguns reports.
4. **value com virgula** — `value: '199,90'` (string com virgula) em vez de `value: 199.90` (float). Quebra agregacao.
5. **discount/coupon nao tracked** — `coupon` e `discount` em `items` sao opcionais; sem eles, analise de promo zero.

### 11.4 Server-side ecommerce (sGTM ecommerce events)

- sGTM permite receber `purchase` no servidor (ex.: webhook Shopify/VTEX) e disparar para GA4 + Meta CAPI + Google Ads CAPI simultaneamente.
- **Vantagem:** ecommerce events sobrevivem adblock e ITP. Recovery 10-30%.
- **Stape.io tem template Shopify <-> sGTM** que reduz setup de dias para horas.

---

## 12. Mensuracao + benchmarks 2026

### 12.1 Engagement rate benchmark (sites BR + global)

| Tipo de site | Engagement Rate saudavel | Bounce Rate equivalente |
|--------------|--------------------------|-------------------------|
| SaaS landing page (good fit) | >= 60% | <= 40% |
| Site institucional B2B | 50-65% | 35-50% |
| Ecommerce homepage | 45-60% | 40-55% |
| Site de conteudo (blog) | 50-65% | 35-50% |
| Noticia/jornalismo | 30-45% | 55-70% |
| Landing page de ad paid | 40-60% | 40-60% |

> **Avise stakeholders:** engagement rate baixo NAO e necessariamente ruim — depende da intent de pagina. Pagina informativa pode ter 30% saudavel se entrega resposta em 8s.

### 12.2 Average session duration benchmark

- **SaaS B2B**: 2-4 min healthy.
- **Ecommerce**: 1.5-3 min healthy (rapido = bom em ecommerce).
- **Conteudo**: 3-5 min healthy.
- **Noticia**: 1-2 min healthy.

### 12.3 Conversion rate (% sessions com Key Event)

- **Lead generation B2B**: 1-3% (form_submit).
- **Ecommerce DTC**: 1-3% (purchase).
- **Ecommerce nicho**: 3-5%.
- **SaaS sign-up**: 5-15% (free trial).

> **Cristal C2 — comparar contra historico proprio.** Benchmark de mercado e referencia, nao verdade absoluta. Comparar contra historico do proprio cliente (mes anterior + mesmo mes ano anterior) e mais util.

### 12.4 Health checks GA4 (mensal)

- [ ] **Real-time** ativo (events chegando).
- [ ] **Top 10 events** sem `(other)` no top.
- [ ] **engagement_rate >= 30%** (alerta) / >= 50% (saudavel).
- [ ] **Key Events ativos** + `purchase` (ou principal) com volume estavel + 0% (sem queda inesperada).
- [ ] **Sessions sem source** (`(direct)/(none)` <= 30%) — acima disso, problema de UTM/referrer.
- [ ] **Default Channel "Unassigned" <= 5%** — acima, mau tagging.
- [ ] **Property linker** Google Ads, GSC, BigQuery operacionais.
- [ ] **Consent Mode v2 status** verde no DebugView.
- [ ] **Retention 14 meses** confirmada (nao reduziu para 2 meses por bug).

---

## 13. Aplicacao MKT — 5 audiencias canonicas

### 13.1 Data Analyst

**Pergunta principal:** "como respondo perguntas de negocio com dados confiaveis?"

- Dominar Explorations (Funnel, Path, Cohort, Free Form).
- Dominar BigQuery + SQL para superar limites de UI (sample, cardinalidade, retention).
- Documentar **dataLayer spec** + **events catalog** (markdown ou Notion).
- Auditoria pos-migracao + auditoria mensal.
- KPIs: Engagement Rate, Conversion Rate, ROI por canal, LTV per cohort.
- Skill complementar: `metricas-marketing`, `funil-jornada`.

### 13.2 CMO

**Pergunta principal:** "consigo confiar no dado para alocar budget?"

- Looker Studio dashboard executivo: revenue per channel + CAC + LTV + ROAS + funnel.
- Cross-source: GA4 + Google Ads + Meta Ads + LinkedIn Ads + CRM.
- Attribution model coerente (DDA default; ler documentacao).
- KPIs: marketing-sourced revenue %, MQL/SQL flow, customer acquisition cost, payback period.
- Skill complementar: `dominio-negocios-mkt`, `metricas-marketing`.

### 13.3 Founder + Dev

**Pergunta principal:** "como instrumento meu produto/site CORRETO desde o dia 1?"

- Setup canonical: GA4 + GTM (web) + Consent Mode v2 + BigQuery export ON imediato + Looker Studio.
- dataLayer planejado **antes** do dev — spec antes do codigo.
- Recommended events sempre que possivel (nao inventar nomes).
- Apos validar tracking quantitativo, considerar Hotjar para qualitativo.
- Apos atingir 100k page_views/mo, considerar sGTM + product analytics (Amplitude).
- Skill complementar: `seo-tecnico` (CWV impact), `dominio-empreendedorismo-mkt`.

### 13.4 Agencia

**Pergunta principal:** "como entrego setup + dashboard repetivel para 10+ clientes?"

- **Template GA4 + GTM container** (export/import) por nicho (ecommerce, SaaS, B2B lead gen, noticia).
- **Looker Studio template** padrao + custom branding cliente.
- **Audit checklist** mensal por cliente.
- **Documentacao handoff** clara (cliente sabe o que fazer mesmo se trocar agencia).
- **Pricing**: setup one-time + audit recorrente + retention dashboard.
- Skill complementar: `dominio-juridico-mkt` (contrato + LGPD), `comunicacao-corporativa`.

### 13.5 Growth + Performance

**Pergunta principal:** "como otimizo conversao + LTV usando GA4?"

- Funnel exploration + Path exploration para identificar leak points.
- A/B test events customizados (`experiment_id`, `variant`) + Custom Dimensions.
- Predictive audiences (likely 7-day purchasers) para Google Ads bidding.
- Cohort retention semanal + ativacao optimization.
- Cross-stream (web + app) attribution.
- Skill complementar: `funil-jornada`, `persuasao-eticas`, `microcopy`.

---

## 14. Anti-patterns + armadilhas

| Anti-pattern | Por que e ruim | Fix |
|--------------|----------------|-----|
| Inventar `add_cart` em vez de `add_to_cart` | Quebra reports ecommerce nativos | Usar Recommended events sempre |
| Marcar 50 eventos como Key Event | Limite 30; "Conversao" perde significado | Marcar so 5-10 que importam para Ads bidding |
| Esquecer de registrar Custom Dimension | Parametros nao aparecem em reports | Admin > Custom Definitions; register apos primeiro disparo |
| Nao ligar BigQuery export | Perde raw data para sempre apos 14 meses | Ligar dia 1 mesmo se nao for usar agora |
| Ignorar Consent Mode v2 | Perde modeling + viola LGPD/GDPR | Implantar Advanced + CMP TCF v2.3 |
| Cross-domain sem `_gl` linker | _ga cookie nao propaga; user vira "novo" | Configurar Configure your domains |
| `transaction_id` reused | Duplicate purchases em refresh | Server-side trigger + idempotency |
| Filtrar IP interno via dimensao Custom | Nao funciona historicamente | Internal Traffic filter (Admin > DataStream > More tagging settings) |
| Esperar dados em UI passados sem retencao | Sample + retention = dados truncados | BigQuery export para historico |
| GA4 connector Looker para 50M+ events | Sample, lento, cardinality truncada | BigQuery connector |
| sGTM em PME com 10k page_views/mo | Custo nao se paga | Manter web GTM ate volume justificar |
| Custom CMP "barra aceita-tudo" | Nao compliant LGPD | CMP profissional com opt-in granular |
| Mixpanel + GA4 desincronizados | Eventos com nomes diferentes em cada | Catalog unico de events; mapping documentado |
| Loop infinito de redirect dispara `page_view` 100x | Bloat de events + bill BigQuery | Filtro de redirect detection + sample no client |
| `(direct)/(none)` > 50% trafego | UTMs faltantes ou ITP comendo referer | Investigar fonte; sGTM + first-party Cookies ajuda |
| Comparar Engagement Rate vs Bounce Rate UA | Definicao DIFERENTE | Comparar Engagement Rate atual vs Engagement Rate anterior |
| 30 events Key marcados, todos contam Once per session | Distorce volumes | Each event vs Once: pensar caso a caso |
| Auditoria pos-migracao nao feita | 4.7 discrepancias media nao detectadas | Audit obrigatorio 90 dias pos-migracao |

---

## 15. Regras de Ouro

1. **Ligue BigQuery export DIA 1.** Cada dia perdido = raw data perdida apos 14 meses.
2. **Use Recommended events.** Inventar nomes quebra reports nativos e comparacao com benchmark.
3. **Plante dataLayer ANTES do codigo.** Spec markdown + review com analyst antes do dev tocar.
4. **Audit pos-migracao em 90 dias.** Estatistica: 4.7 discrepancias media. Sem audit = decidir com dado errado.
5. **Consent Mode v2 ja, nao depois.** TCF v2.3 mandatory 28-Fev-2026. Implantar Advanced + CMP profissional.
6. **Engagement Rate > Bounce Rate como KPI.** Bounce Rate em GA4 e inverso; semantica diferente.
7. **Key Events <= 10.** 30 e o limite, mas marcar so 5-10 que importam para bidding.
8. **Cross-check cross-source.** GA4 vs Google Ads vs Meta vs CRM — diferencas <=20% sao normais; >20% investigar.
9. **DDA default + nao confiar cegamente.** Olhar `traffic_source` (first), `collected_traffic_source` (session), `session_traffic_source_last_click` (last click) em BigQuery para 360 view.
10. **Retention 14 meses + BigQuery forever.** UI = janela operacional; BQ = arquivo historico.
11. **sGTM por volume + LGPD strict; nao por moda.** PME <100k page_views/mo: custo-beneficio fraco.
12. **Predictive metrics = 1k+ users 28 dias.** Sem volume, GA4 nao serve predictive — nao confiar.
13. **Nao confundir users / sessions / engaged sessions.** 3 metricas distintas; reports usam diferentes default.
14. **Documente events catalog.** Notion/Markdown shared; analyst + dev + agencia mesma fonte de verdade.
15. **Volatility high (3 meses).** Re-validar TUDO antes de publicar peca formal — Google muda silenciosamente.

---

## 16. Exemplos comportamentais

### 16.1 Cliente: "engagement rate 32% — esta ruim?"

**Resposta calibrada:**
"Depende do tipo de site. Para SaaS B2B landing, 32% e baixo (esperado >=60%). Para site de noticias, 32% pode ser saudavel (mediana setor ~35-45%). Antes de chamar de 'ruim', responder 3 perguntas:

1. Qual a intent media da pagina (informativo curto vs deep)?
2. Comparado ao mes anterior + mesmo mes ano anterior, esta caindo, estavel ou subindo?
3. Channel breakdown — Direct/Organic Search >= 50%? Paid Social cair de mais de 60% pra 32% e bandeira; Direct estar em 32% e normal.

Antes de mexer em pagina, valide instrumentacao: `engaged_session` precisa **>=10s OU 2+ pageviews OU Key Event**. Pagina SPA mal configurada pode reportar engagement_time_msec=0 mesmo usuario tendo navegado 5 minutos."

### 16.2 Cliente: "vamos migrar de UA para GA4 agora"

**Resposta calibrada:**
"UA Standard sunset Jul-2023; UA 360 sunset Jul-2024. **Em 2026 UA nao processa hits ha quase 2 anos**. Migracao agora e setup limpo, nao mais 'paralelo UA + GA4'. Plano:

1. Criar GA4 Property + Web Stream (+ App Streams se mobile).
2. **Plano dataLayer** ANTES do dev — spec markdown.
3. GTM container (web + sGTM se volume justificar).
4. Enhanced Measurement ON; Recommended events implementados.
5. Consent Mode v2 + CMP TCF v2.3.
6. **BigQuery export ligado dia 1.**
7. Linkers Google Ads + GSC + BigQuery.
8. Custom Dimensions/Metrics registrados.
9. Key Events marcados (<=10).
10. Audiences definidas.
11. Validation: DebugView + Tag Assistant + Realtime + Looker Studio dashboard.
12. **Audit pos-migracao em 90 dias** (estatistica: 4.7 discrepancias media; nao pular).

Stack 2026 PME BR canonico: GA4 + GTM + (sGTM Stape se >=500k pv/mo) + BigQuery + Looker Studio + Consent Mode v2 + CMP profissional."

### 16.3 Cliente: "Mixpanel ou GA4 para meu SaaS B2B?"

**Resposta calibrada:**
"Ambos. **GA4** para web ads attribution (paid traffic, SEO, content marketing -> sign-up). **Mixpanel ou Amplitude** para in-app product analytics (feature usage, retention curves, behavioral cohorts).

Razao: GA4 e otimo em web + ecommerce, **deficiente em product analytics** (cohort behavioral complexa, A/B test analysis com guardrails, JIT analytics in-app). Mixpanel/Amplitude foram desenhados para isso.

Padrao SaaS B2B BR 2026:
- GA4 (web ads + SEO + content) + BigQuery export
- Amplitude OU Mixpanel (in-app product) + sync via Segment.com ou Reverse ETL para CRM/CDP
- Hotjar OR FullStory (qualitativo UX) — opcional

Custo: GA4 free; Mixpanel free ate 1k users + paid ~$833/mo enterprise; Amplitude free ate 10M events/mo + paid ~$995/mo. Para SaaS B2B com <10M events/mo, Amplitude free tier costuma cobrir. Para PMM com 200k+ users ativos, comparar."

### 16.4 Cliente: "Looker Studio so com GA4 connector — vale BQ?"

**Resposta calibrada:**
"Para dashboards executivos rapidos, GA4 connector e suficiente (cards agregados, filtros simples). Para qualquer um destes, BigQuery e melhor:

- Dataset >= 10M events em janela (sample em GA4 connector).
- Cardinalidade alta (>50k rows; GA4 connector trunca).
- Joins com CRM/ERP/dados externos.
- Retention >14 meses.
- Funnel/path/cohort customizado SQL.
- Real-time (streaming export).
- Compartilhar dashboard com 50+ usuarios sem rate limit.

Custo: free tier 1TB queries + 10GB storage cobre PME BR (3-5GB/mo events tipico). Acima, $5/TB queried. Otimizar com `_TABLE_SUFFIX` partition pruning + materialized views.

Recomendacao: comecar com GA4 connector para 80% dos dashboards executivos. Migrar para BQ connector dashboards profundos."

### 16.5 Cliente: "Consent Mode v2 — Basic ou Advanced?"

**Resposta calibrada:**
"**Advanced.** Razoes:

1. **Modeling de Google funciona so com Advanced.** Google extrapola conversoes nao consentidas via behavioral modeling. Em mercados EU, modeling recovery 30-60% das conversoes "perdidas". Sem Advanced, este recovery nao acontece.
2. **Basic = bloqueio total ate consent.** Sem consent = zero data. Basic so faz sentido em casos ultra-strict (saude, seguros) com risk legal proibitivo.
3. **TCF v2.3 mandatory 28-Fev-2026.** Implementacao Advanced + CMP TCF v2.3 cobre LGPD + GDPR + ANPD via mesma infra.
4. **Cookieless ping** em Advanced manda sinal anonimo (sem cookies) ate consent — Google usa para modeling. Privacy-respecting.

Setup minimo: gtag + 4 consent signals (`ad_storage`, `analytics_storage`, `ad_user_data`, `ad_personalization`) inicializados como `denied` antes de qualquer Google tag. CMP onaccept atualiza para `granted`.

CMPs recomendadas BR 2026: Cookiebot (gratis ate 100 paginas), Iubenda (BR-popular), OneTrust (enterprise), CookieFirst (simples)."

---

## 17. Checklist de Contraditorio Interno

Antes de fechar uma resposta GA4, rodar:

- [ ] Citei diferenca event-based vs session-based quando relevante?
- [ ] Atualizei terminologia para 2026 (Key Events, nao "Conversions"; Engagement Rate, nao Bounce Rate como KPI primario)?
- [ ] Considerei limite 500 distinct event names + 30 Key Events + 50 Custom Dimensions?
- [ ] Recomendei Recommended events antes de Custom?
- [ ] Citei BigQuery export quando volume/retention justifica?
- [ ] Verifiquei se cliente esta no EEA OU usa Google Signals -> Consent Mode v2 mandatory?
- [ ] Cross-checkei com Google Ads / GSC / CRM em casos de discrepancia?
- [ ] Citei sample 10M default em Explorations + workaround BQ?
- [ ] Verifiquei retention 14 meses (Standard) ou 38 (360)?
- [ ] DDA default mencionado em casos de attribution?
- [ ] Considerei nuance Brasil (LGPD, ANPD, padroes Magalu/Mercado Livre/Nubank)?
- [ ] Disclaimer educational + volatility high (3 meses) ressaltado?
- [ ] Cross-skill: `conhecimento-meta-ads`, `conhecimento-google-ads`, `conhecimento-search-console`, `conhecimento-conar-cdc`, `seo-tecnico`, `metricas-marketing`, `funil-jornada`, `dominio-juridico-mkt`?

---

## 18. Referencias

### 18.1 Documentacao oficial Google

- [Google Analytics Help Center](https://support.google.com/analytics)
- [Google Analytics for Developers](https://developers.google.com/analytics)
- [GA4 Data Collection guide](https://developers.google.com/analytics/devguides/collection/ga4)
- [GA4 Changelog (Measurement Protocol + Events)](https://developers.google.com/analytics/devguides/collection/protocol/ga4/changelog)
- [GA4 Recommended events](https://support.google.com/analytics/answer/9267735)
- [GA4 Ecommerce events](https://support.google.com/analytics/answer/12200568)
- [GA4 Funnel exploration](https://support.google.com/analytics/answer/9327974)
- [GA4 Path exploration](https://support.google.com/analytics/answer/9317498)
- [GA4 Cohort exploration](https://support.google.com/analytics/answer/9670133)
- [GA4 Default channel group](https://support.google.com/analytics/answer/9756891)
- [GA4 Data retention](https://support.google.com/analytics/answer/7667196)
- [GA4 BigQuery Export schema](https://support.google.com/analytics/answer/7029846)
- [GA4 BigQuery Export setup](https://support.google.com/analytics/answer/9358801)
- [Looker Studio](https://lookerstudio.google.com)
- [Google Tag Manager Help](https://support.google.com/tagmanager)
- [Server-side Tag Manager](https://developers.google.com/tag-platform/tag-manager/server-side)
- [Consent Mode v2](https://developers.google.com/tag-platform/security/guides/consent)
- [User Deletion API](https://developers.google.com/analytics/devguides/config/userdeletion/v1)

### 18.2 Migracao + audit

- [Nicola Lazzari — GA4 Migration Guide 2026](https://nicolalazzari.ai/articles/google-analytics-vs-ga4-migration-guide)
- [InfluencerDB — GA4 Migration 2026 Guide](https://influencerdb.net/analytics/ga4-migration/)
- [E-CENS — GA4 Enterprise 12-Week Framework](https://e-cens.com/blog/ga4-migration-services-for-enterprise-a-12-week-framework/)
- [Trackingplan — GA4 Migration Checklist](https://webflow.trackingplan.com/guides/ga4-migration-checklist-transition-guide)
- [Digital Applied — GA4 Adoption Stats 2026](https://www.digitalapplied.com/blog/google-analytics-statistics-2026-ga4-adoption)
- [Ankit Nagarsheth — Doing GA4 in 2026 (post-cookie era)](https://ankitnagarsheth.medium.com/doing-ga4-in-2026-the-definitive-guide-to-google-analytics-in-the-post-cookie-era-c717faed2033)
- [Tatvic — Everything GA4 in 2026](https://www.tatvic.com/blog/everything-you-need-to-know-about-google-analytics-4-ga4-in-2025/)
- [InfluenceFlow — GA4 Conversion Tracking 2026](https://influenceflow.io/resources/google-analytics-4-conversion-tracking-complete-guide-for-2026/)
- [Analytics Help — UA->GA4 Migration legacy](https://support.google.com/analytics/answer/10607999)

### 18.3 Explorations + analise

- [Goodish — 2026 GA4 Funnel & Path Masterclass](https://goodish.agency/the-2026-analysis-hub-masterclass-in-ga4-funnel-path-explorations/)
- [AnalyticsMania — Funnel Exploration GA4](https://www.analyticsmania.com/post/funnel-analysis-report-in-google-analytics-4/)
- [AnalyticsMania — Path Exploration GA4 2026](https://www.analyticsmania.com/post/how-to-do-path-analysis-in-google-analytics-4/)
- [Anomaly AI — GA4 Custom Report Builder 2026](https://www.findanomaly.ai/ga4-custom-report-builder-guide)
- [EasyInsights — Funnel Exploration Complete](https://easyinsights.ai/blog/explorations-in-ga4-funnel-exploration/)
- [MeasureSchool — Funnel Exploration Report GA4](https://measureschool.com/funnel-exploration-report-in-ga4/)
- [data-community.publishing.service.gov.uk — GA4 funnel explorations](https://docs.data-community.publishing.service.gov.uk/analysis/govuk-ga4/use-ga4/funnel-explorations/)
- [MRS Digital — GA4 Explorations Step-by-Step](https://mrs.digital/blog/ga4-explorations-step-by-step-guide/)

### 18.4 BigQuery + Looker Studio

- [Anomaly AI — Connect GA4 to Looker Studio 2026](https://www.findanomaly.ai/connect-ga4-to-looker-studio-complete-guide)
- [Seresa — GA4 Looker vs BigQuery connector](https://seresa.io/blog/ga4-measurement-protocol/ga4-looker-studio-connector-vs-bigquery-connector-why-the-free-native-option-costs-you-data)
- [Anomaly AI — GA4 Data Analysis Tools 2026](https://www.findanomaly.ai/ga4-data-analysis-tools-2026)
- [GA4BigQuery — Lightning fast Looker Studio dashboard](https://www.ga4bigquery.com/how-to-create-a-low-cost-lightning-fast-ga4-looker-studio-dashboard-powered-by-the-bigquery-export/)
- [Paolo Bietolini — GA4 BigQuery Cost Optimization](https://paolobietolini.com/analytics/ga4-bigquery-export-cost/)
- [Looker Studio Masterclass — Optimize GA4 BQ Looker](https://lookerstudiomasterclass.com/blog/optimize-ga4-bigquery-integration-looker-studio)
- [OWOX — GA4 BigQuery Looker Studio Dashboard](https://www.owox.com/blog/articles/ga4-bigquery-export-building-looker-studio-dashboard)
- [Seresa — WordPress BigQuery Looker Pipeline 2026](https://seresa.io/blog/bigquery-data-warehousing/build-your-own-analytics-stack-wordpress-to-bigquery-to-looker)
- [GA4BigQuery — Introduction GA4 BigQuery](https://www.ga4bigquery.com/introduction-to-google-analytics-4-ga4-export-data-in-bigquery/)
- [DiveTeam — BigQuery + Looker + GA4](https://dive.team/news-blog/using-bigquery-and-looker-studio-with-google-analytics-4)

### 18.5 Consent Mode v2 + LGPD/GDPR

- [SecurePrivacy — Consent Mode GA4 CMP 2025](https://secureprivacy.ai/blog/google-consent-mode-ga4-cmp-requirements-2025)
- [CookieHub — Consent Mode V2](https://www.cookiehub.com/blog/what-is-google-consent-mode-v2)
- [MonsterInsights — GA Cookies & Consent](https://www.monsterinsights.com/guide-to-google-analytics-cookies-consent-in-ga4/)
- [Usercentrics — Google Consent Mode Implementation](https://usercentrics.com/knowledge-hub/google-consent-mode/)
- [Venue Cloud — sGTM + Consent Mode v2](https://venue.cloud/news/insights/cookieless-measurement-done-right-server-side-tagging-ga4-consent-mode-v2)
- [Cookie-Script — Is GA4 GDPR Compliant?](https://cookie-script.com/blog/google-analytics-4-and-gdpr)
- [UniConsent — Consent Mode V2 Explained](https://www.uniconsent.com/blog/google-consent-mode-v2-explained)
- [Cookie-Script — GA Cookies in GA4](https://cookie-script.com/blog/google-analytics-cookies)
- [TinyCookie — Does GA require consent?](https://tinycookie.com/blog/google-analytics-cookies/)
- [CookieFirst — Consent Mode V2 Released](https://cookiefirst.com/google-consent-mode-v2-released/)
- [ANPD - Autoridade Nacional de Protecao de Dados](https://www.gov.br/anpd)
- [LGPD Lei 13.709/2018](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm)

### 18.6 GTM + sGTM server-side

- [JENTIS — Server-side GTM Overview](https://www.jentis.com/blog/server-side-google-tag-manager-overview)
- [Google Developers — Tag Manager Server-side](https://developers.google.com/tag-platform/tag-manager/server-side)
- [Ceaksan — sGTM 2026 Cloud Run vs Stape](https://ceaksan.com/en/gtm-server-side-tagging)
- [Data-Marketing-School — GTM Server Side Tracking](https://data-marketing-school.com/en/blog/google-tag-manager/server-side-tagging/)
- [EdgeAngel — sGTM Architecture & Governance 2026](https://edgeangel.co/en/notes/server-side-tagging-avec-google-tag-manager)
- [AnalyticsMania — GTM Server-side Guide](https://www.analyticsmania.com/post/introduction-to-google-tag-manager-server-side-tagging/)
- [Napkyn — sGTM What Marketers Need to Know](https://www.napkyn.com/blog/server-side-tagging-with-google-tag-manager)
- [FiveNineStrategy — sGTM vs Google Tag Gateway](https://fiveninestrategy.com/google-tag-gateway-vs-server-side-gtm/)
- [Bounteous — Server-Side Analytics 2026 and Beyond](https://www.bounteous.com/insights/2026/03/02/server-side-analytics-2026-and-beyond/)
- [Stape — Server-Side Tracking 2026](https://stape.io/blog/how-to-start-with-server-side-tracking)
- [Simo Ahava blog (ground-truth)](https://www.simoahava.com)

### 18.7 Ecommerce GA4

- [Google Developers — Measure ecommerce](https://developers.google.com/analytics/devguides/collection/ga4/ecommerce)
- [Analytics Help — Set up ecommerce events](https://support.google.com/analytics/answer/12200568)
- [InfluencerDB — Enhanced Ecommerce GA4](https://influencerdb.net/analytics/enhanced-ecommerce-ga4/)
- [Napkyn — GA4 Ecommerce Tracking Setup](https://www.napkyn.com/blog/how-to-set-up-ga4-ecommerce-tracking)
- [HTT — GA4 Ecommerce + DataLayer](https://www.htt.it/en/ga4-ecommerce-setup-events-conversions-server-side-tracking/)
- [Ceaksan — GA4 Ecommerce Events DataLayer](https://ceaksan.com/en/gtm-enhanced-ecommerce-events)
- [Simo Ahava — GA4 Ecommerce GTM](https://www.simoahava.com/analytics/google-analytics-4-ecommerce-guide-google-tag-manager/)
- [Magefan — Top 10 Ecommerce Events GA4](https://magefan.com/blog/ecommerce-events-to-track-in-ga4)
- [Propellernet — Data Layers GA4 Ecommerce](https://www.propellernet.co.uk/insights/data-layers-for-enhanced-ecommerce-guide/)

### 18.8 Tools + alternativas

- [Mixpanel](https://mixpanel.com)
- [Amplitude](https://amplitude.com)
- [Heap](https://heap.io)
- [Hotjar](https://www.hotjar.com)
- [FullStory](https://www.fullstory.com)
- [Segment.com (CDP)](https://segment.com)
- [Snowplow (open analytics)](https://snowplow.io)
- [Plausible (privacy-first)](https://plausible.io)
- [Matomo (open-source)](https://matomo.org)
- [PostHog (product analytics open-source)](https://posthog.com)

### 18.9 BR-specific + cases

- [Magazine Luiza — Tech Blog](https://luizalabs.com)
- [Mercado Livre — Tech](https://mercadolibre.tech)
- [Nubank — Engineering Blog](https://building.nubank.com.br)
- [iFood — Tech](https://ifoodideas.com.br)

---

## 19. Integracao com o ecossistema Frank-MKT

- **Acoplamento com `conhecimento-meta-ads`** (sister) — CAPI Meta + GA4 cross-source attribution; Consent Mode v2 cobre ambos.
- **Acoplamento com `conhecimento-google-ads`** (sister) — Key Events GA4 importadas como Conversions Google Ads; DDA default coerente.
- **Acoplamento com `conhecimento-linkedin-ads`** (sister) — LinkedIn Insight Tag + GA4 cross-source para B2B; UTMs disciplinadas.
- **Acoplamento com `conhecimento-search-console`** (sister) — GSC + GA4 linker para query-level data; `landing_page` + `query` cross-tab.
- **Acoplamento com `conhecimento-conar-cdc`** (sister) — LGPD + ANPD compliance contexto BR; Consent Mode v2 + CMP profissional.
- **Acoplamento com `seo-tecnico`** — CWV (LCP/INP/CLS) impacto em `engagement_time_msec`; render mode (CSR/SSR/SSG/ISR) afeta page_view firing.
- **Acoplamento com `metricas-marketing`** — KPIs upstream (CAC, LTV, ROAS, MRR) que entram em GA4 via Key Events / Custom Dimensions.
- **Acoplamento com `funil-jornada`** — AARRR mapeado em events GA4 (Acquisition=`first_visit`, Activation=`tutorial_complete`, Retention=`session_start` recurring, Referral=`share`, Revenue=`purchase`).
- **Acoplamento com `dominio-juridico-mkt`** — LGPD compliance + politicas de privacidade que sustentam Consent Mode v2.
- **Acoplamento com `email-marketing`** — UTM disciplina para email + GA4 default channel `Email`.
- **Acoplamento com `copywriting-conversao`** — A/B test events customizados; eventos `experiment_id` + `variant`.
- **Acoplamento com `microcopy`** — micro-eventos de UX (form_field_focus, form_validation_error) ajudam debug funnel drop-off.
- **Acoplamento com `dominio-empreendedorismo-mkt`** — founder + dev setup canonico desde dia 1.
- **Acoplamento com o agente `auditor`** — auditor roda regras PASS/FAIL em GA4 setup (BigQuery export ON, Consent Mode v2 deployed, Key Events <=10, dataLayer documented, audit pos-migracao done, retention 14m+, predictive metrics requirements met).
- **Memoria** — `.frank-mkt/ga4/<cliente>/<data>/` (audits, dataLayer specs, Looker Studio templates, BigQuery queries cookbook).
- **Contraditorio interno** — Checklist Sec 17.
- **Decaimento temporal** — volatility `high` (3 meses). Google muda silenciosamente (events recomendados, defaults, limites, Consent Mode features). Re-validar tudo em `next_review`.
- **Regra de ouro para `frank-mkt`** — nenhuma decisao GA4 (audit, migracao, setup novo, Key Events, BigQuery export, sGTM, Consent Mode v2) sai do plugin sem passar por esta skill.

---

> **Aviso:** o plugin `frank-mkt` e um assistente educacional de analise. Recomendacoes desta skill sao orientativas e devem ser adaptadas ao contexto do cliente (volume de trafego, mercado regulatorio, stack tecnico, time interno) + validadas com testes reais (DebugView, Tag Assistant, BigQuery cross-check) antes de aplicar em property de producao. **Volatility `high` (3 meses)** — Google atualiza GA4 silenciosamente (events, defaults, limites, Consent Mode); re-validar antes de publicar peca formal. Nao substitui consultoria especializada em casos de migracao enterprise, regulatory-strict (saude, financeiro), ou setups multi-stream complexos. Esta skill nao oferece consultoria juridica LGPD — combinar com `dominio-juridico-mkt` + DPO interno do cliente.

---

*Plugin `frank-mkt` — skill `conhecimento-ga4` (v0.1.0)*
*Ultima atualizacao: 2026-05-09*
*Pesquisa de campo: 6 web searches em 2026-05-09 (GA4 2026 framework event model migration, GA4 Explorations 2026 funnel path segments, GA4 BigQuery export 2026 Looker Studio, GA4 Consent Mode v2 2026 LGPD GDPR third-party cookies, GTM Server-side sGTM 2026, GA4 ecommerce 2026 enhanced events tracking)*

Sources used in field research (web search 2026-05-09):
- [Nicola Lazzari — GA4 Migration Guide 2026](https://nicolalazzari.ai/articles/google-analytics-vs-ga4-migration-guide)
- [Goodish — 2026 Analysis Hub Masterclass](https://goodish.agency/the-2026-analysis-hub-masterclass-in-ga4-funnel-path-explorations/)
- [Anomaly AI — Connect GA4 to Looker Studio 2026](https://www.findanomaly.ai/connect-ga4-to-looker-studio-complete-guide)
- [SecurePrivacy — Consent Mode GA4 CMP](https://secureprivacy.ai/blog/google-consent-mode-ga4-cmp-requirements-2025)
- [Ceaksan — sGTM 2026 Cloud Run vs Stape](https://ceaksan.com/en/gtm-server-side-tagging)
- [Bounteous — Server-Side Analytics 2026 and Beyond](https://www.bounteous.com/insights/2026/03/02/server-side-analytics-2026-and-beyond/)
- [Google Developers — Measure ecommerce GA4](https://developers.google.com/analytics/devguides/collection/ga4/ecommerce)
- [Simo Ahava — GA4 Ecommerce GTM](https://www.simoahava.com/analytics/google-analytics-4-ecommerce-guide-google-tag-manager/)
- [Digital Applied — GA4 Adoption Stats 2026](https://www.digitalapplied.com/blog/google-analytics-statistics-2026-ga4-adoption)
- [Ankit Nagarsheth — Doing GA4 in 2026](https://ankitnagarsheth.medium.com/doing-ga4-in-2026-the-definitive-guide-to-google-analytics-in-the-post-cookie-era-c717faed2033)
