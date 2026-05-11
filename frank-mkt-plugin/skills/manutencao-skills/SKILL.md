---
name: manutencao-skills
description: Meta-skill manutencao plugin frank-mkt — versionamento semver + decaimento temporal por volatility (high 3m / medium 6m / low 12m) + re-validacao via pesquisa de campo + lifecycle skill creation/update/deprecation + governance documental + INDEX/CHANGELOG/plugin.json/ROADMAP sync + paralelizacao agentes (4 paralelizacoes validadas v2.24-v2.27) + lessons learned. FECHA Bloco Meta-skill 1/1.
volatility: medium
last_review: 2026-05-09
next_review: 2026-11-09
languages: [pt-BR]
audience: [maintainer-frank-mkt, plugin-developers, knowledge-managers, doc-engineers]
ascii_only: true
---

# Skill: manutencao-skills

## Decaimento Temporal

**Volatility: MEDIUM (6 meses).**

**Justificativa do decaimento moderado:**

Manutencao de skills e um dominio meta — descreve como manter as outras 77 skills frescas. O nucleo e estavel (semver + lifecycle + audit), mas o ferramental de Knowledge Management evolui em ritmo medio:

- **Frameworks de freshness scoring (Atlan, Bloomfire, APQC):** novas metricas surgem 1-2x ao ano em 2026 (LLM Knowledge Base Freshness Scoring, Self-Healing Knowledge Systems).
- **Anthropic Skills (Agent Skills):** a especificacao de SKILL.md, frontmatter e progressive disclosure foi formalizada em fim de 2025 e segue evoluindo. Novas convencoes de metadata podem aparecer em releases trimestrais do Claude Code.
- **Padroes de versionamento:** semver 2.0.0 e estavel desde 2013. As politicas de deprecation N-2 / sunset 18-24m sao consolidadas. O que muda e a cadencia recomendada para conteudo (vs codigo).
- **Regulacao:** LGPD ANPD publica guidance que pode reclassificar volatility de skills inteiras (ex: conhecimento-meta-ads volatility high passa a critical se ANPD publicar nova orientacao sobre tracking).
- **Plataformas de paid media:** Meta, Google, TikTok, LinkedIn — mudam 5-15x por ano. Disparam re-validacoes nas skills high-volatility.

**Implicacoes praticas:**
- Esta skill `manutencao-skills` deve ser revisada a cada 6 meses (next_review: 2026-11-09).
- O catalogo de volatilities por skill (Fundacao 1) deve ser auditado a cada quarter.
- A lista de paralelizacoes validadas (Fundacao 7) e historica + cresce; nao precisa re-validacao, so adicao.

**Quando esta SKILL precisar de revisao acelerada (antes de 6 meses):**
1. Anthropic publica nova spec de SKILL.md (frontmatter, progressive disclosure, agentic invocation).
2. ANPD publica guidance que reclassifica volatility de skills do Bloco Conhecimento de Plataforma.
3. Plugin frank-mkt atinge 100+ skills (escala muda governance).
4. Surge ferramenta de auto-staleness-detection compativel com Claude Code skills.
5. Mudanca material em semver (release de v3.0.0 com novas regras de pre-release).

---

## Visao Geral

`manutencao-skills` e a meta-skill do plugin frank-mkt: documenta como manter, versionar, re-validar, deprecar e governar as outras 77 skills do plugin. Resolve um problema real: sem governance ativa, skills viram "documentacao zumbi" (lookup ainda funciona, mas o conteudo esta desatualizado e produz recomendacoes erradas).

**Por que manutencao-skills importa em 2026:**

- **Volume:** 77 skills implementadas + roadmap para 100+. Sem framework, manutencao vira caos.
- **Velocidade do dominio:** marketing digital muda 5-15x/ano por plataforma. Skills high-volatility (Meta Ads, Google Ads, LinkedIn Ads, TikTok) precisam re-validacao trimestral.
- **Cross-skill coupling:** uma skill cita outras 5-15 skills via Cross-Skill References. Quando uma deprecia, as referencias quebram. Sem governance, debt cresce exponencial.
- **Trust:** plugin frank-mkt e usado por founders/CMOs para decisoes reais. Skill desatualizada = recomendacao errada = perda de trust no plugin.
- **LGPD / regulacao:** conteudo regulatorio (LGPD, CONAR, CDC, Marco Civil) muda com guidance ANPD. Skills com base legal incorreta sao risco juridico para usuarios.

**Mudanca estrutural na pratica de manutencao 2024-2026 (essencial entender):**

A pratica migrou de **"documentacao estatica + revisao anual"** para **"living documentation + freshness scoring + auto-detection de staleness"**. Em 2026, knowledge management treats content like infrastructure: cada documento tem owner, last_verified, classification, domain. Sem `last_verified`, staleness detection e impossivel.

Frank-mkt adota essa filosofia via frontmatter YAML obrigatorio em toda SKILL.md (volatility + last_review + next_review + languages + audience + ascii_only).

**Posicao dentro do Bloco Meta-skill:**

`manutencao-skills` e a 1a e unica skill do Bloco Meta-skill. **FECHA o Bloco Meta-skill 1/1.** O bloco existe para documentar o proprio plugin (auto-referencia governance), nao um dominio de marketing externo. Outras skills meta (ex: `criacao-skill-novo-bloco`, `auditoria-trimestral`) podem nascer no futuro, mas sao satelites desta.

---

## Fundacao 1 — Volatility Tiers (high 3m / medium 6m / low 12m)

**Conceito:** cada skill recebe um tier de volatility no frontmatter. O tier define quando a skill deve ser re-validada.

**Tabela de tiers:**

| Tier     | Cadencia revisao | Justificativa                                          | Exemplos plugin frank-mkt                                                 |
| -------- | ---------------- | ------------------------------------------------------ | ------------------------------------------------------------------------- |
| **high** | 3 meses          | Plataformas + algoritmos + regulacao em movimento      | conhecimento-meta-ads, conhecimento-google-ads, instagram-feed-reels      |
| **medium** | 6 meses        | Metodologias estaveis + frameworks com refinamento     | manutencao-skills, esg-comunicacao, copywriting-conversao, branding       |
| **low**  | 12 meses         | Principios fundamentais + frameworks consolidados      | posicionamento-marca, persuasao-eticas, big-idea, vies-cognitivo          |

**Criterios de decisao para classificar:**

1. **Pergunta-chave:** "Em 6 meses, partes desta skill estarao numericamente erradas ou eticamente desatualizadas?"
   - Se sim em 0-3m -> high
   - Se sim em 3-6m -> medium
   - Se nao em <12m -> low

2. **Indicadores de high volatility:**
   - Cita numeros especificos de plataforma (CTR, CPM, ROAS benchmarks).
   - Cita features de produto que mudam (Advantage+ AI, Performance Max, Smart Bidding).
   - Cita politicas/regulacoes em formacao (ANPD guidance, DSA, AI Act enforcement).
   - Cita ferramentas SaaS com pricing/features volateis.

3. **Indicadores de medium volatility:**
   - Frameworks com refinamento gradual (e.g., AARRR, RACE, Jobs-To-Be-Done aplicado).
   - Metodologias com evolucao de pratica (e.g., copywriting AIDA + PAS + 4Cs).
   - Compliance estavel mas com guidance evolutiva (LGPD principios fixos, ANPD guidance evolutiva).

4. **Indicadores de low volatility:**
   - Principios cognitivos (vieses, gatilhos psicologicos, neurociencia do consumo).
   - Modelos mentais consolidados (Porter 5 forcas, BCG matrix, Ansoff).
   - Lei consolidada (CDC arts. fundamentais, CF/88 garantias).

**Aplicacao no plugin frank-mkt (catalogo de volatilities):**

- **High volatility (3m revisao):** todas as 6 skills do Bloco Conhecimento de Plataforma (conhecimento-meta-ads, conhecimento-google-ads, conhecimento-linkedin-ads, conhecimento-search-console, conhecimento-ga4, conhecimento-conar-cdc). Skills de plataformas de social organico (instagram-feed-reels, tiktok-criativo, x-twitter, youtube-shorts).
- **Medium volatility (6m revisao):** skills metodologicas com numeros (copywriting-conversao, email-marketing, seo-fundamentos, seo-on-page, metricas-marketing). Skills regulatorias com guidance (esg-comunicacao, comunicacao-crise, terceiro-setor). manutencao-skills (esta skill).
- **Low volatility (12m revisao):** posicionamento-marca, branding, big-idea, persuasao-eticas, vies-cognitivo, prova-social-honesta, gatilhos-eticos, storytelling, ux-heuristicas (Nielsen 10 sao pre-2000).

**Anti-pattern:** classificar skill regulatoria como low. Mesmo principios estaveis (LGPD bases legais) tem guidance ANPD que muda. Default: medium para qualquer skill com componente regulatorio.

---

## Fundacao 2 — Versionamento Semver + Frontmatter (last_review + next_review + volatility)

**Conceito:** plugin segue Semantic Versioning 2.0.0. Cada SKILL.md carrega frontmatter YAML com metadata mandatory.

**Semver no plugin (vMAJOR.MINOR.PATCH):**

- **MAJOR:** breaking change na arquitetura do plugin. Ex: rename de comandos slash, mudanca de estrutura de pastas, remocao de blocos inteiros. Em frank-mkt, MAJOR ainda e v2.x — v3 hipotetico se Anthropic publicar nova spec de SKILL.md incompativel.
- **MINOR:** adicao de nova skill, novo bloco, ou refinamento estrutural backward-compatible. Ex: v2.24.0 adiciona Bloco Corporativo 6/6. v2.25.0 adiciona Bloco Copy 4/4.
- **PATCH:** correcao em skill existente (bug em exemplo, link quebrado, typo, atualizacao de stats sem mudar estrutura). Ex: v2.27.1 corrige link na skill conhecimento-meta-ads.

**Regras semver aplicadas:**

1. **Once released, immutable.** v2.24.0 nao pode ser modificada apos publicada. Correcoes vao para v2.24.1 ou v2.25.0.
2. **Deprecation triggers MINOR.** Marcar uma skill como `deprecated: true` no frontmatter eleva MINOR (semver issue 712 + 835).
3. **Remocao de skill triggers MAJOR.** Apagar uma skill que outras citam quebra Cross-Skill References = breaking change.
4. **Pre-release tags opcionais.** v2.28.0-beta.1 para testes antes do release.
5. **Build metadata opcional.** v2.27.0+20260509 para identificar build especifica.

**Frontmatter YAML mandatory em toda SKILL.md:**

```yaml
---
name: nome-skill-kebab-case
description: <500 chars, primeira frase deve disparar lookup correto pelo agente
volatility: high|medium|low
last_review: YYYY-MM-DD
next_review: YYYY-MM-DD  # last_review + 3/6/12 meses conforme volatility
languages: [pt-BR]       # array, futuro suporte multi-lingua
audience: [persona1, persona2, persona3]
ascii_only: true
---
```

**Campos extras opcionais (futuro):**

- `deprecated: true` — marca skill em sunset.
- `superseded_by: nome-da-skill-substituta` — aponta sucessora.
- `experimental: true` — skill em beta, sem garantia de estabilidade.
- `external_dependencies: [meta-ads-api, ga4-api]` — declara dependencias para staleness detection.

**Por que esses campos especificos:**

- `last_verified` (Atlan, 2026): metadata mandatory para staleness detection. Frank-mkt usa `last_review` (mesma semantica).
- `volatility` + `next_review`: derivam cadencia automatica. Sem next_review, manutencao vira "lembrar manualmente" = entropy.
- `ascii_only: true`: marker explicito de policy do plugin (sem acentos PT-BR — Fundacao 6 explica rationale).
- `audience`: ajuda lookup do agente Claude (semantic match com persona do user).

**Anti-pattern:** frontmatter sem next_review. Resultado: skill envelhece sem trigger de revisao.

---

## Fundacao 3 — Re-validacao via Pesquisa de Campo (6 web searches paralelas)

**Conceito:** quando next_review chega, ou quando trigger acelerado dispara, a skill passa por re-validacao com pesquisa de campo obrigatoria. Padrao do plugin: 6 web searches paralelas + cross-checking 5+ sources independentes.

**Por que 6 searches paralelas:**

- **Cobertura:** dominio multi-faceted (e.g., conhecimento-meta-ads: algoritmo + AI + privacidade + creative + benchmarks + regulacao). 1-2 searches deixam blind spots.
- **Custo otimo:** 6 e o limite pratico antes de retornar diminishing returns + ruido. Mais que 6 polui contexto.
- **Paralelismo:** 6 chamadas WebSearch simultaneas no Claude Code rodam em ~10-20s. Sequencial levaria 60-120s.
- **Validacao cruzada:** numeros que aparecem em 3+ das 6 searches sao trustworthy. Numero unico em 1 search = flag.

**Template das 6 searches por skill (high volatility):**

1. `<topico> 2026 trends`
2. `<topico> 2026 statistics benchmarks`
3. `<topico> 2026 best practices`
4. `<topico> 2026 case studies`
5. `<topico> 2026 regulation policy compliance`
6. `<topico> 2026 platform updates features`

**Template para skills metodologicas (medium volatility):**

1. `<framework> 2026 evolution`
2. `<framework> 2026 case studies enterprise`
3. `<framework> 2026 critique limitations`
4. `<framework> 2026 alternatives`
5. `<framework> 2026 measurement metrics`
6. `<framework> 2026 industry adoption`

**Template para skills de principios (low volatility):**

1. `<principio> 2026 academic research updates`
2. `<principio> 2026 application examples`
3. `<principio> 2026 critiques`
4. `<principio> Brazil specifics`
5. `<principio> ethics application 2026`
6. `<principio> AI era application`

**Cross-checking 5+ sources independentes:**

Numeros, claims e estatisticas devem ser validados em:
1. **Fonte primaria** (relatorio oficial da plataforma, ex: Meta Reports, Google Insights).
2. **Industry analyst** (Gartner, Forrester, IDC, Hootsuite Social Media Trends).
3. **Plataforma agregadora** (Statista, eMarketer, AdAmigo).
4. **Pratica de mercado** (case studies, agencias publishing benchmarks).
5. **Regulador / policy** (ANPD, FTC, CMA, CONAR).

**Quando claim aparece em <3 fontes -> flag como "evidencia fraca" no texto.**

**Disciplina critica:**

- **NUNCA inventar URL.** Se search nao retornou link, escrever generico ("relatorio Meta Q1/2026") sem hyperlink falso.
- **NUNCA inventar estatistica.** Se nao achou numero confirmavel, escrever "estimativas variam entre X e Y conforme metodologia".
- **NUNCA citar tweet/post LinkedIn como fonte primaria.** OK para color/anedota, NAO para benchmark.
- **DATAR claims explicitamente.** "Q1/2026 benchmark" envelhece graciosamente; "atualmente" envelhece mal.

**Anti-pattern:** atualizar skill sem nova pesquisa. Resultado: skill antiga + novo wrapper texto = lipstick on pig.

---

## Fundacao 4 — Lifecycle Skill (Creation + Update + Deprecation + Sunset)

**Conceito:** skills tem ciclo de vida bem-definido. Cada estagio tem checklist obrigatorio.

### Estagio 1: Creation (nascimento de nova skill)

**Trigger:** roadmap define nova skill, ou usuario do plugin reporta gap critico.

**Checklist:**
1. Pesquisa de campo: 6 web searches paralelas no topico (Fundacao 3).
2. Escrita SKILL.md com estrutura padrao do plugin (frontmatter + 8 fundacoes + anti-patterns + 18 regras + exemplos + checklist + referencias + cross-skill + integracao + disclaimer).
3. Decisao volatility (Fundacao 1).
4. Frontmatter completo (Fundacao 2).
5. Cross-skill references: identificar 8-15 skills relacionadas e citar.
6. Update 4 trackers (Fundacao 5): INDEX.md + CHANGELOG.md + plugin.json + ROADMAP.
7. Commit semver (MINOR bump por nova skill).
8. Update memoria persistente do projeto (`MEMORY.md` user-level).

**Tempo medio:** 30-60 minutos por skill quando 1 agente. Reduz a 5-10 minutos quando paralelizado em 4-7 agentes (Fundacao 7).

### Estagio 2: Update (manutencao programada ou triggered)

**Trigger:** next_review atingido OU acelerador disparado (regulacao, plataforma, mercado).

**Checklist:**
1. Re-pesquisa: 6 web searches paralelas atualizadas (Fundacao 3).
2. Diff: comparar findings novos vs SKILL.md atual. Listar mudancas.
3. Edicao incremental: nao reescrever inteira; preservar blocos estaveis, atualizar pontuais.
4. Update frontmatter: `last_review: <hoje>`, `next_review: <hoje + 3/6/12m>`.
5. Adicionar entrada em CHANGELOG.md (PATCH ou MINOR conforme escopo).
6. Update plugin.json se MINOR (versao + descricao).
7. Verificar cross-skill references: nenhuma referencia quebrou? Nenhuma skill referenciada deprecada?

**Diferenca PATCH vs MINOR no update:**
- **PATCH:** corrige stat numerica, atualiza link, ajusta exemplo. Estrutura intocada.
- **MINOR:** adiciona nova fundacao, novo anti-pattern, nova persona em exemplos, nova referencia regulatoria.

### Estagio 3: Deprecation (skill superseded ou domain shrinks)

**Trigger:** outra skill assume escopo, plataforma morreu (ex: Google+), framework caiu em desuso.

**Checklist:**
1. Adicionar `deprecated: true` no frontmatter.
2. Adicionar `superseded_by: nome-skill-sucessora` se aplicavel.
3. Adicionar banner no topo: "DEPRECATED em YYYY-MM-DD. Use <skill-sucessora>. Sunset em YYYY-MM-DD (90 dias)."
4. Update CHANGELOG.md com entrada deprecation (MINOR bump).
5. Update INDEX.md mostrando status `[DEPRECATED]`.
6. Auditar cross-skill references: outras skills citando esta devem ter referencia atualizada para sucessora.
7. Comunicar usuarios: nota em README.md `## Deprecations` + memoria persistente.

**Periodo de coexistencia:** 30-90 dias entre deprecation e sunset. Ajuste conforme severidade.

### Estagio 4: Sunset (remocao definitiva)

**Trigger:** periodo de deprecation expirou.

**Checklist:**
1. Mover SKILL.md para `skills/_deprecated/<skill-name>/` (preserva historia git).
2. Update INDEX.md removendo entrada da listagem ativa.
3. Update plugin.json (MAJOR bump se quebra cross-skill references; MINOR se sucessora ja absorveu).
4. CHANGELOG.md entrada sunset.
5. Commit semver.
6. Verificar: nenhuma skill ativa cita a removida.

**Lessons learned no plugin frank-mkt:**

- **Frank-mkt v1.x -> v2.x foi MAJOR justamente porque mudou estrutura de skills (de single-file para pasta dedicada com SKILL.md).**
- **v2.24.0 -> v2.27.0 (5 sessoes em ~1 mes) foi MINOR continuo: adicao de Blocos Corporativo + Copy + UX/UI + Psicologia + Conhecimento.**
- **Ainda nao houve deprecation real no plugin (todas 77 skills sao ativas em 2026-05-09). Esta skill (manutencao-skills) e a primeira a documentar formalmente o processo.**

---

## Fundacao 5 — Trackers Sync (INDEX + CHANGELOG + plugin.json + ROADMAP)

**Conceito:** quando uma skill e criada/atualizada/deprecada, 4 trackers devem ser sincronizados. Falha em qualquer um = inconsistencia que polui descoberta.

### Tracker 1: `INDEX.md` (raiz do plugin)

**Funcao:** listagem human-readable de todas as skills, agrupadas por bloco, com status.

**Schema esperado por linha:**
```
| <numero> | <nome-skill> | <bloco> | <volatility> | <last_review> | <status> |
```

**Status possiveis:** `active`, `deprecated`, `experimental`, `sunset-scheduled`.

**Quando atualizar:**
- Creation: nova linha adicionada na secao do bloco.
- Update: coluna `last_review` atualizada.
- Deprecation: status muda para `deprecated`, adicionar coluna `superseded_by`.
- Sunset: linha removida (preservada em git history).

### Tracker 2: `CHANGELOG.md` (raiz do plugin)

**Funcao:** historia versionada do plugin no padrao Keep a Changelog (https://keepachangelog.com/).

**Schema por entrada:**
```
## [v2.28.0] - 2026-05-09

### Added
- Skill `manutencao-skills`: meta-skill manutencao + governance. FECHA Bloco Meta-skill 1/1.

### Changed
- Skill `conhecimento-meta-ads`: atualizado benchmark Q1/2026 (CTR 1.04%, CPM R$ 18,50).

### Deprecated
- (nenhuma)

### Removed
- (nenhuma)

### Fixed
- Link quebrado em skill `seo-fundamentos` (referencia 12).
```

**Quando atualizar:** TODA mudanca que dispara semver bump (PATCH/MINOR/MAJOR) deve ter entrada CHANGELOG.

### Tracker 3: `.claude-plugin/plugin.json` (manifest)

**Funcao:** manifest oficial do Claude Code plugin. Define versao instalavel.

**Campos relevantes para manutencao:**
```json
{
  "name": "frank-mkt",
  "version": "2.28.0",
  "description": "<inclui contagem de skills atualizada>",
  "author": "Alexandre Jalkh",
  "skills_count": 78
}
```

**Quando atualizar:**
- Creation: incrementar `version` (MINOR), `skills_count`, atualizar `description` se mudou bloco.
- Update PATCH: incrementar `version` patch.
- Deprecation: nao muda `skills_count` (skill ainda existe). Atualiza descricao se relevante.
- Sunset: decrementa `skills_count`, MAJOR bump se quebra cross-skill.

### Tracker 4: `docs_mkt/ROADMAP-FRANK-MKT.md`

**Funcao:** roadmap publico de blocos planejados, em progresso, fechados.

**Schema por linha de bloco:**
```
| Bloco | Skills planejadas | Skills entregues | Status | Data fechamento |
```

**Status possiveis:** `planejado`, `em-progresso`, `fechado`, `parcial`.

**Quando atualizar:**
- Creation de skill que pertence a bloco em-progresso: atualizar contagem.
- Bloco completo: status muda para `fechado`, registrar data.
- Adicao de nova skill em bloco fechado: bloco volta a `parcial` ou abre v2 do bloco.

### Tracker bonus: `MEMORY.md` (user-level, fora do repo)

**Funcao:** memoria persistente Claude Code do mantenedor.

**Quando atualizar:** apos cada release MINOR ou MAJOR. Registra HEAD commit, contagem skills, blocos fechados.

**Localizacao no setup do mantenedor frank-mkt (Alexandre):** `C:\Users\alexa\.claude\projects\D--4nk--cria-frank-juridico-ti-marketplace\memory\MEMORY.md`.

**Anti-pattern:** atualizar 1-2 trackers e esquecer outros 2-3. Resultado: usuario instala via plugin.json mas INDEX.md mostra contagem errada = confusao.

---

## Fundacao 6 — Brasil 2026 Especificidades (LGPD + Brasil cultural codes + tropicalizacao)

**Conceito:** plugin frank-mkt e brazilian-first. Especificidades regulatorias e culturais influenciam manutencao.

### LGPD compliance no proprio plugin

- **Plugin nao processa dados pessoais.** SKILL.md sao conteudo educacional, sem PII.
- **Mas:** skills citam exemplos de tratamento de dados (ex: conhecimento-meta-ads cita CAPI). Esses exemplos devem ser ANPD-aligned.
- **Guidance ANPD que dispara re-validacao:**
  1. Resolucao CD/ANPD nova (transferencia internacional, base legal, agentes).
  2. Tomada de subsidios sobre tema relevante (e.g., AI Act brasileiro, tracking).
  3. Sancao publicada (precedente).

- **Skills com componente LGPD que precisam vigilancia:** conhecimento-meta-ads, conhecimento-google-ads, conhecimento-linkedin-ads, conhecimento-ga4, conhecimento-search-console, conhecimento-conar-cdc, comunicacao-corporativa, esg-comunicacao, terceiro-setor.

### Brazil cultural codes

- **Tom:** plugin usa tom direto, brazilian-warm, sem corporate-speak importado. Manutencao preserva esse tom.
- **Exemplos:** preferir cases brasileiros (Magalu, iFood, Nubank, Mercado Livre, Natura, Localiza, RD Saraiva) sobre cases US (Amazon, Apple, Google) quando ambos servem.
- **Linguagem:** PT-BR neutro paulista-carioca. Evita regionalismos extremos (gauchismos, paraibismos) que perdem audiencia.
- **Datas/feriados:** carnaval + dia das maes + black friday + natal sao temporadas comerciais. Skills de social/ads citam ciclos brasileiros.

### Tropicalizacao vs traducao

- **Traducao:** verter texto US para PT-BR. Risco: importar contexto que nao se aplica (e.g., 401k retirement, GDPR-only references).
- **Tropicalizacao:** adaptar conceito para realidade BR. Substituir 401k por previdencia privada PGBL/VGBL. Substituir GDPR por LGPD com nuances ANPD.
- **Plugin frank-mkt e tropicalizado, nao traduzido.** Manutencao preserva isso.

### ASCII PT-BR sem acentos — rationale

- **Compatibilidade:** filesystem Windows + macOS + Linux + git + alguns terminais ainda apresentam edge cases com UTF-8 BOM em arquivos .md. ASCII garante portabilidade total.
- **Searchability:** ferramentas grep/ripgrep tratam acentos inconsistente. ASCII garante hits 100%.
- **Padrao do plugin:** `ascii_only: true` no frontmatter e contrato. Manutencao deve preservar.
- **Custo:** leitura levemente mais dura, mas zero ambiguidade tecnica.

**Excecoes onde acentos sao OK:** dentro de strings codigo (ex: regex match `r"^Sao Paulo$"` precisa do `~` se for matching real). Exemplos de copy real (ex: "ANUNCIE NA SEMANA DO BRASIL!") em blocos de codigo. Sempre comentar a excecao.

**Anti-pattern:** corrigir acentos sem entender o contrato. Mantenedor que rebatize tudo para PT-BR-com-acentos quebra hooks/filtros do plugin.

---

## Fundacao 7 — Paralelizacao 4 Agentes Validadas (v2.24/v2.25/v2.26/v2.27 — lessons learned)

**Conceito:** plugin frank-mkt usa paralelizacao via Task agents para criar/atualizar multiplas skills simultaneamente. Foram validadas 4 paralelizacoes em 4 releases consecutivas.

### Release v2.24.0 — Bloco Corporativo 6/6 simultaneo

- **Paralelismo:** 6 agentes simultaneos.
- **Skills criadas:** comunicacao-corporativa + employer-branding + terceiro-setor + comunicacao-crise + empreendedorismo-impacto + esg-comunicacao.
- **Tempo total:** ~25 minutos (vs ~3-4h sequencial estimado).
- **Lessons learned:**
  1. Brief prescritivo + headers literais explicitos -> ZERO retrabalho manual.
  2. Cada agente recebe 6 web searches paralelas no proprio brief -> qualidade alta consistente.
  3. Cross-skill references foram pre-mapeadas no brief -> sem necessidade de revisao manual.
  4. Frontmatter padrao no template -> sem inconsistencia entre agentes.

### Release v2.25.0 — Bloco Copy 4/4 simultaneo

- **Paralelismo:** 4 agentes simultaneos.
- **Skills criadas:** copywriting-conversao + storytelling + email-marketing + redacao-publicitaria.
- **Lessons learned:**
  1. Bloco menor = paralelismo mais facil de coordenar.
  2. Agentes que citam exemplos de copy real precisam de directive explicito sobre ASCII (caso contrario inserem acentos).
  3. Re-validacao pos-paralelizacao foi minima (5-10 min total para 4 skills).

### Release v2.26.0 — Bloco UX/UI 4/4 + Bloco Psicologia 3/3 simultaneo (recordista)

- **Paralelismo:** 7 agentes simultaneos (4 UX + 3 Psico em paralelo).
- **Skills criadas:** design-system-basico + ux-heuristicas + acessibilidade-wcag + microcopy (UX/UI) + gatilhos-eticos + prova-social-honesta + vies-cognitivo (Psicologia).
- **Lessons learned:**
  1. **Recordista de paralelismo do plugin: 7 agentes simultaneos validados.**
  2. Briefs precisam ser ainda mais especificos quando 7+ agentes (risco de overlap em exemplos / cross-references duplicadas).
  3. Memoria do mantenedor precisa pre-load de quem-faz-o-que para evitar conflitos de cross-skill.
  4. Custo token foi linear (7x), nao supra-linear. Worth it.

### Release v2.27.0 — Bloco Conhecimento 6/6 simultaneo

- **Paralelismo:** 6 agentes simultaneos.
- **Skills criadas:** conhecimento-meta-ads + conhecimento-google-ads + conhecimento-linkedin-ads + conhecimento-search-console + conhecimento-ga4 + conhecimento-conar-cdc.
- **Lessons learned:**
  1. Skills de plataforma (high volatility) precisam search templates especificos (Fundacao 3).
  2. Numeros/benchmarks paralelos podem divergir entre agentes (search results variaveis). Solucao: cross-check final pelo mantenedor.
  3. Skills regulatorias (conar-cdc) sao mais demoradas; agente pode levar 50% mais tempo. OK em paralelo, mas tracking individual ajuda.

### Patterns universais (4 paralelizacoes):

- **Brief prescritivo:** headers literais + frontmatter pronto + cross-references pre-mapeadas + estrutura obrigatoria. Sem isso, paralelismo gera inconsistencia.
- **6 web searches por agente:** mesmo padrao da Fundacao 3, executadas pelo agente no inicio do trabalho dele.
- **ZERO correcao manual quando bem instruido:** o teste-final do brief e "consigo passar isso para 6 agentes diferentes e obter resultado consistente?". Se nao, brief precisa refinamento.
- **Escalabilidade testada ate 7+ agentes simultaneos.** Acima disso ainda nao foi validado em frank-mkt — risco de context bloat no orchestrador.
- **Trackers atualizados pelo orchestrador, nao pelos agentes.** Cada agente entrega sua SKILL.md. Trackers (INDEX/CHANGELOG/plugin.json/ROADMAP) sao atualizados em commit separado pelo mantenedor para evitar race conditions.

**Anti-pattern de paralelizacao:** brief vago + sem template de frontmatter + sem cross-references pre-mapeadas. Resultado: 6 SKILL.md inconsistentes que requerem 2-3h de cleanup. Pior que sequencial.

---

## Fundacao 8 — Aplicacao em Content MKT (Maintainer + Founders + Plugin developers)

**Conceito:** esta meta-skill tem 4 audiencias claramente distintas. Aplicacao difere por persona.

### Audiencia 1: Maintainer plugin frank-mkt (Alexandre Jalkh + futuros co-mantenedores)

**Uso primario:** governance ativa do plugin.

**Aplicacao pratica:**
- Toda quarter (Q1, Q2, Q3, Q4): rodar audit de skills high-volatility (next_review proximo).
- Toda semestre: audit de medium-volatility.
- Toda ano: audit de low-volatility.
- Toda creation: seguir checklist Fundacao 4 (Estagio 1).
- Toda update: seguir checklist Fundacao 4 (Estagio 2).
- Sempre: 4 trackers sync (Fundacao 5).
- Para creation em batch: paralelizacao 4-7 agentes (Fundacao 7).

**Skill como contrato:** mantenedor pode delegar manutencao a outro humano sabendo que o framework esta documentado aqui.

### Audiencia 2: Founder usando frank-mkt como referencia

**Uso primario:** compreender o "porque" do plugin para tirar maximo proveito.

**Aplicacao pratica:**
- Entender que skills high-volatility (Meta/Google/LinkedIn Ads) precisam re-validacao trimestral. Founder nao deve confiar 100% em benchmarks de skill com last_review > 90 dias sem cross-check rapido.
- Entender que skills low-volatility (posicionamento, branding, big-idea) sao "evergreen" e podem ser usadas com confianca por 12 meses.
- Saber o tier antes de aplicar: ler frontmatter `volatility: high|medium|low`.

**Acao recomendada:** ao consultar skill high-volatility, conferir `last_review`. Se >90 dias, fazer 1 web search atual antes de aplicar recomendacao.

### Audiencia 3: Plugin developer construindo plugin similar

**Uso primario:** copiar framework de manutencao para outro plugin Claude Code.

**Aplicacao pratica:**
- Copiar estrutura de frontmatter (volatility + last_review + next_review + languages + audience + ascii_only).
- Adaptar tiers de volatility para o dominio do plugin (ex: plugin de seguranca pode ter `volatility: critical` 1m para CVEs).
- Replicar lifecycle 4-stage (Creation/Update/Deprecation/Sunset).
- Adaptar paralelizacao para o tamanho do plugin (4-7 agentes funciona para 4-6 skills por bloco; ajustar para tamanhos diferentes).

**Skill como blueprint:** outros plugins podem fork frank-mkt governance.

### Audiencia 4: Knowledge manager corporativo

**Uso primario:** aplicar o framework em wiki/Confluence/Notion corporativo, nao plugin Claude.

**Aplicacao pratica:**
- Volatility tiers se aplicam a qualquer documento corporativo (procedimento operacional medium 6m, politica low 12m, manual de produto high 3m).
- Frontmatter YAML pode ser metadata de pagina Confluence/Notion (last_verified + classification + domain — Atlan 2026 recomenda).
- Lifecycle 4-stage e o mesmo de gestao documental ISO 9001 (Creation -> Active -> Obsolete -> Archived).
- Re-validacao via pesquisa de campo equivale a "external benchmarking" em qualidade.
- Cross-skill references = hyperlinks internos com integrity check.

**Skill como ponte tech-doc:** knowledge manager corporativo le isto e leva insights para Confluence/Notion sem precisar virar plugin developer.

---

## Anti-Patterns 19

1. **Skill sem frontmatter completo.** Falta `volatility` ou `last_review` ou `next_review` -> staleness detection impossivel. Resultado: skill envelhece em silencio.

2. **Volatility classificada por "feeling" sem criterio.** Mantenedor classifica como low porque "parece estavel". Decisao deve usar Fundacao 1 com pergunta-chave + 4 indicadores.

3. **Update sem nova pesquisa.** Mantenedor edita SKILL.md mas nao roda 6 searches. Resultado: pequenas correcoes cosmeticas sem trazer dados frescos. Skill envelhece.

4. **Atualizar 1-2 trackers e esquecer outros 2-3.** plugin.json correto mas INDEX.md desatualizado. Inconsistencia confunde usuarios.

5. **Skills com `last_review` no futuro.** Erro de typo ou copy-paste. Quebra ordering de quem-precisa-revisao.

6. **Cross-skill references quebradas.** Skill A cita Skill B; Skill B foi deprecada/renomeada. Ninguem auditou. Usuario chega em link morto.

7. **Inventar URL/estatistica.** Mantenedor escreve "Meta reportou 3.5B MAUs em 2026" sem fonte. Outras pessoas citam isso. Virus.

8. **Citar tweet/post LinkedIn como fonte primaria.** OK para anedota, NAO para benchmark. Se tweet desaparece (delete user, plataforma), claim fica orfao.

9. **Acentos PT-BR mesmo com `ascii_only: true`.** Quebra contrato do plugin. Mantenedor que aceita PR sem revisar acentos prejudica grep/portabilidade.

10. **Deprecation sem coexistencia 30-90 dias.** Mantenedor deleta skill no mesmo dia que cria sucessora. Usuario que clonou plugin antes do deprecation nao tem aviso.

11. **MAJOR bump sem ser breaking.** Mantenedor pula direto v2.x -> v3.0 porque "muitas mudancas". Quebra semver convention. Outros plugins/users esperam v3 = breaking; se nao for, frustracao.

12. **PATCH bump em mudanca estrutural.** Mantenedor adiciona nova fundacao em skill existente e versiona como PATCH. Should be MINOR.

13. **Paralelizacao sem brief prescritivo.** "Crie 6 skills do Bloco X" sem template = 6 SKILL.md inconsistentes que requerem 3h de merge manual.

14. **Esquecer de atualizar memoria persistente do mantenedor.** Apos release MINOR/MAJOR, MEMORY.md deve refletir HEAD novo. Sem update, mantenedor abre nova sessao Claude Code com contexto antigo.

15. **Misturar PT-BR e EN no mesmo SKILL.md.** Frontmatter `languages: [pt-BR]` mas exemplos em EN. Quebra consistency. Excecoes (termos tecnicos sem traducao, ex: "clickbait", "engagement") sao OK; secoes inteiras em EN nao.

16. **Skill com volatility errada para o dominio.** Skill `instagram-ads` classificada como medium (6m). Errado: high (3m). Algoritmo Instagram muda mensalmente.

17. **Sunset sem migrar cross-skill references.** Skill removida; outras 5 skills citam. Resultado: 5 links mortos no plugin.

18. **Mantenedor solo eternal bottleneck.** Sem este SKILL.md documentando processo, novo co-mantenedor nao consegue contribuir. Bus factor = 1.

19. **Skills que prescrevem tecnica visual sem operacionalizar feedback visual real produzem output cego.** Aprendizado capturado em 2026-05-11 (`docs_mkt/aprendizado_infografico.md`): agente atelier-criativo entregou SVG declarando sucesso porque nunca renderizou + viu o resultado. Skill `svg-engineering-ia` previa "render-loop" como tecnica conceitual mas nao operacionalizava. Sem comando concreto + tool multimodal + Bash para fechar o loop (Write -> Bash render -> Read PNG multimodal -> Edit corrige), validacao e mental e produz falsos positivos. **Toda skill que gera artefato visual nao-trivial DEVE incluir loop de validacao operacional** (commands prontos por OS, criterios de avaliacao, stop conditions). Operacionalizado em skill `render-loop-svg` (v2.37.0). Referenciada em `svg-engineering-ia`. Replicar padrao em skills futuras que gerem imagem, audio, video, infografico.

---

## 19 Regras de Ouro

1. **Toda skill tem frontmatter YAML completo.** Sem excecoes.

2. **Volatility decisao usa Fundacao 1.** Nunca por feeling.

3. **`next_review` derivado de `last_review` + tier.** Nunca arbitrario.

4. **Re-validacao = 6 web searches paralelas.** Sempre. Mesmo para PATCH.

5. **Cross-checking 5+ fontes independentes para numeros.** Sempre.

6. **NUNCA inventar URL ou estatistica.** Quando incerto, escrever generico + datar.

7. **DATAR claims explicitamente.** "Q1/2026" envelhece graciosamente.

8. **Lifecycle 4-stage seguido a risca.** Creation -> Update -> Deprecation -> Sunset.

9. **4 trackers atualizados juntos.** INDEX + CHANGELOG + plugin.json + ROADMAP.

10. **Memoria persistente atualizada apos release MINOR/MAJOR.**

11. **Semver respeitado.** PATCH para fix, MINOR para add, MAJOR para break.

12. **Deprecation com coexistencia 30-90 dias.** Sempre aviso publico.

13. **ASCII PT-BR sem acentos preservado.** Salvo excecoes documentadas.

14. **Tropicalizacao Brasil 2026.** Cases brasileiros + LGPD-aligned + cultural codes.

15. **Paralelizacao 4-7 agentes com brief prescritivo.** Sem brief = retrabalho.

16. **Cross-skill references auditadas em creation/update.** Sem links mortos.

17. **Disclaimers educacionais em toda SKILL.md.** Plugin nao substitui consultoria juridica/financeira/medica.

18. **Bus factor > 1.** Manutencao documentada para que terceiro consiga assumir.

19. **Skills visuais incluem feedback visual operacional.** Toda skill que gera artefato visual (SVG, infografico, layout, imagem, audio renderizavel, video) DEVE incluir mecanismo de validacao por feedback real (render-loop, preview, side-by-side). Sem isso, skill produz output cego. Cristal capturado em 2026-05-11 apos sessao de teste com poster cientifico Gestuum. Skill canonica de referencia: `render-loop-svg` (commands cross-platform + criterios visuais + stop conditions).

---

## Exemplos Comportamentais

### Persona 1: Maintainer plugin frank-mkt (Alexandre, 2026-08-09)

**Cenario:** Q3/2026 quarterly audit. 6 skills high-volatility hit `next_review` simultaneamente.

**Aplicacao:**

1. Lista skills high-volatility: conhecimento-meta-ads + conhecimento-google-ads + conhecimento-linkedin-ads + conhecimento-search-console + conhecimento-ga4 + instagram-feed-reels.

2. Decide paralelizar 6 agentes simultaneos (replica do v2.27.0 pattern, Fundacao 7).

3. Brief prescritivo para cada agente:
   - Re-rodar 6 web searches no topico.
   - Diff vs SKILL.md atual.
   - Atualizar benchmarks numericos Q3/2026.
   - Atualizar `last_review: 2026-08-09`, `next_review: 2026-11-09`.
   - Adicionar entrada em CHANGELOG.md (PATCH para cada).

4. Apos 30 minutos, recebe 6 SKILL.md atualizadas.

5. Mantenedor faz cross-check final: numeros divergentes entre agentes? URLs validas? Frontmatter consistente?

6. Update trackers em commit separado:
   - INDEX.md: 6 linhas com `last_review` novo.
   - CHANGELOG.md: entrada v2.28.0 com 6 PATCHs ou 1 MINOR consolidado.
   - plugin.json: bump v2.28.0.
   - ROADMAP-FRANK-MKT.md: status Bloco Conhecimento de Plataforma "fechado, ultima revisao Q3/2026".
   - MEMORY.md: HEAD atualizado.

7. Tempo total: ~50 minutos. Sem paralelizacao seria ~5h.

### Persona 2: Founder usando frank-mkt como referencia (Marina, fundadora de SaaS B2B brasileira)

**Cenario:** Marina vai investir R$ 80k em campanha LinkedIn Ads. Consulta `conhecimento-linkedin-ads` no plugin. Skill mostra `last_review: 2026-02-09`. Hoje e 2026-08-15.

**Aplicacao:**

1. Marina ve frontmatter: `volatility: high`, `last_review: 2026-02-09` (>6 meses atras).

2. Marina aplica regra Audiencia 2 (Fundacao 8): high + >90 dias = nao confiar 100% em numeros, fazer cross-check.

3. Marina pega CTR/CPM/CPC benchmarks da skill como starting point, mas roda 1 web search rapido "LinkedIn Ads benchmarks Q2 2026 BRL B2B" para validar.

4. Web search confirma 80% dos numeros, refina 1 (CPM B2B BR subiu 12% Q2 vs Q1). Marina ajusta budget plan.

5. Marina nao culpa o plugin pela skill estar atrasada — ela usa frontmatter como sinal de "preciso validar".

### Persona 3: Plugin developer construindo plugin similar (Bruno, dev independente, plugin "frank-jur")

**Cenario:** Bruno quer construir plugin Claude Code para advogados. Estuda frank-mkt para copiar framework.

**Aplicacao:**

1. Bruno le esta skill (`manutencao-skills`) para entender a governance.

2. Bruno fork da estrutura:
   - Frontmatter padrao (volatility + last_review + next_review + languages + audience + ascii_only).
   - Lifecycle 4-stage.
   - Paralelizacao 4-7 agentes.

3. Bruno adapta tiers para dominio juridico:
   - **high (3m):** skills sobre jurisprudencia em formacao (STJ Tema X em movimento, lei recem-promulgada).
   - **medium (6m):** skills sobre praxis processual (CPC procedimentos, tribunais especificos).
   - **low (12m):** skills sobre principios constitucionais e Codigo Civil consolidado.

4. Bruno adiciona tier extra: **critical (1m)** para skills que rastreiam jurisprudencia recente do STF/STJ (mudanca diaria).

5. Bruno cita frank-mkt no README como inspiracao + cita esta skill como blueprint.

### Persona 4: Knowledge manager corporativo (Camila, KM lead em multinacional FMCG no Brasil)

**Cenario:** Camila precisa estruturar wiki Confluence de 4.500 paginas. Le esta skill via blog-post compartilhado.

**Aplicacao:**

1. Camila adapta volatility tiers para wiki corporativo:
   - **high (3m):** procedimentos operacionais sujeitos a mudanca de fornecedor + auditoria.
   - **medium (6m):** politicas de RH com guidance evolutiva.
   - **low (12m):** valores corporativos + missao + manual de marca consolidado.

2. Camila adiciona metadata Confluence em toda pagina nova:
   - `last_verified: YYYY-MM-DD`
   - `volatility: high|medium|low`
   - `owner: nome-do-steward`
   - `domain: rh|operacoes|financeiro|comunicacao`

3. Camila implementa relatorio semanal: paginas com `last_verified` > tier-cadencia entram em backlog de revisao.

4. Camila atribui knowledge stewards por dominio (Atlan 2026 recomenda) — 1 steward para cada dominio + responsabilidade clara.

5. Camila roda audit trimestral seguindo Fundacao 3 adaptada (cross-checking interno + benchmarking externo).

6. Wiki passa de "documentacao zumbi" para "living documentation" em 6 meses.

---

## Checklist Contraditorio Interno (10 perguntas)

Antes de fechar release ou publicar update, mantenedor responde 10 perguntas:

1. **Toda skill modificada teve `last_review` atualizado?** Se nao, qual ficou esquecida?

2. **Volatility classificada com Fundacao 1 ou por feeling?** Se feeling, voltar e justificar.

3. **6 web searches paralelas foram rodadas para cada skill atualizada?** Print/log existe?

4. **Numeros novos foram cross-checked em 5+ fontes?** Quais sao as 5 fontes?

5. **Cross-skill references foram auditadas?** Algum link morto?

6. **4 trackers atualizados juntos?** INDEX + CHANGELOG + plugin.json + ROADMAP — confirmar visualmente cada um.

7. **Semver bump correto?** PATCH para fix, MINOR para add, MAJOR para break — qual escolhi e por que?

8. **MEMORY.md (memoria do mantenedor) foi atualizada com HEAD novo?**

9. **ASCII PT-BR sem acentos preservado?** Algum acento escapou em PR/commit?

10. **Algum disclaimer educational ausente?** Plugin nao substitui consultoria — toda SKILL.md tem essa nota?

**Se 1+ resposta e "nao" -> nao fechar release. Voltar e corrigir.**

---

## Referencias

### Documentation lifecycle + versioning

- [Document Lifecycle Management 2026 (Technical Writer HQ)](https://technicalwriterhq.com/documentation/document-lifecycle-management/)
- [Document Lifecycle Definition Best Practices 2026 (Docsie)](https://www.docsie.io/blog/glossary/document-lifecycle/)
- [API Versioning Best Practices (Gravitee)](https://www.gravitee.io/blog/api-versioning-best-practices)
- [API Versioning Best Practices (Redocly)](https://redocly.com/blog/api-versioning-best-practices)
- [Document Version Control Best Practices (Ideagen)](https://www.ideagen.com/thought-leadership/blog/document-version-control-best-practices)
- [Software Versioning Best Practices 2026 (Moon Technolabs)](https://www.moontechnolabs.com/qanda/software-versioning-best-practices/)
- [Managing Product Lifecycle with Versioning + Sunset (Agile Seekers)](https://agileseekers.com/blog/managing-product-lifecycle-with-versioning-and-sunset-strategies)
- [Document Lifecycle with Version Control (ClickHelp)](https://clickhelp.com/clickhelp-technical-writing-blog/document-lifecycle-with-version-control-from-creation-to-archiving/)
- [Versioning Design System Best Practices (Mindful Chase)](https://www.mindfulchase.com/deep-dives/design-system-framework/versioning-your-design-system-best-practices-for-updates-and-maintenance.html)
- [Versioning Definition Examples 2026 (Docsie)](https://www.docsie.io/blog/glossary/versioning/)

### Knowledge management + freshness scoring

- [LLM Knowledge Base Freshness Scoring (Atlan)](https://atlan.com/know/llm-knowledge-base-freshness-scoring/)
- [Context Engineering Framework Enterprise AI 2026 (Atlan)](https://atlan.com/know/context-engineering-framework/)
- [LLM Knowledge Base Definition Components (Atlan)](https://atlan.com/know/what-is-an-llm-knowledge-base/)
- [The 8 Best Knowledge Management Tools 2026 (SIIT)](https://www.siit.io/blog/tools-for-knowledge-management)
- [Best Knowledge Management Software 2026 (Toolradar)](https://toolradar.com/guides/best-knowledge-management-software)
- [6 Knowledge Management Trends Redefining 2026 (Bloomfire)](https://bloomfire.com/blog/knowledge-management-trends/)
- [Key Knowledge Management Strategies 2026 (Bloomfire)](https://bloomfire.com/blog/knowledge-management-strategy/)
- [2026 Knowledge Management Predictions (APQC)](https://www.apqc.org/resources/blog/2026-knowledge-management-predictions)
- [Top KM System Features 2026 (Context Clue)](https://context-clue.com/blog/top-10-knowledge-management-system-features-in-2026/)
- [How to Integrate AI KM with Slack 2025-2026 (Question Base)](https://www.questionbase.com/resources/blog/how-to-integrate-ai-knowledge-management-with-slack-20252026-guide)

### Content audit + information architecture

- [SEO Content Audit After Core Update 2026 (Digital Applied)](https://www.digitalapplied.com/blog/seo-content-audit-after-core-update-template-2026)
- [Content Audit Ultimate Guide 2026 AI Authority (ClickRank)](https://www.clickrank.ai/content-audit/)
- [8-Step Content Auditing Framework SEO Marketing (SEOtistics)](https://seotistics.com/content-auditing-framework/)
- [Information Architecture and Content Strategy (AGUX)](https://www.agux.co/information-architecture/information-architecture-and-content-strategy-must-work-together)
- [Content Strategy 2026 What Changed (Search Engine Land)](https://searchengineland.com/guide/content-strategy-in-2026)
- [Information Architecture Audit Right (Heretto)](https://www.heretto.com/blog/get-information-architecture-right)
- [Content 101 Information Architecture (Bynder)](https://www.bynder.com/en/blog/content-101-information-architecture/)
- [Audit Your Information Architecture (Slickplan)](https://slickplan.com/blog/audit-your-information-architecture)
- [Website Content Audit 101 Learnings (Sara Wang Medium)](https://medium.com/@sarawang_39831/website-content-audit-101-68cd572f1925)
- [SharePoint Information Architecture Enterprises (i3 Solutions)](https://i3solutions.com/insights-sharepoint/sharepoint-information-architecture/)

### Semver + deprecation policy

- [Semantic Versioning 2.0.0 Spec (semver.org)](https://semver.org/)
- [Semver RC.2 Spec (semver.org)](https://semver.org/spec/v2.0.0-rc.2.html)
- [Semver Deprecation Discussion Issue 835 (GitHub)](https://github.com/semver/semver/issues/835)
- [Semver Deprecation Issue 712 Deletion Functionality (GitHub)](https://github.com/semver/semver/issues/712)
- [Semver Issue 257 Deprecation Backwards Incompatible (GitHub)](https://github.com/semver/semver/issues/257)
- [Semver Issue 983 Deprecated Obsoleted Packages (GitHub)](https://github.com/semver/semver/issues/983)
- [Semantic Versioning APIs Complete Guide SemVer (Zuplo)](https://zuplo.com/learning-center/semantic-api-versioning)
- [Pandas Policies Deprecation (Pandas docs)](https://pandas.pydata.org/docs/development/policies.html)
- [Python Semver 3.0.4 API Reference](https://python-semver.readthedocs.io/en/3.0.4/api.html)
- [Keep a Changelog](https://keepachangelog.com/)

### Prompt engineering + Claude skills

- [Anthropic Prompt Engineering Interactive Tutorial (GitHub)](https://github.com/anthropics/prompt-eng-interactive-tutorial)
- [Best Open Source Claude Code Skills 2026 Guide (BuildBetter)](https://blog.buildbetter.ai/best-open-source-skills-for-claude-code-in-2026-complete-guide/)
- [Claude API Prompt Engineering Overview](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview)
- [Claude API Prompting Best Practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- [Claude Code Handbook + Prompt Engineering Guide (GitHub)](https://github.com/ThamJiaHe/claude-prompt-engineering-guide)
- [Anthropic Prompt Engineering Course 2026 (Analytics Vidhya)](https://www.analyticsvidhya.com/blog/2024/08/anthropic-prompt-engineering-course/)
- [Master Prompt Engineering Anthropic Course (Caner Aras)](https://www.caneraras.com/learn/master-prompt-engineering-anthropic-course)
- [Anthropic Skills Guide Execution Design (Glen Rhodes)](https://glenrhodes.com/anthropic-skills-guide-formalizes-structured-execution-design-over-prompt-engineering-for-claude-agents/)
- [Anthropic Prompt Engineering Guide (AI Flow Chat)](https://aiflowchat.com/blog/articles/anthropic-prompt-engineering-guide)
- [Claude Code Best Practice Vibe to Agentic (GitHub)](https://github.com/shanraisshan/claude-code-best-practice)

### Living documentation + enterprise update cadence

- [HashiCorp Self-Managed Enterprise Release Cadence Changes 2026](https://support.hashicorp.com/hc/en-us/articles/48015293517203-Changes-to-HashiCorp-Self-Managed-Enterprise-Product-Release-Cadence-and-Support)
- [Microsoft 365 Apps Semi-Annual Enterprise Channel Changes (Topedia)](https://blog-en.topedia.com/2026/04/upcoming-changes-to-the-semi-annual-enterprise-channel-for-microsoft-365-apps/)
- [Windows 11 Release Information (Microsoft Learn)](https://learn.microsoft.com/en-us/windows/release-health/windows11-release-information)

### Brasil + LGPD + governance

- [LGPD Lei 13.709/2018 (Planalto)](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm)
- [ANPD Autoridade Nacional Protecao Dados](https://www.gov.br/anpd/pt-br)
- [CONAR Conselho Nacional de Autorregulamentacao Publicitaria](http://www.conar.org.br/)
- [Codigo de Defesa do Consumidor (Planalto)](https://www.planalto.gov.br/ccivil_03/leis/l8078compilado.htm)

### Plugin frank-mkt assets internos

- Repositorio plugin frank-mkt (alexandrejalkh/frank-mkt no GitHub)
- INDEX.md (raiz do plugin)
- CHANGELOG.md (raiz do plugin)
- .claude-plugin/plugin.json (manifest)
- docs_mkt/ROADMAP-FRANK-MKT.md (roadmap publico)

---

## Cross-Skill References

Esta meta-skill se aplica a TODAS as 77 outras skills do plugin frank-mkt. Exemplos de aplicacao por skill especifica (mapeamento volatility):

**High volatility (3m revisao) — re-validacao trimestral:**

- `conhecimento-meta-ads` — algoritmo + Advantage+ AI + iOS ATT mudam mensalmente.
- `conhecimento-google-ads` — Performance Max + Smart Bidding + Search updates.
- `conhecimento-linkedin-ads` — recente expansao para mid-market BR.
- `conhecimento-search-console` — Core Updates Google Q1/Q2/Q3/Q4.
- `conhecimento-ga4` — sampling thresholds + reports evolution.
- `instagram-feed-reels` — algoritmo Reels muda mensalmente.
- `tiktok-criativo` — formato/algoritmo evolui constantemente.
- `youtube-shorts` — monetizacao/algoritmo YPP.
- `x-twitter` — pos-Musk + features Premium + algoritmo.
- `facebook-ads` + `instagram-ads` + `linkedin-ads` (skills aplicadas vs conhecimento puro).
- `seo-tecnico` + `seo-keywords` + `seo-on-page` + `seo-link-building` + `seo-ai-otimizacao` — Core Updates + AEO + AI Overviews.

**Medium volatility (6m revisao) — re-validacao semestral:**

- `manutencao-skills` (esta skill).
- `esg-comunicacao` — guidance ANPD + CVM evolutiva.
- `comunicacao-crise` — frameworks evoluem com casos reais.
- `terceiro-setor` — MROSC + regulacao OS/OSCIP.
- `comunicacao-corporativa` — IR/Disclosure CVM + ESG.
- `employer-branding` — talent market BR + compensation trends.
- `empreendedorismo-impacto` — sistema B + impact investing BR.
- `copywriting-conversao` + `email-marketing` + `redacao-publicitaria` + `storytelling`.
- `seo-fundamentos` + `metricas-marketing`.
- `funil-jornada` + `branding`.
- `pesquisa-mercado-fundamentos` + `persona-icp-deep` + `analise-concorrencia` + `white-space-analysis` + `trendwatching` + `competitive-intelligence`.
- `dominio-vertical-fundamentos` + 11 skills `dominio-*-mkt` (TI, juridico, empreendedorismo, negocios, IA, RH, DP, financeiro, fiscal, adm, IoT).
- `tecnicas-ia-claude-gemini-mkt` — modelos evoluem trimestralmente.
- `atas-relatorios-corporativos` + `comunicacoes-corporativas`.
- `audio-musica-ia` + `geracao-imagens-ia` — modelos GenAI evoluem.
- `conhecimento-conar-cdc` — guidance CONAR + jurisprudencia CDC.

**Low volatility (12m revisao) — re-validacao anual:**

- `posicionamento-marca` — Trout/Ries + Aaker frameworks consolidados.
- `big-idea` — Ogilvy/Bernbach principios.
- `persuasao-eticas` — Cialdini 7 principios.
- `vies-cognitivo` — Kahneman/Tversky + neurociencia consolidada.
- `gatilhos-eticos` + `prova-social-honesta` — psicologia consolidada.
- `ux-heuristicas` — Nielsen 10 heuristicas (1994).
- `acessibilidade-wcag` — WCAG 2.x consolidado (atencao: WCAG 3.0 quando publicar muda para medium).
- `microcopy` — principios estaveis.
- `design-system-basico` — atomic design + tokens consolidados.
- `social-media-fundamentos` — principios estaveis (excecao: features especificas vao em high).
- `escrita-por-publico` + `multi-platform-narrative` + `conteudo-evergreen`.
- `engajamento-comunidade` + `guerrilha-criativa` + `newsjacking-real-time`.
- `infograficos-diagramas` + `composicao-visual` + `github-presence`.
- `facebook-organico` + `linkedin-organico` (organico mais estavel que ads).

**Total mapeamento:** 12+ skills high volatility, 30+ medium, 30+ low. Distribuicao reflete realidade: maioria do plugin e metodologico/principio, minoria e plataforma-especifica volatil.

---

## Integracao Ecossistema Frank-MKT

**Posicao da skill:** `manutencao-skills` e a 1a e unica skill do **Bloco Meta-skill 1/1**. **FECHA** o bloco com 1 skill.

**Por que apenas 1 skill no bloco:**

- Manutencao e tema horizontal: aplica-se a TODAS as outras skills, nao precisa fragmentar.
- Sub-skills futuras (ex: `auditoria-trimestral`, `criacao-skill-novo-bloco`, `migracao-skill-deprecada`) sao satelites desta — viveriam em outro bloco hipotetico "Operacoes plugin" ou seriam fragmentos desta.
- **Decisao arquitetural:** 1 skill densa > 5 skills fragmentadas para meta-tema.

**Bloco Meta-skill no roadmap:**

- Status: **FECHADO** em 2026-05-09.
- Skills: 1/1 (manutencao-skills).
- Posicao no plugin: 78a skill total do frank-mkt.

**Relacao com outros blocos do plugin frank-mkt:**

`manutencao-skills` e meta de TODOS os outros blocos:

1. **Bloco Mkt Fundamentos** — branding, posicionamento-marca, big-idea, etc. -> applies (Fundacao 1 mostra como classificar volatility).
2. **Bloco Social Media** — facebook, instagram, tiktok, linkedin, x-twitter, etc. -> applies (a maioria high volatility).
3. **Bloco SEO** — fundamentos, on-page, tecnico, keywords, link-building, ai-otimizacao -> applies (Core Updates trigger re-validation).
4. **Bloco Conteudo** — evergreen, multi-platform, escrita-por-publico, etc. -> applies.
5. **Bloco Visual + Audio** — composicao-visual, infograficos, audio-musica-ia, geracao-imagens-ia -> applies (modelos GenAI evoluem).
6. **Bloco Pesquisa & Inteligencia** — fundamentos, persona-icp, analise-concorrencia, white-space, trendwatching, CI -> applies.
7. **Bloco Verticais** — dominio-vertical-fundamentos + 11 dominios -> applies.
8. **Bloco Corporativo** — esg, employer-branding, terceiro-setor, comunicacao-crise, empreendedorismo-impacto, comunicacao-corporativa -> applies.
9. **Bloco Copy** — conversao, storytelling, email-marketing, redacao-publicitaria -> applies.
10. **Bloco UX/UI** — design-system, ux-heuristicas, acessibilidade-wcag, microcopy -> applies.
11. **Bloco Psicologia** — gatilhos-eticos, prova-social-honesta, vies-cognitivo -> applies (low volatility, mas re-validacao anual ainda obrigatoria).
12. **Bloco Conhecimento de Plataforma** — meta-ads, google-ads, linkedin-ads, search-console, ga4, conar-cdc -> applies (todos high volatility).
13. **Bloco Meta-skill** — esta skill propria (1/1 FECHADO).

**Resultado:** apos esta skill, mantenedor possui o "manual do dono" do plugin. Bus factor sobe de 1 para N. Plugin tem governance documentada para escalar para 100+ skills.

**Proximos passos pos-fechamento Bloco Meta-skill:**

- Aplicar Fundacao 1 e classificar volatility de TODAS as 77 skills existentes (audit inicial).
- Aplicar Fundacao 2 e auditar frontmatter de TODAS as 77 (consistencia).
- Aplicar Fundacao 5 e sincronizar 4 trackers no commit que adiciona esta skill.
- Programar Q3/2026 audit usando Fundacao 7 (paralelizacao 6 agentes).

---

## Disclaimer educational

Esta skill e material educacional sobre praticas de manutencao documental aplicadas ao plugin Claude Code frank-mkt. **Nao substitui:**

- Consultoria juridica especializada (LGPD, propriedade intelectual, contratos de uso).
- Consultoria de governanca corporativa (ISO 9001, ITIL, COBIT).
- Aconselhamento de arquitetura de informacao por profissional certificado IA/UX.
- Suporte oficial Anthropic Claude Code para questoes de plataforma.

As recomendacoes aqui refletem praticas observadas no plugin frank-mkt + frameworks publicos de Knowledge Management 2026 (Atlan, Bloomfire, APQC) + Semantic Versioning 2.0.0. Numeros e cadencias sugeridas (3m/6m/12m) sao defaults razoaveis — ajuste para o seu dominio especifico.

LGPD, CONAR, CDC e outras regulacoes brasileiras evoluem com guidance ANPD/CONAR + jurisprudencia. Quando duvida, consulte advogado especialista em privacidade/publicidade.

Plugin frank-mkt nao garante que skills mantidas conforme este framework eliminam todo risco de obsolescencia. Reduzem materialmente. Mantenedor e responsavel final pela qualidade e atualidade do conteudo.

Skill mantida por: Alexandre Jalkh + co-mantenedores futuros.
Ultima revisao: 2026-05-09.
Proxima revisao: 2026-11-09.
