---
name: seo-on-page
description: "SEO on-page aplicado: title, meta description, URL/slug, breadcrumbs, hierarquia de headings, body com TL;DR/inverted pyramid, internal/external linking, otimizacao de imagens (alt, file name, AVIF/WebP, lazy, schema), videos, schema.org/JSON-LD (Article, FAQPage, HowTo, Product, Review, Person, Organization, BreadcrumbList, LocalBusiness, ImageObject, VideoObject, NewsArticle, Recipe, Event, JobPosting), OpenGraph + Twitter Cards, EEAT on-page (autor box, credenciais, fonte, data, disclosure), otimizacao para SERP features (Featured Snippet, PAA, AI Overview), anatomia por tipo de pagina (pillar, cluster, listicle, comparativo, howto, product, local, blog), anti-patterns (keyword stuffing, doorway, hidden text), auditoria checklist, templates JSON-LD, AI/LLM optimization."
user-invocable: false
last_verified: 2026-05-07
next_review: 2026-11-07
volatility: medium
regrounding_sources:
  - "https://developers.google.com/search"
  - "https://developers.google.com/search/docs/appearance/structured-data"
  - "https://schema.org"
  - "https://search.google.com/test/rich-results"
  - "https://web.dev/articles/structured-data"
  - "https://developers.google.com/search/docs/crawling-indexing/special-tags"
  - "https://ogp.me"
  - "https://developer.x.com/en/docs/twitter-for-websites/cards"
  - "https://www.w3.org/WAI/standards-guidelines/wcag/"
---

# Skill: seo-on-page

> **Decaimento Temporal**
> Ultima verificacao: 2026-05-07 | Proxima revisao: 2026-11-07 | Volatility: **medium** (6 meses)
> Google adiciona/remove rich result types e ajusta SERP features silenciosamente; schema.org evolui versoes; OpenGraph/Twitter Cards estaveis. Re-validar antes de publicar peca formal:
> - Google Search Central — Structured Data — https://developers.google.com/search/docs/appearance/structured-data
> - schema.org — https://schema.org
> - Google Rich Results Test — https://search.google.com/test/rich-results
> - Schema Markup Validator — https://validator.schema.org
> - Google Search Status Dashboard — https://status.search.google.com
> - web.dev (structured data + perf) — https://web.dev
> - Google Search Liaison (X/Twitter) — atualizacoes informais
>
> **Acionamento:** brief de pagina, otimizacao de page existente, schema markup, title/meta/H, internal linking, anatomia de pillar/cluster/listicle/comparativo/howto/product/local, otimizacao para Featured Snippet/AI Overview, EEAT on-page.
> **Skills relacionadas:** `seo-fundamentos` (carrega ANTES desta), `seo-keywords` (define KW+intent+URL alvo que esta skill operacionaliza), `seo-tecnico` (saude tecnica que viabiliza on-page), `conteudo-evergreen`, `copywriting-conversao`, `ux-heuristicas`, `microcopy`, `acessibilidade-wcag`, `conhecimento-search-console`.
> **Pre-requisito:** ter carregado `seo-fundamentos` (modelo mental crawl/render/index/rank, EEAT, HCS, AI Overview) e `seo-keywords` (output: KW alvo + intent + sub-queries + URL alvo). Esta skill operacionaliza esses outputs em pagina otimizada.

---

## 1. Visao Geral

SEO on-page e a disciplina de transformar um briefing (KW + intent + URL alvo + angulo) em **pagina renderizada otimizada** — para humano, para Googlebot, e em 2026, para sistemas de busca generativa (AI Overview, Perplexity, ChatGPT search, Copilot).

Esta skill nao repete o que esta em `seo-fundamentos` (estrategico) nem em `seo-keywords` (descoberta). Aqui aprofundamos a **execucao tactica**:

- **Title tag** — formula, comprimento, branded suffix, CTR optimization.
- **Meta description** — comprimento, papel (CTR > ranking), reescrita pelo Google.
- **URL / slug / breadcrumb** — estrutura, comprimento, separadores.
- **Hierarquia de headings (H1-H6)** — H1 unico, ordem semantica, espelhamento de query.
- **Body content** — TL;DR / inverted pyramid, profundidade, fluencia, anti-fluff.
- **Internal linking** — anchor, ratio, distribuicao, hub-and-spoke.
- **External linking** — fontes primarias, dofollow / nofollow / UGC / sponsored.
- **Imagens** — alt, file name, AVIF/WebP, lazy, schema ImageObject.
- **Videos** — schema VideoObject, transcript, embed, lazy.
- **Schema.org / JSON-LD** — biblioteca dos schemas mais usados, com exemplo.
- **OpenGraph + Twitter Cards** — social sharing.
- **EEAT on-page** — autor box, credenciais, fonte, data, disclosure.
- **SERP features optimization** — Featured Snippet, PAA, AI Overview, Image/Video pack.
- **Anatomia por tipo de pagina** — pillar, cluster, listicle, comparativo, howto, product, local, blog editorial.
- **Anti-patterns** — keyword stuffing, doorway, hidden text, cloaking, exact-match abuse.
- **Auditoria de pagina existente** — checklist operacional.
- **AI/LLM optimization** — formato + schema + EEAT que aumentam citacao em AI Overview / LLM-search.

### 1.1 Acionamento — quando esta skill carrega

| Gatilho | Exemplo |
|---------|---------|
| Brief de pagina nova | "preciso da estrutura ideal de uma pagina sobre `crm para startup`" |
| Otimizacao de pagina existente | "essa URL caiu no ranking, o que ajustar?" |
| Schema markup | "que JSON-LD colocar nessa pagina?" |
| Featured Snippet roubo | "concorrente esta na posicao zero, como tirar?" |
| AI Overview citation | "como aumentar chance de meu site ser citado em AI Overview?" |
| Cluster anatomy | "como estruturar a pillar page e os spokes?" |
| Comparativo / listicle / howto | "quero criar `Pipedrive vs RD Station` — estrutura ideal?" |
| Auditoria | "rodar checklist on-page nessa URL" |

### 1.2 Pre-requisitos

- [ ] **Briefing de keyword** (output de `seo-keywords`): KW principal + KW secundarias + intent + sub-queries (PAA) + URL alvo + autor sugerido.
- [ ] **Acesso ao CMS / repositorio** (WordPress, Webflow, Next.js, Astro, headless, etc.).
- [ ] **Stack do site** conhecida (CMS, render — CSR/SSR/SSG/ISR, framework, CDN).
- [ ] **Politica editorial e de marca** (voz, tom, glossario, sinonimos a evitar).
- [ ] **Persona / ICP** (define linguagem, profundidade, exemplos).
- [ ] **EEAT acessivel** — quem assina, com que credencial, com que fonte.
- [ ] **GSC + GA4** para medicao posterior.

> **Cristal C0 — NAO CHUTAR.** Estrutura de pagina recomendada deve ser baseada em SERP atual + briefing real. Sem briefing de KW, esta skill **nao executa** — pede a `seo-keywords` rodar primeiro, ou pede que o usuario forneca KW + intent + URL.

---

## 2. Anatomia da pagina otimizada — modelo mental

Toda pagina SEO segue uma anatomia base, com variacoes por tipo (Secao 16). Modelo mental:

```
=========================================
| <head>                                |
|   <title>                             |
|   <meta description>                  |
|   <link rel="canonical">              |
|   <link rel="alternate" hreflang>     |
|   <meta robots>                       |
|   OpenGraph + Twitter Cards           |
|   schema.org JSON-LD                  |
|   <link preconnect/preload>           |
|   <link rel="icon">                   |
| </head>                               |
| <body>                                |
|   Header com nav + breadcrumb         |
|   ----- ABOVE-THE-FOLD -----          |
|   H1 + sub-titulo                     |
|   Autor box (se editorial)            |
|   TL;DR / resposta direta             |
|   ----- BODY -----                    |
|   H2-1 (sub-intent 1)                 |
|     conteudo + imagens + tabelas      |
|     internal links contextual         |
|   H2-2 (sub-intent 2)                 |
|     ...                               |
|   H2-N (FAQ)                          |
|     FAQPage schema                    |
|   ----- BELOW-THE-FOLD -----          |
|   Conclusao / CTA                     |
|   Bio do autor expandida              |
|   Conteudo relacionado                |
|   Footer                              |
| </body>                               |
=========================================
```

### 2.1 Above-the-fold = decisao em 3 segundos

- **H1 que espelha a query** (intent confirmation).
- **Sub-titulo** que explicita o angulo unico.
- **TL;DR / resposta direta** em 40-60 palavras (oportunidade de Featured Snippet + AI Overview).
- **Autor + credencial + data** visiveis (EEAT).

### 2.2 Body = profundidade + escaneabilidade

- **Inverted pyramid**: resposta -> contexto -> profundidade.
- **Hierarquia clara** com H2/H3 espelhando sub-intents.
- **Componentes visuais** (imagens originais, tabelas, listas, callouts) a cada 200-400 palavras.
- **Internal links contextuais** em paragrafos, nao em "leia mais".

### 2.3 Below-the-fold = signals de qualidade

- **CTA** alinhada ao intent (TOFU = newsletter; BOFU = trial/contato).
- **Bio do autor expandida** com credenciais.
- **Conteudo relacionado** (cluster sibling links).
- **Schema** completo (Article + Author + Organization + BreadcrumbList).

---

## 3. Title tag — formula e melhores praticas

### 3.1 Funcao

- Aparece como link clicavel na SERP (Google **pode** reescrever — ~60% dos casos em estudos de mercado).
- Aparece na aba do navegador.
- Aparece em links de compartilhamento (fallback se nao houver `og:title`).

### 3.2 Comprimento

| Aspecto | Valor |
|---------|-------|
| Limite **pixel** (Google) | ~600 px (varia mobile/desktop) |
| Limite **caracteres** indicativo | 50-60 |
| Branded suffix recomendado | " | Marca" ou " - Marca" no final |
| Truncamento | Google adiciona "..." se exceder |

> Google reescreve title quando: (a) muito longo; (b) keyword stuffed; (c) duplicado; (d) generico ("Home"); (e) nao casa com a query do usuario.

### 3.3 Formulas

| Formula | Exemplo |
|---------|---------|
| **Keyword + Beneficio** | "CRM para Startup: 5 Opcoes Gratis e Pagas (Guia 2026)" |
| **Numero + Keyword + Beneficio** | "11 Melhores CRMs para Pequenas Empresas em 2026" |
| **How to + Keyword** | "Como Configurar GA4 em 30 Minutos (Passo a Passo)" |
| **Keyword + vs + Keyword** | "Pipedrive vs RD Station: Comparativo Completo 2026" |
| **Pergunta + Keyword** | "O que e Core Web Vitals? Guia Definitivo" |
| **Keyword + [Ano]** | "Marketing Digital para Advogados: Guia Atualizado 2026" |
| **Definicao + Keyword** | "DPA: O que e e Como Implementar (LGPD)" |

### 3.4 Modificadores de CTR

| Modificador | Quando usar |
|-------------|-------------|
| **Numero** ("11", "7", "5") | Listicle / comparativo |
| **Ano** ("2026") | Conteudo volatil; lembrar de atualizar |
| **[Bracket]** ("[Guia]", "[Template Gratis]") | Diferenciar visualmente |
| **Pergunta** | Intent informacional |
| **"Definitivo" / "Completo"** | Pillar page (cuidado com clickbait) |
| **"Gratis"** | Trans/comercial |
| **"Atualizado [data]"** | Topicos volateis |

### 3.5 Anti-patterns

- Keyword stuffing: "CRM CRM Vendas CRM Sistema CRM" -> Google reescreve ou penaliza.
- Title generico: "Home" / "Blog" / "Categoria 1".
- Duplicacao em massa: 200 paginas com mesmo title -> cannibalization + reescrita Google.
- Mismatch com H1: title diz X, H1 diz Y -> sinal incoerente.

---

## 4. Meta description

### 4.1 Funcao

- **NAO e fator de ranking direto** (Google confirmou multiplas vezes).
- E **fator de CTR** — afeta cliques na SERP.
- Google **reescreve** em ~60-70% dos casos baseado na query.
- E o pitch da pagina em ~155 chars.

### 4.2 Comprimento

| Aspecto | Valor |
|---------|-------|
| Limite indicativo | 150-160 caracteres |
| Limite mobile | ~120 caracteres (varia) |
| Truncamento | Google adiciona "..." |

### 4.3 Formula

```
[Verbo de acao] + [keyword] + [beneficio principal] + [diferencial/credibilidade] + [CTA implicita ou explicita]
```

Exemplos:
- "Compare 11 CRMs para startup em 2026 — preco, integracao com WhatsApp, e implantacao em 30 dias. Por especialista com 10+ anos."
- "Guia passo a passo de Core Web Vitals 2026: LCP, INP, CLS, threshold e como medir em CrUX. Inclui template de auditoria."
- "DPA: o que e, quando exigir e clausulas obrigatorias para LGPD. Template aprovado por especialista juridico — download gratis."

### 4.4 Anti-patterns

- Copiar primeira frase do conteudo (Google ja faz isso).
- Keyword stuffing.
- Generica: "Saiba mais sobre nosso produto."
- Promessa que pagina nao entrega (clickbait — Helpful Content penaliza).
- Vazia (Google pega snippet do body — perde controle do pitch).

---

## 5. URL / slug / breadcrumb

### 5.1 Estrutura recomendada

```
https://dominio.com/categoria/keyword-principal/
```

| Aspecto | Recomendacao |
|---------|---------------|
| **Comprimento** | <= 60-80 caracteres |
| **Separador** | Hifen (`-`), nunca underscore (`_`) |
| **Caso** | Sempre lowercase |
| **Acentos** | Evitar (compatibilidade) |
| **Stop words** | Remover ("de", "para", "a", "o") quando nao prejudica leitura |
| **Profundidade** | Max 3-4 niveis (`/cat/sub/pagina/`) |
| **Trailing slash** | Consistente em todo o site (sempre com OU sempre sem) |

### 5.2 URL falando = SEO + UX + share

- Ruim: `/post?id=2387`
- Ruim: `/2026/05/07/crm-para-startup-guia-completo-em-portugues/`
- Boa: `/crm-para-startup/`
- Boa: `/blog/crm-para-startup/`

### 5.3 Breadcrumb

Caminho navegavel + schema BreadcrumbList:

```
Home > Blog > CRM > CRM para Startup
```

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://dominio.com/" },
    { "@type": "ListItem", "position": 2, "name": "Blog", "item": "https://dominio.com/blog/" },
    { "@type": "ListItem", "position": 3, "name": "CRM", "item": "https://dominio.com/blog/crm/" },
    { "@type": "ListItem", "position": 4, "name": "CRM para Startup" }
  ]
}
```

> Aparece como rich result na SERP em vez do dominio puro.

### 5.4 Migrations

Trocar URL = perder ranking se nao houver 301:

- **Mapping 1:1** sempre (URL antiga -> URL nova).
- **301 permanente** (passa autoridade).
- **NAO encadear redirects** (302 -> 301 -> 200 -> 301 -> 200 e ruim).
- Atualizar **internal links** para a URL nova.
- Atualizar **sitemap** + submeter no GSC.
- Monitorar GSC > Cobertura por 30-60 dias.

---

## 6. Hierarquia de headings (H1-H6)

### 6.1 Regras

| Regra | Detalhe |
|-------|---------|
| **H1 unico por pagina** | 1 H1 e o titulo principal — espelha a query principal |
| **H2 = sub-intents** | Cada H2 cobre um sub-intent / sub-pergunta (PAA) |
| **H3 = sub-secoes de H2** | Aprofundamento |
| **H4-H6 raramente uteis** | Usar apenas se hierarquia exige |
| **Ordem semantica** | Nunca pular niveis (H1 -> H3 sem H2) — quebra accessibility |
| **NAO usar para estilizacao** | H nao e tamanho de fonte; isso e CSS |

### 6.2 H1 — formulas

- Espelhar a query principal (variacao OK, contanto que sinonimos cubram a intencao).
- Pode ser igual ou ligeiramente diferente do title (mais natural no body).
- Comprimento livre (mas legivel — 60-80 chars).

| Exemplo | Bom / Ruim |
|---------|-----------|
| H1: "CRM para Startup: Guia Completo 2026" | Bom |
| H1: "Bem-vindo ao nosso blog!" | Ruim — sem keyword |
| H1: "CRM CRM CRM Startup CRM" | Ruim — stuffed |
| H1: "Home" | Ruim — generico |

### 6.3 H2 — espelhar PAA + sub-intents

A partir de PAA + related searches da KW principal:

```
H1: CRM para Startup: Guia Completo 2026
  H2: O que e CRM para startup (e como difere de CRM enterprise)
  H2: Quando uma startup precisa de CRM
  H2: Funcionalidades essenciais
  H2: Comparativo: 5 CRMs avaliados
    H3: Pipedrive
    H3: RD Station
    H3: HubSpot
    H3: Agendor
    H3: Folk
  H2: Quanto custa um CRM para startup
  H2: Como implementar em 30 dias
  H2: Perguntas frequentes (FAQ)
```

H2 em formato pergunta = aumenta chance de Featured Snippet + AI Overview.

### 6.4 Acessibilidade (WCAG)

- Ordem hierarquica = leitor de tela navega corretamente.
- Sem pular niveis.
- H1 deve descrever a pagina (nao "Menu" ou "Logo").
- Contraste suficiente.

---

## 7. Body content — TL;DR + inverted pyramid

### 7.1 Estrutura

```
H1
sub-titulo

[TL;DR — 40-60 palavras] <- Featured Snippet + AI Overview oportunidade

H2-1: [pergunta principal]
  Resposta direta no primeiro paragrafo
  Contexto + profundidade

H2-2: [sub-pergunta 1]
  Resposta direta
  Profundidade

...

H2-N: FAQ
  FAQPage schema
```

### 7.2 TL;DR / resposta direta

- 40-60 palavras.
- Responde a query principal sem floreio.
- Logo apos o H1 (acima do fold).
- Estrutura: definicao + 2-3 caracteristicas-chave + ressalva.

Exemplo:
> **TL;DR:** Core Web Vitals sao 3 metricas oficiais do Google que medem UX em campo: **LCP** (carregamento <= 2.5s), **INP** (interacao <= 200ms) e **CLS** (estabilidade visual <= 0.1). Substituiram FID em mar/2024. Sao parte do Page Experience Signal e medidas via dados reais (CrUX), nao apenas Lighthouse lab.

### 7.3 Profundidade

- Profundidade necessaria para responder o intent — nao mais, nao menos.
- "1500 palavras" nao e regra; e media observada para topicos competitivos.
- Profundidade desejavel:
  - Topico TOFU informacional simples: 800-1500 palavras.
  - Pillar page: 2500-5000 palavras.
  - Listicle / comparativo: 1500-3000 palavras.
  - HowTo: 800-2000 palavras + screenshots.

### 7.4 Anti-fluff

- Nao escrever "neste artigo, vamos abordar" no inicio. Va direto.
- Eliminar paragrafos repetitivos (que dizem o mesmo de outra forma).
- Eliminar generalidades vazias ("e importante levar em conta varios fatores").
- Cada paragrafo deve adicionar **fato, exemplo, dado, ou nuance**.

### 7.5 Estilo escaneavel

| Tecnica | Por que |
|---------|---------|
| Bullet/numero a cada 3-5 paragrafos | Quebra visual |
| **Negrito** em termos-chave (sem abusar) | Eye-anchor |
| Tabelas para comparativo, lista de features | Scan rapido |
| Callout / blockquote para frase-chave | Destaque |
| Imagens originais a cada 200-400 palavras | Engajamento + image SEO |
| Subhead a cada 200-300 palavras | Hierarquia clara |

### 7.6 Originalidade

Helpful Content System penaliza:
- Conteudo escalado / IA sem revisao + sem expertise.
- Reproducao de fontes existentes sem valor agregado.
- Reescrita superficial ("spinning") de top 3 da SERP.

Originalidade demonstravel:
- Dado proprio (research, survey, dataset).
- Experiencia direta (screenshots, prints, video do produto sendo usado).
- Opiniao fundamentada (com EEAT visivel).
- Caso real (com cliente, anonimizado se necessario).

---

## 8. Internal linking

### 8.1 Funcao

- Distribui **autoridade** (PageRank interno) entre paginas.
- Define **arquitetura semantica** do site (cluster topical).
- Ajuda Googlebot a **descobrir** paginas novas.
- Ajuda usuario a **navegar** profundamente.

### 8.2 Anchor text

| Tipo de anchor | Exemplo | Quando usar |
|-----------------|---------|-------------|
| **Exact match** | "CRM para startup" | Limitar — Google penaliza over-optimization |
| **Partial match** | "guia de CRM para startup" | Default, mais natural |
| **Branded** | "no Pipedrive" | Para marca |
| **Generico** | "leia aqui", "saiba mais" | Evitar — desperdica sinal |
| **Naked URL** | "https://..." | Raramente, em referencias |
| **Imagem (alt como anchor)** | imagem clicavel com alt descritivo | Quando faz sentido visual |

> Distribuicao saudavel: ~20-40% exact/partial, ~30-50% branded, ~20% naked + generico (raro). Variar.

### 8.3 Ratio e distribuicao

- Cada pagina recebe links de pelo menos 3-5 paginas internas.
- Pillar -> spokes (todos).
- Spokes -> pillar (no inicio).
- Spokes -> spoke siblings (transversal contextual).
- Homepage -> pillars (autoridade descendo).

### 8.4 Hub-and-spoke / pillar-cluster

```
[Home] --> [Pillar /crm-para-startup]
                  |
        +---------+---------+---------+---------+
        |         |         |         |         |
   [Spoke 1]  [Spoke 2]  [Spoke 3]  [Spoke 4]  [Spoke 5]
        |         |         |         |         |
        +---------+---------+---------+---------+
                  | (siblings linkam entre si quando contextual)
```

### 8.5 Anti-patterns

- "Read more" como anchor exclusivo.
- Footer com 200 links (link farm interno).
- Linkar apenas para homepage / categoria (nao distribui autoridade).
- Quebrar paginas profundas (orfas — sem link interno apontando).
- Cannibalization de anchor (mesma anchor para multiplas URLs).

### 8.6 Auditoria

| Ferramenta | O que verifica |
|------------|----------------|
| Screaming Frog | Crawl + relatorio de internal links |
| Ahrefs Site Explorer > Internal Links | Por URL |
| Semrush Site Audit | Internal linking issues |
| Google Search Console > Links | Visao Google das paginas mais linkadas |

---

## 9. External linking

### 9.1 Funcao

- Da contexto e credibilidade ao conteudo.
- Sinaliza pesquisa real (EEAT — fonte primaria).
- NAO "vaza autoridade" significativamente — mito antigo.

### 9.2 Atributos `rel` (HTML5 + Google)

| Atributo | Significado |
|----------|-------------|
| **(sem rel)** | Dofollow — endorsa o link, passa autoridade |
| **rel="nofollow"** | Nao endorsa para SEO; em 2019 Google passou a tratar como hint, nao directive |
| **rel="ugc"** | User-generated content (comentario, forum) |
| **rel="sponsored"** | Conteudo pago / patrocinado / afiliado |
| **rel="noopener"** | Seguranca em `target="_blank"` |
| **rel="noreferrer"** | Privacidade — nao envia referer |

### 9.3 Quando linkar

- **SIM**: fonte primaria (paper, norma, dados oficiais), citacao de autoridade reconhecida, ferramenta mencionada.
- **CUIDADO**: concorrentes diretos (so se valor agregado for alto).
- **NAO**: links pagos sem `rel="sponsored"` (viola Spam Policies).
- **NAO**: link spam reciproco em massa.

### 9.4 Disclosure (LGPD / CONAR / CDC + Helpful Content)

Conteudo afiliado / patrocinado deve ter:
- `rel="sponsored"` no link.
- Disclosure visivel no inicio do conteudo ("Este post contem links de afiliado").
- Schema (em alguns casos: `Product` com `seller`/`offers`).

---

## 10. Imagens

### 10.1 Atributos basicos

```html
<img
  src="/images/crm-startup-comparativo-2026.avif"
  srcset="/images/crm-startup-comparativo-2026.avif 1x,
          /images/crm-startup-comparativo-2026@2x.avif 2x"
  sizes="(max-width: 768px) 100vw, 800px"
  width="800"
  height="450"
  loading="lazy"
  decoding="async"
  alt="Comparativo de 5 CRMs para startup em 2026 com preco e funcionalidades"
  fetchpriority="auto"
/>
```

### 10.2 Alt text

- **Descritivo**, nao keyword stuffed.
- 5-15 palavras tipico.
- Inclui keyword **se natural**.
- Vazio (`alt=""`) para imagens decorativas (acessibilidade).
- NUNCA `alt="image1.jpg"` ou `alt="foto"`.

### 10.3 File name

- Descritivo, com hifens, lowercase.
- Bom: `crm-startup-comparativo-2026.avif`
- Ruim: `IMG_2387.jpg`

### 10.4 Formato

| Formato | Quando usar |
|---------|-------------|
| **AVIF** | Default 2026 — melhor compressao |
| **WebP** | Fallback amplo, ainda excelente |
| **JPEG** | Fallback legado |
| **PNG** | Imagem com transparencia / texto pixelado nitido |
| **SVG** | Icone, logo, ilustracao vetorial |

### 10.5 Performance (impacta CWV — LCP)

- Imagem hero: `fetchpriority="high"` + `preload`.
- Demais: `loading="lazy"` + `decoding="async"`.
- Definir `width` + `height` (evita CLS).
- `srcset` + `sizes` para responsive.
- CDN com transformacoes automaticas (Cloudflare Images, Cloudinary, Imgix).

### 10.6 Schema ImageObject

```json
{
  "@context": "https://schema.org",
  "@type": "ImageObject",
  "contentUrl": "https://dominio.com/images/crm-startup-comparativo-2026.avif",
  "name": "Comparativo de 5 CRMs para startup em 2026",
  "description": "Tabela comparando preco, funcionalidades e integracoes",
  "creditText": "Frank-MKT / SPKR",
  "creator": { "@type": "Person", "name": "Alexandre Jalkh" },
  "license": "https://dominio.com/licenca",
  "acquireLicensePage": "https://dominio.com/licenca",
  "copyrightNotice": "(c) 2026 SPKR"
}
```

---

## 11. Videos

### 11.1 Embed

- Preferir embed lazy (Youtube embed lite, Vimeo lazy).
- `loading="lazy"` no iframe (suporte parcial).
- Thumbnail original como `poster`.

### 11.2 Schema VideoObject

```json
{
  "@context": "https://schema.org",
  "@type": "VideoObject",
  "name": "Como configurar GA4 em 30 minutos",
  "description": "Tutorial passo a passo de configuracao GA4...",
  "thumbnailUrl": ["https://dominio.com/thumb.avif"],
  "uploadDate": "2026-05-07T10:00:00-03:00",
  "duration": "PT12M30S",
  "contentUrl": "https://dominio.com/video/ga4.mp4",
  "embedUrl": "https://www.youtube.com/embed/XYZ",
  "publisher": { "@type": "Organization", "name": "SPKR", "logo": { "@type": "ImageObject", "url": "..." } },
  "author": { "@type": "Person", "name": "Alexandre Jalkh" },
  "transcript": "Texto completo do video...",
  "hasPart": [
    { "@type": "Clip", "name": "Introducao", "startOffset": 0, "url": "...?t=0s" },
    { "@type": "Clip", "name": "Criar conta GA4", "startOffset": 90, "url": "...?t=90s" }
  ]
}
```

### 11.3 Transcript

- Aumenta indexacao (texto completo).
- Acessibilidade.
- Pode aparecer em SERP via "Key Moments".

---

## 12. Schema.org / JSON-LD — biblioteca operacional

### 12.1 Tipos mais usados

| Tipo | Para que pagina | Rich result Google? |
|------|------------------|---------------------|
| **Article** / **NewsArticle** / **BlogPosting** | Conteudo editorial | Top Stories, Key Moments |
| **FAQPage** | FAQ explicito | Sim — FAQ rich result |
| **HowTo** | Passo a passo | Sim — HowTo rich result |
| **Product** + **Offer** | Pagina de produto | Sim — Shopping, Reviews |
| **Review** / **AggregateRating** | Reviews | Sim — Stars |
| **Person** | Autor / perfil | Knowledge panel possivel |
| **Organization** | Empresa | Knowledge panel possivel |
| **BreadcrumbList** | Navegacao | Sim — Breadcrumb na SERP |
| **LocalBusiness** + sub-tipos | Negocio local | Local pack |
| **Recipe** | Receita | Sim — Recipe rich result |
| **Event** | Evento | Sim — Event rich result |
| **JobPosting** | Vaga | Sim — Google Jobs |
| **Course** | Curso | Sim — Course rich result |
| **Book** | Livro | Sim — Book rich result |
| **VideoObject** | Video | Sim — Key Moments |
| **ImageObject** | Imagem | Image rich result |
| **WebSite** + **SearchAction** | Homepage com busca | Sitelinks search box |
| **WebPage** | Generica | Default |
| **SpeakableSpecification** | Trecho falavel (voice) | Voice search |
| **Dataset** | Dados estruturados | Dataset Search |

> **Re-validar disponibilidade de rich result em** https://developers.google.com/search/docs/appearance/structured-data — Google adiciona/remove tipos. Em 2023, FAQ e HowTo tiveram visibilidade reduzida em alguns mercados; re-checar antes de citar.

### 12.2 Localizacao

- Colocar JSON-LD em `<head>` ou imediatamente antes de `</body>`.
- Multiplos blocos JSON-LD na mesma pagina sao OK (Google funde).
- Validar com **Schema Markup Validator** (validator.schema.org) e **Rich Results Test** (search.google.com/test/rich-results).

### 12.3 Article (template completo)

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://dominio.com/crm-para-startup/" },
  "headline": "CRM para Startup: Guia Completo 2026",
  "description": "Comparativo de 5 CRMs para startup em 2026, com preco, integracao com WhatsApp e plano de implementacao em 30 dias.",
  "image": [
    "https://dominio.com/images/crm-startup-1x1.avif",
    "https://dominio.com/images/crm-startup-4x3.avif",
    "https://dominio.com/images/crm-startup-16x9.avif"
  ],
  "datePublished": "2026-05-07T10:00:00-03:00",
  "dateModified": "2026-05-07T10:00:00-03:00",
  "author": {
    "@type": "Person",
    "name": "Alexandre Jalkh",
    "url": "https://dominio.com/autor/alexandre-jalkh",
    "sameAs": [
      "https://www.linkedin.com/in/alexandrejalkh",
      "https://lattes.cnpq.br/XXXXX"
    ],
    "jobTitle": "Consultor de Marketing e Inteligencia de Mercado",
    "worksFor": { "@type": "Organization", "name": "SPKR" }
  },
  "publisher": {
    "@type": "Organization",
    "name": "SPKR",
    "logo": {
      "@type": "ImageObject",
      "url": "https://dominio.com/logo-spkr.png",
      "width": 600, "height": 60
    }
  },
  "inLanguage": "pt-BR",
  "articleSection": "CRM",
  "keywords": ["CRM startup", "Pipedrive", "RD Station", "vendas B2B"],
  "wordCount": 3200
}
</script>
```

### 12.4 FAQPage

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "O que e CRM para startup?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "CRM para startup e um sistema de gestao de relacionamento com clientes adaptado a empresas em estagio inicial — leve, rapido de implementar, com pricing escalavel e integracoes essenciais (e-mail, WhatsApp, calendario)."
      }
    },
    {
      "@type": "Question",
      "name": "Quando uma startup precisa de CRM?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Tipicamente apos o primeiro ano com pelo menos 50 leads/mes, ou quando o time de vendas tem 2+ pessoas e planilha ja gera retrabalho."
      }
    }
  ]
}
```

### 12.5 HowTo

```json
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "Como configurar GA4 em 30 minutos",
  "description": "Tutorial passo a passo para configurar Google Analytics 4 em um site novo.",
  "totalTime": "PT30M",
  "estimatedCost": { "@type": "MonetaryAmount", "currency": "BRL", "value": "0" },
  "supply": [{ "@type": "HowToSupply", "name": "Conta Google" }],
  "tool": [{ "@type": "HowToTool", "name": "Google Tag Manager (opcional)" }],
  "step": [
    { "@type": "HowToStep", "position": 1, "name": "Criar conta GA4", "text": "...", "url": "https://dominio.com/tutorial-ga4#passo-1", "image": "https://..." },
    { "@type": "HowToStep", "position": 2, "name": "Configurar fluxo de dados", "text": "...", "url": "https://dominio.com/tutorial-ga4#passo-2", "image": "https://..." }
  ]
}
```

### 12.6 Product + Offer + AggregateRating

```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Pipedrive Starter",
  "image": "https://dominio.com/images/pipedrive-starter.avif",
  "description": "Plano basico do Pipedrive para times pequenos.",
  "brand": { "@type": "Brand", "name": "Pipedrive" },
  "sku": "PD-STARTER-2026",
  "offers": {
    "@type": "Offer",
    "url": "https://dominio.com/pipedrive-trial",
    "priceCurrency": "USD",
    "price": "14.90",
    "priceValidUntil": "2026-12-31",
    "availability": "https://schema.org/InStock",
    "seller": { "@type": "Organization", "name": "Pipedrive" }
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.5",
    "reviewCount": "128"
  }
}
```

### 12.7 Person + Organization + sameAs (EEAT)

```json
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "Alexandre Jalkh",
  "url": "https://dominio.com/autor/alexandre-jalkh",
  "image": "https://dominio.com/avatar/alexandre.avif",
  "jobTitle": "Consultor de Marketing e Inteligencia de Mercado",
  "worksFor": { "@type": "Organization", "name": "SPKR" },
  "alumniOf": "Universidade X",
  "knowsAbout": ["Marketing Digital", "SEO", "Pesquisa de Mercado", "Branding"],
  "sameAs": [
    "https://www.linkedin.com/in/alexandrejalkh",
    "https://lattes.cnpq.br/XXXXX",
    "https://twitter.com/alexandrejalkh",
    "https://www.wikidata.org/wiki/QXXXXX"
  ]
}
```

### 12.8 LocalBusiness

```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "@id": "https://dominio.com/contato/#empresa",
  "name": "SPKR Servicos e Consultoria",
  "url": "https://dominio.com",
  "telephone": "+55-11-XXXX-XXXX",
  "email": "contato@dominio.com",
  "image": "https://dominio.com/foto-fachada.avif",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Rua Exemplo, 123",
    "addressLocality": "Sao Paulo",
    "addressRegion": "SP",
    "postalCode": "01234-567",
    "addressCountry": "BR"
  },
  "geo": { "@type": "GeoCoordinates", "latitude": -23.55, "longitude": -46.63 },
  "openingHoursSpecification": [
    { "@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"], "opens": "09:00", "closes": "18:00" }
  ],
  "priceRange": "$$",
  "sameAs": [
    "https://www.linkedin.com/company/spkr",
    "https://www.instagram.com/spkr"
  ],
  "aggregateRating": { "@type": "AggregateRating", "ratingValue": "4.8", "reviewCount": "67" }
}
```

### 12.9 WebSite + SearchAction

```json
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "url": "https://dominio.com/",
  "name": "SPKR",
  "potentialAction": {
    "@type": "SearchAction",
    "target": "https://dominio.com/buscar?q={search_term_string}",
    "query-input": "required name=search_term_string"
  }
}
```

### 12.10 Composicao multipla

Uma pagina pode (e deve, quando aplicavel) ter varios JSON-LD: BreadcrumbList + Article + Person (autor) + Organization (publisher) + FAQPage + ImageObject. Validar com Schema Markup Validator + Rich Results Test.

---

## 13. OpenGraph + Twitter Cards

### 13.1 OpenGraph (Facebook, LinkedIn, WhatsApp)

```html
<meta property="og:type" content="article" />
<meta property="og:title" content="CRM para Startup: Guia Completo 2026" />
<meta property="og:description" content="Comparativo de 5 CRMs..." />
<meta property="og:url" content="https://dominio.com/crm-para-startup/" />
<meta property="og:image" content="https://dominio.com/images/og/crm-startup-1200x630.avif" />
<meta property="og:image:width" content="1200" />
<meta property="og:image:height" content="630" />
<meta property="og:site_name" content="SPKR" />
<meta property="og:locale" content="pt_BR" />
<meta property="article:published_time" content="2026-05-07T10:00:00-03:00" />
<meta property="article:modified_time" content="2026-05-07T10:00:00-03:00" />
<meta property="article:author" content="https://dominio.com/autor/alexandre-jalkh" />
```

### 13.2 Twitter Cards

```html
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:site" content="@spkr" />
<meta name="twitter:creator" content="@alexandrejalkh" />
<meta name="twitter:title" content="CRM para Startup: Guia Completo 2026" />
<meta name="twitter:description" content="Comparativo de 5 CRMs..." />
<meta name="twitter:image" content="https://dominio.com/images/og/crm-startup-1200x630.avif" />
```

### 13.3 Recomendacoes

- Imagem 1200x630 (proporcao 1.91:1) para `og:image` e `twitter:image`.
- AVIF/WebP com fallback JPEG.
- `og:locale` correto (pt_BR vs pt_PT vs en_US).
- Validar:
  - Facebook: developers.facebook.com/tools/debug
  - LinkedIn: www.linkedin.com/post-inspector
  - X (Twitter): cards-dev.twitter.com (descontinuado parcialmente — checar)
  - WhatsApp: usa OG; testar via mensagem direta.

---

## 14. EEAT on-page — sinais visiveis e estruturados

### 14.1 Visiveis ao usuario

| Sinal | Onde |
|-------|------|
| **Bio do autor** com foto, credencial, link para perfil | Topo + final do artigo |
| **Data de publicacao + ultima atualizacao** | Topo do artigo, com tooltip se diferente |
| **Editorial standards** | Pagina dedicada linkada do footer |
| **Politica de correcao** | Pagina dedicada |
| **Disclosure** (afiliado / patrocinado / conflito) | Topo do artigo, antes do conteudo |
| **Fontes citadas** | Inline no texto, com link |
| **Reviewed by [especialista]** | Quando aplicavel (YMYL) |
| **Trust badges** (certificacoes, premios) | Footer / about |

### 14.2 Estruturados (schema)

- `Person` para autor com `sameAs` a perfis profissionais.
- `Organization` para publisher com `logo`, `sameAs` a Wikidata, perfis sociais.
- `Article` com `author`, `publisher`, `dateModified`.
- `Reviewed by` (extensoes em `creator`, `editor`).

### 14.3 YMYL — EEAT extra

Para topicos YMYL (saude, financas, legal, seguranca, eleicao), reforcar:
- Autor com **credencial regulada** (CRM, OAB, CRC, doutorado).
- "Reviewed by" especialista qualificado.
- Fontes primarias oficiais (lei, paper, norma).
- Disclosure: "Este conteudo nao substitui consulta profissional."

---

## 15. Otimizacao para SERP features

### 15.1 Featured Snippet (posicao zero)

Estrutura por tipo:

| Tipo | Como otimizar |
|------|---------------|
| **Paragraph** | Pergunta como H2 + resposta em 40-60 palavras logo abaixo |
| **Numbered list** | H2 + `<ol>` com itens curtos (10-15 palavras) |
| **Bulleted list** | H2 + `<ul>` com itens curtos |
| **Table** | H2 + `<table>` com `<th>` semanticos |
| **Video** | YouTube embed + transcript + `VideoObject` schema |

### 15.2 People Also Ask (PAA)

- Cobrir 3-5 PAA da KW principal como H2 ou em `FAQPage` schema.
- Resposta direta na primeira frase de cada secao.
- Linguagem natural conversacional.

### 15.3 AI Overview / SGE / LLM citation

Heuristica observada (re-validar):

- **TL;DR no inicio** — citacao mais provavel quando ha resposta direta concentrada.
- **Estrutura semantica forte** — H, listas, tabelas, FAQ schema.
- **Fatos verificaveis** com fonte primaria linkada.
- **Schema.org rico** — Article + Author + Organization + FAQPage + (HowTo se aplicavel).
- **Cobertura de entidade** com atributos e relacoes.
- **`dateModified`** atualizada.
- **Autoridade do dominio** (autoridade -> citacao).
- **Co-citacoes** — site mencionado em outros sites autoritativos.
- **EEAT** demonstravel.

### 15.4 Image Pack

- Imagens originais.
- Alt + file name descritivos.
- Schema `ImageObject` quando relevante.
- Imagem otimizada (peso baixo, AVIF/WebP).
- Captions e contexto na pagina.

### 15.5 Top Stories

- Schema `NewsArticle`.
- Publisher reconhecido (Google News se cadastrado).
- Freshness (`datePublished` recente).
- AMP nao e mais requerido (mudanca de 2021).

---

## 16. Anatomia por tipo de pagina

### 16.1 Pillar page

```
H1: [Topico amplo] — Guia Completo [Ano]
sub-titulo: angulo unico

[TL;DR — 60-80 palavras]
[Index / table of contents com anchor links]

H2: O que e [topico] (definicao + entidade)
  Definicao + atributos + relacoes

H2: Quando / Por que [topico] importa
  Contexto, casos de uso

H2: Componentes / Sub-temas (link para spokes)
  Mini-resumo de cada subtema + link

H2: Comparativo / Lista (se aplicavel)

H2: Como aplicar / passo a passo (se cabe)

H2: Erros comuns

H2: Tendencias e atualizacoes (decay temporal)

H2: Perguntas frequentes (FAQPage schema)

H2: Conclusao + CTA

Bio do autor expandida.
Schema: Article + Person + Organization + BreadcrumbList + FAQPage.
~2500-5000 palavras.
```

### 16.2 Cluster (spoke) page

```
H1: [Sub-topico especifico]
sub-titulo

[TL;DR — 40-60 palavras]
[Link contextual para pillar no inicio: "Este artigo faz parte do guia [Topico]"]

H2: [Sub-intent 1]
H2: [Sub-intent 2]
H2: [Sub-intent 3]
H2: FAQ (FAQPage)
H2: CTA + Conteudo relacionado (siblings)

Schema: Article + Person + Organization + BreadcrumbList + FAQPage.
~1000-2000 palavras.
```

### 16.3 Listicle ("11 melhores X para Y")

```
H1: 11 Melhores [X] para [Y] em [Ano]
sub-titulo

[TL;DR — top 3 + ressalva]
[Tabela comparativa resumo]

H2: Como avaliamos [criterios] (transparencia + EEAT)
H2: 1. [Item 1]
  H3: Quem usa
  H3: Pros
  H3: Contras
  H3: Preco
  H3: Veredicto
H2: 2. [Item 2]
...
H2: 11. [Item 11]
H2: Como escolher entre [X] (decision tree)
H2: FAQ
H2: Metodologia (apendice)

Schema: Article + Person + Organization + BreadcrumbList + Product (cada item) + AggregateRating + FAQPage.
~2500-4000 palavras.
```

### 16.4 Comparativo (X vs Y)

```
H1: [X] vs [Y]: Comparativo Completo [Ano]
sub-titulo

[TL;DR — vencedor por categoria]
[Tabela lado a lado: feature por feature]

H2: Visao geral de [X]
H2: Visao geral de [Y]
H2: [X] vs [Y] — Funcionalidades
H2: [X] vs [Y] — Preco
H2: [X] vs [Y] — Integracoes
H2: [X] vs [Y] — Suporte
H2: [X] vs [Y] — Curva de aprendizado
H2: Quem deve escolher [X]
H2: Quem deve escolher [Y]
H2: Veredicto
H2: FAQ

Schema: Article + Product (X) + Product (Y) + Review + AggregateRating + FAQPage.
~2000-3500 palavras.
```

### 16.5 HowTo / passo a passo

```
H1: Como [tarefa] em [tempo] (Passo a Passo)
sub-titulo

[TL;DR + total time + custo + materiais]

H2: O que voce precisa antes de comecar
H2: Passo 1: [acao]
  Texto + screenshot + tip
H2: Passo 2: [acao]
...
H2: Passo N: [acao]
H2: Como verificar que funcionou
H2: Erros comuns e como resolver
H2: FAQ

Schema: HowTo (com `step`, `tool`, `supply`, `totalTime`) + Article + Person + FAQPage.
~1000-2500 palavras.
```

### 16.6 Product page (e-commerce)

```
H1: [Nome do produto]
[Preco] [Avaliacao com estrelas] [Link de compra]

[Galeria de imagens]
[Resumo do produto — beneficio em 2 linhas]
[Variacoes/opcoes]

H2: Descricao
H2: Especificacoes (tabela)
H2: Como usar / aplicar
H2: Avaliacoes (Reviews)
H2: Perguntas frequentes (FAQPage)
H2: Politica de troca / garantia

Schema: Product + Offer + AggregateRating + Review (varios) + BreadcrumbList + FAQPage + Image.
```

### 16.7 Local page (negocio local)

```
H1: [Servico] em [cidade/bairro]
sub-titulo: "Atendimento desde [ano]"

[NAP — Nome, Endereco, Telefone, mapa]
[Horario de funcionamento]
[Reviews em destaque]

H2: O que oferecemos
H2: Bairros / regioes atendidos
H2: Como chegar (mapa + transporte)
H2: Reviews
H2: FAQ
H2: Contato

Schema: LocalBusiness + GeoCoordinates + OpeningHours + AggregateRating + Review + FAQPage + BreadcrumbList.
```

### 16.8 Blog editorial

```
H1: [Titulo editorial]
[autor, data, tempo de leitura]

[Hero image]
[TL;DR — 40-60 palavras]

H2-H2-H2 conforme angulo

Bio do autor.
Conteudo relacionado.

Schema: Article ou BlogPosting + Person + Organization + BreadcrumbList.
```

---

## 17. Anti-patterns

| Anti-pattern | Por que e problema |
|--------------|---------------------|
| **Keyword stuffing** | Spam Policies — penaliza pagina |
| **Hidden text/links** (cor de fundo, off-screen) | Spam Policies — penalizacao manual |
| **Cloaking** (servir HTML diferente para Googlebot) | Spam Policies — banimento |
| **Doorway pages** (paginas geradas para KW que redirecionam para destino unico) | Spam Policies — penalizacao |
| **Thin content** (200-300 palavras genericas) | Helpful Content — rebaixa site |
| **Scaled content abuse** (mar/2024) | Spam Policies — site-wide |
| **Exact-match anchor over-optimization** (90% dos backlinks com mesma anchor) | Penal Penguin — penalizacao manual |
| **Title clickbait + nao entrega** | Helpful Content — penaliza |
| **H1 multiplo / nenhum** | Acessibilidade + sinal confuso |
| **Duplicate content** sem canonical | Index dilution + cannibalization |
| **FAQ schema com Q&A invisivel ao usuario** | Spam policies — schema deve refletir conteudo visivel |
| **Schema com dado inflado** (rating 5.0 falso) | Manual action — schema spam |

---

## 18. Auditoria on-page — checklist

```
AUDITORIA ON-PAGE — CHECKLIST
===============================

CABECALHO
[ ] Title <= 60 chars, com keyword principal, beneficio, branded suffix
[ ] Meta description 150-160 chars, com call-to-pitch
[ ] Canonical autorreferencial OU para variacao correta
[ ] Robots meta: index, follow (a menos que intencional)
[ ] hreflang (se internacional) bidirecional
[ ] OG (og:title, og:description, og:image 1200x630, og:url, og:type)
[ ] Twitter Card (summary_large_image)
[ ] JSON-LD: Article + Person + Organization + BreadcrumbList (no minimo)
[ ] FAQPage schema (se ha FAQ visivel)
[ ] Validado em Schema Markup Validator + Rich Results Test
[ ] Preconnect/preload para recursos criticos

URL
[ ] Slug curto, descritivo, com keyword
[ ] Sem parametros desnecessarios
[ ] Lowercase, hifens, sem acento
[ ] Trailing slash consistente

H1
[ ] Unico
[ ] Espelha query principal
[ ] Concorda com title (sem mismatch)

ABOVE-THE-FOLD
[ ] H1 + sub-titulo
[ ] Autor + data publicacao + ultima atualizacao
[ ] Disclosure (se aplicavel)
[ ] TL;DR / resposta direta 40-60 palavras
[ ] Index/anchor links se conteudo longo

BODY
[ ] Hierarquia H2 -> H3 sem pular
[ ] H2 espelha sub-intents / PAA
[ ] Inverted pyramid (resposta antes de contexto)
[ ] Profundidade adequada ao intent
[ ] Originalidade (dado / experiencia / opiniao fundamentada)
[ ] Sem fluff
[ ] Imagens originais a cada 200-400 palavras
[ ] Tabelas/listas/callouts para escaneabilidade
[ ] Internal links contextuais (nao "leia mais")
[ ] External links para fontes primarias com rel apropriado

IMAGENS
[ ] Alt descritivo (5-15 palavras)
[ ] File name descritivo com hifens
[ ] AVIF ou WebP com fallback
[ ] width/height definidos
[ ] loading=lazy (exceto hero)
[ ] fetchpriority=high no hero
[ ] CDN com transformacoes
[ ] Schema ImageObject quando relevante

VIDEOS
[ ] Embed lazy
[ ] Thumbnail otimizada
[ ] Schema VideoObject com transcript
[ ] Captions

EEAT
[ ] Autor box com foto + credencial + link
[ ] Bio expandida no rodape do artigo
[ ] Reviewed by (em YMYL)
[ ] Fontes primarias inline
[ ] Disclosure (afiliado/patrocinado)
[ ] Editorial standards linkados no footer

CTA + RELACIONADOS
[ ] CTA alinhada ao intent
[ ] Conteudo relacionado (siblings de cluster)
[ ] Internal linking de saida adequado

PERFORMANCE (sumario — detalhe em seo-tecnico)
[ ] LCP <= 2.5s mobile (CrUX)
[ ] INP <= 200ms
[ ] CLS <= 0.1
[ ] Sem render-blocking acima do fold

ACESSIBILIDADE (WCAG 2.x)
[ ] Hierarquia H sem pular
[ ] Alt nao vazio em imagens com info
[ ] Contraste AA
[ ] Focus visivel
[ ] Forms com label
[ ] Aria onde HTML semantico nao chega
```

---

## 19. AI / LLM optimization — heuristicas para AI Overview e LLM-search

Em 2026, Google AI Overviews / Bing Copilot / Perplexity / ChatGPT search / Claude consultam web e citam fontes. Otimizacao on-page para citacao:

### 19.1 Estrutura

- **TL;DR no inicio** — resposta concentrada antes do contexto.
- **H/listas/tabelas/FAQ** — semantica HTML rica.
- **Frase declarativa** com fato verificavel.
- **Linguagem conversacional** alinhada a como usuarios perguntam em LLMs.

### 19.2 Schema

- `Article` + `Person` + `Organization` + `FAQPage` + `HowTo` quando aplicavel.
- `sameAs` em Person/Organization apontando para perfis autoritativos.
- `dateModified` recente.
- `inLanguage` correto.

### 19.3 EEAT visivel

- Autor real + credencial + foto.
- Fonte primaria linkada inline.
- Data e disclosure transparentes.

### 19.4 Cobertura de entidade

- Definicao + atributos + relacoes.
- Cluster topical extenso.
- Co-citacoes em fontes autoritativas.

### 19.5 Tracking de citacoes

| Ferramenta | Cobertura |
|------------|-----------|
| **Profound** | AI Overviews + ChatGPT + Perplexity + Copilot |
| **Authoritas** | SGE / AI Overviews |
| **BrightEdge Generative Parser** | Enterprise |
| **GSC > Search Appearance** | Em rollout — Google promete metrica de AI Overview |

---

## 20. Regras de Ouro

1. **NAO CHUTAR** — sem briefing de keyword + intent + URL alvo, esta skill nao executa. Pede a `seo-keywords` ou ao usuario.
2. **Title nao e nome do produto** — e pitch da pagina para o usuario na SERP.
3. **H1 unico** — semantica e acessibilidade.
4. **TL;DR no topo** — Featured Snippet + AI Overview oportunidade obvia.
5. **Schema valida** — Schema Markup Validator + Rich Results Test antes de publicar.
6. **Schema reflete o que esta na pagina** — schema spam (FAQ schema sem FAQ visivel) gera manual action.
7. **EEAT visivel + estruturado** — autor real, foto, credencial, sameAs em schema Person.
8. **Internal linking contextual** — anchor descritiva, distribuicao saudavel, hub-and-spoke.
9. **Imagens originais + otimizadas** — alt descritivo, AVIF/WebP, lazy, dimensoes definidas.
10. **OpenGraph + Twitter Cards** — sem isso, share em redes vira link feio.
11. **`dateModified` e atualizado de verdade** quando o conteudo muda — nao apenas para parecer fresh.
12. **Mobile-first** — auditar primeiro em 360px, depois desktop.
13. **Anti-pattern check** antes de publicar — keyword stuffing, hidden, doorway, thin, scaled.
14. **Page Experience cruzado** — CWV, HTTPS, sem intersticial intrusivo (detalhe em `seo-tecnico`).

---

## 21. Exemplos comportamentais — on-page

### Exemplo 1 — Cliente envia title cheio de keyword

**Input:** "Title sugerido: 'CRM CRM para Startup CRM Vendas Startup CRM Online Brasil 2026'. Ta bom?"

**Resposta esperada:**
> CORRIGE: "Keyword stuffing classico. Google reescreve em ~60% dos casos OU rebaixa por sinal de spam. Title funciona como pitch + intent confirmation, nao como deposito de KW. Reescrita: `CRM para Startup: 5 Opcoes Comparadas (Guia 2026)`. Cobre keyword principal `crm para startup`, oferece beneficio (`5 opcoes comparadas`), traz freshness (`2026`), tem branded suffix opcional (`| SPKR`). 56 chars, dentro do limite. Variacao alternativa: `Melhor CRM para Startup em 2026: Comparativo de 5 Opcoes` (intent comercial mais explicito). Antes de fechar, validar intent na SERP atual — se top 5 e dominado por listicles, manter formato listicle no title."

**Comportamento-chave:** rejeita stuffing, explica risco, oferece 2 alternativas testadas, exige confirmacao de intent na SERP antes de fechar.

### Exemplo 2 — FAQPage schema com perguntas invisiveis

**Input:** "Adicionei FAQPage schema com 20 perguntas para aparecer rich result, mas as perguntas nao estao no body da pagina (so no schema). Ta certo?"

**Resposta esperada:**
> CORRIGE: "Violacao de Spam Policies — `FAQ schema com Q&A nao visivel ao usuario` cai em **Marcacao de dados estruturados spammy**. Risco: manual action (Search Console > Acoes manuais > Marcacao spammy). Schema deve **refletir o conteudo visivel da pagina**, nao adicionar conteudo paralelo. Correcao: (a) escolher 5-8 perguntas que efetivamente estao na FAQ visivel da pagina e marcar so essas; (b) OU adicionar visualmente as 20 perguntas em um bloco FAQ no fim da pagina (acordeao OK, contanto que conteudo esteja no HTML inicial — nao por JS apenas). Importante: em 2023, Google reduziu visibilidade de FAQ rich result para sites comerciais; vale a pena? Validar com Rich Results Test se a pagina ainda e elegivel para rich result no nicho do cliente. Se nao for, manter FAQPage para sinal semantico (LLM/AI Overview ainda usa) mas sem expectativa de star rich result."

**Comportamento-chave:** identifica violacao especifica, cita politica oficial, oferece 2 caminhos de correcao, atualiza expectativa de rich result conforme realidade 2023+.

### Exemplo 3 — H1 generico em homepage

**Input:** "Homepage do cliente tem H1 = 'Bem-vindo ao [Marca]'. SEO OK?"

**Resposta esperada:**
> CORRIGE: "H1 generico desperdica o sinal mais importante de relevancia da pagina. `Bem-vindo` nao casa com nenhuma query, e `[Marca]` so ajuda em busca branded — onde o site ja vence por nome. Reescrita: posicionar pelo que o cliente OFERECE + para QUEM. Ex.: `Marketing Digital para Advogados B2B` (se for esse o foco). Frase curta, com keyword non-branded principal + persona. Se a homepage cobre multiplos servicos, escolher o de maior valor e usar H2 para os outros. Pratica adicional: title da home com mesmo formato + branded suffix; meta description com pitch em 1 linha. Validar em GSC apos 30 dias se queries non-branded comecam a trazer impressao."

**Comportamento-chave:** desconstroi `Bem-vindo`, oferece formula posicionamento + persona, alinha com title/meta, define KPI de validacao.

### Exemplo 4 — Pillar page sem internal linking

**Input:** "Publiquei a pillar `crm para startup` (3500 palavras) ha 2 meses. Nao rankeia. Por que?"

**Resposta esperada:**
> Diagnostico em camadas: "Ranking lento de pillar tem 5 hipoteses comuns. (1) **Internal linking insuficiente** — pillar precisa receber links de outras paginas do site (cluster spokes, homepage, blog index, navegacao). Verificar em Ahrefs > Internal Backlinks. Sem 5+ internal links, autoridade nao distribui. (2) **Cluster ausente** — pillar sem spokes parece pagina isolada para Google; topical authority nao se estabelece. Idealmente 5-8 spokes ja publicados linkando ao pillar. (3) **Indexacao** — confirmar em GSC > URL Inspection que esta `Indexada`. (4) **Intent mismatch** — buscar `crm para startup` em modo anonimo: top 10 e listicle, comparativo, ou guia? A pillar atende o formato dominante? (5) **Helpful Content** — pillar foi escrita para humano (com expertise direta, dado proprio, EEAT) ou para SEO (re-spinning de top 3)? (6) **Backlinks externos** — KD pode exigir 5-15 referring domains autoritativos para top 10. Sem backlink externo, dificilmente top 10 em KW competitiva. Plano: rodar checklist on-page (Secao 18), publicar 3 spokes em 4 semanas com internal linking ao pillar, confirmar indexacao, monitorar GSC > Performance da query por 60 dias."

**Comportamento-chave:** rejeita causa unica, lista 6 hipoteses estruturadas, da plano de validacao + acao em 60 dias.

---

## 22. Checklist de Contraditorio Interno — on-page

| # | Pergunta destruidora | O que busca |
|---|----------------------|-------------|
| 1 | Title casa com **intent dominante da SERP atual**, ou foi escrito a partir do briefing sem ver SERP? | Intent confirmation |
| 2 | Meta description tem **pitch real** com diferencial e CTA, ou e copia da primeira frase do body? | CTR optimization |
| 3 | URL e **curta, descritiva, com keyword**, sem parametros, sem profundidade excessiva? | URL hygiene |
| 4 | H1 e **unico**, espelha a query, **NAO duplica title** literalmente? | Heading hygiene |
| 5 | TL;DR / resposta direta esta nas **primeiras 60-80 palavras** do body, em formato de 40-60 palavras concisas? | Featured Snippet + AI Overview |
| 6 | Schema.org **valida** em Schema Markup Validator + Rich Results Test, e o conteudo do schema **espelha o conteudo visivel**? | Schema sem spam |
| 7 | EEAT esta **visivel ao usuario** (autor box, credencial, data, fonte) E **estruturado** (`Person` schema com `sameAs`)? | EEAT visivel + estruturado |
| 8 | Internal linking distribui autoridade do pillar para spokes (e vice-versa) com **anchor descritiva**, sem `leia mais`? | Internal linking saudavel |
| 9 | Imagens tem **alt descritivo**, AVIF/WebP, dimensoes definidas, lazy (exceto hero), e **schema ImageObject** quando relevante? | Image SEO + CWV |
| 10 | Pagina **NAO contem** keyword stuffing, hidden text, FAQ schema com Q&A invisivel, scaled content (mar/2024), ou clickbait que nao entrega? | Anti-spam |

---

## 23. Referencias canonicas

### 23.1 Oficiais Google

- **Google Search Central** — https://developers.google.com/search
- **Structured Data Guide** — https://developers.google.com/search/docs/appearance/structured-data
- **Rich Results gallery** — https://developers.google.com/search/docs/appearance/structured-data/article
- **Google Rich Results Test** — https://search.google.com/test/rich-results
- **Schema Markup Validator** — https://validator.schema.org
- **Special tags Google supports** — https://developers.google.com/search/docs/crawling-indexing/special-tags
- **Title best practices** — https://developers.google.com/search/docs/appearance/title-link
- **Meta description best practices** — https://developers.google.com/search/docs/appearance/snippet
- **URL best practices** — https://developers.google.com/search/docs/crawling-indexing/url-structure
- **Image SEO best practices** — https://developers.google.com/search/docs/appearance/google-images
- **Video best practices** — https://developers.google.com/search/docs/appearance/video
- **Spam Policies** — https://developers.google.com/search/docs/essentials/spam-policies

### 23.2 schema.org + padroes

- **schema.org** — https://schema.org
- **OpenGraph protocol** — https://ogp.me
- **X (Twitter) Cards** — https://developer.x.com/en/docs/twitter-for-websites/cards
- **WCAG 2.x** — https://www.w3.org/WAI/standards-guidelines/wcag

### 23.3 Web performance

- **web.dev — Structured data** — https://web.dev/articles/structured-data
- **web.dev — Image optimization** — https://web.dev/learn/images
- **web.dev — Vitals** — https://web.dev/articles/vitals

### 23.4 Bing

- **Bing Webmaster Guidelines** — https://www.bing.com/webmasters/help/webmasters-guidelines-30fba23a

### 23.5 Bibliografia profissional

- Aleyda Solis — SEO international, technical & on-page
- Jess Joyce — on-page audit
- Lily Ray — EEAT/YMYL
- Tom Capper (Moz) — on-page + ranking factors
- Kevin Indig — content + on-page
- Mark Williams-Cook — Google leak analysis
- Andrea Volpini (WordLift) — entity SEO + schema

### 23.6 Brasil

- **CONAR** — https://www.conar.org.br
- **CDC (Lei 8.078/1990)** — http://www.planalto.gov.br/ccivil_03/leis/l8078compilado.htm
- **LGPD (Lei 13.709/2018)** — http://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm

---

## 24. Referencia cruzada de skills

| Situacao | Skills relacionadas |
|----------|----------------------|
| Brief de pagina nova | `seo-fundamentos` + `seo-keywords` + `seo-on-page` + `copywriting-conversao` |
| Otimizacao de pagina existente | `seo-on-page` + `seo-keywords` (cannibalization, intent) + `seo-tecnico` |
| Pillar / cluster / hub-and-spoke | `seo-on-page` (anatomia) + `conteudo-evergreen` + `seo-keywords` |
| Schema markup | `seo-on-page` + `seo-tecnico` (validacao + render) |
| Featured Snippet roubo | `seo-on-page` (estrutura) + `seo-keywords` (KW alvo) |
| AI Overview / LLM citation | `seo-on-page` + `seo-fundamentos` (Secao 13/14) |
| EEAT visivel | `seo-on-page` + `comunicacao-corporativa` (autor) |
| Migracao de URL | `seo-on-page` (5.4) + `seo-tecnico` (redirects) |
| Local page | `seo-on-page` (16.7) + `seo-keywords` (local) |
| Product page | `seo-on-page` (16.6) + `copywriting-conversao` |
| Acessibilidade + on-page | `seo-on-page` + `acessibilidade-wcag` + `microcopy` |
| Disclosure afiliado/patrocinado | `seo-on-page` + `conhecimento-conar-cdc` |

---

## 25. Integracao com o ecossistema Frank-MKT

Esta skill integra-se ao agente principal `frank-mkt` (`agents/frank-mkt.md`) e ao restante do plugin da seguinte forma:

- **Pre-requisitos: `seo-fundamentos` + `seo-keywords`** — esta skill PRESSUPOE que o agente carregou esses dois antes. `seo-fundamentos` define modelo mental; `seo-keywords` entrega KW + intent + sub-queries + URL alvo. Sem isso, `seo-on-page` nao opera.
- **Acoplamento com `seo-tecnico`** — schema, render, CWV, redirects, hreflang sao dominio compartilhado. `seo-on-page` instrui o que colocar; `seo-tecnico` instrui como entregar tecnicamente (CSR/SSR, build, validation no CI/CD).
- **Acoplamento com `conteudo-evergreen`** — anatomia de pillar e cluster (Secao 16) sao o output que `conteudo-evergreen` operacionaliza em calendario editorial e atualizacao continua.
- **Acoplamento com `copywriting-conversao`** — body content, TL;DR, microcopy de CTA, headline (acima do fold) sao escritos por copywriter. `seo-on-page` define ESTRUTURA + slots; `copywriting-conversao` enche os slots com copy de alta conversao.
- **Acoplamento com `ux-heuristicas` + `microcopy` + `acessibilidade-wcag`** — hierarquia, focus, contraste, microcopy e parte tanto de UX quanto de SEO. Page Experience Signal cruza ambos.
- **Acoplamento com o agente `auditor`** — auditor roda regras PASS/FAIL na pagina (title valido, meta description, H1 unico, schema valida, EEAT visivel, anti-pattern check). Esta skill fornece o framework normativo + checklist (Secao 18).
- **Acoplamento com o agente `redator-hacker`** — copy estruturada para SEO + conversao + EEAT, sem dark pattern.
- **Acoplamento com o agente `seo-strategist`** — agente especialista em SEO orquestra outputs desta skill em planos por cliente.
- **Acoplamento com `comunicacao-corporativa`** — autor box, EEAT, editorial standards, politica de correcao sao tambem decisoes de comunicacao corporativa.
- **Acoplamento com `conhecimento-conar-cdc`** — disclosure de afiliado/patrocinado, claim publicitario, schema Product com preco e estoque atendem regulacao publicitaria + consumerista BR.
- **Acoplamento com `compliance-lgpd`** (plugin juridico) — captura de leads, cookies em forms, banners, consentimento — interface obrigatoria com plugin juridico para topicos LGPD.
- **Memoria e rastreabilidade** — briefings on-page, snippets de schema, checklists preenchidos sao persistidos em `.frank-mkt/seo/<cliente>/<data>/on-page/` pelo agente `suporte-documental` (a criar) ou diretamente pelo `frank-mkt`. Versionar para revisar evolucao temporal e impacto de core updates.
- **Contraditorio interno** — o agente principal aciona o modulo `contraditorio-interno` carregando o Checklist da Secao 22 desta skill antes de entregar pagina otimizada ou parecer on-page.
- **Decaimento temporal** — esta skill esta em volatility `medium` (6 meses). Re-grounding obrigatorio em fontes da Secao 23 antes de citar fato volatil (rich result types disponiveis, mudanca em comportamento de title/meta, novos tipos schema.org) em peca formal.
- **Regra de ouro para `frank-mkt`** — nenhuma pagina otimizada ou parecer on-page sai do plugin sem passar por esta skill; isso inclui briefings, checklists, schemas, anatomias, otimizacao de pagina existente, e roubo de Featured Snippet.

---

> **Aviso:** o plugin `frank-mkt` e um assistente de analise. Recomendacoes desta skill devem ser adaptadas a stack do site (CMS, render, framework, CDN), persona, autoridade do dominio e nicho, e validadas em Schema Markup Validator + Rich Results Test + GSC + ferramenta de crawl antes de publicar em peca formal. Schema.org evolui; Google adiciona/remove rich result types. Re-validar antes de citar.

---

*Plugin `frank-mkt` — skill `seo-on-page` (v0.1.0)*
*Ultima atualizacao: 2026-05-07*
