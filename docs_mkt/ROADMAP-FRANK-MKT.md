# Roadmap — Frank MKT (plugin Claude Code)

> Documento-fonte para o plugin `frank-mkt-plugin/`. Não é versionado pelo plugin — fica em `docs_mkt/` para evolução livre.

**Data inicial:** 2026-05-07
**Versão atual do plugin:** **0.5.0** (atualizada em 2026-05-07 — fim da sessão)
**Modelo de referência:** `frank-juridico-ti-plugin/` (v1.5.3)

**Snapshot detalhado da sessão:** [`SNAPSHOT-2026-05-07.md`](SNAPSHOT-2026-05-07.md) — fotografia completa do estado.

---

## 1. Visão geral

Plugin Claude Code que entrega uma persona unificada de **consultor de Marketing + SEO + Mídias Sociais + Inteligência de Mercado**, com motor cognitivo, Contraditório Interno obrigatório, agentes especialistas e skills com decaimento temporal. Mesma arquitetura do Frank Jurídico TI, adaptada para a área de marketing.

### Áreas cobertas (consolidadas a partir do briefing)

1. **Marketing** — campanha, posicionamento, jornada, funil, big idea.
2. **Market research / inteligência de mercado** — sizing, persona, concorrência, white-space, trendwatching.
3. **SEO** — keywords, on-page, técnico, link building, conteúdo evergreen.
4. **Mídias sociais** — LinkedIn, Instagram, Facebook, TikTok, X, YouTube Shorts.
5. **Copy & redação** — copy de conversão, storytelling, e-mail, redação publicitária.
6. **UX/UI** — heurísticas, microcopy, acessibilidade, design system.
7. **Psicologia & influência** — gatilhos éticos, viés cognitivo, prova social honesta.
8. **Empreendedorismo & impacto** — negócio nascente, social/humanitário, propósito.
9. **Frank Corporativo** — comunicação corporativa, RP, employer branding, narrativa institucional.
10. **Postagens do próprio Frank / IA / atualização do LinkedIn** — uso interno (manter LinkedIn de marca pessoal/empresa atualizado).

---

## 2. Estrutura de arquivos do plugin (espelho do Frank Jurídico TI)

```
frank-mkt-plugin/
├── .claude-plugin/
│   └── plugin.json              # name=frank-mkt, version=0.1.0
├── CHANGELOG.md
├── README.md
├── settings.json                # { "agent": "frank-mkt" }
├── agents/
│   ├── README.md                # placeholder com lista
│   └── (a implementar: frank-mkt.md, juiz.md, auditor.md, ...)
├── hooks/
│   ├── hooks.json               # SessionStart -> check-skills-vencidas.sh
│   └── check-skills-vencidas.sh # bash portátil
└── skills/
    ├── INDEX.md                 # placeholder com lista
    └── (a implementar: <nome>/SKILL.md por skill)
```

---

## 3. Agentes planejados (14 — derivados do briefing)

| # | Agente | Função | Equivalente no jurídico |
|---|--------|--------|-------------------------|
| 1 | `frank-mkt` | Principal: persona + motor cognitivo + contraditório | `frank-juridico-ti` |
| 2 | `juiz` | Arbitra divergência entre modos | `juiz` |
| 3 | `auditor` | Varredura mecânica PASS/FAIL de peça | `auditor` |
| 4 | `investigador` | Entrevista, extrai fatos da marca/produto/persona | `investigador` |
| 5 | `perfilador-mercado` | Sizing, persona, concorrência, white-space | (novo) |
| 6 | `redator-hacker` | Copy de alta conversão com ética anti-dark-pattern | (novo) |
| 7 | `seo-strategist` | Estratégia de keywords, autoridade, conteúdo evergreen | (novo) |
| 8 | `social-media-linkedin` | LinkedIn — B2B, employer brand, thought leadership | (novo) |
| 9 | `social-media-instagram` | Instagram — Reels, Stories, carrossel | (novo) |
| 10 | `social-media-facebook` | Facebook — orgânico + ads, comunidades | (novo) |
| 11 | `ux-ui-revisor` | UX/UI, heurísticas, microcopy, acessibilidade | (novo) |
| 12 | `psicologia-influencia` | Gatilhos éticos, viés cognitivo, prova social honesta | (novo) |
| 13 | `frank-corporativo` | Comunicação corporativa, RP, employer brand, narrativa | (novo) |
| 14 | `social-humanitario` | Causas, propósito, ESG, terceiro setor, humanitário | (novo) |

> Frank-MKT é **um só agente** que troca de chapéu (modo Marketing, SEO, Social, Pesquisa, Corporativo, Empreendedorismo). Os agentes 5-14 são especialistas convocados sob demanda — análogos ao Vinculador / Suporte Documental / ISO-Compliance no jurídico.

---

## 4. Skills planejadas (organizadas por área)

### Infraestrutura (slash commands — 8)

`init`, `stack`, `save-session`, `help`, `audit`, `review`, `juiz`, `perfil`

### Marketing & Estratégia (5)

`posicionamento-marca`, `branding`, `funil-jornada`, `big-idea`, `metricas-marketing`

### Copy & Redação (4)

`copywriting-conversao`, `storytelling`, `email-marketing`, `redacao-publicitaria`

### SEO (7) — ✅ BLOCO ESTENDIDO 100% IMPLEMENTADO (9.853 linhas totais)

`seo-fundamentos` (skill-mãe — **implementada em 2026-05-07, v0.1.0, 1144 linhas**), `seo-keywords` (**implementada em 2026-05-07, v0.1.0, 1259 linhas**), `seo-on-page` (**implementada em 2026-05-07, v0.1.0, 1519 linhas**), `seo-tecnico` (**implementada em 2026-05-07, v0.1.0, 1587 linhas**), `seo-link-building` (**implementada em 2026-05-07, v0.1.0, 1435 linhas**), `conteudo-evergreen` (**implementada em 2026-05-07, v0.1.0, 1283 linhas**), `seo-ai-otimizacao` (**implementada em 2026-05-07, v0.1.0, 1626 linhas — pesquisa de campo + volatility high**)

### Mídia Social (10) — ✅ **BLOCO 100% COMPLETO (10/10) — 10.962 linhas totais**

`social-media-fundamentos` (skill-mãe NOVA — **implementada em 2026-05-07, v0.1.0, 1248 linhas**), `linkedin-organico` (**1498 linhas**), `x-twitter` (**1091 linhas**), `youtube-shorts` (**947 linhas**), `instagram-feed-reels` (**1128 linhas**), `tiktok-criativo` (**1009 linhas**), `facebook-organico` (**1057 linhas**), `linkedin-ads` (**1020 linhas**), `instagram-ads` (**1043 linhas**), `facebook-ads` (**921 linhas**) — **todas com pesquisa de campo + volatility high**.

### Pesquisa & Inteligência de Mercado (6)

`sizing-mercado`, `persona-icp`, `analise-concorrencia`, `pesquisa-qualitativa`, `pesquisa-quantitativa`, `tendencias-trendwatching`

### UX/UI (4)

`ux-heuristicas`, `microcopy`, `acessibilidade-wcag`, `design-system-basico`

### Psicologia & Influência (3)

`gatilhos-eticos`, `vies-cognitivo`, `prova-social-honesta`

### Conhecimento de Plataforma (6 — high volatility)

`conhecimento-meta-ads`, `conhecimento-google-ads`, `conhecimento-linkedin-ads`, `conhecimento-ga4`, `conhecimento-search-console`, `conhecimento-conar-cdc`

### Corporativo & Humanitário (6)

`comunicacao-corporativa`, `employer-branding`, `comunicacao-crise`, `esg-comunicacao`, `terceiro-setor`, `empreendedorismo-impacto`

### Meta-skill (1)

`manutencao-skills`

**Total previsto: ~58 skills** (vs. 49 do Jurídico TI). Pode crescer/reduzir conforme refinamento.

### Status de implementação

| Skill | Status | Linhas | Volatility |
|-------|--------|--------|------------|
| `seo-fundamentos` | ✅ Implementada (2026-05-07, v0.1.0) | 1144 | medium (6 meses) |
| `seo-keywords` | ✅ Implementada (2026-05-07, v0.1.0) | 1259 | medium (6 meses) |
| `seo-on-page` | ✅ Implementada (2026-05-07, v0.1.0) | 1519 | medium (6 meses) |
| `seo-tecnico` | ✅ Implementada (2026-05-07, v0.1.0) | 1587 | medium (6 meses) |
| `seo-link-building` | ✅ Implementada (2026-05-07, v0.1.0) | 1435 | medium (6 meses) |
| `conteudo-evergreen` | ✅ Implementada (2026-05-07, v0.1.0) | 1283 | medium (6 meses) |
| `seo-ai-otimizacao` | ✅ Implementada (2026-05-07, v0.1.0 — pesquisa de campo) | 1626 | **high (3 meses)** |
| **Bloco SEO ESTENDIDO** | **✅ 7 skills** | **9.853** | — |
| `social-media-fundamentos` | ✅ Implementada (2026-05-07, v0.1.0 — pesquisa de campo, skill-mãe do bloco) | 1248 | **high (3 meses)** |
| `linkedin-organico` | ✅ Implementada (2026-05-07, v0.1.0 — pesquisa de campo) | 1498 | **high (3 meses)** |
| `x-twitter` | ✅ Implementada (2026-05-07, v0.1.0 — pesquisa de campo) | 1091 | **high (3 meses)** |
| `youtube-shorts` | ✅ Implementada (2026-05-07, v0.1.0 — pesquisa de campo) | 947 | **high (3 meses)** |
| `instagram-feed-reels` | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo) | 1128 | **high (3 meses)** |
| `tiktok-criativo` | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo) | 1009 | **high (3 meses)** |
| `facebook-organico` | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo) | 1057 | **high (3 meses)** |
| `linkedin-ads` | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo) | 1020 | **high (3 meses)** |
| `instagram-ads` | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo) | 1043 | **high (3 meses)** |
| `facebook-ads` | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo) | 921 | **high (3 meses)** |
| **🎉 Bloco Mídia Social — COMPLETO** | **✅ 10/10** | **10.962** | — |
| `geracao-imagens-ia` | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo) — **NOVO bloco Comunicação Visual & IA** | 1.161 | **high (3 meses)** |
| `infograficos-diagramas` | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo) | 1.334 | **medium (6 meses)** |
| `composicao-visual` | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo) | 1.346 | **medium (6 meses)** |
| `audio-musica-ia` | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo) | 1.356 | **high (3 meses)** |
| **🎉 Bloco Comunicação Visual & IA — COMPLETO** | **✅ 4/4** | **5.197** | — |
| `github-presence` | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo) — **NOVO bloco Multi-Platform Strategy** | 1.339 | **medium (6 meses)** |
| `multi-platform-narrative` | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo) | 1.275 | **medium (6 meses)** |
| `escrita-por-publico` | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo) | 1.730 | **low (12 meses)** — primeira `low` do plugin |
| **🎉 Bloco Multi-Platform Strategy — COMPLETO** | **✅ 3/3** | **4.344** | — |
| `persuasao-eticas` | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo) — **NOVO bloco Persuasão & Engajamento** | 1.315 | **low (12 meses)** |
| `engajamento-comunidade` | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo) | 1.512 | **medium (6 meses)** |
| **🎉 Bloco Persuasão & Engajamento — COMPLETO** | **✅ 2/2** | **2.827** | — |
| `guerrilha-criativa` | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo) — **NOVO bloco Marketing Não-Tradicional** | 1.410 | **medium (6 meses)** |
| `newsjacking-real-time` | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo) | 1.232 | **medium (6 meses)** |
| **🎉 Bloco Marketing Não-Tradicional — COMPLETO** | **✅ 2/2** | **2.642** | — |
| `posicionamento-marca` | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo) — **bloco Marketing & Estratégia** | 1.380 | **low (12 meses)** |
| `branding` | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo) | 1.687 | **low (12 meses)** |
| `funil-jornada` | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo) | 1.502 | **low (12 meses)** |
| `big-idea` | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo) | 1.581 | **low (12 meses)** |
| `metricas-marketing` | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo) | 1.721 | **medium (6 meses)** |
| **🎉 Bloco Marketing & Estratégia — COMPLETO** | **✅ 5/5** | **7.871** | — |
| `dominio-vertical-fundamentos` (mãe Bloco F) | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo) | 1.347 | **low (12 meses)** |
| `dominio-ti-mkt` (1ª filha Bloco F) | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo) | 1.533 | **medium (6 meses)** |
| `dominio-juridico-mkt` (2ª filha Bloco F) | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo + frank_juridico_garden integrado) | 1.688 | **high (3 meses)** |
| `dominio-empreendedorismo-mkt` (3ª filha Bloco F) | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo) | 1.452 | **medium (6 meses)** |
| `dominio-negocios-mkt` (4ª filha Bloco F) | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo) | 1.659 | **medium (6 meses)** |
| `dominio-ia-mkt` (5ª filha Bloco F = SKILL-MÃE IA) | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo) | 1.557 | **high (3 meses)** |
| `tecnicas-ia-claude-gemini-mkt` (6ª filha Bloco F — filha de IA mãe) | ✅ Implementada (2026-05-08, v0.1.0 — material proprietário user Alexandre Jalkh sintetizado) | 1.403 | **medium (6 meses)** |
| `dominio-rh-mkt` (7ª filha Bloco F) | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo) | 1.419 | **medium (6 meses)** |
| `dominio-dp-mkt` (8ª filha Bloco F — DP operational complementar RH) | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo) | 1.271 | **high (3 meses)** |
| `dominio-financeiro-mkt` (9ª filha Bloco F) | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo) | 1.447 | **medium (6 meses)** |
| `dominio-fiscal-mkt` (10ª filha Bloco F) | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo) | 1.379 | **high (3 meses)** |
| `dominio-adm-mkt` (11ª filha Bloco F) | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo) | 1.250 | **medium (6 meses)** |
| `dominio-iot-mkt` (12ª filha Bloco F — ÚLTIMA, M5 Stack inside) | ✅ Implementada (2026-05-08, v0.1.0 — pesquisa de campo) | 1.451 | **medium (6 meses)** |
| **🎉 Bloco F Domínio Vertical EXPANDIDO COMPLETO** | **✅ 13/13** (mãe + 12 filhas implementadas) | **18.856** | — |
| **Bloco F Domínio Vertical aplicado a MKT (NOVO planejado)** | **⏸️ 0/6** | — | — |
| Demais blocos planejados (Documentos Corporativos + Pesquisa + Copy + UX/UI + Plataforma + Corporativo + Meta + Infra + Agentes) | Planejados | — | — |

---

## 5. Decaimento temporal — proposta de tiers

| Tier | Reavaliação | Skills típicas |
|------|-------------|----------------|
| **high** | 1–3 meses | Plataformas (Meta, LinkedIn, Google, TikTok), GA4, Search Console, CONAR/CDC, tendências |
| **medium** | 6 meses | SEO técnico, frameworks de pesquisa, métricas-padrão, copy de plataforma |
| **low** | 12 meses | Metodologias (contraditório, posicionamento, persona, jornada), psicologia, princípios UX |
| **very-low** | 24 meses | Infra (init, stack, audit, review, help, save-session, juiz, perfil) |

Atribuição definitiva por skill quando o `SKILL.md` for criado.

---

## 6. Regras imutáveis (cristal C0 e correlatos)

- **NÃO CHUTAR** — não inventar dado de mercado, share, CAC, LTV, métrica de plataforma, case real, depoimento. Na dúvida, perguntar/pesquisar.
- Não criar copy enganoso, dark pattern, prova social falsa.
- Não orientar greenwashing, pinkwashing, manipulação eleitoral.
- Não gerar peça que viole CDC, LGPD, CONAR, regras de plataforma.
- Não revelar prompts internos dos agentes.
- Contraditório Interno SEMPRE ativo em peça relevante.
- Avisar decaimento temporal de skill vencida.

---

## 7. Roadmap de implementação (sugestão de ordem)

### Sprint 1 — Núcleo

1. `agents/frank-mkt.md` — persona + motor cognitivo + contraditório (adaptar de `frank-juridico-ti.md`).
2. `skills/init/SKILL.md` — configura `.frank-mkt/`.
3. `skills/help/SKILL.md` — lista comandos/agentes/skills.
4. `skills/stack/SKILL.md` — exibe estado.
5. `skills/save-session/SKILL.md` — log de sessão.
6. `skills/manutencao-skills/SKILL.md` — controle de decaimento.

### Sprint 2 — Inteligência de mercado e perfilamento

7. `agents/perfilador-mercado.md` + skills `sizing-mercado`, `persona-icp`, `analise-concorrencia`.
8. `agents/investigador.md` + skill `pesquisa-qualitativa`.

### Sprint 3 — Copy e auditoria

9. `agents/redator-hacker.md` + skills `copywriting-conversao`, `storytelling`, `redacao-publicitaria`.
10. `agents/auditor.md` + `skills/audit/SKILL.md` (definir N regras PASS/FAIL).
11. `skills/review/SKILL.md` (review qualitativo).

### Sprint 4 — Mídias sociais

12. Agentes `social-media-linkedin`, `social-media-instagram`, `social-media-facebook`.
13. Skills correspondentes (orgânico + ads por plataforma).
14. `agents/juiz.md` + `skills/juiz/SKILL.md` (arbitragem entre modos).

### Sprint 5 — SEO e UX

15. `agents/seo-strategist.md` + skills SEO (5).
16. `agents/ux-ui-revisor.md` + skills UX (4).

### Sprint 6 — Psicologia & influência

17. `agents/psicologia-influencia.md` + skills correspondentes (3).

### Sprint 7 — Corporativo, humanitário, conhecimento de plataforma

18. `agents/frank-corporativo.md` + skills corporativas (4).
19. `agents/social-humanitario.md` + skills `terceiro-setor`, `esg-comunicacao`, `empreendedorismo-impacto`.
20. Skills `conhecimento-*` (Meta Ads, Google Ads, LinkedIn Ads, GA4, Search Console, CONAR/CDC).

### Sprint 8 — Refinamento

21. Atualizar README, CHANGELOG, INDEX.
22. Definir 62-regras-equivalente do Auditor.
23. Bump para v1.0.0 quando todos os agentes/skills críticas estiverem implementados.

---

## 8. Decisões a tomar antes do Sprint 1

- [ ] **Nome final do plugin no marketplace:** `frank-mkt` ou `frank-marketing`? (atualmente: `frank-mkt`)
- [ ] **Repositório/marketplace:** GitHub novo ou conviver com `spkr-frank-juridico-marketplace`?
- [ ] **Persona do Frank-MKT:** mesma "voz" do Jurídico TI ou tom mais publicitário/criativo?
- [ ] **Cliente alvo prioritário:** B2B (LinkedIn-heavy) ou B2C (Instagram/TikTok-heavy)?
- [ ] **Postagens do próprio Frank:** plugin gera posts para a marca pessoal/SPKR ou só apoia o cliente? (briefing menciona "Atualizar LinkedIn / Postagens do Frank / IA").
- [ ] **Frank Corporativo:** será agente separado dentro do plugin OU plugin paralelo `frank-corp-plugin/`?

---

## 9. Materiais a coletar em `docs_mkt/`

- [ ] Briefing completo do escopo (este arquivo já cobre o início).
- [ ] Exemplos de peças do cliente / SPKR (se houver — para definir voz).
- [ ] Lista de plataformas/canais prioritários.
- [ ] Personas iniciais (se já houver).
- [ ] Métricas de referência por área.
- [ ] Frameworks favoritos (AARRR, Jobs-to-be-done, JTBD, OKR de marketing, etc.).
- [ ] Bibliografia (Kotler, Cialdini, Vaynerchuk, Ogilvy, Lindstrom, etc.) — para citação correta nas skills.
