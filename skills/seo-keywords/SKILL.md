---
name: seo-keywords
description: "Pesquisa de palavras-chave aplicada. Universe (head/body/long-tail/zero-volume), volume mensal (MSV), dificuldade (KD), intent profundo, modificadores semanticos, long-tail strategy, KGR (Keyword Golden Ratio), entidades e Knowledge Graph, cluster topical, cannibalization detection, branded vs non-branded, PAA mining, Featured Snippet, AI Overview keywords (GEO/LLMO), local keywords, sazonalidade, content/keyword gap. Ferramentas comparadas (GSC, GKP, Ahrefs, Semrush, Sistrix, Mangools, Moz, AnswerThePublic, AlsoAsked, SparkToro, Profound). Workflow em 12 fases + templates."
user-invocable: false
last_verified: 2026-05-07
next_review: 2026-11-07
volatility: medium
regrounding_sources:
  - "https://developers.google.com/search"
  - "https://ads.google.com/aw/keywordplanner/home"
  - "https://search.google.com/search-console"
  - "https://trends.google.com"
  - "https://ahrefs.com/blog/keyword-research/"
  - "https://www.semrush.com/blog/keyword-research/"
  - "https://moz.com/learn/seo/keyword-research"
  - "https://www.bing.com/webmasters/help/keyword-research-tool-7e57e7e2"
  - "https://schema.org"
  - "https://www.wikidata.org"
---

# Skill: seo-keywords

> **Decaimento Temporal**
> Ultima verificacao: 2026-05-07 | Proxima revisao: 2026-11-07 | Volatility: **medium** (6 meses)
> Ferramentas atualizam metodologia de volume e dificuldade silenciosamente; AI Overview muda comportamento de zero-click; LLM-search expande superficie de query. Re-validar antes de publicar peca formal:
> - Google Search Console (queries reais) — https://search.google.com/search-console
> - Google Keyword Planner — https://ads.google.com/aw/keywordplanner/home
> - Google Trends — https://trends.google.com
> - Ahrefs / Semrush / Sistrix — atualizacoes de KD e MSV
> - Bing Keyword Research Tool — https://www.bing.com/webmasters/help/keyword-research-tool-7e57e7e2
>
> **Acionamento:** keyword research, plano de conteudo, cluster topical, intent, cannibalization, content gap, AI Overview keywords, GEO/LLMO, local SEO keywords, sazonalidade, briefing de conteudo SEO.
> **Skills relacionadas:** `seo-fundamentos` (carrega ANTES desta), `seo-on-page`, `seo-tecnico`, `conteudo-evergreen`, `seo-link-building`, `analise-concorrencia`, `persona-icp`, `copywriting-conversao`, `conhecimento-search-console`.
> **Pre-requisito:** ler `seo-fundamentos` primeiro — modelo mental (crawl/render/index/rank, EEAT, HCS, AI Overview) e fundamento desta skill.

---

## 1. Visao Geral

Pesquisa de palavras-chave (keyword research) e a etapa que define **o que rankear, em que ordem, com que profundidade e em qual formato**. E o ponto de entrada operacional do SEO. Erro de keyword propaga: errar intent custa mais que errar copy. Um plano de conteudo mal-keyword-mapped queima orcamento por meses sem retorno.

Esta skill nao repete o que esta em `seo-fundamentos`. Aqui aprofundamos:

- **Universe** de keywords (head, body, long-tail, micro-tail, zero-volume).
- **Volume real** (MSV) — fontes, vies, sazonalidade, geo, anonimizacao.
- **Dificuldade** (KD) — modelos diferentes por ferramenta, e por que KD e relativo.
- **Intent profundo** — alem dos 4 tipos classicos, modificadores semanticos e estagio.
- **Long-tail e zero-volume strategy** (KGR, micro-tail, conversational queries).
- **Entidades / Knowledge Graph / Wikidata** — keyword research como entity research.
- **Cluster topical** — metodos praticos para construir.
- **Cannibalization detection** — duas paginas competindo pela mesma keyword.
- **Branded vs non-branded** — separacao critica para medir crescimento real.
- **PAA + related + AlsoAsked** — mining sistematico de variacoes.
- **Featured Snippet keywords** — formato proprio para zero-position.
- **AI Overview / SGE / LLM keywords** — generative engine optimization (GEO/LLMO) em 2026.
- **Local keywords** — geo modifiers + Google Business Profile.
- **Sazonalidade** — Google Trends + planejamento de calendario.
- **Concorrencia** — content gap + keyword gap.
- **Ferramentas** — guia comparativo detalhado.
- **Workflow** em 12 fases + templates.

### 1.1 Quando o agente aciona esta skill

| Gatilho | Exemplo de input |
|---------|------------------|
| Briefing de conteudo | "preciso de 50 ideias de pauta para o blog" |
| Plano de cluster | "como estruturar conteudo do nicho fintech" |
| Auditoria de keywords | "quais keywords ja trazem trafego mas estao em posicao 8-15?" |
| Cannibalization | "tenho duas paginas rankeando para a mesma keyword" |
| Validacao de pauta | "essa keyword vale a pena ou e zero-volume?" |
| GEO / LLMO | "como otimizar conteudo para aparecer em ChatGPT/Perplexity?" |
| Local | "quero rankear em '[servico] em [cidade]' — como?" |
| Concorrencia | "que keywords meu concorrente tem e eu nao tenho?" |

### 1.2 Pre-requisitos operacionais

- [ ] Acesso a **GSC** do dominio (fonte de queries reais).
- [ ] Acesso a **GA4** com conversoes (medir valor de cada keyword).
- [ ] Acesso a **Google Keyword Planner** (gratis com conta Google Ads ativa, mesmo que sem campanha rodando).
- [ ] Acesso a **uma plataforma profissional** (Ahrefs ou Semrush sao default; Sistrix forte em DACH/EU; Mangools custo-beneficio).
- [ ] **Google Trends** (gratis, fonte de sazonalidade).
- [ ] **Bing Webmaster Tools** + **Bing Keyword Research** (~3-7% do mercado, mas alimenta Copilot e DuckDuckGo).
- [ ] Conhecimento da **persona/ICP** do cliente (sem persona, intent vira chute).
- [ ] Conhecimento da **autoridade do dominio** (KD absoluto e enganoso — e relativo a sua autoridade).

> **Cristal C0 — NAO CHUTAR.** Volume, KD, CTR, posicao, citacao em AI Overview NUNCA sao inventados. Se nao ha dado de ferramenta, marcar como hipotese explicita ou pedir acesso.

---

## 2. Universe de keywords — taxonomia operacional

Universe = todas as queries possiveis dentro do escopo do cliente. Modelo mental para nao perder oportunidade nem queimar tempo em head terms inalcansaveis.

### 2.1 Tiers por tamanho

| Tier | Tamanho tipico | MSV (BR, ordem de grandeza) | Conversao | Concorrencia |
|------|----------------|------------------------------|-----------|---------------|
| **Head** | 1 palavra | >= 10k/mes | Baixa, generica | Brutal |
| **Body** | 2-3 palavras | 1k-10k/mes | Media | Alta |
| **Long-tail** | 4-6 palavras | 100-1k/mes | Alta | Media |
| **Micro-tail** | 7+ palavras / pergunta inteira | 10-100/mes | Muito alta | Baixa |
| **Zero-volume** | Pergunta especifica, conversacional | "no data" / 0 reportado | Variavel | Inexistente |

> **Observacao:** "zero-volume" frequentemente NAO e zero. Ferramentas nao medem cauda fina ou agrupam em buckets. GSC pode mostrar impressoes para queries que Ahrefs reporta 0.

### 2.2 Tiers por intent (recap de `seo-fundamentos` + modificadores)

| Intent | Modificadores tipicos | Exemplo |
|--------|------------------------|---------|
| **Informacional** | "o que e", "como", "por que", "guia", "tutorial", "exemplos" | "o que e core web vitals" |
| **Navegacional** | nome de marca, "login", "site oficial" | "ahrefs login" |
| **Investigacao comercial** | "melhor", "vs", "review", "comparativo", "alternativa", "ranking" | "melhor crm para startup" |
| **Transacional** | "comprar", "preco", "desconto", "cupom", "trial", "perto de mim" | "ahrefs preco" |
| **Local** | nome de cidade/bairro, "perto de mim", CEP | "advogado tributario sao paulo" |
| **Comparativo** | "X vs Y", "diferenca entre X e Y" | "pipedrive vs hubspot" |
| **Como-fazer** | "como [verbo]", passo-a-passo | "como configurar gsc" |
| **Definicao** | termo unico + contexto definicional | "DPA" |

### 2.3 Tiers por estagio do funil

| Estagio | Intent dominante | Caracteristica |
|---------|------------------|-----------------|
| **TOFU (Top)** | Informacional | Educa, atrai novo publico |
| **MOFU (Middle)** | Investigacao comercial | Compara, considera |
| **BOFU (Bottom)** | Transacional | Decide, compra |
| **Pos-venda** | Informacional/Navegacional | Suporte, retencao |
| **Marca / institucional** | Navegacional | Fortalecimento de marca |

### 2.4 Tiers por valor para o negocio

| Valor | Caracteristica | Exemplo |
|-------|----------------|---------|
| **Money keyword** | Alta intencao de compra/lead | "contratar SEO B2B" |
| **Supporting keyword** | Educa, alimenta cluster, gera autoridade | "o que e SEO" |
| **Branding keyword** | Fortalece presenca | "blog [marca]" |
| **Defensive keyword** | Protege contra reviews/comparativos negativos | "[marca] reclame aqui", "[marca] e confiavel" |

---

## 3. Volume mensal de busca (MSV) — leitura critica

### 3.1 Fontes possiveis

| Fonte | Como obtem | Confiabilidade | Granularidade |
|-------|------------|----------------|---------------|
| **Google Search Console (queries)** | Dados reais do site, anonimizado em parte | Alta para queries que o site ja recebe | Por query / por pagina |
| **Google Keyword Planner (GKP)** | Anonimizado e agrupado em **buckets** (ex.: 10-100, 1k-10k, 10k-100k) | Media — sem precisao fina | Por keyword / por geo |
| **Ahrefs** | Clickstream + GKP + ML | Media-alta — modelo proprio | Por keyword / geo |
| **Semrush** | Clickstream + GKP + ML | Media-alta — modelo proprio | Por keyword / geo |
| **Sistrix** | Visibilidade index + KW | Media (forte em DACH/EU) | Por keyword |
| **Bing Keyword Research** | Dados Bing/Edge | Util cruzado com Google | Por keyword |
| **Google Trends** | Indice relativo (0-100), nao volume absoluto | Alta para tendencia | Por tema / regiao |
| **GSC + GA4 cruzados** | Trafego real, conversao | Alta | Por keyword + valor |
| **Reddit / Quora / forums** | Volume implicito (numero de threads/views) | Indicativo, nao numerico | Por tema |

### 3.2 Vies a considerar

- **Sazonalidade** — "abadas carnaval" tem MSV mensal medio enganoso; concentrado em jan-fev.
- **Geografia** — MSV agregado nacional pode esconder concentracao regional.
- **Idioma** — pt-BR vs pt-PT sao mercados distintos; mesma palavra, intent diferente.
- **Anonimizacao GKP** — buckets 10/100/1k/10k. "330" e "440" podem cair no mesmo bucket.
- **Clickstream** — ferramentas privadas usam dados de painel + ML; podem subestimar nichos pequenos.
- **AI Overview** — query informacional pode ter MSV alto mas zero-click. Volume nao = oportunidade.
- **Bot traffic** — algumas plataformas filtram, outras nao.

### 3.3 Triangulacao recomendada

Para keyword critica, validar em **>= 3 fontes**:

1. GSC (se a query ja apareceu).
2. Google Keyword Planner (geo correto).
3. Ahrefs OU Semrush.
4. Cross-check com Google Trends (tendencia).

Diferencas grandes (>50%) entre fontes -> tratar como hipotese, escolher faixa, e marcar como "MSV indicativo, nao auditavel".

### 3.4 GSC como fonte mais confiavel para queries existentes

Search Console reporta:

- **Impressoes**: quantas vezes a query mostrou seu site.
- **Cliques**: quantos cliques recebeu.
- **CTR**: cliques / impressoes.
- **Posicao media**: posicao ponderada por impressao.

Limitacoes:
- GSC **anonimiza** queries com poucas impressoes (~50% das queries totais ficam ocultas em "Outros").
- Posicao media e media — pode esconder queries em posicoes muito diferentes.
- Filtro de pais e dispositivo crucial — nao olhar agregado.

> **Pratica do agente:** se a keyword ja apareceu na GSC do cliente, GSC e a fonte primaria. Se ainda nao apareceu, GKP + Ahrefs/Semrush + Trends.

---

## 4. Dificuldade de keyword (KD) — leitura critica

### 4.1 Modelos por ferramenta

| Ferramenta | Como calcula | Escala |
|------------|---------------|--------|
| **Ahrefs KD** | Quantidade de referring domains das paginas top 10 | 0-100 |
| **Semrush KD** | Mistura: backlinks + autoridade + volume + competidores | 0-100 |
| **Moz KD** | Combinacao de Page Authority + SERP features + intent | 0-100 |
| **Sistrix Difficulty** | Visibility-based + competidor | 0-100 |
| **Mangools KD** | Backlinks + LPS (Link Profile Strength) | 0-100 |
| **KGR (Keyword Golden Ratio — Doug Cunnington)** | (allintitle results) / MSV | <0.25 = oportunidade |

### 4.2 Por que KD e relativo, nao absoluto

KD = 30 NAO significa o mesmo para todos:

| Site | Domain Rating (Ahrefs) | KD 30 e... |
|------|------------------------|-----------|
| Dominio novo (DR <10) | <10 | Dificil — ainda sem autoridade |
| Dominio medio (DR 30-50) | 30-50 | Possivel com bom conteudo |
| Dominio forte (DR >70) | >70 | Trivial |

> **Frase-chave:** "KD nao e dificuldade da keyword. E dificuldade RELATIVA a sua autoridade. Sem ler sua propria autoridade, KD e numero solto."

### 4.3 Sinais qualitativos da SERP (alem do KD)

| Sinal | Implicacao |
|-------|------------|
| **Top 10 dominado por marcas globais** (Wikipedia, Amazon, Salesforce) | Dificil quebrar |
| **Top 10 com paginas especificas** (artigos de blog, nao homepages) | Possivel |
| **Diversidade de dominios** (10 dominios distintos) | Mais democratica |
| **Mesmas paginas em multiplas keywords** (cluster forte) | Topical authority em jogo |
| **Reviews/listicles de afiliados** dominando | Comercial — exige autoridade ou angulo unico |
| **AI Overview presente** | Zero-click — pesar ROI |
| **Featured Snippet ocupado por concorrente** | Roubavel se conteudo for melhor estruturado |

### 4.4 KGR (Keyword Golden Ratio) — Doug Cunnington

Formula:

```
KGR = allintitle_results / MSV
```

Onde:
- `allintitle_results` = numero de resultados em `allintitle:"keyword"` no Google.
- `MSV` = volume mensal de busca.

Interpretacao:
- KGR < 0.25 e MSV < 250 -> "Golden" (oportunidade de rankear rapido em domain novo).
- 0.25 <= KGR < 1 -> mediano.
- KGR >= 1 -> saturado.

> **Limitacao 2026:** Google ja nao mostra `allintitle:` com a mesma confiabilidade de 2018-2020. Resultado pode ser 0 mesmo havendo competidores. Usar como UM sinal entre varios, nao como unico criterio.

### 4.5 Heuristica pratica de "vale a pena ou nao"

```
SE (MSV > 0) E (intent claro) E (KD relativo viavel) E (ROI estimado positivo)
   E (sem cannibalization com pagina existente)
   E (alinhado a topical authority do site)
   ENTAO: criar conteudo
SENAO: descartar OU ajustar (long-tail, angulo unico, formato)
```

---

## 5. Intent profundo — alem dos 4 tipos classicos

### 5.1 Inferindo intent na pratica

Tres metodos:

**(1) Modificador lexical**
"como" -> informacional how-to.
"melhor" -> comercial.
"comprar" -> transacional.
"perto de mim" -> local transacional.

**(2) SERP atual (mais confiavel)**
Veja o que o Google ja decidiu mostrar:
- Top 3 dominado por tutoriais? -> Informacional.
- Top 3 com lojas/Shopping? -> Transacional.
- Mistura? -> Intent ambivalente / dividido.

**(3) PAA + related searches**
Perguntas relacionadas revelam o que o usuario REALMENTE quer alem da query digitada.

### 5.2 Intent dividido (mixed intent)

Quando a SERP mostra varios formatos, o intent e dividido. Exemplo: "pipedrive" pode ser navegacional (login) ou comercial (review). Decisao:

- **Atacar o intent dominante** (formato com mais resultados no top 5).
- OU **criar duas paginas** mapeadas para sub-intents distintos.

### 5.3 Intent fractional (Aleyda Solis)

Uma mesma keyword pode atender intents diferentes para personas diferentes:
- "CRM" para founder = pesquisa inicial -> informacional.
- "CRM" para head de vendas = avaliacao -> comercial.
- "CRM" para TI = avaliacao tecnica -> comercial-tecnica.

Implicacao: na mesma URL, cobrir os multiplos intents (estrutura modular: comparativo + tutorial + tabela tecnica).

### 5.4 Intent volátil

Intent pode mudar com o tempo. Casos classicos:
- "ChatGPT" — em nov/2022 era navegacional novo; em 2026 e ambivalente (login + review + alternativas).
- "fintech" — antes era informacional academico; hoje e comercial.

Reavaliar intent de keywords criticas em **revisoes trimestrais**.

---

## 6. Modificadores semanticos — biblioteca operacional

Catalogo de modificadores que ampliam keyword head em variacoes uteis. Usar como matriz: keyword head x modificador.

### 6.1 Modificadores informacionais

| Categoria | Exemplos |
|-----------|----------|
| Definicao | "o que e", "significado de", "definicao de" |
| Como-fazer | "como", "como fazer", "passo a passo", "tutorial" |
| Por que | "por que", "porque", "razao" |
| Onde | "onde", "onde encontrar", "onde fica" |
| Quando | "quando", "em que momento", "qual epoca" |
| Quem | "quem", "qual profissional", "quem faz" |
| Lista | "lista de", "X exemplos", "tipos de", "categorias" |
| Guia | "guia", "guia completo", "manual", "ebook" |
| Curso | "curso", "aprender", "treinamento" |

### 6.2 Modificadores comerciais

| Categoria | Exemplos |
|-----------|----------|
| Comparativo | "X vs Y", "comparacao", "diferenca entre" |
| Melhor / top | "melhor", "melhores", "top 10", "ranking" |
| Review | "review", "avaliacao", "opinioes", "vale a pena" |
| Alternativa | "alternativa a", "concorrente de", "como X" |
| Recomendacao | "recomendado para", "ideal para", "indicado para" |
| Custo-beneficio | "custo-beneficio", "barato e bom" |

### 6.3 Modificadores transacionais

| Categoria | Exemplos |
|-----------|----------|
| Compra | "comprar", "comprar online", "loja" |
| Preco | "preco", "quanto custa", "valor", "tabela de precos" |
| Desconto | "desconto", "cupom", "promocao", "black friday" |
| Trial | "trial", "teste gratis", "free trial", "demo" |
| Contratar | "contratar", "consultoria", "servico de" |
| Download | "download", "baixar" |
| Frete | "frete gratis", "entrega" |

### 6.4 Modificadores locais

| Categoria | Exemplos |
|-----------|----------|
| Geo explicito | "[cidade]", "[bairro]", "[regiao]", "perto de [ponto de referencia]" |
| Geo implicito | "perto de mim", "aqui", "proximo" |
| CEP | "[CEP]", "[primeiros 3 digitos do CEP]" |

### 6.5 Modificadores temporais

| Categoria | Exemplos |
|-----------|----------|
| Atualidade | "2026", "atual", "agora", "ultimas atualizacoes" |
| Sazonal | "ferias", "natal", "carnaval", "back to school" |
| Urgencia | "rapido", "urgente", "24h", "hoje" |

### 6.6 Modificadores de qualificador (long-tail expansion)

| Modificador | Exemplo aplicado a "CRM" |
|-------------|---------------------------|
| Persona | "CRM para vendedor", "CRM para founder" |
| Setor | "CRM para clinica medica", "CRM imobiliaria" |
| Porte | "CRM para pequena empresa", "CRM enterprise" |
| Geografia | "CRM brasileiro", "CRM em portugues" |
| Tecnologia | "CRM open source", "CRM no-code", "CRM com IA" |
| Integracao | "CRM com WhatsApp", "CRM integrado ao Shopify" |
| Funcionalidade | "CRM com automacao", "CRM com pipeline kanban" |
| Modelo de negocio | "CRM B2B", "CRM B2C", "CRM SaaS" |
| Preco | "CRM gratis", "CRM barato", "CRM ate R$100" |

> **Tecnica:** matriz keyword head x cada categoria de modificador gera dezenas a centenas de variacoes long-tail/micro-tail. Filtrar por intent + KD + ROI.

---

## 7. Long-tail e zero-volume strategy

### 7.1 Long-tail — por que importa

- ~50-70% das buscas no Google sao **unique queries** (nunca buscadas antes ou raramente).
- Long-tail tem **conversao mais alta** (intent mais especifico).
- Long-tail tem **competicao menor** (head terms saturados).
- Cluster de long-tails **constroi topical authority** — vetor de autoridade do dominio.

### 7.2 Zero-volume keywords — quando valem

Keywords reportadas com MSV = 0 ou "no data" frequentemente:

- **Tem volume real** (cauda fina nao agrupada na ferramenta).
- Sao **conversacionais** (alimentam AI Overview / SGE / LLM).
- Sao **especificas do produto** (ex.: "como configurar pipedrive com twilio sms" — 0 reportado mas alta intencao).
- **Aparecem em GSC** mesmo nao aparecendo em Ahrefs.

Estrategia:

1. **Extrair** zero-volume de fontes alternativas:
   - Reddit (search interno, ranking de threads ativas).
   - Quora.
   - Comentarios em concorrentes (Disqus, Facebook).
   - Suporte do produto (tickets, FAQ).
   - Vendas (objecoes recorrentes).
   - Sales call recordings (Gong, Chorus).
   - Comunidades Slack/Discord.

2. **Validar** em GSC (apos publicacao) — se aparece com >= 10 impressoes/mes, tem volume.

3. **Cluster** zero-volumes proximos em uma so URL densa (em vez de 1 URL por query).

### 7.3 KGR pipeline

```
1. Brainstorm de keywords long-tail (4+ palavras)
2. Para cada: buscar `allintitle:"keyword"` no Google (modo anonimo)
3. Calcular KGR = allintitle / MSV
4. Filtro: KGR < 0.25 E MSV < 250
5. Validar intent na SERP
6. Validar com GKP que MSV existe (mesmo em bucket)
7. Priorizar por valor (BOFU > MOFU > TOFU)
```

> **Realidade 2026:** KGR puro perdeu confiabilidade (Google nao mostra allintitle como antes). Mas o conceito — buscar long-tail com poucos competidores diretos — segue valido. Adaptar usando "site:[concorrente] keyword" para checar se concorrentes ja cobrem.

---

## 8. Pesquisa por entidades — Knowledge Graph e Wikidata

Google deixou de pensar em **strings** (palavras literais) e passou a pensar em **entities** (conceitos com atributos e relacoes). MUM, BERT, Knowledge Graph operam em entidades.

### 8.1 O que e uma entidade

- Pessoa, empresa, produto, lugar, evento, conceito.
- Com **identificador unico** no Knowledge Graph (`kgmid`).
- Com **atributos** (nome, fundacao, fundador, descricao).
- Com **relacoes** (Pipedrive -> CRM -> SaaS -> Sales).

### 8.2 Implicacoes para keyword research

- Buscar **entidades correlatas** alem de keywords textuais.
- Cobrir **atributos** da entidade (datas, fundadores, funcionalidades, alternativas).
- Linkar **fontes autoritativas** (Wikipedia, Wikidata, schema.org, sites oficiais) para reforcar a entidade.

### 8.3 Ferramentas

| Ferramenta | Uso |
|------------|-----|
| **Google Knowledge Graph Search API** | Buscar entidade pelo nome, pegar `kgmid` |
| **Wikidata Query Service** | SPARQL para extrair atributos/relacoes |
| **InLinks** | Identifica entidades em conteudo + cobertura |
| **WordLift** | Schema + entity reconciliation |
| **MarketMuse / Frase / Clearscope** | Topical relevance score baseado em entidades correlatas |
| **TextRazor / Google Cloud NLP** | Entity extraction de textos |

### 8.4 Schema.org como ponte

Usar schema.org/JSON-LD para **explicitar** a entidade ao Google:

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Pipedrive",
  "url": "https://www.pipedrive.com",
  "sameAs": [
    "https://www.wikidata.org/wiki/Q12345",
    "https://en.wikipedia.org/wiki/Pipedrive",
    "https://www.linkedin.com/company/pipedrive"
  ]
}
```

`sameAs` reconcilia a entidade com fontes autoritativas. Forte sinal para Google indexar como entidade.

---

## 9. Cluster topical — metodos praticos

### 9.1 Metodo manual (planilha)

```
COLUNAS (planilha de cluster):
- ID
- Keyword
- Tipo (head / body / long-tail / micro-tail)
- Intent (info / nav / com / trans / local)
- MSV (BR ou geo alvo)
- KD (escolher 1 ferramenta padrao)
- SERP feature (AI Overview / FS / PAA / nada)
- Subtopico
- Pillar associado
- URL alvo (existente ou nova)
- Status (publicado / planejado / descartado)
- Conversao alvo (baixa/media/alta)
- Prioridade (1-3)
```

Agrupamento por **subtopico** -> cluster.
Agrupamento por **pillar** -> hub-and-spoke.

### 9.2 Metodo SERP overlap

Para keywords A e B, comparar top 10 de cada:

- **Overlap >= 50%** -> mesmo cluster, possivelmente mesma URL.
- **Overlap 20-50%** -> mesmo cluster, URLs separadas mas linkadas.
- **Overlap < 20%** -> clusters diferentes.

Ferramentas: Keyword Insights, Surfer SEO, Semrush Keyword Strategy Builder.

### 9.3 Metodo entidades

Cluster por entidade central + sub-entidades:

```
[Entidade: CRM]
   ├── [SubEnt: Pipeline]
   │       ├── KW: o que e pipeline de vendas
   │       ├── KW: pipeline kanban
   │       └── KW: melhores ferramentas de pipeline
   ├── [SubEnt: Lead Scoring]
   │       └── ...
   └── [SubEnt: Automacao de vendas]
           └── ...
```

### 9.4 Metodo intent-stage

Cluster por intent x estagio do funil (matriz Secao 2.3).

```
                    TOFU (info)        MOFU (com.)         BOFU (trans.)
Tema A (CRM)      "o que e CRM"     "melhor CRM B2B"     "Pipedrive preco"
Tema B (Pipeline) "pipeline vendas"  "pipeline visual"   "Pipedrive trial"
Tema C (Auto.)    "automacao"        "ferramentas auto." "RD Station preco"
```

Cada celula = 1 ou mais URLs. Internal linking horizontal (mesmo estagio) e vertical (descer no funil).

---

## 10. Cannibalization detection

Cannibalization = 2+ paginas do mesmo dominio competindo pela mesma keyword. Resultado: Google escolhe uma com baixa convicao, alterna posicao, dilui autoridade.

### 10.1 Como detectar

1. **GSC > Performance > Pages** com filtro por query.
2. Se a query mostra **mais de 1 URL** com cliques significativos, ha cannibalization.

3. **Site search**: `site:dominio.com "keyword"` no Google.
   Se aparecem multiplas paginas relevantes, suspeitar.

4. **Ferramentas dedicadas**:
   - Ahrefs: aba "Cannibalization" no Site Explorer.
   - Semrush: Position Tracking + filtro "URL changed".
   - SE Ranking, Sitebulb, Screaming Frog (export + analise).

### 10.2 Como decidir

Para cada par cannibal:

| Cenario | Acao |
|---------|------|
| Paginas duplicadas (mesmo conteudo) | Escolher canonical, 301 outra |
| Paginas distintas mas competindo pelo mesmo intent | Consolidar em 1, 301 a outra |
| Paginas com intents distintos (ambivalente) | Diferenciar conteudo, ajustar title/H1, internal linking |
| Pagina nova canibalizou pagina antiga (que rankeava) | Revisar pagina nova ou despromover |

### 10.3 Prevencao

- Mapping URL <-> keyword unico antes de publicar.
- Revisao de cannibalization a cada novo cluster.
- Auditoria trimestral.

---

## 11. Branded vs non-branded — separacao critica

### 11.1 Por que separar

- **Branded** = queries com nome da marca. Ja sao pos-brand awareness.
- **Non-branded** = queries que NAO contem a marca. Sao captura genuina de novo publico.

Misturar oculta o crescimento real. Site pode ter "trafego organico crescente" puramente porque a marca cresceu — sem SEO real.

### 11.2 Como separar em GSC

```
GSC > Performance > Queries > Filtro "Query NAO contem [nome da marca]"
```

Salvar dois reports:
- **Branded performance**: query CONTEM marca.
- **Non-branded performance**: query NAO contem marca.

KPI mais fiel ao SEO: **trafego non-branded crescente**.

### 11.3 Defensive keywords

Branded keywords criticas que valem ser monitoradas:
- "[marca]" puro (top 1 obrigatorio).
- "[marca] login" (top 1 obrigatorio).
- "[marca] reclame aqui" / "[marca] e confiavel" / "[marca] golpe" (controlar narrativa).
- "[marca] vs [concorrente]" (defender comparativo).
- "[marca] alternativa" (alguns vao migrar — capturar com proposta de retencao).

---

## 12. PAA + Related Searches + AlsoAsked — mining sistematico

### 12.1 People Also Ask (PAA)

Caixas de pergunta na SERP. Cada pergunta:

- Reflete intent real do usuario.
- Pode ser **dinamica** (clicar gera mais).
- E forte sinal de **co-ocorrencia semantica**.

### 12.2 Mineracao

Ferramentas:
- **AlsoAsked.com** — visualiza arvore de PAA (gratis com limite).
- **AnswerThePublic** — questions, prepositions, comparisons.
- **Semrush PAA** — feature dedicada.
- **Ahrefs Keywords Explorer > Questions**.
- **Manual** — buscar a query, expandir 5 PAA, clicar, capturar mais 5, etc.

### 12.3 Aplicacao

1. Coletar 30-100 PAA de uma keyword head.
2. Agrupar por sub-intent.
3. Decidir: cobrir como **FAQ schema** numa unica URL, OU criar URLs separadas para PAA com volume proprio.
4. Schema FAQPage para FAQ visivel na SERP.

---

## 13. Featured Snippet keywords — formato para zero-position

### 13.1 O que rankeia em Featured Snippet

| Tipo | Estrutura |
|------|-----------|
| **Paragraph** | Definicao concisa (~40-60 palavras) logo apos H |
| **List (numerada/bullet)** | Lista clara em <ol> ou <ul> com itens curtos |
| **Table** | <table> com header semantico |
| **Video** | YouTube com timestamp + transcript |

### 13.2 Como otimizar

1. **Resposta no inicio**: primeira frase apos o H deve ser a resposta.
2. **40-60 palavras** para snippet de paragrafo.
3. **Listas explicitas** com <ol>/<ul>, NAO disfarcadas.
4. **Tabela com semantica HTML correta**.
5. **Schema.org QAPage / FAQPage** quando aplicavel.
6. **H2 espelhando a query** ("O que e X").
7. **Sub-headings em formato pergunta**.

### 13.3 Roubando Featured Snippet

Para keyword que ja tem FS de concorrente:

1. Analisar formato (paragrafo / lista / tabela).
2. Replicar formato com conteudo MAIS preciso/util.
3. Estrutura HTML mais limpa.
4. EEAT mais alto.
5. Aguardar (pode demorar dias-semanas).

---

## 14. AI Overview / SGE / LLM keywords — GEO/LLMO em 2026

### 14.1 O que mudou

- AI Overviews agregam **multiplas fontes** numa resposta sintetizada.
- ChatGPT search, Perplexity, Copilot, Claude consultam web e citam fontes.
- Queries em LLMs sao **mais longas, conversacionais, com contexto**.
- "Otimizacao para LLM" ainda em maturacao em 2026 — nao ha SOP universal.

### 14.2 Sinais de oportunidade em AI Overview

| Sinal | Implicacao |
|-------|------------|
| Site citado em AI Overview de keyword critica | Manter e replicar formato |
| Concorrente citado, voce nao | Auditar formato + autoridade do concorrente |
| AI Overview ausente | Ainda ha CTR organico tradicional |
| AI Overview com 0 fontes claras | Conteudo do site nao e estruturado o suficiente |

### 14.3 Como otimizar (LLMO / GEO — heuristica)

- **Resposta direta** no inicio do conteudo (TL;DR).
- **Estrutura semantica forte**: H, listas, tabelas, FAQ.
- **Fatos verificaveis** com fonte primaria linkada.
- **Schema.org rico**: Article, FAQ, HowTo, Product, Person, Organization.
- **EEAT** alto (autor real, credenciais, fonte, data).
- **Cobertura de entidade** completa (atributos + relacoes).
- **Atualizacoes frequentes** com `dateModified` schema.
- **Mencoes em fontes autoritativas** (digital PR para autoridade do dominio).
- **Linguagem natural conversacional** (espelhando como pessoas perguntam).
- **Disclosure** transparente.

### 14.4 Tracking de citacoes em AI

| Ferramenta | Cobertura |
|------------|-----------|
| **Profound** | AI Overviews + ChatGPT + Perplexity + Copilot |
| **Authoritas** | SGE / AI Overviews tracking |
| **BrightEdge Generative Parser** | Enterprise |
| **Mention / Brand24** | Mencoes amplas, nao especifico AI |
| **GSC Performance > Search Appearance** | Em rollout — Google promete metrica de AI Overview |

### 14.5 Hipotese de keyword research para LLM

Tipos de query que LLMs respondem bem (e citam):

- "Compare X e Y considerando [criterio]"
- "Resume [topico] em 5 pontos"
- "Quais sao alternativas a X?"
- "Como [topico] funciona em [contexto especifico]?"
- "Top [N] [coisa] para [persona]"
- "Tutorial de [topico] passo a passo"

Cobrir esses formatos de query no conteudo aumenta chance de citacao.

---

## 15. Local keywords — geo SEO

### 15.1 Estrutura

```
[servico] + [geo modifier]
[servico] + "perto de mim"
[geo] + [servico]
```

Exemplos:
- "advogado tributario em sao paulo"
- "marketing digital perto de mim"
- "rio de janeiro fotografo casamento"

### 15.2 Sinais locais relevantes

- **Google Business Profile** (antigo Google My Business) completo.
- **NAP consistency** (Name, Address, Phone) em todas as plataformas.
- **Reviews** quantidade + qualidade + recencia.
- **Local citations** (listings em diretorios — Yelp, Foursquare, plataformas BR como ApontaderoOnde, GuiaMais).
- **Localizacao nas paginas-chave** (texto, schema LocalBusiness, GeoCoordinates).
- **Conteudo local** (paginas por bairro/cidade).
- **Backlinks locais** (jornal local, associacao da cidade).

### 15.3 Multilocacoes

Site com multiplas filiais:
- 1 pagina por filial (com NAP, foto, mapa, depoimentos locais).
- Schema LocalBusiness por filial.
- Internal linking de hub geral -> paginas locais.

### 15.4 Local pack vs blue links

Top 3 do Local Pack (mapa) e separado dos blue links. Otimizar ambos:
- Local Pack: Google Business Profile.
- Blue links: SEO classico + paginas locais.

---

## 16. Sazonalidade e Google Trends

### 16.1 Tipos de sazonalidade

| Tipo | Exemplo |
|------|---------|
| **Anual** | "presente dia das maes" |
| **Trimestral** | "back to school" (jan-fev BR) |
| **Mensal** | "imposto de renda" (mar-abr) |
| **Semanal** | "almoco de domingo" |
| **Evento** | "black friday", "copa do mundo" |
| **Estrutural** | tendencia de longo prazo (subindo/descendo) |

### 16.2 Google Trends — leitura

- Indice 0-100 RELATIVO ao pico do periodo escolhido.
- NAO e volume absoluto.
- Util para: tendencia, comparativo entre keywords, geo, sazonalidade.

### 16.3 Workflow sazonal

```
JAN: planejar conteudo de mar-abr (volume sobe na sazonalidade)
   |
FEV: publicar (Google leva 2-8 semanas para indexar/rankear bem)
   |
MAR-ABR: pico de busca, conteudo ja rankeado
   |
MAI: revisar performance, aprender
   |
PROXIMO ANO: atualizar conteudo (manter URL, atualizar dateModified, fatos)
```

> **Padrao de erro:** publicar em mar quando o pico ja chegou. Sem indexacao + ranking, perde-se a janela.

---

## 17. Concorrencia — content gap e keyword gap

### 17.1 Keyword gap

Keywords que **concorrente rankeia** e **voce NAO**.

Ferramentas:
- Ahrefs: Site Explorer > Competing Domains > Content Gap.
- Semrush: Keyword Gap.
- Sistrix: Comparacao de visibilidade.

Output: lista de keywords + concorrente que rankeia + sua posicao (ou "n/a").

### 17.2 Content gap

Topicos que concorrente cobre e voce nao. Mais amplo que keyword gap.

Workflow:
1. Identificar 3-5 concorrentes diretos.
2. Listar todos os topicos cobertos por cada (auditoria de site).
3. Identificar overlap e gaps.
4. Priorizar gaps com volume + intent + alinhamento estrategico.

### 17.3 SERP gap (granular)

Para cada keyword critica:
1. Analisar top 10.
2. Mapear "fatores" que cada pagina tem (formato, profundidade, schema, EEAT, freshness).
3. Identificar que combinacao falta.
4. Construir conteudo que tenha essa combinacao + algo unico (dado original, expertise, formato).

---

## 18. Ferramentas — guia comparativo detalhado

### 18.1 Gratis / Oficiais

| Ferramenta | Forte em | Limitacao |
|------------|----------|-----------|
| **Google Search Console** | Queries reais com cliques/impressoes/CTR/posicao | So ve queries que ja apareceram para o seu site |
| **Google Keyword Planner** | Volume oficial Google (em buckets) | Buckets imprecisos; precisa conta Google Ads |
| **Google Trends** | Tendencia, sazonalidade, geo, comparativo | Indice relativo, nao volume absoluto |
| **Bing Webmaster + Keyword Research** | Equivalente do GSC + KGP para Bing | ~3-7% mercado |
| **Bing Search "related searches"** | Sugestoes laterais | Manual |
| **Google Search "People Also Ask" / Related** | Mining manual | Tedioso em escala |
| **YouTube Search Suggestions** | Tendencia em video | Especifico |
| **Reddit / Quora search** | Linguagem natural, perguntas reais | Volume implicito |

### 18.2 Pagas — All-in-one

| Ferramenta | Forte em | Faixa de preco USD/mes |
|------------|----------|------------------------|
| **Ahrefs** | Backlinks, KW research, content gap, site audit | 99-999+ |
| **Semrush** | KW research, position tracking, ads, content | 130-500+ |
| **Sistrix** | Visibilidade DACH/EU, Google updates tracking | 100-400+ |
| **Moz Pro** | DA/PA, link explorer, on-page grader | 99-599+ |
| **Mangools (KWFinder)** | KW research focado, custo-beneficio | 30-130 |
| **SE Ranking** | Tracking + audit, intermediario | 65-260 |
| **Serpstat** | KW + PPC + audit | 60-500 |
| **SpyFu** | Foco em ads + KW espionagem | 39-299 |

### 18.3 Pagas — Especializadas

| Ferramenta | Foco |
|------------|------|
| **AnswerThePublic** | Visualizacao de questions/preps/comparisons |
| **AlsoAsked** | Arvore PAA |
| **Keyword Insights** | Cluster automatizado por SERP overlap |
| **SurferSEO** | Brief + on-page SERP analysis |
| **Frase** | AI-assisted brief |
| **Clearscope** | Topical relevance score |
| **MarketMuse** | Topical authority + planning |
| **InLinks** | Entity SEO |
| **WordLift** | Schema + entity reconciliation |
| **SparkToro** | Audience research (alem de KW — onde audiencia esta) |
| **Profound** | Citacoes em AI Overview / ChatGPT / Perplexity |
| **Authoritas** | SGE tracking |
| **Search Console Insights** | GSC + GA4 unificado (Google) |

### 18.4 Comparativo simplificado

```
                Gratis  | Pago basico | Pago profissional
KW research:    GKP+GSC | KWFinder    | Ahrefs / Semrush
Backlinks:      GSC     | Mangools    | Ahrefs (lider)
Position track: GSC     | SE Ranking  | Semrush / Sistrix
Site audit:     Ligh.   | SE Ranking  | Screaming Frog + Ahrefs / Semrush
Content brief:  -       | Frase       | Surfer / Clearscope
AI tracking:    -       | Profound    | Authoritas / BrightEdge
```

> **Recomendacao default do agente:** Ahrefs OU Semrush (escolher 1) + Google Search Console + Google Keyword Planner + Google Trends. Adicionar Surfer/Frase para brief + Profound se AI Overview e relevante no nicho.

---

## 19. Workflow de pesquisa de keywords em 12 fases

```
KEYWORD RESEARCH — 12 FASES
=============================

FASE 1 — DESCOBERTA DO NEGOCIO
  [ ] Persona / ICP definida
  [ ] Modelo de negocio (B2B/B2C, SaaS/servico/produto)
  [ ] Geografia alvo
  [ ] Idioma (pt-BR, pt-PT, es, en)
  [ ] Concorrentes diretos (3-5)
  [ ] Funil + estagios

FASE 2 — SEED KEYWORDS
  [ ] Brainstorm com cliente: 20-50 termos iniciais
  [ ] Termos de produto, categoria, problema, solucao, benefit
  [ ] Sinonimos e jargao do nicho
  [ ] Termos de objecao (sales call recordings)

FASE 3 — EXPANSAO
  [ ] GKP: cada seed -> ideias
  [ ] Ahrefs/Semrush: matching terms, related, questions
  [ ] AnswerThePublic / AlsoAsked: PAA, prepositions
  [ ] Reddit/Quora: linguagem real
  [ ] YouTube/TikTok suggestions

FASE 4 — APLICACAO DE MODIFICADORES
  [ ] Matriz keyword head x modificadores (Secao 6)
  [ ] Long-tail expansion sistematica
  [ ] Local modifiers (se aplicavel)
  [ ] Temporal modifiers (sazonal)

FASE 5 — VOLUME E DIFICULDADE
  [ ] MSV via GKP + Ahrefs/Semrush (triangular)
  [ ] KD via ferramenta padrao
  [ ] Sinais qualitativos da SERP (Secao 4)
  [ ] Trends para tendencia
  [ ] Marcar "no data" como hipotese

FASE 6 — INTENT
  [ ] Buscar cada keyword em modo anonimo + geo correto
  [ ] Identificar formato dominante top 5
  [ ] PAA + related
  [ ] SERP features
  [ ] Marcar intent (info / nav / com / trans / local / misto)

FASE 7 — VALOR PARA O NEGOCIO
  [ ] Money / Supporting / Branding / Defensive
  [ ] Estagio do funil
  [ ] Conversao estimada (a partir de GA4 historico, se houver)
  [ ] Score de prioridade (1-3)

FASE 8 — CANNIBALIZATION CHECK
  [ ] site:dominio.com "keyword" para cada KW critica
  [ ] GSC > Pages com query
  [ ] Decidir: nova URL OU expandir existente

FASE 9 — CLUSTER E MAPPING
  [ ] Agrupar por subtopico/pillar
  [ ] Decidir 1 URL por cluster vs 1 URL por KW
  [ ] Mapear URL alvo (existente ou nova)
  [ ] Internal linking plan

FASE 10 — SERP GAP E ANGULO
  [ ] Para cada KW critica: top 10 atual
  [ ] Que combinacao de fatores ja existe?
  [ ] Que combinacao falta?
  [ ] Angulo unico (dado, expertise, formato)

FASE 11 — PRIORIZACAO
  [ ] Matriz Esforco x Impacto
  [ ] Quick wins: posicao 4-15 + volume + nao-cannibalizada
  [ ] Plano de 90 dias
  [ ] Distribuicao por funil

FASE 12 — ENTREGAVEIS
  [ ] Planilha keyword universe
  [ ] Mapping URL <-> KW
  [ ] Briefings SERP-first (top 10)
  [ ] Calendario editorial
  [ ] KPIs de monitoramento
  [ ] Cadencia de revisao (mensal + apos core update)
```

---

## 20. Templates

### 20.1 Template de planilha — keyword universe

```
| ID | Keyword | Tipo | Intent | MSV | KD | SERP feat. | Subtopico | Pillar | URL alvo | Status | Conv | Prio |
|----|---------|------|--------|-----|----|-----------:|-----------|--------|----------|--------|------|-----:|
| 1  | crm para startup | body | comercial | 1.2k | 38 | AI Overview, PAA | crm-startup | crm | /crm-startup | planejado | media | 1 |
| 2  | melhor crm b2b | body | comercial | 880 | 42 | listicles | crm-comparativo | crm | /melhor-crm-b2b | publicado | alta | 1 |
| 3  | como configurar pipeline pipedrive | micro-tail | informacional | 90 | 12 | nada | tutorial-pipedrive | crm | /tutorial-pipedrive | planejado | baixa | 2 |
```

### 20.2 Template de mapping URL <-> KW

```
URL: /crm-para-startup
KW principal: crm para startup
KW secundarias (intent compativel):
  - melhor crm para startup
  - crm de vendas para startup
  - como escolher crm para startup
KW NAO cobrir (cannibal risk):
  - crm enterprise (pagina diferente)
  - crm b2b (cluster diferente)
Schema: Article + FAQPage + Person (autor) + Organization
Internal link DE: /crm (pillar)
Internal link PARA: /crm-pricing-comparativo, /crm-funcionalidades, /como-implementar-crm
```

### 20.3 Template de quick win report

```
QUICK WINS (POSICAO 4-15 EM GSC)
=================================

| URL | Query | Pos atual | Impressoes/mes | CTR atual | Volume estimado | Intent | Acao recomendada |
|-----|-------|-----------|----------------|-----------|-----------------|--------|------------------|
| /seo-tecnico | "core web vitals 2026" | 8.2 | 1.200 | 1.1% | ~2k | info | Atualizar conteudo (CWV 2024 -> 2026), reforcar EEAT, schema |
| /pillar-crm  | "melhor crm para startup" | 11.5 | 540 | 0.4% | ~880 | com. | SERP-first rewrite, comparativo expandido, autor com credencial |
| /pricing | "pipedrive preco brasil" | 6.8 | 380 | 2.8% | ~440 | trans. | Tabela em portugues, ressalva de cambio, FAQ schema |
```

### 20.4 Template de brief de cluster

```
CLUSTER: CRM-STARTUP

Pillar: /crm-para-startup (~3500 palavras)
  - H1: CRM para startup: guia 2026
  - H2-1: O que startup precisa de CRM (vs empresa estabelecida)
  - H2-2: Funcionalidades essenciais
  - H2-3: Comparativo top 5 (Pipedrive, RD, HubSpot, Agendor, Folk)
  - H2-4: Quanto custa um CRM para startup
  - H2-5: Como implementar em 30 dias
  - H2-6: FAQ

Spokes (5):
  1. /pipedrive-startup-review (1500 palavras) - intent comercial
  2. /como-implementar-crm-30-dias (2000 palavras) - intent how-to
  3. /crm-gratis-startup (1200 palavras) - intent transacional/com.
  4. /pipeline-vendas-startup (1500 palavras) - intent informacional
  5. /pipedrive-vs-rd-station (1800 palavras) - intent comparativo

Internal linking:
  - Pillar -> cada spoke (com anchor descritivo, nao "leia mais")
  - Spoke -> pillar (no inicio, contextualizacao)
  - Spoke -> spoke (transversal, quando topico se cruza)

Autor: [Nome] (especialista em vendas SaaS, X anos, links LinkedIn/Lattes/cases)

Schema:
  - Pillar: Article + Person (autor) + Organization + BreadcrumbList + FAQPage
  - Spokes: Article + Person + (HowTo onde aplicavel) + BreadcrumbList

KPIs:
  - Posicao top 10 em "crm para startup" (pillar) em 6 meses
  - Posicao top 5 em 5 long-tails dos spokes em 4 meses
  - Trafego non-branded organico do cluster: 5k visitas/mes em 9 meses
  - Conversao de leads: 50/mes em 12 meses
```

---

## 21. Regras de Ouro para o agente `frank-mkt` (modo SEO/keywords)

1. **NAO CHUTAR volume, KD, posicao, CTR, citacao em AI Overview** — sem dado de ferramenta, marcar como hipotese explicita ou pedir acesso.
2. **Triangular MSV em 3 fontes** quando keyword e critica.
3. **KD e relativo, nao absoluto** — sempre cruzar com autoridade do dominio do cliente.
4. **Confirmar intent na SERP atual**, nao supor pelo modificador lexical.
5. **Branded vs non-branded SEMPRE separados** em report.
6. **Cannibalization check** antes de publicar.
7. **Long-tail e zero-volume tem valor** — nao descartar pela ferramenta.
8. **Cluster topical > volume bruto** — autoridade vem de cobertura.
9. **AI Overview / SGE pesa no ROI** de keywords informacionais — ajustar expectativa.
10. **GSC e fonte primaria** para queries que ja apareceram. Ferramentas terceiras sao secundarias.
11. **Sazonalidade muda decisao** — publicar antes do pico, atualizar antes do proximo ciclo.
12. **Helpful Content System rebaixa site inteiro** — keyword research nao salva conteudo nao-util. KW boa + conteudo medioco = nao publica.

---

## 22. Exemplos comportamentais — keyword research

### Exemplo 1 — Cliente quer rankear em head term inalcansavel

**Input:** "Quero rankear em primeiro em `CRM` no Google."

**Resposta esperada do agente:**
> CORRIGE: "Head term `CRM` no Brasil tem volume alto (validar em GKP — provavel >100k/mes) e e dominado por marcas globais com autoridade construida em 10-20 anos (Salesforce, HubSpot, RD Station, Pipedrive). Para um dominio com DR baixo, ranking top 1 em `CRM` puro e proximo de impossivel em horizonte de <2 anos. Estrategia realista: cluster de long-tail com intent qualificado e progresso para body terms ao longo de 12-18 meses. Sugestao concreta: cluster `crm para startup` (volume body validado em ferramenta), com 1 pillar + 5-8 spokes cobrindo subtopicos (gratis, comparativo, integracao, implementacao, persona especifica, setor especifico). Ranking top 5 em 6-9 meses se EEAT e link building forem feitos. Body term `crm para startup` (provavel ~1k MSV) tipicamente converte 3-5x melhor que `CRM` puro. Antes de fechar plano: validar volume, KD, intent e SERP gap em ferramenta + confirmar autoridade atual do cliente em GSC + Ahrefs."

**Comportamento-chave:** rejeita head term inalcansavel, propoe cluster long-tail viavel, exige validacao em ferramenta antes de fechar plano, separa volume bruto de valor de negocio.

### Exemplo 2 — Volume reportado 0 mas keyword vale a pena

**Input:** "Pesquisei `como integrar pipedrive com twilio sms` e o Ahrefs reporta volume 0. Descarta?"

**Resposta esperada do agente:**
> Nao descarta automaticamente. "Volume 0 em Ahrefs significa: (1) keyword pode ter volume real abaixo do threshold de medicao (~10/mes), nao sendo agrupavel; (2) e zero-volume real. Validar antes de descartar: (a) GSC do cliente — alguma impressao? (b) Tickets de suporte — clientes pediram essa integracao? (c) Vendas — surge em call? (d) Reddit/Quora — alguem perguntou? Se SIM em pelo menos 1 sinal, vale criar conteudo. Conteudo de zero-volume tem 2 efeitos colaterais positivos: alimenta AI Overview / Perplexity / ChatGPT (queries conversacionais), e fortalece topical authority do cluster integracao-pipedrive. Estrategia: NAO criar URL dedicada. Adicionar como secao em pagina de cluster (ex.: pillar `integracao pipedrive` com H2 dedicado a Twilio + outras integracoes). Resultado: 1 pagina densa cobrindo 10-20 zero-volumes do mesmo subcluster, indexada e citada em AI search."

**Comportamento-chave:** distingue zero-volume real de cauda fina nao-medida, oferece sinais alternativos de validacao, propoe arquitetura economica (1 pagina cobrindo varias zero-volumes).

### Exemplo 3 — Cannibalization detectada

**Input:** "GSC mostra 2 paginas competindo em `marketing digital para advogados`. O que fazer?"

**Resposta esperada do agente:**
> Diagnostico antes de acao: "Analisar: (1) qual pagina rankeia mais alto historicamente? (2) qual tem mais cliques + impressoes + CTR melhor? (3) qual tem mais backlinks externos? (4) qual cobre intent melhor (avaliar SERP atual da KW)? (5) sao realmente o mesmo intent ou variacoes (ex.: tutorial vs comparativo de agencias)? Cenarios: (A) Mesmo intent + uma pagina claramente superior -> consolidar (canonical da fraca para a forte; OU 301 + content merge). (B) Intent realmente diferente (ex.: 1 e tutorial, outra e listicle de agencias) -> diferenciar title/H1, ajustar conteudo para cada sub-intent, internal linking explicito. (C) Sub-paginas legitimas de cluster -> manter, garantir canonical autorreferencial e diferenciacao topica. Antes de 301 ou canonical, exportar backlinks externos da pagina a despromover (Ahrefs > Backlinks) — outreach posterior para atualizar links importantes para nova URL. Apos a acao: monitorar GSC > Performance da query por 30-90 dias; pode haver oscilacao temporaria."

**Comportamento-chave:** rejeita acao automatica, exige diagnostico, oferece arvore de cenarios + acao por cenario, alerta sobre backlinks como ativo a preservar.

### Exemplo 4 — Cliente pede keyword research "para ChatGPT"

**Input:** "Quero otimizar conteudo para aparecer no ChatGPT e Perplexity. Como fazer keyword research disso?"

**Resposta esperada do agente:**
> Frame: "Generative Engine Optimization (GEO) / LLMO ainda em maturacao em 2026 — sem SOP universal, mas heuristica solida ja existe. Diferencas-chave em relacao a SEO classico: (1) queries em LLM sao MAIS LONGAS e CONVERSACIONAIS (`compare X e Y considerando custo e curva de aprendizado para time pequeno`); (2) LLMs respondem com SINTESE de varias fontes — nao basta ser top 1, precisa ser CITAVEL; (3) sem clique direto na maior parte dos casos — tracking via Profound/Authoritas, nao GSC. Workflow adaptado: (a) base normal de keyword research (Secao 19); (b) expandir cada KW em forma conversacional ('como X funciona', 'qual e a melhor opcao para Y', 'liste alternativas a Z'); (c) cobrir cada query com resposta direta no inicio do conteudo (TL;DR), estrutura semantica forte (H, listas, tabelas, FAQ schema), fatos verificaveis com fonte primaria, EEAT alto; (d) incluir entidade central + atributos + relacoes (schema.org sameAs com Wikipedia/Wikidata); (e) atualizar `dateModified` quando dados mudam; (f) tracking em Profound mensal — quais queries citam meu site? quais citam concorrentes? quais sao zero-share? Realista: GEO complementa SEO, nao substitui — manter cluster classico + camada de otimizacao GEO."

**Comportamento-chave:** distingue maturidade da pratica (heuristica > SOP), conecta com fundamentos (Secao 14 de seo-fundamentos), aponta tracking apropriado, ressalta que GEO complementa em vez de substituir.

---

## 23. Checklist de Contraditorio Interno — keyword research

| # | Pergunta destruidora | O que busca |
|---|----------------------|-------------|
| 1 | O **volume foi triangulado em pelo menos 3 fontes** (GKP + GSC + Ahrefs/Semrush + Trends), ou e numero de fonte unica? | Anti-chute de MSV |
| 2 | O **intent foi confirmado na SERP atual** em modo anonimo + geo correto, ou foi inferido apenas pelo modificador lexical? | Anti-suposicao de intent |
| 3 | A **dificuldade (KD) foi cruzada com a autoridade atual do dominio do cliente** (DR/DA + GSC), ou foi tratada como absoluta? | KD relativo |
| 4 | Existe **risco de cannibalization** com pagina ja publicada? Foi feito `site:dominio "keyword"` + GSC > Pages? | Cannibalization check |
| 5 | A keyword tem **AI Overview / SGE ativo na SERP**? Se sim, qual a expectativa de zero-click e como o ROI se ajusta? | Realidade SERP 2026 |
| 6 | **Branded vs non-branded** estao separados em todos os reports e KPIs? | Crescimento real, nao da marca |
| 7 | A **sazonalidade** foi considerada (Google Trends 12-24 meses)? O calendario editorial publica ANTES do pico? | Janela de oportunidade |
| 8 | A **localizacao e idioma** estao corretos (BR vs PT vs EN-US, geografia alvo)? | Anti-confusao geo/idioma |
| 9 | A **conversao historica** desse tipo de keyword foi considerada (GA4 por canal organic + segmentacao por landing), ou so o volume bruto? | KPI de negocio, nao vaidade |
| 10 | O **cluster faz sentido topical** (sub-entidades reais, SERP overlap, internal linking natural), ou foi forcado a partir de planilha sem analise de SERP? | Topical authority autentica |

---

## 24. Referencias canonicas

### 24.1 Oficiais

- **Google Search Console** — https://search.google.com/search-console
- **Google Keyword Planner** — https://ads.google.com/aw/keywordplanner/home
- **Google Trends** — https://trends.google.com
- **Google Search Central — Keyword Research** (orientacao geral) — https://developers.google.com/search/docs
- **Google Knowledge Graph Search API** — https://developers.google.com/knowledge-graph
- **Bing Webmaster Tools — Keyword Research** — https://www.bing.com/webmasters/help/keyword-research-tool-7e57e7e2
- **Wikidata** — https://www.wikidata.org
- **schema.org** — https://schema.org

### 24.2 Bibliografia profissional

- **Ahrefs Blog — Keyword Research** — https://ahrefs.com/blog/keyword-research/
- **Semrush Blog — Keyword Research** — https://www.semrush.com/blog/keyword-research/
- **Moz — Keyword Research** — https://moz.com/learn/seo/keyword-research
- **Backlinko — Keyword Research Guide** (Brian Dean — referencia popular, com ressalvas)
- **Aleyda Solis — Crawling Mondays** — https://www.aleydasolis.com
- **Doug Cunnington — KGR (Keyword Golden Ratio)** — https://nichesiteproject.com (referencia historica)
- **Koray Tugberk Gubur — Holistic SEO / Topical Authority** — https://www.holisticseo.digital
- **Lily Ray — EEAT/YMYL** — Twitter/X / Search Engine Land
- **Glenn Gabe** — analise de core updates / keyword visibility
- **SparkToro** — audience research

### 24.3 Ferramentas (sites)

- Ahrefs — https://ahrefs.com
- Semrush — https://www.semrush.com
- Sistrix — https://www.sistrix.com
- Moz Pro — https://moz.com/pro
- Mangools — https://mangools.com
- SE Ranking — https://seranking.com
- Serpstat — https://serpstat.com
- AnswerThePublic — https://answerthepublic.com
- AlsoAsked — https://alsoasked.com
- SurferSEO — https://surferseo.com
- Frase — https://www.frase.io
- Clearscope — https://www.clearscope.io
- MarketMuse — https://www.marketmuse.com
- Keyword Insights — https://www.keywordinsights.ai
- InLinks — https://inlinks.com
- WordLift — https://wordlift.io
- SparkToro — https://sparktoro.com
- Profound — https://www.tryprofound.com
- Authoritas — https://www.authoritas.com

### 24.4 Padroes / Referencias correlatas

- **RFC 9309 — Robots Exclusion Protocol** — https://www.rfc-editor.org/rfc/rfc9309
- **Sitemaps protocol** — https://www.sitemaps.org

### 24.5 Brasil

- **CONAR** — https://www.conar.org.br
- **CDC (Lei 8.078/1990)** — http://www.planalto.gov.br/ccivil_03/leis/l8078compilado.htm
- **LGPD (Lei 13.709/2018)** — http://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm
- **IAB Brasil** — https://iabbrasil.com.br

---

## 25. Referencia cruzada de skills

| Situacao | Skills relacionadas |
|----------|----------------------|
| Plano de conteudo organico | `seo-fundamentos` + `seo-keywords` + `conteudo-evergreen` + `copywriting-conversao` |
| Brief de pagina nova (SERP-first) | `seo-keywords` + `seo-on-page` + `copywriting-conversao` |
| Auditoria de site | `seo-fundamentos` + `seo-tecnico` + `seo-keywords` (cannibalization, gap) |
| Drop apos core update | `seo-fundamentos` + `seo-keywords` (re-mapping intent) + `manutencao-skills` |
| Cluster topical | `seo-keywords` + `conteudo-evergreen` + `analise-concorrencia` |
| Estrategia de autoridade | `seo-keywords` + `seo-link-building` + `comunicacao-corporativa` |
| Otimizacao para AI Overviews / LLM | `seo-keywords` + `seo-on-page` + `seo-fundamentos` (Secao 14 SGE) |
| Pesquisa de persona (alinhar intent) | `seo-keywords` + `persona-icp` + `analise-concorrencia` |
| Sazonalidade / calendario editorial | `seo-keywords` + `tendencias-trendwatching` + `branding` |
| Local SEO | `seo-keywords` + `seo-on-page` (LocalBusiness schema) + `comunicacao-corporativa` |
| Conteudo afiliado/patrocinado | `seo-keywords` + `conhecimento-conar-cdc` + `copywriting-conversao` |

---

## 26. Integracao com o ecossistema Frank-MKT

Esta skill integra-se ao agente principal `frank-mkt` (`agents/frank-mkt.md`) e ao restante do plugin da seguinte forma:

- **Pre-requisito obrigatorio: `seo-fundamentos`** — esta skill PRESSUPOE que o agente ja carregou `seo-fundamentos` (modelo mental crawl/render/index/rank, EEAT, HCS, Spam Policies, CWV, AI Overviews). Sem essa base, recomendacoes de keyword viram operacao isolada sem racional estrategico.
- **Acoplamento com `seo-on-page`** — depois que esta skill define keyword + intent + cluster + URL alvo, `seo-on-page` instrui como otimizar a pagina (title, meta, H, schema, internal linking, copy estruturada). Output desta skill alimenta input daquela.
- **Acoplamento com `seo-tecnico`** — em auditorias, esta skill identifica keywords com queda de visibilidade; `seo-tecnico` investiga causa-raiz quando o problema e indexacao, render, CWV, canonical.
- **Acoplamento com `conteudo-evergreen`** — cluster topical desta skill alimenta plano de pillar/cluster da `conteudo-evergreen`. Aquela skill detalha pillar pages, hub-and-spoke, atualizacao continua, decay temporal de conteudo.
- **Acoplamento com `seo-link-building`** — keywords money + KD relativo alto -> alvo prioritario de digital PR. Esta skill define alvos; `seo-link-building` define tatica de aquisicao.
- **Acoplamento com `analise-concorrencia`** — content gap + keyword gap dependem de `analise-concorrencia` para identificar concorrentes diretos e benchmarkar visibilidade. Saidas correlatas.
- **Acoplamento com `persona-icp`** — intent fractional (Secao 5.3) requer persona definida. Sem ICP, intent vira chute. Esta skill puxa output de `persona-icp` para qualificar keywords por persona/estagio.
- **Acoplamento com `copywriting-conversao`** — keyword com intent transacional alimenta brief para copy de landing/anuncio. Esta skill entrega keyword + intent + sub-queries; `copywriting-conversao` entrega copy.
- **Acoplamento com o agente `auditor`** — auditor roda regras PASS/FAIL em plano de keywords (volume validado? intent confirmado? cannibalization checada? GSC integrado?). Esta skill fornece o framework normativo.
- **Acoplamento com o agente `perfilador-mercado`** — share of voice, share of SERP feature, share of AI Overview citations sao output cruzado entre esta skill e perfilador-mercado.
- **Acoplamento com `conhecimento-search-console`** — esta skill instrui que GSC e fonte primaria; aquela skill instrui mecanica avancada de GSC (filtros, regex, comparativo, exportacao para BigQuery).
- **Acoplamento com `conhecimento-ga4`** — valor de keyword (conversao real) requer GA4 conectado. Aquela skill instrui mecanica de eventos, conversoes, atribuicao.
- **Acoplamento com `conhecimento-conar-cdc`** — keywords transacionais com claim ("melhor", "mais barato", "garantido") cruzam com regulacao publicitaria BR. Disclosure obrigatorio em afiliado/patrocinado.
- **Memoria e rastreabilidade** — keyword universe, mapping URL <-> KW, briefings, calendarios editoriais sao persistidos em `.frank-mkt/seo/<cliente>/<data>/keywords/` pelo agente `suporte-documental` (a criar) ou diretamente pelo `frank-mkt`. Versionar para revisar evolucao temporal e impacto de core updates.
- **Contraditorio interno** — o agente principal aciona o modulo `contraditorio-interno` carregando o Checklist da Secao 23 desta skill antes de entregar plano, briefing ou recomendacao de keywords.
- **Decaimento temporal** — esta skill esta em volatility `medium` (6 meses). Re-grounding obrigatorio em fontes da Secao 24 antes de citar fato volatil (metodologia de KD, threshold de KGR, citacoes em AI, mudanca de ferramenta) em peca formal.
- **Regra de ouro para `frank-mkt`** — nenhuma entrega que envolva keyword sai do plugin sem passar por esta skill; isso inclui briefings, planos de conteudo, calendarios editoriais, auditorias, planos de cluster, e respostas a `quais keywords devo trabalhar`.

---

> **Aviso:** o plugin `frank-mkt` e um assistente de analise. Recomendacoes desta skill devem ser adaptadas a realidade de cada cliente, mercado, autoridade do dominio e nicho, e validadas em ferramenta + GSC + GA4 antes de aplicar em peca formal. Keyword research e disciplina dinamica — Google muda metodologia silenciosamente; ferramentas tambem. AI Overview / SGE / LLM-search ainda em maturacao em 2026.

---

*Plugin `frank-mkt` — skill `seo-keywords` (v0.1.0)*
*Ultima atualizacao: 2026-05-07*
