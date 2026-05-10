---
name: seo-link-building
description: "Link building etico e construcao de autoridade externa. Modelo mental (PageRank, link equity, anchor signal, co-citacao, brand mention), tipos de backlink (rel dofollow/nofollow/ugc/sponsored, posicao, contexto, editorial vs UGC), metricas de autoridade (DR/DA/AS/URL Rating/Trust Flow/Citation Flow/Brand Authority), backlink quality signals (8 fatores), toxic links + Google Spam Policies (PBN, link farms, paid sem disclosure, link schemes), disavow tool (quando SIM, quando NAO), anchor text distribution natural, link velocity, auditoria de perfil de backlinks, reverse engineering de competidores, linkable assets (15+ tipos: research, tools, calculators, ultimate guides, statistics pages), estrategias (Skyscraper, Broken Link, Resource Page, Guest Post com cuidado, Unlinked Brand Mention, Podcast Guesting, Newsjacking, HARO/Connectively, Image Reverse), digital PR + journalist outreach + pitch templates, outreach (email frameworks, personalization, follow-up, ferramentas), local link building (citations, NAP, GBP, diretorios BR), B2B SaaS (Capterra, G2, integration pages, partnerships), e-commerce, anti-patterns black/gray hat, auditoria 12 fases, templates."
user-invocable: false
last_verified: 2026-05-07
next_review: 2026-11-07
volatility: medium
regrounding_sources:
  - "https://developers.google.com/search"
  - "https://developers.google.com/search/docs/essentials/spam-policies"
  - "https://developers.google.com/search/docs/crawling-indexing/links-crawlable"
  - "https://developers.google.com/search/blog"
  - "https://search.google.com/search-console/disavow-links-tool"
  - "https://ahrefs.com/blog/link-building/"
  - "https://www.semrush.com/blog/link-building/"
  - "https://moz.com/learn/seo/link-building"
  - "https://www.connectively.us"
  - "https://www.bing.com/webmasters/help/webmasters-guidelines-30fba23a"
---

# Skill: seo-link-building

> **Decaimento Temporal**
> Ultima verificacao: 2026-05-07 | Proxima revisao: 2026-11-07 | Volatility: **medium** (6 meses)
> Google atualiza politicas de link spam e core algorithm; HARO foi descontinuado em 2024 e substituido por Connectively + alternativas; ferramentas de outreach evoluem. Re-validar antes de publicar peca formal:
> - Google Spam Policies — https://developers.google.com/search/docs/essentials/spam-policies
> - Google Search Central — Link best practices — https://developers.google.com/search/docs/crawling-indexing/links-crawlable
> - Google Search Liaison (X/Twitter) — atualizacoes informais
> - Google Disavow Tool — https://search.google.com/search-console/disavow-links-tool
> - Connectively (sucessor do HARO) — https://www.connectively.us
> - Bing Webmaster Guidelines — https://www.bing.com/webmasters/help/webmasters-guidelines-30fba23a
>
> **Acionamento:** plano de link building, auditoria de backlinks, recovery pos-manual-action, digital PR, linkable asset, HARO/Connectively pitch, outreach, autoridade local, B2B SaaS link building, e-commerce link building, disavow, anti-PBN, link velocity.
> **Skills relacionadas:** `seo-fundamentos` (carrega ANTES desta), `seo-keywords` (KW alvo de campanha), `seo-on-page` (linkable asset estruturado), `seo-tecnico` (preservar links em migracao), `analise-concorrencia`, `comunicacao-corporativa` (digital PR), `copywriting-conversao` (pitch + linkable asset), `conhecimento-conar-cdc` (disclosure de patrocinio).
> **Pre-requisito:** ter carregado `seo-fundamentos` (modelo mental, EEAT, HCS, Spam Policies). Sem isso, link building vira tatica isolada com risco de penalizacao.

---

## 1. Visao Geral

Link building e a disciplina de **adquirir backlinks editoriais** de sites autoritativos e relevantes para construir **autoridade do dominio** ao longo do tempo. E o vetor mais antigo de SEO (PageRank original, 1996) e ainda um dos mais impactantes em 2026 — apesar de Google diminuir importancia retorica, o vazamento da Content Warehouse API (mai/2024) confirmou sinais como `siteAuthority` e `linkAuthority`.

Esta skill nao repete fundamentos. Aqui aprofundamos:

- **Modelo mental**: PageRank, link equity, anchor signal, co-citacao, brand mention.
- **Tipos de backlink**: `rel`, posicao, contexto, editorial vs UGC vs sponsored.
- **Metricas de autoridade**: DR (Ahrefs), DA (Moz), AS (Semrush), URL Rating, Trust Flow / Citation Flow (Majestic), Brand Authority (Moz).
- **Backlink quality signals**: 8 fatores de qualidade (relevancia, autoridade, trafego, anchor, posicao, contexto, spam score, idioma).
- **Toxic links + Spam Policies + Disavow correto**.
- **Anchor text distribution natural**.
- **Link velocity** — crescimento natural vs spike artificial.
- **Auditoria de perfil**: workflow + ferramentas.
- **Reverse engineering** de competidores — content gap + link gap.
- **Linkable assets** — 15+ tipos.
- **Estrategias de aquisicao**: Skyscraper, Broken Link, Resource Page, Guest Post (com cuidado), Unlinked Brand Mention, Podcast Guesting, Newsjacking, HARO/Connectively, Image Reverse, Statistics Pages, Original Research.
- **Digital PR**: workflow + journalist outreach + pitch templates.
- **Outreach**: frameworks de email, personalizacao, follow-up, ferramentas.
- **Local + B2B SaaS + e-commerce**: tatica especifica.
- **Anti-patterns**: black hat / gray hat / Spam Policies.

### 1.1 Acionamento — quando esta skill carrega

| Gatilho | Exemplo |
|---------|---------|
| Plano de autoridade | "como construir DR de 30 para 60 em 12 meses?" |
| Auditoria de backlinks | "perfil esta saudavel? ha toxico?" |
| Recovery pos-penalizacao | "GSC acao manual: 'links artificiais' — o que fazer?" |
| Digital PR | "queremos midia falando do nosso negocio" |
| HARO/Connectively | "como pitchar journalists?" |
| Linkable asset | "que conteudo cria backlinks naturalmente?" |
| Concorrente forte | "concorrente tem 500 referring domains, nos 50 — como atacar?" |
| Disavow | "ha 2k backlinks spam apontando, vale disavow?" |
| Local | "como conseguir backlinks de cidade/regiao?" |
| B2B SaaS | "queremos sair em Capterra, G2, comparativo de SaaS" |

### 1.2 Pre-requisitos

- [ ] **`seo-fundamentos` carregada** (modelo mental + Spam Policies + Helpful Content).
- [ ] **GSC > Links** acessivel.
- [ ] **Ferramenta de backlinks**: Ahrefs (default da industria) OU Semrush OU Majestic OU Moz Pro.
- [ ] **Inventario de top backlinks atual** + benchmark de 3-5 concorrentes.
- [ ] **Politica editorial e de marca** (voz, tom, expertise, autores publicaveis).
- [ ] **EEAT acessivel** — quem da quote, com que credencial.
- [ ] **Glossario / dado original / asset** que o cliente possui ou pode produzir.
- [ ] **Email profissional + dominio** para outreach (NAO Gmail pessoal).

> **Cristal C0 — NAO CHUTAR.** DR/DA/AS/Trust Flow nao sao numeros oficiais Google — sao indices proprietarios de cada ferramenta. Tratar como referencia, nao como verdade absoluta. Trafico organico estimado e mais util que indice de autoridade.

---

## 2. Modelo mental — PageRank, link equity, anchor signal, co-citacao, brand mention

### 2.1 PageRank (algoritmo original, 1996, atualizado)

Cada link e um "voto". Voto vale mais quando:
- Vem de pagina com **muitos votos recebidos** (autoridade).
- Vem de pagina com **poucos links de saida** (concentra valor).
- Vem de pagina **relevante semanticamente** (Google evoluiu para topical PageRank).
- Pagina **dofollow**, indexavel, nao penalizada.

### 2.2 Link equity / link juice

Quantidade de "valor SEO" que um link transmite. Influenciada por:
- Autoridade da pagina origem.
- Contexto (texto ao redor).
- Posicao na pagina (body > sidebar > footer).
- Quantidade de links de saida na mesma pagina.
- `rel` attribute.

### 2.3 Anchor text como sinal

Texto clicavel do link sinaliza para Google sobre o que e a pagina destino:
- "guia completo de SEO" -> destino sobre SEO.
- "click here" -> sinal nulo.
- Anchor over-exact-match em massa -> sinal de manipulacao.

### 2.4 Co-citacao e co-ocorrencia

Quando duas marcas/sites sao **mencionados juntos** repetidamente (mesmo sem link direto), Google associa entidades:
- "Pipedrive e Salesforce sao CRMs lider de mercado" -> Pipedrive ganha associacao com "CRM" e com "Salesforce".

### 2.5 Brand mention sem link

Mencao da marca em texto (sem link) tambem e sinal — confirmado em vazamento Content Warehouse (`brandConfidence`, `entityConfidence`). Importante: **mention** + **brand awareness** crescem autoridade mesmo sem link.

### 2.6 EEAT + autoridade

Autoridade do dominio nao e so backlinks. Inclui:
- Co-citacoes em fontes autoritativas.
- Mencoes em Wikipedia/Wikidata (`sameAs` em Person/Organization).
- Reviews verificaveis.
- Cobertura de imprensa.
- Aparicoes em podcasts, conferencias, livros.

---

## 3. Tipos de backlink

### 3.1 Por atributo `rel`

| Atributo | Significado | Passa autoridade? |
|----------|-------------|-------------------|
| **(sem rel)** | Dofollow editorial | Sim — alvo principal |
| `rel="nofollow"` | Hint de nao-endorso | Pouco (em 2019 Google passou a tratar como hint, nao directive — pode passar parcialmente) |
| `rel="ugc"` | User-generated content | Hint nao-endorso |
| `rel="sponsored"` | Pago/patrocinado/afiliado | Hint nao-endorso (obrigatorio em paid links) |
| `rel="noopener"` / `rel="noreferrer"` | Seguranca/privacidade | Nao afeta SEO |

> Em 2026, Google trata `nofollow`/`ugc`/`sponsored` como **hint** — pode considerar para ranking se contexto justifica. Nao descartar como zero-valor.

### 3.2 Por posicao na pagina

| Posicao | Valor relativo |
|---------|----------------|
| **Body content** (paragrafo editorial) | Alto |
| **Sidebar** | Medio |
| **Header / nav** | Medio (sitewide pode ser visto como manipulativo) |
| **Footer** | Baixo (sitewide footer link e classico spam) |
| **Comentarios** | Baixo (`rel=ugc` tipicamente) |
| **Author bio em guest post** | Baixo-medio |

### 3.3 Por contexto

| Contexto | Valor |
|----------|-------|
| **Editorial** (jornalista/redator decidiu citar) | Alto |
| **Recurso curado** (pagina "best of...") | Alto |
| **Diretorio editorial** (Awwwards, Product Hunt) | Medio-alto |
| **Diretorio generico** (Hotfrog, Manta) | Baixo |
| **Comentario em forum** | Baixo |
| **Footer de portfolio** ("designed by X") | Medio |
| **Guest post relevante** | Medio |
| **Press release distribuido em massa** | Baixo (Google reduziu valor) |
| **Wikipedia** | Alto qualitativo (mesmo nofollow) — gera trafego + autoridade reflexa |

### 3.4 Por escopo

| Escopo | Detalhe |
|--------|---------|
| **Single-page link** | 1 pagina linka — saudavel |
| **Sitewide link** | Footer/header replicado em milhares de paginas — risco de manipulacao se exato em massa |
| **Author bio sitewide** (em guest post) | Pode ser visto como manipulativo se em massa |

---

## 4. Metricas de autoridade — comparativo

### 4.1 Indices proprietarios

| Metrica | Ferramenta | Como calcula | Escala |
|---------|------------|--------------|--------|
| **Domain Rating (DR)** | Ahrefs | Forca do perfil de backlinks do dominio (logaritmica) | 0-100 |
| **URL Rating (UR)** | Ahrefs | Forca do perfil da URL especifica | 0-100 |
| **Domain Authority (DA)** | Moz | ML model que correlaciona com posicao | 0-100 |
| **Page Authority (PA)** | Moz | Equivalente a UR | 0-100 |
| **Authority Score (AS)** | Semrush | Combinacao de backlinks + trafego + spam | 0-100 |
| **Trust Flow (TF)** | Majestic | Qualidade dos backlinks (proximidade a sites confiaveis) | 0-100 |
| **Citation Flow (CF)** | Majestic | Quantidade de backlinks (forca bruta) | 0-100 |
| **Brand Authority** | Moz | Forca de marca (mencoes, queries marca) | 0-100 |

### 4.2 Triangulacao recomendada

Para keyword/dominio critico, validar autoridade em **>= 2 fontes**:
- Ahrefs DR + Trafego organico estimado.
- Moz DA + Brand Authority.
- Semrush AS + organic search traffic.

Diferencas grandes (>30 pontos) = um indice esta enganando, ou perfil tem distorcao (ex.: muitos backlinks toxicos inflando CF).

### 4.3 Logaritmica vs linear

Subir DR de 30 para 40 e mais facil que de 60 para 70. Escala logaritmica reflete diminishing returns. Plano deve respeitar:
- DR 0-20: foco em fundacao basica.
- DR 20-40: momentum + linkable assets.
- DR 40-60: digital PR + autoridade tematica.
- DR 60+: parcerias estrategicas + thought leadership.

### 4.4 Limitacoes

- **NAO sao numeros oficiais Google** — Google tem `siteAuthority` interno (vazamento), mas nao publico.
- Podem ser inflados por links spam.
- Nao consideram totalmente trafego ou conversao.
- Trafego organico estimado e KPI mais util.

---

## 5. Backlink quality signals — 8 fatores

| # | Fator | Por que importa |
|---|-------|-----------------|
| 1 | **Relevancia tematica** | Link de site do mesmo nicho/topico vale mais. Topical PageRank |
| 2 | **Autoridade do dominio origem** | DR/DA/AS alto = link forte (com ressalvas) |
| 3 | **Trafego organico real do dominio origem** | Trafego > indice — site morto com DR alto (vazado em 2023+) e armadilha |
| 4 | **Anchor text** | Descritivo > generico; natural > over-optimized |
| 5 | **Posicao na pagina** | Body editorial > sidebar > footer |
| 6 | **Contexto ao redor** | Texto adjacente reforca relevancia |
| 7 | **Spam score / cleanliness** | Origem sem links toxicos sai-(out)bound em massa |
| 8 | **Match de idioma + geo** | pt-BR -> pt-BR = mais valor; en-US -> pt-BR = OK se relevante |

### 5.1 Sinais adicionais 2024+

- **Trafego natural** do site origem (Ahrefs Estimated Traffic, Semrush Organic Traffic).
- **Diversidade de IP** (links de muitos hosts diferentes).
- **Diversidade de C-class IP** (rede de hospedagem).
- **Idade do dominio origem**.
- **First-link priority** — Google pode considerar primeiro link da pagina (controverso).

---

## 6. Toxic links + Google Spam Policies

### 6.1 O que Google considera link spam (Spam Policies oficiais)

Lista oficial em https://developers.google.com/search/docs/essentials/spam-policies. Categorias:

| Categoria | Detalhe |
|-----------|---------|
| **Buying or selling links** que passam ranking signal | Pagar por link DOFOLLOW e violacao. `rel="sponsored"` obrigatorio em afiliado/patrocinado |
| **Excessive link exchanges** | "Linka pra mim que linko pra voce" em massa |
| **Large-scale article marketing / guest post campaigns** com anchor over-optimized | Guest post 100x com anchor exact-match = manipulacao |
| **Automated programs / services to create links** | Bots, scrapers, spinners |
| **Hidden links** | Texto invisivel, off-screen |
| **Forum signature spam** | Assinaturas com link em massa em forums |
| **Comment spam** | Comments em massa com link |
| **Widgetbait / footerbait** | "Powered by X" em widget de terceiros, em escala massiva |
| **PBN (Private Blog Networks)** | Rede de blogs sob mesmo controle para criar links |

### 6.2 Sinais de site toxico

- Trafego organico ~zero apesar de DR alto.
- Anchor cloud com termos sensiveis (casino, pharma, adult, loans).
- Idioma diferente do nicho.
- Hospedagem em IP-class compartilhado com PBN conhecida.
- Outbound links de saida em massa.
- Conteudo gerado por scraping / spinning.
- Sites em TLDs suspeitos (`.click`, `.top`, `.xyz` em massa).
- Idade do dominio: 2-3 anos com perfil totalmente artificial.

### 6.3 Penalizacoes

| Tipo | Como detectar | Como reverter |
|------|---------------|----------------|
| **Algoritmica** (Penguin / SpamBrain) | Queda silenciosa, sem aviso em GSC | Auditoria, disavow se necessario, conteudo de qualidade, esperar reavaliacao algoritmica |
| **Manual action — Unnatural links to your site** | GSC > Acoes manuais | Auditoria + disavow + Reconsideration Request |
| **Manual action — Unnatural links from your site** | GSC > Acoes manuais | Remover/nofollow os links suspeitos + Reconsideration |

### 6.4 Resposta a penalizacao manual de links

```
RESPOSTA A "UNNATURAL LINKS TO YOUR SITE"
============================================

ETAPA 1 — DOCUMENTAR
  [ ] Print da acao manual em GSC (data, escopo: site-wide ou parcial)
  [ ] Snapshot de trafego organico no momento

ETAPA 2 — AUDITORIA
  [ ] Export todos backlinks (Ahrefs + GSC + Semrush + Majestic — multiplas fontes)
  [ ] Classificar: claramente toxico / suspeito / legitimo
  [ ] Documentar criterio de classificacao

ETAPA 3 — REMOCAO (preferida)
  [ ] Outreach aos webmasters dos links toxicos pedindo remocao OU adicao de nofollow
  [ ] Documentar tentativa (email enviado, data, resposta)
  [ ] Threshold: pelo menos 2-3 tentativas por dominio

ETAPA 4 — DISAVOW (apenas para o que nao foi removido)
  [ ] Arquivo .txt em UTF-8 (Secao 7)
  [ ] Submeter em https://search.google.com/search-console/disavow-links-tool
  [ ] Confirmar submissao

ETAPA 5 — RECONSIDERATION REQUEST
  [ ] Documento explicando: (a) o que aconteceu (causa-raiz),
      (b) tentativas de remocao com evidencia,
      (c) disavow submetido,
      (d) processo para evitar reincidencia
  [ ] Submeter em GSC > Acoes manuais > Solicitar reconsideracao

ETAPA 6 — ESPERA + MONITORAR
  [ ] Resposta: dias a semanas
  [ ] Se rejeitado: documentar feedback, refinar, re-submeter
  [ ] Recovery de trafego: 4-12+ semanas
```

---

## 7. Disavow tool — quando SIM, quando NAO

### 7.1 Quando NAO usar disavow

- **Sem manual action E sem queda significativa de trafego correlacionada a links.**
- Por "limpeza preventiva" de sites desconhecidos/baixa autoridade — **risco de remover sinal valido**.
- Em panico apos core update sem evidencia de que o problema sao links.

> John Mueller (Google) reiterou: "Maioria dos sites nunca precisa de disavow."

### 7.2 Quando usar

- **Manual action — Unnatural links to your site** em GSC.
- **Histórico documentado de link spam** (campanha de SEO black hat em ate ~3 anos passados, vendor de links comprado).
- **Spike repentino** de backlinks de PBN/spam confirmado, sem que tenham desaparecido sozinhos em 90 dias.

### 7.3 Formato do arquivo

```
# Comentarios iniciam com #
# Disavow domain inteiro (preferido para PBN/spam evidente):
domain:exemplo-spam.com
domain:outra-rede-pbn.net

# Disavow URL especifica:
https://exemplo-legitimo.com/post-com-link-suspeito/

# UTF-8, encoding ASCII, sem BOM
# Tamanho maximo: 100k linhas / 2 MiB
```

### 7.4 Submissao

- https://search.google.com/search-console/disavow-links-tool
- Selecionar property
- Upload .txt
- Confirmar

### 7.5 Cuidados

- Disavow e poderoso — pode prejudicar mais que ajudar.
- Sempre **export atual** antes de mudar — para recuperar caso tenha removido sinal valido.
- Evitar disavow de links de Wikipedia, sites grandes legitimos (mesmo "DR baixo segundo a ferramenta").
- **Re-submissao** sobrescreve a anterior — incluir TODOS os disavows ainda validos.

---

## 8. Anchor text distribution

### 8.1 Tipos

| Tipo | Exemplo (URL alvo: /seo-tecnico/) |
|------|--------------------------------|
| **Exact match** | "seo tecnico" |
| **Partial match** | "guia de seo tecnico", "auditoria seo tecnico" |
| **Branded** | "SPKR", "blog SPKR" |
| **Generico** | "leia aqui", "este artigo", "saiba mais" |
| **Naked URL** | "https://dominio.com/seo-tecnico/" |
| **Imagem (alt como anchor)** | imagem clicavel |
| **No-text** (so URL) | raro |
| **Over-optimized exact** | 70%+ exact match — sinal de manipulacao |

### 8.2 Distribuicao natural saudavel (referencia)

| Tipo | % saudavel |
|------|-----------|
| Branded | 30-50% |
| Naked URL | 10-20% |
| Generico | 10-20% |
| Partial match | 15-30% |
| Exact match | 1-5% (max 10%) |
| Imagem | depende (5-15%) |

### 8.3 Anchor cloud — auditoria

Ferramentas:
- Ahrefs > Site Explorer > Anchors.
- Semrush > Backlink Analytics > Anchors.
- Majestic > Anchor Text.

Sinais de manipulacao:
- Exact match > 15-20% para keyword competitiva.
- Multiple exact match anchors apontando para mesma URL (over-optimization).
- Anchor cloud com termos fora do nicho (potencial penalty SEO ou hack).

### 8.4 Quando reescrever anchor

- Manual action por anchor over-optimization -> contatar webmasters para mudar exact -> branded/partial.
- Em campanha futura, focar em branded/partial; deixar exact match emergir naturalmente.

---

## 9. Link velocity

### 9.1 Definicao

Quantidade de novos backlinks adquiridos por unidade de tempo (semana / mes).

### 9.2 Padrao saudavel

- **Crescimento gradual e consistente** ao longo do tempo.
- **Spikes** ocasionais correlacionados a evento explicavel: lancamento de produto, original research, news coverage, conferencia.

### 9.3 Padrao suspeito

- 0 backlinks/mes por 6 meses, depois 200 backlinks em 1 semana, depois 0 — sem explicavel.
- Crescimento exponencial de PBN.
- Espelho do crescimento de concorrente em ate 1-2 dias.

### 9.4 Auditoria

- Ahrefs > Backlink Profile > Backlinks > grafico de aquisicao.
- Semrush > Backlink Analytics > New & Lost.

### 9.5 Aplicacao em estrategia

- Plano de outreach com spread temporal (50 contatos/semana, nao 500/dia).
- Digital PR coordenado com lancamentos / sazonalidade.
- Linkable asset com ciclo de aquisicao prolongado (6-24 meses).

---

## 10. Auditoria de perfil de backlinks — workflow

```
AUDITORIA DE BACKLINK — WORKFLOW
==================================

FASE 1 — COLETA
  [ ] GSC > Links > Top sites linkados > Mais sites linkados
  [ ] Ahrefs > Site Explorer > Backlinks
  [ ] Semrush > Backlink Analytics
  [ ] Majestic > Backlink History
  [ ] Cruzar 3+ fontes (cada ferramenta tem cobertura diferente)

FASE 2 — METRICAS-BASE
  [ ] Total de backlinks
  [ ] Total de referring domains
  [ ] DR/DA/AS atual + historico (ultimos 12-24 meses)
  [ ] Trafego organico estimado
  [ ] Anchor cloud distribution
  [ ] Top 50 backlinks (por DR/UR)
  [ ] Link velocity (mes a mes)

FASE 3 — CLASSIFICACAO
  Cada backlink em uma categoria:
  [ ] Editorial relevante (alvo)
  [ ] Editorial irrelevante (neutro)
  [ ] Diretorio editorial reconhecido (medio)
  [ ] Diretorio generico (baixo)
  [ ] Comentario / UGC (baixo)
  [ ] Forum (baixo)
  [ ] Suspeito de PBN (toxico)
  [ ] Spam confirmado (toxico)
  [ ] Reciproco artificial (cinza)

FASE 4 — TOXIC AUDIT
  [ ] Sites com trafego ~zero + DR alto
  [ ] Anchor cloud sensivel (casino, pharma, adult, loans)
  [ ] Hospedagem em IP-class de PBN
  [ ] Outbound link massivo
  [ ] Conteudo scraped / spun
  [ ] Decision: remocao / nofollow / disavow / aceitar

FASE 5 — COMPETITIVE GAP
  [ ] 3-5 concorrentes diretos
  [ ] Backlinks que concorrente tem e voce nao (link gap)
  [ ] Linkable assets que concorrente publicou
  [ ] Top backlinks de cada concorrente (oportunidades)

FASE 6 — RELATORIO + PLANO
  [ ] Saude geral (saudavel / em risco / penalizado)
  [ ] Acoes urgentes (remocao / disavow / Reconsideration)
  [ ] Plano de aquisicao 90 dias (linkable assets, outreach, digital PR, parcerias)
  [ ] KPIs (referring domains, DR, trafego organico non-branded)
```

---

## 11. Reverse engineering de competidores

### 11.1 Link gap analysis

Identificar **referring domains que linkam para concorrente e NAO para voce**:

- Ahrefs > Link Intersect (>= 2 concorrentes; voce nao).
- Semrush > Backlink Gap.
- Majestic > Compare Domains.

Output: lista de dominios que linkam para 2+ concorrentes -> alta probabilidade de linkar para voce se houver pitch + asset.

### 11.2 Top pages dos concorrentes (linkable assets)

Para cada concorrente:
- Ahrefs > Site Explorer > Top Pages by Backlinks.
- Identificar PADROES: que tipo de conteudo recebeu mais links?
  - Original research?
  - Free tool / calculator?
  - Ultimate guide?
  - Statistics page?
  - Glossario?
  - Free template?

### 11.3 Linkable strategy gap

Se concorrente publicou "Statistics on Marketing Trends 2026" e teve 200 RD, voce pode:
- Replicar com angulo proprio (dado proprio, atualizacao 2027 antecipada, segmentacao por industria).
- Identificar cada um dos 200 sites que linkaram e fazer outreach direto com seu asset.

### 11.4 Anchor profile analysis

Anchor cloud de concorrente revela:
- Que keywords associaram a marca.
- Estrategia de anchor (over-exact-match? branded?).
- Se ha indicios de penalty risk.

---

## 12. Linkable assets — 15+ tipos

Asset = conteudo que **gera backlinks naturalmente** quando promovido. Investimento alto, retorno longo prazo.

### 12.1 Catalogo de tipos

| # | Asset | Por que funciona |
|---|-------|-------------------|
| 1 | **Original research / pesquisa propria** | Dado novo = fonte para jornalistas, blogs, papers |
| 2 | **Survey / data report anual** | "Estado de [X] 2026" — repetir cria expectativa |
| 3 | **Free tool / calculator** | Utilidade pratica + share organico |
| 4 | **Ultimate guide / pillar page** | Profundidade + autoridade tematica |
| 5 | **Statistics page** ("100 estatisticas de marketing 2026") | Recurso citacional para outros artigos |
| 6 | **Free template / boilerplate** | Solucao pratica + share |
| 7 | **Industry report / whitepaper** | Profundidade + autoridade vertical |
| 8 | **Infographic** (com asset visual + dado original) | Visual + share + embeds |
| 9 | **Glossario / dicionario tematico** | Citacional |
| 10 | **Case study com dado real** | Prova social + cobertura |
| 11 | **Comparativo profundo (X vs Y vs Z vs ...)** | Recurso decisivo |
| 12 | **Free course / bootcamp** | Utilidade educacional |
| 13 | **Open-source library / dataset** | Comunidade tecnica |
| 14 | **Award / ranking ("top 50 X de 2026")** | Citacional + ego bait |
| 15 | **Live event / conferencia / podcast** | Cobertura + parceria |
| 16 | **Quiz / assessment** | Interativo + share |
| 17 | **Newsletter premium / community** | Audiencia engajada que compartilha |
| 18 | **Original imagery / photography library** | Reuso (com atribuicao + link) |

### 12.2 Anatomia de um linkable asset

- **Angulo unico** — algo que NAO existe igual no top 10.
- **Dado proprio** — survey, dataset, scraping legitimo, parceria com fonte.
- **Visualizacao** — graficos, tabelas, mapas, calculadora interativa.
- **EEAT alto** — autor, metodologia, fontes, transparencia.
- **Embedable** (`<iframe>` / `<img embed code>`) com link de atribuicao.
- **Quote-friendly** — frases extraiveis, estatisticas-chave destacadas.
- **Atualizacao recorrente** — `dateModified` + ciclo anual.

### 12.3 Promocao do asset

Asset sem promocao = arquivo no servidor. Plano de promocao:

```
1. Pre-launch (1-2 semanas antes)
   - Identificar 50-200 alvos de outreach
   - Press release embargado para journalists chave
   - Avisar parceiros / influencers

2. Launch
   - Post no blog (URL definitiva)
   - Anuncio em LinkedIn, X, Instagram, newsletter
   - Press release publico (com `rel="sponsored"` se pago)
   - Outreach individual (Connectively, journalists)

3. Sustain (1-3 meses pos-launch)
   - Mencao em podcasts (proprio + parceiros)
   - Webinar com dado
   - Citacao em outros artigos do blog
   - Pitch em quote requests
   - Atualizar anualmente
```

---

## 13. Estrategias de aquisicao de backlinks

### 13.1 Skyscraper Technique 2.0 (Brian Dean)

Versao atualizada (skyscraper puro perdeu eficacia pos-Helpful Content):

1. Identificar conteudo concorrente com **muitos backlinks**.
2. Criar versao **claramente superior**: dado novo, expertise direta, formato superior, atualizacao (nao apenas "mais palavras").
3. Outreach aos sites que linkam para original — pitch destacando diferencial concreto.

### 13.2 Broken Link Building

1. Identificar pagina de recursos no nicho com link 404 / 410.
   - `link:dominio-alvo.com` no Google.
   - Ahrefs > Site Explorer > Outgoing > Broken Links.
   - Check My Links (Chrome ext).
2. Outreach ao webmaster: "Notei que voces tem um link 404 em [pagina X]. Aqui esta um substituto atualizado em [seu link]."
3. Funciona melhor com asset realmente substituto (relevancia + qualidade).

### 13.3 Resource Page Link Building

1. Buscar paginas de recursos: `inurl:recursos OR inurl:resources OR inurl:links "[topico]"`.
2. Avaliar relevancia + autoridade.
3. Outreach: "Tenho um recurso que pode complementar — [seu link]. Vale incluir?"
4. Foco em valor real (nao auto-promocao crua).

### 13.4 Guest Posting (com cuidado)

Google Spam Policies cita "large-scale article marketing/guest post campaigns with keyword-rich anchor" como spam. Guest post seguro:

- **Sites realmente relevantes** ao seu nicho.
- **Conteudo unico, expertise propria** — nao spinnado.
- **Anchor** branded OU partial-match (NAO exact-match).
- **Volume moderado** (1-3/mes, nao 30/mes).
- **Bio** com link para perfil pessoal/empresa, nao para money page.
- **EEAT visivel** no perfil.

### 13.5 Unlinked Brand Mention

Mencao da marca sem link -> oportunidade de pedir link.

1. Monitorar mencoes: Google Alerts, Mention.com, Brand24, Talkwalker.
2. Identificar mencoes sem link.
3. Outreach: "Obrigado pela mencao em [artigo]. Seria possivel adicionar link para [URL] para o leitor encontrar mais facil?"
4. Taxa de conversao tipicamente alta (mencao ja confirma interesse editorial).

### 13.6 Podcast Guesting

1. Identificar podcasts no nicho com audiencia engajada.
2. Pitch valor-primeiro: "Posso falar sobre [topico especifico, ineditismo, dado proprio]."
3. Episodio aparece em podcast site + show notes (link).
4. Cross-promocao: cliente promove episodio.
5. Bonus: trafego direto + autoridade EEAT.

### 13.7 Newsjacking

1. Monitorar tendencias: Google Trends, X/Twitter trending, news verticals.
2. Identificar topico emergente onde voce tem expertise.
3. Publicar resposta rapida (24-72h) com dado/angulo proprio.
4. Pitch journalists relevantes via Connectively / email direto.
5. Funciona em janela curta — agilidade > polimento.

### 13.8 HARO / Connectively / Journalist Outreach

**HARO (Help A Reporter Out)** foi descontinuado em 2024 e substituido por **Connectively** (operado pela Cision). Alternativas: **Featured.com**, **Help A B2B Writer**, **Qwoted**, **JournoRequest** (X hashtag), **Source Bottle**.

Workflow:

1. Inscrever-se em multiplas plataformas (broadcast diaria de queries de journalists).
2. Filtrar queries relevantes ao expertise do cliente/autor.
3. Responder rapido (primeiras 30 min apos query e ouro).
4. Pitch em formato journalist-ready: quote pronta + bio + foto profissional + dados verificaveis.
5. Tracking de mencoes/links resultantes.

### 13.9 Image Reverse Search (image link reclamation)

Imagens originais frequentemente sao reusadas sem credito.

1. Reverse image search: Google Images, TinEye.
2. Identificar reuso sem link.
3. Outreach: "Voces estao usando [imagem]. Politica permite com atribuicao linkada — pode adicionar?"
4. Taxa de conversao alta.

### 13.10 Statistics Page link building

Conteudo "100 estatisticas de [topico] 2026" com fontes citadas vira recurso para outros redatores.

- Atualizar anual.
- Citar fonte primaria.
- Permitir embed.
- Pitch journalists e content sites.

### 13.11 Original Research

Survey proprio (Typeform, Google Forms, Tally) com >= 100 respostas qualificadas vira asset citacional. Distribuicao:

- Press release com 3-5 estatisticas-chave.
- Visualizacoes em infograficos / Twitter cards.
- Embed code para sites externos.
- Relatorio PDF gated (lead generation bonus).

### 13.12 Tool / Calculator

Calculadora de [dominio] vira asset de longo prazo. Examples:
- Calculadora de impostos para SaaS.
- Calculadora de CAC/LTV.
- Calculadora de imposto de renda.

Auto-link: usuarios mencionam, journalists citam, blogs incluem em "best free tools".

### 13.13 Comparison link building (B2B SaaS especifico)

- Capterra, G2, GetApp, Software Advice — criar perfil completo.
- Solicitar reviews.
- Update regular.
- Bonus: ranking interno + backlink autoritativo.

### 13.14 Integration partner pages

SaaS X integra com SaaS Y -> X aparece em pagina "Integrations" de Y, e vice-versa.

- Mapear integracoes existentes.
- Solicitar listagem reciproca.
- Criar pagina "[X] + [Y] integration" propria.

### 13.15 .edu / .gov links (com cuidado)

`.edu` / `.gov` / `.org` legitimos = autoridade. Estrategias:

- Scholarship programs (cuidado: practica ja explorada por SEO, alguns marcam como sponsored).
- Curriculum mention (pesquisa academica, parceria com cursos).
- Jornal universitario (pitch jornalistic).
- Citacoes em papers (publicar pesquisa).

NAO pagar por link em `.edu` — viola politicas.

---

## 14. Digital PR — workflow + journalist outreach

### 14.1 Digital PR vs link building tradicional

| Tradicional | Digital PR |
|-------------|------------|
| Outreach a SEOs / bloggers | Outreach a journalists / editors |
| Asset SEO-focado | Story news-worthy |
| KPI = backlinks | KPI = mencoes editoriais + backlinks + brand awareness |
| Volume medio | Volume baixo + alto impacto |
| Anchor descritivo | Anchor branded (e ok) |

### 14.2 Workflow Digital PR

```
DIGITAL PR — WORKFLOW
=======================

1. NEWSWORTHY ANGLE
   [ ] Tendencia atual + dado proprio + expertise = angulo
   [ ] Filtros: e novidade? e surpreendente? e estatistica? e timely?
   [ ] Validar com journalist friend / mentor

2. PRESS KIT
   [ ] Press release ~500 palavras (lead, contexto, dado, quote, sobre, contato)
   [ ] Infografico ou visualizacao
   [ ] Foto profissional do porta-voz
   [ ] Dados em formato facil (tabela, CSV)
   [ ] Pagina dedicada no site com versao publica

3. TARGETING
   [ ] Identificar 30-100 journalists por nicho
   [ ] Beat (vertical), publicacao, frequencia
   [ ] Twitter/LinkedIn handles
   [ ] Email (verificar com Hunter.io, Apollo.io)

4. PITCH
   [ ] Email pitch com subject hook + 3 paragrafos
   [ ] Personalizacao real (artigo recente do journalist)
   [ ] Asset ou dado anexado/linkado
   [ ] Janela embargada se relevante
   [ ] Follow-up em 3-5 dias se sem resposta (1 vez, nao 3)

5. SUSTAIN
   [ ] Trackear mencoes (Mention, Brand24, Google Alerts)
   [ ] Agradecer publicamente em redes
   [ ] Construir relacionamento long-term com journalists
   [ ] Ser fonte para futuros artigos
```

### 14.3 Pitch templates

**Template 1 — Newsjacking**

```
Subject: [Dado original / quote pronta] sobre [topico em alta]

Oi [Nome],

Vi seu artigo sobre [topico] hoje (link). Tenho um dado proprio que pode complementar:

[1 frase com dado-chave + numero].

Fonte: pesquisa propria com [N respondentes / metodologia]. Posso enviar PDF
completo se util.

Se interessar, posso oferecer quote e/ou dados adicionais. Disponivel ate
[hora] hoje para confirmar.

[Assinatura: Nome | Cargo | Empresa | Telefone | Site]
```

**Template 2 — Asset launch**

```
Subject: [Stat surpreendente] — pesquisa de [N] [profissionais/usuarios] sobre [topico]

Oi [Nome],

Saiu hoje pesquisa propria com [N] [profissao] sobre [topico]. Resultado mais
surpreendente:

> [Estatistica chocante em formato quote-ready]

Cobertura completa em [URL]. Quote livre para uso, com atribuicao.

Topicos cobertos:
- [Subtopico 1 + numero]
- [Subtopico 2 + numero]
- [Subtopico 3 + numero]

Se vale para [Publicacao], envio pacote completo em 1h.

[Assinatura]
```

**Template 3 — Resource page outreach**

```
Subject: Recurso atualizado sobre [topico] — para [pagina X]

Oi [Nome],

Encontrei sua pagina de recursos sobre [topico] (link). Ela e referencia.

Notei que [link Y] esta retornando 404. Tenho um recurso atualizado e gratuito
que pode substituir:

[URL] — [breve descricao do que faz]

Se vale, posso enviar mais detalhes.

[Assinatura]
```

---

## 15. Outreach — frameworks operacionais

### 15.1 Email anatomia

```
[Subject — gancho concreto + valor + sem clickbait]

Oi [Primeiro nome],

[Linha 1 — personalizacao real: artigo recente, post no LinkedIn, evento]

[Linha 2 — proposta de valor em 1 frase]

[Linha 3-4 — contexto + asset/dado/oportunidade]

[Linha 5 — pergunta clara / CTA leve]

Sem pressa. Se nao for fit, sem problema.

[Nome]
[Cargo, Empresa, Site, LinkedIn]
```

### 15.2 Personalizacao — sinais reais

- Mencionar artigo especifico do journalist/blogger (com link).
- Comentario substancial sobre tese.
- Conexao mutua relevante.
- Evento que ambos participaram.
- Dado ou recurso especifico para o que eles cobrem.

NAO conta:
- "Adoro seu blog!" (vago).
- "Vi seu site." (banal).
- "[FIRST_NAME], [TOPIC]." (placeholder mal substituido).

### 15.3 Follow-up

- 1 follow-up em 3-5 dias.
- 1 follow-up final em 7-10 dias (opcional, contextualizado).
- Nunca 3+ follow-ups (vira spam).
- Mensagem de follow-up: "Sem pressao — so confirmando que viu" + valor adicional.

### 15.4 Ferramentas de outreach

| Ferramenta | Uso |
|------------|-----|
| **Hunter.io** | Encontrar email a partir de nome + dominio |
| **Apollo.io** | Database + outreach |
| **Snov.io** | Email finder + verificador |
| **Pitchbox** | Outreach SEO/PR especializado |
| **BuzzStream** | Outreach + CRM |
| **Mailshake** | Email sequences |
| **Reply.io** | Multi-channel sequences |
| **Connectively** | HARO sucessor |
| **Featured.com** | Quote requests |
| **Mention / Brand24** | Brand monitoring |
| **Help A B2B Writer** | Quote requests B2B |

### 15.5 Taxa de conversao realista

- Outreach frio cold: 1-5% conversao (link adquirido).
- Outreach com personalizacao real: 10-20%.
- Outreach com relacionamento previo: 30%+.
- HARO/Connectively com pitch rapido: 5-15%.

> **Realidade:** ate 100 outreaches para 5-15 backlinks de qualidade. Volume saudavel = 200-500 outreaches/mes para campanha agressiva, com spread temporal.

---

## 16. Local link building (BR-specific)

### 16.1 NAP consistency

Nome, Endereco, Telefone consistentes em TODAS as plataformas:

- Google Business Profile.
- Bing Places.
- Apple Maps.
- Facebook.
- Instagram.
- LinkedIn (empresa).
- Diretorios BR: ApontaderoOnde, GuiaMais, Yelp, Foursquare, TripAdvisor (se aplicavel).
- Associacoes da cidade / setor.

Inconsistencia = sinal de cuidado de Google.

### 16.2 Citations BR

- Diretorios setoriais (camara de comercio local, sindicatos, ABF, ABRADi).
- Listings locais.
- Reviews (Google, Trustpilot, Reclame Aqui).
- Imprensa local (jornais, blogs de cidade).

### 16.3 Local backlinks tatica

- Patrocinio de evento local (com link em pagina de patrocinadores).
- Doacao a ONG local (com link em "Quem nos apoia").
- Curso ou aula em universidade local (com bio do palestrante).
- Quote em jornal local (newsjacking + pitch).

### 16.4 Google Business Profile

- Perfil 100% completo.
- Posts semanais.
- Reviews + respostas.
- Photos atualizadas.
- Q&A pre-respondidas.

---

## 17. B2B SaaS link building

### 17.1 Comparison sites (autoridade alta + intent comercial)

| Site | Vertical |
|------|----------|
| **G2** | SaaS amplo |
| **Capterra** | SaaS amplo |
| **GetApp** | SaaS amplo |
| **Software Advice** | SaaS amplo |
| **TrustRadius** | B2B enterprise |
| **Product Hunt** | Lancamentos |
| **AlternativeTo** | "alternativa a..." |
| **Slant** | Comparativos detalhados |
| **Crozdesk** | SaaS enterprise |

Estrategia: criar perfil completo + solicitar reviews + responder reviews.

### 17.2 Integration partner pages

- Mapear integracoes existentes (Zapier, Make, native).
- Solicitar listagem em "Integrations" do parceiro.
- Criar pagina "[Seu produto] + [Parceiro]" propria.

### 17.3 Customer case studies (cross-link)

- Cliente publica case usando seu produto.
- Voce publica case sobre cliente.
- Cross-link mutuo.

### 17.4 Industry reports + roundups

- Participar de "State of [X] 2026" com dado proprio.
- Patrocinar industry survey.
- Quote em report de analyst (Gartner, Forrester, IDC — caro).

---

## 18. E-commerce link building

### 18.1 Tatica especifica

- **Cupom / deal sites**: Cuponeria, Mequetrefe, Promobit, Pelando — listagem com link.
- **Influencer affiliate**: micro-influencers com `rel="sponsored"`.
- **Comparativos de produto**: Buscape, Zoom, Reclame Aqui (review).
- **Press de produto**: lancamento + journalist pitch.
- **Sustainability / cause marketing**: parceria ONG.
- **User-generated content campaigns**: hashtag + share + cobertura.

### 18.2 Risco especifico

- E-commerce e nicho saturado de spam (afiliados em massa).
- Anchor "comprar [produto]" exact-match e armadilha — manter branded majority.
- Disclosure obrigatorio em afiliado (CONAR + CDC + Spam Policies).

---

## 19. Internal linking como complemento

> Detalhe completo em `seo-on-page` (Secao 8). Aqui resumo aplicado a link building:

- Hub-and-spoke (pillar -> spokes <-> spokes).
- Autoridade externa entrega -> distribuicao interna importa.
- Quando adquirir backlink para spoke, pillar tambem se beneficia (e vice-versa).

---

## 20. Metricas de sucesso

### 20.1 Operacionais

| Metrica | Onde |
|---------|------|
| **Total de backlinks** | Ahrefs, Semrush, GSC |
| **Referring domains** | Ahrefs, Semrush |
| **DR / DA / AS** | Indice proprietario |
| **Anchor distribution** | Anchor cloud reports |
| **Link velocity** | Grafico de aquisicao |
| **Trafego organico** (proxy de autoridade) | GSC + GA4 |
| **Brand search volume** | Google Trends + GKP |

### 20.2 Estrategicos

| KPI | Como calcular |
|-----|---------------|
| **Trafego organico non-branded** | GSC > Performance > excluir queries marca |
| **Autoridade tematica** | Posicao em multiplas queries do tema |
| **Share of Voice** | Ahrefs SoV / Semrush SoV |
| **Brand search lift** | Trafego de queries marca antes vs depois |
| **Mencoes editoriais** (linked + unlinked) | Mention, Brand24, Google Alerts |
| **Quotes em Connectively / HARO** | Tracking proprio |
| **Co-citacoes em fontes autoritativas** | Manual + audit |

### 20.3 Vaidade vs valor

| Vaidade | Por que e enganoso |
|---------|---------------------|
| DR alto sem trafego organico | Pode ser inflado por links toxicos |
| Total backlinks alto sem RD | Sitewide footer multiplicando 1 dominio = 1 RD |
| Backlink de site grande sem trafego | Site morto perdeu valor |
| Anchor exact-match em massa | Risk Penalty |

---

## 21. Auditoria de link building em 12 fases

```
LINK BUILDING AUDIT — 12 FASES
=================================

FASE 1 — ESTADO ATUAL
  [ ] Total RD, total backlinks, DR/DA/AS
  [ ] Trafego organico estimado vs DR (sanity check)
  [ ] Top 50 backlinks
  [ ] Anchor distribution
  [ ] Link velocity 24 meses

FASE 2 — TOXIC AUDIT
  [ ] Sites suspeitos (Secao 6.2)
  [ ] Anchor anomalo
  [ ] Spike artificial
  [ ] Decisao: remocao / nofollow / disavow / aceitar

FASE 3 — MANUAL ACTION CHECK
  [ ] GSC > Acoes manuais
  [ ] Se sim: Secao 6.4 (resposta a manual action)

FASE 4 — COMPETITIVE GAP
  [ ] 3-5 concorrentes
  [ ] Link Intersect
  [ ] Top pages de cada (linkable assets a inspirar)

FASE 5 — LINKABLE ASSET INVENTORY
  [ ] Que assets ja existem?
  [ ] Quais geraram backlinks?
  [ ] Padrao reaproveitavel?
  [ ] Gaps a produzir

FASE 6 — TARGET LIST
  [ ] Prospects de outreach (priorizado por relevancia + autoridade + trafego)
  [ ] Categorias: editorial, resource page, broken link, brand mention, podcast, guest post, comparison site, integration partner

FASE 7 — DIGITAL PR PLAN
  [ ] Newsworthy angles em 6 meses
  [ ] Press kit
  [ ] Lista de journalists por beat
  [ ] Calendario editorial alinhado

FASE 8 — OUTREACH OPS
  [ ] Email sequences template
  [ ] Ferramentas (Hunter, Pitchbox, Connectively)
  [ ] Cadencia (volume / spread temporal)
  [ ] Tracking de conversao

FASE 9 — INTERNAL ALIGNMENT
  [ ] Internal linking review (autoridade externa precisa redistribuir bem)
  [ ] On-page do destino (linkable asset estruturado)
  [ ] Tecnico: paginas alvo nao tem 4xx/5xx, canonical OK

FASE 10 — KPIs
  [ ] Definir baseline + targets 90/180/365 dias
  [ ] Dashboard de monitoramento

FASE 11 — RISCOS
  [ ] Politica anti-PBN
  [ ] Disclosure obrigatorio em paid/sponsored
  [ ] Spam Policies review
  [ ] Anchor distribution monitorar

FASE 12 — RELATORIO + ROADMAP
  [ ] Saude geral
  [ ] Acoes urgentes (toxic / manual action)
  [ ] Plano 90 dias
  [ ] Plano 12 meses
  [ ] Cadencia de revisao
```

---

## 22. Templates rapidos

### 22.1 Disavow file template

```
# Disavow file for dominio.com
# Last updated: 2026-05-07
# Author: Alexandre Jalkh (alexjalkh@gmail.com)

# PBN identificada
domain:exemplo-pbn-1.com
domain:exemplo-pbn-2.net

# Spam comment site
domain:comment-spam-site.org

# Specific URLs (preserva resto do dominio)
https://site-misto.com/comment-page/?cid=spam-link
```

### 22.2 Outreach tracking sheet

```
| Date | Site origem | DR | Trafego | Pessoa | Email | Data envio | Follow-up 1 | Follow-up 2 | Resposta | Link adquirido | URL alvo | Anchor |
|------|-------------|-----|---------|--------|-------|------------|-------------|-------------|----------|----------------|----------|--------|
```

### 22.3 Linkable asset planning template

```
ASSET: [Nome]
TIPO: [research/tool/guide/statistics/template/...]
DIFERENCIAL UNICO: ...
DADO PROPRIO: ...
PUBLICO ALVO: ...
KW ALVO (cluster seo-keywords): ...
URL ALVO: ...
SCHEMA: Article + (HowTo / Dataset / etc.)

PROMOCAO:
- Pre-launch outreach (50 alvos): [lista]
- Press release embargado: [3 journalists]
- Launch day: blog + LinkedIn + X + newsletter
- Sustain: podcast + webinar + atualizacao 6 meses

KPI:
- Referring domains em 90 dias: [meta]
- Cliques organicos em 12 meses: [meta]
- Brand mentions: [meta]
- Quote pickups: [meta]

CADENCIA:
- Revisao mensal (3 meses)
- Revisao trimestral (6-12 meses)
- Atualizacao anual (apos)
```

---

## 23. Anti-patterns

| Anti-pattern | Por que e problema |
|--------------|---------------------|
| **Comprar backlinks dofollow sem `rel="sponsored"`** | Spam Policies — manual action |
| **PBN proprio ou alugado** | Spam Policies — banimento de longo prazo |
| **Link exchange em massa** ("linka pra mim que linko pra voce") | Spam Policies — penalizacao |
| **Guest post 30x/mes com anchor exact-match** | Spam Policies — penalizacao |
| **Comment spam em forum / blog** | Spam Policies — manual action + dilui marca |
| **Forum signature spam** | Spam Policies |
| **Profile link spam** (criar perfil em 100 forums so para link) | Spam Policies |
| **Disavow agressivo "preventivo" sem evidencia** | Remove sinal valido — perda de trafego |
| **Outreach em massa sem personalizacao** | Taxa baixissima + bloqueio de email + reputacao |
| **HARO/Connectively pitch generico em massa** | Block do journalist |
| **Anchor over-optimization (>15-20% exact)** | Penalizacao |
| **Footer/header sitewide link em massa** | Penalizacao |
| **Comprar reviews falsos para Capterra/G2/Trustpilot** | Banimento da plataforma + risco legal (CDC/CONAR) |
| **Asset "linkable" generico** (= mais um Ultimate Guide sem dado proprio) | NAO gera link — investimento perdido |
| **Disclosure ausente em afiliado/patrocinado** | CONAR + CDC + Spam Policies |
| **Link velocity spike artificial sem evento explicavel** | Sinal de manipulacao — algorithmic penalty |

---

## 24. Regras de Ouro

1. **NAO CHUTAR** — DR/DA/AS sao indices proprietarios, nao verdade. Trafego organico real e KPI mais util.
2. **EEAT antes de outreach** — autor real, credencial, expertise demonstravel. Pitch sem EEAT cai em 0% conversao.
3. **Linkable asset > campanha de outreach generica** — sem asset diferenciado, outreach tem teto baixo.
4. **Anchor distribution natural** — branded majority, exact-match minimo.
5. **Link velocity sustentavel** — spread temporal, sem spikes artificiais.
6. **Spam Policies sao linha vermelha** — PBN, paid sem disclosure, link schemes = banimento.
7. **Disavow e ferramenta de ultimo recurso** — risco de remover sinal valido.
8. **Digital PR > link building tradicional** em horizonte longo — mencoes + links + brand awareness.
9. **Triangular metricas em 2+ ferramentas** — Ahrefs, Semrush, Moz, Majestic.
10. **Reverse engineering de competidor** revela linkable assets que funcionaram comprovadamente.
11. **Outreach com personalizacao real** ou nao faca — taxa cold sem personalizacao e <2%.
12. **HARO sucessor (Connectively + alternativas)** + journalist outreach = melhor ROI por hora investida.
13. **Local link building exige NAP consistency** + GBP completo + diretorios BR.
14. **B2B SaaS: comparison sites + integration pages** sao alvos de alto retorno.
15. **Disclosure obrigatorio** em paid, sponsored, afiliado — CONAR + CDC + Spam Policies.

---

## 25. Exemplos comportamentais — link building

### Exemplo 1 — Cliente quer comprar 100 backlinks rapidamente

**Input:** "Encontrei vendor que oferece 100 backlinks dofollow DR 30+ por R$ 5k. Vale?"

**Resposta esperada:**
> CORRIGE com forca: "Risco extremo de penalizacao manual + perda de tudo que ja foi conquistado. 100 backlinks DR 30+ em 1 lote por R$ 5k indica: (1) PBN proprio do vendor (Spam Policies — banimento); (2) link farm reciproco (Spam Policies — penalty); (3) sites comprados/expirados re-utilizados (mar/2024: 'expired domain abuse'); (4) backlinks em paginas de 'recurso' artificiais. Em todos os cenarios: violacao de Spam Policies > Buying links que passam ranking signal. Resultado provavel em 2-12 meses: queda de trafego 50-90%, recovery em 12-24 meses (e nem sempre). Casos publicos: ja teve site enterprise levar 18 meses para recuperar pos-Penguin classico. Alternativa segura no mesmo budget: (a) R$ 2k em produzir 1 linkable asset (research proprio com survey de 100-300 respondentes); (b) R$ 2k em digital PR (PR especialista por 1-2 meses); (c) R$ 1k em ferramentas (Connectively + Hunter + Mention). Resultado: 5-20 backlinks editoriais reais em 60-90 dias, sustentaveis e sem risco. ROI superior em horizonte de 12+ meses. Se vendor e a unica opcao, recusar — e armadilha."

**Comportamento-chave:** rejeita oferta com base em politica oficial citada, lista cenarios concretos, oferece alternativa equivalente em budget, argumenta com horizonte realista.

### Exemplo 2 — Manual action de "Unnatural links" em GSC

**Input:** "GSC mostra acao manual: 'Links artificiais para o seu site'. Trafego caiu 45%. O que fazer?"

**Resposta esperada:**
> Plano estruturado em 6 etapas (Secao 6.4): "Diagnostico: penalty manual e severo mas reversivel — recovery em 4-12 semanas se executado bem. Etapa 1 — DOCUMENTAR: print da acao manual (data, escopo: site-wide ou parcial). Snapshot de trafego pre-penalty para baseline. Etapa 2 — AUDITORIA: export TODOS backlinks (Ahrefs + Semrush + GSC + Majestic — multiplas fontes; cobertura nao e 100% em ferramenta unica). Classificar como toxico/suspeito/legitimo com criterio documentado. Etapa 3 — REMOCAO: outreach aos webmasters dos toxicos pedindo remocao OU adicao de nofollow. Documentar tentativa (email, data, resposta). Threshold: pelo menos 2-3 tentativas por dominio. Etapa 4 — DISAVOW: arquivo .txt para o que NAO foi removido. NAO disavow links legitimos (mesmo de DR baixo) — risco de over-disavow. Submeter em GSC > Disavow Tool. Etapa 5 — RECONSIDERATION: documento explicando: causa-raiz (vendor antigo? campanha de SEO em 2022?), tentativas de remocao com evidencia, disavow submetido, processo para evitar reincidencia (politica interna anti-PBN). Submeter em GSC. Etapa 6 — ESPERA: dias a semanas para resposta. Se rejeitado: documentar feedback do Google, refinar, re-submeter. Recovery de trafego 4-12 semanas APOS aceitacao. Nao prometer ranking instantaneo — backlinks legitimos ainda precisam reativar autoridade. Plano paralelo: comecar campanha de digital PR limpo durante o periodo de espera para construir nova autoridade."

**Comportamento-chave:** estrutura em 6 etapas claras, cita politica especifica, alerta sobre over-disavow, alinha expectativa de recovery, propoe acao paralela.

### Exemplo 3 — Site novo sem autoridade

**Input:** "Cliente novo, dominio com 6 meses, DR 8, 12 referring domains. Como construir autoridade do zero?"

**Resposta esperada:**
> Plano de 12 meses em 4 fases: "Site novo segue jornada DR 0-20 (fundacao) -> 20-40 (momentum) -> 40-60 (digital PR scale). Plano em 4 fases. **FASE 1 — FUNDACAO (mes 1-3, alvo DR 15-25):** (a) Citations basicas: GBP, Bing Places, Apple Maps, diretorios setoriais BR (camara de comercio, sindicato, associacoes); (b) Social profiles: LinkedIn empresa, Twitter, Instagram, YouTube, Pinterest — todos com link no perfil; (c) Schema.org Organization + Person com sameAs apontando para todos os perfis sociais + Wikidata (criar entidade se possivel); (d) 1-2 podcast guesting/mes com expertise direta; (e) HARO/Connectively cadastrado — pitch diario aos primeiros 30 dias. **FASE 2 — LINKABLE ASSET (mes 4-6, alvo DR 25-35):** produzir 1 asset diferenciado: research proprio com 100-300 respondentes + relatorio publico + press kit. Promocao: outreach a 100 journalists no nicho + 200 bloggers via Connectively + Hunter. Meta: 30-60 RD em 90 dias pos-launch. **FASE 3 — DIGITAL PR (mes 7-9, alvo DR 35-45):** newsjacking semanal alinhado com tendencias do setor (Google Trends + X trending). Quote em jornais setoriais. Podcast guesting expandido (1/semana). 1 asset adicional (free tool / calculator). Meta: cobertura editorial em 5-10 publicacoes do nicho. **FASE 4 — SCALE (mes 10-12, alvo DR 45-55):** parceria com analyst (G2 review, Capterra perfil completo se SaaS), conferencia speaking, integration partner pages, customer case studies cross-promovidos. KPI ao final dos 12 meses: 100-300 RD, DR 45-55, trafego organico non-branded crescente, 5-10 mencoes editoriais. Realista? Sim, com investimento de R$ 8-15k/mes em conteudo + outreach + ferramentas. NAO comprar atalhos."

**Comportamento-chave:** quebra em 4 fases com KPIs progressivos, lista taticas concretas por fase, alinha investimento e horizonte temporal, alerta contra atalhos.

### Exemplo 4 — Disavow agressivo sem evidencia

**Input:** "Auditoria mostrou 5000 backlinks de DR baixo (<10). Vou disavow tudo para limpar o perfil. OK?"

**Resposta esperada:**
> CORRIGE: "Disavow agressivo SEM evidencia clara de manual action ou problema correlacionado e anti-pattern. John Mueller (Google) reiterou em multiplas declaracoes: 'Maioria dos sites nunca precisa de disavow.' DR baixo nao = toxico. Sites de DR <10 incluem: blogs pessoais legitimos, paginas locais, projetos open-source, recursos academicos pequenos, novos sites. Disavow em massa pode REMOVER sinais validos -> queda de autoridade nao-recuperavel facilmente. Procedimento correto: (1) Verificar GSC > Acoes manuais — ha penalty? Se NAO -> nao precisa disavow. (2) Verificar trafego organico — caiu correlacionado a alguma data ou update? Se NAO -> provavelmente nao e link issue. (3) Auditoria toxic com criterios objetivos (Secao 6.2): trafego ~zero + DR alto, anchor sensivel, IP-class de PBN, outbound massivo. APENAS sites que atendem 2+ criterios sao candidatos a disavow. (4) Para os candidatos: tentar remocao primeiro (outreach), disavow apenas se nao remover. Numero realista: 5000 backlinks raramente tem 5000 toxicos. Audit cuidadoso tipicamente identifica 50-300. Recomendacao: PARAR o disavow agressivo, fazer audit objetivo, re-avaliar com criterios concretos, e apenas disavow o que falhar em 2+ criterios objetivos. Investir o tempo poupado em construcao de novos backlinks legitimos (digital PR + linkable asset)."

**Comportamento-chave:** rejeita acao baseada em DR puro, cita declaracao oficial, oferece criterios objetivos, propoe priorizacao alternativa do tempo investido.

---

## 26. Checklist de Contraditorio Interno — link building

| # | Pergunta destruidora | O que busca |
|---|----------------------|-------------|
| 1 | **Toxic link audit** foi feito com criterios objetivos (Secao 6.2), ou e julgamento subjetivo de "DR baixo"? | Audit objetivo |
| 2 | DR/DA/AS foram **cruzados com trafego organico estimado** do site origem? Sites de DR alto sem trafego sao armadilha | Sanidade dos indices |
| 3 | **Anchor distribution** esta natural (branded majority, exact-match <= 5%)? Anchor cloud foi auditada? | Anti-over-optimization |
| 4 | **Link velocity** e sustentavel ou planejada com spike artificial sem evento explicavel? | Anti-spike artificial |
| 5 | **Disavow** sera usado APENAS em manual action confirmada OU evidencia clara de PBN/spam, NAO preventivamente? | Disavow conservador |
| 6 | **Conteudo/asset** tem diferenciacao real (dado proprio, expertise direta, formato superior), ou e mais um Ultimate Guide generico? | Linkable asset real |
| 7 | **Outreach** tem personalizacao real (artigo recente, conexao mutua), ou e template em massa? | Anti-spam outreach |
| 8 | **Concorrente** foi reverse-engineered (Link Intersect + top pages by backlinks)? Linkable patterns identificados? | Competitive intelligence |
| 9 | **KPIs** medem negocio (trafego organico non-branded, conversao, brand search lift), ou apenas vaidade (DR, total backlinks)? | KPI de negocio |
| 10 | **Helpful Content + Spam Policies** revisados antes da campanha? Plano respeita ambos? | Compliance Google |

---

## 27. Referencias canonicas

### 27.1 Oficiais Google

- **Google Search Central** — https://developers.google.com/search
- **Spam Policies** — https://developers.google.com/search/docs/essentials/spam-policies
- **Link best practices** — https://developers.google.com/search/docs/crawling-indexing/links-crawlable
- **Disavow links tool** — https://search.google.com/search-console/disavow-links-tool
- **Google Search Liaison (X/Twitter)** — atualizacoes informais

### 27.2 Bing / Microsoft

- **Bing Webmaster Guidelines** — https://www.bing.com/webmasters/help/webmasters-guidelines-30fba23a

### 27.3 Plataformas de outreach / quote requests

- **Connectively** (sucessor do HARO) — https://www.connectively.us
- **Featured.com** — https://featured.com
- **Help A B2B Writer** — https://www.helpab2bwriter.com
- **Qwoted** — https://www.qwoted.com
- **Source Bottle** — https://www.sourcebottle.com
- **JournoRequest** (X hashtag) — https://x.com/hashtag/JournoRequest

### 27.4 Ferramentas de outreach

- Hunter.io — https://hunter.io
- Apollo.io — https://www.apollo.io
- Snov.io — https://snov.io
- Pitchbox — https://pitchbox.com
- BuzzStream — https://www.buzzstream.com
- Mailshake — https://mailshake.com
- Reply.io — https://reply.io

### 27.5 Ferramentas de backlink analysis

- Ahrefs — https://ahrefs.com
- Semrush — https://www.semrush.com
- Majestic — https://majestic.com
- Moz Pro — https://moz.com/pro
- LinkResearchTools — https://www.linkresearchtools.com
- Mention — https://mention.com
- Brand24 — https://brand24.com

### 27.6 Bibliografia profissional

- **Ahrefs Blog — Link Building** — https://ahrefs.com/blog/link-building/
- **Semrush Blog — Link Building** — https://www.semrush.com/blog/link-building/
- **Moz — Beginner's Guide to Link Building** — https://moz.com/learn/seo/link-building
- **Backlinko (Brian Dean)** — Skyscraper, Link Building Guide
- **Authority Hacker** — link building cursos
- **Search Engine Journal** — link building column
- **Search Engine Land** — link building column
- **Lily Ray (Amsive)** — EEAT + autoridade
- **Glenn Gabe (G-Squared)** — algorithm + links analysis
- **Marie Haynes** — newsletters de updates
- **Aleyda Solis (Crawling Mondays)** — link building tecnico

### 27.7 B2B / SaaS specific

- G2 — https://www.g2.com
- Capterra — https://www.capterra.com
- GetApp — https://www.getapp.com
- Software Advice — https://www.softwareadvice.com
- TrustRadius — https://www.trustradius.com
- Product Hunt — https://www.producthunt.com
- AlternativeTo — https://alternativeto.net

### 27.8 Brasil

- **CONAR** — https://www.conar.org.br
- **CDC (Lei 8.078/1990)** — http://www.planalto.gov.br/ccivil_03/leis/l8078compilado.htm
- **LGPD (Lei 13.709/2018)** — http://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm
- **IAB Brasil** — https://iabbrasil.com.br

---

## 28. Referencia cruzada de skills

| Situacao | Skills relacionadas |
|----------|----------------------|
| Plano de autoridade | `seo-fundamentos` + `seo-link-building` + `seo-keywords` |
| Auditoria de backlinks | `seo-link-building` + `analise-concorrencia` |
| Recovery pos-manual-action | `seo-link-building` (Secao 6.4) + `seo-tecnico` |
| Linkable asset (research proprio) | `seo-link-building` + `pesquisa-quantitativa` + `seo-on-page` (estrutura) |
| Digital PR | `seo-link-building` (Secao 14) + `comunicacao-corporativa` + `comunicacao-crise` |
| HARO / Connectively pitch | `seo-link-building` + `copywriting-conversao` |
| Local link building | `seo-link-building` (Secao 16) + `seo-keywords` (local) + `seo-on-page` (16.7 local page) |
| B2B SaaS | `seo-link-building` (Secao 17) + `analise-concorrencia` |
| E-commerce link | `seo-link-building` (Secao 18) + `seo-on-page` (16.6 product) + `conhecimento-conar-cdc` |
| Migracao + preservar autoridade | `seo-link-building` + `seo-tecnico` (17 migration) |
| Disclosure de afiliado/patrocinado | `seo-link-building` + `conhecimento-conar-cdc` |

---

## 29. Integracao com o ecossistema Frank-MKT

Esta skill integra-se ao agente principal `frank-mkt` (`agents/frank-mkt.md`) e ao restante do plugin da seguinte forma:

- **Pre-requisito: `seo-fundamentos`** — modelo mental + Spam Policies + Helpful Content + EEAT. Sem isso, link building vira tatica isolada com risco de penalizacao site-wide.
- **Acoplamento com `seo-keywords`** — KW alvo de campanha (money keyword, defensiva, supporting) define a URL alvo do backlink. Anchor text alinhado com cluster topical de `seo-keywords`.
- **Acoplamento com `seo-on-page`** — linkable asset precisa ser bem estruturado on-page (TL;DR, schema, EEAT, internal linking, hierarquia). Asset tecnicamente impecavel converte mais outreach em link.
- **Acoplamento com `seo-tecnico`** — saude tecnica preserva autoridade adquirida. Migracao mal feita evapora link equity (Secao 17 de `seo-tecnico`).
- **Acoplamento com `conteudo-evergreen`** — atualizacao recorrente de linkable asset (statistics page, ultimate guide, original research anual) mantem autoridade entrando ao longo do tempo.
- **Acoplamento com `analise-concorrencia`** — reverse engineering de competidores (Secao 11) e cruzamento de dominio. Concorrente identificado em `analise-concorrencia` e benchmarked em link gap aqui.
- **Acoplamento com `comunicacao-corporativa` e `comunicacao-crise`** — digital PR e crise envolvem outreach a journalists. Esta skill instrui tatica; aquelas instruem voz e narrativa institucional.
- **Acoplamento com `copywriting-conversao`** — pitch de outreach, asset content, press release sao copy. Esta skill define ESTRUTURA + slots; copywriter enche com texto persuasivo.
- **Acoplamento com `pesquisa-quantitativa`** — original research (asset principal) requer metodologia rigorosa: amostra, intervalo de confianca, vies. Aquela skill instrui mecanica.
- **Acoplamento com o agente `auditor`** — auditor roda regras PASS/FAIL em campanha de link building (anchor distribution? velocity sustentavel? disclosure em paid? toxic audit?). Esta skill fornece o framework.
- **Acoplamento com o agente `seo-strategist`** — agente especialista orquestra esta skill em planos de aquisicao de longo prazo (12-24 meses).
- **Acoplamento com `conhecimento-conar-cdc`** — disclosure obrigatorio em paid/sponsored/afiliado e regulado por CONAR + CDC. Cruzamento obrigatorio.
- **Acoplamento com `compliance-lgpd`** (plugin juridico) — outreach via email tipicamente OK (legitimo interesse B2B); cuidado com PII em listas compradas.
- **Memoria e rastreabilidade** — auditorias de backlinks, listas de outreach, tracking de campanha, KPIs sao persistidos em `.frank-mkt/seo/<cliente>/<data>/link-building/` pelo agente `suporte-documental` (a criar) ou diretamente pelo `frank-mkt`. Versionar para revisar evolucao temporal e impacto de core updates.
- **Contraditorio interno** — o agente principal aciona o modulo `contraditorio-interno` carregando o Checklist da Secao 26 desta skill antes de entregar plano de link building, recomendacao de disavow, ou pitch de digital PR.
- **Decaimento temporal** — esta skill esta em volatility `medium` (6 meses). Re-grounding obrigatorio em fontes da Secao 27 antes de citar fato volatil (mudanca de Spam Policies, descontinuacao de plataforma como HARO em 2024, novos rich result types) em peca formal.
- **Regra de ouro para `frank-mkt`** — nenhuma campanha de link building, decisao de disavow, plano de digital PR, ou compra de "link service" sai do plugin sem passar por esta skill. Custos de erro sao altos: penalty manual, recovery em 12+ meses, autoridade volatilizada.

---

> **Aviso:** o plugin `frank-mkt` e um assistente de analise. Recomendacoes desta skill devem ser adaptadas ao nicho, autoridade atual, mercado, recurso disponivel, e validadas em ferramenta + GSC + crawler antes de aplicar em peca formal. Link building e disciplina sensivel a politicas Google — Spam Policies sao atualizadas; HARO descontinuou em 2024; ferramentas de outreach evoluem. Re-validar antes de citar.

---

*Plugin `frank-mkt` — skill `seo-link-building` (v0.1.0)*
*Ultima atualizacao: 2026-05-07*
