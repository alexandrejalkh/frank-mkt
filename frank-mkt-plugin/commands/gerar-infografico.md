---
description: Orquestra geracao de infografico SVG denso com loop visual obrigatorio. Atelier-criativo (visao estetica) + svg-engineering-ia (markup) + renderer-visual (validacao) em cadeia explicita. Aceita brief + referencia visual opcional. Stop conditions definidas. Fallback explicito se tooling de render ausente.
argument-hint: "<brief>" [--ref=path/referencia.png] [--width=1024] [--height=1536] [--max-iter=5]
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Agent
---

# /frank-mkt:gerar-infografico

Comando wrapper que orquestra a cadeia completa para gerar **infografico SVG denso com validacao visual real**. Diferente de invocar svg-engineering-ia sozinha (gera markup mas nao valida), este comando garante render-loop obrigatorio antes de entregar.

## O que este comando faz

Cadeia de 5 etapas:

1. **Listening** — usa agente `investigador` ou pergunta direto user para extrair: tema, audiencia, dimensoes, referencia, paleta, tom.
2. **Visao estetica** — invoca agente `atelier-criativo` para definir conceito + paleta + tipografia + composicao + cross-pollination. Output: brief executavel.
3. **Markup tecnico** — invoca skill `svg-engineering-ia` para gerar SVG inicial (V1) baseado na visao do atelier.
4. **Validacao visual** — invoca agente `renderer-visual` para render-loop. Loop ate aceitar / convergir / cap 5 iteracoes.
5. **Entrega** — apresenta SVG final + PNG render + relatorio de findings + auto-critica honesta.

## Quando usar este comando

Use `/frank-mkt:gerar-infografico` quando:

1. **Infografico denso** — multiplas zonas, mini-charts, layout multi-coluna, densidade >80%
2. **Replicar referencia visual** — user tem PNG de inspiracao (Imagen, poster existente, exemplo agencia)
3. **Poster cientifico/academico** — formulas + ilustracao + grid + referencias
4. **Quer SVG editavel + escalavel + indexavel** — vs PNG raster que perde edicao
5. **Projeto comercial onde validacao visual importa** — vs entrega cega que pode ter erros invisiveis

## Quando NAO usar

NAO use este comando quando:

1. **Logo simples / wordmark** — overkill; usar atelier-criativo + svg-engineering-ia direto, sem cadeia completa
2. **Diagrama Mermaid simples** — skill `infograficos-diagramas` cobre Mermaid + PlantUML, raster eh OK
3. **Ilustracao hand-drawn organica** — SVG-via-LLM tem teto ~85% estetica; melhor caminho hibrido (Imagen via `geracao-imagens-ia` + skill `composicao-visual`)
4. **Ambiente sem tooling de render** — sem Edge/Chrome/Playwright/Resvg, comando degrada para V1 sem validacao (avisar user)
5. **Briefing puramente conceitual** — se precisa decidir IDEIA antes de execucao, usar `/frank-mkt:atelier` standalone

## Diferenca vs invocacoes separadas

| Aspecto | `/frank-mkt:atelier` | `svg-engineering-ia` direto | **`/frank-mkt:gerar-infografico`** |
|---|---|---|---|
| Foco | Visao estetica conceitual | Markup tecnico | Workflow completo end-to-end |
| Output | Proposta autoral defendida | SVG markup tecnico | SVG validado via render-loop |
| Render-loop | Nao executa | Conceitual (Fundacao 6) | **Obrigatorio** (5 iter max) |
| Cadeia | Standalone | Standalone | atelier -> svg-engineering -> renderer-visual |
| Tempo | 15-40min | 10-20min | 30-60min |
| Custo tokens | ~10-30k | ~10-20k | ~40-80k (loop adiciona) |

## Workflow detalhado das 5 etapas

### Etapa 1 — Listening (extracao de brief)

Se $ARGUMENTS vazio ou brief vago, perguntar:

1. **Tema/conteudo** — o que o infografico precisa comunicar?
2. **Audiencia** — quem le? (founder, CMO, cientista, publico geral)
3. **Dimensoes** — formato (A4 portrait 1024x1536? landscape? quadrado social 1080x1080?)
4. **Referencia visual** — tem PNG/URL de inspiracao? (--ref=path)
5. **Paleta** — definida ou livre? Extrair de referencia?
6. **Tom** — corporativo? cientifico? editorial? brasilidade tropical?
7. **Tempo/budget tokens** — projeto rapido (1-2 iter) ou critico (5 iter)?

Salvar respostas em `.frank-mkt/entregaveis/<slug>/brief.md` para versionamento.

### Etapa 2 — Visao estetica via atelier-criativo

Invocar agente atelier-criativo com brief estruturado:

```
Agent atelier-criativo:
  Brief: <tema + audiencia>
  Referencia visual: <path se fornecida>
  Dimensoes: <WxH>
  Foco: visual (cor + forma + composicao)

  Output esperado:
    - Cross-pollination (3-5 referencias cross-domain)
    - Paleta especifica (hex codes)
    - Tipografia (3 familias hierarquicas)
    - Grid (zonas + proporcoes)
    - Tensao (2-3 visoes antagonicas + escolha defendida)
    - Sintese autoral
    - Pinceis a invocar (svg-engineering-ia + companions)
```

Atelier nao gera SVG — gera **brief executavel** para svg-engineering-ia.

Salvar visao em `.frank-mkt/entregaveis/<slug>/visao-atelier.md`.

### Etapa 3 — Markup tecnico via svg-engineering-ia

Invocar skill svg-engineering-ia (via Read + aplicacao da metodologia) com visao do atelier:

- Definir viewBox + dimensoes baseado em etapa 1
- Construir em camadas (background + zonas + elementos + detalhes)
- Aplicar paleta + tipografia + grid do atelier
- Embedar elementos via `<defs>` + `<symbol>` + `<marker>` quando reuse
- Validar W3C SVG 2.0 syntax
- Output: arquivo `.frank-mkt/entregaveis/<slug>/v1.svg`

### Etapa 4 — Validacao via renderer-visual (LOOP)

Invocar agente renderer-visual em modo loop:

```
Agent renderer-visual:
  svg_path: .frank-mkt/entregaveis/<slug>/v1.svg
  output_path: .frank-mkt/entregaveis/<slug>/v1_render.png
  width: <W do brief>
  height: <H do brief>
  reference_png: <ref do brief se fornecida>
  mode: loop
  max_iterations: 5
  criteria:
    - <criterios especificos extraidos do brief>
```

Renderer-visual executa:

```
Iteracao 1:
  - Bash render via Edge headless
  - Read PNG multimodal
  - Aplicar checklist 8-dimensoes
  - Comparar vs referencia se fornecida
  - Reportar findings

Se ACEITAR -> proximo etapa
Se ITERAR -> invocar svg-engineering-ia OU atelier-criativo conforme tipo de issue:
  - Issues de markup -> svg-engineering-ia
  - Issues esteticos (visao) -> atelier-criativo (raro nesta etapa, prefere descartar)
  - Issues de tipografia -> tipografia-corporativa
  - Issues de cor -> paleta-cores-corporativa

Iteracao 2-5: idem.

Stop conditions:
  - ACEITAR alcancado
  - Convergencia (mudanca <10% em 3 iter consecutivas)
  - Cap 5 iteracoes
  - User intervention
```

### Etapa 5 — Entrega

Apresentar ao usuario:

```markdown
[/frank-mkt:gerar-infografico — resultado]

Slug: <slug>
Caminho: .frank-mkt/entregaveis/<slug>/

Arquivos:
- brief.md          — extracao do briefing
- visao-atelier.md  — visao estetica defendida do atelier-criativo
- v1.svg            — V1 inicial
- v1_render.png     — V1 renderizado
- v2.svg, v3.svg... — iteracoes (se houve loop)
- final.svg         — versao aceita
- final_render.png  — render final para preview

Metricas:
- Iteracoes ate aceitar: <N>
- Tempo total: <min>
- Tokens estimados: <K>
- Paridade vs referencia (se fornecida): <X>% comunicacional / <Y>% estetica

Auto-critica honesta:
- Surpresa: <avaliacao do atelier>
- Coerencia: <avaliacao>
- Anti-AI-slop: <avaliacao>
- Limites IA reconhecidos: <onde nao consegui chegar>

Proximos passos sugeridos:
- Validacao humana senior antes de uso comercial
- Audit WCAG formal (`acessibilidade-wcag`) se publicacao web
- Export PDF/print (Inkscape) se aplicacao impressa
- Versionamento Git do SVG final
```

## Fallback explicito quando render-loop falha

Se etapa 4 detectar AUSENCIA de tooling (Edge/Chrome/Playwright/Resvg todos indisponiveis):

```markdown
[/frank-mkt:gerar-infografico — degradacao parcial]

ATENCAO: render-loop nao pode executar neste ambiente (tooling de browser ausente).

V1 SVG foi entregue mas NAO foi validado visualmente. Limitacoes:
- Erros de coordenada / overlap / legibilidade podem estar invisiveis
- Densidade real desconhecida
- Comparacao vs referencia impossivel automaticamente

Para validar:
1. Instalar Edge (https://microsoft.com/edge — pre-instalado em Windows 11)
2. OU instalar Node + Playwright (`npm i playwright; npx playwright install chromium`)
3. OU abrir arquivo .svg no browser manualmente + revisar gaps + voltar ao comando

Status: V1 entregue como rascunho NAO validado.
```

## Argumentos

`$ARGUMENTS` formato:

```
/frank-mkt:gerar-infografico "<brief>" [--ref=path] [--width=N] [--height=N] [--max-iter=N]
```

**Brief** (mandatory): descricao do infografico em 1-3 frases.

**Flags opcionais:**

- `--ref=path` — referencia visual (PNG/URL) para replicar/inspirar
- `--width=N` — viewport horizontal (default 1024)
- `--height=N` — viewport vertical (default 1536, A4-like portrait)
- `--max-iter=N` — cap de iteracoes do render-loop (default 5)

## 4 exemplos de invocacao

### Exemplo 1 — Replicar poster cientifico

```
/frank-mkt:gerar-infografico "Replicar poster Gestuum (wearable que traduz gestos) com 8 features matematicos + DTW + distancia ponderada + grid 3D + assinatura orbital" --ref=docs/gestuum_matematica.png --width=1024 --height=1536
```

Cadeia executa:
1. Listening pula (brief detalhado + ref fornecida)
2. Atelier define paleta extraida do ref (#173A5C navy + #EA7E58 coral + #04404A teal + ...) + tipografia (Inter sans display + Cambria Math formulas + JetBrains Mono codigo) + grid 7 zonas
3. svg-engineering-ia gera v1.svg
4. renderer-visual loop ate convergir (caso real: 3 iteracoes, 85% paridade)
5. Entrega com auto-critica

### Exemplo 2 — Infografico LinkedIn weekly

```
/frank-mkt:gerar-infografico "5 tendencias B2B SaaS 2026 para CMOs brasileiros — formato carrossel LinkedIn 1080x1080" --width=1080 --height=1080 --max-iter=3
```

Cadeia:
1. Listening minimo
2. Atelier define visao (paleta corporativa + tipografia LinkedIn-friendly + grid limpo)
3. svg-engineering-ia gera SVG com 5 zonas equivalentes
4. renderer-visual valida densidade + legibilidade mobile
5. Entrega para post LinkedIn

### Exemplo 3 — Capa de relatorio investor pitch

```
/frank-mkt:gerar-infografico "Capa pitch deck Series A fintech anti-banco brasileira — visual impactante anti-AI-slop" --width=1920 --height=1080
```

Cadeia:
1. Atelier puxa cross-pollination (Caetano + manifesto antropofago + Niemeyer + Steve Jobs) — combate AI-slop firme
2. svg-engineering-ia executa SVG com tipografia bold + paleta tropical contraste
3. renderer-visual valida originalidade + impacto visual
4. Entrega capa final

### Exemplo 4 — Sem referencia, brief curto, ambiente Linux CI/CD

```
/frank-mkt:gerar-infografico "Diagrama arquitetura microservicos com 6 servicos + barramento Kafka + observability"
```

Em Linux container sem Edge:
1. Etapa 4 detecta AUSENCIA — fallback ativado
2. Sugerir install Playwright OU degradar para V1 nao-validado
3. Entrega V1 com alerta explicito

## Dependencias declaradas (transparencia para arquitetura)

Este comando depende de:

```
Comando /frank-mkt:gerar-infografico
   ↓ invoca
Agente atelier-criativo (Read, Write, Edit, Glob, Grep, WebSearch, WebFetch, Agent)
   ↓ delega
Skill svg-engineering-ia (referencia tecnica)
   ↓ markup pronto
Agente renderer-visual (Read, Write, Edit, Bash, Glob, Grep, Agent)
   ↓ executa
Skill render-loop-svg (referencia tecnica + commands)
   ↓ feedback visual
[loop iterativo]
   ↓ aceitar
Output final
```

**Single point of failure detectado:** se `renderer-visual` falhar (tooling ausente), cadeia degrada para entrega sem validacao. Documentado em fallback explicito acima.

**Cadeia de 5 nos:** mudancas em qualquer no podem afetar comando. Cobertura por:
- `manutencao-skills` (volatility tier por nó)
- Auditoria pre-mudanca obrigatoria em release MINOR/MAJOR (`frank-pentest:arquiteto`)

## Anti-patterns deste comando

1. **Pular etapa 4 (render-loop) "para economizar tokens"** — defeats the whole point. Use atelier sozinho se nao quer loop.
2. **Iterar alem do cap** — 5 iteracoes max. Apos, decidir aceitar OU descartar OU redesenhar.
3. **Aceitar sem ler PNG renderizado** — render-loop sem multimodal Read = teatro.
4. **Esconder fallback** — se tooling falta, dizer ao user honestamente.
5. **Ignorar referencia fornecida** — se user deu --ref, comparacao lado-a-lado e obrigatoria.

## Disclaimer educational

Este comando orquestra cadeia de agentes/skills mas **nao garante** infografico pronto para producao comercial. Render-loop reduz output cego (~+45 pontos de paridade documentados em sessao 2026-05-11 com poster Gestuum) mas:

- **SVG-via-LLM tem teto ~85% paridade estetica** vs Imagen-via-diffusion. Gap remanescente exige caminho hibrido (Imagen + embed) ou designer humano senior.
- **Audit WCAG formal** nao e executado por este comando — invocar `acessibilidade-wcag` antes de publicacao web.
- **Decisoes esteticas finais** sao do atelier + cliente humano. Voce pode discordar do atelier — ele acata.
- **Producao comercial com risco/budget alto** sempre acoplar revisor humano senior.

Cross-skill complementar: agentes `atelier-criativo`, `renderer-visual` + skills `svg-engineering-ia`, `render-loop-svg`, `composicao-visual`, `tipografia-corporativa`, `paleta-cores-corporativa`, `iconografia-corporativa`, `geracao-imagens-ia`, `acessibilidade-wcag`, `manutencao-skills` (cristal "skills visuais sem feedback visual = output cego").

Aprendizado raiz documentado em `docs_mkt/aprendizado_infografico.md` (commit 8c951f8, 2026-05-11).
