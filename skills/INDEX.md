# INDEX — Skills do Frank MKT

> Mapa de todas as skills do plugin `frank-mkt`. Skills implementadas em pastas individuais com `SKILL.md` interno (mesmo padrão do Frank Jurídico TI). Acionamento automático pelo agente principal conforme contexto, exceto as marcadas com `/` (slash commands).

## Status (v0.8.0 — 2026-05-08) — 🎉 4 BLOCOS PRINCIPAIS COMPLETOS

**24 skills implementadas / 30.356 linhas totais.**

| Bloco | Implementadas | Linhas |
|-------|--------------:|-------:|
| **SEO Estendido** | ✅ **7/7** | 9.853 |
| **Mídia Social** | ✅ **10/10** | 10.962 |
| **Comunicação Visual & IA** | ✅ **4/4** | 5.197 |
| **Multi-Platform Strategy** | ✅ **3/3** | 4.344 |
| Infraestrutura (slash commands) | ⏸️ 0/8 | — |
| Marketing & Estratégia | ⏸️ 0/5 | — |
| Copy & Redação | ⏸️ 0/4 | — |
| Pesquisa & Inteligência de Mercado | ⏸️ 0/6 | — |
| UX/UI | ⏸️ 0/4 | — |
| Psicologia & Influência | ⏸️ 0/3 | — |
| Conhecimento de Plataforma | ⏸️ 0/6 | — |
| Corporativo & Humanitário | ⏸️ 0/6 | — |
| Meta-skill | ⏸️ 0/1 | — |
| **TOTAL** | **24/~70** | **30.356** |

**Volatility:** 9 skills `medium` (re-validar a cada 6 meses) + 14 skills `high` (re-validar a cada 3 meses — próxima validação 2026-08-07/08-08) + **1 skill `low` (re-validar a cada 12 meses, próxima 2027-05-08)**.

**Roadmap expandido:** com novo bloco Comunicação Visual & IA (4 skills planejadas) + outros blocos novos sugeridos (Multi-Platform Strategy 3, Persuasão & Engajamento 2, Marketing Não-Tradicional 2, Documentos Corporativos 2 = +13 skills além das 9 originais ainda não iniciadas), total previsto subiu de ~58 para ~70.

Detalhes em [`SNAPSHOT-2026-05-07.md`](../../docs_mkt/SNAPSHOT-2026-05-07.md).

## Skills de Infraestrutura (8 — slash commands)

| Comando | Skill | Função |
|---------|-------|--------|
| `/frank-mkt:init` | `init` | Configura `.frank-mkt/` do cliente/marca |
| `/frank-mkt:stack` | `stack` | Mostra estado atual (marca, persona, campanhas, decisões) |
| `/frank-mkt:save-session` | `save-session` | Salva log estruturado da sessão |
| `/frank-mkt:help` | `help` | Lista comandos, agentes e skills |
| `/frank-mkt:audit` | `audit` | Dispara Auditor (varredura mecânica) |
| `/frank-mkt:review` | `review` | Review qualitativo de campanha/peça |
| `/frank-mkt:juiz` | `juiz` | Convoca Juiz para divergência entre modos |
| `/frank-mkt:perfil` | `perfil` | Convoca Perfilador de Mercado |

## Skills de Marketing & Estratégia (acionamento automático)

| Skill | Tema |
|-------|------|
| `posicionamento-marca` | Posicionamento, value prop, diferenciação |
| `branding` | Identidade verbal, voz, tom, personalidade |
| `funil-jornada` | Funil AARRR / jornada do cliente / mapas |
| `big-idea` | Conceito criativo central de campanha |
| `metricas-marketing` | KPIs (CAC, LTV, ROAS, CTR, CPM, etc.) com ressalva |

## Skills de Copy & Redação (acionamento automático)

| Skill | Tema |
|-------|------|
| `copywriting-conversao` | Copy de venda, AIDA, PAS, headlines |
| `storytelling` | Narrativa, arco, personagem, gancho |
| `email-marketing` | E-mail, sequência, automation, CRM |
| `redacao-publicitaria` | Slogan, claim, manifesto, peça publicitária |

## Skills de SEO (acionamento automático)

| Skill | Tema | Status |
|-------|------|--------|
| [seo-fundamentos](seo-fundamentos/SKILL.md) | Skill-mãe: pipeline crawl/render/index/rank, intent, SERP features, EEAT, Helpful Content, Spam Policies, CWV, AI Overviews, frameworks, KPIs, regulação BR | **v0.1.0 (2026-05-07)** |
| [seo-keywords](seo-keywords/SKILL.md) | Universe, MSV, KD relativo, intent profundo, modificadores, long-tail/zero-volume, KGR, entidades, cluster topical, cannibalization, branded vs non-branded, PAA, Featured Snippet, AI Overview/LLMO, local, sazonalidade, content/keyword gap, ferramentas, workflow 12 fases, templates | **v0.1.0 (2026-05-07)** |
| [seo-on-page](seo-on-page/SKILL.md) | Title, meta, URL/slug, breadcrumb, hierarquia H1-H6, body com TL;DR, internal/external linking, imagens (AVIF/WebP/lazy/schema), vídeos, **schema.org/JSON-LD** (Article, FAQPage, HowTo, Product, Person, Organization, BreadcrumbList, LocalBusiness, etc.), OG + Twitter Cards, EEAT on-page, otimização para Featured Snippet/PAA/AI Overview, anatomia por tipo de página (pillar, cluster, listicle, comparativo, howto, product, local, blog), anti-patterns, checklist, AI/LLM optimization | **v0.1.0 (2026-05-07)** |
| [seo-tecnico](seo-tecnico/SKILL.md) | Crawl (robots.txt RFC 9309, crawl budget, server logs, Googlebot verification), sitemaps XML (index, image, video, news, hreflang), indexabilidade, canonical strategy, hreflang/i18n, HTTP status + redirects (301/302/307/308 + chains), HTTPS/HSTS, mobile-first, render (CSR/SSR/SSG/ISR + WRS + JS SEO), Core Web Vitals técnico (LCP/INP/CLS), performance avançada (TTFB, render-blocking, HTTP/2-3, Brotli, preload), structured data render, pagination/faceted nav/infinite scroll, site architecture, **migration playbook completo**, server logs analysis, CDN/edge/JAMstack, auditoria 14 fases, templates (robots/sitemap/nginx/Apache/hreflang) | **v0.1.0 (2026-05-07)** |
| [seo-link-building](seo-link-building/SKILL.md) | Modelo mental (PageRank, link equity, anchor signal, co-citação, brand mention), tipos de backlink (rel + posição + contexto), métricas (DR/DA/AS/Trust Flow), 8 backlink quality signals, toxic links + Google Spam Policies, **disavow tool quando SIM/NÃO**, anchor distribution natural, link velocity, auditoria de perfil, reverse engineering de competidores, **15+ tipos de linkable asset**, estratégias (Skyscraper 2.0, Broken Link, Resource Page, Guest Post, Unlinked Brand Mention, Podcast, Newsjacking, HARO/Connectively, Image Reverse, Statistics, Original Research, Tools), digital PR + journalist outreach + 3 pitch templates, outreach (frameworks, personalização, follow-up, ferramentas), local + B2B SaaS (Capterra/G2) + e-commerce, anti-patterns black/gray hat, auditoria 12 fases, templates | **v0.1.0 (2026-05-07)** |
| [conteudo-evergreen](conteudo-evergreen/SKILL.md) | Filosofia evergreen vs trending, **decay temporal por tipo de conteúdo** (definitional, how-to, comparativo, listicle, statistics, original research, ultimate guide, regulatório, tutorial), content lifecycle em 6 estágios, content audit metodológico com matriz Esforço×Impacto, **content pruning** (decision tree, 410 vs 404, batches), **content consolidation** (workflow + master URL), **refresh strategy** (4 tipos, dateModified honesto, checklist substancial), atualização programada por volatility, topical authority sistemática, hub-and-spoke maintenance, internal linking dinâmico, AI Overview/SGE preparation, HCS-proofing pós-update, **programmatic SEO ético vs scaled content abuse mar/2024**, sazonal vs evergreen com calendário BR, republishing strategy, distribuição evergreen (newsletter/social/repurposing), métricas (life value, decay rate, refresh ROI, Content Health Score), auditoria 12 fases, templates | **v0.1.0 (2026-05-07)** |
| [seo-ai-otimizacao](seo-ai-otimizacao/SKILL.md) | **Skill de pesquisa de campo (volatility HIGH — 3 meses)**. Parte I — sites construídos com AI builders (Lovable, v0, Bolt, Cursor, Replit Agent, Webflow AI, Wix AI, Framer AI): problema central CSR/SPA, diagnóstico em 6 testes, fixes via prerender (Prerender.io, LovableHTML, DataJelly) ou migração SSR/SSG (TanStack Start, Next.js, Astro), receitas por builder. Parte II — **GEO/LLMO/AEO** com stats quantitativas 2026 (44% citações no primeiro terço, 3.2x freshness <30d, 3x trust profiles, 3x sequential heading, +40% answer-first, 15% taxa de citação, ChatGPT 200M WAU + 20% search global), 3 fatores principais (structure + authority + freshness), 8 técnicas operacionais. Parte III — **llms.txt** (spec oficial Jeremy Howard set/2024, formato markdown, status 2026, exemplos, llms-full.txt). Parte IV — **AI bots robots.txt** (6 bots críticos GPTBot/OAI-SearchBot/ClaudeBot/PerplexityBot/Google-Extended/Meta + Bytespider non-compliant via WAF; distinção training vs search vs user-triggered, templates). Parte V — schema.org para AI content (Author + sameAs + IPTC TrainedAlgorithmicMedia). Parte VI — Helpful Content + AI generated (Google posição oficial 2026). Workflow + 4 sprints + templates + 14 anti-patterns + 16 Regras de Ouro + 4 exemplos + Contraditório Interno | **v0.1.0 (2026-05-07)** |

## Skills de Mídia Social (acionamento automático) — bloco em construção

| Skill | Tema | Status |
|-------|------|--------|
| [social-media-fundamentos](social-media-fundamentos/SKILL.md) | **Skill-mãe (NOVA, pesquisa de campo, volatility HIGH)**. Modelo mental interest-graph vs follow-graph, sinais de algoritmo (dwell time + completion rate), cenário BR 2026 (184M conectados, 3h46min/dia, 6-7 plataformas/usuário, ranking YouTube 89%/IG 85%/FB 84%/TikTok 49%/X 36%/LinkedIn 35% com 90M users BR), benchmarks engagement 2026 (LinkedIn 6.2%, FB 5.6%, IG 5.5%, TikTok 4.6%; carrossel IG +109% vs Reels, LinkedIn carrossel 21.77%), tipos de conteúdo, persona×plataforma, calendário cross-platform + repurposing 1→N, **regulação BR completa** (Lei 15.325/2026 do Influenciador, CONAR 3 elementos cumulativos, tags #publi/#parceriapaga, LGPD em pixel+custom audience+cookies, CDC), Threads vs X vs Bluesky, creator economy ($234B, micro 45.5% spend), employee advocacy, UGC, anti-patterns, ferramentas BR (mLabs/Etus/Squid/Airfluencers) e globais | **v0.1.0 (2026-05-07)** |
| [linkedin-organico](linkedin-organico/SKILL.md) | **Pesquisa de campo (volatility HIGH)**. Algoritmo 2026 (dwell time como sinal #1 oficial, janela inicial 60-90 min, comments 15x peso de likes, profile-to-content alignment, external links -60%, **link-in-comments PATCHED 2026**), formatos comparados (document/PDF carousel **6.60% engagement = top, +278% vs vídeo, +596% vs text-only**; sweet spot 7-10 slides), guia carrossel completo, anatomia de post (hook 3 primeiras linhas, 1300 chars ideal), vídeo curto vertical, Articles long-form, **Newsletters bypassam feed algorithm com push+email+in-app + open rate 35-40% + 14M users Creator Mode**, Live, Polls, **protocolo janela inicial 60-90 min** com employee advocacy, profile optimization (headline + about + skills + Creator Mode), **personal profile > Pages**, topical authority, B2B strategy 40/30/30, best times BR (Ter-Qui 8-11h e 13-14h), Lei 15.325/2026 + CONAR Branded Content, ferramentas (Taplio, Shield, ContentIn, Supergrow, Canva), 18 Regras de Ouro, 4 exemplos comportamentais | **v0.1.0 (2026-05-07)** |
| [linkedin-ads](linkedin-ads/SKILL.md) | **Pesquisa de campo (volatility HIGH)**. Benchmarks 2026: **CPC $5.50-$8.50** (B2B SaaS $8-25 por vertical), CPM $30-50 (+3-8% YoY), CTR 0.44-0.65%, CVR 2.0-3.5%. **Lead Gen Forms 10-18% CVR** (5x landing externa); CPL $50-130. **Thought Leader Ads (expandido 2026): 4.3x lower CPC vs Single Image ($2.29 vs $13.23)** — agora pode sponsor de QUALQUER member (não só employees), event sponsoring + 30s sneak-peek. **BrandLink NOVO 2026** (rebrand Wire Program): in-stream pre-roll antes de publisher/creator content (Bartlett, Minkoff, Vaynerchuk). **Document Ads = champion: $38-82 CPL, 22.73% completion**. **Pipeline 2026**: Cost per SQL $300-600 top vs $800-2k industry; **LinkedIn 1st-touch → closed-won = 281 dias** (Dreamdata) — 30-day ROAS sempre falha mesmo com 6-10x em 365d. **Budget mínimo $5-8k/mês**. **ACV-based**: $30k+ → 20-30%; $100k+ → 40-50%; <$15k → 10-15% (Google melhor). ABM com layered targeting + Predictive Audiences AI NOVO. Lei 15.325/2026 + LGPD em Pixel/Custom Audience | **v0.1.0 (2026-05-08)** |
| [instagram-feed-reels](instagram-feed-reels/SKILL.md) | **Pesquisa de campo (volatility HIGH)**. Algoritmo IG 2026 confirmado por Mosseri jan/2026: **3 sinais TOP — watch time + likes per reach + DM shares (sends)**, comments simples NÃO contam (track conversation depth), likes virou sinal mais fraco, **Views unificada como métrica primária**, janela 24-48h. **Carousels DOMINAM engagement 2026: 1.92% avg = 4x mais que Reels (0.50%) e single (0.45%)**; +114% engagement vs single; **save rate 5-15% top performers — sinal mais forte**; sweet spot 8-10 slides, peak reach slide 13, limite 20 slides. **Reels descoberta**: 60-90s sweet spot, **hold rate 3s >60% = 5-10x reach**, 50-60% drop-off primeiros 3s. Stories: 500M daily, **Story comments NOVO 2026** (público não DM), daily 3-7 frames = +73% retention, polls/quizzes/countdowns/link stickers. **Mix ideal 2026**: 60-70% Reels + 20-30% Carousels + Stories diárias + imagens raras. Engagement plataforma -24% YoY 2025 — retention > acquisition. **BR**: 85% / 145M users (2º lugar). Best times: Qua 12h/18h, Qui 9h, Reels 5-8h e 18-21h. Caption SEO crescente 2026, hashtags 3-5 (papel reduzido). Lei 15.325/2026 + CONAR (Branded Content nativo). Ferramentas (Later, Metricool, Canva, CapCut, Iconosquare) | **v0.1.0 (2026-05-08)** |
| [instagram-ads](instagram-ads/SKILL.md) | **Pesquisa de campo (volatility HIGH)**. Benchmarks 2026: CPM **$6-10** (Reels $4-7 mais barato, Feed $10-15, Stories $6-8); CPC $0.40-1.80; **Brasil Tier 3 = $4.20 CPM** (6x mais barato US). **Reels ROAS 3.12x lider** vs Stories 2.71x; +22% engagement, 726M users alcance, 60% conversões com -40% CPA, sound-on environment. **Meta Advantage+ NOVO DEFAULT 2026**: -32% CPA Shopping, +22% ROAS, **Andromeda algorithm**, 73% top ads = vídeo, AI creative tools +18% CTR. **Partnership Ads expandido 2026**: -19% CPA + 13% CTR, 82% outperform creator handle ads, **Professional Mode profiles elegíveis NOVO** (100M DAU), creator pre-share ad code. **Affiliate commerce NOVO**: creators tag products + commissions, buy button within ads testing. **Carousel Reels NOVO híbrido**: 12% engagement vs 6% Reels regular = **4x performance**. **Brasil**: 132M users (3º maior mundo), ROAS médio 4.2x, conversão e-commerce 14.29%. **CAPI obrigatório 2026** (Pixel only = -30-50% tracking). Lei 15.325/2026 + ECA Digital (multa R$ 50M) + LGPD | **v0.1.0 (2026-05-08)** |
| [facebook-organico](facebook-organico/SKILL.md) | **Pesquisa de campo (volatility HIGH)**. **Realidade 2026**: Pages reach **<2.2%** (vs 5.5% ano passado, 15% em 2014) — Pages punidas. **BR**: **187.6M users (84.1%)** NapoleonCat mar/2026, 55.2% mulheres, maior 25-34 anos (55.9M), forte 35+, **62% compraram via FB**. Algoritmo prioriza meaningful interactions + **UTIS (User True Interest Survey) NOVO jan/2026** para Reels. **Reels FB = 3-5x reach**, **Lives = 10-15% reach (highest)**. **Groups = O OURO 2026**: 1.8B MAU, 25M+ ativos, **+40% engagement vs public**, regra 80/20 (educacional + promo). **Mix 2026 Pages**: 50% Reels + 25% images + 15% Lives + 10% community. Marketplace BR forte (response <1h = melhor placement); Events discovery orgânico único. Engagement plataforma 0.15% flat YoY; Albums 2.6-2.9% top format; Education 2x/sem = 2.97%. Lei 15.325/2026 + CONAR + **ECA Digital BR (vigor 17 mar/2026, multa R$ 50M)**. Meta Business Suite, Buffer, mLabs/Etus | **v0.1.0 (2026-05-08)** |
| [facebook-ads](facebook-ads/SKILL.md) | **Pesquisa de campo (volatility HIGH)**. Compartilha Meta Ads Manager com IG (cross-ref `instagram-ads`). Features Facebook-específicas: **Marketplace Ads** (1B MAU, 80% intent compra), **Audience Network** (16% incremental reach, 95% mobile, lower CPM, **DESATIVAR direct response**), **Local Awareness Ads** (radius 3-15km, brick-and-mortar), **Lead Ads forms** (CPL surged +21% YoY = $27.66, CVR caiu 8.67%→7.72% — **CRM-CAPI pivot obrigatório**), Catalog Ads + DPA. Benchmarks 2026: **CPM mediano $13.48** (+8-38% YoY por indústria), CPC $0.97 (+12% YoY). **Reels ROAS 3.12x líder** vs Feed 2.84x vs Stories 2.71x. **Allocation 60-70% Feed + 20-30% Reels + 10-20% Stories**. **Brasil 2026**: 187.6M users, demographic 35+ mais valioso, e-commerce CVR 14.29%, CPC e-commerce BR $0.38 médio (+75% YoY). Algoritmo abr/2026 prioriza Creative Signals + Data Pipelines. Lei 15.325/2026 + ECA Digital (multa R$ 50M) + LGPD | **v0.1.0 (2026-05-08)** |
| [tiktok-criativo](tiktok-criativo/SKILL.md) | **Pesquisa de campo (volatility HIGH)**. Algoritmo FYP 2026 (watch time + **completion 70%+ threshold em 2026** vs 50% em 2024 = #1, **shares/saves > likes**, **NOVO 2026: testado com followers PRIMEIRO**, penaliza watermarks/reposts/mass-produced). **TikTok = search engine** (49% US, 65% Gen Z). Hold rate 3s 70-85% = 2.2x views; **84.3% dos virais usaram hook psicológico nos primeiros 3s**. Duration 15-30s default, 30-45s B2B sweet spot. **Engagement 4.20% (+9% YoY)**, Fashion 9.8%/Entertainment 9.45%; **<100k = 7.50% vs 10M+ = 2.88%**. **BR**: 49%/131M users — **lider tempo retentivo 28-34h/mês**. **Monetização BR**: Creator Rewards Program **DISPONÍVEL BR**, RPM $0.40-1.00/1k; **TikTok Shop BR = R$ 1k-8k/mês** (comissão 5-20%); creator 100k+3% ER = R$ 2-8k/mês. **REGULAÇÃO BR CRÍTICA**: **ECA Digital (Lei 15.211/2025) — vigor 17 mar/2026**, idade mínima 16 anos, infinite scrolling PROIBIDO menores, multa **R$ 50M**. B2B 40% users 25-44, NOVO targeting Business Services/Enterprise Software/IT Solutions. Lei 15.325/2026 + CONAR. CapCut/Pentos/Tokboard/Exolyt | **v0.1.0 (2026-05-08)** |
| [x-twitter](x-twitter/SKILL.md) | **Pesquisa de campo (volatility HIGH)**. Algoritmo X 2026 com pesos exatos (Reply ×13.5, Retweet ×20, **Reply 27x like, Conversation 150x**), in-network 50% / out-of-network 50% (Real Graph + SimClusters 145k), **time decay -50% a cada 6h**, janela inicial 30-60 min, TweepCred. **X Premium = 10x reach** (Premium 600+ vs Non-Premium <100; Premium+ 1.550+; boost 4x in-network + 2x out + TweepCred +4-16). **Engagement caiu 9% em 2026** — plataforma 0.10%, B2B 0.5-3%, thought leaders 3-8%. **Threads dominam** (8-12 tweets = +47% performance, +63% imps, 3x engagement vs single, 1 imagem cada 3-4 tweets = +40% completion). Spaces (audio com host/co-host/captions/schedule). **Longform Articles** ($1M contest 2026). **Realidade B2B brutal**: LinkedIn 80% leads vs X 12.73% — X = thought leadership niche + real-time + conversation depth, NÃO lead gen. **Communities descontinuado mai/2026** (<0.4%). Best times BR Ter-Qui 8-10h e 12-14h. Lei 15.325/2026 + CONAR. Ferramentas (Typefully, Hypefury, Tweet Hunter) | **v0.1.0 (2026-05-07)** |
| [youtube-shorts](youtube-shorts/SKILL.md) | **Pesquisa de campo (volatility HIGH)**. YouTube Shorts + integração long-form. Algoritmo Shorts 2026 (**#1 metric Viewed vs Swiped Away ratio**, **decoupled de long-form set/2025**, **Anti-Repetitive AI Filter NOVO**, janela 30-60 min). **YouTube Shorts líder short-form**: **5.91% engagement** (vs TikTok 5.75%, Reels IG 5.53%); **2B users, 200B views/dia**. **Hook 3 segundos**: 50-60% drop-off, intro retention >70% target. Duration sweet spot 30-45s default B2B. **Hybrid 3-5 Shorts + 1-2 long-form/sem = 3x growth**. **B2B SaaS**: 96% marketers ROI, **12+ Shorts/mês = -35% CPL**. **Monetização YPP**: 45% revenue share Shorts (vs 55% long-form), **3 tiers** (Entry 500 subs+3k watch hours OR 3M Shorts/90d, Standard 1k+4k OR 10M, Premium 10k+), **RPM Shorts $0.02-$0.10/1k vs $2-$8 long-form**, music corta receita. SEO Shorts NEW (Shorts-specific search filters), thumbnails 1280×720 long-form, captions sempre. **89% brasileiros, 150M users BR**. Lei 15.325/2026 + CONAR ("Includes paid promotion" nativo). Ferramentas (OpusClip, CapCut, Descript, Klap, vidIQ, TubeBuddy) | **v0.1.0 (2026-05-07)** |

## Skills de Comunicação Visual & IA Generativa (NOVO bloco — ✅ COMPLETO 4/4)

| Skill | Tema | Status |
|-------|------|--------|
| [geracao-imagens-ia](geracao-imagens-ia/SKILL.md) | **Pesquisa de campo (volatility HIGH)**. Comparativo profundo dos 7+ modelos top 2026 + workflow IA→IA. **Modelos**: Midjourney v7 (artistic king, --oref/--sref, 95% text V7), GPT Image 1.5 (prompt understanding king), **Imagen 4 family Google** (3 tiers Fast $0.02 / Standard $0.04 / Ultra premium, 2K resolution, S-tier photorealism abr/2026, SynthID watermark obrigatório), **FLUX.2 Black Forest Labs nov/2025** (10 reference images, LoRA brand-specific, $0.01-0.10), Stable Diffusion 4 (free open-source), **Adobe Firefly** (UNICO IP indemnification enterprise-safe), Ideogram V3 (text 90-95% accuracy). **Claude — UNICO para SVG/vector** (código SVG/HTML/React/Mermaid via Artifacts panel — best-in-class, NÃO bitmap). **Workflow IA→IA**: ChatGPT briefing → Midjourney executa → Imagen refina → Claude SVG overlay → loop. **Brand consistency**: FLUX LoRA OU Midjourney --oref/--sref OU style guide. **Vector vs Bitmap decision** crítica (logo escalável = Claude SVG; photo = Midjourney/Imagen). **Compliance**: Firefly único enterprise-safe, SynthID Imagen invisível, Lei 15.325/2026 + LGPD + Código Civil art. 20 (direito de imagem). Use cases marketing: product shots, social ads, infografic illustrations, ad creative, brand identity, mockups. **Custos**: combo Midjourney+ChatGPT+Claude = $50-90/mês (80% das necessidades startup) | **v0.1.0 (2026-05-08)** |
| [infograficos-diagramas](infograficos-diagramas/SKILL.md) | **Pesquisa de campo (volatility medium)**. **Mermaid (Claude excelente)** — 20+ tipos: flowchart, sequence, ERD, journey, gantt, timeline, mindmap, quadrantChart, C4, architecture novo 2026; renderiza nativo GitHub/Notion/GitLab/Confluence. **PlantUML** — formal UML/C4 enterprise (10% casos). **AI Infographic tools 2026**: Pikto AI ($14/mes, PDF→infografico em 10s), Canva Magic Design (free social-first), Visme ($24.75 animado/interativo), Infogram (data-heavy). Visual builders: Excalidraw (sketch), Draw.io (free pro), Lucidchart (enterprise), Miro/FigJam. **Customer Journey B2B vs B2C** (B2B = buying committee 6-10 stakeholders + meses + loops); 7 stages classicos; tools UXPressia/Smaply/TheyDo. **AARRR Pirate Metrics** (Dave McClure 2007 + Awareness Growth Tribe 2016); dashboards Looker Studio/Geckoboard/PostHog/Amplitude. Princípios 2026: strategic minimalism, storytelling linear (timeline forte), hierarquia em 3 segundos. Use cases: pillar pages SEO, LinkedIn carousels, sales decks C4, dashboards | **v0.1.0 (2026-05-08)** |
| [composicao-visual](composicao-visual/SKILL.md) | **Pesquisa de campo (volatility medium)**. Teoria de cores aplicada (color wheel, esquemas, **psicologia 2026 + cultura BR/Asia/EU geo-targeting** — earth tones autênticos > bright greens; +80% brand recognition com cor consistente). Tipografia 2026 (**variable fonts = baseline**, serif return premium, type-as-hero, kinetic, 3D, **acessibilidade > ornamentação**); 2-3 fontes max + Google Fonts recomendadas. **Hierarquia visual** (size+contrast+alignment+white space+proximity+cues; F-pattern texto, Z-pattern landing); mobile-first prioritização. **Fotografia**: rule of thirds (9 segments igual), **golden ratio 1:1.618** (unequal natural), golden spiral nautilus-like. **6 Gestalt principles** (proximity, similarity, closure, continuity, figure/ground, symmetry/Prägnanz). **Vector vs Bitmap profundo** (SVG escalável, **AVIF 30-50% menor que WebP em 2026**, PNG loseless, JPG lossy). **Avatares + mascotes**: **Duolingo Duo case $100M+ value** (3D + personality > aesthetics, internet-native, consistent anos). Brand consistency 60-30-10 paleta. **WCAG 2.x** (contrast 4.5:1 body, 3:1 large, color blindness 8% homens). Mobile touch 44×44 (iOS) / 48×48 (Android). Design system tokens CSS. Anti-patterns: 5+ cores ruído, 4+ fontes Frankenstein | **v0.1.0 (2026-05-08)** |
| [audio-musica-ia](audio-musica-ia/SKILL.md) | **Pesquisa de campo (volatility HIGH)**. Geração música IA 2026: **Suno v5.5 lider** (2M paid subs, $300M ARR, 8min v4.5, 1.200 genre tags, voice cloning + Suno Studio DAW v5.5), **Udio inpainting único** (substituir 2s surgical, 48kHz audiophile), AIVA orchestral, Beatoven.ai marketing-focused, Soundraw granular, Stable Audio open-source, ElevenLabs Music novo. **Voz IA**: **ElevenLabs líder** (Instant 1-2min vs Professional 30min cloning, **dubbing 30+ idiomas com lip sync**, Free 10k SEM commercial / **Starter $5 OBRIGATÓRIO commercial** / Creator $22 / Pro $99 / Business $1.320), Adobe Podcast (free enhance), Descript Overdub + text-based editing, Murf, PlayHT. **Background music**: Mubert royalty-free, Soundraw, Epidemic Sound whitelisting auto YT/IG/TikTok. **Copyright STATUS CRÍTICO 2026**: **Suno v Sony lawsuit ATIVA** (Warner settled nov/2025, Universal-Udio settled out/2025, Sony única litigando, **ruling fair-use SUMMER 2026 = pivotal**). Original lyrics + paid plan = ToS commercial OK; **Suno Enterprise = IP indemnification**. **Sonic branding cases**: Intel 4-note iconic, **McDonald's I'm Lovin' It $2B brand value**, Netflix ta-dum, Coca-Cola can opening **+34% purchase intent neurociência**; **audio assets 3.44x mais efetivos que visual** (Ipsos), **+96% brand recognition** com sonic consistente; mercado **$1.12B 2024 CAGR 13.9%**. **5 elementos sonic branding**: audio logo (3-5s), sonic mnemonic, jingle/anthem, soundscape, brand voice. Use cases: Reels music, podcast intro/outro, jingle, voiceover ads, audiobook (90% mais barato que studio tradicional), dubbing internacional. **Compliance BR**: ECAD, CONAR audio, Lei 15.325/2026 (disclosure IA), **LGPD voz como dado biométrico** (termo escrito obrigatório), ECA Digital. Loudness: -16 LUFS Reels/TikTok, -14 YouTube, -19 audiobook, -23 broadcast TV. Anti-patterns: Suno free comercial, voice cloning sem consentimento, sonic inconsistente | **v0.1.0 (2026-05-08)** |

## Skills de Multi-Platform Strategy (NOVO bloco — ✅ COMPLETO 3/3)

| Skill | Tema | Status |
|-------|------|--------|
| [github-presence](github-presence/SKILL.md) | **Pesquisa de campo (volatility medium)**. GitHub como canal marketing técnico subestimado (100M+ devs, audiência high-intent, zero CPC). **Profile README pessoal**: first impression dev (translate focus 1 line), every section earns place, dynamic stats (ReadMe Stats, Streak, Activity Graph), Mermaid diagrams 10s comprehension; awesome-github-profile-readme curated. **Organization page**: GitHub 2026 Brand Guidelines 89p oficial, employer branding (75% job seekers research before apply, AI synthesizes employer summaries via ChatGPT/Perplexity). **Repository README**: **10s time-to-value loop**, badges essenciais, demo GIF top, install 1-comando, quickstart 5-lines code. **GitHub SEO**: nome+description+**20 topics max** (tags = discoverability), README first 200 words críticos. **Awesome-lists distribution underrated** mas permanente high-DA (sindresorhus/awesome meta-list). **Launch tactics 2026**: **48h concentrado >> distribuído** (HN+Reddit+PH+X simultâneos triggers Trending algorithm); **HN impact: avg +121 stars/24h, +189/48h, +289/sem**. **GitHub Sponsors monetization**: **100% repasse personal** (sem fees), enterprise tiers $500-2k/mês críticos; **cases**: Caleb Porzio **$112k+/ano + $1M total**, Tanner Linsley React Query **$45k/mês**, AFFiNE 60K stars/33k em 18 meses. GitHub Pages free + custom domain (CNAME), GitHub Actions visibility, Stars program, Discussions, Projects. Anti-patterns: README só badges decorative, 1 launch + crickets, project abandonado 6m+, comprar stars (ban risk), star-begging, FUD comparações | **v0.1.0 (2026-05-08)** |
| [multi-platform-narrative](multi-platform-narrative/SKILL.md) | **Pesquisa de campo (volatility medium)**. **Cross-posting idêntico = SUPPRESSED em todas plataformas 2026** (LinkedIn external links -60%, X cross-post automated suppressed). Native content boosted universalmente. **Atomic content vs Repurposing**: atomization = quebrar pillar em peças independentes (1 webinar 60min → 30+ pieces); repurposing = reformatar pillar novo formato. **Hub-and-spoke model**: 1 pillar long-form (45-60min webinar/3000+ blog post/podcast 30min) + N spokes platform-specific = **+35% reach vs isolated posts**, **+40% output sem aumentar tempo**. **9:16 gold standard 2026** (1080x1920) — **95% mobile video consumption**; LinkedIn vertical preferential placement 2026; 16:9 ainda usado YouTube long + LinkedIn landscape. **Length por plataforma**: TikTok 11-18s viral / 21-34s storytelling / 30-60s educational; Reels 60-90s sweet spot; LinkedIn doc 7-10 slides; X thread 8-12 tweets; YouTube long 8-15min sweet; podcast 25-45min. **Tom + voice por plataforma**: LinkedIn formal/B2B / IG visual+aspirational / TikTok casual+entertaining / X polêmico+real-time / YouTube tutorial+long-form / blog SEO long-tail. **Sequencing temporal 3 estratégias**: simultaneous (HN/PH/Reddit launch — velocity Trending), waterfall (single-by-single Spotify EP-style), cascade (cada plataforma janela 24-48h). 3-phase: pre-launch 6-8 sem + launch 1-2 sem + post-launch 4-6 sem. **AI repurposing tools 2026**: Opus Clip ($19-99/mês auto clips long-form com virality score), Repurpose.io ($19-49/mês auto distribution), Castmagic ($29-99/mês podcast→text), Riverside Magic Clips, Descript ($24+/mês), ChatGPT/Claude prompt template adaptation. Brand voice doc per-platform; calendar editorial template hub-and-spoke. Anti-patterns: copy-paste idêntico, watermarks cross-platform, hashtags transversais, length wrong, sem captions accessibility (-30% reach), ignorar timezone | **v0.1.0 (2026-05-08)** |
| [escrita-por-publico](escrita-por-publico/SKILL.md) | **Pesquisa de campo (volatility LOW — 12 meses)**. Adapta por **AUDIÊNCIA** (vs `multi-platform-narrative` que adapta por PLATAFORMA). **Framework 4D**: Who+Need+Action+Context. **6 audiências canônicas**: **(1) B2B** formal autoritativo data-driven, sem slang/memes, vende eficiência+crescimento+custo; **(2) B2C** emocional conversacional human, casual fun, vende conveniência+diversão+sentimentos, sem corporate buzzwords; **(3) Investor (seed/A/B 2026)** **'efficient growth' >> 'growth at all costs'**, **authenticity > polish** (slick deck = red flag), grounded+honest+proven metrics+realistic projections, founder learnings genuínos não-AI-generated; estrutura YC pitch 10 slides, métricas Series A target (NRR 110%+, CAC payback <18m, burn multiple <1.5, Rule of 40); **(4) Government/setor público BR** **Lei 14.133/2021 Nova Lei Licitações**, RFP/RFQ format estrito, jurídico-formal indireto impessoal, certidões + atestados + ICP-Brasil mandatory; **(5) Talent/recruiting** **88% candidates dizem employer brand influencia decisão apply**, authenticity > polish, transparent salary range mandatory, mobile-first, real photos não stock, anti-padrões "family"+"rockstars"+"unlimited PTO sem context"; **(6) Developer/técnico** code-first + API docs (use case > endpoint reference), Microsoft/Google Developer/Write the Docs styles, sem marketing speak, concise. **Same insight, 6 versões** (insight base "30min onboarding calls = 3x retention" reescrito 6x). **Audience-aware 2026**: psychographics > demographics, brief writers com **audience language vs brand language**, AI-powered psychographic analysis. Combinar com `multi-platform-narrative` = matriz 6 audiências × 9 plataformas = 54 manifestações. Anti-patterns: one-size-fits-all, B2B em ad B2C, marketing speak em docs, hype em investor deck, casual em RFP gov, polish demais em recruiting | **v0.1.0 (2026-05-08)** |

## Skills de Pesquisa & Inteligência de Mercado (acionamento automático)

| Skill | Tema |
|-------|------|
| `sizing-mercado` | TAM/SAM/SOM, oportunidade |
| `persona-icp` | Persona, ICP, JTBD |
| `analise-concorrencia` | Benchmark, posicionamento competitivo, gaps |
| `pesquisa-qualitativa` | Entrevista, focus group, etnografia, roteiro |
| `pesquisa-quantitativa` | Pesquisa, amostra, intervalo de confiança |
| `tendencias-trendwatching` | Sinais fracos, white-space, oportunidade |

## Skills de UX/UI (acionamento automático)

| Skill | Tema |
|-------|------|
| `ux-heuristicas` | Nielsen, hierarquia, fluxos |
| `microcopy` | Botão, erro, vazio, sucesso, onboarding |
| `acessibilidade-wcag` | WCAG 2.1, contraste, leitor de tela, ARIA |
| `design-system-basico` | Tokens, componentes, consistência |

## Skills de Psicologia & Influência (acionamento automático)

| Skill | Tema |
|-------|------|
| `gatilhos-eticos` | Cialdini, escassez, autoridade — uso ético |
| `vies-cognitivo` | Heurísticas, ancoragem, framing |
| `prova-social-honesta` | Depoimento real, case verificável |

## Skills de Conhecimento de Plataforma (acionamento automático — high volatility)

| Skill | Tema |
|-------|------|
| `conhecimento-meta-ads` | Manager, públicos, criativos, política Meta |
| `conhecimento-google-ads` | Search, PMax, YouTube, política Google |
| `conhecimento-linkedin-ads` | Campaign Manager, pixel, conversões LinkedIn |
| `conhecimento-ga4` | GA4, eventos, conversões, audiences |
| `conhecimento-search-console` | Cobertura, queries, performance |
| `conhecimento-conar-cdc` | CONAR, CDC, peças veiculadas no Brasil |

## Skills Corporativas & Humanitárias (acionamento automático)

| Skill | Tema |
|-------|------|
| `comunicacao-corporativa` | RP, comunicado, manifesto institucional |
| `employer-branding` | Marca empregadora, atração e retenção |
| `comunicacao-crise` | Resposta a crise, gerenciamento de narrativa |
| `esg-comunicacao` | ESG sem greenwashing |
| `terceiro-setor` | Captação, narrativa de propósito, doação |
| `empreendedorismo-impacto` | MVP de comunicação para negócio nascente |

## Meta-skill

| Skill | Tema |
|-------|------|
| `manutencao-skills` | Re-grounding, decaimento temporal, controle de `next_review` |

## Tiers de Decaimento (proposta inicial)

- **high** (1–3 meses): plataformas (Meta, LinkedIn, Google, TikTok), GA4, Search Console, política CONAR/CDC, tendências.
- **medium** (6 meses): SEO técnico, frameworks de pesquisa, métricas-padrão, copy de plataforma.
- **low** (12 meses): metodologias (contraditório, posicionamento, persona, jornada), psicologia da persuasão, princípios de UX.
- **very-low** (24 meses): infra do plugin (init, stack, audit, review, help, save-session, juiz, perfil).

> Tiers definitivos serão atribuídos quando cada skill for criada. Detalhes em [`../../docs_mkt/ROADMAP-FRANK-MKT.md`](../../docs_mkt/ROADMAP-FRANK-MKT.md).
