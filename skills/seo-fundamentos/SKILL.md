---
name: seo-fundamentos
description: "Skill-mae de SEO. Pipeline crawl/render/index/rank, intent de busca, SERP features, fatores de ranking, E-E-A-T, Helpful Content System, Spam Policies, Core Web Vitals, ferramentas oficiais, AI Overviews/SGE, frameworks (pillar-cluster, topical authority), KPIs, regulacao BR (CONAR/CDC/LGPD em SEO). Base para seo-keywords, seo-on-page, seo-tecnico, seo-link-building e conteudo-evergreen."
user-invocable: false
last_verified: 2026-05-07
next_review: 2026-11-07
volatility: medium
regrounding_sources:
  - "https://developers.google.com/search"
  - "https://developers.google.com/search/docs/essentials"
  - "https://developers.google.com/search/docs/fundamentals/seo-starter-guide"
  - "https://web.dev/articles/vitals"
  - "https://schema.org"
  - "https://www.bing.com/webmasters/help/webmasters-guidelines-30fba23a"
  - "https://blog.google/products/search/"
  - "https://search.google.com/search-console"
  - "https://services.google.com/fh/files/misc/hsw-sqrg.pdf"
  - "https://www.iab.com"
---

# Skill: seo-fundamentos

> **Decaimento Temporal**
> Ultima verificacao: 2026-05-07 | Proxima revisao: 2026-11-07 | Volatility: **medium** (6 meses)
> Google ajusta sistemas de ranking, EEAT e politicas de spam silenciosamente. Re-validar antes de publicar peca formal:
> - Google Search Central — https://developers.google.com/search
> - Google Search Essentials (antigo Webmaster Guidelines) — https://developers.google.com/search/docs/essentials
> - web.dev (Core Web Vitals) — https://web.dev/articles/vitals
> - Search Quality Rater Guidelines (PDF) — https://services.google.com/fh/files/misc/hsw-sqrg.pdf
> - Google Search Status Dashboard — https://status.search.google.com
> - Google Search Liaison (X/Twitter) — atualizacoes informais de updates
> - Bing Webmaster Guidelines — https://www.bing.com/webmasters/help/webmasters-guidelines-30fba23a
> - schema.org — https://schema.org
>
> **Acionamento:** SEO, busca organica, ranking, conteudo evergreen, auditoria SEO, EEAT, AI Overviews, SGE, pillar/cluster, autoridade, indexacao, Core Web Vitals.
> **Skills relacionadas:** `seo-keywords`, `seo-on-page`, `seo-tecnico`, `seo-link-building`, `conteudo-evergreen`, `copywriting-conversao`, `ux-heuristicas`, `conhecimento-search-console`, `conhecimento-ga4`, `conhecimento-conar-cdc`.

---

## 1. Visao Geral

SEO (Search Engine Optimization) e a disciplina de obter trafego organico qualificado de buscadores — Google, Bing, DuckDuckGo, Yandex, Baidu — e, crescentemente, de sistemas generativos (Google AI Overviews/SGE, Bing Copilot, Perplexity, ChatGPT search, Claude).

Esta skill e a **fundacao** das demais skills SEO do plugin `frank-mkt`. Sempre que o agente principal `frank-mkt` ativar o modo SEO, esta skill carrega antes das especialistas (`seo-keywords`, `seo-on-page`, `seo-tecnico`, `seo-link-building`, `conteudo-evergreen`).

### 1.1 Objetivos

- Estabelecer modelo mental compartilhado de **como buscadores realmente funcionam** (crawl, render, index, rank, serve).
- Padronizar **vocabulario tecnico** entre cliente, redator, SEO, dev, designer e analista de pesquisa.
- Definir **fatores de ranking** que o agente pode citar com seguranca e os que deve marcar como hipotese.
- Listar **ferramentas oficiais e profissionais** com finalidade especifica de cada uma.
- Padronizar **KPIs** que medem negocio, nao vaidade.
- Calibrar o impacto de **AI Overviews / SGE** no CTR organico (zero-click crescente).
- Garantir conformidade com **Google Spam Policies** (escalado, abuso de dominio expirado, abuso de reputacao de site) — risco de penalizacao manual ou algoritmica.
- Garantir conformidade com regulacao BR — **CONAR**, **CDC**, **LGPD** em conteudo SEO local.

### 1.2 Quando o agente aciona esta skill

| Gatilho | Exemplo de input do usuario |
|---------|------------------------------|
| Briefing de conteudo organico | "preciso de um plano de conteudo para o blog do cliente X" |
| Auditoria de site | "o site dropou no Google nas ultimas 4 semanas" |
| Decisao tecnica de stack | "vamos sair de WordPress para Next.js — vai afetar SEO?" |
| Resposta a update de algoritmo | "saiu um core update — o que fazer?" |
| Calculo de ROI de SEO | "vale a pena investir em SEO se AI Overviews esta tomando trafego?" |
| Concorrencia organica | "o concorrente nos passou no SERP da keyword principal" |

### 1.3 Pre-requisitos

Antes de aplicar esta skill em peca formal, validar:

- [ ] Acesso ao **Google Search Console** (GSC) do dominio em analise.
- [ ] Acesso ao **Google Analytics 4** (GA4) com eventos e conversoes configurados.
- [ ] Acesso a **uma ferramenta de backlink/keywords** (Ahrefs, Semrush, Sistrix, Mangools).
- [ ] Acesso a **crawler** (Screaming Frog, Sitebulb, Ryte, ou GSC Cobertura).
- [ ] Conhecimento minimo da **stack do site** (CMS, render — CSR/SSR/SSG/ISR — CDN, framework).
- [ ] Politica de Privacidade e LGPD em ordem (formulario de captura, cookies, consentimento) — ver `compliance-lgpd` no plugin juridico ou adapt cao em `conhecimento-conar-cdc`.

> **Cristal C0 — NAO CHUTAR.** Sem acesso aos dados (GSC, GA4, ferramenta de backlink), o agente NAO inventa volume, posicao, CTR, dificuldade ou autoridade. Pede acesso ou trabalha com hipotese explicita.

---

## 2. Como o Google realmente funciona — pipeline em 5 fases

```
DESCOBERTA -> CRAWL -> RENDER -> INDEX -> RANK -> SERVE
   (links,    (HTTP    (JS exec  (parse  (algos) (SERP)
   sitemaps,  GET por  no Web    + score
   feeds)     Googlebot)Renderer) por sinais)
```

### 2.1 Descoberta

O Google descobre URLs por **3 vias principais**:

| Via | Detalhe | Ferramenta de controle |
|-----|---------|------------------------|
| **Links internos e externos** | Followed links em paginas ja conhecidas | Internal linking + backlinks |
| **Sitemaps XML** | Submetidos via GSC ou referenciados em `robots.txt` | `sitemap.xml`, `sitemap-index.xml` |
| **Submissao manual** | URL Inspection -> "Solicitar indexacao" no GSC | Google Search Console |

URL descoberta ainda **nao significa rastreada**. Pode ficar em fila de crawl por dias/semanas.

### 2.2 Crawl

Googlebot busca a URL via HTTP GET. Pontos criticos:

| Aspecto | Detalhe |
|---------|---------|
| **User-agents** | `Googlebot Smartphone` (default — mobile-first), `Googlebot Desktop`, `Googlebot Image`, `Googlebot Video`, `Googlebot News`, `AdsBot-Google`, `Mediapartners-Google` |
| **`robots.txt`** | RFC 9309 (2022). Diretivas `Disallow`/`Allow` aplicam-se ao path. Nao impede indexacao por links externos — pra isso usar `noindex` |
| **Crawl budget** | Quantidade de URLs que Googlebot rastreia por sessao. Importante em sites grandes (>100k URLs). Monitorar em GSC -> Estatisticas de rastreamento |
| **Rate limit** | Google ajusta automaticamente. Servidor lento -> menos crawl |
| **Renderable HTTP codes** | 200 OK (rastreia + indexa); 301/302 (segue redirect); 404/410 (drop); 5xx (retry e queda de prioridade); 429 (rate limit) |
| **Cabecalhos importantes** | `X-Robots-Tag`, `Last-Modified`, `ETag`, `Cache-Control` |

### 2.3 Render

Googlebot usa o **Web Rendering Service (WRS)**, baseado em Chromium evergreen (versao recente do Chrome). Executa JS, CSS, imagens.

| Aspecto | Detalhe |
|---------|---------|
| **Render budget** | Render e caro (CPU/memoria). Sites pesados em JS podem ter atraso de render |
| **CSR (Client-Side Rendering)** | SPA puro. Risco: conteudo so aparece apos JS executar — Googlebot pode esperar, mas nem sempre |
| **SSR (Server-Side Rendering)** | HTML completo no GET. Recomendado para SEO |
| **SSG (Static Site Generation)** | HTML pre-renderizado em build. Excelente para SEO + performance |
| **ISR (Incremental Static Regeneration)** | Hibrido (Next.js, Astro). Bom equilibrio |
| **Dynamic Rendering** | Anteriormente recomendado pelo Google, hoje **descontinuado/desencorajado**. Preferir SSR ou hibrido |
| **Hydration** | Cuidado: conteudo principal NAO deve depender de hydration para aparecer |

> **Frase-chave:** "Se o conteudo nao esta no HTML (SSR) ou esta apos um JS pesado (CSR), o Google pode nao ler — e mesmo lendo, vai rankear pior do que paginas que entregam HTML pronto."

### 2.4 Index

Apos render, o conteudo e parseado e armazenado no **indice** com sinais associados.

| Sinal armazenado | Exemplo |
|------------------|---------|
| Texto principal | Body, H1-H6, paragrafos |
| Estrutura | Schema.org / JSON-LD, microdata, RDFa |
| Metadados | `<title>`, `<meta description>`, OpenGraph, Twitter Cards |
| Imagens/videos | Alt text, captions, transcriptions |
| Links | Internos e externos (anchor, contexto) |
| Tecnico | Canonical, hreflang, mobile-friendly, HTTPS, CWV |
| Comportamental (em parte) | Sinais derivados de SERP (CTR, dwell, pogo-stick) — controverso |

**Estados de indexacao no GSC:**

| Estado | Significado | Acao |
|--------|-------------|------|
| **Indexada** | URL no indice e elegivel a aparecer | OK |
| **Rastreada — atualmente nao indexada** | Google viu mas nao achou util | Revisar conteudo, EEAT, helpful content |
| **Detectada — atualmente nao indexada** | Google viu o link, ainda nao rastreou | Crawl budget; aumentar autoridade interna |
| **Excluida por tag noindex** | Tag `<meta name="robots" content="noindex">` ou `X-Robots-Tag: noindex` | Intencional? Confirmar |
| **Erro de canonical alternativo** | Google escolheu canonical diferente do declarado | Revisar `<link rel="canonical">` |
| **Pagina alternativa com tag canonica adequada** | Duplicata legitima | OK |
| **Bloqueada por robots.txt** | `Disallow` impede crawl | Intencional? Confirmar |
| **Erro 404 (nao encontrado)** | URL retorna 404 | Corrigir ou aceitar |

### 2.5 Rank

Para uma query, Google seleciona ~milhares de candidatos do indice e os **rankeia** com multiplos sistemas em paralelo. Ver Secao 5.

### 2.6 Serve (SERP)

Resultado final apresentado ao usuario na **Search Engine Results Page (SERP)**. Ver Secao 4.

---

## 3. Intent de busca — taxonomia e matriz

Identificar o **intent** correto e a decisao mais alta no funil de SEO. Conteudo com intent errado nao rankeia, mesmo bem otimizado.

### 3.1 Os 4 tipos classicos (Andrei Broder, 2002 — atualizado)

| # | Intent | Pergunta do usuario | Tipo de SERP | Exemplo |
|---|--------|---------------------|--------------|---------|
| 1 | **Informacional (know)** | "o que e", "como", "por que" | Artigos, listas, AI Overview, People Also Ask | "o que e core web vitals" |
| 2 | **Navegacional (go)** | "quero chegar a um site/pagina especifica" | Sitelinks, knowledge panel | "linkedin login", "ahrefs blog" |
| 3 | **Investigacao comercial (compare/learn-to-buy)** | "melhor", "vs", "review" | Listas, tabelas comparativas, reviews | "melhor crm para startup", "ahrefs vs semrush" |
| 4 | **Transacional (do/buy)** | "comprar", "preco", "perto de mim" | Shopping, ads, mapas, listings | "comprar curso de seo", "pizzaria perto de mim" |

### 3.2 Subtipos uteis (Bing IntentRank, Search Engine Land)

- **Local** — "perto de mim", cidade explicita.
- **Visual** — query que pede imagem (ex.: "infografico funil de vendas").
- **News** — query com tendencia recente.
- **Como-fazer** — passo a passo.
- **Definicao** — palavra unica + intencao "what is".

### 3.3 Como inferir intent a partir da SERP (metodo de 3 passos)

1. **Buscar a keyword** em modo anonimo + localizacao alvo.
2. **Observar formato dominante** das 10 primeiras posicoes:
   - Maioria de tutoriais? -> Informacional how-to.
   - Maioria de listas? -> Comercial / informacional comparativo.
   - Lojas / e-commerce? -> Transacional.
   - Misto -> intent dividido (ambivalente — risco mais alto).
3. **Observar SERP features** ativas:
   - AI Overview presente -> Google entende como informacional.
   - Shopping / Ads dominantes -> Transacional.
   - Knowledge Panel -> Navegacional / entidade.
   - People Also Ask + Featured Snippet -> Informacional FAQ.
   - Local Pack -> Local.

> **Regra de ouro de intent:** o conteudo deve **espelhar** o formato dominante da SERP. Tentar empurrar formato divergente (ex.: blog post longo numa SERP de e-commerce) raramente funciona.

### 3.4 Matriz keyword x estagio do funil

| Estagio | Intent dominante | Tipo de keyword | Exemplo (CRM) |
|---------|------------------|-----------------|----------------|
| **Topo (TOFU)** | Informacional | Educativa, ampla | "o que e CRM" |
| **Meio (MOFU)** | Investigacao comercial | Comparativa, lista | "melhor CRM para vendas B2B" |
| **Fundo (BOFU)** | Transacional | Marca + modificador comercial | "Salesforce preco", "Pipedrive desconto" |
| **Pos-venda** | Informacional/Navegacional | Suporte, troubleshooting | "como integrar Pipedrive com WhatsApp" |

---

## 4. SERP — anatomia e features

Em 2026, a SERP do Google **nao e mais 10 links azuis**. Cada query pode mostrar 10+ tipos de feature competindo pelo espaco visivel.

### 4.1 Componentes principais

| Feature | Descricao | Como aparecer |
|---------|-----------|---------------|
| **AI Overview / SGE** | Resposta gerada por IA no topo, com fontes citadas | Conteudo bem-estruturado, fonte autoritativa, EEAT alto, schema.org |
| **Featured Snippet** ("posicao zero") | Trecho de pagina extraido como resposta direta | Resposta concisa, formatada (lista, tabela, paragrafo curto) que responda a query |
| **People Also Ask (PAA)** | Caixa de perguntas relacionadas | Cobrir variantes da query no conteudo, FAQ schema |
| **Knowledge Panel** | Card lateral com info de entidade | Reconhecimento como entidade (Wikipedia, Wikidata, schema Organization/Person) |
| **Sitelinks** | Links secundarios sob o resultado | Estrutura de site clara, autoridade, navegacao logica |
| **Top Stories** | Carrossel de noticias | Publisher reconhecido, schema NewsArticle, freshness |
| **Image Pack** | Linha de imagens | Imagens otimizadas (alt, file name, contexto, schema ImageObject) |
| **Video carousel** | Carrossel de videos (YouTube domina) | Schema VideoObject, transcript, thumbnail |
| **Shopping** | Produtos com foto/preco/loja | Merchant Center, schema Product, feed |
| **Local Pack (Maps)** | 3 negocios locais + mapa | Google Business Profile (antigo GMB), reviews, NAP consistente |
| **Reviews** | Avaliacoes em estrelas | Schema Review/AggregateRating |
| **Discussions and forums** | Reddit, Quora, comunidades | Participacao autentica em foruns + autoridade do dominio |
| **HowTo / Recipe / Event** | Cards estruturados | Schema correspondente |
| **Site Filters / Things to know** | Refinamentos da query | Estrutura semantica forte do site |

### 4.2 Zero-click — o problema do CTR decrescente

| Periodo | Zero-click rate (estimativa de mercado) |
|---------|------------------------------------------|
| 2019 | ~50% das buscas no Google |
| 2022 | ~57% |
| 2024 | ~60% (com a chegada de SGE) |
| 2026 | Tendencia de alta com AI Overview default em mais paises (re-validar — ver fontes do frontmatter) |

**Implicacao estrategica:** um trafego em queda pode nao significar perda de relevancia — pode ser AI Overview respondendo no SERP. Medir **share of impressions**, **share of voice na entidade**, **citacoes em AI Overviews** (ferramentas terceiras), nao so cliques.

### 4.3 Personalizacao da SERP

Fatores que mudam a SERP que **voce ve** vs a que o **cliente ve**:

- Localizacao (IP, GPS).
- Historico de busca pessoal.
- Idioma do navegador / sistema.
- Dispositivo (mobile vs desktop).
- Login no Google.
- Configuracao de SafeSearch.

> **Pratica obrigatoria do agente:** sempre auditar SERP em **modo anonimo + localizacao do publico-alvo**, nao na propria sessao logada.

---

## 5. Fatores de ranking — sistemas conhecidos do Google

### 5.1 Sistemas de ranking documentados pelo Google

Lista oficial mantida em https://developers.google.com/search/docs/appearance/ranking-systems-guide. Estado conhecido (validar em fonte oficial antes de citar):

| Sistema | Funcao | Tipo |
|---------|--------|------|
| **BERT** (2019) | Compreensao de contexto, processamento natural | Core |
| **MUM (Multitask Unified Model)** (2021) | Multimodal, multilingue, multi-tarefa | Core / specifico |
| **Neural Matching** | Conexao entre conceitos e queries | Core |
| **RankBrain** (2015) | ML para queries nunca vistas | Core |
| **Helpful Content System** (2022) | Penaliza conteudo nao-util feito para SEO | Site-wide (incorporado ao core em mar/2024) |
| **Reviews System** (antigo Product Reviews) | Eleva reviews aprofundadas | Sitewide / pagina |
| **Spam Detection (SpamBrain)** | Detecta spam algoritmicamente | Core |
| **Page Experience Signal** | UX (CWV, HTTPS, sem intersticiais) | Core |
| **Original Content System** | Eleva conteudo original | Core |
| **Topic Authority System** (news) | Autoridade em topicos para news | News |
| **Crisis Information System** | Informacao em crises (saude, desastre) | Specifico |
| **Removal-Based Demotion (DMCA)** | Rebaixa sites com muitas remocoes | Punitivo |
| **Exact Match Domain (EMD)** | Limita boost de dominio igual a keyword | Negativo |
| **Site Diversity** | Limita resultados do mesmo dominio na pagina 1 | Diversidade |

### 5.2 Categorias de fatores (modelo simplificado)

| Categoria | Exemplos |
|-----------|----------|
| **Relevancia** | Match semantico, palavras-chave, schema, anchor text |
| **Qualidade do conteudo** | Helpful Content, EEAT, originalidade, profundidade |
| **Autoridade do dominio** | Backlinks, mencoes, idade do dominio, sinais de marca |
| **Experiencia do usuario** | CWV, HTTPS, mobile, intersticiais, layout |
| **Contexto da query** | Localizacao, idioma, intent, freshness |
| **Sinais comportamentais** | (controverso) CTR, dwell time, pogo-sticking |

### 5.3 Fatores **NAO** confirmados

Lista popular de "200+ fatores de ranking" (Backlinko, Brian Dean) — **nao e oficial**. Tratar como hipotese, nao como fato. O agente cita com ressalva: "fator atribuido a SEO comunitario, nao confirmado pelo Google".

> **Atualizacao 2024 — vazamento de docs do Google API.** Em mai/2024, vazou documentacao interna do Content Warehouse API com ~14.000 atributos. Confirmou existencia de sinais como `siteAuthority`, `clickRadius50Percent`, `navboost`, hostAge, mas Google declarou que **estar no API nao significa ser usado em ranking de producao**. Tratar como informacao secundaria, nao oficial.

### 5.4 Core Updates

Atualizacoes amplas do nucleo do algoritmo. Frequencia: 2-4 por ano. Impacto: pode redistribuir trafego de forma significativa.

| Acao | Detalhe |
|------|---------|
| **Monitorar** | Google Search Status Dashboard, comunicado oficial no @searchliaison |
| **Diagnostico apos queda** | Antes do update, foco em conteudo de baixa utilidade, EEAT, paginas finas, escala industrial de conteudo |
| **Recovery** | Tipicamente 6-12 meses ou ate proximo update — nao e instantaneo |
| **Falacia comum** | Atribuir queda imediatamente ao update sem cross-checar GSC, GA4, search.google.com/search-console/coverage e calendario do update |

---

## 6. E-E-A-T — Experience, Expertise, Authoritativeness, Trustworthiness

E-E-A-T e um **conceito** das Search Quality Rater Guidelines (SQRG). Nao e fator de ranking direto, mas Google **treina sistemas** para identificar sinais de EEAT.

### 6.1 Os 4 pilares

| Pilar | Pergunta-chave | Como demonstrar |
|-------|----------------|-----------------|
| **Experience** (adicionado em dez/2022) | A pessoa **viveu** o assunto? | Foto real, video, "eu fui", "eu testei", screenshots originais, datas de uso, prova de propriedade |
| **Expertise** | A pessoa tem **competencia** tecnica? | Credenciais (CRM, OAB, CRC, doutorado), certificacoes, anos de experiencia, publicacoes |
| **Authoritativeness** | A pessoa/site e **referencia reconhecida**? | Citacoes em sites autoritativos, mencoes, premios, reviews |
| **Trustworthiness** (o pilar central) | E **confiavel**? | HTTPS, politica clara, autor real e contactavel, fontes citadas, transparencia editorial, sem manipulacao |

### 6.2 YMYL — Your Money or Your Life

Topicos YMYL (saude, financas, legal, seguranca, eleicoes, futuro do leitor) exigem **EEAT mais alto**. Sites sem credenciais demonstraveis tipicamente nao rankeiam em YMYL.

| Subcategoria YMYL | Exemplo |
|-------------------|---------|
| **Saude e seguranca** | Sintomas, tratamentos, dietas, mental health, drogas, suicidio |
| **Estabilidade financeira** | Investimentos, emprestimos, impostos, seguros, aposentadoria |
| **Sociedade** | Conselho legal, eleicoes, noticias |
| **Outras** | Custodia infantil, adocao, decisoes de vida importantes |

### 6.3 Sinais praticos de EEAT no site

- [ ] **Pagina "Sobre"** detalhada com historia, missao, time, contato.
- [ ] **Bio do autor** em cada artigo, com foto real, credenciais, link para perfil profissional (LinkedIn, ORCID, Lattes).
- [ ] **Schema.org Author + Person + Organization** marcado.
- [ ] **Editorial standards / disclosure**: como o conteudo e produzido, revisado, atualizado.
- [ ] **Disclosure de conflito de interesse** (afiliados, patrocinio).
- [ ] **Data de publicacao + ultima atualizacao** visiveis e marcadas em schema (`datePublished`, `dateModified`).
- [ ] **Fontes primarias** linkadas no texto (papers, normas, dados originais).
- [ ] **Politica de correcao** publica.
- [ ] **HTTPS** + politica de privacidade + termos de uso.
- [ ] **Mencoes externas** em sites autoritativos do nicho.
- [ ] **Reviews / avaliacoes** verificaveis (Google Business, Trustpilot, Reclame Aqui).

### 6.4 Search Quality Rater Guidelines (SQRG)

PDF publico, ~170 paginas. Define como avaliadores humanos pontuam paginas de exemplo. **NAO** e usado em producao para ranking direto, mas serve de **guia de design** para o que Google considera qualidade.

URL: https://services.google.com/fh/files/misc/hsw-sqrg.pdf (re-validar versao na pagina principal de SearchCentral).

---

## 7. Helpful Content System (HCS)

Lancado em ago/2022 como sistema separado. **Incorporado ao core algorithm em mar/2024** — agora roda continuamente, nao em "updates" pontuais.

### 7.1 Self-assessment do Google (lista oficial)

Conteudo util, segundo o Google, atende perguntas como:

| Pergunta | O que verificar |
|----------|------------------|
| Voce tem **publico-alvo** existente que veria essa pagina como util? | Audiencia real, nao apenas SEO |
| O conteudo demonstra **expertise direto** e profundidade do assunto? | EEAT |
| O site tem **foco principal** claro? | Topical authority |
| Apos ler, a pessoa **resolve seu problema** (info ou tarefa)? | Outcome-oriented |
| A pessoa sentiria que teve uma **experiencia satisfatoria**? | UX completa |
| O conteudo segue as **diretrizes de core update** e helpful content? | Validar com SQRG |

### 7.2 Sinais que HCS penaliza

- Conteudo escrito **principalmente para ranking** (keyword stuffed, generico).
- Conteudo **escalado** sem expertise (ex.: 10.000 paginas geradas em massa, mesmo nao por IA).
- Conteudo que **nao adiciona valor** alem do que ja existe.
- Conteudo que **promete sem entregar** (clickbait).
- Conteudo **fora do foco** principal do site (ex.: blog de TI publicando sobre receitas).
- **AI content sem revisao humana e EEAT** — Google nao penaliza IA per se, mas penaliza conteudo nao-util independente de origem.

### 7.3 HCS e penalizacao site-wide

Diferente de penalizacao por pagina, HCS pode rebaixar **o site inteiro**. Recovery exige:

1. **Auditoria completa** do conteudo: quanto e helpful, quanto e thin/scaled.
2. **Decisao**: melhorar, consolidar (canonicalizar/301) ou **deletar** (404/410).
3. **Espera** — Google reavalia ao longo de meses. Sem botao de "tentar de novo".

> **Frase-chave:** "Em HCS, conteudo medioco arrasta conteudo bom. Cortar mais e tipicamente melhor que tentar resgatar tudo."

---

## 8. Spam Policies — Google Search Essentials

Lista oficial em https://developers.google.com/search/docs/essentials/spam-policies.

### 8.1 Categorias de spam (selecao critica)

| Pratica | Descricao | Risco |
|---------|-----------|-------|
| **Cloaking** | Mostrar conteudo diferente para Googlebot e usuario | Banimento |
| **Doorway pages** | Paginas geradas para palavras-chave que redirecionam para destino unico | Penalizacao |
| **Hidden text/links** | Texto/link invisivel para usuario mas legivel ao bot | Penalizacao |
| **Keyword stuffing** | Repeticao excessiva de palavra-chave | Penalizacao |
| **Link spam** | PBN, troca reciproca artificial, links pagos, comentarios em massa | Penalizacao manual / algoritmica |
| **Machine-generated traffic** | Bots simulando acessos | Banimento |
| **Malware / harmful behavior** | Codigo malicioso, phishing | Banimento |
| **Misleading functionality** | Promete X, entrega Y | Penalizacao |
| **Scraped content** | Reproducao sem valor agregado | Penalizacao |
| **Sneaky redirects** | Redirect baseado em referer/dispositivo | Penalizacao |
| **Thin affiliate** | Conteudo afiliado sem valor agregado | Penalizacao |
| **User-generated spam** | Spam em comentarios, foruns nao-moderados | Penalizacao |

### 8.2 Atualizacao mar/2024 — 3 novas categorias

| Categoria | Descricao | Exemplo |
|-----------|-----------|---------|
| **Scaled content abuse** | Producao em massa (humana, IA ou hibrida) com proposito de manipular ranking | 10.000 artigos finos gerados em 2 semanas |
| **Site reputation abuse** ("parasite SEO") | Publicar conteudo de terceiros (afiliado, patrocinado) em dominio de autoridade alheia para se beneficiar do ranking do dominio | "Best of" pages em sites de noticias com link de afiliado |
| **Expired domain abuse** | Comprar dominio expirado e usar a autoridade residual com conteudo nao-relacionado | Ex-blog de medicina virou casino |

### 8.3 Acoes manuais

GSC > Seguranca e acoes manuais > Acoes manuais. Tipos:
- Conteudo improprio (spam puro).
- User-generated spam.
- Spam estruturado.
- Cloaking + redirects sneaky.
- Hacked content.
- Thin content.
- Marcacao de dados estruturados spammy.
- Links de saida nao-naturais.
- Links recebidos nao-naturais.

Para reverter: **Reconsideration Request** com plano de remediacao detalhado. Resposta tipica: dias a semanas.

---

## 9. Core Web Vitals (CWV) — UX tecnico mensuravel

Page Experience Signal usa CWV como um dos componentes (junto com HTTPS, mobile-friendly, sem intersticiais intrusivos).

### 9.1 As 3 metricas oficiais (a partir de mar/2024)

| Metrica | O que mede | Bom | Precisa melhorar | Ruim |
|---------|------------|-----|------------------|------|
| **LCP — Largest Contentful Paint** | Tempo ate o maior elemento visivel | <= 2.5s | <= 4.0s | > 4.0s |
| **INP — Interaction to Next Paint** (substituiu FID em mar/2024) | Latencia de interacao -> proxima atualizacao visual | <= 200ms | <= 500ms | > 500ms |
| **CLS — Cumulative Layout Shift** | Estabilidade visual (deslocamento) | <= 0.1 | <= 0.25 | > 0.25 |

> Re-validar thresholds em https://web.dev/articles/vitals — Google ajusta periodicamente.

### 9.2 Lab vs Field

| Tipo | Como medir | Uso |
|------|------------|-----|
| **Lab** | Lighthouse, PageSpeed Insights (lab tab), DevTools | Diagnostico, debug, dev local |
| **Field (CrUX)** | Chrome User Experience Report — dados reais agregados | Decisao de ranking — Google usa Field, nao Lab |

CrUX disponivel em PageSpeed Insights, GSC > Core Web Vitals, BigQuery (CrUX history dataset).

### 9.3 Otimizacoes mais comuns

| Metrica | Otimizacao tipica |
|---------|-------------------|
| **LCP** | Imagem hero priorizada (`fetchpriority="high"`), `preload`, AVIF/WebP, CDN, server-side render do hero, eliminar render-blocking JS/CSS |
| **INP** | Reduzir JS de terceiros, code splitting, `requestIdleCallback`, evitar long tasks (>50ms), debounce de handlers, mover trabalho para Web Workers |
| **CLS** | `width`/`height` em imagens, `aspect-ratio` em containers, reservar espaco para ads/embeds, evitar fontes que mudam metrica (`font-display: swap` com cuidado), CSS estavel |

### 9.4 Outras metricas relevantes (nao-CWV mas correlatas)

- **TTFB** (Time to First Byte) — qualidade de servidor/CDN.
- **FCP** (First Contentful Paint) — primeiro pixel renderizado.
- **TBT** (Total Blocking Time) — proxy de INP em lab.
- **Speed Index** — velocidade percebida.

---

## 10. Metricas e KPIs — negocio vs vaidade

### 10.1 Metricas operacionais (GSC + GA4)

| Metrica | Fonte | Uso |
|---------|-------|-----|
| **Impressoes** | GSC | Quanto fui mostrado |
| **Cliques** | GSC | Quanto fui escolhido |
| **CTR** | GSC | Atratividade do snippet |
| **Posicao media** | GSC | Onde estou — ressalva: media ponderada, pode esconder cauda |
| **Paginas indexadas** | GSC > Cobertura | Saude tecnica |
| **Erros de cobertura** | GSC > Cobertura | Bloqueios, 404, redirects |
| **Backlinks** | GSC > Links externos + Ahrefs/Semrush | Autoridade |
| **Referring domains** | Ahrefs/Semrush | Diversidade de autoridade |
| **Sessions / Users** | GA4 | Trafego efetivo |
| **Engaged sessions** | GA4 | Qualidade do trafego |
| **Conversoes** | GA4 | Acao de negocio |
| **Receita assistida** | GA4 + atribuicao | Contribuicao em multi-touch |

### 10.2 KPIs estrategicos

| KPI | Definicao | Como calcular |
|-----|-----------|---------------|
| **Share of Voice (SoV)** | % de impressoes do meu dominio sobre total da minha lista de keywords vs concorrencia | Ahrefs / Semrush track de keyword set |
| **Trafego organico nao-marca** | Trafego de queries que nao contem o nome da marca | GSC > Filtros por query (excluir marca) |
| **Topical Authority** | Cobertura de um topico (% de subtopicos cobertos vs concorrencia) | Topic cluster analysis |
| **Conversion Rate organico** | Conversoes / sessoes organicas | GA4 (canal organic search) |
| **Custo por aquisicao organica** | Custo total de SEO / conversoes | Financeiro + GA4 |
| **ROI organico** | (Receita organica - custo) / custo | Financeiro + GA4 |
| **Citacoes em AI Overviews** | Quantidade de aparicoes em AI Overviews | Ferramentas terceiras (BrightEdge, Authoritas, Profound) |

### 10.3 Vaidade vs valor

| Metrica de vaidade | Por que e vaidade | Substituir por |
|--------------------|-------------------|-----------------|
| Ranking #1 numa keyword | Pode ser keyword sem volume, sem conversao, ou em SERP zero-click | Cliques + conversoes |
| Volume de impressoes | Sem cliques nao gera negocio | CTR + cliques |
| Quantidade de backlinks | Qualidade > quantidade; um link autoritativo vale 100 lixos | Referring domains autoritativos + DR |
| DA / DR genericos | Indices proprietarios, sem oficialidade | Trafego organico estimado + crescimento de domains |
| Posts publicados / mes | Volume nao e qualidade | Posts indexados, com trafego, com conversao |

---

## 11. Ferramentas — oficiais e profissionais

### 11.1 Oficiais Google

| Ferramenta | URL | Uso |
|------------|-----|-----|
| **Google Search Console** | search.google.com/search-console | Cobertura, queries, sitemap, links, CWV, manual actions |
| **Google Analytics 4** | analytics.google.com | Comportamento, conversao, funil |
| **Google Trends** | trends.google.com | Tendencia de busca, sazonalidade |
| **PageSpeed Insights** | pagespeed.web.dev | CWV lab + field |
| **Lighthouse** | DevTools / npm | Auditoria completa (perf, SEO, a11y, best practices) |
| **Rich Results Test** | search.google.com/test/rich-results | Testa schema |
| **URL Inspection (no GSC)** | GSC | Estado atual da URL no indice |
| **Google Business Profile** | business.google.com | SEO local |
| **Mobile-Friendly Test** | Descontinuado em 2023 — usar Lighthouse + GSC |

### 11.2 Bing / Microsoft

| Ferramenta | Uso |
|------------|-----|
| **Bing Webmaster Tools** | Equivalente do GSC para Bing/Copilot |
| **Bing Keyword Research** | Sugestoes Bing |

### 11.3 Crawlers profissionais

| Ferramenta | Forte em |
|------------|----------|
| **Screaming Frog SEO Spider** | Crawler desktop, completo, padrao da industria |
| **Sitebulb** | Visualizacao + insights, bom para report |
| **Ryte** | Crawl + monitoring continuo |
| **OnCrawl** | Log analysis + crawl, enterprise |
| **DeepCrawl / Lumar** | Enterprise, agendamento |

### 11.4 Plataformas all-in-one

| Plataforma | Forte em | Notas |
|------------|----------|-------|
| **Ahrefs** | Backlinks, keyword research, content gap | Index de backlinks dos maiores |
| **Semrush** | Keyword research, posicao tracking, ads | Suite ampla |
| **Sistrix** | Visibilidade DACH/EU, IndexWatch | Forte na Alemanha |
| **Moz Pro** | DA, On-Page Grader, link explorer | Pioneiro |
| **Mangools** | KWFinder, SERPChecker — bom para small biz | Custo-beneficio |
| **SE Ranking** | Tracking + audit, custo intermediario | Bom para freelancer |
| **Serpstat** | Keyword research, PPC, audit | Custo competitivo |

### 11.5 Conteudo / On-page

| Ferramenta | Uso |
|------------|-----|
| **SurferSEO** | Brief + SERP analysis para on-page |
| **Frase** | AI-assisted brief |
| **Clearscope** | Topical relevance score |
| **MarketMuse** | Topical authority + content planning |
| **Ahrefs Content Explorer** | Topicos com performance |

### 11.6 Schema / Structured Data

| Ferramenta | Uso |
|------------|-----|
| **Schema Markup Validator** (validator.schema.org) | Valida qualquer schema |
| **Google Rich Results Test** | Testa apenas schemas que Google suporta como rich result |
| **Schema App / WordLift** | Geradores de schema enterprise |

### 11.7 AI Overview / SGE tracking

| Ferramenta | Uso |
|------------|-----|
| **Profound** | Citacoes em AI Overviews + ChatGPT/Perplexity |
| **Authoritas** | Tracking de SGE |
| **BrightEdge Generative Parser** | Enterprise — tracking de SGE |
| **AlsoAsked / AnswerThePublic** | PAA + question mining |

---

## 12. Frameworks e metodologias

### 12.1 Pillar Page + Topic Cluster (HubSpot, 2017)

```
                      [PILAR — guia completo de SEO]
                       /        |         |         \
            [cluster:        [cluster:  [cluster:    [cluster:
             keywords]       on-page]   tecnico]     link building]
              |   |            |  |       |   |        |   |
            [post][post]    [post][post] [post][post] [post][post]
```

- **Pilar (pillar page)**: pagina ampla, ~2000-5000 palavras, cobertura completa do topico.
- **Clusters**: posts especificos sobre subtemas, linkados ao pilar.
- **Internal linking**: clusters -> pilar (e pilar -> clusters), reforcando autoridade temalogica.

### 12.2 Topical Authority (Koray Tugberk Gubur)

- Construir autoridade em **um topico amplo** antes de pulverizar para outros.
- Cobertura horizontal (todas as subqueries) + vertical (profundidade).
- Internal linking semantico (entidades + atributos).
- Resultado: Google passa a rankear o site **independente de backlinks** em subtopicos do topico-mae.

### 12.3 Skyscraper Technique (Brian Dean / Backlinko)

1. Identificar conteudo que ja **rankeia + tem backlinks**.
2. Criar versao **claramente superior** (mais profunda, atualizada, melhor design, dados originais).
3. Outreach: contatar quem linka para o original e oferecer a versao melhorada.

> Critico hoje: Skyscraper puro ("mesmo conteudo + 10%") nao passa em Helpful Content. Versao 2.0 exige diferenciacao real.

### 12.4 Hub-and-Spoke

- Variante do pilar/cluster com foco em autoridade radial.
- Hub = pagina central, spoke = paginas-satelite.
- Mais comum em e-commerce (categoria como hub, subcategorias e produtos como spokes).

### 12.5 SERP-First Content Brief

Em vez de comecar pelo brief do redator, **comecar pela SERP atual** da keyword:

1. Analisar top 10 (formato, comprimento, tom, estrutura, schema).
2. Extrair PAA, related searches.
3. Mapear AI Overview citations.
4. Identificar gap: o que falta na SERP atual que voce pode cobrir.
5. Brief com: angulo unico, profundidade-alvo, formato, schema necessario, autor sugerido (EEAT).

### 12.6 Search Intent Optimization (SIO)

- Analise de intent dominante.
- Conferencia cada secao do conteudo a um sub-intent da query.
- Eliminar paragrafos que nao respondem a intent.
- Estrutura espelhada com Featured Snippet / AI Overview.

### 12.7 Programmatic SEO (controverso)

- Geracao de paginas em escala usando templates + dados estruturados (ex.: Tripadvisor, Zapier, Indeed).
- Funciona quando: dados sao genuinos, unicos, uteis ao usuario.
- Falha (e cai em Spam Policies "scaled content abuse") quando: paginas finas, redundantes, sem valor agregado.

---

## 13. AI Overviews / SGE / Generative Search

### 13.1 Estado em 2026 (re-validar)

- **Google AI Overviews** — sucessor do SGE. Default em mais paises, ainda em rollout.
- **Bing Copilot** — AI search integrado.
- **Perplexity** — search engine AI-first.
- **ChatGPT search** — search com citacoes (OpenAI).
- **Claude** — search com citacoes (Anthropic).

### 13.2 Como aparecer em AI Overviews

| Sinal | Detalhe |
|-------|---------|
| **Conteudo bem-estruturado** | Headings claros, listas, tabelas, FAQ |
| **Resposta direta no inicio** | "Inverted pyramid" — resposta antes do contexto |
| **Schema.org rico** | Article, FAQ, HowTo, Product |
| **EEAT alto** | Autor real, fontes citadas |
| **Autoridade do dominio** | Backlinks + mencoes |
| **Freshness** | `dateModified` recente em topicos voláteis |
| **Cobertura da entidade** | Definir + atributos + relacoes |

### 13.3 Impacto no CTR

- Quando AI Overview esta presente, **CTR organico cai** (estudos de mercado: -20% a -60%, varia por intent).
- Intent informacional simples ("o que e X") tem queda maior.
- Intent transacional / comercial ("comprar X", "X vs Y") menos afetado.

### 13.4 Estrategia hibrida

- Para queries informacionais: aceitar zero-click parcial; otimizar para **citacao** em AI Overview (autoridade > tudo).
- Para queries transacionais: priorizar conteudo que converte na propria pagina.
- Diversificar fontes de trafego (newsletter, social organico, comunidades).

### 13.5 LLM-friendly content

- Estrutura semantica forte (headings, listas, tabelas).
- Resposta direta, sem fluff.
- Dados originais e verificaveis.
- Citacoes inline com fonte autoritativa.
- Nome da marca + nome da entidade visiveis em contexto.

---

## 14. Workflow de auditoria SEO em 10 fases

```
AUDITORIA SEO COMPLETA — 10 FASES
====================================

FASE 1 — DESCOBERTA E ACESSO
  [ ] Mapear stakeholders (cliente, dev, content, marketing, juridico)
  [ ] Coletar acessos: GSC, GA4, GTM, CMS admin, hospedagem
  [ ] Coletar acesso a Ahrefs/Semrush ou contratar
  [ ] Documentar stack: CMS, render, CDN, framework
  [ ] Listar dominios (canonical, redirects, internacional, mobile separado)

FASE 2 — CRAWL E SAUDE TECNICA
  [ ] Crawl completo (Screaming Frog ou similar) — modo Googlebot Smartphone
  [ ] robots.txt: bloqueios intencionais? errados?
  [ ] sitemap.xml: completo, atualizado, submetido em GSC?
  [ ] Codigos de status: 4xx, 5xx, redirects em massa
  [ ] Canonical: corretos, autorreferenciais quando aplicavel
  [ ] hreflang: bidirecional, codigo de regiao correto
  [ ] X-Robots-Tag, meta robots: noindex acidental?
  [ ] Renderizacao: CSR/SSR/SSG? Conteudo no HTML inicial?

FASE 3 — INDEXACAO
  [ ] GSC > Cobertura: indexadas vs nao-indexadas
  [ ] "Rastreada — nao indexada": quantas? Por que?
  [ ] "Detectada — nao indexada": crawl budget? Autoridade?
  [ ] Duplicatas: paginas alternativas com canonical
  [ ] URL Inspection em paginas-chave

FASE 4 — CORE WEB VITALS
  [ ] PageSpeed Insights de paginas-chave (mobile + desktop)
  [ ] GSC > Core Web Vitals: % de URLs em "Bom"
  [ ] CrUX dataset (BigQuery) para historico
  [ ] Identificar gargalos por metrica (LCP, INP, CLS)

FASE 5 — CONTEUDO
  [ ] Inventario de conteudo (URL, titulo, intent, volume, ranking, trafico, conversao)
  [ ] Identificar conteudo thin / scaled / duplicado
  [ ] Auditoria de EEAT por topico
  [ ] Cobertura de pillar / cluster
  [ ] Conteudo desatualizado (dateModified > 12 meses em topicos volateis)
  [ ] Cannibalization: duas paginas competindo pela mesma keyword

FASE 6 — KEYWORDS E INTENT
  [ ] Keyword set atual (Ahrefs/Semrush + GSC queries)
  [ ] Mapear intent por URL
  [ ] Gap analysis vs concorrencia
  [ ] Identificar quick wins (posicao 4-15 com volume)
  [ ] Identificar oportunidades em PAA, related searches, AI Overviews

FASE 7 — BACKLINKS
  [ ] Perfil de backlinks (Ahrefs/Semrush)
  [ ] Referring domains: crescimento, qualidade, anchor distribution
  [ ] Toxic links: PBN, spam, anchor over-optimized
  [ ] Disavow file (apenas se manual action ou risco real)
  [ ] Comparativo com concorrencia

FASE 8 — SERP E CONCORRENCIA
  [ ] Top 10 keywords-chave: quem rankeia? por que?
  [ ] SERP features: AI Overview, FS, PAA presentes?
  [ ] Share of Voice
  [ ] Comparativo de conteudo (profundidade, schema, EEAT)

FASE 9 — UX E ACESSIBILIDADE
  [ ] Mobile first: render correto em 360px
  [ ] Layout shift visual em paginas-chave
  [ ] Acessibilidade (WCAG): aria, alt, heading order, contraste
  [ ] Intersticiais intrusivos
  [ ] Pop-ups vs Page Experience

FASE 10 — PRIORIZACAO E PLANO
  [ ] Matriz Esforco x Impacto
  [ ] 90-day plan: top 10 acoes
  [ ] KPIs definidos
  [ ] Cadencia de revisao (mensal + apos core update)
```

---

## 15. Template — Briefing de conteudo SEO (SERP-first)

```
BRIEFING DE CONTEUDO SEO
==========================

1. KEYWORD-ALVO E CONTEXTO
   - Keyword principal: ____________
   - Volume mensal (Brasil): ____
   - Dificuldade (Ahrefs/Semrush): ____
   - Intent: [Informacional / Navegacional / Comercial / Transacional]
   - Estagio do funil: [TOFU / MOFU / BOFU / Pos-venda]
   - Variacoes / sinonimos: __________
   - Long-tails relacionadas: __________

2. ANALISE DA SERP ATUAL
   - Top 10 (URL + titulo + dominio)
   - SERP features ativas: [ ] AI Overview [ ] Featured Snippet [ ] PAA [ ] Image Pack [ ] Video [ ] Shopping [ ] Local [ ] Top Stories [ ] Knowledge Panel
   - Formato dominante: ____
   - Comprimento medio: ____ palavras
   - Tipo de fonte: [ ] Blog [ ] E-commerce [ ] Forum [ ] Wikipedia [ ] News [ ] Outro

3. PEOPLE ALSO ASK / RELATED
   - PAA 1: ____
   - PAA 2: ____
   - PAA 3: ____
   - Related searches: ____

4. ANGULO UNICO (DIFERENCIACAO)
   - O que falta na SERP atual?
   - Que dado original posso trazer?
   - Que experiencia (E de EEAT) posso demonstrar?
   - Que formato a SERP nao tem?

5. ESTRUTURA SUGERIDA
   - H1: ____ (com keyword + benefit)
   - H2-1: ____ (responder a query principal de cara)
   - H2-2: ____ (sub-intent 1)
   - H2-3: ____ (sub-intent 2)
   - ...
   - FAQ: ____ (3-5 perguntas)

6. EEAT
   - Autor: ____ (com bio, credencial, foto)
   - Schema: Article + Author + Organization
   - Fontes a citar (linkar): ____
   - Disclosure (afiliado/conflito)? ____

7. SCHEMA REQUERIDO
   [ ] Article / NewsArticle
   [ ] FAQPage
   [ ] HowTo
   [ ] Product
   [ ] Review / AggregateRating
   [ ] BreadcrumbList
   [ ] Person (autor)
   [ ] Organization

8. INTERNAL LINKING
   - Link DE qual pilar/cluster?
   - Link PARA quais paginas?
   - Anchor sugeridos: ____

9. ASSETS
   - Imagens originais: ____
   - Infografico: ____
   - Video: ____
   - Tabela/calculadora: ____

10. METAS
    - Posicao-alvo: ____
    - Trafego-alvo (12 meses): ____
    - Conversao-alvo: ____

11. CONTRADITORIO INTERNO
    - Esse conteudo passaria em Helpful Content System?
    - Ha risco de cannibalization com pagina existente?
    - O angulo unico justifica a publicacao?

12. APROVACAO
    - Cliente: ____
    - SEO: ____
    - Editorial: ____
    - Juridico (se aplicavel): ____
```

---

## 16. Outras searches — alem do Google

### 16.1 Bing / Copilot

- Quota de mercado: ~3-7% global, mais alto em corporate (default no Edge), windows 11.
- **Bing Webmaster Tools** equivalente ao GSC.
- **Copilot** integra GPT-4-class. Importante: Bing alimenta Copilot e DuckDuckGo.
- Otimizacoes: similar ao Google, mas Bing valoriza mais social signals e backlinks brutos.

### 16.2 DuckDuckGo

- Resultado vem **principalmente do Bing** (com mistura propria).
- Sem tracking. Importante para audiencia privacy-aware.
- Sem ferramenta de webmaster propria.

### 16.3 Yandex (Russia / CIS)

- Algoritmo proprio (MatrixNet, depois CatBoost).
- **Yandex Webmaster** e o equivalente ao GSC.
- Importante se publico-alvo for Russia, Belarus, Cazaquistao, Ucrania (parte).
- Vazamento de docs em jan/2023 revelou ~1900 fatores — referencia interessante (com ressalva).

### 16.4 Baidu (China)

- Necessario ICP license (registro govt) para hospedagem na China.
- **Baidu Webmaster Tools**.
- Cuidado com servicos Google bloqueados.

### 16.5 Buscas verticais

| Vertical | Buscador / canal |
|----------|-------------------|
| **Video** | YouTube, TikTok (sim, gen Z usa para search), Vimeo |
| **Profissional** | LinkedIn search |
| **E-commerce** | Amazon, Mercado Livre, Magalu — SEO interno |
| **App store** | App Store Optimization (ASO) — Apple App Store, Google Play |
| **Mapas** | Google Maps, Apple Maps, Waze |
| **Comunidade** | Reddit, Quora, Stack Overflow |

### 16.6 LLMs com citacoes (search via IA)

- **Perplexity** — search engine AI-first com citacoes.
- **ChatGPT search** — OpenAI com citacoes.
- **Claude** (com browsing) — Anthropic com citacoes.
- **Gemini** — Google com AI Overviews.
- Ferramentas para otimizar (LLM Optimization / GEO — Generative Engine Optimization): em maturacao em 2026, monitorar.

---

## 17. Regulacao BR — CONAR, CDC, LGPD em SEO

### 17.1 CONAR — Conselho Nacional de Autorregulamentacao Publicitaria

- Codigo Brasileiro de Autorregulamentacao Publicitaria.
- Aplica-se a publicidade — **e SEO conta** quando o conteudo tem natureza publicitaria (afiliado, patrocinado).
- Principios: veracidade, lealdade, identificacao publicitaria, respeito.
- Conteudo afiliado e patrocinado **deve ser identificado** ("este post e patrocinado por X" / "links de afiliado").

### 17.2 CDC — Codigo de Defesa do Consumidor

- Lei 8.078/1990. Aplica-se a relacao de consumo — incluindo informacao em SEO.
- Direito a informacao adequada e clara (art. 6, III).
- Publicidade enganosa (art. 37) — promete o que nao entrega.
- Publicidade abusiva (art. 37, §2) — discriminatoria, explorando crianca, etc.

### 17.3 LGPD em SEO

- Captura de leads via formulario: base legal definida, consentimento ou legitimo interesse.
- Cookies de analytics (GA4) e marketing: banner de cookies + consentimento.
- Remarketing baseado em comportamento de busca: consentimento explicito.
- Direito do titular a apagamento: SEO de paginas com nome de pessoas (ex.: "Pessoa X foi processada") — direito ao esquecimento. Caso a caso.

### 17.4 Marco Civil da Internet (Lei 12.965/2014)

- Neutralidade de rede — relevante em discussoes sobre AMP / preload.
- Guarda de registros de acesso a aplicacoes (art. 15) — 6 meses.

### 17.5 Skill cruzada

Detalhes em `conhecimento-conar-cdc` (a criar). Esta skill apenas alerta o agente de que SEO BR opera sob esse arcabouco.

---

## 18. Regras de Ouro para o agente `frank-mkt`

1. **SEO bom = conteudo bom + UX boa + tecnico solido** — sem atalho. Quem promete "ranking em 7 dias" em keyword competitiva esta vendendo ilusao.
2. **NAO CHUTAR** — nao inventar volume de keyword, dificuldade, posicao, fator de ranking, atualizacao do algoritmo. Se nao tem dado, peca acesso ou marque como hipotese.
3. **Nao recomendar pratica que viole Spam Policies** — PBN, conteudo escalado, abuso de reputacao, doorway, cloaking. Risco de penalizacao manual ou algoritmica de site inteiro.
4. **EEAT tem que ser demonstravel** — autor real, credenciais visiveis, fonte primaria, data, disclosure de conflito. Em YMYL, EEAT e o pilar.
5. **Em SERP com AI Overviews, share of clicks cai** — calcular ROI considerando zero-click. Diversificar canais.
6. **Mobile-first sempre** — Googlebot Smartphone e o default de indexacao desde 2023. Auditar em mobile primeiro.
7. **CWV e medido em campo (CrUX), nao apenas lab** — Lighthouse 100 nao garante "Bom" em CWV se usuarios reais tem rede ruim.
8. **Helpful Content System penaliza site inteiro** — risco sistemico. Conteudo medioco arrasta o bom.
9. **Re-validar fatos voláteis a cada 3-6 meses** — Google muda silenciosamente. Validar em fonte oficial antes de citar em peca formal (decaimento temporal).
10. **Topical authority > volume bruto** — melhor cobrir um topico em profundidade do que pulverizar. 30 posts no mesmo cluster valem mais que 100 dispersos.
11. **Conteudo gerado por IA nao e proibido — mas exige revisao humana e EEAT** — Google penaliza conteudo nao-util, nao IA per se. Conteudo AI sem revisor + sem expertise direta tipicamente cai em scaled content abuse.
12. **Disclosure obrigatorio** em conteudo afiliado, patrocinado, ou com conflito de interesse — CONAR + CDC + Helpful Content + EEAT.

---

## 19. Exemplos comportamentais — SEO

### Exemplo 1 — Cliente promete ranking #1 em 30 dias

**Input do usuario:** "A agencia de SEO promete colocar o cliente em primeiro lugar do Google em 30 dias para a keyword `crm para pequenas empresas`. Vale contratar?"

**Resposta esperada do agente `frank-mkt`:**

> CORRIGE: "Promessa irreal. `crm para pequenas empresas` no Brasil tem dificuldade media-alta (validar em Ahrefs/Semrush — nao chutar volume), domina por marcas estabelecidas (Salesforce, Pipedrive, RD Station, HubSpot, Agendor) com autoridade construida em anos. SEO em keyword competitiva tipicamente leva 6-18 meses para chegar a top 3. Quem promete 30 dias geralmente faz: (1) ranking em keyword sem volume mas que da o numero 1 para o relatorio; (2) PBN ou link spam — risco de penalizacao manual; (3) cloaking ou doorway — banimento. Sinais de alerta: garante posicao, oferece volume de links, sem audit previo, sem GSC compartilhado. Recomendo auditoria SEO de 4 semanas com KPIs de negocio (trafego nao-marca, conversao) antes de qualquer compromisso de ranking."

**Comportamento-chave:** ataca a falsa premissa de "ranking rapido", explica realidade do mercado, sinaliza riscos especificos de Spam Policies, oferece alternativa baseada em KPI de negocio.

### Exemplo 2 — Site dropou apos core update

**Input do usuario:** "O blog do cliente perdeu 60% do trafego organico em 2 semanas. Saiu um core update no mesmo periodo."

**Resposta esperada do agente `frank-mkt`:**

> Ativa diagnostico estruturado: "Antes de atribuir ao core update — confirmar timing exato. Validar: (1) GSC > Performance, comparar 28 dias antes vs 28 dias depois — quais queries e paginas perderam? (2) Search Status Dashboard — datas oficiais do update; (3) Concorrentes do nicho tambem dropparam ou subiram? (4) Indicador de Helpful Content — site tem conteudo escalado, thin, IA sem revisao, tematica difusa? (5) EEAT — autores reais? credenciais visiveis? Em queda apos core update, hipoteses comuns: HCS rebaixou conteudo nao-util; cannibalization apos update de relevancia; perda de autoridade temalogica; topico migrado para AI Overviews. Recovery e tipicamente 6-12 meses ou ate proximo update favoravel — nao ha botao de reverter. Plano de 90 dias: auditar conteudo, deletar/consolidar thin, reforcar EEAT em paginas-chave, criar conteudo unico com angulo proprio. Re-validar resultado a cada core update."

**Comportamento-chave:** rejeita atribuicao automatica ao update, exige dados, lista hipoteses estruturadas, alinha expectativa de recovery, propoe plano.

### Exemplo 3 — IA escrevendo todo o blog

**Input do usuario:** "Quero gerar 500 artigos com ChatGPT em 1 semana e publicar no blog do cliente. Vai escalar SEO, certo?"

**Resposta esperada do agente `frank-mkt`:**

> CORRIGE: "Risco alto de violar Google Spam Policies (mar/2024) — categoria `scaled content abuse`. Google e claro: nao penaliza IA per se; penaliza conteudo NAO util e produzido em escala para manipular ranking. 500 artigos em 1 semana sem revisao humana, sem expertise direta, sem dado original, tipicamente cai nesse criterio. Resultado provavel: HCS rebaixa o site inteiro — nao apenas os 500 artigos. Alternativa segura: usar IA como **assistente** — outline, primeira versao, sumarizacao. Mas exigir revisor humano com expertise no tema, autor identificado, dado original adicionado, fonte primaria citada. Volume realista: 5-15 artigos/semana com qualidade, nao 500/semana sem ela. Pergunta de contraditorio: 'esse conteudo agrega algo que ja nao existe na primeira pagina do Google?' Se a resposta for nao, nao publica."

**Comportamento-chave:** cita politica especifica (mar/2024), distingue uso legitimo de IA vs scaled abuse, propoe alternativa operacional, recoloca a pergunta de Helpful Content.

### Exemplo 4 — Migration de WordPress para Next.js

**Input do usuario:** "Vamos migrar de WordPress para Next.js. Qual o impacto SEO?"

**Resposta esperada do agente `frank-mkt`:**

> Estrutura riscos + plano: "Migration de CMS e zona de risco SEO classica. Riscos principais: (1) URLs mudam sem 301 -> perda de trafego e backlinks; (2) Render muda — se Next.js ficar em CSR puro, pode ter atraso de indexacao; (3) Schema/canonical se nao replicado; (4) hreflang se internacional; (5) sitemap nao atualizado; (6) CWV podem melhorar OU piorar conforme implementacao. Decisoes-chave: SSG (estatico, otimo para SEO + performance), SSR (HTML completo no GET), ISR (hibrido — recomendado para blog grande). Evitar CSR puro. Plano de 8 etapas: (a) inventario completo de URLs WP; (b) mapping 1:1 ou 301 documentado; (c) staging com noindex + lighthouse + screaming frog; (d) replicar schema, canonical, hreflang, sitemap; (e) cutover em janela de baixo trafego; (f) monitorar GSC > Cobertura por 7 dias; (g) submeter sitemap atualizado; (h) acompanhar trafego e queries por 30 dias. Lembrar: backlink externo aponta para URL antiga; sem 301, perde-se autoridade. Plano de re-grounding em 30/60/90 dias."

**Comportamento-chave:** lista riscos especificos, recomenda render correto, fornece plano operacional em etapas, define monitoramento.

---

## 20. Checklist de Contraditorio Interno — SEO

Aplicar antes de entregar parecer, plano ou peca de SEO ao cliente.

| # | Pergunta destruidora | O que busca |
|---|----------------------|-------------|
| 1 | O conteudo proposto **passaria no Helpful Content System** se publicado hoje? Foi feito para humano ou para Google? | Risco HCS sistemico |
| 2 | As keywords escolhidas tem **volume real validado** em ferramenta, ou foi chute? O cluster reflete intent observado na SERP, ou e wishful thinking? | Anti-chute de KW |
| 3 | **EEAT esta demonstravel** (autor real, credenciais, fonte primaria, data, disclosure), ou e generico? | EEAT real |
| 4 | Os **Core Web Vitals** (LCP/INP/CLS) passam o threshold de "Good" em **mobile** com dados de **CrUX**, nao so Lighthouse lab? | UX tecnica de campo |
| 5 | O site e **indexavel** (robots, canonical, sitemap, sem noindex acidental, hreflang correto)? Ja inspecionei URLs-chave no GSC? | Saude tecnica |
| 6 | As paginas-chave estao em **"Indexada"** no GSC, ou em "Detectada — nao indexada" / "Rastreada — nao indexada"? Por que? | Indexacao real |
| 7 | O conteudo seria considerado **escalado** segundo Spam Policies (mar/2024), ou tem diferenciacao real (dado original, expertise, formato)? | Anti-scaled abuse |
| 8 | **AI Overviews / SGE** estao tomando o trafego desse cluster? Ha plano de fallback (zero-click)? | Realidade SERP 2026 |
| 9 | Existem **links nao-naturais** (PBN, troca reciproca artificial, anchor over-optimized)? Risco de penalizacao manual? | Backlink saudavel |
| 10 | KPIs medidos refletem **negocio** (trafego nao-marca, conversao, CAC, LTV) ou so **vaidade** (impressao, posicao 1, DA)? | KPI de negocio |

---

## 21. Referencias canonicas

### 21.1 Oficiais Google

- **Google Search Central** — https://developers.google.com/search
- **Google Search Essentials** (antigo Webmaster Guidelines) — https://developers.google.com/search/docs/essentials
- **SEO Starter Guide** — https://developers.google.com/search/docs/fundamentals/seo-starter-guide
- **Spam Policies** — https://developers.google.com/search/docs/essentials/spam-policies
- **Ranking Systems Guide** — https://developers.google.com/search/docs/appearance/ranking-systems-guide
- **Search Quality Rater Guidelines** (PDF) — https://services.google.com/fh/files/misc/hsw-sqrg.pdf
- **Search Status Dashboard** — https://status.search.google.com
- **Google Search Console** — https://search.google.com/search-console
- **Google Search Liaison** (X/Twitter) — atualizacoes informais
- **Google Search Central Blog** — https://developers.google.com/search/blog
- **web.dev** (Core Web Vitals + best practices) — https://web.dev
- **PageSpeed Insights** — https://pagespeed.web.dev
- **Schema Markup Testing Tool / Rich Results Test** — https://search.google.com/test/rich-results
- **Mobile-Friendly Test** — descontinuado em 2023; usar Lighthouse + GSC

### 21.2 Oficiais Bing / Microsoft

- **Bing Webmaster Tools** — https://www.bing.com/webmasters
- **Bing Webmaster Guidelines** — https://www.bing.com/webmasters/help/webmasters-guidelines-30fba23a

### 21.3 Padroes / Especificacoes

- **schema.org** — https://schema.org
- **RFC 9309 — Robots Exclusion Protocol** (2022) — https://www.rfc-editor.org/rfc/rfc9309
- **Sitemaps protocol** — https://www.sitemaps.org
- **WCAG 2.x** (acessibilidade) — https://www.w3.org/WAI/standards-guidelines/wcag
- **Open Graph protocol** — https://ogp.me

### 21.4 Bibliografia profissional (referencia, nao oficial)

- **Moz — Beginner's Guide to SEO** — https://moz.com/beginners-guide-to-seo
- **Ahrefs Blog** — https://ahrefs.com/blog
- **Backlinko (Brian Dean)** — https://backlinko.com (cuidado: alguns frameworks sao opiniao do autor, nao oficiais)
- **Search Engine Land** — https://searchengineland.com
- **Search Engine Journal** — https://www.searchenginejournal.com
- **Sistrix Blog** — https://www.sistrix.com/blog
- **Aleyda Solis — Crawling Mondays** — referencia em SEO tecnico
- **Lily Ray** — referencia em EEAT/YMYL
- **Glenn Gabe** — analise de core updates
- **Marie Haynes Newsletter** — analise de updates
- **Koray Tugberk Gubur — Holistic SEO** — topical authority

### 21.5 Brasil

- **CONAR** — https://www.conar.org.br
- **CDC (Lei 8.078/1990)** — http://www.planalto.gov.br/ccivil_03/leis/l8078compilado.htm
- **LGPD (Lei 13.709/2018)** — http://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm
- **Marco Civil da Internet (Lei 12.965/2014)** — http://www.planalto.gov.br/ccivil_03/_ato2011-2014/2014/lei/l12965.htm
- **IAB Brasil** — https://iabbrasil.com.br
- **ABRADi (agencias)** — https://abradi.com.br

---

## 22. Referencia cruzada de skills

| Situacao | Skills relacionadas |
|----------|----------------------|
| Plano de conteudo organico para o blog | `seo-fundamentos` + `seo-keywords` + `conteudo-evergreen` + `copywriting-conversao` |
| Auditoria tecnica de site | `seo-fundamentos` + `seo-tecnico` + `ux-heuristicas` + `acessibilidade-wcag` |
| Brief de pagina nova | `seo-fundamentos` + `seo-keywords` + `seo-on-page` + `copywriting-conversao` |
| Estrategia de autoridade | `seo-fundamentos` + `seo-link-building` + `comunicacao-corporativa` |
| Migracao de site | `seo-fundamentos` + `seo-tecnico` + `conhecimento-search-console` |
| Drop apos core update | `seo-fundamentos` + `manutencao-skills` (re-grounding) + `seo-tecnico` |
| Conteudo afiliado / patrocinado | `seo-fundamentos` + `conhecimento-conar-cdc` + `copywriting-conversao` |
| Otimizacao para AI Overviews | `seo-fundamentos` + `seo-on-page` + `conteudo-evergreen` |
| Pesquisa competitiva | `seo-fundamentos` + `analise-concorrencia` + `seo-keywords` |
| LinkedIn / Instagram / Facebook (organico — nao usa SEO classico) | `linkedin-organico` / `instagram-feed-reels` / `facebook-organico` (skills proprias) |

---

## 23. Integracao com o ecossistema Frank-MKT

Esta skill integra-se ao agente principal `frank-mkt` (`agents/frank-mkt.md`) e ao restante do plugin da seguinte forma:

- **Acoplamento com `seo-keywords`, `seo-on-page`, `seo-tecnico`, `seo-link-building`, `conteudo-evergreen`** — esta skill carrega ANTES de qualquer especialista SEO. Estabelece o modelo mental, pipeline (crawl/render/index/rank), intent, fatores de ranking, EEAT, HCS, Spam Policies, CWV, AI Overviews. Especialistas pressupoem que esses conceitos ja estao acessiveis ao agente.
- **Acoplamento com o agente `auditor`** — quando o `auditor` rodar regras PASS/FAIL em peca SEO (artigo, brief, plano), esta skill fornece o framework normativo (Spam Policies, EEAT, HCS, CWV) para o auditor fundamentar PASS ou FAIL com referencia oficial.
- **Acoplamento com o agente `perfilador-mercado`** — a leitura de SERP (Secao 4) e parte do perfilamento competitivo. `perfilador-mercado` consome dados de SoV, share de SERP features, citacoes em AI Overviews; esta skill define como ler.
- **Acoplamento com o agente `redator-hacker`** — copy e SEO sao indissociaveis. `redator-hacker` deve respeitar EEAT (autor + credencial + fonte), Helpful Content (responder a intent real, nao apenas inserir keyword), e disclosure (CONAR/CDC quando afiliado/patrocinado).
- **Acoplamento com o agente `seo-strategist`** — agente especialista em SEO que orquestra as skills SEO. Esta skill e a sua biblia operacional.
- **Acoplamento com o agente `ux-ui-revisor`** — Page Experience Signal cruza UX e SEO. CWV (Secao 9), heuristicas, acessibilidade, intersticiais — todos sao tanto UX quanto SEO.
- **Acoplamento com o agente `social-humanitario` / `frank-corporativo`** — comunicacao com proposito tambem precisa de EEAT alto (especialmente em YMYL: causas de saude, legal, financeira). Esta skill fornece o filtro de EEAT.
- **Acoplamento com `compliance-lgpd` (plugin juridico) ou `conhecimento-conar-cdc`** — captura de leads, cookies, remarketing baseado em busca, direito ao esquecimento — todos sao decisoes hibridas de SEO + Direito.
- **Memoria e rastreabilidade** — auditorias, briefings, planos de 90 dias, monitoramento de core updates sao persistidos em `.frank-mkt/seo/<cliente>/<data>/` pelo agente `suporte-documental` (a criar) ou diretamente pelo `frank-mkt`. Versionar para reuso e comparacao temporal.
- **Contraditorio interno** — o agente principal aciona o modulo `contraditorio-interno` carregando o Checklist da Secao 20 desta skill como gatilho obrigatorio antes de entregar parecer, plano ou peca SEO.
- **Decaimento temporal** — esta skill esta em volatility `medium` (6 meses). Re-grounding obrigatorio em fontes da Secao 21 antes de citar fato volátil (algoritmo, politica, threshold de CWV, sistema de ranking) em peca formal. Skill `manutencao-skills` (a criar) agenda revisao em `next_review`.
- **Regra de ouro para `frank-mkt`** — nenhuma entrega SEO sai do plugin sem passar por esta skill como base; isso inclui briefings, auditorias, planos de conteudo, decisoes de migracao, resposta a core update e estrategia de autoridade.

---

> **Aviso:** o plugin `frank-mkt` e um assistente de analise. Recomendacoes desta skill devem ser adaptadas a realidade de cada cliente, mercado e nicho, e validadas em fonte oficial (Google Search Central, web.dev, schema.org, Bing Webmaster) antes de aplicar em peca formal. SEO e disciplina dinamica — Google atualiza sistemas continuamente.

---

*Plugin `frank-mkt` — skill `seo-fundamentos` (v0.1.0)*
*Ultima atualizacao: 2026-05-07*
