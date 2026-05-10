---
name: conteudo-evergreen
description: "Gestao de conteudo evergreen e ciclo de vida operacional. Filosofia evergreen vs trending, decay temporal por tipo de conteudo, content lifecycle (planning -> producao -> publicacao -> atualizacao -> consolidacao/pruning -> arquivamento), content audit metodologico, content pruning (quando deletar/consolidar/redirecionar), content consolidation (merging + canonical), refresh strategy (quando, o que, sinal dateModified honesto), atualizacao programada (calendario de revisao por tipo), topical authority sistematica, hub-and-spoke maintenance, internal linking dinamico apos cada publicacao, AI Overview / SGE preparation, HCS-proofing pos-update, programmatic SEO etico vs scaled content abuse (mar/2024), conteudo sazonal coordenado, republishing strategy, distribuicao evergreen (newsletter recap, social recycling), metricas (life value por tipo, decay rate, refresh ROI, content health score), auditoria 12 fases, templates."
user-invocable: false
last_verified: 2026-05-07
next_review: 2026-11-07
volatility: medium
regrounding_sources:
  - "https://developers.google.com/search"
  - "https://developers.google.com/search/docs/fundamentals/creating-helpful-content"
  - "https://developers.google.com/search/blog/2022/08/helpful-content-update"
  - "https://developers.google.com/search/docs/essentials/spam-policies"
  - "https://search.google.com/search-console"
  - "https://ahrefs.com/blog/content-audit/"
  - "https://www.semrush.com/blog/content-audit/"
  - "https://moz.com/learn/seo/on-site-seo"
---

# Skill: conteudo-evergreen

> **Decaimento Temporal**
> Ultima verificacao: 2026-05-07 | Proxima revisao: 2026-11-07 | Volatility: **medium** (6 meses)
> Helpful Content System foi incorporado ao core algorithm em mar/2024; politicas anti-scaled-content foram atualizadas em mar/2024 (scaled content abuse, expired domain abuse, site reputation abuse). AI Overviews mudaram dinamica de evergreen vs trending. Re-validar antes de publicar peca formal:
> - Google Search Central — Creating helpful content — https://developers.google.com/search/docs/fundamentals/creating-helpful-content
> - Google Search Central Blog (Helpful Content updates) — https://developers.google.com/search/blog
> - Google Spam Policies (scaled content) — https://developers.google.com/search/docs/essentials/spam-policies
> - Search Status Dashboard — https://status.search.google.com
> - Google Search Liaison (X/Twitter) — atualizacoes informais
>
> **Acionamento:** plano de conteudo, content audit, content pruning, refresh de conteudo antigo, hub-and-spoke maintenance, topical authority, calendario editorial evergreen + sazonal, decay de trafego, AI Overview adaptation, programmatic SEO etico, scaling com IA sem virar scaled content abuse.
> **Skills relacionadas:** `seo-fundamentos` (carrega ANTES desta), `seo-keywords` (KW + cluster), `seo-on-page` (anatomia de pillar/cluster — Secao 16 daquela), `seo-tecnico` (sitemap + lastmod + canonical em consolidacao), `seo-link-building` (linkable asset evergreen), `copywriting-conversao` (refresh de copy), `manutencao-skills` (modelo de decaimento aplicado), `conhecimento-search-console` (medicao), `conhecimento-ga4` (conversao por idade do conteudo).
> **Pre-requisito:** ter carregado `seo-fundamentos` (HCS, EEAT, Spam Policies, AI Overview) + `seo-keywords` (cluster) + `seo-on-page` (anatomia de pagina). Esta skill operacionaliza ciclo de vida.

---

## 1. Visao Geral

Conteudo evergreen e conteudo que **mantem relevancia ao longo do tempo** com manutencao moderada — vs conteudo trending que pico e cai. Esta skill foca o **operacional**: decisao de publicar, atualizar, consolidar, ou aposentar; calendario de revisao; auditoria de inventario; pruning de baixo desempenho; topical authority sistematica; HCS-proofing.

Nao repete:
- **Anatomia** de pillar/cluster/listicle/howto/etc. -> `seo-on-page` Secao 16.
- **Cluster topical** definicao -> `seo-keywords` Secao 9.
- **EEAT** -> `seo-fundamentos` Secao 6.
- **HCS** -> `seo-fundamentos` Secao 7.

Aqui aprofunda:

- **Filosofia evergreen vs trending** — quando cada faz sentido.
- **Decay temporal por tipo** — vida util esperada por categoria.
- **Content lifecycle** — 6 estagios.
- **Content audit metodologico** com matriz Esforco x Impacto.
- **Pruning** — quando deletar (404/410), consolidar (301), ou refresh.
- **Consolidation** — merge de URLs canibalizando.
- **Refresh strategy** — `dateModified` honesto vs cosmético.
- **Atualizacao programada** — calendario por tipo.
- **Topical authority sistematica** — cobertura horizontal + vertical.
- **Hub-and-spoke maintenance** — cluster nao para de evoluir.
- **Internal linking dinamico** — atualizar apos cada nova publicacao.
- **AI Overview / SGE preparation** — adaptar conteudo para citacao.
- **HCS-proofing** — sobreviver a Helpful Content System.
- **Programmatic SEO etico** vs scaled content abuse.
- **Sazonal vs evergreen** — calendario coordenado.
- **Republishing** — nova URL ou mesma URL com refresh.
- **Distribuicao evergreen** — newsletter, social, video.
- **Metricas** — life value, decay rate, refresh ROI, content health score.
- **12 fases de auditoria + templates**.

### 1.1 Acionamento — quando esta skill carrega

| Gatilho | Exemplo |
|---------|---------|
| Plano de conteudo | "calendario editorial 6 meses" |
| Content audit | "tenho 800 posts publicados em 5 anos, ajudar a organizar" |
| Drop em conteudo | "post de 2022 tinha 5k visitas/mes, hoje 800" |
| Pruning | "vale deletar 200 posts antigos sem trafego?" |
| Consolidation | "tenho 6 paginas sobre `crm para startup` competindo" |
| Refresh sistematico | "como manter pillar `seo` sempre atualizado?" |
| Topical authority | "cobrir nicho fintech do zero — por onde comecar?" |
| AI Overview | "aparecemos em AI Overview ano passado, hoje saimos" |
| Programmatic | "queremos gerar 5k paginas de produto — risco?" |
| Sazonal | "calendario IRPF 2026 + evergreen normal" |
| Republishing | "republicar post de 2021 com nova URL ou refresh?" |

### 1.2 Pre-requisitos

- [ ] **`seo-fundamentos` + `seo-keywords` + `seo-on-page` carregadas**.
- [ ] **GSC + GA4** para medir performance por URL.
- [ ] **Inventario completo de URLs** (CMS export, sitemap, ou crawl).
- [ ] **Categorizacao por tipo de conteudo** (pillar, cluster, blog, glossario, listicle, howto, etc.).
- [ ] **Topical map** — clusters do site mapeados.
- [ ] **Politica editorial** — voz, tom, autores.
- [ ] **Acesso ao CMS** para deletar, redirecionar, consolidar.

> **Cristal C0 — NAO CHUTAR.** Decisao de pruning/refresh requer dado: trafego organico, conversao, backlinks, posicao. Sem GSC + GA4 + ferramenta de backlink, nao decidir.

---

## 2. Filosofia evergreen vs trending

### 2.1 Definicoes

| Tipo | Vida util | Caracteristica | Exemplo |
|------|-----------|-----------------|---------|
| **Evergreen** | 12-60+ meses | Topico estavel; intent perene | "O que e CRM" |
| **Pseudo-evergreen** | 6-18 meses | Topico estavel + ano no titulo | "Melhor CRM em 2026" |
| **Seasonal** | Pico ciclico anual | Topico recorrente | "IRPF 2026" |
| **Trending** | Dias-semanas | Topico volatil ou newsy | "Novo update do Algoritmo X" |
| **News** | Horas-dias | Notitia pura | "Google anunciou hoje..." |

### 2.2 Mix recomendado

Para a maioria dos sites B2B / B2C:

| Tipo | % do volume publicado |
|------|------------------------|
| **Evergreen + pseudo-evergreen** | 70-85% |
| **Seasonal** | 5-15% |
| **Trending** | 5-15% |
| **News** | 0-10% (apenas se publisher) |

Evergreen e a base; trending da pico; seasonal pega janelas previsiveis.

### 2.3 ROI por tipo

| Tipo | ROI imediato | ROI longo prazo | Manutencao |
|------|--------------|------------------|------------|
| Evergreen | Baixo (3-9 meses para rankear) | Alto (anos) | Anual |
| Pseudo-evergreen | Medio | Medio (atualizar ano) | Anual |
| Seasonal | Alto no pico | Recorrente | Anual antes do ciclo |
| Trending | Alto curto | Baixo | Nenhuma |
| News | Alto curtissimo | Quase zero | Nenhuma |

### 2.4 AI Overview muda calculo

Em 2026, Google AI Overviews + LLM-search mudam dinamica:

- **Evergreen informacional simples** (como "o que e X") tem **mais zero-click** -> ROI direto cai, mas conteudo eh **citado em AI Overview** (autoridade reflexa).
- **Trending** ainda tem CTR forte (Google AI Overview menos confiavel em topico fresh).
- **Seasonal** depende: financeiro/saude/regulado tem AI Overview pesado; lifestyle/viagem tem menos.

Implicacao: evergreen continua valendo, mas tracking precisa medir **citacao em AI Overview** (Profound, Authoritas), nao so cliques.

---

## 3. Decay temporal de conteudo — vida util por tipo

Conceito: todo conteudo decai (HCS reavalia continuamente; concorrencia atualiza; intent muda; AI Overview entra). Vida util **antes do decay relevante** varia por tipo:

| Categoria de conteudo | Vida util sem refresh | Decay rate (apos vida util) | Volatility |
|------------------------|------------------------|------------------------------|------------|
| **Definitional / glossario** ("o que e X") | 24-60 meses | Lento | very-low |
| **How-to fundamental** ("como configurar Y") | 6-24 meses | Medio | medium-low |
| **How-to com produto / interface** ("como usar GA4") | 3-12 meses | Rapido | medium |
| **Comparativo (X vs Y)** | 6-12 meses | Rapido (preco, features mudam) | medium |
| **Listicle / "melhores"** | 6-12 meses | Rapido (ranking muda) | medium |
| **Statistics page** | 6-12 meses (atualizar ano) | Medio | medium |
| **Original research** | 12-24 meses (re-survey opcional) | Lento se referenciada | medium-low |
| **Ultimate guide / pillar** | 12-24 meses (refresh anual) | Medio | medium |
| **News / opinion editorial** | Dias-semanas | Brutal | high |
| **Tutorial de plataforma** | 3-12 meses | Rapido (UI muda) | medium-high |
| **Regulatorio / compliance** ("LGPD em 2026") | 3-12 meses (lei muda) | Medio-rapido | medium-high |
| **Receita / how-to manual** | 24-60 meses | Lento | very-low |
| **Tendencia setorial** ("futuro do X") | 6-18 meses | Medio | medium |
| **Calculadora / tool** | 12-24 meses (logica + dados de referencia) | Lento | low |

### 3.1 Sinais de decay

- **Trafego organico cai** sem core update favoravel a outros.
- **Posicao perde** progressivamente.
- **CTR cai** (snippet/title nao acompanha SERP atual).
- **PAA muda** e conteudo nao cobre.
- **AI Overview** passa a citar concorrente.
- **Backlinks param de chegar** (se asset).
- **Conversao cai** (intent mudou).

### 3.2 Calendario de revisao recomendado

```
Volatility very-low     -> revisao a cada 24 meses
Volatility low          -> revisao a cada 12 meses
Volatility medium-low   -> revisao a cada 9 meses
Volatility medium       -> revisao a cada 6 meses
Volatility medium-high  -> revisao a cada 3-4 meses
Volatility high         -> revisao a cada 1-2 meses (ou aposentar)
```

Aplicar tag `next_review` no CMS / planilha (analogo ao frontmatter YAML das skills do plugin).

---

## 4. Content lifecycle — 6 estagios

```
[1. PLANNING] -> [2. PRODUCAO] -> [3. PUBLICACAO] -> [4. PROMOCAO] -> [5. MANUTENCAO] -> [6. ARQUIVAMENTO]
                                                                          |
                                                                          +---> RE-FRESH (volta a 5)
                                                                          +---> CONSOLIDACAO (merge + 301)
                                                                          +---> PRUNING (delete + 410 ou 404)
```

### 4.1 Planning

- Definir KW + intent + sub-queries (output de `seo-keywords`).
- Decidir tipo (pillar/cluster/listicle/...).
- Decidir autor (EEAT).
- Decidir schema (output de `seo-on-page`).
- Decidir cluster + URL alvo.
- Decidir KPI (posicao, trafego, conversao).
- Decidir vida util esperada + cadencia de revisao.

### 4.2 Producao

- Brief SERP-first.
- Redacao com expertise / dado / experiencia direta (HCS-proof).
- Imagens originais.
- Schema valido.
- EEAT visivel.
- Internal linking plan.

### 4.3 Publicacao

- Slug correto.
- Schema validado em Schema Markup Validator + Rich Results Test.
- Submeter no GSC > URL Inspection > Solicitar indexacao.
- Adicionar ao sitemap.
- Internal links de saida e entrada.
- OG + Twitter Cards verificados.

### 4.4 Promocao

- LinkedIn + X + Instagram + Facebook (formato adaptado por canal).
- Newsletter.
- Outreach (se asset linkable).
- Atualizar pagina relacionada com link.

### 4.5 Manutencao

- Monitorar GSC + GA4 nos primeiros 30/60/90 dias.
- Refresh conforme calendario por tipo (Secao 3.2).
- Atualizar internal linking apos novas publicacoes do cluster.
- Re-grounding em fonte oficial em conteudo regulado.

### 4.6 Arquivamento

Quando vida util encerrou e refresh nao compensa:
- **Pruning**: deletar (410 preferido sobre 404 — sinal mais forte).
- **Consolidation**: 301 para destino superior.
- **Noindex** (raro — apenas se URL precisa existir mas nao deve indexar).

---

## 5. Content audit metodologico

### 5.1 Inventario

Coletar para cada URL:

| Campo | Fonte |
|-------|-------|
| URL | Sitemap / CMS / crawl |
| Titulo | Crawl |
| H1 | Crawl |
| Tipo | Manual / categoria CMS |
| Cluster | Manual (topical map) |
| Data publicacao | CMS / schema datePublished |
| Data ultima atualizacao | CMS / schema dateModified |
| Autor | CMS / schema |
| Status indexacao | GSC > URL Inspection (em massa via API) |
| Impressoes 90d | GSC |
| Cliques 90d | GSC |
| CTR | GSC |
| Posicao media | GSC |
| Sessoes organicas 90d | GA4 |
| Conversoes 90d | GA4 |
| Backlinks (RD) | Ahrefs / Semrush |
| KW principal posicao | Ahrefs / Semrush |
| AI Overview citation | Profound / Authoritas |

### 5.2 Categorizar por performance

| Categoria | Criterio | Acao |
|-----------|----------|------|
| **TOP** | Trafego alto + conversao + posicao top 5 | Manter + refresh por calendario |
| **GROWING** | Trafego subindo + posicao 6-15 | Quick win — refresh + interna |
| **PLATEAU** | Trafego estavel mas baixo | Avaliar potencial — refresh aprofundado OU consolidar |
| **DECLINING** | Trafego caindo > 30% em 6 meses | Diagnostico (HCS? intent? concorrencia?) -> refresh OU consolidar OU prune |
| **UNDERPERFORMER** | Trafego baixo + posicao > 30 | Avaliar topical relevance — consolidar OU prune |
| **ZERO** | Trafego ~ 0 + 0 backlinks + sem conversao | Prune (delete + 410 OU 301) |

### 5.3 Categorizar por intent x estagio do funil

Cruzar com matriz de `seo-keywords` (Secao 2.3):

```
                    TOFU            MOFU            BOFU            POS-VENDA
Definicional     [URLs lista]      —               —               —
Comparativo      —              [URLs lista]       —               —
Transacional     —                 —             [URLs lista]      —
Suporte          —                 —               —             [URLs lista]
```

Identificar gaps + over-coverage.

### 5.4 Matriz Esforco x Impacto

```
                  IMPACTO BAIXO     IMPACTO ALTO
ESFORCO BAIXO   [Quick wins]      [TOP priority]
                Rebuild snippet,    Refresh + interna,
                fix typo,           schema rico,
                sub-titulo          autor visivel
                
ESFORCO ALTO    [Avaliar prune]   [Major rewrite]
                Conteudo morto,    Pillar full refresh,
                consolidar         original research,
                                   asset linkable
```

---

## 6. Content pruning

### 6.1 Quando aplicar

Pruning = remover conteudo nao-util do site para que Google reavalie qualidade media. Helpful Content System rebaixa **site inteiro** quando ha muito thin/scaled.

Candidatos a pruning:

| Sinal | Threshold tipico |
|-------|-------------------|
| Trafego organico nos ultimos 12 meses | < 5 sessoes |
| Backlinks externos (RD) | 0 |
| Conversao | 0 |
| Posicao media | > 30 |
| Cobertura GSC | "Rastreada nao indexada" / "Detectada nao indexada" >= 6 meses |
| Topical relevance | Fora do foco do site |
| Helpful Content self-assessment | Falha em 3+ criterios |
| Idade desde ultima atualizacao | > vida util do tipo |

### 6.2 Decisao: deletar / consolidar / refresh

```
Para cada candidato a pruning:

1. Tem backlinks externos? (RD > 0)
   SIM: NUNCA deletar com 404. Considerar 301 para destino relevante.
   NAO: prosseguir.

2. Conteudo e topicamente relevante ao site?
   SIM: avaliar refresh aprofundado (rewrite + EEAT + dado novo).
        Se refresh nao se justifica, consolidar com pagina existente do cluster.
   NAO: deletar com 410 (preferido) ou 301 para categoria mae.

3. Pagina foi linkada em paginas-chave do site?
   SIM: atualizar internal links antes de deletar/redirecionar.

4. Pagina aparece em sitemap?
   SIM: remover do sitemap antes (ou contemporaneo) da acao.

5. Pagina tinha trafego significativo no passado?
   SIM: 301 para destino superior preserva parte da autoridade.
```

### 6.3 410 vs 404

| Status | Significado | Quando usar |
|--------|-------------|-------------|
| **404 Not Found** | URL nao encontrada (Google reverifica periodicamente) | Default |
| **410 Gone** | URL removida permanentemente | Sinal mais forte de remocao — Google retira do indice mais rapido |

Para pruning intencional em massa: **410 preferido**. Para erros nao-intencionais: 404.

### 6.4 Cuidados em pruning de massa

- Pruning de 30%+ do site em um lote pode disparar reavaliacao algoritmica abrupta — preferir batches menores (5-10% por mes).
- Manter log de pruning (URL deletada + motivo + status) para auditoria.
- Acompanhar GSC > Cobertura por 30-60 dias pos-pruning.
- Se trafego total CAI mais que o esperado, reavaliar criterios.

### 6.5 Pruning vs noindex

| Acao | Quando |
|------|--------|
| **Delete + 410** | Conteudo morto irrelevante |
| **Delete + 301** | Conteudo morto com autoridade externa OU substituto direto |
| **Noindex** | URL precisa existir (UX) mas nao deve indexar (filtros, paginacao alem de N, perfil de usuario) |
| **Refresh** | Conteudo recuperavel com investimento moderado |

---

## 7. Content consolidation — merging URLs

### 7.1 Por que consolidar

Sites antigos acumulam paginas que **competem entre si** pela mesma intent (cannibalization). Consolidar:

- Concentra autoridade em 1 URL master.
- Resolve cannibalization.
- Reduce thin content count.
- Melhora HCS.

### 7.2 Identificar candidatos a consolidar

- GSC > Performance > queries com multiplas URLs aparecendo.
- `site:dominio.com "keyword"` com varias URLs relevantes.
- Topical map: 2+ URLs no mesmo subtopic.
- Cluster bagunçado (5 posts sobre o mesmo tema, 0 deles dominam).

### 7.3 Workflow

```
CONSOLIDATION WORKFLOW
========================

1. IDENTIFICAR
   [ ] Lista de URLs candidatas a consolidar (mesma intent / subtopic)

2. ELEGER MASTER
   Criterio: maior trafego organico + maior autoridade (backlinks) + melhor estrutura
   [ ] URL master definida

3. EXTRAIR CONTEUDO UNICO
   [ ] Capturar paragrafos / dados / exemplos uteis das URLs secundarias
   [ ] Adicionar ao master sem inflar artificialmente
   [ ] Atualizar EEAT, schema, internal linking, copy

4. REDIRECIONAR
   [ ] 301 das secundarias para o master
   [ ] Confirmar redirects funcionam (curl + Screaming Frog)

5. ATUALIZAR INTERNAL LINKS
   [ ] Sitewide: encontrar links que apontavam para secundarias
   [ ] Atualizar para master
   [ ] Atualizar sitemap

6. MONITORAR
   [ ] GSC > Performance da query master por 30-90 dias
   [ ] Backlink update via outreach (se backlinks importantes)
   [ ] Confirmar que master rankeia melhor que soma das secundarias antes
```

### 7.4 Exemplo concreto

```
ANTES:
- /post-2020-melhor-crm-startup/  (DR 30, 200 sessoes/mes)
- /melhor-crm-startup-2022/       (DR 25, 150 sessoes/mes)
- /crm-para-startup-comparativo/  (DR 40, 600 sessoes/mes)
- /pipedrive-vs-rd-station-startup/ (DR 35, 350 sessoes/mes)

DEPOIS:
- /crm-para-startup/  (master — refresh + extracao do unico das outras)
   <- 301 de /post-2020-melhor-crm-startup/
   <- 301 de /melhor-crm-startup-2022/
   <- 301 de /crm-para-startup-comparativo/
- /pipedrive-vs-rd-station-startup/ (mantida — intent comparativo distinto)

Esperado: master converge ~1300 sessoes/mes em 3-6 meses + posicao mais alta + autoridade concentrada.
```

---

## 8. Refresh strategy

### 8.1 Tipos de refresh

| Tipo | Esforco | Impacto |
|------|---------|---------|
| **Cosmético** | Baixo (30 min) | Baixo / negativo se sem mudança real |
| **Atualização de fato** | Medio (1-2h) | Medio |
| **Refresh substancial** | Alto (4-8h) | Alto |
| **Major rewrite** | Muito alto (8-20h) | Muito alto |

### 8.2 dateModified honesto

`dateModified` deve refletir mudança **real** — adicionar, remover, atualizar fato, melhorar estrutura. NAO trocar por:
- Substituir 1 palavra.
- Atualizar plugin do CMS.
- Re-salvar sem modificar.

Google detecta `dateModified` enganoso (compara com mudanca real do conteudo). Risco: HCS rebaixa pagina por sinal manipulativo.

### 8.3 Checklist de refresh substancial

```
REFRESH CHECKLIST
===================

1. CONTEXTO ATUAL
   [ ] Re-buscar KW principal em modo anonimo + geo correto
   [ ] Top 10 atual: que mudou desde ultima publicacao?
   [ ] PAA / related searches: que perguntas surgiram?
   [ ] AI Overview: pagina e citada? por que sim/nao?
   [ ] Concorrentes: novas publicacoes a referenciar?

2. ATUALIZACAO DE FATO
   [ ] Datas no titulo / body / schema
   [ ] Numeros (precos, estatisticas, marcas)
   [ ] Screenshots (UI desatualizada)
   [ ] Links (atualizar fontes que mudaram URL)
   [ ] Schema (rich result types ainda disponiveis?)
   [ ] Internal links (apontar para conteudo mais recente)

3. ESTRUTURA
   [ ] H2/H3 espelham PAA atual
   [ ] TL;DR atualizado
   [ ] Adicionar secao FAQ se faltava
   [ ] Adicionar tabela / comparativo se faltava
   [ ] Schema FAQPage / HowTo se aplicavel

4. EEAT
   [ ] Autor + data + ultima atualizacao visiveis
   [ ] Bio do autor expandida
   [ ] "Reviewed by" se YMYL
   [ ] Disclosure se afiliado/patrocinado

5. ON-PAGE TECNICO
   [ ] CWV: imagem hero AVIF/WebP, lazy, dimensoes
   [ ] Schema valido em Schema Markup Validator + Rich Results Test
   [ ] OG + Twitter Cards atualizados
   [ ] Canonical autorreferencial confirmado

6. EXPERIENCE
   [ ] Adicionar imagem original / video / interactive
   [ ] Adicionar dado proprio / experiencia direta (E de EEAT)

7. PUBLICAR
   [ ] dateModified atualizado HONESTAMENTE
   [ ] URL Inspection > Solicitar indexacao
   [ ] Atualizar sitemap (lastmod)
   [ ] Promo: newsletter recap, social repost com angulo "atualizado"

8. MONITORAR
   [ ] GSC > Performance da query 30-90 dias
   [ ] Posicao subiu? CTR melhorou?
   [ ] Citacao em AI Overview voltou?
```

### 8.4 Anti-refresh

NAO refresh se:
- Conteudo ja esta em posicao top 3 + estavel + sem decay.
- Refresh sera cosmetico apenas.
- Sem orcamento para refresh substancial — melhor consolidar / prune.

---

## 9. Atualizacao programada — calendario

### 9.1 Por tipo

| Tipo | Cadencia recomendada | Sazonalidade adicional |
|------|----------------------|--------------------------|
| Pillar evergreen | Anual (mesmo trimestre) | — |
| Listicle "melhores [N] de [ano]" | Anual antes do ano fiscal | — |
| Comparativo (X vs Y) | Trimestral | — |
| HowTo de produto / interface | Trimestral (UI muda) | — |
| Statistics page | Anual (publicacao de novos dados) | — |
| Original research | A cada 12-24 meses | — |
| Glossario | Bianual + ad-hoc quando termo muda | — |
| Regulatorio | Trimestral + ad-hoc quando lei muda | Fim de ano (mudancas ocorrem) |
| Sazonal | Anual antes do pico | Especifica |
| Trending | Sem refresh — aposentar quando esfria | — |

### 9.2 Implementacao no CMS

Tagar cada pagina com:
- `volatility: very-low | low | medium | medium-high | high`
- `last_verified: 2026-05-07`
- `next_review: 2026-11-07`
- `regrounding_sources: [URLs]`

Mesmo modelo das skills do plugin (frontmatter YAML em cada SKILL.md). Hook ou script de CI lista paginas com `next_review < hoje` -> backlog editorial.

### 9.3 Backlog editorial dinamico

```
WEEK 1 - dia 1: dump das paginas vencidas
   |
   |    Output:
   |    - /pillar-crm/         volatility: medium    next_review: 2026-04-15 (vencida)
   |    - /pipedrive-vs-rd/    volatility: medium    next_review: 2026-04-20 (vencida)
   |    - /seo-fundamentos/    volatility: medium    next_review: 2026-05-01 (vencida)
   |
   |
WEEK 1 - dia 2-5: priorizar (matriz Esforco x Impacto)
   |
WEEK 2: refresh dos top 5
   |
WEEK 3: refresh dos seguintes 5
   |
WEEK 4: monitor + ajustes + planejamento de novo conteudo
```

---

## 10. Topical authority sistematica

### 10.1 Conceito

Site cresce autoridade em **um topico** (ex.: marketing digital) cobrindo:
- **Horizontalmente**: todos os subtemas relevantes.
- **Verticalmente**: cada subtema em profundidade.
- **Conexoes**: internal linking semantico entre subtemas.

Quando autoridade tematica e estabelecida, Google rankeia novas paginas do mesmo topico **mais facil**, ate sem backlinks externos significativos.

### 10.2 Mapeamento

```
TOPICAL MAP — SEO (exemplo)
=============================

NIVEL 0 — TEMA RAIZ
  SEO

NIVEL 1 — PILLARS (4-8)
  - SEO Fundamentos
  - SEO Keywords
  - SEO On-page
  - SEO Tecnico
  - SEO Link Building
  - Conteudo Evergreen

NIVEL 2 — CLUSTERS por pillar (8-15 cada)
  Sob "SEO Tecnico":
    - Robots.txt
    - Sitemaps
    - Canonical
    - Hreflang
    - Render JS
    - Core Web Vitals
    - Migration
    - Server logs
    ...

NIVEL 3 — SPOKES por cluster (3-10 cada)
  Sob "Core Web Vitals":
    - LCP otimizacao
    - INP otimizacao
    - CLS otimizacao
    - CrUX vs Lighthouse
    - CWV em Next.js
    ...

Total: 4 pillars × 10 clusters × 5 spokes = 200 URLs.
```

### 10.3 Sequencia de cobertura

```
1. Pillar (ampla cobertura, ~2500-5000 palavras)
   |
2. 5-10 spokes de cada pillar (~1000-2000 palavras cada)
   Foco em sub-intent especifico do pillar
   |
3. Quick wins em cluster com volume + KD relativo viavel
   |
4. Refresh continuo + adicao de spokes adjacentes
```

### 10.4 Internal linking semantico

- Pillar -> todos spokes (exclusivamente do mesmo cluster).
- Spoke -> pillar (no inicio: "Este artigo faz parte do guia [Pillar]").
- Spoke -> spoke siblings (transversal contextual).
- Spoke ocasional -> pillar de outro cluster relevante.

---

## 11. Hub-and-spoke maintenance

Cluster nao para de evoluir. Tarefas continuas:

| Frequencia | Tarefa |
|-----------|--------|
| **A cada nova publicacao** | Atualizar internal links no pillar para incluir novo spoke |
| **A cada nova publicacao** | Atualizar internal links em spokes adjacentes |
| **Mensal** | Audit do cluster (cannibalization, gaps, decay) |
| **Trimestral** | Refresh do pillar com referencia aos spokes mais recentes |
| **Anual** | Major rewrite do pillar |
| **Ad-hoc** | Consolidar spokes redundantes |

---

## 12. Internal linking dinamico

### 12.1 Ao publicar nova pagina

```
NEW POST CHECKLIST — INTERNAL LINKING
========================================

1. Outbound (do novo post):
   [ ] Link para pillar do cluster (no inicio)
   [ ] 3-5 links para spokes adjacentes (contextuais no body)
   [ ] 1-2 links para outras paginas relacionadas do site
   [ ] Source primaria externa (com rel apropriado)

2. Inbound (de outras paginas para o novo post):
   [ ] Atualizar pillar com link para novo spoke
   [ ] Atualizar 2-5 spokes existentes com link contextual
   [ ] Atualizar pagina /sitemap-blog ou /index do cluster (se houver)
   [ ] Atualizar newsletter (proximo envio)

3. Internal anchor text:
   [ ] Anchor descritivo (sem "leia mais")
   [ ] Variar entre exact-match parcial, sinonimos, branded
   [ ] Sem over-optimization (anchor cloud sitewide)
```

### 12.2 Auditoria periodica de internal linking

- Screaming Frog > Internal Linking report.
- Ahrefs > Site Explorer > Internal Backlinks.
- Identificar paginas orfas (sem internal link apontando).
- Identificar paginas com poucos links de saida (oportunidade de fortalecer cluster).

---

## 13. AI Overview / SGE preparation

### 13.1 Sinais para citacao

(Recap de `seo-fundamentos` Secao 13 + `seo-on-page` Secao 15.3 — aqui aplicado a evergreen)

- TL;DR no inicio.
- Estrutura semantica forte (H, listas, tabelas, FAQ).
- Schema rico (Article + Person + Organization + FAQPage + sameAs).
- EEAT visivel + estruturado.
- Fontes primarias linkadas.
- `dateModified` honesto e recente.
- Cobertura de entidade (atributos + relacoes).
- Autoridade do dominio + co-citacoes.

### 13.2 Tracking continuo

- Ferramentas: Profound, Authoritas, BrightEdge Generative Parser.
- Mensal: que % das suas KW criticas mostram AI Overview? Sao citadas?
- Identificar perda de citacao -> investigar (concorrente fortaleceu? estrutura caiu?) -> refresh focado.

### 13.3 Refresh para AI Overview

Quando perder citacao:
- Reescrever TL;DR com resposta direta concentrada.
- Adicionar tabela / lista / FAQ explicita.
- Reforcar EEAT.
- Atualizar `dateModified`.
- Linkar fonte primaria + autoridade.

---

## 14. HCS-proofing pos-update

Helpful Content System reavalia continuamente. Pos-refresh, validar:

```
HCS SELF-ASSESSMENT
=====================

[ ] Conteudo demonstra expertise direta e profundidade?
[ ] Site tem foco principal claro? Conteudo alinhado?
[ ] Apos ler, leitor resolve o problema?
[ ] Experiencia satisfatoria?
[ ] Conteudo NAO foi escrito principalmente para ranking?
[ ] Conteudo NAO foi gerado em escala sem expertise?
[ ] Conteudo NAO promete e nao entrega?
[ ] Autor real, com credencial verificavel?
[ ] Fontes citadas, primarias?
[ ] Refresh atualizou fato real, nao apenas data cosmetica?
```

Falhar em 3+ -> conteudo em risco. Continuar trabalhando ou despromover.

---

## 15. Programmatic SEO etico vs scaled content abuse

### 15.1 Definicao

**Programmatic SEO**: gerar paginas em escala via templates + dados estruturados (Tripadvisor com paginas por cidade, Zapier com paginas por integracao, Indeed com paginas por vaga).

**Scaled content abuse** (Spam Policies, mar/2024): geracao em massa (humana, IA ou hibrida) com **proposito de manipular ranking**, sem valor agregado.

### 15.2 Linha divisoria

| Programmatic etico | Scaled abuse |
|---------------------|---------------|
| Dados unicos por pagina (ex.: lista de produtos por loja) | Texto generico variado por keyword |
| Utilidade pratica ao usuario | Apenas para capturar trafego |
| Conteudo extraido de fonte legitima | Spinning / IA sem revisao + sem expertise |
| Volume justificado pela natureza dos dados | Volume desproporcional ao site |
| Cada pagina tem intent unico | Paginas redundantes / canibalizando |
| Indexacao + trafego organico real | Paginas finas, indexacao fraca, sem trafego |

### 15.3 Casos legitimos

- E-commerce: pagina por produto.
- Marketplace: pagina por listing.
- Job board: pagina por vaga.
- Real estate: pagina por imovel.
- Travel: pagina por destino.
- Local: pagina por cidade/bairro x servico.
- SaaS: pagina por integracao (X + Y).
- Comparativo: pagina por par (X vs Y).

### 15.4 Boas praticas em programmatic

- **Dados originais ou licenciados** legitimamente.
- **Valor agregado** alem do dado puro (analise, contexto, recomendacao).
- **EEAT** no template (autor / publisher / metodologia).
- **Schema rico** alinhado ao tipo (Product, Place, JobPosting, etc.).
- **Internal linking** robusto (categoria, tags, relacionados).
- **Indexacao seletiva** — gerar 10k paginas mas indexar apenas as 2k com volume real (`noindex, follow` no resto).
- **Monitoramento de cobertura** GSC.

### 15.5 IA na producao em massa

Google: "Nao penalizamos IA per se. Penalizamos conteudo nao-util." (mar/2024 + repetido em 2025).

Uso aceitavel:
- IA como **assistente** (outline, primeira versao, sumarizacao, traducao).
- **Revisor humano** com expertise no tema.
- **Autor identificado** + EEAT.
- **Dado original** ou expertise direta adicionada.
- **Volume realista** (5-15 artigos/semana com qualidade, nao 500/semana sem).

Uso problematico:
- IA gera + publica sem revisao.
- 100% generico.
- Volume + topicos fora do nicho.
- Sem autor / EEAT.

---

## 16. Sazonal vs evergreen — calendario coordenado

### 16.1 Calendario base BR (referencia)

| Mes | Sazonais BR de relevancia |
|-----|----------------------------|
| **Jan** | Volta as aulas, ferias, planejamento ano novo, fechamento fiscal pessoa juridica |
| **Fev** | Carnaval, ferias, IRPF preparacao |
| **Mar** | IRPF declaracao, dia da mulher, outono (NA -> BR), back to school |
| **Abr** | IRPF deadline, pascoa, Tiradentes |
| **Mai** | Dia das maes, dia do trabalhador, copa (anos pares) |
| **Jun** | Festa junina, dia dos namorados, copa |
| **Jul** | Ferias escolares, inverno |
| **Ago** | Volta as aulas, dia dos pais, vestibular |
| **Set** | Independencia, primavera, vendas inicio segundo semestre |
| **Out** | Dia das criancas, halloween, eleicoes (anos pares), DOC mes da seguranca |
| **Nov** | Black Friday (4ª sex), Cyber Monday, Proclamacao Republica, Black November |
| **Dez** | Natal, ano novo, fim de ano fiscal, retrospectiva |

### 16.2 Coordenacao

```
TIMELINE EXEMPLO — IRPF
=========================

DEZ ano anterior: planejar pauta IRPF
JAN: publicar guia (volume sobe a partir de jan)
   |
FEV: refresh com ajustes da Receita Federal
   |
MAR: pico de busca — pagina ja rankeada
   |
ABR: pico final — ate deadline
   |
MAI: declinio rapido
   |
JUN-DEZ: "evergreen baixo" — pagina mantem ranking residual
   |
JAN proximo ano: refresh anual com mudancas legais

Ao mesmo tempo, conteudo evergreen ("o que e DPA", "como configurar GA4")
roda independente do calendario sazonal.
```

### 16.3 Distribuicao

- **70-85% evergreen** (publicar continuamente).
- **5-15% sazonal** (publicar/refresh 30-60 dias antes do pico).
- **5-15% trending/news** (oportunismo).

---

## 17. Republishing strategy

### 17.1 Tipos

| Tipo | Quando |
|------|--------|
| **Refresh in-place** | Mesma URL, dateModified atualizado | Default — preserva backlinks e historico |
| **Republish em nova URL** | Apenas se URL antiga e problematica (slug ruim, estrutura legada, CMS migration) | Raro |
| **Re-promotion** | Mesma URL, mesma data, mas re-divulgar | Para conteudo evergreen que ainda performa |

### 17.2 Anti-pattern: re-publish trocando data

Trocar `datePublished` para "fingir conteudo novo" e:
- Enganar usuarios (HCS).
- Sinal manipulativo.
- Pode disparar reavaliacao negativa.

`dateModified` honesto e o unico sinal a usar.

---

## 18. Distribuicao evergreen

### 18.1 Newsletter recap

- Mensal: recap do top 5 posts evergreen do site (nao apenas novos).
- Quarterly: "best of" thematic.
- Annual: "100 artigos para X" como linkable asset.

### 18.2 Social recycling

- Post evergreen pode ser re-divulgado no LinkedIn / X / Instagram a cada 6-12 meses.
- Variar o angulo (quote diferente, imagem diferente, hook diferente).
- NAO repetir o mesmo formato literalmente.

### 18.3 Video / podcast

- Top 10 evergreen -> series de videos / episodios.
- Cross-link mutuo.

### 18.4 Repurposing

- Long-form pillar -> SlideShare / linkedin carousel + 5 posts curtos.
- Original research -> 1 PDF gated + 3 posts + 5 social tiles + 1 podcast episode.

---

## 19. Metricas

### 19.1 Por pagina (life value)

| Metrica | Como calcular |
|---------|---------------|
| **Lifetime Sessions** | Soma de sessoes organicas desde publicacao |
| **Lifetime Conversoes** | Soma de conversoes atribuidas |
| **Lifetime Revenue** | Soma de receita atribuida |
| **Decay Rate** | Variacao mes a mes, identificar inflexao |
| **Refresh ROI** | (Sessoes 90d pos-refresh) - (sessoes 90d pre-refresh) / esforco do refresh |
| **AI Overview citation rate** | % dos meses em que a pagina foi citada |

### 19.2 Por cluster

| Metrica | Como calcular |
|---------|---------------|
| **Cluster Total Traffic** | Soma de sessoes do cluster |
| **Cluster Topical Authority** | % das KW do cluster em top 10 |
| **Cluster Conversion** | Conversoes do cluster |
| **Cluster Backlink Profile** | RD apontando para qualquer pagina do cluster |
| **Cluster Health Score** | Composite (cobertura + ranking + freshness + EEAT) |

### 19.3 Site-wide

| Metrica | Como calcular |
|---------|---------------|
| **Content Health Score** | % de paginas em "TOP" / "GROWING" do audit (Secao 5.2) |
| **Pruning Ratio** | % de URLs aposentadas em 12 meses |
| **Average dateModified Age** | Media de idade da ultima atualizacao |
| **HCS Risk Indicator** | % de paginas com sinais de thin/scaled |

---

## 20. Auditoria de conteudo em 12 fases

```
CONTENT AUDIT — 12 FASES
==========================

FASE 1 — INVENTARIO
  [ ] Export de URLs do CMS
  [ ] Sitemap completo
  [ ] Crawl complementar (Screaming Frog)
  [ ] Cruzar 3 fontes para evitar perda

FASE 2 — METADADOS POR URL
  [ ] Tipo, cluster, autor, data publicacao, data update
  [ ] Indexacao (GSC URL Inspection batch)

FASE 3 — PERFORMANCE
  [ ] GSC: impressoes, cliques, CTR, posicao 90d
  [ ] GA4: sessoes, conversoes, revenue 90d
  [ ] Backlinks RD por URL (Ahrefs)
  [ ] AI Overview citation (Profound)

FASE 4 — CATEGORIZACAO PERFORMANCE
  [ ] TOP / GROWING / PLATEAU / DECLINING / UNDERPERFORMER / ZERO
  [ ] Por cluster

FASE 5 — INTENT MAPPING
  [ ] Cruzar URL vs intent vs estagio do funil
  [ ] Identificar gaps + over-coverage

FASE 6 — CANNIBALIZATION DETECTION
  [ ] GSC > queries com 2+ URLs
  [ ] Site search por KW critica
  [ ] Lista de candidatos a consolidar

FASE 7 — TOPICAL MAP
  [ ] Pillars + clusters + spokes
  [ ] Identificar buracos (sub-intents nao cobertos)
  [ ] Identificar sobreposicao (clusters concorrentes internamente)

FASE 8 — DECAY DETECTION
  [ ] Paginas com queda > 30% em 6 meses
  [ ] Hipoteses (HCS, intent, concorrente, AI Overview)

FASE 9 — DECISAO POR URL
  Para cada URL:
  [ ] Manter (refresh por calendario)
  [ ] Refresh substancial agora
  [ ] Consolidar (com qual master)
  [ ] Prune (delete + 410 ou 301)

FASE 10 — PLANO DE ACAO
  [ ] Matriz Esforco x Impacto
  [ ] 90-day action list
  [ ] Cadencia de revisao por tipo

FASE 11 — INTERNAL LINKING REVIEW
  [ ] Paginas orfas (sem in-link)
  [ ] Paginas com over-link interno
  [ ] Hub-and-spoke health

FASE 12 — RELATORIO + ROADMAP
  [ ] Content Health Score baseline
  [ ] Pruning ratio target
  [ ] Refresh schedule
  [ ] KPIs de monitoramento
```

---

## 21. Templates rapidos

### 21.1 Content audit sheet (esquema)

```
| URL | Titulo | Tipo | Cluster | Autor | Pub | Last | Indexada? | Imps | Cliques | CTR | Pos | Sessoes 90d | Conv | RD | Categoria | Decisao |
|-----|--------|------|---------|-------|-----|------|-----------|------|---------|-----|-----|-------------|------|-----|-----------|---------|
| /crm-startup/ | CRM para Startup 2026 | pillar | crm-startup | A.Jalkh | 2025-08 | 2026-04 | sim | 12.4k | 380 | 3.0% | 6.1 | 1100 | 12 | 8 | TOP | refresh out/2026 |
| /post-2020/ | CRM melhor 2020 | post | crm-startup | A.Jalkh | 2020-03 | 2020-03 | nao | 0 | 0 | — | — | 0 | 0 | 0 | ZERO | prune (410) |
| /pipedrive-vs-rd/ | Pipedrive vs RD Station | comparativo | crm-startup | A.Jalkh | 2024-01 | 2024-01 | sim | 4.2k | 180 | 4.3% | 8.2 | 520 | 7 | 3 | GROWING | refresh + interna |
```

### 21.2 Pruning decision tree

```
                     [URL candidata a prune]
                              |
                              v
                  [Tem backlinks externos?]
                    SIM /              \  NAO
                       v                v
              [Conteudo relevante?]   [Topicalmente relevante?]
                  SIM /     \ NAO         SIM /       \ NAO
                     v       v              v          v
                  [Refresh] [301 p/      [Refresh ou  [Delete +
                            categoria]    consolidar]  410]
                                                       
```

### 21.3 Refresh schedule (esquema CMS)

```
Cada URL no CMS recebe:
  - volatility: very-low | low | medium | medium-high | high
  - last_verified: YYYY-MM-DD
  - next_review: YYYY-MM-DD
  - regrounding_sources: [URLs]
  - last_refresh_type: cosmetico | atualizacao | substancial | rewrite
  - refresh_history: [
      { date: 2025-08-15, type: substancial, notes: "..." },
      { date: 2026-04-20, type: atualizacao, notes: "..." }
    ]
```

---

## 22. Anti-patterns

| Anti-pattern | Por que e problema |
|--------------|---------------------|
| **dateModified cosmetico** (sem mudanca real) | HCS detecta — sinal manipulativo |
| **Re-publish trocando datePublished** | Engano — risco HCS |
| **Pruning massivo (>30%) em lote unico** | Reavaliacao algoritmica abrupta — preferir batches |
| **Pruning sem 301 onde havia backlink** | Volatiliza autoridade externa |
| **404 generico em pruning intencional** | 410 e mais forte para sinal de remocao |
| **Refresh apenas adicionando palavras** | Inflar contagem nao melhora HCS |
| **Republishing sem extracao de conteudo unico das URLs antigas** | Perde valor + cannibalization persiste |
| **Programmatic sem dado unico por pagina** | Scaled content abuse (mar/2024) |
| **IA sem revisao + sem expertise + em escala** | Scaled content abuse |
| **Sazonal publicado durante o pico** (em vez de antes) | Janela de indexacao + ranking perdida |
| **Cluster sem internal linking entre spokes** | Topical authority diluida |
| **Atualizacao de cluster sem atualizar internal linking** | Pillar fica desatualizado |
| **Trending publicado e esquecido sem aposentar** | Conteudo morto inflando contagem thin |
| **Refresh sem re-indexacao** (URL Inspection nao acionada) | Google leva mais tempo para reavaliar |

---

## 23. Regras de Ouro

1. **NAO CHUTAR** — decisao de refresh/prune/consolidar requer dado (GSC + GA4 + Ahrefs). Sem dado, nao decidir.
2. **dateModified honesto** — atualizar so quando muda fato real.
3. **Pruning protege HCS** — site limpo > site grande com thin.
4. **Backlinks sao ativo** — pruning de URL com RD usa 301, nunca 404 puro.
5. **410 > 404** para pruning intencional em massa.
6. **Refresh > Republish** quase sempre (preserva URL + backlinks + historico).
7. **Calendario por volatility** — cada tipo tem cadencia propria.
8. **Topical authority sistematica** — cobertura horizontal + vertical, nao dispersao.
9. **Internal linking dinamico** — cada nova pagina dispara update no cluster.
10. **AI Overview citation e KPI 2026** — tracking continuo (Profound/Authoritas).
11. **Programmatic etico** — dado unico + valor agregado + EEAT.
12. **HCS-proofing pos-refresh** — re-validar self-assessment.
13. **Sazonal coordenado com evergreen** — 70-85% evergreen + sazonal antes do pico.
14. **Distribuicao multiplica ROI** — newsletter recap, social recycling, repurposing.
15. **Cluster e organismo vivo** — refresh do pillar quando spokes maturam.

---

## 24. Exemplos comportamentais — conteudo evergreen

### Exemplo 1 — "Vamos publicar 10 artigos por semana"

**Input:** "Cliente quer publicar 10 artigos/semana com IA + 1 freelancer. Vai escalar SEO?"

**Resposta esperada:**
> CORRIGE: "Volume nao escala SEO em 2026. Risco alto: (1) **Scaled content abuse** (Spam Policies mar/2024) — geracao em massa sem expertise + sem dado unico cai nessa categoria. (2) **HCS site-wide** — 40 artigos/mes em volume sem qualidade individual rebaixa media do site, prejudicando ate as paginas boas. (3) **Cannibalization** — sem topical map, 10 artigos/semana criam paginas concorrentes. Alternativa: **5 artigos/semana com expertise + dado original** OU **2 artigos/semana de muita profundidade**. Muitos sites maturos publicam 1-3/semana e dominam o nicho. Plano sustentavel: (a) **topical map** primeiro (Secao 10) — onde investir; (b) **5 artigos/semana**: 2 evergreen profundos + 2 long-tail com dado proprio + 1 de manutencao (refresh). (c) IA como assistente (outline, primeira versao, traducao) com **revisor humano com expertise** + autor identificado + dado original adicionado. (d) HCS self-assessment ANTES de publicar cada um. Volume realista: 200-260 artigos/ano de qualidade, nao 500/ano genericos. ROI 12 meses: cluster com topical authority real > pulverizacao com 1500 artigos esquecidos. Recomendar piloto de 30 dias com volume reduzido + measurement antes de comprometer com 500/ano."

**Comportamento-chave:** rejeita volume cego, cita politica especifica, oferece alternativa quantitativa, propoe piloto antes de comprometimento.

### Exemplo 2 — Post de 2022 caiu de 5k para 800 visitas/mes

**Input:** "Post `melhores plugins WordPress 2022` tinha 5k visitas/mes em 2023, hoje 800/mes. O que fazer?"

**Resposta esperada:**
> Diagnostico em camadas: "Listicle com `2022` no titulo decai brutalmente em 12-18 meses — comportamento esperado. Hipoteses: (1) **Ano no titulo desatualizado** — usuarios + Google preferem conteudo de 2026 ou 'atualizado'; (2) **AI Overview** absorveu top 5 plugins (zero-click); (3) **Concorrentes publicaram listicle 2025/2026** com plugins novos; (4) **Plugins citados podem ter sido descontinuados** (sinal de obsolescencia). Decisao depende de dados: (a) Backlinks externos (Ahrefs RD)? Se >= 3 RD legitimos -> refresh substancial mantendo URL + 301 nao necessario. Se 0 RD + sem trafego conversao -> consolidar com pillar `plugins WordPress` ou prune. (b) Conversao historica? Se conversao boa antes da queda -> refresh substancial vale. Se sempre baixa -> consolidar. **Plano refresh** (se decisao for refresh): mudar URL? Em 99% dos casos NAO — perderia backlinks. Manter URL `/melhores-plugins-wordpress-2022/` (mesmo com '2022' no slug) e reescrever H1 + title + body para `Melhores Plugins WordPress 2026 (Atualizado)`. Refresh substancial: revisar todos plugins citados, remover descontinuados, adicionar 2-3 novos relevantes, atualizar prints/UI, EEAT visivel, schema FAQPage com PAA atual, dateModified honesto. Re-promover em newsletter + social. Monitor 60-90 dias. Realista: voltar a 3-4k visitas/mes em 90-180 dias. NAO criar URL nova `/plugins-2026/` — split de autoridade."

**Comportamento-chave:** identifica padrao previsivel, exige dados antes de decidir, alerta sobre URL change, propoe refresh substancial concreto.

### Exemplo 3 — Pillar publicado ha 2 anos sem refresh

**Input:** "Pillar `seo` foi publicado em 2024, 4500 palavras, 2k visitas/mes estavel. Vale refresh?"

**Resposta esperada:**
> Avaliar custo-beneficio: "Estavel + 2k visitas/mes em pillar = sinal positivo. Mas pillar evergreen tem cadencia anual (volatility medium). 2 anos sem refresh expoe ao decay. Antes de refresh full, validar: (1) **Top 10 SERP atual** — que mudou desde 2024? (Helpful Content updates, AI Overview, novos sistemas Google, Core Web Vitals INP); (2) **PAA atual** — perguntas novas que pillar nao cobre? (3) **AI Overview** cita o pillar? Se nao, por que? (estrutura, EEAT, autoridade); (4) **Backlinks externos** chegaram nos ultimos 12 meses ou estancou? (5) **CTR** caiu? Title/meta acompanha SERP atual? **Plano refresh substancial** (4-8h investimento): atualizar (a) intro + TL;DR; (b) sec ao Helpful Content System (incorporada ao core mar/2024); (c) Spam Policies novas (mar/2024); (d) CWV (INP substituiu FID em mar/2024); (e) AI Overview / SGE (Secao nova); (f) atualizar prints/UI; (g) adicionar 2-3 sub-secoes para PAA novas; (h) reforcar EEAT (autor + bio + credenciais); (i) schema validado; (j) internal linking para spokes publicados em 2025-2026; (k) `dateModified` honesto + URL Inspection. Esperado em 60-90 dias: 2k -> 3.5-4.5k visitas/mes + posicao melhor + AI Overview citation possivel. Investimento alto, ROI alto. Vale."

**Comportamento-chave:** valida com dados antes de agir, lista mudancas relevantes 2024-2026, oferece plano em 11 acoes, define ROI esperado.

### Exemplo 4 — Programmatic SEO em SaaS B2B

**Input:** "SaaS B2B quer gerar 1500 paginas `[Produto] + [Integracao]` programaticamente — risco?"

**Resposta esperada:**
> Programmatic legitimo SE feito corretamente: "Padrao reconhecido em SaaS (Zapier, Make, IFTTT) — Google aceita quando ha valor. Linha divisoria entre programmatic etico e scaled abuse esta no **dado unico + valor agregado** por pagina. Plano: (a) **Listar integracoes legitimas** — quantas APIs reais? Cada uma realmente integra com o produto? Se 1500 pretende existir mas 1200 sao integracoes hipoteticas/sem documentacao -> abuse. (b) **Conteudo unico por pagina**: descricao real da integracao, casos de uso reais (depoimento ou case study, se possivel), screenshots reais de UI, codigo de exemplo, troubleshooting, FAQ especifica. NAO template generico variando apenas o nome. (c) **Schema rico**: Product + SoftwareApplication + sameAs apontando para sites oficiais dos parceiros. (d) **Indexacao seletiva**: gerar 1500 mas marcar `noindex, follow` nas 800 com volume zero validado em GKP/Ahrefs. Indexar apenas 700 com volume real OU intent claro. (e) **EEAT**: autor da equipe tecnica/integracao, com credencial. (f) **Internal linking**: hub `/integracoes/` listando todas + tags por categoria + cross-link entre integracoes complementares. (g) **Monitoring**: GSC > Cobertura mensal — `Rastreada nao indexada` em massa = sinal vermelho de HCS. **Risco**: se 800 paginas cairem em 'rastreada nao indexada' E permanecerem assim por 90 dias -> Google julgou nao-util -> retirar do site. **NAO**: 1500 paginas todas indexadas com texto generico spinned -> scaled content abuse, manual action de marcacao spammy + HCS site-wide. Recomendar piloto: 30 integracoes em 4 semanas, monitorar 60 dias, validar metricas, expandir."

**Comportamento-chave:** distingue programmatic etico de scaled abuse, define criterios objetivos, propoe indexacao seletiva, alerta para risco HCS, recomenda piloto.

---

## 25. Checklist de Contraditorio Interno — conteudo evergreen

| # | Pergunta destruidora | O que busca |
|---|----------------------|-------------|
| 1 | **Decay temporal foi mapeado** por tipo de conteudo? Cada URL tem `volatility` + `next_review` definidos? | Cadencia de manutencao |
| 2 | **Pruning candidates foram identificados** com criterios objetivos (Secao 6.1), nao por gut feeling? | Pruning data-driven |
| 3 | **`dateModified` reflete mudanca real** de fato/estrutura/EEAT, nao cosmetico? | dateModified honesto |
| 4 | **Internal linking foi atualizado** apos cada nova publicacao (pillar + spokes adjacentes)? | Hub-and-spoke vivo |
| 5 | **Topical authority cresce** ou esta dispersa em multiplos clusters? | Foco vs pulverizacao |
| 6 | **HCS self-assessment** passa apos cada update? | HCS-proofing |
| 7 | **AI Overview citation** esta sendo trackeada? Perda foi investigada e endereçada via refresh? | KPI 2026 |
| 8 | **Calendario evergreen + sazonal** esta coordenado (sazonal publicado antes do pico, evergreen continuo)? | Janela de oportunidade |
| 9 | **ROI por refresh** esta sendo medido (sessoes 90d pre vs pos)? Refreshes baixo-impacto sendo identificados? | Investimento eficiente |
| 10 | **Cluster cannibalization** foi reauditada apos expansao? Novos spokes nao competem com pillar? | Cannibalization continua |

---

## 26. Referencias canonicas

### 26.1 Oficiais Google

- **Google Search Central** — https://developers.google.com/search
- **Creating helpful, reliable, people-first content** — https://developers.google.com/search/docs/fundamentals/creating-helpful-content
- **Helpful Content Update history** — https://developers.google.com/search/blog
- **Spam Policies (scaled content abuse)** — https://developers.google.com/search/docs/essentials/spam-policies
- **Programmatic SEO (Indeed, Tripadvisor — Google guidance)** — https://developers.google.com/search/blog/2018/03/quality-content-and-fewer-low-quality
- **Search Status Dashboard** — https://status.search.google.com
- **Google Search Liaison (X/Twitter)** — atualizacoes informais

### 26.2 Bibliografia profissional

- **Ahrefs Blog — Content Audit** — https://ahrefs.com/blog/content-audit/
- **Semrush Blog — Content Audit** — https://www.semrush.com/blog/content-audit/
- **Moz — On-site SEO** — https://moz.com/learn/seo/on-site-seo
- **Backlinko (Brian Dean)** — Skyscraper, Content Hub
- **Animalz** — content marketing + decay
- **Ross Hudgens (Siege Media)** — content marketing strategy
- **Nick Eubanks (From The Future)** — programmatic + topical authority
- **Koray Tugberk Gubur** — Topical Authority + Holistic SEO
- **Aleyda Solis — Crawling Mondays** — content + technical
- **Lily Ray** — EEAT + Helpful Content updates
- **Glenn Gabe (G-Squared)** — analise de updates
- **Marie Haynes** — newsletters de updates
- **Kevin Indig** — content + organic growth

### 26.3 Ferramentas

- **Google Search Console** — https://search.google.com/search-console
- **Google Analytics 4** — https://analytics.google.com
- **Ahrefs** — https://ahrefs.com
- **Semrush** — https://www.semrush.com
- **Sistrix** — https://www.sistrix.com
- **Screaming Frog** — https://www.screamingfrog.co.uk
- **Sitebulb** — https://sitebulb.com
- **Profound** — https://www.tryprofound.com
- **Authoritas** — https://www.authoritas.com
- **Animalz Revive** — content audit (descontinuado mas referencia conceitual)
- **MarketMuse** — content planning
- **Clearscope** — topical relevance
- **SurferSEO** — content optimization
- **Frase** — content brief

### 26.4 Brasil

- **CONAR** — https://www.conar.org.br
- **CDC (Lei 8.078/1990)** — http://www.planalto.gov.br/ccivil_03/leis/l8078compilado.htm
- **LGPD (Lei 13.709/2018)** — http://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm
- **IAB Brasil** — https://iabbrasil.com.br

---

## 27. Referencia cruzada de skills

| Situacao | Skills relacionadas |
|----------|----------------------|
| Plano editorial + calendario | `seo-fundamentos` + `seo-keywords` + `conteudo-evergreen` + `seo-on-page` (anatomias) |
| Content audit | `conteudo-evergreen` (Secao 5+20) + `seo-keywords` (cannibalization) + `seo-tecnico` (sitemap + canonical) |
| Pruning massivo | `conteudo-evergreen` (Secao 6) + `seo-tecnico` (redirects + sitemap update) + `seo-link-building` (preservar autoridade) |
| Refresh sistematico | `conteudo-evergreen` (Secao 8+9) + `seo-on-page` (anatomia atualizada) |
| Topical authority | `conteudo-evergreen` (Secao 10) + `seo-keywords` (cluster) + `seo-link-building` (autoridade externa) |
| Programmatic SEO | `conteudo-evergreen` (Secao 15) + `seo-on-page` (template de pagina) + `seo-tecnico` (indexacao seletiva) |
| Sazonal + evergreen | `conteudo-evergreen` (Secao 16) + `seo-keywords` (sazonalidade) |
| AI Overview adaptation | `conteudo-evergreen` (Secao 13) + `seo-on-page` (Secao 15.3) + `seo-fundamentos` (Secao 13) |
| Linkable asset evergreen | `conteudo-evergreen` + `seo-link-building` (Secao 12 linkable assets) |
| Refresh + republishing | `conteudo-evergreen` (Secao 8+17) + `manutencao-skills` (modelo de decaimento) |

---

## 28. Integracao com o ecossistema Frank-MKT

Esta skill integra-se ao agente principal `frank-mkt` (`agents/frank-mkt.md`) e ao restante do plugin da seguinte forma:

- **Pre-requisitos**: `seo-fundamentos` + `seo-keywords` + `seo-on-page`. Sem modelo mental + cluster + anatomia, esta skill nao opera.
- **Acoplamento com `seo-keywords`** — output de `seo-keywords` (cluster, mapping URL <-> KW, cannibalization detection) alimenta content audit + refresh + consolidation. Esta skill usa esse output operacionalmente.
- **Acoplamento com `seo-on-page`** — anatomia de pillar/cluster (Secao 16 daquela skill) e a base que esta skill mantem ao longo do tempo. Refresh substancial revisita a anatomia.
- **Acoplamento com `seo-tecnico`** — pruning + consolidation envolvem 301/410, sitemap update, canonical strategy, internal linking sitewide. Esta skill define O QUE; `seo-tecnico` garante COMO ENTREGAR tecnicamente.
- **Acoplamento com `seo-link-building`** — linkable assets (research, statistics page, ultimate guide) sao tipicamente evergreen. Esta skill garante refresh anual. `seo-link-building` garante outreach periodica.
- **Acoplamento com `copywriting-conversao`** — refresh de copy (TL;DR, CTA, microcopy) e atualizacao de tom alinhado com a marca. Esta skill define WHEN; `copywriting-conversao` define WHAT.
- **Acoplamento com `manutencao-skills`** — modelo de decaimento temporal usado em todas as skills do plugin (frontmatter YAML com `volatility` + `last_verified` + `next_review` + `regrounding_sources`) e o mesmo modelo aplicado ao conteudo do site do cliente. `manutencao-skills` formaliza a metodologia.
- **Acoplamento com `pesquisa-quantitativa`** — original research (asset evergreen) requer metodologia rigorosa. Aquela skill instrui mecanica de survey, amostra, vies.
- **Acoplamento com o agente `auditor`** — auditor roda regras PASS/FAIL em content audit (paginas com decay > 30%? URLs com 0 backlinks + 0 trafego flagged? cannibalization detectada? `dateModified` honesto?). Esta skill fornece o framework normativo.
- **Acoplamento com o agente `seo-strategist`** — agente especialista orquestra esta skill em planos editoriais de longo prazo (12-24 meses).
- **Acoplamento com `comunicacao-corporativa`** — refresh de pillar pode envolver alinhamento institucional (autor, voz, posicionamento da marca em determinado topico).
- **Acoplamento com `conhecimento-search-console`** + **`conhecimento-ga4`** — esta skill consome dados delas para audit + decisao por URL.
- **Acoplamento com `compliance-lgpd`** (plugin juridico) — pruning de paginas com PII (case studies com cliente identificado, formularios com dados antigos) requer cuidado LGPD. Cruzamento obrigatorio.
- **Memoria e rastreabilidade** — content audits, decisao por URL (refresh/consolidate/prune), refresh history, baseline de Content Health Score sao persistidos em `.frank-mkt/seo/<cliente>/<data>/conteudo-evergreen/` pelo agente `suporte-documental` (a criar) ou diretamente pelo `frank-mkt`. Versionar para revisar evolucao temporal.
- **Contraditorio interno** — o agente principal aciona o modulo `contraditorio-interno` carregando o Checklist da Secao 25 desta skill antes de entregar plano editorial, recomendacao de pruning, ou major rewrite de pillar.
- **Decaimento temporal** — esta skill esta em volatility `medium` (6 meses). Re-grounding obrigatorio em fontes da Secao 26 antes de citar fato volatil (atualizacoes de Helpful Content, mudanca em Spam Policies, AI Overview behavior) em peca formal.
- **Regra de ouro para `frank-mkt`** — nenhuma decisao de pruning, consolidation, refresh substancial, programmatic em massa, ou plano editorial de longo prazo sai do plugin sem passar por esta skill. Custos de erro sao altos: HCS rebaixa site, autoridade perdida, conteudo bom enterrado.

---

> **Aviso:** o plugin `frank-mkt` e um assistente de analise. Recomendacoes desta skill devem ser adaptadas a tamanho do site, nicho, autoridade, recursos disponiveis, e validadas em GSC + GA4 + ferramenta de backlink antes de aplicar em peca formal. Helpful Content System foi incorporado ao core algorithm em mar/2024 e reavalia continuamente; Spam Policies novas (scaled content abuse, expired domain abuse, site reputation abuse) sao linha vermelha. Pruning agressivo demais ou refresh cosmético podem prejudicar mais que ajudar — operar com dado, nao gut feeling.

---

*Plugin `frank-mkt` — skill `conteudo-evergreen` (v0.1.0)*
*Ultima atualizacao: 2026-05-07*
