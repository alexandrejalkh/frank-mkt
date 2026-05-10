---
name: seo-tecnico
description: "SEO tecnico aplicado: crawlability (robots.txt RFC 9309, crawl budget, server logs Googlebot verification), sitemaps XML (index, image, video, news, hreflang in sitemap), indexabilidade (meta robots, X-Robots-Tag, GSC Cobertura, soft 404), canonical strategy (autorreferencial, cross-domain, parametros, paginacao), hreflang/i18n (ccTLD vs subdomain vs subdirectory, x-default, bidirecional, GSC International), HTTP status (2xx/3xx/4xx/5xx), redirects (301/302/307/308 + chains), HTTPS/HSTS/mixed content, mobile-first indexing, render (CSR/SSR/SSG/ISR + Web Rendering Service + hydration + render budget), JavaScript SEO, Core Web Vitals tecnico (LCP/INP/CLS + lab vs CrUX), performance (TTFB, FCP, render-blocking, code splitting, third-party, HTTP/2 vs HTTP/3, Brotli, preload/preconnect/dns-prefetch), structured data render (SSR vs CSR + CI validation), pagination/faceted nav/infinite scroll, site architecture (depth, internal PageRank), migration playbook (CMS/URL/domain/HTTPS), server logs analysis, CDN/edge, headless/JAMstack, auditoria 14 fases, templates (robots/sitemap/nginx/Apache/hreflang)."
user-invocable: false
last_verified: 2026-05-07
next_review: 2026-11-07
volatility: medium
regrounding_sources:
  - "https://developers.google.com/search"
  - "https://developers.google.com/search/docs/crawling-indexing"
  - "https://developers.google.com/search/docs/crawling-indexing/robots/intro"
  - "https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview"
  - "https://developers.google.com/search/docs/specialty/international"
  - "https://web.dev/articles/vitals"
  - "https://web.dev/articles/structured-data"
  - "https://www.rfc-editor.org/rfc/rfc9309"
  - "https://www.sitemaps.org"
  - "https://search.google.com/search-console"
---

# Skill: seo-tecnico

> **Decaimento Temporal**
> Ultima verificacao: 2026-05-07 | Proxima revisao: 2026-11-07 | Volatility: **medium** (6 meses)
> Google ajusta rendering pipeline, crawl behavior, CWV thresholds, e politicas de canonical/hreflang silenciosamente. Re-validar antes de publicar peca formal:
> - Google Search Central — https://developers.google.com/search
> - Google Search Central — Crawling and indexing — https://developers.google.com/search/docs/crawling-indexing
> - RFC 9309 (Robots Exclusion Protocol) — https://www.rfc-editor.org/rfc/rfc9309
> - Sitemaps protocol — https://www.sitemaps.org
> - web.dev (CWV + perf) — https://web.dev
> - Google Search Status Dashboard — https://status.search.google.com
> - Google Search Liaison (X/Twitter) — atualizacoes informais
>
> **Acionamento:** auditoria tecnica, drop pos-migracao, indexacao falha, render pesado em JS, CWV ruim, faceted navigation explosiva, hreflang quebrado, redirect chains, soft 404 em massa, CMS migration, domain migration, HTTPS migration.
> **Skills relacionadas:** `seo-fundamentos` (carrega ANTES desta), `seo-keywords` (mapping URL <-> KW para auditoria), `seo-on-page` (schema render + CWV), `conhecimento-search-console`, `conhecimento-ga4`, `acessibilidade-wcag`.
> **Pre-requisito:** ter carregado `seo-fundamentos` (modelo mental crawl/render/index/rank, EEAT, HCS, Spam Policies, CWV). Esta skill aprofunda execucao tecnica.

---

## 1. Visao Geral

SEO tecnico e a disciplina que garante que o **conteudo bom seja efetivamente rastreado, renderizado, indexado, mensuravel e rapido** — em mobile, em campo (nao so em lab). E o "encanamento" do SEO. Conteudo brilhante em site tecnicamente quebrado nao rankeia; conteudo medio em site tecnicamente impecavel pode rankear.

Esta skill nao repete o pipeline conceitual de `seo-fundamentos`. Aqui aprofundamos a **execucao tecnica**:

- **Crawl**: robots.txt (RFC 9309), crawl budget, server logs, Googlebot verification.
- **Sitemap**: XML, index, sub-tipos (image/video/news), hreflang in sitemap, lastmod.
- **Indexabilidade**: meta robots, X-Robots-Tag, GSC Cobertura, soft 404, "Detectada nao indexada".
- **Canonical**: autorreferencial, cross-domain, parametros, paginacao.
- **Hreflang / i18n**: ccTLD vs subdomain vs subdirectory, x-default, bidirecional.
- **HTTP status + redirects**: 301/302/307/308, redirect chains.
- **HTTPS**: SSL/TLS, HSTS, mixed content.
- **Mobile-first indexing**: viewport, responsive, mobile user-agent.
- **Render**: CSR/SSR/SSG/ISR, Web Rendering Service, hydration, render budget, JS SEO pitfalls.
- **CWV tecnico**: LCP/INP/CLS por metrica, lab vs CrUX.
- **Performance**: TTFB, FCP, render-blocking, code splitting, third-party, HTTP/2-3, Brotli, preload/preconnect.
- **Structured data render**: SSR vs CSR + validation no CI/CD.
- **Pagination / faceted nav / infinite scroll**.
- **Site architecture**: profundidade, internal PageRank.
- **Migration playbook**: URL, CMS, domain, HTTPS.
- **Server logs analysis**.
- **CDN / edge / headless / JAMstack**.

### 1.1 Acionamento — quando esta skill carrega

| Gatilho | Exemplo |
|---------|---------|
| Auditoria tecnica completa | "rodar audit tecnico no site do cliente" |
| Drop apos migracao | "site mudou de WordPress para Next.js — perdemos 50% trafego" |
| Indexacao falha | "GSC mostra 5k 'Rastreada nao indexada' — por que?" |
| JS-render pesado | "SPA em React, GSC cobertura ruim" |
| CWV ruim | "PageSpeed 30 mobile, como subir?" |
| Faceted navigation explosiva | "loja virou 200k URLs, crawl budget queimado" |
| Hreflang quebrado | "versao en-US do site nao indexa" |
| Redirect chains | "Ahrefs aponta cadeia de 4 redirects" |
| Soft 404 em massa | "GSC reporta soft 404 em 800 URLs" |
| Domain migration | "vamos mudar dominio, plano de zero perda" |

### 1.2 Pre-requisitos

- [ ] **Acessos**: GSC, GA4, GTM, CMS admin, hospedagem (cPanel / SSH / repo Git), CDN dashboard.
- [ ] **Stack documentada**: CMS, framework, render mode (CSR/SSR/SSG/ISR), CDN, registrar/DNS.
- [ ] **Crawler profissional**: Screaming Frog SEO Spider, Sitebulb, Ryte, OnCrawl, ou similar.
- [ ] **Acesso a server logs** (idealmente 30 dias) — Apache `access.log`, nginx `access.log`, ou CDN logs (Cloudflare, Fastly).
- [ ] **PageSpeed Insights / CrUX dataset** para CWV historico.
- [ ] **Conhecimento dos consumidores externos** que linkam ao site (Ahrefs / Semrush) — para preservar autoridade em migracao.

> **Cristal C0 — NAO CHUTAR.** Nenhuma decisao tecnica (canonical, hreflang, robots.txt, redirect strategy) e tomada sem dado de crawl + server logs + GSC. "Achismo" tecnico em SEO custa dinheiro e tempo de recovery.

---

## 2. Modelo mental tecnico — stack + render + entrega

```
USUARIO / GOOGLEBOT
     |
     V
[DNS] -> [CDN/edge] -> [Servidor / origem]
                              |
                              V
                       [Aplicacao (CMS / framework)]
                              |
                              V
                       [HTML + assets]
                              |
                              V
              [Render: CSR / SSR / SSG / ISR]
                              |
                              V
            [Resposta HTTP (status + headers + body)]
```

Cada camada tem decisoes que afetam SEO:

| Camada | Decisao SEO-relevante |
|--------|------------------------|
| **DNS** | TTL, Anycast, latencia |
| **CDN/edge** | Cache, geo-distribution, edge functions, image optim |
| **Servidor** | TTFB, HTTP/2 vs HTTP/3, Brotli/gzip, headers |
| **Aplicacao** | Render mode, sitemap dinamico, canonical, hreflang |
| **HTML + assets** | Title/meta/H, schema, internal links, imagens |
| **Render** | CSR (perigoso), SSR (default seguro), SSG (otimo), ISR (hibrido) |
| **Resposta** | Status correto, cache-control, content-type, x-robots-tag |

---

## 3. Crawl — robots.txt, crawl budget, server logs

### 3.1 robots.txt — RFC 9309 (2022)

`robots.txt` na raiz do dominio. Diretivas:

```
# Default: tudo permitido
User-agent: *
Disallow:

# Bloquear admin
User-agent: *
Disallow: /admin/
Disallow: /wp-admin/
Allow: /wp-admin/admin-ajax.php

# Bloquear parametros de busca interna
Disallow: /search/
Disallow: /*?s=
Disallow: /*?q=

# Bloquear staging
User-agent: *
Disallow: /staging/

# Restringir crawler especifico
User-agent: AhrefsBot
Crawl-delay: 10

# Sitemap (uma diretiva por linha; URL absoluta)
Sitemap: https://dominio.com/sitemap.xml
Sitemap: https://dominio.com/sitemap-news.xml
```

Pontos criticos:

| Ponto | Detalhe |
|-------|---------|
| **Localizacao** | https://dominio.com/robots.txt — exatamente nesse path |
| **Encoding** | UTF-8 sem BOM |
| **Tamanho** | <= 500 KiB (Google ignora alem) |
| **Disallow nao impede indexacao** | Google pode indexar URL sem rastrear conteudo se ha link externo. Para impedir indexacao, usar `noindex` |
| **Wildcards** | `*` em pattern, `$` para fim de URL |
| **Crawl-delay** | NAO suportado pelo Google — usar GSC > Configuracoes > Taxa de rastreamento |
| **Comentarios** | Linha iniciada por `#` |
| **Case-sensitive** | Path e case-sensitive |

### 3.2 Crawl budget

| Conceito | Detalhe |
|----------|---------|
| **Crawl rate limit** | Quantas requests/segundo Googlebot faz, ajustado automaticamente pela saude do servidor |
| **Crawl demand** | Quantidade de URLs que Google quer rastrear (popularidade + freshness) |
| **Crawl budget** | Resultado das duas — relevante em sites > 100k URLs |
| **Como monitorar** | GSC > Configuracoes > Estatisticas de rastreamento |
| **Como otimizar** | Eliminar URLs desnecessarias (faceted, sessao, parametros), bloquear lixo via robots, retornar 404/410 para URLs mortas, manter sitemap limpo, melhorar TTFB |

### 3.3 Googlebot user-agents

| User-agent | Funcao | Prioridade |
|------------|--------|------------|
| `Googlebot/2.1 (+http://www.google.com/bot.html)` | Web crawler default | Mobile (Smartphone) e a default desde 2023 |
| `Googlebot Smartphone` | Mobile-first | Default |
| `Googlebot Desktop` | Desktop fallback | Secundario |
| `Googlebot Image` | Imagens | Image search |
| `Googlebot Video` | Videos | Video carousel |
| `Googlebot News` | News | Top Stories |
| `AdsBot-Google` | Verificacao de landing page para Ads | Ads |
| `Mediapartners-Google` | AdSense | AdSense |
| `Storebot-Google` | E-commerce | Shopping |
| `Google-InspectionTool` | URL Inspection no GSC | GSC |

### 3.4 Verificacao de Googlebot (anti-spoofing)

Bots maliciosos forjam `User-Agent: Googlebot`. Verificacao real:

```bash
# Reverse DNS lookup
host 66.249.x.x
# deve retornar googlebot.com OU google.com

# Forward DNS lookup
host crawl-66-249-x-x.googlebot.com
# deve retornar o IP original

# OU usar IP ranges oficiais
# https://developers.google.com/search/apis/ipranges/googlebot.json
```

### 3.5 Server logs analysis

Server logs (nginx/Apache/CDN) revelam o que Googlebot esta REALMENTE fazendo — diferente de "esperamos que ele esteja fazendo".

| Insight | Como extrair |
|---------|--------------|
| **Quantas URLs Googlebot rastreia/dia** | Filtrar por user-agent + verificar via reverse DNS |
| **Que URLs Googlebot prioriza** | Ranking de URLs com mais hits |
| **URLs orfas que Googlebot rastreia** | URLs em logs sem links internos apontando |
| **Crawl budget queimado** | URLs duplicadas, parametros, faceted no top do ranking |
| **Status code de resposta a Googlebot** | 5xx em massa = sinal vermelho |
| **TTFB que Googlebot recebe** | Latencia bot vs usuario |

Ferramentas:
- **Screaming Frog Log File Analyser** — desktop, padrao da industria.
- **OnCrawl** — log + crawl unificado.
- **Botify** — enterprise.
- **JetOctopus** — log + crawl.
- **CDN dashboards** — Cloudflare Analytics, Fastly, Akamai.
- **ELK / Splunk / BigQuery** — para sites grandes.

---

## 4. Sitemap XML

### 4.1 Sitemap basico — protocolo sitemaps.org

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://dominio.com/</loc>
    <lastmod>2026-05-07T10:00:00-03:00</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://dominio.com/blog/crm-para-startup/</loc>
    <lastmod>2026-05-07T10:00:00-03:00</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
</urlset>
```

| Tag | Notas |
|-----|-------|
| `<loc>` | URL absoluta, ate 2048 chars |
| `<lastmod>` | ISO 8601, importante (Google usa para crawl scheduling) |
| `<changefreq>` | Google IGNORA — manter por compatibilidade ou remover |
| `<priority>` | Google IGNORA — manter por compatibilidade ou remover |

### 4.2 Sitemap-index (multiplos sitemaps)

Sitemap unico tem limite: 50.000 URLs OU 50 MiB descomprimido. Acima disso, usar sitemap-index:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <sitemap>
    <loc>https://dominio.com/sitemap-posts.xml</loc>
    <lastmod>2026-05-07T10:00:00-03:00</lastmod>
  </sitemap>
  <sitemap>
    <loc>https://dominio.com/sitemap-products.xml</loc>
    <lastmod>2026-05-07T10:00:00-03:00</lastmod>
  </sitemap>
  <sitemap>
    <loc>https://dominio.com/sitemap-images.xml</loc>
    <lastmod>2026-05-07T10:00:00-03:00</lastmod>
  </sitemap>
</sitemapindex>
```

### 4.3 Image sitemap

```xml
<url>
  <loc>https://dominio.com/blog/crm-para-startup/</loc>
  <image:image xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">
    <image:loc>https://dominio.com/images/crm-startup-comparativo.avif</image:loc>
    <image:caption>Comparativo de 5 CRMs para startup em 2026</image:caption>
    <image:title>CRM Startup Comparativo</image:title>
  </image:image>
</url>
```

### 4.4 Video sitemap

```xml
<url>
  <loc>https://dominio.com/tutorial-ga4/</loc>
  <video:video xmlns:video="http://www.google.com/schemas/sitemap-video/1.1">
    <video:thumbnail_loc>https://dominio.com/thumb.avif</video:thumbnail_loc>
    <video:title>Como configurar GA4 em 30 minutos</video:title>
    <video:description>Tutorial passo a passo...</video:description>
    <video:content_loc>https://dominio.com/video/ga4.mp4</video:content_loc>
    <video:duration>750</video:duration>
    <video:publication_date>2026-05-07T10:00:00-03:00</video:publication_date>
  </video:video>
</url>
```

### 4.5 News sitemap (Google News, ate 48h apos publicacao)

```xml
<url>
  <loc>https://dominio.com/noticia/exemplo/</loc>
  <news:news xmlns:news="http://www.google.com/schemas/sitemap-news/0.9">
    <news:publication>
      <news:name>SPKR Noticias</news:name>
      <news:language>pt</news:language>
    </news:publication>
    <news:publication_date>2026-05-07T10:00:00-03:00</news:publication_date>
    <news:title>Titulo da noticia</news:title>
  </news:news>
</url>
```

### 4.6 Hreflang in sitemap (alternativa a hreflang em HTML)

```xml
<url>
  <loc>https://dominio.com/pt-br/produto/</loc>
  <xhtml:link rel="alternate" hreflang="pt-BR" href="https://dominio.com/pt-br/produto/" xmlns:xhtml="http://www.w3.org/1999/xhtml"/>
  <xhtml:link rel="alternate" hreflang="en-US" href="https://dominio.com/en-us/product/" xmlns:xhtml="http://www.w3.org/1999/xhtml"/>
  <xhtml:link rel="alternate" hreflang="es-MX" href="https://dominio.com/es-mx/producto/" xmlns:xhtml="http://www.w3.org/1999/xhtml"/>
  <xhtml:link rel="alternate" hreflang="x-default" href="https://dominio.com/en-us/product/" xmlns:xhtml="http://www.w3.org/1999/xhtml"/>
</url>
```

### 4.7 Regras de ouro de sitemap

- **APENAS URLs canonicas indexaveis** no sitemap. Nao incluir noindex, redirect, 404, parametrizadas.
- **lastmod fiel** — atualizar quando o conteudo realmente muda.
- **Submeter no GSC** (Sitemaps) e referenciar em `robots.txt`.
- **Auditoria periodica** — sitemap desatualizado e sinal de site abandonado.
- **Compressao gz** se grande — Google aceita `sitemap.xml.gz`.

---

## 5. Indexabilidade — controles

### 5.1 Meta robots (no HTML)

```html
<!-- Permite tudo (default — geralmente nao precisa declarar) -->
<meta name="robots" content="index, follow" />

<!-- Bloqueia indexacao -->
<meta name="robots" content="noindex" />

<!-- Bloqueia indexacao + nao segue links -->
<meta name="robots" content="noindex, nofollow" />

<!-- Bloqueia rich snippets / cache -->
<meta name="robots" content="noarchive, nosnippet" />

<!-- Especificar para bot especifico -->
<meta name="googlebot" content="noindex" />
<meta name="bingbot" content="noindex" />
```

### 5.2 X-Robots-Tag (HTTP header)

Equivalente do meta robots para arquivos nao-HTML (PDF, imagens) ou para definir via servidor:

```
HTTP/1.1 200 OK
Content-Type: application/pdf
X-Robots-Tag: noindex

# nginx
add_header X-Robots-Tag "noindex" always;

# Apache .htaccess
<FilesMatch "\.(pdf|doc|docx)$">
  Header set X-Robots-Tag "noindex"
</FilesMatch>
```

### 5.3 Estados em GSC > Cobertura (recap de seo-fundamentos com aprofundamento tecnico)

| Estado | Causa tecnica comum | Acao |
|--------|---------------------|------|
| **Indexada** | OK | Manter |
| **Indexada, mas nao enviada no sitemap** | URL alcancada por crawl, ausente do sitemap | Adicionar ao sitemap |
| **Rastreada nao indexada** | Conteudo julgado nao-util (HCS), thin, duplicado | Melhorar conteudo, EEAT, originalidade |
| **Detectada nao indexada** | Crawl budget esgotado / autoridade interna baixa | Reforcar internal linking, sitemap, autoridade externa |
| **Pagina alternativa com tag canonica adequada** | Duplicata legitima com canonical | OK |
| **Pagina duplicada, Google escolheu canonical diferente** | Canonical declarado e ignorado pelo Google | Investigar — sinal mais forte de outro lado? |
| **Excluida por tag noindex** | Intencional? | Remover noindex se erro |
| **Bloqueada por robots.txt** | Disallow impede crawl | Remover disallow se erro |
| **Erro de servidor (5xx)** | Servidor instavel | Investigar |
| **Erro 404** | URL retorna 404 | Manter (se intencional) ou redirecionar |
| **Soft 404** | Retorna 200 mas conteudo "nao encontrado" | Retornar 404 real OU enriquecer conteudo |
| **Pagina com redirecionamento** | URL e redirect | Apontar links para destino direto |

### 5.4 Soft 404 — armadilha comum

Pagina retorna **200 OK** mas Google detecta que e "vazia" / "nao encontrada":

- Pagina de busca interna sem resultados.
- Pagina de categoria vazia.
- "Produto removido".
- Empty state com pouco texto.

**Correcao:** retornar **404 real** (status code) OU enriquecer conteudo (sugestoes, internal links, contato).

### 5.5 Indexacao em massa via API (Indexing API — restricoes)

Google Indexing API e oficial **apenas** para:
- JobPosting schema (vagas).
- BroadcastEvent / LiveBlogPosting (eventos ao vivo).

Uso fora desse escopo viola Termos de Uso. NAO submeter site inteiro via Indexing API.

---

## 6. Canonical strategy

### 6.1 Sintaxe basica

```html
<!-- Autorreferencial (default) -->
<link rel="canonical" href="https://dominio.com/produto-x/" />

<!-- Apontando para versao master -->
<link rel="canonical" href="https://dominio.com/produto-x/" />
<!-- (em pagina /produto-x/?utm=xxx ou /pt/produto-x/) -->
```

Regras:
- **URL absoluta** com protocolo e dominio.
- **Match exato** com URL de destino (case + slash + protocolo).
- Pode ser **autorreferencial** (recomendado em todas as paginas).
- Pode apontar para **outro dominio** (cross-domain canonical — usar com cuidado).

### 6.2 Em HTTP header (para arquivos nao-HTML)

```
HTTP/1.1 200 OK
Content-Type: application/pdf
Link: <https://dominio.com/whitepaper.pdf>; rel="canonical"
```

### 6.3 Casos comuns

| Caso | Estrategia |
|------|-----------|
| **URL com parametros UTM/session** | Canonical aponta para URL limpa |
| **Versao mobile separada (m.dominio.com)** | DESCONTINUADO — usar responsive. Se legacy: rel=alternate + canonical |
| **Paginacao** | Cada pagina canonical autorreferencial; rel=prev/next foi DESCONTINUADO em 2019 |
| **Variacoes de produto (cor/tamanho)** | Canonical para pagina principal OU canonical autorreferencial (depende de UX) |
| **HTTPS vs HTTP** | Canonical para HTTPS sempre |
| **www vs sem www** | Canonical para versao escolhida |
| **Conteudo sindicado** | Canonical para original (cross-domain) ou aceitar perda |

### 6.4 Erros comuns

- Canonical apontando para URL que retorna 404/redirect.
- Canonical em massa apontando para homepage.
- Canonical autorreferencial em paginas que deveriam apontar para master.
- Conflito entre canonical em HTML e em HTTP header.
- Canonical para URL noindex (sinais conflitantes).

### 6.5 Quando Google ignora seu canonical

GSC mostra "Pagina duplicada, Google escolheu canonical diferente" quando:
- Canonical declarado nao bate com sinais (links internos, sitemap, hreflang).
- Pagina escolhida tem mais autoridade (backlinks).
- Inconsistencia entre canonical e outros sinais.

**Solucao:** alinhar TODOS os sinais (canonical + sitemap + internal links + hreflang) para a mesma URL.

---

## 7. Hreflang / i18n

### 7.1 Decisao de arquitetura

| Arquitetura | Exemplo | Pros | Contras |
|-------------|---------|------|---------|
| **ccTLD** | dominio.com.br, dominio.de | Geo signal forte | Caro, autoridade fragmentada |
| **Subdomain** | br.dominio.com, de.dominio.com | Separa indexacao | Autoridade nao se acumula tanto |
| **Subdirectory** | dominio.com/pt-br/, dominio.com/de/ | Autoridade unificada | Geo signal mais fraco |
| **URL parameter** | dominio.com/?lang=pt | Evitar | Ruim para SEO |

Recomendacao default 2026: **subdirectory** (`/pt-br/`, `/en-us/`). ccTLD apenas se ha presenca local forte (CNPJ, escritorio fisico, regulacao local).

### 7.2 Sintaxe hreflang em HTML

```html
<link rel="alternate" hreflang="pt-BR" href="https://dominio.com/pt-br/produto/" />
<link rel="alternate" hreflang="en-US" href="https://dominio.com/en-us/product/" />
<link rel="alternate" hreflang="es-MX" href="https://dominio.com/es-mx/producto/" />
<link rel="alternate" hreflang="x-default" href="https://dominio.com/en-us/product/" />
```

### 7.3 Regras

- **Bidirecional**: pagina A linka para B; pagina B linka para A. Sem isso, hreflang e ignorado.
- **Self-referencing**: pagina deve incluir hreflang apontando para si mesma.
- **Codigo de idioma + regiao** (ISO 639-1 + ISO 3166-1 alpha-2) — `pt-BR`, `en-US`, `es-MX`.
- **x-default** para fallback (pagina mostrada quando nenhum match perfeito).
- URL absoluta.
- Mesma estrutura em hreflang em HTML, sitemap, ou HTTP header — escolher UM canal e ser consistente.

### 7.4 Hreflang em HTTP header (arquivos nao-HTML)

```
HTTP/1.1 200 OK
Content-Type: application/pdf
Link: <https://dominio.com/pt-br/manual.pdf>; rel="alternate"; hreflang="pt-BR",
      <https://dominio.com/en-us/manual.pdf>; rel="alternate"; hreflang="en-US"
```

### 7.5 Erros comuns (em GSC > International Targeting — feature reduzida em GSC moderno)

- Hreflang nao bidirecional ("return tag missing").
- Codigo invalido ("pt-PT-BR" nao existe).
- URL apontada nao existe (404/redirect).
- Hreflang em pagina noindex.
- Mistura de dialetos (pt-BR + pt-PT como idiomas distintos OU como mesmo idioma).

---

## 8. HTTP status + redirects

### 8.1 Status codes — implicacoes SEO

| Code | Significado | SEO |
|------|-------------|-----|
| **200 OK** | Sucesso | Indexavel |
| **301 Moved Permanently** | Redirect permanente | Passa autoridade (~100% em 2024+) |
| **302 Found** | Redirect temporario | Pouco passa autoridade — se permanente, virar 301 |
| **303 See Other** | Redirect (POST -> GET) | Raramente em SEO |
| **307 Temporary Redirect** | Redirect temporario (preserva metodo) | Pouca autoridade |
| **308 Permanent Redirect** | Redirect permanente (preserva metodo) | Equivalente a 301 |
| **404 Not Found** | URL nao existe | Removida do indice apos confirmacao |
| **410 Gone** | URL removida permanentemente | Removida mais rapido que 404 |
| **451 Unavailable for Legal Reasons** | Restricao legal | Removida |
| **500 Internal Server Error** | Erro servidor | Risco — Google pausa crawl |
| **502 Bad Gateway** | CDN nao alcanca origem | Risco — investigar |
| **503 Service Unavailable** | Manutencao | OK temporario; usar com `Retry-After` header |
| **504 Gateway Timeout** | Timeout | Risco |
| **429 Too Many Requests** | Rate limit | Reduzir crawl rate |

### 8.2 Redirect chains — anti-pattern

Cadeia: A -> B -> C -> D. Cada hop perde tempo + dilui autoridade. Ideal: A -> D direto.

Como detectar:
- Screaming Frog > Redirects.
- Ahrefs > Site Audit > Redirect chains.
- `curl -ILv https://url-a.com` (manual).

Como corrigir:
- Atualizar regras de redirect para apontar A -> D diretamente.
- Atualizar internal links e sitemap para D.

### 8.3 Templates — nginx redirects

```nginx
# Redirect 301 simples
location /url-antiga/ {
    return 301 https://dominio.com/url-nova/;
}

# Redirect com regex (preservar segmento)
location ~ ^/blog/(\d{4})/(\d{2})/(\d{2})/(.+)/$ {
    return 301 https://dominio.com/blog/$4/;
}

# Redirect HTTP -> HTTPS
server {
    listen 80;
    server_name dominio.com www.dominio.com;
    return 301 https://dominio.com$request_uri;
}

# Redirect www -> sem www
server {
    listen 443 ssl;
    server_name www.dominio.com;
    return 301 https://dominio.com$request_uri;
}

# Redirect com trailing slash forcado
rewrite ^(.+[^/])$ $1/ permanent;
```

### 8.4 Templates — Apache .htaccess

```apache
# 301 simples
Redirect 301 /url-antiga/ https://dominio.com/url-nova/

# Regex
RewriteEngine On
RewriteRule ^blog/(\d{4})/(\d{2})/(\d{2})/(.+)/?$ /blog/$4/ [L,R=301]

# HTTPS forcado
RewriteCond %{HTTPS} off
RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]

# www -> sem www
RewriteCond %{HTTP_HOST} ^www\.dominio\.com$ [NC]
RewriteRule ^(.*)$ https://dominio.com/$1 [L,R=301]
```

### 8.5 Mapping em migracao — template

```
| URL antiga                                    | Status atual | URL nova                            | Tipo redirect | Backlinks externos |
|-----------------------------------------------|--------------|-------------------------------------|---------------|--------------------|
| /blog/2023/12/15/post-x/                      | 200          | /blog/post-x/                       | 301           | 5                  |
| /post-y                                       | 200          | /blog/post-y/                       | 301           | 12                 |
| /antigo-pagina-deletada/                      | 200          | (none)                              | 410           | 0                  |
| /produto-descontinuado/                       | 200          | /produtos/                          | 301           | 3                  |
```

---

## 9. HTTPS / seguranca

### 9.1 Obrigatorio em 2026

- Google sinaliza HTTPS como ranking factor (leve) desde 2014.
- Browsers (Chrome, Firefox) mostram "Nao seguro" para HTTP.
- HTTPS e pre-requisito para HTTP/2 e HTTP/3 nos browsers.

### 9.2 Certificado

- Let's Encrypt (gratis) ou paid CA.
- Renovacao automatica.
- Cobertura: dominio principal + www + subdomains relevantes.

### 9.3 Mixed content

Pagina HTTPS carregando recurso HTTP -> browser bloqueia ou avisa. Auditar:
- Imagens.
- Scripts.
- iframes.
- Forms (action HTTP em pagina HTTPS).

Ferramentas:
- DevTools > Console.
- Why No Padlock (whynopadlock.com).
- Mixed Content Scan (OWASP).

### 9.4 HSTS — HTTP Strict Transport Security

```
HTTP/1.1 200 OK
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
```

Forca browser a usar HTTPS por X segundos. `preload` adiciona ao Chrome HSTS Preload List (uma vez incluido, dificil reverter — cuidado).

### 9.5 HTTP migration — passos seguros

1. Instalar certificado em **staging**.
2. Auditar mixed content.
3. Configurar redirects 301 HTTP -> HTTPS para TODAS URLs.
4. Atualizar canonical, sitemap, robots.txt para HTTPS.
5. Adicionar HTTPS property em GSC.
6. Submeter sitemap atualizado.
7. Atualizar internal links.
8. Adicionar HSTS apos confirmar tudo OK por 1-2 semanas.

---

## 10. Mobile-first indexing

### 10.1 Default desde 2023

Googlebot Smartphone e o user-agent **default** para indexacao. Conteudo mobile = conteudo indexado.

### 10.2 Riscos comuns

- **Conteudo mobile reduzido vs desktop** — Google indexa o que ve no mobile. Se mobile esconde conteudo (em vez de colapsar), perde-se indexacao.
- **Schema.org so em desktop** — schema deve estar em ambos.
- **Imagens diferentes** — alt text, file name, etc. devem ser identicos em mobile/desktop.
- **Lazy loading agressivo** — conteudo principal nao deve depender de scroll para aparecer.
- **Intersticial intrusivo em mobile** — penaliza Page Experience.

### 10.3 Auditoria mobile

- Google Mobile-Friendly Test descontinuado em 2023; usar **Lighthouse + Rich Results Test + GSC Cobertura mobile**.
- Crawlar com user-agent Googlebot Smartphone.
- DevTools > Toggle device toolbar.

### 10.4 Responsive vs Dynamic Serving vs Mobile separado

| Tecnica | Status 2026 |
|---------|-------------|
| **Responsive design** | Recomendado |
| **Dynamic serving** (mesmo URL, HTML diferente por user-agent) | Suportado, mais complexo |
| **Mobile separado** (m.dominio.com) | DESCONTINUADO — migrar para responsive |

---

## 11. Render — CSR, SSR, SSG, ISR + JS SEO

### 11.1 Modos de render

| Modo | O que e | SEO |
|------|---------|-----|
| **CSR (Client-Side Rendering)** | HTML vazio + JS gera conteudo no browser | Perigoso — Googlebot pode nao esperar JS |
| **SSR (Server-Side Rendering)** | HTML completo no GET | Excelente |
| **SSG (Static Site Generation)** | HTML pre-renderizado em build | Otimo (perf + SEO) |
| **ISR (Incremental Static Regeneration)** | Hibrido — paginas estaticas regeneradas on-demand (Next.js, Astro, Nuxt) | Otimo |
| **Dynamic Rendering** | Servir HTML diferente para bots vs usuarios | DESCONTINUADO oficialmente — preferir SSR/SSG |

### 11.2 Web Rendering Service (WRS)

- Googlebot usa WRS (Chromium evergreen) para executar JS.
- Render budget: render e caro (CPU/memoria).
- Atrasos: render pode demorar dias-semanas em sites pesados.
- WRS NAO clica botao, NAO submete form, NAO lazy-scroll alem do viewport inicial.

### 11.3 JavaScript SEO — pitfalls

| Pitfall | Solucao |
|---------|---------|
| **Conteudo principal so apos JS executar** | SSR/SSG do conteudo principal |
| **Internal links via `onclick`** | Usar `<a href>` real |
| **Lazy load por scroll de conteudo principal** | Carregar conteudo critico no HTML inicial |
| **Title/meta dinamico via JS so** | SSR de title/meta |
| **Schema.org so via JS** | SSR de JSON-LD |
| **Hash-based routing** (`#/page`) | Migrar para path-based (`/page`) |
| **Service Workers que servem HTML diferente para bots** | Evitar |
| **Hidratacao quebrando antes de conteudo aparecer** | Resolver hydration mismatch |
| **Tag `<noscript>` com conteudo critico** | NAO confiar — Googlebot ignora tipicamente |

### 11.4 Diagnostico de render

- **GSC > URL Inspection > "Pagina renderizada" > Screenshot + HTML renderizado** — ouro.
- **Lighthouse > SEO** — flag basica.
- **Screaming Frog > Configurar render JS** — crawl em modo JS.
- **Puppeteer / Playwright** — render local.
- **`view-source:` no Chrome** — HTML inicial (antes de JS).

### 11.5 Hydration mismatch

Quando HTML servido (SSR) difere do HTML que o JS gera no cliente:
- Browser warning.
- Layout shift (CLS impact).
- Bug visual.
- Googlebot pode confundir.

Solucao: garantir parity entre server e client render.

---

## 12. Core Web Vitals — execucao tecnica

(Conceito em `seo-fundamentos`. Aqui execucao.)

### 12.1 LCP — Largest Contentful Paint

Threshold: <= 2.5s (Bom), <= 4.0s (Precisa Melhorar), > 4.0s (Ruim).

Otimizacoes:

| Causa comum | Otimizacao |
|-------------|------------|
| Imagem hero pesada | AVIF/WebP, srcset, `fetchpriority="high"`, preload |
| TTFB alto (servidor lento) | CDN, cache, melhor host, edge function |
| Render-blocking CSS/JS | Inline critical CSS, defer/async JS |
| Servidor sem cache | Cache HTTP (CDN edge) |
| Fontes web lentas | `font-display: swap`, preload, self-host |
| JavaScript bundle grande | Code splitting, tree shaking |

### 12.2 INP — Interaction to Next Paint

Threshold: <= 200ms (Bom), <= 500ms (Precisa Melhorar), > 500ms (Ruim).

Otimizacoes:

| Causa | Otimizacao |
|-------|------------|
| Long tasks (>50ms) bloqueando main thread | Code splitting, debounce, `requestIdleCallback` |
| Third-party scripts (analytics, chat) | Defer, lazy, avaliar custo-beneficio |
| Hydration pesada | Partial hydration, islands architecture, RSC |
| Event handlers caros | Mover trabalho para Web Worker |
| DOM grande (>1500 elementos) | Virtualization, simplify |

### 12.3 CLS — Cumulative Layout Shift

Threshold: <= 0.1 (Bom), <= 0.25 (Precisa Melhorar), > 0.25 (Ruim).

Otimizacoes:

| Causa | Otimizacao |
|-------|------------|
| Imagens sem dimensoes | `width` + `height` + `aspect-ratio` |
| Ads / embeds sem espaco reservado | Reservar via CSS `min-height` |
| Fontes que mudam metrica | `font-display: swap` + size-adjust |
| Conteudo injetado dinamicamente | Reservar espaco antes |
| Banners dismissable | Posicionar fora do flow |

### 12.4 Lab vs Field

| Tipo | Ferramenta | Uso |
|------|-----------|-----|
| **Lab** | Lighthouse, PageSpeed Insights (lab tab), DevTools, WebPageTest | Diagnostico, debug |
| **Field (CrUX)** | PageSpeed Insights (field tab), GSC Core Web Vitals, BigQuery CrUX | Decisao Google |

> **Regra de ouro:** Lighthouse 100 nao garante "Bom" no CrUX. Google usa CrUX (real-user) para ranking.

---

## 13. Performance avancada

### 13.1 TTFB (Time to First Byte)

- Threshold informal: <= 800ms.
- Causas comuns: servidor lento, sem cache, distancia geografica.
- Solucao: CDN, edge functions, cache HTTP, melhor host.

### 13.2 Render-blocking resources

```html
<!-- BLOQUEIA render -->
<link rel="stylesheet" href="/styles.css" />
<script src="/main.js"></script>

<!-- NAO BLOQUEIA -->
<link rel="stylesheet" href="/styles.css" media="print" onload="this.media='all'" />
<script src="/main.js" defer></script>
<script src="/analytics.js" async></script>
```

### 13.3 Resource hints

```html
<!-- DNS prefetch (background) -->
<link rel="dns-prefetch" href="https://cdn.dominio.com" />

<!-- Preconnect (DNS + TCP + TLS) -->
<link rel="preconnect" href="https://cdn.dominio.com" crossorigin />

<!-- Preload (alta prioridade) -->
<link rel="preload" href="/hero.avif" as="image" fetchpriority="high" />
<link rel="preload" href="/font-main.woff2" as="font" type="font/woff2" crossorigin />
<link rel="preload" href="/main.js" as="script" />

<!-- Modulepreload (ES modules) -->
<link rel="modulepreload" href="/main.module.js" />

<!-- Prefetch (proxima navegacao) -->
<link rel="prefetch" href="/proxima-pagina/" />
```

### 13.4 HTTP/2 vs HTTP/3 (QUIC)

- **HTTP/1.1** — multiplas connections, head-of-line blocking.
- **HTTP/2** — multiplexing em uma connection, server push (deprecado em Chrome).
- **HTTP/3** — QUIC, sobre UDP, melhor em redes ruins.

Em 2026, HTTP/3 ja e default em Cloudflare, Fastly, Akamai. HTTP/2 ainda majoritario.

### 13.5 Compressao

- **Brotli (br)** — melhor compressao, default em CDNs modernos.
- **gzip** — fallback amplo.
- Headers: `Accept-Encoding: br, gzip` -> `Content-Encoding: br`.

### 13.6 Cache HTTP

```
Cache-Control: public, max-age=31536000, immutable
# (assets versionados — JS/CSS com hash no nome)

Cache-Control: public, max-age=3600, must-revalidate
# (HTML — cache curto + revalidate)

Cache-Control: private, no-cache
# (paginas autenticadas)
```

ETag / Last-Modified para revalidacao condicional.

### 13.7 Third-party scripts — auditoria

Cada script externo (analytics, chat, ads, A/B test, fonts) custa:
- DNS lookup + TCP + TLS.
- Bytes downloaded.
- Main thread time.
- Risco de single point of failure.

Auditoria:
- Lighthouse > Third-party usage.
- WebPageTest > Request map.
- Critical = manter; valor baixo = remover.

---

## 14. Structured data render — SSR vs CSR

### 14.1 Regra basica

JSON-LD deve ser **renderizado server-side** ou **gerado em build (SSG)**. JSON-LD via JS tardio pode nao ser indexado a tempo.

```html
<!-- BOM (em SSR/SSG) -->
<head>
  <script type="application/ld+json">
  { "@context": "https://schema.org", "@type": "Article", ... }
  </script>
</head>

<!-- RUIM (gerado por JS depois) -->
<script>
  fetch('/api/schema').then(r => r.json()).then(data => {
    const s = document.createElement('script');
    s.type = 'application/ld+json';
    s.text = JSON.stringify(data);
    document.head.appendChild(s);
  });
</script>
```

### 14.2 Validacao no CI/CD

```yaml
# Exemplo GitHub Actions (pseudo)
- name: Build site
  run: npm run build

- name: Validate Schema.org
  run: |
    npx schema-validator dist/**/*.html

- name: Lighthouse CI
  uses: treosh/lighthouse-ci-action@v9
  with:
    urls: |
      https://staging.dominio.com/
      https://staging.dominio.com/blog/post-x/
    uploadArtifacts: true
    temporaryPublicStorage: true

- name: Crawl staging com Screaming Frog
  run: |
    screamingfrogseospider \
      --crawl https://staging.dominio.com \
      --headless \
      --export-tabs "Internal:All" \
      --output-folder ./reports
```

Ferramentas para CI:
- **Schema Markup Validator** API.
- **Google Rich Results Test** API (limitada).
- **Lighthouse CI**.
- **Screaming Frog headless**.
- **Sitebulb headless**.

---

## 15. Pagination, faceted nav, infinite scroll

### 15.1 Pagination

`rel=prev/next` foi **descontinuado pelo Google em 2019**. Estrategia atual:

- Cada pagina paginada com canonical autorreferencial.
- Title diferenciado: "Categoria — Pagina 2".
- Meta description diferenciada (ou ausente em paginas paginadas).
- Internal linking entre paginas (1, 2, 3, ...).
- "View all" page (single page com todo conteudo) como alternativa para certos casos.

### 15.2 Faceted navigation — risco

Loja com 10 categorias x 5 cores x 4 tamanhos x 3 marcas = 600 URLs combinadas + ordenacoes + filtros = explosao.

Solucoes:

| Abordagem | Quando |
|-----------|--------|
| **Permitir crawl + index** | Combinacoes com volume + intent comercial real |
| **noindex, follow** | Combinacoes sem volume mas que ajudam navegacao |
| **Disallow no robots.txt** | Combinacoes que NUNCA terao valor |
| **Canonical para categoria mae** | Variacoes minimas (ordenacao por preco) |
| **AJAX sem URL change** | Filtros que nao precisam ser indexados |
| **Parameter handling em GSC** | Legado (descontinuado em sua maior parte) |

### 15.3 Infinite scroll

Risco: conteudo apos scroll pode nao ser indexado (Googlebot nao "scrolla").

Solucao: **infinite scroll com paginacao subjacente** — URL atualiza ao scrollar (History API), e existe versao paginada acessivel via link.

```
/blog/                  -> pagina 1
/blog/page/2/           -> pagina 2 (acessivel direto + link)
/blog/page/3/           -> ...
```

Bibliotecas: `IntersectionObserver` + `history.pushState`.

---

## 16. Site architecture

### 16.1 Profundidade

- **Click depth from home** — quantos cliques da homepage ate a pagina.
- Recomendado: <= 3 cliques para conteudo importante.
- Crawler reports (Screaming Frog, Sitebulb) mostram distribuicao.

### 16.2 Internal PageRank distribution

- Homepage tem mais autoridade.
- Internal links distribuem.
- Paginas linkadas da home / nav recebem mais.
- Footer com 200 links dilui.

### 16.3 Topologia ideal

```
[Homepage]
   |
   +-- [Pillar 1] (categoria principal)
   |      |
   |      +-- [Cluster 1.1] -- [Cluster 1.2] -- [Cluster 1.3]
   |             |                    |
   |             +-- [Spoke 1.1.1]    +-- [Spoke 1.2.1]
   |
   +-- [Pillar 2]
   |      |
   |      ...
```

---

## 17. Migration playbook

### 17.1 Tipos de migracao

| Tipo | Risco | Esforco |
|------|-------|---------|
| **HTTPS migration** | Baixo | Baixo |
| **URL structure change** | Medio | Medio |
| **CMS migration** (mesma URL) | Medio | Medio |
| **CMS migration + URL change** | Alto | Alto |
| **Domain migration** | Muito alto | Alto |
| **Domain + CMS + URL** | Critico | Critico |

### 17.2 Playbook (CMS migration + URL change)

```
PRE-MIGRACAO (2-4 semanas antes)
[ ] Inventario de URLs atual (Screaming Frog crawl + sitemap + GSC)
[ ] Inventario de top URLs (GA4 trafego organico + GSC clicks)
[ ] Inventario de top backlinks (Ahrefs / Semrush)
[ ] Mapping 1:1 antiga -> nova
[ ] Identificar URLs sem destino (410)
[ ] Identificar redirects existentes (evitar chain)
[ ] Documentar schema.org atual
[ ] Snapshot de meta robots, canonical, hreflang
[ ] Documentar redirects de 3rd-party (Cloudflare workers, edge rules)
[ ] Backup completo do site

STAGING
[ ] Deploy de novo site em staging com noindex em TODAS as URLs
[ ] Crawl completo do staging (Screaming Frog)
[ ] Comparativo de URL inventory antiga vs nova
[ ] Validar canonical, schema, hreflang, sitemap, robots.txt
[ ] Lighthouse + CWV baseline
[ ] QA visual + funcional
[ ] Validar redirects 301 em staging (testar 50-100 URLs criticas)

CUTOVER (idealmente em janela de baixo trafego — sex tarde / sab madrugada)
[ ] Remover noindex
[ ] Ativar redirects 301 antiga -> nova
[ ] Atualizar DNS (TTL baixo previamente — 300s)
[ ] Submeter sitemap atualizado em GSC
[ ] Atualizar internal links (se algum link no body apontava para URL antiga)
[ ] Confirmar HTTPS, HSTS

POS-CUTOVER (24-48h)
[ ] Monitorar GSC > Cobertura (esperar 2-7 dias para sincronizar)
[ ] Monitorar GA4 > Aquisicao organic (queda esperada de 10-30% nos primeiros 30 dias e normal)
[ ] Checar Sentry/error monitoring (404 inesperados, 5xx)
[ ] Crawl pos-cutover com Screaming Frog
[ ] URL Inspection das top 20 URLs no GSC
[ ] Confirmar redirects nao formaram chain

POS-MIGRACAO (30/60/90 dias)
[ ] Comparar trafego organico mensal vs baseline
[ ] Monitorar queries em GSC (queda em queries-chave?)
[ ] Outreach para top 30 backlinks externos pedindo update para URLs novas
[ ] Resolver soft 404, redirect chains, indexacao falha
[ ] Atualizar internal linking conforme cluster amadurece
[ ] Relatorio executivo de impacto SEO da migracao
```

### 17.3 Domain migration — adicionais

- Em GSC: "Mudanca de endereco" (Settings > Change of address).
- Manter dominio antigo com 301 por 6-12 meses.
- DNS: TTL baixo previamente.
- SSL para novo dominio.
- Atualizar Google Business Profile, social, listings.

---

## 18. Server logs analysis — workflow

```
LOG ANALYSIS — WORKFLOW
=========================

1. COLETAR
   [ ] Logs de pelo menos 30 dias
   [ ] Filtrar por user-agent Googlebot/Bingbot/AhrefsBot
   [ ] Validar bot via reverse DNS (Secao 3.4)

2. PARSEAR
   [ ] Estrutura: timestamp | IP | UA | URL | status | bytes | response-time
   [ ] Ferramentas: Screaming Frog Log File Analyser / OnCrawl / awk+sort+uniq

3. ANALISAR
   [ ] Top URLs rastreadas por Googlebot
   [ ] URLs com status 4xx / 5xx
   [ ] URLs orfas (rastreadas mas sem internal link)
   [ ] Crawl rate por dia (queda? pico?)
   [ ] Distribuicao de status code
   [ ] Profundidade de URLs rastreadas
   [ ] Frequencia: paginas-chave estao sendo recrawled?
   [ ] Crawl budget waste (parametros, faceted, duplicate)

4. AGIR
   [ ] Bloquear lixo via robots.txt
   [ ] Retornar 410 para URLs mortas
   [ ] Adicionar internal links para paginas sub-rastreadas
   [ ] Melhorar TTFB se Googlebot reduziu rate
   [ ] Limpar sitemap

5. MONITORAR
   [ ] Repetir analise mensalmente em sites grandes
   [ ] Trimestral em sites medios
```

---

## 19. CDN, edge, headless, JAMstack

### 19.1 CDN

| CDN | Forte em |
|-----|----------|
| **Cloudflare** | DNS + CDN + WAF + edge workers, plano gratis |
| **Fastly** | Performance enterprise, edge computing |
| **Akamai** | Enterprise tradicional |
| **Vercel Edge / Netlify Edge** | JAMstack-native |
| **AWS CloudFront** | Integracao AWS |
| **Bunny CDN** | Custo-beneficio |

Configuracoes SEO-relevantes:
- Cache HTML curto (5-60 min) com revalidate.
- Cache assets longo (1 ano) com hash no filename.
- Brotli compression.
- HTTP/3.
- Image optimization automatica (resize, AVIF/WebP).
- Edge redirects para evitar hop ate origem.

### 19.2 Headless CMS + JAMstack

| Stack | Considr SEO |
|-------|--------------|
| **Next.js + headless CMS** | SSR/ISR -> SEO ok; CSR -> risco |
| **Astro** | SSG default + islands -> excelente SEO |
| **Nuxt** | SSR/SSG -> SEO ok |
| **Gatsby** | SSG -> excelente SEO (mas legado) |
| **SvelteKit** | SSR/SSG -> SEO ok |
| **Eleventy** | SSG puro -> excelente SEO |
| **Hugo** | SSG -> excelente SEO |

Pitfalls comuns:
- Build esquecendo de regenerar paginas que mudaram (stale).
- ISR sem strategy clara (revalidate too long).
- Falta de fallback SSR para 404.
- Sitemap nao atualizado automaticamente.

---

## 20. Auditoria tecnica em 14 fases

```
AUDITORIA TECNICA — 14 FASES
==============================

FASE 1 — DESCOBERTA E STACK
  [ ] CMS, framework, render mode
  [ ] CDN, hospedagem, DNS provider
  [ ] Versao de protocolo (HTTP/2, HTTP/3)
  [ ] Versao SSL/TLS
  [ ] Acessos: GSC, GA4, GTM, CMS, hosting, CDN

FASE 2 — CRAWL
  [ ] Screaming Frog crawl em modo Googlebot Smartphone
  [ ] Comparar com lista de URLs no GSC > Cobertura
  [ ] URLs orfas, profundas, infinitas

FASE 3 — ROBOTS.TXT
  [ ] Sintaxe valida
  [ ] Sem disallow acidental de paginas-chave
  [ ] Sitemap referenciado
  [ ] User-agents adequados

FASE 4 — SITEMAP
  [ ] Apenas URLs canonicas indexaveis
  [ ] Lastmod fiel
  [ ] Tamanho dentro do limite (50k URLs / 50 MiB)
  [ ] Submetido no GSC

FASE 5 — INDEXABILIDADE
  [ ] Estados em GSC > Cobertura
  [ ] Soft 404, "rastreada nao indexada", "detectada nao indexada"
  [ ] Meta robots e X-Robots-Tag adequados

FASE 6 — CANONICAL
  [ ] Autorreferencial nas paginas master
  [ ] Sem cadeias canonical -> redirect -> outro
  [ ] Alinhado com sitemap, internal links, hreflang

FASE 7 — HREFLANG
  [ ] Bidirecional
  [ ] x-default presente
  [ ] Codigos de idioma+regiao corretos
  [ ] Sem apontar para 404/redirect

FASE 8 — STATUS CODES E REDIRECTS
  [ ] Sem 5xx em massa
  [ ] Redirects 301 para destino direto (sem chain)
  [ ] 404 vs 410 para URLs mortas
  [ ] HTTPS forced + sem mixed content

FASE 9 — RENDER
  [ ] CSR/SSR/SSG/ISR identificado
  [ ] Conteudo principal no HTML inicial (nao apenas pos-JS)
  [ ] Schema.org SSR
  [ ] Internal links como `<a href>` reais
  [ ] GSC > URL Inspection > "Pagina renderizada"

FASE 10 — CWV E PERFORMANCE
  [ ] PageSpeed Insights mobile + desktop em paginas-chave
  [ ] GSC > Core Web Vitals % "Bom" mobile
  [ ] CrUX historico (BigQuery se aplicavel)
  [ ] TTFB, render-blocking, third-party

FASE 11 — MOBILE-FIRST
  [ ] Responsive design
  [ ] Conteudo mobile = desktop
  [ ] Schema mobile = desktop
  [ ] Sem intersticiais intrusivos

FASE 12 — STRUCTURED DATA
  [ ] Validacao em Schema Markup Validator
  [ ] Validacao em Rich Results Test
  [ ] Schema reflete conteudo visivel
  [ ] sameAs em Person/Organization

FASE 13 — LOGS
  [ ] Crawl rate Googlebot
  [ ] Status code distribution
  [ ] Crawl budget waste

FASE 14 — RELATORIO E ACAO
  [ ] Matriz Esforco x Impacto
  [ ] 30-60-90 day plan
  [ ] KPIs de monitoramento
```

---

## 21. Templates rapidos

### 21.1 robots.txt template

```
# https://dominio.com/robots.txt
# Atualizado: 2026-05-07

User-agent: *
Disallow: /admin/
Disallow: /wp-admin/
Allow: /wp-admin/admin-ajax.php
Disallow: /search/
Disallow: /*?s=
Disallow: /*?q=
Disallow: /carrinho/
Disallow: /checkout/
Disallow: /minha-conta/
Disallow: /*?ref=
Disallow: /*?utm_

Sitemap: https://dominio.com/sitemap.xml
Sitemap: https://dominio.com/sitemap-news.xml
```

### 21.2 .htaccess HTTPS + canonical

```apache
RewriteEngine On

# Force HTTPS
RewriteCond %{HTTPS} off
RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]

# Force without www
RewriteCond %{HTTP_HOST} ^www\.dominio\.com$ [NC]
RewriteRule ^(.*)$ https://dominio.com/$1 [L,R=301]

# Force trailing slash
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_URI} !(.*)/$
RewriteRule ^(.*)$ https://dominio.com/$1/ [L,R=301]
```

### 21.3 nginx — security + performance headers

```nginx
server {
    listen 443 ssl http2;
    server_name dominio.com;

    # Security
    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header X-Frame-Options "SAMEORIGIN" always;
    add_header Referrer-Policy "strict-origin-when-cross-origin" always;

    # Performance
    gzip on;
    gzip_types text/css application/javascript application/json image/svg+xml;
    brotli on;
    brotli_types text/css application/javascript application/json image/svg+xml;

    # Cache
    location ~* \.(?:css|js|woff2|avif|webp|jpg|jpeg|png)$ {
        expires 1y;
        add_header Cache-Control "public, immutable";
    }

    location / {
        expires 1h;
        add_header Cache-Control "public, must-revalidate";
    }
}
```

### 21.4 Hreflang HTML template

```html
<head>
  <link rel="canonical" href="https://dominio.com/pt-br/produto/" />
  <link rel="alternate" hreflang="pt-BR" href="https://dominio.com/pt-br/produto/" />
  <link rel="alternate" hreflang="en-US" href="https://dominio.com/en-us/product/" />
  <link rel="alternate" hreflang="es-MX" href="https://dominio.com/es-mx/producto/" />
  <link rel="alternate" hreflang="x-default" href="https://dominio.com/en-us/product/" />
</head>
```

---

## 22. Anti-patterns

| Anti-pattern | Por que e problema |
|--------------|---------------------|
| **Disallow + noindex juntos** | Robots bloqueia crawl; Google nunca le noindex |
| **Canonical apontando para URL noindex** | Sinais conflitantes |
| **Redirect chain (3+ hops)** | Diluicao de autoridade + crawl budget |
| **Multiple H1 / no H1** | Confusao semantica + acessibilidade |
| **Conteudo so em JS sem SSR** | Risco de nao indexar |
| **Schema.org gerado tardio por JS** | Pode nao ser indexado |
| **Sitemap com URLs noindex/404/redirect** | Sinal de site abandonado |
| **Soft 404 em massa** | Erodir indice |
| **Hreflang nao bidirecional** | Ignorado pelo Google |
| **Mixed content em HTTPS** | Browser warning + perda de confianca |
| **Crawl-delay em robots.txt para Google** | Ignorado — usar GSC |
| **Faceted nav sem controle** | Crawl budget queimado |
| **Infinite scroll sem URL update** | Conteudo nao indexado |
| **`Indexing API` para conteudo nao-permitido** | Violacao de TOS |

---

## 23. Regras de Ouro

1. **NAO CHUTAR** — toda decisao tecnica baseada em crawl + server logs + GSC. "Acho que e o canonical" nao basta.
2. **Mobile-first sempre** — auditar em 360px primeiro.
3. **Render visivel ao Googlebot** — testar em GSC URL Inspection > "Pagina renderizada".
4. **Sitemap = verdade unica** — apenas URLs canonicas indexaveis.
5. **Canonical autorreferencial em paginas master** + alinhado com sitemap, internal links, hreflang.
6. **301 sem chain** — A -> destino, nao A -> B -> C -> D.
7. **CWV em campo (CrUX), nao apenas Lighthouse lab**.
8. **JSON-LD em SSR/SSG**, nunca apenas pos-JS.
9. **Faceted nav controlada** — noindex+follow, robots.txt, ou canonical para mae.
10. **Migration so com playbook completo** (Secao 17.2) — sem mapping 301 e perda garantida.
11. **Server logs sao verdade absoluta** sobre o que Googlebot faz.
12. **HTTPS + HSTS sempre**.
13. **Lighthouse 100 nao e meta** — meta e CrUX "Bom" em mobile.
14. **CSR e risco** — preferir SSR/SSG/ISR.

---

## 24. Exemplos comportamentais — SEO tecnico

### Exemplo 1 — Drop pos-migracao sem mapping 301

**Input:** "Trocamos de WordPress para Next.js semana passada. Trafico organico caiu 60% em 3 dias. O que fazer?"

**Resposta esperada:**
> Diagnostico em camadas: "Drop em 3 dias pos-migracao = quase sempre **falta de redirects 301 + URLs novas com indexacao falha**. Acoes em ordem de prioridade: (1) **GSC > Cobertura** — explosao de '404' / 'Excluida por noindex'? (2) **Crawl atual com Screaming Frog** vs lista pre-migracao — quantas URLs antigas retornam 404 sem redirect? (3) **Backlink check (Ahrefs)** — top 50 backlinks externos apontam para URLs antigas? Sem 301, 100% da autoridade volatilizou. Plano de emergencia (24-72h): (a) gerar mapping 1:1 antiga -> nova de TODAS URLs com >= 1 visita organica nos ultimos 6 meses (GA4 export); (b) implementar 301 em nginx/Cloudflare workers/Next.js middleware para top 200 URLs em 24h; (c) atualizar sitemap.xml com URLs novas e submeter no GSC; (d) URL Inspection das top 20 URLs novas, pedir indexacao; (e) outreach para top 10 backlinks pedindo update. Recovery realista: 4-12 semanas para voltar ao baseline (parcial em algumas KW). Migracao sem playbook (Secao 17) e o anti-pattern numero 1 de SEO; documentar leecoes para evitar reincidir."

**Comportamento-chave:** rejeita panico generico, lista hipoteses estruturadas, da plano de 24-72h em sequencia, alinha expectativa de recovery.

### Exemplo 2 — SPA em React puro (CSR) nao indexa

**Input:** "Site e SPA em React puro com hash routing (`/#/produto`). Google so indexou 3 paginas. Por que?"

**Resposta esperada:**
> "3 problemas combinados: (1) **CSR puro** — HTML inicial tem `<div id='root'></div>` vazio; conteudo so aparece pos-JS. WRS executa JS mas com atraso e nao 100% confiavel. Validar em GSC > URL Inspection > 'Pagina renderizada': se conteudo nao aparece, e CSR falhando. (2) **Hash routing** — `#/produto` e fragmento; Google trata como mesma URL que `/`. **DESCONTINUADO** desde 2015. Migrar para path-based (`/produto`) usando React Router em modo `BrowserRouter` + servidor configurado para fallback SPA. (3) **Schema.org / title / meta gerados por JS** — nao chega ao indice rapido. Solucoes em ordem: (a) curto prazo — pre-rendering (rendertron, prerender.io) para servir HTML completo a bots; (b) medio prazo — migrar para SSR (Next.js) ou SSG (Astro) com export estatico das paginas-chave; (c) eliminar hash routing. Tracking: cobertura GSC + URL Inspection apos cada fix. Realista: indexacao completa pode levar 4-8 semanas apos correcao."

**Comportamento-chave:** identifica 3 causas combinadas, oferece curto/medio prazo, alinha expectativa.

### Exemplo 3 — Faceted nav explodiu 100k URLs

**Input:** "Loja de e-commerce gerou 100k URLs combinadas (categoria + cor + tamanho + preco + ordenacao). Crawl budget consumido. Sem trafego nessa cauda."

**Resposta esperada:**
> "Classico crawl budget waste. Estrategia em 3 niveis. **NIVEL 1 — Permitir crawl + index** (combinacoes valiosas): identificar combinacoes com volume real em GKP/Ahrefs, intent comercial, e poder competir. Tipicamente 200-2000 combinacoes (categoria x atributo principal). Manter indexavel. **NIVEL 2 — noindex, follow** (combinacoes uteis para UX, sem volume): permite navegacao mas nao polui indice. `<meta name='robots' content='noindex, follow'>`. Aplicar a combinacoes 2-3 facetas. **NIVEL 3 — Disallow no robots.txt + canonical para categoria mae** (combinacoes lixo): ordenacao por preco, paginacao alem de 5, combinacoes 4+ facetas, parametros de sessao. Implementacao: (a) GSC > Estatisticas de rastreamento — top URLs queimando crawl budget; (b) regras em CMS para anexar canonical + meta robots conforme nivel; (c) atualizar robots.txt; (d) sitemap apenas com NIVEL 1; (e) monitorar GSC > Cobertura por 4-8 semanas. Bonus: AJAX para filtros de NIVEL 3 (sem URL change) — UX preservada, indice limpo. Reduzir 100k para ~3k URLs indexaveis e meta realista."

**Comportamento-chave:** estrutura em 3 niveis, define criterios objetivos, fornece plano de implementacao em CMS.

### Exemplo 4 — Sitemap com URLs noindex/404/redirect

**Input:** "Auditoria mostra 1500 URLs no sitemap, mas 600 retornam 404, 200 redirect, 100 noindex. Sitemap esta sujo."

**Resposta esperada:**
> "Sitemap sujo e sinal forte de **site abandonado** ou **CMS gerando sitemap automaticamente sem filtro**. Google trata como 'desconfianca' — pode reduzir crawl rate. Plano: (1) **Identificar gerador** — WordPress (Yoast/RankMath/AIOSEO), Next.js custom, Webflow, Shopify. (2) **Configurar filtros** — apenas URLs canonicas indexaveis devem entrar. Em Yoast: revisar 'Search appearance' por tipo de conteudo + remover noindex types. Em Next.js custom: filtrar `getStaticProps` queries. (3) **Regenerar** sitemap. (4) **Submeter** no GSC e remover sitemap antigo. (5) **Para os 600 404** — investigar: sao paginas legitimamente removidas? Retornar 410 (gone) acelera limpeza vs 404. (6) **Para os 200 redirect** — atualizar internal links e sitemap para destino direto. (7) **Para os 100 noindex** — confirmar intencao; se acidental, remover noindex; se proposital, remover do sitemap. Validacao final: crawler interno cruzar sitemap com status de cada URL — alvo: 100% das URLs do sitemap retornarem 200 + indexaveis. Cadencia: revisao trimestral."

**Comportamento-chave:** identifica causa-raiz (CMS sem filtro), oferece plano operacional, define meta numerica, define cadencia de manutencao.

---

## 25. Checklist de Contraditorio Interno — SEO tecnico

| # | Pergunta destruidora | O que busca |
|---|----------------------|-------------|
| 1 | **robots.txt foi auditado** linha-a-linha e nao bloqueia paginas-chave acidentalmente? | Anti-disallow acidental |
| 2 | **Sitemap inclui SOMENTE URLs canonicas indexaveis** (sem noindex, 404, redirect, parametrizadas)? | Sitemap limpo |
| 3 | **Canonical e autorreferencial** nas paginas master, alinhado com sitemap + internal links + hreflang? | Sinais consistentes |
| 4 | **Hreflang e bidirecional**, com x-default, codigos validos, e apontando para URLs 200? | Hreflang funcional |
| 5 | **Sem redirect chains** (>= 2 hops)? Top URLs externamente linkadas chegam ao destino em 1 hop? | Autoridade preservada |
| 6 | **Core Web Vitals em CAMPO (CrUX)** estao "Bom" em mobile, nao apenas Lighthouse lab? | UX real |
| 7 | **JS render** entrega conteudo principal, schema, internal links, title/meta no HTML inicial — confirmado em GSC URL Inspection? | Render acessivel |
| 8 | **JSON-LD e renderizado server-side** (SSR/SSG), nao apenas via JS pos-load? | Schema indexavel |
| 9 | **Faceted navigation / pagination / infinite scroll** estao controladas (canonical, noindex+follow, robots, AJAX onde apropriado)? | Crawl budget |
| 10 | **Server logs foram analisados** nas ultimas 30-60 dias? Crawl rate, status, budget waste, URLs orfas, top crawled vs top valuable? | Verdade absoluta |

---

## 26. Referencias canonicas

### 26.1 Oficiais Google

- **Google Search Central** — https://developers.google.com/search
- **Crawling and indexing** — https://developers.google.com/search/docs/crawling-indexing
- **Robots.txt** — https://developers.google.com/search/docs/crawling-indexing/robots/intro
- **Sitemaps** — https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview
- **Canonical** — https://developers.google.com/search/docs/crawling-indexing/canonicalization
- **International (hreflang)** — https://developers.google.com/search/docs/specialty/international
- **JavaScript SEO** — https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics
- **Structured data render** — https://developers.google.com/search/docs/appearance/structured-data
- **Mobile-first indexing** — https://developers.google.com/search/mobile-sites/mobile-first-indexing
- **Crawl budget** — https://developers.google.com/search/docs/crawling-indexing/large-site-managing-crawl-budget
- **HTTP status codes interpretation** — https://developers.google.com/search/docs/crawling-indexing/http-network-errors
- **Indexing API** — https://developers.google.com/search/apis/indexing-api
- **Verifying Googlebot** — https://developers.google.com/search/docs/crawling-indexing/verifying-googlebot

### 26.2 Padroes / RFCs

- **RFC 9309 (Robots Exclusion Protocol)** — https://www.rfc-editor.org/rfc/rfc9309
- **Sitemaps protocol** — https://www.sitemaps.org
- **HTTP/1.1 (RFC 9110-9112)**, **HTTP/2 (RFC 9113)**, **HTTP/3 (RFC 9114)**
- **WCAG 2.x** — https://www.w3.org/WAI/standards-guidelines/wcag

### 26.3 web.dev

- **Vitals** — https://web.dev/articles/vitals
- **LCP** — https://web.dev/articles/lcp
- **INP** — https://web.dev/articles/inp
- **CLS** — https://web.dev/articles/cls
- **Image optimization** — https://web.dev/learn/images
- **Structured data** — https://web.dev/articles/structured-data

### 26.4 Bibliografia profissional

- Aleyda Solis — SEO international + technical
- Bartosz Goralewicz (Onely) — JS SEO
- Mike King (iPullRank) — technical + leak analysis
- Jenny Halasz — log files + diagnose
- Hamlet Batista (in memoriam) — Python + SEO
- Search Engine Land — technical SEO column
- Sitebulb / Screaming Frog blogs

### 26.5 Ferramentas

- Screaming Frog SEO Spider — https://www.screamingfrog.co.uk
- Sitebulb — https://sitebulb.com
- OnCrawl — https://www.oncrawl.com
- Ryte — https://en.ryte.com
- Botify — https://www.botify.com
- JetOctopus — https://jetoctopus.com
- DeepCrawl / Lumar — https://www.lumar.io
- WebPageTest — https://www.webpagetest.org
- PageSpeed Insights — https://pagespeed.web.dev
- Lighthouse CI — https://github.com/GoogleChrome/lighthouse-ci

---

## 27. Referencia cruzada de skills

| Situacao | Skills relacionadas |
|----------|----------------------|
| Auditoria tecnica completa | `seo-fundamentos` + `seo-tecnico` + `seo-keywords` (cannibalization, gap) |
| Migracao | `seo-tecnico` (Secao 17) + `seo-on-page` (5.4 URL) + `seo-link-building` (preservar autoridade) |
| Drop pos-update | `seo-fundamentos` + `seo-tecnico` (re-validar render, indexacao) |
| Render JS | `seo-tecnico` (Secao 11) + `seo-on-page` (schema render) |
| CWV otimizacao | `seo-tecnico` (Secao 12-13) + `ux-heuristicas` (UX correlacionada) |
| Faceted / E-commerce | `seo-tecnico` (Secao 15) + `seo-on-page` (16.6 product) |
| Sitemap dinamico | `seo-tecnico` + `conhecimento-search-console` |
| Hreflang / i18n | `seo-tecnico` + `seo-on-page` (16 anatomias por mercado) |
| Logs analysis | `seo-tecnico` + `conhecimento-search-console` |
| HTTPS migration | `seo-tecnico` (Secao 9) + `compliance-lgpd` (cookies) |

---

## 28. Integracao com o ecossistema Frank-MKT

Esta skill integra-se ao agente principal `frank-mkt` (`agents/frank-mkt.md`) e ao restante do plugin da seguinte forma:

- **Pre-requisito: `seo-fundamentos`** — modelo mental crawl/render/index/rank, EEAT, HCS, Spam Policies. Sem isso, decisoes tecnicas viram operacao isolada.
- **Acoplamento com `seo-keywords`** — esta skill investiga causa tecnica de visibilidade caindo em keywords-chave. `seo-keywords` define WHAT cair; `seo-tecnico` investiga WHY.
- **Acoplamento com `seo-on-page`** — schema, canonical, hreflang, render do JSON-LD sao dominio compartilhado. `seo-on-page` define O QUE; `seo-tecnico` define COMO ENTREGAR (SSR, validation no CI/CD).
- **Acoplamento com `conteudo-evergreen`** — atualizacao em massa de conteudo (refresh de 100 artigos) pode disparar issues tecnicos (crawl budget, sitemap re-submit, lastmod massivo). Coordenar com esta skill.
- **Acoplamento com `seo-link-building`** — backlinks externos sao ativos a preservar em migracao (Secao 17). Outreach pos-cutover.
- **Acoplamento com o agente `auditor`** — auditor roda regras PASS/FAIL em saude tecnica (sitemap valido? canonical autorreferencial? hreflang bidirecional? sem chain?). Esta skill fornece o framework normativo + checklist 14 fases (Secao 20).
- **Acoplamento com o agente `seo-strategist`** — agente especialista orquestra esta skill em planos de auditoria, migracao, recovery pos-update.
- **Acoplamento com `ux-heuristicas` + `acessibilidade-wcag`** — Page Experience cruza UX + tecnico + acessibilidade. CWV, intersticiais, focus, contraste sao decisoes hibridas.
- **Acoplamento com `compliance-lgpd`** (plugin juridico) — HTTPS, cookies, tracking, mixed content em forms, consentimento sao decisoes tecnicas + juridicas.
- **Acoplamento com `conhecimento-search-console`** — esta skill instrui mecanica avancada de GSC (Cobertura, URL Inspection, Logs, International). Ela e complementar.
- **Memoria e rastreabilidade** — auditorias tecnicas, mappings de migracao, server log reports, baseline de CWV sao persistidos em `.frank-mkt/seo/<cliente>/<data>/tecnico/` pelo agente `suporte-documental` (a criar) ou diretamente pelo `frank-mkt`. Versionar para revisar evolucao temporal e impacto de migracoes / core updates.
- **Contraditorio interno** — o agente principal aciona o modulo `contraditorio-interno` carregando o Checklist da Secao 25 desta skill antes de entregar parecer tecnico, plano de migracao ou recomendacao de stack.
- **Decaimento temporal** — esta skill esta em volatility `medium` (6 meses). Re-grounding obrigatorio em fontes da Secao 26 antes de citar fato volatil (mudanca em Googlebot, novo render mode suportado, deprecacao de protocolo, threshold de CWV) em peca formal.
- **Regra de ouro para `frank-mkt`** — nenhuma decisao tecnica (canonical, hreflang, robots.txt, redirect, render mode, migracao) sai do plugin sem passar por esta skill. Custos de erro tecnico sao altos: trafego perdido, autoridade volatilizada, recovery em meses.

---

> **Aviso:** o plugin `frank-mkt` e um assistente de analise. Recomendacoes desta skill devem ser adaptadas a stack do site, autoridade do dominio, mercado, e validadas em GSC + crawler + server logs + CrUX antes de aplicar em peca formal. SEO tecnico e disciplina dinamica — Google atualiza render pipeline, crawl behavior, CWV thresholds, e politicas de canonical/hreflang silenciosamente. Auditorias tecnicas tem horizonte de validade ~3-6 meses.

---

*Plugin `frank-mkt` — skill `seo-tecnico` (v0.1.0)*
*Ultima atualizacao: 2026-05-07*
