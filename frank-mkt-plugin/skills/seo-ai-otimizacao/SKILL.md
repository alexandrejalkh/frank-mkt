---
name: seo-ai-otimizacao
description: "SEO em sites feitos com IA + otimizacao para motores generativos (GEO/LLMO/AEO). Parte I — sites construidos com AI builders (Lovable, v0, Bolt, Cursor, Replit Agent, Webflow AI, Wix AI, Framer AI, Hostinger, Squarespace AI): problema central CSR/SPA, fixes via prerender (Prerender.io, LovableHTML, DataJelly) ou migracao SSR/SSG (TanStack Start, Next.js, Astro), receitas por builder. Parte II — GEO (Generative Engine Optimization) / LLMO / AEO: como ChatGPT/Google AI Overview/Perplexity/Claude/Bing Copilot/Gemini descobrem, recuperam e citam; 3 fatores de citacao (structure + domain authority + freshness); answer-first content (40-60 palavras + BLUF), 120-180 palavras entre headings, sequential H1>H2>H3 (3x mais citacao em ChatGPT), conteudo atualizado <30d (3.2x), trust profiles (Trustpilot/G2/Capterra/Yelp = 3x), brand mention + co-citation, content chunks (200-500 chars), entity coverage, tracking (Profound/Authoritas/BrightEdge). Parte III — llms.txt (spec Jeremy Howard set/2024, markdown na raiz, status 2026, Yoast plugin, llms-full.txt). Parte IV — AI bots (GPTBot, OAI-SearchBot, ClaudeBot, PerplexityBot, Google-Extended, Meta-ExternalAgent + Bytespider non-compliant). Parte V — schema.org para AI content (Author + sameAs, IPTC DigitalSourceType TrainedAlgorithmicMedia). Parte VI — Helpful Content + AI generated (Google posicao oficial 2026). Workflow + anti-patterns + templates."
user-invocable: false
last_verified: 2026-05-07
next_review: 2026-08-07
volatility: high
regrounding_sources:
  - "https://developers.google.com/search/docs/fundamentals/using-gen-ai-content"
  - "https://developers.google.com/search/docs/fundamentals/creating-helpful-content"
  - "https://llmstxt.org"
  - "https://docs.lovable.dev/tips-tricks/seo-geo"
  - "https://platform.openai.com/docs/bots"
  - "https://docs.anthropic.com/en/docs/agents-and-tools/web-fetch-tool"
  - "https://developers.google.com/search/docs/crawling-indexing/google-extended"
  - "https://www.tryprofound.com"
  - "https://searchengineland.com/seo-2026-higher-standards-ai-influence-web-catching-up-473540"
  - "https://www.convertmate.io/research/geo-benchmark-2026"
---

# Skill: seo-ai-otimizacao

> **Decaimento Temporal**
> Ultima verificacao: 2026-05-07 | Proxima revisao: 2026-08-07 | Volatility: **high** (3 meses)
> AI builders adicionam SSR rapidamente (Lovable -> TanStack Start abr/2026; Bolt Cloud SSR mid-2025); novos AI bots aparecem; politicas de Google sobre AI content sao atualizadas; standards (`llms.txt`) ainda em maturacao. **Re-validar TUDO antes de publicar peca formal:**
> - Google Search Central — Gen AI content guidance — https://developers.google.com/search/docs/fundamentals/using-gen-ai-content
> - llmstxt.org (especificacao oficial) — https://llmstxt.org
> - OpenAI bots — https://platform.openai.com/docs/bots
> - Anthropic agent identification — https://docs.anthropic.com/en/docs/agents-and-tools/web-fetch-tool
> - Google-Extended — https://developers.google.com/search/docs/crawling-indexing/google-extended
> - Lovable docs SEO/GEO — https://docs.lovable.dev/tips-tricks/seo-geo
> - Search Engine Land "SEO in 2026" — https://searchengineland.com/seo-2026-higher-standards-ai-influence-web-catching-up-473540
> - GEO Benchmark Study 2026 — https://www.convertmate.io/research/geo-benchmark-2026
>
> **Acionamento:** site feito com AI builder (Lovable/v0/Bolt/Cursor/Replit/Webflow AI/Wix AI/Framer AI), CSR/SPA com cobertura GSC ruim, plano de GEO/LLMO/AEO, otimizacao para citacao em ChatGPT/AI Overview/Perplexity/Claude/Copilot, llms.txt, AI bots robots.txt, schema para AI content, disclosure de AI generated.
> **Skills relacionadas:** `seo-fundamentos` (carrega ANTES; modelo mental crawl/render/index/rank, EEAT, HCS, AI Overview), `seo-tecnico` (Secao 11 render CSR/SSR/SSG/ISR), `seo-on-page` (schema, EEAT visivel, anatomia), `seo-keywords` (intent que LLMs respondem), `conteudo-evergreen` (HCS-proofing, scaled abuse), `seo-link-building` (autoridade + brand mention).
> **Pre-requisito:** `seo-fundamentos` + `seo-tecnico` + `seo-on-page` carregadas.

---

## 1. Visao Geral

Esta skill cobre **dois eixos** que convergiram em 2026:

1. **Sites CONSTRUIDOS com IA** — AI builders (Lovable, v0, Bolt, Cursor, Replit Agent, Webflow AI, Wix AI, Framer AI, Hostinger AI, Squarespace AI) geram **SPAs com client-side rendering (CSR)**. Resultado: Googlebot indexa parcialmente, AI crawlers e social platforms NAO executam JS — vendo HTML vazio. Sem fix, site nao rankeia e nao e citado.
2. **Otimizacao para AI search engines (GEO / LLMO / AEO)** — Generative Engine Optimization (cite-se em ChatGPT, Perplexity, Google AI Overviews, Bing Copilot, Claude, Gemini) tornou-se discipline propria com fatores de ranking distintos do SEO tradicional.

Ambos sao **alta volatility** (re-validacao a cada 3 meses): AI builders evoluem (Lovable lancou TanStack Start com SSR em abr/2026), novos AI bots aparecem, padroes (`llms.txt`) ainda em maturacao, politicas Google sobre AI content sao revisadas.

### 1.1 Estrutura desta skill

| Parte | Tema |
|-------|------|
| **I** | Sites feitos com AI builders — diagnostico, fixes (prerender vs SSR/SSG), receitas por builder |
| **II** | GEO / LLMO / AEO — como LLMs citam, fatores quantitativos 2026, tecnicas |
| **III** | `llms.txt` — especificacao, status 2026, exemplos |
| **IV** | AI bots e robots.txt — 6 bots criticos, training vs search, Bytespider non-compliant |
| **V** | Schema.org para AI content — disclosure, atribuicao, IPTC DigitalSourceType |
| **VI** | Helpful Content + AI — Google posicao oficial 2026, EEAT em AI content |
| **VII** | Workflow + templates + anti-patterns |

### 1.2 Acionamento

| Gatilho | Exemplo |
|---------|---------|
| Site novo com Lovable / v0 / Bolt | "fiz site com Lovable, GSC mostra 0 paginas indexadas" |
| Migracao de WordPress para AI builder | "vamos migrar pra v0, vai funcionar pra SEO?" |
| Nao aparece em ChatGPT / AI Overview | "concorrente e citado em ChatGPT, eu nao" |
| Plano GEO / LLMO | "queremos virar fonte autoritativa para LLMs" |
| llms.txt | "vale implementar llms.txt em 2026?" |
| AI bots robots.txt | "como bloquear treinamento mas permitir AI search?" |
| Schema para AI content | "publicamos infografico AI-generated, marcar como?" |
| Disclosure de AI content | "blog usa IA + revisao humana, precisa disclosure?" |

### 1.3 Pre-requisitos

- [ ] **`seo-fundamentos` + `seo-tecnico` + `seo-on-page` carregadas**.
- [ ] **GSC + GA4** acessiveis.
- [ ] **Stack identificada**: builder usado, render mode, framework, CDN.
- [ ] **Acesso ao codigo / build** (Lovable Code Connect, v0 deploy, Bolt repo, etc.).
- [ ] **Profound ou Authoritas** (ou similar) para tracking de citacoes em AI.
- [ ] **Politica editorial** sobre uso de IA no conteudo (transparencia, autor, revisor).

> **Cristal C0 — NAO CHUTAR.** Esta area muda rapidamente. Toda recomendacao deve ser cruzada com fonte oficial atualizada antes de aplicar (volatility `high` — re-validar a cada 3 meses).

---

# PARTE I — Sites construidos com AI builders

## 2. O cenario 2026

### 2.1 AI builders dominantes

| Builder | Stack default | SSR/SSG nativo? | Foco |
|---------|---------------|------------------|------|
| **Lovable** | React + Vite | **Parcial em 2026** — TanStack Start com SSR rolling out (abr/2026); projetos antigos ainda Vite SPA puro | Full-stack apps com Supabase |
| **v0 (Vercel)** | Next.js | **Sim** — SSR/ISR via Next.js padrao | UI components + apps |
| **Bolt.new (StackBlitz)** | Variavel (React, Vue, Svelte, etc.) | **Bolt Cloud (mid-2025) adiciona SSR**; Bolt classico via Netlify foi CSR | Prototipos rapidos |
| **Cursor / Replit Agent** | Variavel | Depende do que IA gerar | Dev tooling + apps |
| **Webflow AI** | Webflow CMS | **SSG nativo** | Sites content-heavy |
| **Wix AI** | Wix | **SSR Wix** | Pequenos negocios |
| **Framer AI** | Framer | **SSR Framer** | Design-first |
| **Hostinger AI** | Variavel | **SSR/SSG** | Custo-beneficio |
| **Squarespace AI** | Squarespace | **SSR Squarespace** | Conteudo estavel |
| **Mocha** | Variavel | Variavel | Apps |

### 2.2 Problema central — CSR/SPA

Lovable, v0 (configurado mal), Bolt classico, Cursor (depende do prompt), Replit Agent (idem) tipicamente geram **SPA com CSR**:

```
USUARIO          GOOGLEBOT       AI CRAWLER (GPTBot, ClaudeBot, PerplexityBot)
   |                |                       |
   v                v                       v
HTML vazio      HTML vazio              HTML vazio
   |                |                       |
JS executa     2-pass: tenta render    GIVE UP — nao executa JS
   |           se atraso, indexa
Conteudo!      parcial                  CONTEUDO INVISIVEL
```

**Implicacoes:**

- **Google**: indexacao em 2 passes (HTML + render JS posterior) funciona para a maioria, mas **atrasa** indexacao e **falha em sites pesados em JS / com timeouts**.
- **AI crawlers** (GPTBot, ClaudeBot, PerplexityBot, OAI-SearchBot, Google-Extended): **NAO executam JS**. Conteudo dinamico = invisivel = **0 chance de citacao em ChatGPT, Perplexity, AI Overview**.
- **Social** (Facebook, LinkedIn, X, WhatsApp): nao executam JS para gerar OG preview = link feio sem imagem.
- **Bing**: render JS limitado.

### 2.3 Sintomas

| Sintoma | Onde detectar |
|---------|----------------|
| GSC > Cobertura: paginas em "Detectada — nao indexada" / "Rastreada — nao indexada" | Google Search Console |
| URL Inspection > "Pagina renderizada" mostra HTML vazio | GSC |
| `view-source:` no Chrome retorna `<div id="root"></div>` quase vazio | Browser |
| Compartilhar link em LinkedIn/WhatsApp gera preview generico | Social |
| ChatGPT / Perplexity nao citam apesar de site existir e ser relevante | LLM-search test |
| AI Overview nao cita o site em queries relacionadas | Profound / Authoritas |
| GA4 mostra trafego orgânico estável-baixo apesar de conteudo extenso | GA4 |

---

## 3. Diagnostico — confirmar que e CSR sem render adequado

### 3.1 Checklist de 6 testes

```
DIAGNOSTICO CSR/SPA — 6 TESTES
================================

1. VIEW-SOURCE
   [ ] Abrir `view-source:https://dominio.com` no Chrome
   [ ] Procurar pelo conteudo principal (H1, paragrafo principal)
   [ ] AUSENTE = CSR puro / hydration fail
   [ ] PRESENTE = SSR ou SSG (OK)

2. GSC URL INSPECTION
   [ ] Abrir GSC > URL Inspection > URL critica
   [ ] Clicar "Test Live URL"
   [ ] Aba "Screenshot" — pagina renderizada igual ao usuario?
   [ ] Aba "HTML" — H1 + body presentes?

3. JS-DISABLED TEST
   [ ] Chrome DevTools > Settings > Disable JavaScript (Cmd/Ctrl+Shift+P -> "Disable JavaScript")
   [ ] Recarregar pagina
   [ ] Conteudo aparece? AUSENTE = depende de JS.

4. CRAWL EM USER-AGENT GOOGLEBOT
   [ ] Screaming Frog > Configuration > User-Agent > Googlebot Smartphone
   [ ] Configuration > Spider > Rendering > "Text Only" (vs "JavaScript")
   [ ] Comparar resultados — diferenca grande = CSR-dependente

5. SOCIAL DEBUG
   [ ] Facebook Debugger: developers.facebook.com/tools/debug
   [ ] LinkedIn Post Inspector: linkedin.com/post-inspector
   [ ] OG preview correto?

6. AI CRAWLER SIMULATION
   [ ] Curl com user-agent GPTBot:
       curl -A "GPTBot/1.0; +https://openai.com/gptbot" https://dominio.com
   [ ] Conteudo aparece no HTML retornado?
   [ ] AUSENTE = AI crawlers nao verao
```

### 3.2 Severidade por resultado

| Cenario | Severidade |
|---------|------------|
| view-source vazio + GSC URL Inspection mostra HTML vazio + AI crawler test vazio | **Critica** — sem fix, site nao rankeia nem cita |
| view-source vazio + GSC OK + AI vazio | **Alta** — Google indexa mas AI ignora; perda de GEO |
| view-source com conteudo basico (skeleton) + GSC OK | **Media** — funciona mas frágil; melhorar prerender |
| view-source com HTML completo (SSR/SSG) | **OK** — manutencao normal |

---

## 4. Fixes — prerender vs migracao SSR/SSG

Duas estrategias principais:

### 4.1 Estrategia A — Prerender (sem mudar codigo)

**Como funciona:** servico de prerender intercepta requisicoes de bots (Googlebot, GPTBot, ClaudeBot, etc.) e serve HTML pre-renderizado. Usuarios humanos continuam com SPA rapida.

**Servicos:**

| Servico | Foco |
|---------|------|
| **Prerender.io** | Mais consolidado; integra Lovable, Bolt, v0, Webflow, qualquer SPA |
| **LovableHTML** | Especifico Lovable, menos burocracia |
| **DataJelly** | Especifico Lovable + GEO focado |
| **Rendertron** (Google, deprecado) | Self-hosted, sem suporte oficial atual |
| **Cloudflare Pages prerender** | Edge-based |

**Pros:**
- Implementacao em horas-dias.
- Sem mudar codigo do builder.
- Cobre tanto Google quanto AI bots.

**Contras:**
- Custo recorrente (~$15-200/mes).
- Cache pode ficar stale.
- "Cloaking" — Google trata bem se conteudo identico, mas zona cinzenta historicamente.
- Dependencia de terceiro.

**NAO e cloaking de fato** quando o conteudo servido a bot e EQUIVALENTE ao que usuario veria apos JS executar. Google publica orientacao especifica em https://developers.google.com/search/docs/crawling-indexing/javascript/dynamic-rendering — embora dynamic rendering tenha sido **descontinuado oficialmente** como recomendacao em 2024 (Google passou a preferir SSR/SSG), prerender ainda e tolerado quando conteudo equivale.

### 4.2 Estrategia B — Migracao para SSR/SSG (mudar a stack)

**Como funciona:** trocar render mode de CSR para SSR (server-side render) ou SSG (static site generation) ou ISR (incremental static regeneration).

**Caminhos por builder:**

| De | Para | Esforco |
|----|------|---------|
| Lovable Vite SPA | **Lovable TanStack Start** (rolling out abr/2026) | Baixo se builder permite re-fork |
| Lovable Vite SPA | **Next.js / Astro** (export do codigo + reimplementacao) | Medio-alto |
| v0 mal-configurado | **Next.js SSR/ISR padrao** | Baixo (default) |
| Bolt classico (Netlify) | **Bolt Cloud (SSR built-in mid-2025)** | Baixo |
| Bolt classico | **Migrar para Next.js / Astro** | Medio |
| WordPress legacy | **Headless WP + Next.js SSR** | Alto |
| Wix / Squarespace / Webflow AI | Ja tem SSR/SSG nativo — verificar | Trivial |

**Pros:**
- Solucao definitiva, sem dependencia de prerender.
- Performance melhor (TTFB reduz).
- AI bots, social, Bing — todos funcionam.

**Contras:**
- Esforco de re-implementacao.
- Curva de aprendizado se equipe nao conhece a stack.

### 4.3 Decision tree

```
                      [Site CSR detectado]
                              |
                              v
                    [Quanto trafego ja tem?]
                  Pouco /              \  Muito
                       v                v
                  [Curto prazo?]    [Tem desenvolvedor?]
                  SIM /     \ NAO     SIM /         \ NAO
                     v       v          v            v
                [Prerender] [Migrar  [Migrar SSR/   [Prerender
                 imediato]   SSR/SSG]   SSG planejado]  ate ter dev]
```

### 4.4 Resultado esperado

Com fix correto:

| Métrica | Antes (CSR puro) | Depois (SSR/SSG ou prerender) |
|---------|-------------------|-------------------------------|
| GSC paginas indexadas | 10-30% | 80-95% |
| Tempo ate indexacao | 7-30 dias | 1-7 dias |
| Citacao em ChatGPT/AI Overview | Quase 0 | Possivel (se EEAT + autoridade) |
| OG preview correto em social | Nao | Sim |
| LCP mobile | Variavel | Tipicamente melhor (com SSG) |

---

## 5. Receitas por builder

### 5.1 Lovable

**Estado em 2026:** TanStack Start com SSR sendo lancado em abr/2026; **alguns projetos novos ja saem com SSR, outros (mesmo da semana) saem como Vite SPA puro**. Auditar o projeto especifico.

**Stack:** React + Vite (SPA classico) OU React + TanStack Start (SSR novo).

**Documentacao oficial:** https://docs.lovable.dev/tips-tricks/seo-geo

**Recomendacoes Lovable oficiais (resumo):**

```
LOVABLE SEO/GEO CHECKLIST
==========================

FOUNDATION
[ ] Custom domain (CRITICO — agrega autoridade, evita lovable.app subdomain)
[ ] XML sitemap com lastmod + prioridade
[ ] robots.txt com Sitemap directive
[ ] Canonical autorreferencial
[ ] URLs limpas (sem hash routing, sem IDs aleatorios)

ON-PAGE
[ ] Title <= 60 chars
[ ] Meta description 140-160 chars
[ ] H1 unico + H2/H3 hierarquica
[ ] Semantic HTML (<main>, <nav>, <footer>, <section>)
[ ] Imagens: alt descritivo, width/height, WebP/SVG

SOCIAL & AI
[ ] OG tags unicas (og:title, og:description, og:image 1200x630)
[ ] Twitter Cards
[ ] Schema.org JSON-LD (Product, Article, FAQPage, Organization)
[ ] Conteudo-chave em HTML estatico (NAO so apos JS)

GEO ESPECIFICO
[ ] Conteudo "LLM-quotable": respostas curtas, definicoes claras, fatos
[ ] /llm.html — pagina dedicada com info estruturada da empresa, produtos, pricing, FAQs
[ ] Controle de AI bots em robots.txt

PERFORMANCE
[ ] LCP <= 2.5s, INP <= 200ms, CLS <= 0.1
[ ] Mobile: tap targets 48x48px, fonte minima 16px, viewport meta
[ ] Lighthouse 90+ em todas as 4 categorias (Performance/A11y/BP/SEO=100)
```

**Fix CSR em Lovable:**

| Opcao | Como |
|-------|------|
| **Prerender.io** | Cadastrar dominio + adicionar token middleware (15 min) |
| **LovableHTML** | Servico especifico Lovable, mais simples |
| **DataJelly** | Lovable + GEO focado |
| **Migrar para TanStack Start** | Re-criar projeto em Lovable se opcao SSR aparecer |
| **Export + re-build em Next.js/Astro** | Lovable permite export do codigo React |

**Manutencao recomendada (Lovable docs):**

| Frequencia | Tarefa |
|------------|--------|
| Semanal | Cobertura GSC + tendencias performance |
| Mensal | Sitemap atualizado, refresh underperformer titles, Lighthouse |
| Trimestral | Audit tecnico (canonicals, robots, schema, internal links, mobile) |

### 5.2 v0 (Vercel)

**Stack default:** Next.js — **SSR/ISR/SSG nativos**. Em principio nao tem o problema de CSR.

**Riscos comuns:**
- Componentes "use client" abundantes -> tudo vira CSR mesmo em Next.js.
- Falta de `metadata` export em paginas (title/description faltando).
- Schema nao gerado.

**Fix:**
- Revisar componentes — server components por default; client components so quando necessario.
- Adicionar `export const metadata = {...}` em cada `page.tsx`.
- Adicionar JSON-LD inline em SSR.
- Sitemap em `app/sitemap.ts` (Next.js gera automaticamente).
- robots.txt em `app/robots.ts`.

**Deploy:** Vercel default e SSR + edge — funciona out-of-the-box.

### 5.3 Bolt.new

**Estado em 2026:**
- **Bolt Cloud (mid-2025)** — adicionou hosting nativo + databases + auth + SEO config + SSR.
- **Bolt classico** (Netlify deploy) — tipicamente CSR; mesmo problema do Lovable.

**Fix:**
- **Migrar para Bolt Cloud** se nao migrou ainda.
- OU implementar prerender.io/Cloudflare Pages prerender.
- OU re-deploy em Next.js / Astro.

**Recomendacao Bolt 2026:** Bolt Cloud para qualquer site publico.

### 5.4 Cursor / Replit Agent

Builders generalistas — output depende muito do prompt. Sem padrao default. Risco:
- Se prompt nao especifica SSR/SSG, agente tipicamente gera SPA simples.
- Sem schema, sem sitemap, sem robots.txt automaticamente.

**Fix:** prompt explicito durante criacao:
> "Gerar projeto em Next.js 14+ com App Router, SSR/ISR, schema.org JSON-LD em cada pagina, sitemap automatico, robots.txt configurado, metadata exports completos, OG + Twitter Cards. Site para SEO publico."

OU usar AI builder mais especializado (Lovable, v0) e cuidar do CSR fix.

### 5.5 Webflow AI

Webflow tem SSG nativo. **NAO e CSR**. O AI assist gera conteudo + componentes que sao publicados como HTML estatico.

**Foco em Webflow AI:**
- Schema (Webflow tem campos para JSON-LD em CMS).
- Meta tags por pagina.
- Sitemap automatico.
- Hreflang via collections.
- Internal linking via reference fields.

### 5.6 Wix AI / Squarespace AI / Hostinger AI

Plataformas com SSR ja maduro. AI cuida do conteudo, render fica com a plataforma.

**Foco:**
- Configurar schema (varia por plataforma).
- OG / Twitter Cards.
- Sitemap (gerado automatico, validar).
- Mobile-first (default).

### 5.7 Framer AI

Framer tem SSR. AI gera componentes / paginas. Nao tem o problema CSR.

**Foco:**
- Schema (Framer suporta JSON-LD em CMS).
- Meta dinamica via fields do CMS.
- SEO-mode no Framer Pro.

---

## 6. Anti-patterns sites com AI builders

| Anti-pattern | Por que e problema |
|--------------|---------------------|
| **Publicar em CSR puro sem prerender nem SSR** | Google indexa parcial, AI bots ignoram completo |
| **Manter dominio `*.lovable.app` / `*.bolt.new` / `*.vercel.app`** | Autoridade fragmentada, sem custom domain perde GEO |
| **Hash routing** (`/#/page`) | Descontinuado para SEO desde 2015 |
| **JSON-LD gerado via JS pos-load** | Bots veem HTML sem schema |
| **Confiar que "Google renderiza JS"** | Google ate renderiza, mas AI bots nao; OG nao executa JS |
| **Disclosure de AI ausente em conteudo gerado por IA** | Helpful Content / Spam Policies risk |
| **Multi-page mas tudo no mesmo `index.html`** (SPA mascarado) | URLs unicas mas HTML duplicado |
| **Esquecer sitemap dinamico** | AI builders frequentemente nao geram automaticamente |
| **Lazy load excessivo de conteudo principal** | Conteudo critico depende de scroll/JS |

---

# PARTE II — GEO / LLMO / AEO — Otimizacao para AI Engines

## 7. Modelo mental — como LLMs descobrem, recuperam, citam

### 7.1 Pipeline de citacao em LLM

```
USUARIO faz query
         |
         v
[LLM decide se usa retrieval]
   (ChatGPT search ON, Perplexity sempre, Claude opcional)
         |
         v
[Search engine consultado] (Bing para ChatGPT/Copilot, Google para Gemini, propria para Perplexity)
         |
         v
[Top N paginas retornadas] (10-100, varia)
         |
         v
[LLM extrai chunks de paragrafo] (200-500 chars)
         |
         v
[LLM avalia: chunks responde a query?]
         |
         v
[Resposta gerada com 2-7 citacoes] (vs 10 do Google)
```

Diferenca chave vs SEO classico: **e o paragrafo (chunk), nao a pagina, que compete pela citacao**.

### 7.2 Os principais motores em 2026

| Motor | Operadora | Search engine subjacente | Citacao |
|-------|-----------|--------------------------|---------|
| **ChatGPT search** | OpenAI | Bing (default) + indice proprio | Cita 2-7 fontes |
| **Google AI Overviews** | Google | Indice Google | Cita ~5-10 fontes |
| **Perplexity** | Perplexity AI | Indice proprio + Google | Cita 5-15 fontes |
| **Claude** (com browsing) | Anthropic | Brave / propria | Cita conforme prompt |
| **Bing Copilot** | Microsoft | Bing | Cita 3-7 fontes |
| **Gemini** | Google | Indice Google | Cita ~5-10 fontes |
| **Grok** | xAI | X / web | Cita variavel |
| **Mistral Le Chat** | Mistral | Web | Cita variavel |

### 7.3 Stats criticas 2026 (re-validar — fontes na Secao 16)

- **ChatGPT**: 200M+ weekly active users; ~20% do search traffic global em early 2026.
- **AI Overview citation de top-10 caiu de 76% para 38%** entre 2025-2026 (rotacao de citacao).
- **Apenas 15% das paginas recuperadas** sao efetivamente citadas (filtragem pesada).
- **44% das citacoes vem do primeiro terco** do conteudo da pagina.
- **Paginas com 120-180 palavras entre headings** = media de 4.6 citacoes (mais alta).
- **Conteudo atualizado < 30 dias** = 3.2x mais citacoes.
- **Sites com perfil em Trustpilot/G2/Capterra/Yelp** = 3x mais probabilidade de citacao.
- **Sequential heading (H1 > H2 > H3)** = ChatGPT cita ~3x mais que conteudo com hierarquia quebrada.
- **Answer-first content (40-60 palavras na primeira posicao)** = +40% chance de citacao.

---

## 8. Os 3 fatores principais de citacao

Pesquisas convergentes 2025-2026 identificam **tres fatores** consistentes:

### 8.1 Fator 1 — STRUCTURE

| Sinal | Impacto |
|-------|---------|
| Answer-first 40-60 palavras logo apos H | +40% citacao |
| Sequential heading H1 > H2 > H3 | 3x citacao em ChatGPT |
| Listas (numerada / bullet) explicitas | Forte |
| Tabelas semanticas | Forte |
| Paragrafos 120-180 palavras entre headings | Media 4.6 citacoes |
| FAQ schema com Q&A visivel | Forte |
| HowTo schema com passos | Forte |
| Definicoes claras isoladas | Forte |

### 8.2 Fator 2 — DOMAIN AUTHORITY

| Sinal | Impacto |
|-------|---------|
| Backlinks editoriais (cf. `seo-link-building`) | Alto |
| Brand mentions sem link | Medio-alto |
| Trust profile (Trustpilot, G2, Capterra, Yelp) | 3x citacao |
| Co-citacoes em fontes autoritativas | Alto |
| Wikipedia / Wikidata mention | Muito alto |
| EEAT visivel (autor + credenciais + bio + sameAs) | Alto |
| HTTPS + dominio estabelecido | Higiene basica |

### 8.3 Fator 3 — FRESHNESS

| Sinal | Impacto |
|-------|---------|
| `dateModified` < 30 dias | 3.2x citacoes |
| `dateModified` honesto (nao cosmetico) | Critico — cosmetico falha em HCS |
| Conteudo atualizado em fato real | Forte |
| News content recente | Critico para topicos volúveis |
| Statistics page com dados de 2026 | Alto |

---

## 9. Tecnicas operacionais GEO/LLMO

### 9.1 Answer-first content (BLUF — Bottom Line Up Front)

```
H2: O que e Core Web Vitals?

Core Web Vitals sao 3 metricas oficiais do Google que medem UX em campo: 
LCP (carregamento <= 2.5s), INP (interacao <= 200ms) e CLS (estabilidade 
visual <= 0.1). Substituiram FID em mar/2024 e fazem parte do Page 
Experience Signal.

[Apos isso vem o detalhamento, contexto, exemplos.]
```

Critérios:
- **40-60 palavras** (chunk citável).
- **Logo apos o H** (primeira posicao da secao).
- **Resposta DIRETA** — nao "para entender X, primeiro precisamos saber Y".
- **Auto-contida** — nao depende de paragrafos anteriores.
- **Fato verificavel** — numero, data, definicao, regra.

### 9.2 Sequential heading hierarchy

```
H1: Core Web Vitals — Guia Completo 2026
  H2: O que e Core Web Vitals
    H3: As 3 metricas oficiais
    H3: Lab vs Field
  H2: Como medir Core Web Vitals
    H3: Google Search Console
    H3: PageSpeed Insights
    H3: CrUX dataset
  H2: Como otimizar Core Web Vitals
    H3: LCP otimizacao
    H3: INP otimizacao
    H3: CLS otimizacao
  H2: Perguntas Frequentes
```

NUNCA pular niveis (H1 -> H3 sem H2). ChatGPT cita 3x mais com hierarquia sequencial.

### 9.3 Paragrafos 120-180 palavras

Pesquisa GEO mostra esse range como "sweet spot" para citacao. Justificativa:
- Curto demais (<60 palavras) = chunk insuficiente para LLM extrair contexto.
- Longo demais (>250 palavras) = LLM corta prematuramente, resposta perde nuance.

### 9.4 Schema.org rico

| Schema | Por que critico para GEO |
|--------|---------------------------|
| **Article + Author + Organization** | Atribuicao + EEAT |
| **FAQPage** | Resposta direta extraivel + `Question/acceptedAnswer` |
| **HowTo** | Passos extraiveis para "como fazer X" |
| **Product + Offer + AggregateRating** | Para queries comerciais |
| **Person + sameAs** | Reconhecimento de entidade |
| **Organization + sameAs** | Reconhecimento de marca |
| **BreadcrumbList** | Contexto da pagina |
| **Dataset** | Para statistics page / research |

### 9.5 Trust profiles externos

Garantir presenca em **pelo menos 3** dos seguintes:

- Trustpilot (B2C / consumer).
- G2 (B2B SaaS).
- Capterra (SaaS).
- Yelp (local).
- Google Business Profile (local + B2B).
- Reclame Aqui (BR).
- LinkedIn (empresa + autores).

3x citacao quando ha presenca + reviews ativas.

### 9.6 Brand mention + co-citation

- Mencoes de marca em texto (mesmo sem link) sao sinais para LLMs.
- Co-citacao com concorrentes em fontes autoritativas reforca posicionamento.
- Estrategia: digital PR (Secao `seo-link-building` 14) gera mencoes editoriais.

### 9.7 Entity coverage

Para que LLM "entenda" sua marca como entidade:

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "SPKR",
  "url": "https://dominio.com",
  "logo": "https://dominio.com/logo.png",
  "description": "Consultoria em marketing, juridico de TI e implantacao",
  "founder": { "@type": "Person", "name": "Alexandre Jalkh" },
  "foundingDate": "2010-XX-XX",
  "sameAs": [
    "https://www.linkedin.com/company/spkr",
    "https://www.wikidata.org/wiki/QXXXXX",
    "https://www.crunchbase.com/organization/spkr",
    "https://twitter.com/spkr",
    "https://www.instagram.com/spkr"
  ]
}
```

Linkar entity em **multiplas fontes autoritativas** (Wikidata, Wikipedia, Crunchbase, LinkedIn) consolida reconhecimento.

### 9.8 Tracking de citacao

| Ferramenta | Cobertura |
|------------|-----------|
| **Profound** (tryprofound.com) | ChatGPT + Google AI Overview + Perplexity + Bing Copilot |
| **Authoritas** | SGE / AI Overview |
| **BrightEdge Generative Parser** | Enterprise |
| **Otterly.ai** | LLM rank tracking |
| **AthenaHQ** | AI search optimization |
| **GSC > Search Appearance > AI Overview** | Em rollout — Google promete metrica nativa |

KPIs:
- **Citation rate** — % de queries do nicho que citam o site.
- **Share of Voice em AI** — citacoes do site / total de citacoes na vertical.
- **Citation position** — quando citado, em que posicao (1ª, 2ª, ...).
- **Brand mention frequency** — frequencia de mencao em respostas.

---

# PARTE III — llms.txt — o padrao emergente

## 10. O que e llms.txt

Padrao proposto por **Jeremy Howard (Answer.AI)** em **setembro/2024**. Arquivo Markdown na raiz do dominio (`/llms.txt`) que **direciona LLMs aos recursos mais importantes do site**.

Diferenca conceitual:
- **`robots.txt`**: o que NAO indexar.
- **`sitemap.xml`**: TODAS as URLs indexaveis.
- **`llms.txt`**: o que LLMs DEVERIAM saber sobre o site (curado, prioritizado).

### 10.1 Status em 2026

- **Adoção**: emergente. Yoast WordPress plugin tem auto-geracao 1-clique.
- **Google**: declarou explicitamente que **NAO e ranking signal**, nao e recomendado pelo Google Search.
- **OpenAI / Anthropic / Perplexity**: nao confirmaram uso oficial em producao — alguns indicios em logs de servidor que GPTBot e ClaudeBot ocasionalmente buscam, mas pouco frequente.
- **Conclusao 2026**: implementar como sinal experimental, **sem grande investimento de tempo** ate adoção crescer.

### 10.2 Especificacao oficial (llmstxt.org)

Localizacao: `/llms.txt` na raiz (ou opcionalmente em subpaths).

**Estrutura obrigatoria:**

```markdown
# Nome do projeto/site
> Resumo curto com info essencial para entender o resto do arquivo

Detalhes adicionais (paragrafos, listas — sem usar headings)

## Nome da secao
- [Titulo do recurso](https://url): notas opcionais sobre o recurso

## Outra secao
- [Outro recurso](https://url2)

## Optional
- [Recurso secundario](https://url3) — pode ser pulado se contexto curto for necessario
```

**Componentes:**

| Componente | Obrigatorio? | Detalhe |
|-----------|--------------|---------|
| `# H1` com nome | **SIM** | Unica secao requerida |
| `> Blockquote` resumo | NAO (recomendado) | Resumo curto |
| Detalhes em paragrafos/listas | NAO | Sem headings (apenas H2 sao validos para sub-secoes) |
| `## H2` de secoes | NAO | Multiplas secoes com listas de URLs |
| `## Optional` | NAO | Secao especial — LLMs podem pular se contexto curto |

**Formato de cada item:** `[nome](url)` opcionalmente seguido de `: notas`.

### 10.3 Exemplo concreto (FastHTML, do site oficial)

```markdown
# FastHTML

> FastHTML is a python library which brings together Starlette, Uvicorn, HTMX, and 
fastcore's `FT` "FastTags" into a library for creating server-rendered hypermedia 
applications.

Important notes:

- Although parts of its API are inspired by FastAPI, it is *not* compatible with FastAPI 
syntax and is not targeted at building APIs.
- FastHTML is compatible with JS-native web components and any vanilla JS library, 
but not with React, Vue, or Svelte.

## Docs

- [FastHTML quick start](https://docs.fastht.ml/quickstart): A brief overview...
- [HTMX reference](https://htmx.org/reference/): Brief description of all HTMX attributes...

## Examples

- [Todo list application](https://github.com/AnswerDotAI/fasthtml-tut/blob/main/todo.py)

## Optional

- [Starlette full documentation](https://www.starlette.io/): A subset of Starlette's
  functionality is unimported into FastHTML
```

### 10.4 Variantes

- **`/llms.txt`** — versao curta (mapa).
- **`/llms-full.txt`** — versao expandida com conteudo completo dos recursos linkados.
- **`/llms-ctx.txt`** e **`/llms-ctx-full.txt`** — variantes geradas por ferramentas, fora do core spec.

### 10.5 Quando vale implementar

| Cenario | Recomendacao |
|---------|--------------|
| Site SaaS com docs tecnicas extensas | **Implementar** — apoia citacao em ChatGPT/Claude |
| Knowledge base / academy / cursos | **Implementar** — facilita parsing |
| E-commerce | **Baixa prioridade** — sem evidencia de uso |
| Blog editorial / news | **Baixa prioridade** |
| Site institucional simples | **Opcional, baixo custo** — gerar via Yoast/Mintlify e seguir |

### 10.6 Template para Frank-MKT (cliente B2B)

```markdown
# [Nome do cliente]

> [Empresa] e [tipo de empresa] que [proposta de valor em 1-2 linhas]. Atende [persona] 
no [mercado/regiao] com [diferencial].

Fundada em [ano], [N] colaboradores, [outros fatos]. Foco em [especialidade].

## Sobre

- [Sobre nos](https://dominio.com/sobre): Historia, missao, time
- [Equipe](https://dominio.com/equipe): Lideranca + especialistas (com EEAT)
- [Como trabalhamos](https://dominio.com/processo): Metodologia

## Servicos / Produtos

- [Servico 1](https://dominio.com/servicos/1): Descricao concisa
- [Servico 2](https://dominio.com/servicos/2): Descricao concisa
- [Servico 3](https://dominio.com/servicos/3): Descricao concisa

## Recursos

- [Pillar SEO](https://dominio.com/seo): Guia completo de SEO 2026
- [Calculadora de [X]](https://dominio.com/calculadora): Tool gratuita
- [Estatisticas de [setor] 2026](https://dominio.com/research): Dados originais

## FAQ

- [Quanto custa?](https://dominio.com/precos): Faixa de preco e fatores
- [Em quanto tempo entrega?](https://dominio.com/sla): SLA e prazos
- [Atende minha regiao?](https://dominio.com/cobertura): Cobertura geografica

## Contato

- [Fale conosco](https://dominio.com/contato): Email + telefone + WhatsApp
- [LinkedIn](https://linkedin.com/company/dominio)

## Optional

- [Blog completo](https://dominio.com/blog): Arquivo geral
- [Termos de uso](https://dominio.com/termos)
- [Politica de privacidade](https://dominio.com/privacidade)
```

---

# PARTE IV — AI bots e robots.txt

## 11. Os 6 bots criticos em 2026

| Bot | Operadora | Funcao | Default |
|-----|-----------|--------|---------|
| **GPTBot** | OpenAI | Treinamento de modelos | Mais bloqueado em 2026 |
| **OAI-SearchBot** | OpenAI | ChatGPT search live | Permite por default |
| **ChatGPT-User** | OpenAI | User-triggered fetch (browsing) | Permite |
| **ClaudeBot** | Anthropic | Treinamento | Permite por default |
| **Claude-User** | Anthropic | User-triggered fetch | Permite |
| **Claude-SearchBot** | Anthropic | Search live | Permite |
| **PerplexityBot** | Perplexity AI | Indice + answers | Permite |
| **Perplexity-User** | Perplexity | User fetch | Permite |
| **Google-Extended** | Google DeepMind | Treinamento Gemini / Bard | Default permitido (Google trata separado de Googlebot) |
| **Meta-ExternalAgent** | Meta AI | Treinamento + AI products | Permite |
| **Bytespider** | ByteDance / TikTok | Treinamento | **NON-COMPLIANT — ignora robots.txt** |
| **Applebot-Extended** | Apple | Treinamento | Permite |
| **CCBot** | Common Crawl | Web archive (alimenta varios LLMs) | Variavel |

### 11.1 Distincao critica: training vs search vs user-triggered

| Tipo | Exemplos | Bloquear afeta? |
|------|----------|------------------|
| **Training** | GPTBot, ClaudeBot, Google-Extended, Meta-ExternalAgent | NAO afeta resposta a queries em ChatGPT/Claude/Gemini (modelos ja foram treinados). Apenas evita que conteudo NOVO entre em treinamento futuro. |
| **Search live** | OAI-SearchBot, Claude-SearchBot, PerplexityBot, Bingbot, Googlebot | Bloquear = nao aparecer em ChatGPT search / Perplexity / Google AI Overview / Bing Copilot |
| **User-triggered** | ChatGPT-User, Claude-User | Bloquear = usuario pedindo "pega o conteudo de https://X.com" recebe erro |

**Regra de ouro:** bloquear training NAO impede aparecer em search. Sao bots distintos.

### 11.2 Estrategias

| Estrategia | Quem usa | Robots.txt |
|------------|----------|------------|
| **Allow tudo** | Maioria — quer maxima visibilidade em AI | (Default — sem disallow) |
| **Block training, allow search** | Publishers / quem nao quer alimentar treinamento | Disallow GPTBot, ClaudeBot, Google-Extended, Meta-ExternalAgent. Allow OAI-SearchBot, Claude-SearchBot, PerplexityBot |
| **Block tudo de IA** | Sites enterprise sensiveis | Disallow todos AI bots |
| **Block apenas Bytespider** | Combate a comportamento abusivo | Disallow Bytespider (ignora — bloquear na firewall) |

### 11.3 Stats Cloudflare Q1 2026

- **GPTBot e o mais bloqueado** dos AI bots.
- **ClaudeBot crawl 20.583 paginas para cada referral retornado** (ratio crawl/value alto).
- **89.4% do trafego AI crawler e training/mixed**, nao search live.
- **Bytespider tipicamente representa 90% do trafego AI bot** em alguns clientes Cloudflare, ignorando robots.txt — bloquear na firewall, nao em robots.

### 11.4 Templates robots.txt

**A. Allow tudo (default permissivo):**

```
User-agent: *
Allow: /

Sitemap: https://dominio.com/sitemap.xml
```

**B. Block training, allow search:**

```
User-agent: *
Allow: /

# Block AI training crawlers (does NOT affect AI search/answer engines)
User-agent: GPTBot
Disallow: /

User-agent: ClaudeBot
Disallow: /

User-agent: Google-Extended
Disallow: /

User-agent: Meta-ExternalAgent
Disallow: /

User-agent: Applebot-Extended
Disallow: /

User-agent: CCBot
Disallow: /

# AI search bots — permit (so brand still appears in ChatGPT search, Perplexity, etc.)
User-agent: OAI-SearchBot
Allow: /

User-agent: Claude-SearchBot
Allow: /

User-agent: PerplexityBot
Allow: /

# Bytespider ignora robots.txt — bloquear via firewall/CDN

Sitemap: https://dominio.com/sitemap.xml
```

**C. Block tudo IA:**

```
User-agent: *
Allow: /

User-agent: GPTBot
Disallow: /

User-agent: OAI-SearchBot
Disallow: /

User-agent: ChatGPT-User
Disallow: /

User-agent: ClaudeBot
Disallow: /

User-agent: Claude-User
Disallow: /

User-agent: Claude-SearchBot
Disallow: /

User-agent: PerplexityBot
Disallow: /

User-agent: Google-Extended
Disallow: /

User-agent: Meta-ExternalAgent
Disallow: /

User-agent: Applebot-Extended
Disallow: /

User-agent: CCBot
Disallow: /

User-agent: Bytespider
Disallow: /
# NOTA: Bytespider ignora — usar Cloudflare WAF rule para 403

Sitemap: https://dominio.com/sitemap.xml
```

### 11.5 Bloqueio em CDN / WAF (para bots non-compliant)

```
# Cloudflare WAF rule (pseudo)
Field: User-Agent
Operator: contains
Value: Bytespider
Action: Block (403)
```

### 11.6 Verificacao de bot real (anti-spoofing)

Bots maliciosos forjam User-Agent. Verificacao:

```bash
# Reverse DNS lookup
host 20.171.X.X
# Para GPTBot deve retornar *.openai.com

# Forward verify
host openai-gpt-bot.openai.com
# deve retornar IP original

# OpenAI publica IP ranges:
# https://openai.com/gptbot.json
```

---

# PARTE V — Schema.org para AI content

## 12. Estado em 2026

Schema.org evolui para acomodar AI generated content. **Properties dedicadas para disclosure de AI ainda em desenvolvimento** mas:

- **IPTC DigitalSourceType** ja tem termos para imagens AI generated.
- **CreativeWork + Author + Organization** sao os blocos principais.
- **`sameAs`** e critico para reconhecimento de entidade pelos LLMs.

## 13. Author Schema reforcado para IA

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Guia de Marketing Digital 2026",
  "datePublished": "2026-05-07T10:00:00-03:00",
  "dateModified": "2026-05-07T10:00:00-03:00",
  "author": {
    "@type": "Person",
    "name": "Alexandre Jalkh",
    "url": "https://dominio.com/autor/alexandre-jalkh",
    "image": "https://dominio.com/avatar/alexandre.avif",
    "jobTitle": "Consultor de Marketing e Inteligencia de Mercado",
    "alumniOf": { "@type": "Organization", "name": "Universidade X" },
    "knowsAbout": ["Marketing Digital", "SEO", "GEO", "Branding", "Pesquisa de Mercado"],
    "hasCredential": [
      {
        "@type": "EducationalOccupationalCredential",
        "credentialCategory": "Especializacao",
        "name": "MBA em Marketing"
      }
    ],
    "sameAs": [
      "https://www.linkedin.com/in/alexandrejalkh",
      "https://lattes.cnpq.br/XXXXX",
      "https://twitter.com/alexandrejalkh",
      "https://www.wikidata.org/wiki/QXXXXX"
    ]
  },
  "publisher": {
    "@type": "Organization",
    "name": "SPKR",
    "logo": {
      "@type": "ImageObject",
      "url": "https://dominio.com/logo.png",
      "width": 600, "height": 60
    },
    "sameAs": [
      "https://www.linkedin.com/company/spkr",
      "https://www.wikidata.org/wiki/QXXXXX"
    ]
  },
  "creditText": "Conteudo originalmente desenvolvido com pesquisa propria, com assistencia de ferramentas de IA para outline. Revisao tecnica e final por Alexandre Jalkh.",
  "inLanguage": "pt-BR"
}
```

**Pontos criticos para LLMs:**
- `sameAs` em Person + Organization apontando para Wikidata, LinkedIn, perfis profissionais.
- `hasCredential` declarando credenciais.
- `knowsAbout` listando expertise.
- `creditText` com transparencia sobre uso de IA (quando relevante).

## 14. Disclosure de AI generated content

### 14.1 Em texto (visivel ao usuario)

```html
<div class="disclosure-box">
  <strong>Sobre este conteudo:</strong>
  Este artigo foi desenvolvido pela equipe editorial da SPKR. 
  Outline inicial e pesquisa de fontes foram apoiados por ferramentas 
  de IA (Claude, ChatGPT). Redacao, analise e revisao final foram 
  feitas pelo autor identificado, com base em [N] anos de experiencia 
  em [area]. Fatos e dados foram verificados em fontes primarias 
  citadas no texto.
  
  Ultima atualizacao: 2026-05-07
</div>
```

### 14.2 Em schema (estruturado)

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "creditText": "Pesquisa, analise e redacao por Alexandre Jalkh com assistencia de ferramentas de IA na fase de outline e estruturacao inicial.",
  "contentReferenceTime": "2026-05-07",
  "abstract": "Resumo verificado por humano..."
}
```

### 14.3 Para imagens AI generated (IPTC)

Google requer (em e-commerce e em Top Stories) marcacao IPTC `DigitalSourceType`:

| Termo IPTC | Quando usar |
|-----------|-------------|
| `algorithmicMedia` | Mídia gerada por algoritmo nao-AI |
| `trainedAlgorithmicMedia` | **Mídia gerada por AI/ML** (DALL-E, Midjourney, Stable Diffusion) |
| `compositeWithTrainedAlgorithmicMedia` | Composicao com elementos AI |
| `humanEdited` | Editada por humano |

Implementacao via metadata IPTC embarcada na imagem (ferramentas: ExifTool, Adobe Bridge) OU via schema.org:

```json
{
  "@type": "ImageObject",
  "contentUrl": "https://dominio.com/img/ai-generated.avif",
  "creditText": "Imagem gerada por DALL-E 3 com prompt revisado por equipe editorial",
  "creator": { "@type": "Organization", "name": "OpenAI / DALL-E 3" },
  "encodingFormat": "image/avif"
}
```

### 14.4 Para video AI generated

```json
{
  "@type": "VideoObject",
  "name": "...",
  "creditText": "Video gerado com Sora (OpenAI), narracao gerada com ElevenLabs, roteiro escrito por equipe editorial humana"
}
```

---

# PARTE VI — Helpful Content + AI generated

## 15. Posicao oficial Google 2026

**Documentacao:** https://developers.google.com/search/docs/fundamentals/using-gen-ai-content

### 15.1 Linha clara

| Pratica | Status Google |
|---------|---------------|
| AI como assistente (outline, draft, traducao, sumarizacao) com expertise humana adicionando valor | **Permitido + util** |
| AI gerando conteudo + revisao humana substancial + autor identificado + perspectiva original + credencial verificavel | **Permitido + valorizado** |
| AI gerando conteudo em escala SEM expertise humana, primarily para manipular ranking | **Spam Policies — scaled content abuse (mar/2024)** |

### 15.2 Quote oficial (Google Search Central)

> "Generative AI tools or other similar tools, including AI-generation, to produce content for the primary purpose of manipulating search rankings, is a violation of spam policies."

> "Those seeking success in Google Search should be looking to produce original, high-quality, people-first content demonstrating qualities E-E-A-T."

### 15.3 EEAT em AI content

- **Trust** e o pilar mais importante (acima de Experience, Expertise, Authoritativeness).
- AI content "**substantially edited by named human expert, grounded in original perspective and attributed with verifiable credentials**" performa bem.
- AI content sem revisao + sem expertise + sem perspectiva original tipicamente cai em scaled abuse.

### 15.4 Disclosure quando relevante

> "Sharing details about the processes involved can help readers and visitors better understand any unique and useful role automation may have served."

> "Is the use of automation, including AI-generation, self-evident to visitors through disclosures or in other ways?"

> "Are you providing background about how automation or AI-generation was used to create content?"

> "Are you explaining why automation or AI was seen as useful to produce content?"

### 15.5 Areas com requisito explicito de marcacao

- **E-commerce com imagens AI generated**: IPTC `DigitalSourceType: TrainedAlgorithmicMedia` obrigatorio.
- **Top Stories / News**: schema correto + EEAT + autor identificado.
- **YMYL** (saude, financas, legal): EEAT mais alto exigido — AI sem expertise humana NAO se sustenta.

### 15.6 March 2026 Core Update — direcao

Updates de 2024-2026 reforcaram:
- Autoridade tematica > backlinks brutos.
- Original perspective > resumir top 10.
- Expertise verificavel > anonimato.
- Trust profiles externos (G2, Capterra, etc.) entram como sinal.

---

# PARTE VII — Workflow

## 16. Diagnostico em 8 fases

```
DIAGNOSTICO SEO+GEO PARA SITES IA — 8 FASES
==============================================

FASE 1 — IDENTIFICAR STACK
  [ ] Builder: Lovable / v0 / Bolt / Cursor / Replit / Webflow AI / etc.
  [ ] Render mode: CSR / SSR / SSG / ISR
  [ ] Custom domain: sim / nao
  [ ] Framework subjacente

FASE 2 — DIAGNOSTICO CSR (Secao 3.1, 6 testes)
  [ ] view-source
  [ ] GSC URL Inspection
  [ ] JS-disabled test
  [ ] Crawl com Googlebot user-agent
  [ ] Social debug (FB, LinkedIn)
  [ ] AI crawler simulation (curl GPTBot)

FASE 3 — INDEXACAO ATUAL
  [ ] GSC > Cobertura: % indexada
  [ ] "Detectada nao indexada" / "Rastreada nao indexada"
  [ ] Tempo medio ate indexacao

FASE 4 — GEO/LLMO BASELINE
  [ ] Profound / Authoritas: citacao em ChatGPT / AI Overview / Perplexity
  [ ] Top 20 queries do nicho — e citado em 0 ou >0?
  [ ] Concorrentes citados nas mesmas queries?
  [ ] Trust profiles externos (Trustpilot, G2, Capterra, Yelp, GBP)?

FASE 5 — STRUCTURE AUDIT
  [ ] Answer-first (40-60 palavras)? Sim / Parcial / Nao
  [ ] Sequential heading H1>H2>H3? Sim / Parcial / Nao
  [ ] Paragrafos 120-180 palavras entre headings? Sim / Parcial / Nao
  [ ] FAQPage / HowTo schema? Sim / Parcial / Nao
  [ ] sameAs Person/Organization? Sim / Nao
  [ ] dateModified honesto < 90 dias? Sim / Nao

FASE 6 — AI BOTS POLICY
  [ ] robots.txt atual permite OAI-SearchBot? ClaudeBot? PerplexityBot? Google-Extended?
  [ ] Bytespider tem rule no WAF?
  [ ] Bot verification via reverse DNS validada?

FASE 7 — DISCLOSURE / EEAT
  [ ] Autor real visivel? Bio expandida? Credenciais?
  [ ] Disclosure de uso de IA quando aplicavel?
  [ ] IPTC DigitalSourceType em imagens AI?
  [ ] Politica editorial publica?

FASE 8 — RELATORIO
  [ ] Severidade do problema CSR (critica/alta/media)
  [ ] Decisao prerender vs SSR/SSG
  [ ] Plano GEO/LLMO em 90 dias
  [ ] llms.txt — vale ou nao para esse cliente
```

## 17. Plano em 4 sprints

### Sprint 1 — Fix CSR (semanas 1-3)

```
[ ] Decisao: prerender (servico) ou SSR/SSG (codigo)
[ ] Implementar
[ ] Validar em GSC URL Inspection (HTML completo aparece)
[ ] Validar em curl GPTBot (HTML completo aparece)
[ ] Validar em Facebook Debugger (OG preview correto)
[ ] Submeter sitemap atualizado
[ ] URL Inspection das top 20 URLs — solicitar indexacao
```

### Sprint 2 — Structure GEO (semanas 4-7)

```
[ ] Top 20 paginas: refresh substancial com:
    - Answer-first 40-60 palavras logo apos H
    - Sequential H1>H2>H3
    - Paragrafos 120-180 palavras
    - FAQPage schema com Q&A visivel
    - HowTo schema onde aplicavel
[ ] Schema.org Article + Author + Organization + sameAs em todas as URLs
[ ] dateModified honesto
[ ] OG + Twitter Cards corretos
```

### Sprint 3 — Authority + Trust (semanas 8-12)

```
[ ] Trust profiles externos: Trustpilot OU G2 OU Capterra OU Yelp + GBP
[ ] Solicitar reviews
[ ] LinkedIn empresa + autores ativos
[ ] Schema sameAs apontando para todos perfis sociais + Wikidata (criar entidade)
[ ] Bio do autor expandida com credenciais
[ ] EEAT visivel em pillar pages
[ ] Robots.txt revisado para AI bots policy escolhida
[ ] llms.txt opcional (se faz sentido para o caso)
```

### Sprint 4 — Tracking + iteracao (continuo)

```
[ ] Profound / Authoritas configurado
[ ] Dashboard mensal: citation rate, share of voice, citation position
[ ] Refresh trimestral de top paginas (volatility high para topicos volúveis)
[ ] Re-grounding em fonte oficial a cada 3 meses (volatility desta skill)
[ ] Acompanhar mudancas em AI bots, builders, politicas Google
```

---

## 18. Templates rapidos

### 18.1 Prompt para Cursor/Replit Agent gerar site SEO-friendly

```
Build a public-facing SEO-friendly website using:

- **Framework**: Next.js 14+ with App Router
- **Render**: SSR for content pages, ISR for dynamic content with revalidate
- **Schema.org**: JSON-LD for Article + Person + Organization + BreadcrumbList 
  + FAQPage in every relevant page (server-rendered)
- **Metadata**: export const metadata in every page.tsx with title <60 chars, 
  description 140-160 chars, openGraph (og:title, og:description, og:image 1200x630), 
  twitter card summary_large_image
- **Sitemap**: app/sitemap.ts auto-generating from pages
- **Robots**: app/robots.ts allowing all + sitemap reference
- **Internal linking**: <Link> from next/link with descriptive anchor text
- **EEAT**: author byline visible on every article with photo, credentials, 
  link to LinkedIn, "About the author" expanded section at footer
- **Performance**: optimize for LCP <=2.5s, INP <=200ms, CLS <=0.1; AVIF/WebP 
  images with width/height; fonts self-hosted; minimal client components
- **Accessibility**: WCAG 2.1 AA — semantic HTML, alt text, color contrast, 
  keyboard navigation, focus visible
- **GEO/LLMO**: answer-first structure (40-60 words after each H2), sequential 
  heading hierarchy, FAQPage schema with visible Q&A, paragraphs 120-180 words

Do NOT use:
- Hash routing
- Client-side rendering for content pages
- "use client" unnecessarily
- Heavy animation libraries blocking main thread
- Third-party scripts without justification

Site purpose: [DESCRIBE]
Target audience: [DESCRIBE]
Primary topics: [LIST]
```

### 18.2 robots.txt template para AI builder site

```
# https://dominio.com/robots.txt
# Generated for SEO + GEO

User-agent: *
Allow: /
Disallow: /admin/
Disallow: /api/private/
Disallow: /*?session=
Disallow: /*?utm_

# AI training bots — block (does NOT affect AI search visibility)
User-agent: GPTBot
Disallow: /

User-agent: ClaudeBot
Disallow: /

User-agent: Google-Extended
Disallow: /

User-agent: Meta-ExternalAgent
Disallow: /

User-agent: Applebot-Extended
Disallow: /

User-agent: CCBot
Disallow: /

User-agent: Bytespider
Disallow: /
# Bytespider often ignores — also block via WAF/firewall

# AI search bots — explicitly allow
User-agent: OAI-SearchBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: Claude-SearchBot
Allow: /

User-agent: Claude-User
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Perplexity-User
Allow: /

Sitemap: https://dominio.com/sitemap.xml
```

### 18.3 Article schema com EEAT + AI disclosure

(Ver Secao 13 — Author Schema reforcado.)

### 18.4 Disclosure visivel para conteudo AI-assisted

```html
<aside class="ai-disclosure" aria-label="About this content">
  <h3>Sobre este conteudo</h3>
  <p>
    Este artigo foi pesquisado, analisado e escrito por 
    <a href="/autor/alexandre-jalkh"><strong>Alexandre Jalkh</strong></a>, 
    consultor de marketing com 15 anos de experiencia (LinkedIn linked, 
    Lattes linked, MBA em Marketing).
  </p>
  <p>
    Ferramentas de IA (Claude, ChatGPT) foram usadas para 
    <strong>outline inicial e organizacao da estrutura</strong>. 
    Pesquisa de fontes, redacao final, analise critica e exemplos sao 
    de autoria humana, com base em casos reais.
  </p>
  <p>
    Fatos foram verificados em fontes primarias (linkadas no texto). 
    Ultima revisao em <time datetime="2026-05-07">7 maio 2026</time>.
  </p>
</aside>
```

---

## 19. Anti-patterns

| Anti-pattern | Por que e problema |
|--------------|---------------------|
| **Publicar Lovable/v0/Bolt SPA sem prerender nem SSR** | Google indexa parcial, AI bots ignoram completo |
| **Manter dominio `*.lovable.app`** | Autoridade fragmentada, sem custom domain perde GEO |
| **Confiar que "Google renderiza JS"** | Verdade parcial; AI bots e social NAO renderizam |
| **Bloquear OAI-SearchBot por engano** ao tentar bloquear training | Site some de ChatGPT search |
| **llms.txt como prioridade alta** | Sem evidencia de adoção massa em 2026; foco baixo |
| **Disclosure de IA omitida em conteudo escalado** | HCS / scaled content abuse |
| **AI imagens em e-commerce sem IPTC TrainedAlgorithmicMedia** | Violacao de policy Google |
| **Schema gerado por JS pos-load** | AI bots nao executam JS, schema invisivel |
| **Esquecer Bytespider no WAF** | 90% do trafego AI bot e dele, ignora robots.txt |
| **Refresh cosmetico para "fingir freshness"** para AI | LLM detecta no chunk extraido — perda de citacao |
| **Trust profile zero (sem Trustpilot/G2/Capterra/Yelp)** | 3x menos citacao em ChatGPT |
| **Sequential heading quebrado (H1 -> H3 sem H2)** | 3x menos citacao em ChatGPT |
| **Paragrafos > 250 palavras sem H** | LLM corta chunk antes da informacao chave |
| **Conteudo principal apos JS lazy-load** | AI bots nao scrollam |

---

## 20. Regras de Ouro

1. **NAO CHUTAR** — esta area muda a cada 3 meses. Re-validar antes de aplicar.
2. **CSR puro = SEO suicidal em 2026** — AI bots nao executam JS. Sem prerender ou SSR/SSG, site e invisivel para ChatGPT/Perplexity/AI Overview.
3. **Custom domain SEMPRE** — `*.lovable.app` / `*.vercel.app` / `*.bolt.new` fragmenta autoridade.
4. **Answer-first 40-60 palavras** logo apos cada H2 — +40% citacao.
5. **Sequential H1 > H2 > H3** — 3x mais citacao em ChatGPT.
6. **Paragrafos 120-180 palavras** entre headings — sweet spot de citacao.
7. **dateModified honesto < 30 dias** em conteudo volatil — 3.2x citacoes.
8. **Trust profiles externos** (Trustpilot/G2/Capterra/Yelp + GBP) — 3x citacao.
9. **Schema EEAT estruturado** (Person + Organization + sameAs) — reconhecimento de entidade pelos LLMs.
10. **JSON-LD em SSR/SSG**, NUNCA via JS pos-load — AI bots nao executam JS.
11. **Block training, allow search** — bloquear GPTBot/ClaudeBot/Google-Extended/Meta NAO impede aparecer em ChatGPT search/Perplexity.
12. **Bytespider via WAF**, nao robots.txt — ignora robots, e 90% do trafego AI bot em alguns sites.
13. **Disclosure de IA quando relevante** — HCS valoriza transparencia.
14. **IPTC TrainedAlgorithmicMedia em imagens AI** — obrigatorio em e-commerce + Top Stories.
15. **llms.txt = baixa prioridade em 2026** — emergente, sem evidencia de adoção massa, Google diz que nao e ranking signal.
16. **Tracking continuo de citacao em AI** (Profound / Authoritas) — KPI 2026.

---

## 21. Exemplos comportamentais

### Exemplo 1 — Cliente migrou para Lovable e perdeu trafego

**Input:** "Migramos de WordPress para Lovable ha 2 meses. Trafego organico caiu 70% e GSC mostra `Detectada nao indexada` em 80% das paginas. Por que?"

**Resposta esperada:**

> Diagnostico provavel: **CSR puro com falha de render JS pelo Googlebot**. Confirmar em 6 testes (Secao 3.1). Plano 24-72h: (1) Confirmar via `view-source:URL` — se HTML inicial vazio, problema confirmado; (2) GSC > URL Inspection das top 20 URLs > "Test live URL" > aba HTML — conteudo principal aparece? Se nao, e CSR; (3) Verificar se projeto Lovable e Vite SPA classico ou TanStack Start (rolling out abr/2026 — alguns projetos novos ja saem com SSR). Decisao em 7 dias: (a) **Curto prazo** — implementar Prerender.io OU LovableHTML (15 min config, ~$15-90/mes) — atende Google + AI bots imediatamente; (b) **Medio prazo** — re-criar projeto em Lovable se opcao TanStack Start estiver disponivel para esse cliente; (c) **Definitivo** — export do codigo + rebuild em Next.js (SSR padrao) ou Astro (SSG). Bonus durante migracao: (i) confirmar custom domain (NAO `lovable.app`); (ii) sitemap.xml; (iii) robots.txt com sitemap directive; (iv) JSON-LD Article + Person + Organization em SSR. Recovery realista: 2-6 semanas apos fix para Google reindexar; trafego pode voltar 60-80% em 60 dias. WordPress tinha 5 anos de autoridade — preservar com 301 OBRIGATORIO de URLs antigas para novas (se ainda nao foi feito, prioridade 1).

**Comportamento-chave:** identifica causa-raiz com confidence, oferece 3 caminhos por horizonte, alerta sobre 301 critico de migracao (cf. `seo-tecnico` Secao 17), alinha expectativa de recovery.

### Exemplo 2 — Concorrente cita em ChatGPT, cliente nao

**Input:** "Concorrente direto e citado em ChatGPT search nas queries do nosso nicho. Nos nao aparecemos. Site tem dominio antigo (DR 45), conteudo bom. O que fazer?"

**Resposta esperada:**

> Investigacao em 5 frentes (use Profound ou Authoritas para tracking se nao tem ainda). **Frente 1 — Render**: o site do concorrente entrega HTML completo no GET? E o seu? Curl com user-agent GPTBot em ambos. Se voce e CSR e ele e SSR, esta e a primeira hipotese. **Frente 2 — Estrutura**: GEO benchmark 2026 mostra que conteudo com (a) answer-first 40-60 palavras, (b) sequential H1>H2>H3, (c) paragrafos 120-180 palavras tem 3-4x mais citacao. Comparar 5 paginas suas vs 5 do concorrente — onde esta a diferenca? **Frente 3 — Trust profiles**: concorrente esta em Trustpilot, G2, Capterra, Yelp, com reviews ativas? Voce nao? 3x diferenca de citacao. **Frente 4 — Freshness**: `dateModified` do concorrente nas paginas-chave e dos ultimos 30 dias? `dateModified` honesto < 30d = 3.2x citacao. **Frente 5 — Schema/EEAT**: schema rico (Article + Person + Organization + sameAs Wikidata/LinkedIn/etc.)? Autor visivel com credenciais? Em 99% dos casos a diferenca esta em 2-3 dessas 5 frentes. Plano 90 dias: Sprint 1 fix render se necessario; Sprint 2 refresh top 20 paginas com structure GEO; Sprint 3 trust profiles + EEAT estruturado. Tracking mensal — citation rate em queries do nicho como KPI primario.

**Comportamento-chave:** estrutura 5 hipoteses com benchmarks numericos, propoe plano em sprints, alinha expectativa via tracking continuo.

### Exemplo 3 — "Vale implementar llms.txt?"

**Input:** "Yoast plugin oferece auto-generar llms.txt. Vale ativar?"

**Resposta esperada:**

> Em 2026: **opcional, baixa prioridade**. Realidade: (a) **Google declarou explicitamente que NAO e ranking signal** e nao recomenda; (b) **OpenAI / Anthropic / Perplexity nao confirmaram uso oficial em producao** — server logs mostram acessos esporadicos, nao sistematicos; (c) Adoção e proposta emergente desde set/2024 (Jeremy Howard / Answer.AI), mas sem evidencia robusta de impacto em citacao em LLMs. Quando vale: (i) **SaaS / docs tecnicas extensas** — apoia parsing de Claude/ChatGPT em consultas tecnicas; (ii) **Knowledge base / academy / cursos** — facilita curadoria; (iii) site simples + Yoast oferece 1-clique — custo zero, ativar. Quando nao vale: (i) e-commerce — sem evidencia; (ii) blog editorial / news — sem evidencia; (iii) site enterprise complexo onde gerar llms.txt sob medida custaria horas — investimento melhor em answer-first content + schema rico + trust profiles (esses tem evidencia quantitativa). Recomendacao: ativar via Yoast (custo zero), nao gastar tempo manual. Foco principal continua em: render correto, structure GEO, schema EEAT, trust profiles, freshness honesta. Re-avaliar llms.txt a cada 3-6 meses (volatility deste topico e high).

**Comportamento-chave:** equilibra hipe vs realidade, cita posicao oficial Google, oferece criterio por tipo de site, redireciona para investimentos com evidencia.

### Exemplo 4 — "Bloquear GPTBot vai me tirar do ChatGPT?"

**Input:** "Quero bloquear GPTBot em robots.txt para nao alimentar treinamento OpenAI. Mas tambem queremos aparecer em ChatGPT search. Tem como?"

**Resposta esperada:**

> SIM, perfeitamente possivel — **GPTBot e OAI-SearchBot sao bots distintos com proposito diferente**. (1) **GPTBot** = treinamento de modelos OpenAI (GPT-4, futuros). Bloquear nao afeta resposta do ChatGPT atual a queries (modelo ja foi treinado). Apenas evita que conteudo NOVO entre em treinamento futuro. (2) **OAI-SearchBot** = ChatGPT search (live retrieval para responder ao usuario). Bloquear este = sumir das respostas. (3) **ChatGPT-User** = quando usuario manualmente cola URL no ChatGPT pedindo "leia X". Bloquear = erro nessa funcionalidade. Implementacao no `robots.txt`: bloquear GPTBot, ClaudeBot, Google-Extended, Meta-ExternalAgent (training); permitir OAI-SearchBot, Claude-SearchBot, PerplexityBot (search live). Template completo na Secao 18.2. Verificacao: monitorar server logs por 4 semanas — confirmar que GPTBot parou (deve respeitar robots) e OAI-SearchBot continua acessando. Se OAI-SearchBot tambem parou, voce bloqueou ele por engano (revisar). Bonus: configurar regra Cloudflare WAF para Bytespider — esse ignora robots.txt e responde por 90% do trafego AI bot em alguns sites. Stat 2026 (Cloudflare): 89.4% do trafego AI crawler e training/mixed, nao search live — bloquear training e impacto baixo na visibilidade real em AI search.

**Comportamento-chave:** distingue bots com claridade, oferece template, propoe verificacao concreta, contextualiza com stats.

---

## 22. Checklist de Contraditorio Interno

| # | Pergunta destruidora | O que busca |
|---|----------------------|-------------|
| 1 | **Render mode foi CONFIRMADO** com 6 testes (view-source, GSC URL Inspection, JS-disabled, crawl Googlebot, social debug, curl GPTBot)? | Anti-suposicao de render |
| 2 | Para sites IA-built, **decisao prerender vs SSR/SSG foi tomada** com base em horizonte + recurso disponivel + autoridade existente? | Anti-decisao impulsiva |
| 3 | **Custom domain** esta em uso? NAO `*.lovable.app` / `*.vercel.app` / `*.bolt.new`? | Anti-fragmentacao de autoridade |
| 4 | **Answer-first 40-60 palavras** esta presente nas top 20 paginas? Sequential heading H1>H2>H3? Paragrafos 120-180 palavras? | Structure GEO |
| 5 | **Schema EEAT estruturado** (Person + Organization + sameAs Wikidata/LinkedIn) em SSR/SSG, NUNCA gerado por JS pos-load? | Schema indexavel por AI bots |
| 6 | **Trust profiles externos** (Trustpilot/G2/Capterra/Yelp + GBP) ativos com reviews? | Authority signal AI (3x) |
| 7 | **dateModified honesto < 30 dias** em conteudo volatil? Refresh substancial, nao cosmetico? | Freshness signal AI (3.2x) |
| 8 | **AI bots policy** explicita em robots.txt distinguindo training vs search? Bytespider tratado em WAF? | Bot management correto |
| 9 | **Disclosure de IA visivel + estruturado** em conteudo AI-assisted? IPTC TrainedAlgorithmicMedia em imagens? | HCS + Spam Policies |
| 10 | **Tracking de citacao em AI** (Profound / Authoritas) ativo, com baseline + cadencia mensal? | KPI 2026 |

---

## 23. Referencias canonicas (atualizadas em pesquisa de campo 2026-05)

### 23.1 Oficiais

- **Google Search Central — Gen AI content** — https://developers.google.com/search/docs/fundamentals/using-gen-ai-content
- **Google Search Central — Helpful content** — https://developers.google.com/search/docs/fundamentals/creating-helpful-content
- **Google Search Central — Spam policies (scaled content)** — https://developers.google.com/search/docs/essentials/spam-policies
- **Google-Extended documentation** — https://developers.google.com/search/docs/crawling-indexing/google-extended
- **Google Search Status Dashboard** — https://status.search.google.com
- **OpenAI bots documentation** — https://platform.openai.com/docs/bots
- **OpenAI GPTBot IP ranges** — https://openai.com/gptbot.json
- **Anthropic agent identification** — https://docs.anthropic.com/en/docs/agents-and-tools/web-fetch-tool
- **Perplexity bot information** — https://www.perplexity.ai/hc/en-us/articles/14013421513117

### 23.2 llms.txt (oficial + implementacoes)

- **llmstxt.org (especificacao oficial)** — https://llmstxt.org
- **Answer.AI proposal post (Jeremy Howard)** — https://www.answer.ai/posts/2024-09-03-llmstxt.html
- **Mintlify llms.txt guide** — https://www.mintlify.com/docs/ai/llmstxt
- **Search Engine Land — llms.txt proposed standard** — https://searchengineland.com/llms-txt-proposed-standard-453676
- **Ahrefs — llms.txt analysis** — https://ahrefs.com/blog/what-is-llms-txt/

### 23.3 AI builders (docs oficiais)

- **Lovable docs — SEO/GEO** — https://docs.lovable.dev/tips-tricks/seo-geo
- **v0 / Vercel** — https://v0.dev
- **Bolt.new (StackBlitz) docs** — https://bolt.new
- **Webflow AI** — https://webflow.com/ai
- **Wix AI Site Builder** — https://www.wix.com/studio/ai
- **Framer AI** — https://www.framer.com/ai

### 23.4 GEO / LLMO research

- **GEO: Generative Engine Optimization (paper Aggarwal et al., 2023)** — https://arxiv.org/abs/2311.09735
- **GEO Benchmark Study 2026 (ConvertMate)** — https://www.convertmate.io/research/geo-benchmark-2026
- **Profound 10-step GEO framework** — https://www.tryprofound.com/resources/articles/generative-engine-optimization-geo-guide-2025
- **Search Engine Land GEO column** — https://searchengineland.com/guides/large-language-model-optimization-llmo
- **Search Engine Land — What is GEO** — https://searchengineland.com/what-is-generative-engine-optimization-geo-444418
- **Backlinko — GEO guide** — https://backlinko.com/generative-engine-optimization-geo
- **Onely — How to Optimize for LLMs** — https://www.onely.com/blog/how-to-optimize-content-for-llms/

### 23.5 Citation analytics & ranking factors

- **Search Engine Land — SEO in 2026** — https://searchengineland.com/seo-2026-higher-standards-ai-influence-web-catching-up-473540
- **Averi — ChatGPT vs Perplexity vs Google AI Mode B2B SaaS Citation Benchmarks 2026** — https://www.averi.ai/how-to/chatgpt-vs.-perplexity-vs.-google-ai-mode-the-b2b-saas-citation-benchmarks-report-(2026)
- **Position.digital — 150+ AI SEO Statistics 2026** — https://www.position.digital/blog/ai-seo-statistics/
- **ALM Corp — Google AI Overview Citations Drop 76% to 38%** — https://almcorp.com/blog/google-ai-overview-citations-drop-top-ranking-pages-2026/
- **Digital Bloom — AI Citation Position Revenue Report 2026** — https://thedigitalbloom.com/learn/ai-citation-position-revenue-report-2026/

### 23.6 AI bots / robots.txt

- **Mersel AI — How to Block AI Bots in robots.txt 2026** — https://www.mersel.ai/blog/how-to-block-or-allow-ai-bots-on-your-website
- **Search Engine Journal — Anthropic Claude Bots Granular** — https://www.searchenginejournal.com/anthropics-claude-bots-make-robots-txt-decisions-more-granular/568253/
- **Cloudflare bot solutions docs** — https://developers.cloudflare.com/bots/

### 23.7 Tools (citation tracking)

- **Profound** — https://www.tryprofound.com
- **Authoritas** — https://www.authoritas.com
- **BrightEdge Generative Parser** — enterprise
- **Otterly.ai** — https://otterly.ai
- **AthenaHQ** — https://athenahq.ai

### 23.8 Schema.org

- **Schema.org CreativeWork** — https://schema.org/CreativeWork
- **IPTC DigitalSourceType** — https://cv.iptc.org/newscodes/digitalsourcetype/

### 23.9 Brasil

- **CONAR** — https://www.conar.org.br
- **CDC (Lei 8.078/1990)** — http://www.planalto.gov.br/ccivil_03/leis/l8078compilado.htm
- **LGPD (Lei 13.709/2018)** — http://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm

---

## 24. Referencia cruzada de skills

| Situacao | Skills relacionadas |
|----------|----------------------|
| Site Lovable/v0/Bolt CSR | `seo-ai-otimizacao` (Parte I) + `seo-tecnico` (Secao 11 render) |
| Plano GEO/LLMO | `seo-ai-otimizacao` (Parte II) + `seo-fundamentos` (Secao 13 SGE) + `seo-on-page` (Secao 15.3) + `conteudo-evergreen` |
| llms.txt | `seo-ai-otimizacao` (Parte III) + `seo-tecnico` (sitemap) |
| AI bots robots.txt | `seo-ai-otimizacao` (Parte IV) + `seo-tecnico` (Secao 3.1 robots) |
| Schema para AI content | `seo-ai-otimizacao` (Parte V) + `seo-on-page` (Secao 12 schema) |
| Disclosure de IA | `seo-ai-otimizacao` (Parte VI) + `conteudo-evergreen` (HCS) + `conhecimento-conar-cdc` |
| Citation tracking AI | `seo-ai-otimizacao` (9.8) + `conhecimento-search-console` |
| Migracao para AI builder | `seo-ai-otimizacao` + `seo-tecnico` (Secao 17 migration) + `seo-link-building` |
| Trust profiles externos | `seo-ai-otimizacao` (9.5) + `seo-link-building` (Secao 17 B2B SaaS) |
| Refresh para AI Overview | `seo-ai-otimizacao` (9, 14) + `conteudo-evergreen` (Secao 8 refresh) |

---

## 25. Integracao com o ecossistema Frank-MKT

Esta skill integra-se ao agente principal `frank-mkt` (`agents/frank-mkt.md`) e ao restante do plugin da seguinte forma:

- **Pre-requisitos**: `seo-fundamentos` + `seo-tecnico` + `seo-on-page`. Modelo mental + render + estrutura on-page sao base. Sem isso, esta skill vira tatica isolada.
- **Acoplamento com `seo-tecnico`** (Secao 11 — render CSR/SSR/SSG/ISR) — esta skill aprofunda o caso especifico de SITES BUILT WITH AI builders (Lovable, v0, Bolt). `seo-tecnico` cobre render em geral; aqui foca builders + AI bots especificamente.
- **Acoplamento com `seo-on-page`** — schema.org, EEAT visivel, anatomia. Aqui adiciona disclosure de AI, IPTC DigitalSourceType, sameAs reforcado para LLMs.
- **Acoplamento com `seo-fundamentos`** (Secao 13 SGE / AI Overviews) — aqui aprofunda com stats quantitativas 2026, fatores de citacao especificos, llms.txt, AI bots.
- **Acoplamento com `conteudo-evergreen`** — refresh continuo com `dateModified < 30 dias` e KPI critico para citacao em AI (3.2x). Programmatic SEO com IA (Secao 15 daquela skill) cruza com disclosure de IA aqui.
- **Acoplamento com `seo-link-building`** — trust profiles externos (Trustpilot/G2/Capterra/Yelp) e brand mentions sao sinal direto de citacao em AI (3x). Coordenar campanhas.
- **Acoplamento com `seo-keywords`** — queries que LLMs respondem sao geralmente conversacionais, longas, com contexto. Aquela skill cobre KW research; aqui cobre como STRUCTURE responde a essas queries.
- **Acoplamento com `copywriting-conversao`** — answer-first em 40-60 palavras, BLUF, paragrafos 120-180 — sao decisoes de copy.
- **Acoplamento com `compliance-lgpd`** (plugin juridico) — captura de leads em sites IA-built segue regras LGPD; disclosure de IA cruza com transparencia LGPD.
- **Acoplamento com `conhecimento-conar-cdc`** — disclosure de uso de IA em peca publicitaria + CONAR.
- **Acoplamento com o agente `auditor`** — auditor roda regras PASS/FAIL em sites IA-built (render entrega HTML completo? schema EEAT em SSR? AI bots policy explicita? IPTC em imagens AI? disclosure visivel?). Esta skill fornece o framework normativo.
- **Acoplamento com o agente `seo-strategist`** — agente especialista orquestra esta skill em planos de adoção GEO + recovery pos-migracao para AI builder.
- **Memoria e rastreabilidade** — diagnosticos render, baselines de citacao, tracking AI mensal sao persistidos em `.frank-mkt/seo/<cliente>/<data>/ai-otimizacao/` pelo agente `suporte-documental` (a criar) ou diretamente pelo `frank-mkt`.
- **Contraditorio interno** — o agente principal aciona o modulo `contraditorio-interno` carregando o Checklist da Secao 22 desta skill antes de entregar diagnostico de site IA-built ou plano GEO/LLMO.
- **Decaimento temporal** — esta skill esta em volatility **`high` (3 meses)** — a mais alta entre as skills SEO. Re-grounding obrigatorio em fontes da Secao 23 antes de citar fato volatil. AI builders atualizam render mode rapidamente; AI bots aparecem/mudam politica; `llms.txt` ainda em maturacao; politicas Google sobre AI content sao revisadas.
- **Regra de ouro para `frank-mkt`** — nenhum diagnostico de site IA-built, plano GEO, decisao sobre AI bots policy, ou disclosure de IA sai do plugin sem passar por esta skill. Custos de erro sao altos: site invisivel a AI search, scaled content abuse, perda de cobertura editorial.

---

> **Aviso:** o plugin `frank-mkt` e um assistente de analise. Recomendacoes desta skill devem ser adaptadas a stack do builder, render mode atual, autoridade do dominio, mercado, e validadas em GSC + curl com user-agents AI + Profound/Authoritas + fonte oficial antes de aplicar em peca formal. Esta e a skill com volatility mais alta do plugin (3 meses) — re-validar TODAS as referencias antes de citar em peca formal. AI builders, AI bots, AI search engines e politicas Google evoluem mensalmente; pesquisas de fatores de citacao tambem.

---

*Plugin `frank-mkt` — skill `seo-ai-otimizacao` (v0.1.0)*
*Ultima atualizacao: 2026-05-07*
*Pesquisa de campo: 10 web searches + 3 WebFetch em fontes oficiais (llmstxt.org, Lovable docs, Google Search Central) realizadas em 2026-05-07*
