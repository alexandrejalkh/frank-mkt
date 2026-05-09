---
name: conhecimento-search-console
description: Conhecimento Google Search Console (GSC) 2026 (Performance reports queries/pages/countries/devices + Index Coverage + Core Web Vitals LCP/INP/CLS + URL Inspection + Sitemaps XML + robots.txt + Manual Actions + Security Issues + GSC API extraction + Bing Webmaster Tools IndexNow complement + AI Overviews tracking 2024-2026) para SEO managers/CMO/founders/devs/agencias, com cobertura Core Web Vitals INP substituiu FID Mar-2024 + AI Overviews SGE rollout 2024-2026 + GSC tracking SGE impressions parcial + Bing IndexNow protocol Microsoft + Indexing API Google jobs/livestreams. 5a SKILL Bloco Conhecimento de Plataforma.
volatility: high
last_review: 2026-05-09
next_review: 2026-08-09
languages: [pt-BR]
audience: [SEO-managers, CMO, founders, devs, agencias, content-marketers, technical-SEO]
ascii_only: true
---

# Skill: conhecimento-search-console

> **Decaimento Temporal**
> Ultima verificacao: 2026-05-09 | Proxima revisao: 2026-08-09 | Volatility: **HIGH** (3 meses)
> SEO + AI search mudam rapido. Google Search Console (GSC) recebeu mudancas profundas 2024-2026 (INP substituiu FID em Mar-2024, AI Overviews/SGE expandiu para >48% das SERPs em 2026, GSC adicionou AI Mode tracking em Jun-2025, Bing fortaleceu IndexNow alimentando Copilot/ChatGPT). Re-validar antes de qualquer peca formal:
> - Google Search Central — https://developers.google.com/search
> - GSC oficial — https://search.google.com/search-console
> - Search Console Help — https://support.google.com/webmasters
> - web.dev (CWV) — https://web.dev/articles/vitals
> - Google Search Status Dashboard — https://status.search.google.com
> - Bing Webmaster Tools — https://www.bing.com/webmasters
> - IndexNow protocolo — https://www.indexnow.org
>
> **Acionamento:** queda de trafego organico, drop pos-update Google, indexacao falha em massa, CWV ruim no GSC, manual action recebida, security issue notificada, hreflang quebrado, monitoramento mensal, planejamento SEO trimestral, AI Overviews tracking, Bing/IndexNow setup, extraction de dados via API.
> **Skills relacionadas:** `seo-tecnico` (execucao tecnica), `seo-fundamentos` (modelo mental), `seo-on-page`, `seo-keywords`, `conhecimento-google-ads` (cross-channel SEM/SEO), `conhecimento-meta-ads` + `conhecimento-linkedin-ads` (atribuicao multi-canal), `conhecimento-ga4` (correlacao trafego), `conhecimento-conar-cdc` (compliance content), `metricas-marketing` (KPIs), `comunicacao-corporativa` (GEO — generative engine optimization).
> **Pre-requisito recomendado:** ter carregado `seo-fundamentos` para entender pipeline crawl/render/index/rank antes de operar GSC.

---

## 1. Visao Geral

Google Search Console (GSC) — antigo Google Webmaster Tools — e o **painel oficial gratuito do Google para webmasters/SEOs**. E a unica fonte primaria de dados sobre como o Google ve, rastreia, indexa e exibe um site na Busca. Fora de GSC, qualquer numero "de SEO" e estimativa terceirizada (Ahrefs, Semrush, Moz). Dentro de GSC, o numero e o que o Google de fato registra.

Em 2026, GSC nao e mais "ferramenta de tecnico" — e instrumento de **decisao de negocio** para CMO, founders, agencias e content marketers. Trafego organico continua sendo o canal mais barato em CAC para muitos negocios, e GSC e o termometro deste canal.

### 1.1 Mudancas estruturais 2024-2026

- **Mar-2024**: INP (Interaction to Next Paint) substituiu FID (First Input Delay) como Core Web Vital de responsividade. Threshold "Good" <200ms.
- **Mai-2024**: Google lancou AI Overviews (renomeacao do SGE — Search Generative Experience) em US, expandindo globalmente ao longo de 2024-2025.
- **Jun-2025**: GSC adicionou tracking de AI Mode (impressoes/cliques de AI Overviews) ao Performance Report — antes invisivel.
- **2024-2026**: AI Overviews atinge >48% das queries em Mar-2026 (vs 6.5% ano anterior — crescimento Y-o-Y de ~58 p.p. segundo Searchlab).
- **2024-2026**: Bing IndexNow consolidado — 5+ bilhoes de submissoes diarias; alimenta Microsoft Copilot, ChatGPT search, DuckDuckGo. Google **nao adotou** IndexNow ate Fev-2026.
- **2024-2026**: GSC introduziu views weekly/monthly + AI-powered config no Performance (linguagem natural para filtros).
- **2026**: Apenas 47% dos sites batem CWV thresholds; 43% falham INP — gap competitivo claro.

### 1.2 GSC nao e GA4 — diferencas criticas

| Aspecto | GSC | GA4 |
|---------|-----|-----|
| Origem do dado | Google (lado do crawler/SERP) | Tag no site (lado do browser) |
| O que mede | Cliques, impressoes, CTR, posicao em SERP | Sessoes, eventos, conversoes pos-clique |
| Atribuicao | Pre-clique (SERP) | Pos-clique (jornada no site) |
| Privacidade | Anonimizado por queries de baixo volume | Sujeito a LGPD/GDPR (consent) |
| Retencao | 16 meses (UI) / ilimitado via BigQuery export | Configuravel (max 14 meses por padrao GA4) |
| Sampling | Threshold de privacidade (queries unicas omitidas) | Sampling em queries grandes (UI) |

**Implicacao**: cliques GSC ≠ sessoes GA4. Diferencas de 5-15% sao normais (bots, prerenders, queries omitidas, JS bloqueado). Nao "conciliar a forca".

### 1.3 Acionamento — quando esta skill carrega

| Gatilho | Exemplo de pergunta |
|---------|---------------------|
| Queda de trafego organico | "Cai 30% em 3 dias — foi update Google?" |
| Drop pos-core-update | "Mar-2026 update bateu, como diagnostico?" |
| Indexacao falha em massa | "5k URLs em 'Crawled — currently not indexed'" |
| CWV ruim | "INP vermelho em 60% das paginas mobile" |
| Manual action | "Recebi notificacao de spam manual" |
| Security issue | "Pagina hackeada, site marcado como inseguro" |
| AI Overviews tracking | "Quero ver impressoes em AI Mode" |
| Bing/IndexNow setup | "Como configurar IndexNow para o blog?" |
| Migration playbook | "Trocando dominio, como minimizar perda" |
| Reporting C-level | "CMO quer dashboard mensal de SEO" |

---

## 2. GSC Foundations + Setup

### 2.1 Property types — Domain vs URL prefix

GSC tem **dois tipos de property** com implicacoes diferentes:

| Tipo | O que cobre | Verificacao |
|------|-------------|-------------|
| **Domain property** | Todos os subdominios + protocolos (`www`, `m.`, `blog.`, `http`, `https`) | DNS TXT record (apenas) |
| **URL prefix property** | Apenas o prefixo exato (`https://www.exemplo.com.br/`) | DNS, HTML file, HTML tag, GA, GTM |

**Recomendacao 2026**: criar **Domain property** (cobertura total) + URL prefix properties especificas (para subdiretorios `/blog/`, `/loja/`) quando precisa segmentar relatorios.

### 2.2 Verification methods (5 metodos)

1. **DNS TXT record** (recomendado p/ Domain) — adicionar TXT no painel do registrar (Registro.br, GoDaddy, Cloudflare).
2. **HTML file upload** — subir arquivo `googleXXXX.html` na raiz do site.
3. **HTML meta tag** — adicionar `<meta name="google-site-verification">` no `<head>`.
4. **Google Analytics** — usar tag GA4 ja instalada (precisa Edit no GA).
5. **Google Tag Manager** — usar container GTM (precisa Publish).

> **Cristal C1 — VERIFICAR DOMAIN PROPERTY.** Sempre criar Domain property primeiro. URL prefix sozinho perde dados de subdominios e protocolos alternativos. Se cliente tem `www` e `naked domain` ambos respondendo, perde metade dos dados.

### 2.3 Permissions — Owner / Full / Restricted

| Role | O que pode fazer |
|------|------------------|
| **Owner** | Tudo + adicionar/remover usuarios + remover property |
| **Full user** | Ver tudo + usar URL Inspection + submeter sitemaps + ver Manual Actions |
| **Restricted user** | Ver maioria dos dados (read-only essencialmente) |

> **Cristal C2 — NAO COMPARTILHAR OWNER.** Cliente cede Owner -> agencia pode acidentalmente remover property + perder historico de 16 meses. Sempre Full user para agencias; Owner so para CTO/dev interno.

### 2.4 Multi-property strategy (sites grandes)

- **Domain property raiz** -> visao macro.
- **URL prefix por idioma** (`/pt-br/`, `/en/`, `/es/`) -> performance por mercado.
- **URL prefix por tipo** (`/blog/`, `/loja/`, `/help/`) -> performance por linha.
- **URL prefix por subdominio** (`blog.exemplo.com`, `app.exemplo.com`) -> isolar.

---

## 3. Performance Reports

O **Performance Report** e o coracao de GSC — onde 80% do uso operacional acontece.

### 3.1 Quatro metricas-base

| Metrica | Definicao | Como interpretar |
|---------|-----------|------------------|
| **Cliques** | Cliques no resultado SERP | Trafego real organico (pre-anonimizacao GA4) |
| **Impressoes** | Quantas vezes URL apareceu em SERP visivel | Demanda + cobertura |
| **CTR** | Cliques / Impressoes | Atratividade do snippet (title + meta + rich result) |
| **Posicao media** | Media ponderada de posicao quando apareceu | Ranqueamento — interpretar com cuidado (media nao-linear) |

### 3.2 Cinco dimensoes de breakdown

1. **Queries** (palavras-chave) — anonimizadas para queries de baixo volume (privacidade).
2. **Pages** (URLs) — quais paginas aparecem em SERP.
3. **Countries** — onde o trafego vem.
4. **Devices** — Desktop / Mobile / Tablet.
5. **Search appearance** — rich result (FAQ, Review, Recipe, Job, Video, Product, AI Overviews citation, etc).

> **Cristal C3 — POSICAO MEDIA E ARMADILHA.** Posicao media de "5.2" pode significar "rankeia 1 em 50% das vezes e 10 em 50%" OU "rankeia 5-6 sempre". Sao realidades comerciais opostas. Sempre cross-checar com distribuicao de cliques + breakdown por query.

### 3.3 Filtros + comparacoes

- **Filtros**: query (contains/regex/exact), page, country, device, search appearance, search type (Web/Image/Video/News/Discover).
- **Comparacoes**: data range (last 28d vs prev 28d), Y-o-Y, queries A vs B, paginas A vs B.

**Use case 2026**: AI-powered config no Performance permite linguagem natural — "compare last month vs same month last year for queries containing 'free trial' on mobile". Lancado mid-2025, amadurecido 2026.

### 3.4 Retencao + limites

- **UI**: 16 meses rolling.
- **BigQuery export** (gratis, opcional desde Fev-2023): historico ilimitado, dado raw, sem sampling, sem anonimizacao via threshold (ainda anonimiza queries privadas).
- **Sampling**: queries unicas com volume baixo (~5 cliques/mes em alguns casos) sao agregadas como "anonymized query".
- **Cap por query API**: 50.000 rows/request, ate 25.000 rows com paginacao.

### 3.5 Search type — Web / Image / Video / News / Discover

- **Web**: trafego de busca tradicional (default).
- **Image**: Google Images (relevante p/ ecommerce, fotografia, receitas).
- **Video**: video carousel + video page.
- **News**: Top Stories + Google News (precisa registro em Publisher Center).
- **Discover**: feed mobile (Android Google app + Chrome mobile) — alta volatilidade, sem control direto.

> **Cristal C4 — DISCOVER E LOTERIA.** Trafego Discover pode 10x ou 0.1x sem mudanca tecnica — algoritmo de feed e opaco. Nunca prometer entrega de Discover ao cliente.

### 3.6 KPIs operacionais Brasil 2026

- **CTR mediana** posicao 1 organica: ~28-32% (queda de ~31.7% para ~23.4% quando ha AI Overview presente — Searchlab 2026).
- **CTR mediana** posicao 5: ~4-6%.
- **CTR mediana** posicao 10: ~2-3%.
- **Impressoes/clique benchmark Brasil**: varia por nicho (ecommerce ~4-8%, B2B SaaS ~2-4%, juridico/saude ~3-6%).
- **AI Overviews impact**: -18% a -25% trafego organico em queries onde aparece (Searchlab 2026).

---

## 4. Index Coverage + URL Inspection

### 4.1 Pages report (ex-Index Coverage)

Renomeado de "Index Coverage" -> "Pages" em 2022-2023. Mostra **status de indexacao por URL**:

| Status | Significado | Acao |
|--------|-------------|------|
| **Indexed** (Valid) | Indexada e elegivel a aparecer em SERP | Monitorar |
| **Not indexed** | Excluida — varias razoes | Investigar |

**Sub-razoes "Not indexed"** (top 10 mais comuns 2026):

1. **Crawled — currently not indexed** — Google rastreou mas decidiu nao indexar (qualidade percebida baixa).
2. **Discovered — currently not indexed** — Google sabe que existe mas nao rastreou ainda (crawl budget).
3. **Duplicate without user-selected canonical** — Google escolheu outro canonical.
4. **Duplicate, Google chose different canonical than user** — Google ignorou seu `rel=canonical`.
5. **Page with redirect** — 301/302 — destino e o que importa.
6. **Not found (404)** — URL retornou 404.
7. **Soft 404** — pagina retorna 200 mas conteudo parece "vazio" (Google detecta).
8. **Blocked by robots.txt** — bloqueado intencionalmente (verificar se intencional).
9. **Excluded by 'noindex' tag** — meta robots noindex.
10. **Server error (5xx)** — origem retornou 500/502/503 quando crawler tentou.

> **Cristal C5 — "CRAWLED NOT INDEXED" E SINTOMA DE CONTEUDO RUIM.** Em massa, indica que Google avaliou e descartou. Solucoes: melhorar profundidade do conteudo, consolidar paginas thin, usar EEAT signals, melhorar internal linking.

### 4.2 URL Inspection Tool

Ferramenta crucial para diagnosticar **uma URL especifica** em tempo real ou no indice.

**Duas visoes**:
1. **Indexed Version** — o que Google tem armazenado (ultimo crawl).
2. **Live Test** — refaz crawl agora (com ou sem JS render).

**Componentes do report**:
- **URL is on Google / not on Google**.
- **Coverage** — Last crawl, Crawled as (Smartphone/Desktop), Crawl allowed, Page fetch, Indexing allowed.
- **Enhancements** — rich results detectados (Schema), CWV, Mobile usability.
- **View Crawled Page** — HTML renderizado (pos-JS), screenshot, HTTP response, blocked resources, JS console messages.

### 4.3 Mobile-first indexing (default 2026)

- **Crawled as: Googlebot Smartphone** -> mobile-first ATIVO (default desde 2020 para sites novos; 100% rollout em 2024).
- Tudo que nao esta no HTML mobile **nao existe para SEO**.
- Bug pattern comum 2024-2026: dev esconde conteudo em mobile via `display:none` -> Google nao indexa.

### 4.4 Live Test vs Indexed Version

| Caso | Use Live Test | Use Indexed Version |
|------|---------------|----------------------|
| Mudou template, precisa validar render | Sim | Nao |
| Conteudo nao aparece em SERP, suspeita render | Sim | Sim (comparar) |
| Verificar Schema deployado hoje | Sim | Nao (pode demorar) |
| Verificar canonical efetivo | Nao | Sim |
| Verificar mobile usability historica | Nao | Sim |

### 4.5 Request indexing (rate-limited)

Botao "Request indexing" -> envia URL para fila de crawl prioritario.
- **Limite**: ~10-15 URLs/dia por property (varia, nao publicado).
- **Tempo**: 1 hora a 7 dias para reflectir.
- **Nao garante indexacao** — Google pode rastrear e mesmo assim descartar.

> **Cristal C6 — REQUEST INDEXING NAO RESOLVE QUALIDADE.** Submeter 100x URL ruim nao indexa. Resolva a causa (conteudo, internal linking, canonical).

---

## 5. Core Web Vitals 2026

### 5.1 Os tres CWV — thresholds atuais

| Metrica | Mede | Good | Needs Improvement | Poor |
|---------|------|------|-------------------|------|
| **LCP** (Largest Contentful Paint) | Tempo ate maior elemento renderizar | <2.5s | 2.5-4.0s | >4.0s |
| **INP** (Interaction to Next Paint) | Latencia de interacao (clique, tap) | <200ms | 200-500ms | >500ms |
| **CLS** (Cumulative Layout Shift) | Salto visual no layout | <0.1 | 0.1-0.25 | >0.25 |

**Avaliacao**: pagina passa CWV se **as tres metricas estao "Good" no percentil 75** dos usuarios reais nos ultimos 28 dias (CrUX field data).

### 5.2 INP substituiu FID (Mar-2024)

- **FID** (First Input Delay) — media SO da primeira interacao (defasada).
- **INP** — pega a interacao **pior** durante toda a sessao (mais realista).
- **Implicacao**: sites que passavam FID podem falhar INP — JS pesado em runtime (analytics, chat widget, A/B test) penaliza mais.
- **2026**: 43% dos sites falham INP — metrica mais comum de falha (Searchlab/web.dev 2026).

### 5.3 Lab vs Field (CrUX)

| Aspecto | Lab data | Field data (CrUX) |
|---------|----------|-------------------|
| Origem | PageSpeed Insights (PSI), Lighthouse | Chrome User Experience Report — usuarios Chrome reais |
| O que pesa em ranking | Nao | **Sim** |
| Quando aparece em GSC | Nao | **Sim** (28d rolling, p75) |
| Quando usar | Diagnostico tecnico, debug | Avaliacao real, ranking |
| Volume minimo | Sem | Threshold de trafego para CrUX gerar dado |

> **Cristal C7 — RANKING USA CAMPO, NAO LAB.** Lighthouse 95 nao garante CWV bom em GSC. Sempre olhar Field data (GSC + PSI mode "Field").

### 5.4 Sites com baixo trafego

CrUX precisa volume minimo (~200-500 sessoes Chrome no p75 em 28 dias) por URL ou template. Sem volume:
- GSC mostra "Insufficient data" -> usar **lab + technical proxies** (LCP element analysis no PSI).
- Agrupar por **template** (ex: produto X paginas similares).

### 5.5 Impacto em ranking 2026

- **Page experience signals** (CWV + HTTPS + mobile-friendly + no intrusive interstitials) — ranking factor confirmado desde Jun-2021.
- **Mar-2026 core update** reforcou peso de performance segundo varios casos de mercado.
- CWV **funciona como tiebreaker** entre paginas de qualidade similar — em nichos competitivos faz diferenca mensuravel.
- **Conteudo continua sendo o fator dominante** — CWV nao salva conteudo ruim.

### 5.6 Como otimizar (cross-skill seo-tecnico)

- **LCP**: imagem/video do hero -> `<link rel="preload">`, formato moderno (AVIF, WebP), CDN, server-rendered (SSR/SSG), TTFB <600ms.
- **INP**: fragmentar JS pesado, code-splitting, defer third-party (analytics, chat), reduzir long tasks (>50ms), web workers.
- **CLS**: dimensoes explicitas em img/video/iframe, reservar espaco para ads/embeds, evitar content-shift por fonts (font-display: optional).

Detalhes tecnicos profundos -> cross-skill `seo-tecnico`.

---

## 6. Sitemaps + robots.txt + Indexing

### 6.1 XML Sitemaps

**Funcao**: dizer ao Google **quais URLs existem** e quando foram modificadas. Nao garante indexacao — apenas descoberta.

**Tipos**:
- **Sitemap padrao** (URLs).
- **Sitemap index** (lista de sitemaps — necessario quando >50.000 URLs ou >50MB).
- **Image sitemap**.
- **Video sitemap**.
- **News sitemap** (publishers).
- **Hreflang in sitemap** (sites multi-idioma).

**Submissao**:
1. GSC -> Sitemaps -> Add a new sitemap -> URL relativo do sitemap.
2. `robots.txt` -> linha `Sitemap: https://exemplo.com.br/sitemap.xml` (recomendado tambem).

**Reading sitemap status no GSC**:
- **Success** -> rastreado e parseado.
- **Couldn't fetch** -> erro 4xx/5xx ou DNS.
- **Has errors** -> formatado mal (XML invalido, URLs fora do dominio).

### 6.2 robots.txt — RFC 9309 (2022)

**Funcao**: dizer ao Google **o que NAO rastrear** (Disallow). NAO impede indexacao se Google souber via outro link.

**Anatomia**:
```
User-agent: *
Disallow: /admin/
Disallow: /carrinho/

User-agent: Googlebot
Allow: /admin/public/
Disallow: /admin/

Sitemap: https://exemplo.com.br/sitemap.xml
```

**Pegadinhas comuns**:
- `Disallow: /` em prod -> deindexa site inteiro em 1-2 semanas.
- Bloquear CSS/JS -> Google nao renderiza -> CWV ruim + mobile-friendly fail.
- Confundir Disallow (crawl) com noindex (index) -> URL bloqueada por robots pode aparecer em SERP **sem snippet** ("URL bloqueada por robots.txt").

> **Cristal C8 — NAO USE ROBOTS.TXT PARA NOINDEX.** Para tirar de SERP use `<meta name="robots" content="noindex">` ou `X-Robots-Tag: noindex`. robots.txt impede crawl, nao indexacao.

### 6.3 noindex meta vs robots.txt — quando cada um

| Objetivo | Solucao |
|----------|---------|
| Esconder pasta admin do crawl (economia de budget) | robots.txt Disallow |
| Tirar URL ja indexada do indice | meta noindex (robots.txt deve PERMITIR crawl para Google ver o noindex) |
| URL existe mas e privada (login) | Auth + 401/403 |
| URL parametrizada que duplica | rel=canonical (nao bloquear) |
| Staging/dev | Auth basica + robots.txt Disallow + noindex (defesa em profundidade) |

### 6.4 Crawl budget

**Conceito**: Googlebot tem orcamento finito de URLs/dia para cada site (varia por autoridade).
**Sintoma de problema**: muitos URLs em "Discovered — currently not indexed" + spike de URLs lixo (parametros, faceted nav).
**Solucoes**:
- robots.txt Disallow em paths sem valor (filtros, sort, paginacao infinita).
- canonical para variantes.
- consolidar URLs (eliminar duplicates).
- internal linking que prioriza paginas estrategicas.
- 410 Gone para URLs mortas permanentes (vs 404).

### 6.5 Indexing API (Google) — caso especifico

**Limite oficial**: apenas para `JobPosting` e `BroadcastEvent` (livestreams). Outros usos sao **TOS violation** segundo Google.

**Funcao**: notificar Google de URL nova/atualizada/removida em tempo real.
**NAO use** para blog, ecommerce, paginas comuns -> conta com erro intermitente, e podem penalizar.
**Para casos validos** (vagas, lives): `https://indexing.googleapis.com/v3/urlNotifications:publish` via service account.

---

## 7. Manual Actions + Security Issues

### 7.1 Manual Actions

Penalizacao **manual** aplicada por revisor humano do Google (raras mas serias).

**Tipos comuns**:
- **Unnatural links to your site** (link spam recebido).
- **Unnatural links from your site** (link spam emitido).
- **Thin content with little or no added value**.
- **Pure spam**.
- **User-generated spam** (comentarios, forum sem moderacao).
- **Cloaking and/or sneaky redirects**.
- **Hidden text and/or keyword stuffing**.
- **Cloaked images** / **AMP content mismatch**.
- **Structured data issue** (schema spam).

**Onde ver**: GSC -> Security & manual actions -> Manual actions.

**Como sair**:
1. Identificar paginas/links afetados.
2. Corrigir (remove/disavow links, reescrever conteudo, remover redirects).
3. **Reconsideration request** explicando o que foi corrigido.
4. Aguardar resposta (semanas a meses).

> **Cristal C9 — RECONSIDERATION SO COM PROVA.** Pedido vago = recusa automatica. Anexar lista de URLs corrigidas, screenshots de mudancas, datas.

### 7.2 Security Issues

Avisos de site comprometido — Google avisa usuarios em SERP ("Este site pode ser perigoso").

**Tipos**:
- **Hacked content** (defacement, redirects, conteudo injetado).
- **Malware**.
- **Social engineering** (phishing).
- **Harmful downloads**.

**Como resolver**:
1. Identificar a infeccao (server logs, antivirus, escaneamento Sucuri/Wordfence).
2. Limpar (purgar arquivos infectados, atualizar CMS/plugins).
3. Trocar todas as senhas (WP admin, FTP, hosting, DB).
4. **Request review** no GSC.
5. Tipicamente 24-72h para descer aviso (Google reescaneia).

---

## 8. GSC API + Bing Webmaster Tools + AI Overviews 2024-2026

### 8.1 GSC API — extracao em escala

**Endpoint principal**: Search Analytics Query API.
**URL base**: `https://www.googleapis.com/webmasters/v3/sites/{siteUrl}/searchAnalytics/query`.

**Capacidades**:
- Pull de queries, pages, devices, countries, search appearance.
- Filtros (regex, contains, equals).
- Granularidade dia (date) ou range.
- Format: JSON.

**Limites 2026**:
- Quota gratuita: 1.200 requests/min/projeto, 30.000 requests/dia.
- 50.000 rows max por query (paginar com startRow).
- Anonimizacao de queries privadas mantida.

**Stack de automacao 2026**:
- **Python** + biblioteca oficial `google-api-python-client` ou `searchconsole` (lib comunidade).
- **Cloud Scheduler + Cloud Run/Functions** para pulls diarios.
- **BigQuery** como warehouse — alternativamente, GSC oferece **BigQuery export nativo** (gratis desde Fev-2023) que e mais simples e robusto.
- **Looker Studio** para dashboards.

**Use cases tipicos**:
- Winners & losers — comparar 28d rolling vs 28d anterior por query/page.
- Striking distance — queries em posicao 4-15 (oportunidade rapida).
- CTR gap analysis — queries com CTR muito abaixo do benchmark da posicao.
- Decay detection — paginas com queda Y-o-Y > N%.
- Cannibalization — multiplas paginas rankeando para mesma query.

### 8.2 BigQuery export nativo (recomendacao 2026)

Lancado Fev-2023, e a forma **preferida** em 2026 para datasets grandes:
- **Gratis** (custo de storage BigQuery e tipicamente <USD 5/mes para sites medios).
- **Sem sampling**.
- **Historico ilimitado** apos ativacao.
- **Daily exports** automaticos.
- Schema: `searchdata_site_impression` + `searchdata_url_impression`.

Configuracao: GSC -> Settings -> Bulk data export -> Linka projeto GCP.

### 8.3 Bing Webmaster Tools — equivalente Microsoft

**Setup**:
1. https://www.bing.com/webmasters -> sign in com Microsoft account.
2. Adicionar site — verificar via XML file, meta tag, ou CNAME.
3. Importar GSC (atalho que copia properties + sitemaps).

**Reports principais**:
- Search Performance (cliques, impressoes, CTR, posicao — analogo ao GSC).
- Site Explorer (estrutura + descobertas).
- Crawl Information.
- Sitemaps.
- Backlinks (Bing tem dado proprio — diferente de GSC).
- AI Performance Report (impressoes em Microsoft Copilot — 2026).

**Por que importa em 2026**:
- Bing alimenta **Microsoft Copilot, ChatGPT search, DuckDuckGo, Yahoo**.
- Marketshare desktop EUA: ~10-12% (vs Google ~85%) — pequeno mas crescente em SaaS B2B.
- Brasil: <5% mas crescente em corporativo.
- Custo de configurar: 30 minutos. ROI: visibilidade em superficies AI search.

### 8.4 IndexNow protocol

**O que e**: protocolo open-source (Microsoft + Yandex 2021) para notificar engines de mudancas de URL em tempo real — alternativa ao crawl tradicional.

**Quem suporta** (2026): Bing, Yandex, Naver (Coreia), Seznam (Tcheco).
**Quem NAO suporta**: **Google** (testando desde 2021, sem adocao publica em Fev-2026).

**Como funciona**:
1. Gerar chave UUID-like (32-128 chars).
2. Hospedar arquivo `{key}.txt` na raiz do site contendo a chave.
3. Em cada publish/update/delete, enviar GET para `https://api.indexnow.org/IndexNow?url={url}&key={key}`.
4. Bulk submit: ate 10.000 URLs/dia em payload JSON.

**Implementacoes prontas 2026**:
- WordPress: plugin oficial **IndexNow** (Microsoft).
- Cloudflare: integracao nativa (toggle no painel).
- Next.js / static sites: webhook em CI/CD pipeline (build hook -> POST).
- Shopify: app oficial.

**ROI 2026**: Bing reporta que **22% dos cliques em SERP do Bing vem via IndexNow** — indica que Bing prioriza descoberta por IndexNow vs crawl natural.

### 8.5 AI Overviews tracking (GSC + ferramentas)

**Estado 2026**:
- AI Overviews aparecem em **>48% das queries Google** (Mar-2026 — Searchlab).
- Crescimento Y-o-Y: ~58 p.p.
- Impacto: **-18% a -25% trafego organico** em queries com AI Overview.
- CTR posicao 1: **31.7% -> 23.4%** com AI Overview presente.

**Tracking dentro do GSC** (desde Jun-2025):
- Performance Report -> Search appearance -> filtrar **"AI Overviews"**.
- Mostra impressoes + cliques quando seu site **e citado** como fonte no AI Overview.
- **Limitacao**: so ve seu proprio site, nao competitors. Nao mostra contexto da citacao.

**Tracking fora do GSC**:
- **Manual** — query monitorada em incognito + screenshot semanal.
- **Ferramentas pagas 2026**: Otterly.AI, Keyword.com (AI Mode tracking module), SE Ranking, Semrush AI Visibility, Ahrefs AI Overview tracker.
- **Cobertura emergente**: ChatGPT (citacoes), Perplexity (sources), Microsoft Copilot, Gemini citations — ainda imaturo, sem padrao.

**Estrategia de conteudo para AI Overviews** (cross-skill `seo-on-page` + `comunicacao-corporativa` GEO):
- Conteudo com **answers diretos** a perguntas (estilo featured snippet).
- **EEAT** forte (Experience, Expertise, Authoritativeness, Trust).
- Schema.org: `FAQPage`, `HowTo`, `Article`, `Person` (autor).
- **Fontes citaveis** (linkar dados primarios, estudos, governo).
- Headers H2/H3 que respondem perguntas em <60 palavras.

> **Cristal C10 — AI OVERVIEWS PEGAM CONTEUDO E NAO RETORNAM TRAFEGO.** Em 2026, otimizar para ser citado e **necessario** (visibilidade de marca) mas pagar a conta com cliques perdidos. Diversificar canais — nao depender 100% de Google organic.

---

## 9. Brasil 2026 — Especificidades

### 9.1 Pesquisa em portugues — implications

- **Stemming + stopwords** PT-BR diferente de EN — Google trata "como fazer" / "fazer como" como mesma intent (na maioria das vezes).
- **Acentuacao**: Google trata "café" e "cafe" como variantes (~95% dos casos).
- **Plurais**: tratados como variantes (singular/plural).
- **Long-tail PT-BR** geralmente mais barato em CTR/posicao do que long-tail EN equivalente — menos competicao.
- **Variantes regionais** (PT-BR vs PT-PT vs PT-AO): hreflang `pt-BR`, `pt-PT`, `pt-AO` ajuda; sem hreflang Google escolhe por sinais (geo do servidor, cTLD, language tags).

### 9.2 Hospedagem BR vs USA — latency

- **TTFB Brasil-Brasil**: 50-150ms (CDN BR ou origem em SP/RJ).
- **TTFB USA-Brasil**: 180-300ms (sem CDN).
- **CDN com PoP Brasil** (Cloudflare, Fastly, AWS CloudFront SP/RJ, Akamai): equaliza TTFB ~80-120ms para usuario BR mesmo com origem USA.
- **Implicacao CWV**: TTFB ruim afeta LCP — sites com origem USA + CDN ruim falham CWV no GSC para audiencia BR.

### 9.3 Cases brasileiros 2024-2026

**Magalu (Magazine Luiza)** — investimento em CWV + SEO tecnico desde 2020; em 2024-2025 reportou ganho de cliques organicos pos-otimizacoes INP em paginas de produto. Padrao publico: Next.js + edge rendering + CDN agressivo.

**Mercado Livre** — escala >100M URLs por pais; estrategia publica documentada de canonical + faceted nav controlada via robots.txt + canonical para variantes de filtro. Caso de estudo classico de crawl budget em ML scale.

**iFood** — investimento em Schema.org `Restaurant` + `Menu` + `Review` para rich results em SERP local. GSC -> Search appearance mostra distribuicao por rich result.

**(Casos genericos — sempre cross-checar com material publico oficial das empresas antes de citar em peca formal)**.

### 9.4 LGPD compliance + robots.txt scraping

**LGPD vs scraping**: LGPD nao impede crawl de Googlebot (interesse legitimo + pagina publica = OK). Mas:
- **Dados pessoais publicados** (CPF, endereco) -> nao indexar, usar `noindex` + remocao via GSC (Removals tool).
- **Dados sensiveis** (saude, biometria) -> auth + nao publicar.
- **Direito ao esquecimento** (LGPD art. 18) -> remover via GSC Removal Tool + retirar do site origem.

> **Cristal C11 — REMOVAL TOOL E SO TEMPORARIO.** GSC Remove URL = oculta da SERP por 6 meses. Para remocao definitiva: deletar do origem + retornar 410 + ou noindex permanente.

### 9.5 Mobile-first + 4G/5G Brasil

- **Penetracao 5G Brasil** (Anatel 2026 — cross-checar): expansao em capitais; interior majoritariamente 4G.
- **CWV mobile** e mais critico no Brasil que em mercados desenvolvidos por causa de:
  - Aparelhos Android mid/low-end dominantes.
  - Latencia movel media maior em interior.
- Otimizar para Android budget device (~Moto G mid-range em CrUX) e mais conservador.

---

## 10. Aplicacao MKT — 5 Audiencias

### 10.1 SEO Manager (operacional diario)

**Rotina recomendada**:
- **Diaria** (5min): GSC overview -> qualquer alerta? Manual action / security issue?
- **Semanal** (1h): Performance report 7d vs 7d anterior — query winners/losers; Pages report — novos errors.
- **Mensal** (4h): Reporting C-level + plano do mes seguinte; CWV historico + plano de melhoria; AI Overviews coverage.
- **Trimestral**: auditoria tecnica completa + revisao de strategy.

**KPIs primarios**:
- Cliques organicos (mes vs mes anterior + Y-o-Y).
- Top 10 paginas por cliques.
- Top 10 queries por cliques.
- CWV Good rate (% URLs Good).
- Indexed/total URLs (cobertura).
- AI Overviews citation count.

### 10.2 CMO / Founder (decisao estrategica)

**Dashboard mensal** (Looker Studio + GSC connector):
- Cliques organicos: total + por linha de produto.
- Trafego organico vs paid (Google Ads cross-skill).
- AI Overviews exposure: % de queries onde aparecemos como fonte.
- CWV: % paginas Good (correlacionar com conversao).
- Share of voice em queries-chave.

**Decisoes que GSC informa**:
- Investir em conteudo X vs Y? -> qual tem mais demanda (impressoes) + menor competicao (posicao mediana baixa)?
- Migrar plataforma? -> baseline pre-migracao (cliques + indexed URLs) -> validar pos-migracao 8 semanas.
- Cortar paginas? -> "Crawled — not indexed" em massa = sinal de qualidade percebida baixa.

### 10.3 Devs (technical SEO)

**Workflow integrado**:
- **Pre-deploy**: Lighthouse CI no PR (lab CWV gates).
- **Pos-deploy**: GSC Live Test em URLs criticas.
- **Monitoramento**: BigQuery export -> alertas em CWV regression.
- **Schema validation**: Rich Results Test + Schema.org validator + SEO crawler (Screaming Frog) em CI.

**Checklist CWV em PR**:
- [ ] LCP element identificado e otimizado (preload).
- [ ] JS bundle <= baseline (budget).
- [ ] Imagens com width/height (CLS).
- [ ] Fonts com `font-display: optional` ou `swap`.
- [ ] Long tasks <= baseline (INP).

### 10.4 Agencias (multi-cliente, escala)

**Setup multi-cliente**:
- Cada cliente: 1 Domain property + N URL prefix conforme estrutura.
- Acesso: **Full user** para time da agencia (nunca Owner).
- BigQuery export ativado em todos -> data lake centralizado.
- Looker Studio template replicavel por cliente.

**Servicos vendiveis com base em GSC**:
- **Auditoria SEO** mensal (4h-8h) — relatorio + plano de acao.
- **Recovery pos-update** (Google core update) — diagnostico + roadmap recovery.
- **Migration playbook** — pre/durante/pos com baseline GSC.
- **CWV optimization** — entrega mensuravel (% Good rate antes/depois).
- **AI Overviews strategy** (novo 2025-2026) — content angle + schema + tracking.

### 10.5 Content Marketers (conteudo nao-tecnico)

**O que GSC ensina ao content marketer**:
- **Queries em "Discovered — not indexed"** -> conteudo nao foi descoberto. Internal linking?
- **Queries com posicao 4-15 (striking distance)** -> melhorar conteudo existente, nao criar novo.
- **CTR baixo na posicao 1-3** -> reescrever title + meta description.
- **Top queries inesperadas** -> insights de demanda real (vs keyword tool teorico).

**Hack: query mining**:
1. Performance -> Queries -> filtro "Posicao > 5" + "Impressoes > 100".
2. Lista de queries com demanda + sem ranking forte = pauta de conteudo.
3. Validar intent (comercial/informacional/navegacional) antes de produzir.

---

## 11. Erros Comuns + Cristais Negativos

| Erro | Consequencia | Como evitar |
|------|--------------|-------------|
| Verificar so URL prefix `https://www.` | Perde dados de naked domain + outros subs | Sempre Domain property |
| Disallow CSS/JS em robots.txt | CWV ruim + render falho + mobile-friendly fail | Permitir CSS/JS |
| Bloquear staging com robots.txt sem auth | Staging vaza em SERP | Auth basica + noindex + IP allowlist |
| Confiar so em PSI lab CWV | Field data (real) pode estar ruim | Sempre cross-checar GSC CWV |
| Submeter URL via Indexing API para conteudo geral | TOS violation | Indexing API so para JobPosting + livestreams |
| Pedir reconsideracao vaga apos manual action | Recusa automatica | Listar URLs corrigidas + datas + provas |
| Ignorar Discovered-not-indexed | Conteudo sem trafego | Internal linking + sitemap + qualidade |
| Otimizar so para Google em 2026 | Perde Bing/Copilot/ChatGPT search | Bing Webmaster + IndexNow |
| Comparar cliques GSC com sessoes GA4 e "consertar" | Tempo perdido | Aceitar 5-15% gap normal |
| Ignorar AI Overviews tracking | Subestima impacto na estrategia | Filtrar Search appearance "AI Overviews" |

---

## 12. Templates Operacionais

### 12.1 Reporting mensal C-level (1 pagina)

```
SEO REPORT — {MES}/{ANO}
=========================

PERFORMANCE 28d vs 28d anterior:
- Cliques organicos: {N} ({+/-X}%)
- Impressoes: {N} ({+/-X}%)
- CTR medio: {X.X}% ({+/-X.X}p.p.)
- Posicao mediana: {X.X} ({+/-X.X})

TOP 5 PAGINAS WINNERS:
1. /url-1 (+{N} cliques)
2. /url-2 (+{N} cliques)
...

TOP 5 PAGINAS LOSERS:
1. /url-X (-{N} cliques)
...

INDEXACAO:
- Indexed: {N} URLs (vs sitemap submetido: {M})
- Crawled-not-indexed: {N} (atencao se >5%)
- Excluded total: {N}

CWV (Field, p75):
- LCP: {X.X}s ({Good/NI/Poor})
- INP: {X}ms ({Good/NI/Poor})
- CLS: {X.XX} ({Good/NI/Poor})
- % URLs Good: {X}%

AI OVERVIEWS:
- Impressoes em AI Mode: {N}
- Cliques: {N}
- CTR AI Mode: {X}%

ALERTAS:
- {Manual action / security issue / drop > X% / etc}

PROXIMO MES:
- Foco 1: {acao}
- Foco 2: {acao}
- Foco 3: {acao}
```

### 12.2 Auditoria SEO trimestral (estrutura)

1. **Foundations** — properties OK, verification OK, BigQuery export ativo?
2. **Indexacao** — Indexed/total ratio + breakdown de Excluded.
3. **Performance** — top queries/pages + Y-o-Y + winners/losers.
4. **CWV** — % Good por device + URLs problematicas.
5. **Sitemaps + robots.txt** — submetido vs descoberto vs indexado.
6. **Manual actions + security** — clean?
7. **Schema** — rich results detectados + erros.
8. **Mobile-first** — todas paginas respondem mobile?
9. **AI Overviews** — coverage + estrategia.
10. **Cross-channel** — paid vs organic cannibalization (cross-skill `conhecimento-google-ads`).

### 12.3 Playbook de drop de trafego (-20%+)

1. **Confirmar real** — GSC 7d ano vs ano (sazonal?) + GA4 cross-check.
2. **Isolar dimensoes** — query, page, country, device, search type.
3. **Verificar Google update** — search.google.com/search-console/inspect + Search Status Dashboard.
4. **Verificar Manual Action / Security** — GSC -> Security & manual actions.
5. **Verificar tecnico** — robots.txt mudou? noindex acidental? 5xx errors? CWV regrediu?
6. **Verificar conteudo** — paginas top perderam ranking? competitors melhoraram?
7. **Verificar SERP features** — AI Overview novo? FAQ collapsed? Local pack expandiu?
8. **Plano de acao** — fix tecnico imediato + content roadmap + reconsideration se manual action.

---

## 13. Cross-skill Bridges

| Skill | Como conecta |
|-------|--------------|
| `seo-fundamentos` | Pre-requisito conceitual. GSC operacionaliza o pipeline crawl/render/index/rank. |
| `seo-tecnico` | Execucao tecnica das correcoes que GSC sinaliza (CWV, robots, render). |
| `seo-on-page` | GSC mostra rich results + striking distance queries -> on-page resolve. |
| `seo-keywords` | GSC e fonte primaria de keyword data real (vs ferramentas terceirizadas estimadas). |
| `seo-link-building` | Links report no GSC (top linking sites/pages) — base para outreach. |
| `conhecimento-google-ads` | Cross-channel paid vs organic — search terms compartilhadas. |
| `conhecimento-meta-ads` | Atribuicao multi-canal — usuario chega via FB ad, converte via organic. |
| `conhecimento-linkedin-ads` | B2B SaaS — LinkedIn ads + GSC organic em queries de marca. |
| `conhecimento-ga4` | Correlacao trafego (GSC) vs comportamento (GA4) — queda nao resolvida em GSC pode estar em conversao GA4. |
| `conhecimento-conar-cdc` | Compliance content — claims em paginas indexadas precisam respeitar CDC Brasil. |
| `metricas-marketing` | KPIs do funnel — cliques GSC alimentam topo de funil. |
| `comunicacao-corporativa` (GEO) | Generative Engine Optimization — estrategia para citacao em ChatGPT/Perplexity/Copilot. |
| `acessibilidade-wcag` | Mobile-friendly + CWV CLS overlap com WCAG. |

---

## 14. Disclaimer + Decaimento

> **Disclaimer educacional**. Esta skill consolida boas-praticas publicas de Google Search Central, web.dev, Bing Webmaster Tools, e literatura de SEO 2024-2026. Nao substitui auditoria tecnica especializada nem aconselhamento juridico (LGPD/dados pessoais). Numeros de mercado (CTR, % CWV Good, AI Overviews coverage) sao **medianas publicadas** com variancia por nicho/pais/data — sempre cross-checar com sua propria GSC antes de decidir.

> **Volatility HIGH (3 meses)**. SEO + AI search mudam rapido. Re-validar antes de qualquer peca formal. Mudancas tipicas que invalidam material: novo Google core update, nova metrica CWV, expansao AI Overviews em mercado/idioma, mudanca de threshold INP/LCP/CLS, novo product GSC, mudanca de quota API, IndexNow finalmente adotado por Google (improvavel mas possivel).

> **NUNCA invente** URLs, estatisticas, percentuais, nomes de cases. Se nao tem fonte publica recente, omita ou marque como "estimativa de mercado — cross-checar".

---

## 15. Glossario rapido

- **CWV** — Core Web Vitals (LCP + INP + CLS).
- **LCP** — Largest Contentful Paint.
- **INP** — Interaction to Next Paint (substituiu FID Mar-2024).
- **CLS** — Cumulative Layout Shift.
- **FID** — First Input Delay (descontinuado Mar-2024).
- **CrUX** — Chrome User Experience Report (field data).
- **GSC** — Google Search Console.
- **PSI** — PageSpeed Insights.
- **SERP** — Search Engine Results Page.
- **CTR** — Click-Through Rate.
- **EEAT** — Experience, Expertise, Authoritativeness, Trust.
- **HCS** — Helpful Content System.
- **SGE** — Search Generative Experience (renomeado para AI Overviews em Mai-2024).
- **AI Overviews** — Resumos AI no topo do SERP Google.
- **GEO** — Generative Engine Optimization.
- **IndexNow** — Protocolo open-source de notificacao de indexacao (Microsoft + Yandex).
- **TTFB** — Time To First Byte.
- **WRS** — Web Rendering Service (Googlebot rendering pipeline).

---

## 16. Acionamentos sugeridos (when to load)

- "Cai trafego organico, o que aconteceu" -> sec 12.3 (drop playbook).
- "Como configuro GSC do zero" -> sec 2.
- "INP esta vermelho, como melhorar" -> sec 5 + cross-skill `seo-tecnico`.
- "Quero relatorio mensal SEO" -> sec 12.1.
- "URL nao indexa, por que" -> sec 4.1 + 4.2.
- "AI Overviews esta tomando trafego" -> sec 8.5 + cross-skill `comunicacao-corporativa` (GEO).
- "Como configuro Bing/IndexNow" -> sec 8.3 + 8.4.
- "Migracao de plataforma, baseline GSC" -> sec 12.2.
- "Pegou manual action" -> sec 7.1.
- "Site hackeado" -> sec 7.2.
- "Quero automatizar export GSC" -> sec 8.1 + 8.2.

---

## 17. Quick wins 7 dias

Para audiencia que quer ROI rapido com GSC:

**Dia 1**: Domain property + verificacao DNS + BigQuery export ativado.
**Dia 2**: Sitemap.xml submetido + validado (sem errors).
**Dia 3**: Auditoria de Pages report — listar Excluded > top 50 + categorizar.
**Dia 4**: Top 20 queries striking distance (pos 4-15, impressoes >100/mes) -> plano on-page.
**Dia 5**: CWV report -> top 5 templates problematicos -> brief tecnico para dev.
**Dia 6**: Bing Webmaster + IndexNow setup (replica de Google).
**Dia 7**: Looker Studio dashboard mensal + scheduled email para CMO.

---

## 18. Referencias (selecionadas, ~50)

### Documentacao oficial Google
- [Google Search Central](https://developers.google.com/search)
- [Search Console Help](https://support.google.com/webmasters)
- [URL Inspection tool docs](https://support.google.com/webmasters/answer/9012289)
- [Search Console API reference](https://developers.google.com/webmaster-tools/v1/api_reference_index)
- [Search Analytics Query API](https://developers.google.com/webmaster-tools/v1/searchanalytics/query)
- [Indexing API (jobs/livestreams)](https://developers.google.com/search/apis/indexing-api/v3/quickstart)
- [BigQuery export — Search Console](https://support.google.com/webmasters/answer/12917675)
- [Removals tool docs](https://support.google.com/webmasters/answer/9689846)
- [Manual actions report](https://support.google.com/webmasters/answer/9044175)
- [Security issues report](https://support.google.com/webmasters/answer/9044101)
- [Mobile-first indexing best practices](https://developers.google.com/search/mobile-sites/mobile-first-indexing)
- [Sitemaps overview](https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview)
- [robots.txt intro](https://developers.google.com/search/docs/crawling-indexing/robots/intro)
- [RFC 9309 Robots Exclusion Protocol](https://www.rfc-editor.org/rfc/rfc9309)
- [Sitemaps protocol](https://www.sitemaps.org)
- [Google Search Status Dashboard](https://status.search.google.com)

### Core Web Vitals
- [web.dev Vitals](https://web.dev/articles/vitals)
- [INP overview](https://web.dev/articles/inp)
- [LCP overview](https://web.dev/articles/lcp)
- [CLS overview](https://web.dev/articles/cls)
- [Page experience signals](https://developers.google.com/search/docs/appearance/page-experience)
- [PageSpeed Insights](https://pagespeed.web.dev)
- [CrUX dashboard](https://developer.chrome.com/docs/crux)

### Bing + IndexNow
- [Bing Webmaster Tools](https://www.bing.com/webmasters)
- [IndexNow protocol](https://www.indexnow.org)
- [IndexNow getstarted Bing](https://www.bing.com/indexnow/getstarted)
- [Why IndexNow Bing](https://www.bing.com/indexnow)

### AI Overviews / SGE
- [Google blog — Generative AI in Search 2024](https://blog.google/products/search/generative-ai-google-search-may-2024/)
- [AI Overviews Wikipedia](https://en.wikipedia.org/wiki/AI_Overviews)
- [GSC AI Mode tracking guides 2026 — Ekamoira](https://www.ekamoira.com/blog/how-to-track-rankings-in-google-ai-mode-complete-2026-guide-free-paid-methods)
- [Searchlab AI Overviews stats 2026](https://searchlab.nl/en/statistics/ai-overviews-sge-statistics-2026)
- [SGE / AI Overviews historico — SE Ranking](https://seranking.com/blog/ai-overviews/)

### Guides + walkthroughs (cross-checar antes de citar)
- [GSC ultimate guide 2026 — iMark Infotech](https://www.imarkinfotech.com/google-search-console-the-ultimate-guide-for-2026/)
- [GSC guide 2026 — SEO Hacker](https://seo-hacker.com/google-search-console-guide-2026/)
- [GSC complete 2026 — ALM Corp](https://almcorp.com/blog/google-search-console-complete-guide/)
- [GSC reports explained 2026 — Indexcraft](https://indexcraft.in/blog/tools/google-search-console-guide)
- [GSC API + BigQuery insights — Mohtaweb](https://www.mohtaweb.com/2026/04/gsc-api-bigquery-seo-insights.html)
- [GSC API guide — JC Chouinard](https://www.jcchouinard.com/google-search-console-api/)
- [GSC API + Python winners losers — Botpresso](https://botpresso.com/gsc-api-python-winners-and-losers/)
- [GSC API advanced 2026 — Incremys](https://www.incremys.com/en/resources/blog/google-search-console-api)
- [Core Web Vitals 2026 LCP INP CLS — Mewa Studio](https://www.mewastudio.com/en/blog/seo-core-web-vitals-2026)
- [CWV 2026 optimization — Sky SEO Digital](https://skyseodigital.com/core-web-vitals-optimization-complete-guide-for-2026/)
- [CWV 2026 INP LCP CLS — DigitalApplied](https://www.digitalapplied.com/blog/core-web-vitals-2026-inp-lcp-cls-optimization-guide)
- [CWV 2026 technical SEO — ALM Corp](https://almcorp.com/blog/core-web-vitals-2026-technical-seo-guide/)
- [URL Inspection guide — Search Sentry](https://searchsentry.io/blog/gsc-url-inspection-tool-guide/)
- [URL Inspection beyond indexing — Algo Digital](https://algodigital.co.uk/how-to-use-gscs-url-inspection-tool-beyond-just-indexing-requests/)
- [Mobile-first indexing GSC — Linkbot library](https://library.linkbot.com/how-can-webmasters-use-googles-mobile-first-indexing-tools-and-reports-in-google-search-console-to-ensure-optimal-mobile-performance/)
- [Bing Webmaster setup 2026 — Jetfuel](https://jetfuel.agency/bing-webmaster-tools-setup-2026/)
- [Bing AI Performance Report 2026 — Oddtusk](https://oddtusk.com/our-blog/bing-webmaster-tools-ai-performance-report/)
- [IndexNow Google support 2026 — Pressonify](https://pressonify.ai/blog/indexnow-instant-indexing-press-releases-2026)
- [Indexing tools comparison 2026 — TrySight](https://www.trysight.ai/blog/website-indexing-tools-comparison)
- [AI Overviews optimization 2026 — LinkGraph](https://www.linkgraph.com/blog/ai-overviews-optimization/)
- [AI Overviews SEO survival 2026 — Mintseotools](https://mintseotools.com/blog/what-is-a-google-ai-overview/)
- [Search Generative Experience guide 2026 — Impression Digital](https://www.impressiondigital.com/blog/search-generative-experience-generative-ai-sge-guide/)

---

## 19. Encerramento

GSC e a unica fonte primaria de verdade sobre como Google ve seu site. Em 2026, com AI Overviews tomando >48% das SERPs e Bing alimentando AI search engines, **operar bem GSC + adicionar Bing Webmaster + IndexNow** virou higienica minima de SEO. Para audiencia frank-mkt:
- **Founders/CMO** — uso GSC para decisao estrategica + atribuicao multi-canal.
- **SEO managers** — diario operacional + alertas + reporting.
- **Devs** — CWV + render + technical SEO em CI/CD.
- **Agencias** — multi-cliente + servicos vendiveis.
- **Content marketers** — query mining + striking distance + AI Overviews strategy.

Cross-skill obrigatorio: `seo-fundamentos` (modelo mental) -> `seo-tecnico` (execucao) -> esta skill (operacao + decisao). Para cobertura completa de canais: `conhecimento-google-ads` + `conhecimento-meta-ads` + `conhecimento-linkedin-ads` + `conhecimento-ga4`.

> **Reminder Cristal C0** — NUNCA invente URLs, percentuais, cases, ou estatisticas. Se nao tem fonte publica recente verificavel, omita.
