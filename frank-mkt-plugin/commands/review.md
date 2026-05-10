---
description: Review qualitativo de campanha/peca MKT — analise critica + contraditorio + sugestoes via multiplos agentes especialistas
argument-hint: <caminho-arquivo> [foco-area] (ex: "entregaveis/decks/pitch-v2.pptx" "narrativa")
allowed-tools: Read, Glob, Grep
---

# /frank-mkt:review

Review **qualitativo** de uma campanha, peca ou entregavel de marketing.
Analise critica subjetiva com julgamento, contraditorio entre agentes e
sugestoes priorizadas de melhoria.

> Disclaimer educacional: as analises geradas por este comando refletem
> opinioes profissionais aplicadas dos agentes especialistas, nao garantias
> de performance. Use como insumo para decisao, nao como veredito final.
> Validacao com cliente, A/B test ou metricas de mercado segue essencial.

---

## O que faz

Analise qualitativa profunda em 4 camadas, com **multiplos agentes
especialistas** invocados em paralelo + **arbitragem de divergencias**:

1. **Frank-MKT principal** revisa narrativa + estrategia geral
2. **Agente especialista** (auto-selecionado pelo tipo de peca) revisa
   execucao tecnica
3. **Juiz** arbitra qualquer divergencia entre as 2 analises acima
4. Reporta analise consolidada com recomendacoes priorizadas

Diferente de `/frank-mkt:audit`, que e um gate **mecanico PASS/FAIL**,
este comando produz **julgamento qualitativo** com sugestoes de iteracao.

---

## Diferenca vs `/frank-mkt:audit`

| Aspecto       | `/frank-mkt:audit`         | `/frank-mkt:review`              |
|---------------|----------------------------|----------------------------------|
| Natureza      | Mecanico PASS/FAIL         | Qualitativo subjetivo            |
| Tempo         | Rapido (5-10 min)          | Profundo (15-30 min)             |
| Quando usar   | Antes de entregar (gate)   | Iteracao + refinamento           |
| Output        | Lista violacoes + score    | Analise critica + sugestoes      |
| Custo tokens  | Baixo                      | Medio-Alto (multi-agente)        |
| Substituivel  | Nao — gate obrigatorio     | Nao — julgamento humano-like     |

**Regra pratica**: rode `/frank-mkt:review` durante criacao para iterar;
rode `/frank-mkt:audit` antes de enviar ao cliente para validar.

---

## Quando usar

- Iteracao de copy/landing antes de A/B test
- Revisao de deck pre-pitch (Series A, B, IPO)
- Validacao de post social antes de publicar
- Analise critica de briefing recebido (gaps de pesquisa)
- Plano de midia antes de aprovacao de orcamento
- Re-review pos-correcoes recomendadas em sessao anterior

---

## Quando NAO usar

- Validacao mecanica anti-LGPD/CONAR/OAB → use `/frank-mkt:audit`
- Smoke test rapido pre-commit → use `/frank-mkt:audit`
- Geracao de novo conteudo → use skills especificas
- Diagnostico de marca (estado geral do projeto) → use `/frank-mkt:stack`

---

## Argumentos

`$ARGUMENTS` recebe ate 2 valores posicionais:

1. **caminho-arquivo** (obrigatorio): caminho relativo ao CWD ou absoluto
   - Ex: `entregaveis/decks/pitch-v2.pptx`
   - Ex: `entregaveis/copy/landing-home-v3.md`
   - Ex: `D:\4nk\cliente-x\.frank-mkt\campanhas\black-friday\briefing.md`
2. **foco-area** (opcional): direciona profundidade da analise
   - Valores: `narrativa` | `persuasao` | `visual` | `tecnico` |
     `compliance` | `posicionamento` | `tom` | `geral` (default)

Se foco nao for especificado, o comando faz analise full em todas as
dimensoes aplicaveis ao tipo de peca detectado.

---

## Tipos de peca + agentes selecionados

A selecao de agentes e automatica por extensao + heuristica de conteudo.

### Copy / Landing Page

Detectado por: `*.md` em `entregaveis/copy/`, `*.html`, `landing-*.md`.

- **Frank-MKT (principal)**: narrativa + posicionamento + tom + clarity
- **redator-hacker**: persuasao etica + frameworks (AIDA, PAS, BAB) +
  power words + headline fitness
- **psicologia-influencia**: gatilhos + dark patterns + vieses
  (cross-skill: `gatilhos-eticos` + `vies-cognitivo`)
- **seo-strategist** (se landing publica): keywords + meta + estrutura H

### Post Social

Detectado por: `entregaveis/social/`, `post-*.md`, frontmatter
`platform: linkedin|instagram|facebook|tiktok|x`.

- **Frank-MKT (principal)**: alinhamento com marca + tom de voz
- **social-media-{linkedin|instagram|facebook|tiktok|x}**: best practices
  da plataforma (formato, CTAs, hashtags, hook 3 segundos)
- **psicologia-influencia**: engajamento etico + algoritmo-friendly

### Deck / Apresentacao

Detectado por: `*.pptx`, `*.key`, `*.pdf` em `entregaveis/decks/`,
`pitch-*`, `deck-*`.

- **Frank-MKT (principal)**: storytelling + narrativa + arco
- **frank-corporativo** (se enterprise/B2B/SaaS): tom institucional +
  credibilidade
- **ux-ui-revisor**: hierarquia visual + acessibilidade + contraste +
  densidade de informacao por slide

### Briefing

Detectado por: `briefing*.md`, `kickoff*.md`, `.frank-mkt/cliente.md`.

- **Frank-MKT (principal)**: objetivos + escopo + KPIs claros
- **perfilador-mercado**: persona descrita + insight de mercado + ICP fit
- **investigador**: gaps de pesquisa + premissas nao validadas

### Plano de Midia

Detectado por: `plano-midia*.md`, `media-plan*`, frontmatter
`type: media-plan`.

- **Frank-MKT (principal)**: estrategia geral + alinhamento funil
- **seo-strategist**: organico (SEO, content, link building)
- **social-media-***: ads paid por plataforma + budget split + LTV/CAC

### Naming / Tagline / Slogan

Detectado por: `naming-*.md`, `tagline-*.md`, frontmatter
`type: naming|tagline`.

- **Frank-MKT (principal)**: alinhamento marca + memorabilidade
- **redator-hacker**: ressonancia + ritmo + aliteracao
- **brand-archetype**: fit com arquetipo definido em `marca/identidade.md`

### Email / Newsletter

Detectado por: `entregaveis/email/`, `newsletter-*.md`.

- **Frank-MKT (principal)**: jornada + segmentacao
- **redator-hacker**: subject line + preview + CTA
- **email-deliverability** (cross-skill): spam triggers + reputation

---

## Foco-area (modificador)

Quando o usuario passa um foco, o comando **prioriza** os agentes
relevantes e **suprime** os menos relacionados.

| Foco           | Agentes priorizados                                    |
|----------------|--------------------------------------------------------|
| narrativa      | Frank-MKT + storytelling + brand-archetype             |
| persuasao      | redator-hacker + psicologia-influencia                 |
| visual         | ux-ui-revisor + design-system + acessibilidade         |
| tecnico        | seo-strategist + social-media-* + email-deliverability |
| compliance     | frank-juridico + LGPD + CONAR + OAB                    |
| posicionamento | Frank-MKT + perfilador-mercado + brand-archetype       |
| tom            | Frank-MKT + voice-tone-keeper                          |
| geral (default)| todos os aplicaveis ao tipo                            |

> Nota: `compliance` em `/frank-mkt:review` NAO substitui
> `/frank-mkt:audit`. E uma analise qualitativa de risco, nao um gate.

---

## Workflow interno

```
1. Parse $ARGUMENTS
   ├─ caminho-arquivo (obrigatorio)
   └─ foco-area (opcional, default: geral)

2. Validar arquivo
   ├─ Read do arquivo
   ├─ Detectar extensao + frontmatter + heuristica
   └─ Classificar tipo de peca

3. Carregar contexto .frank-mkt/
   ├─ marca/identidade.md (archetype, posicionamento)
   ├─ marca/voice-tone.md (voz, tom)
   ├─ persona/icp.md (publico-alvo)
   └─ campanhas/{ativa}/briefing.md (se peca pertence a campanha)

4. Selecionar agentes
   ├─ Sempre: Frank-MKT principal
   ├─ Especialista por tipo (tabela acima)
   └─ Filtrar por foco-area se passado

5. Invocar agentes (paralelo logico)
   ├─ Cada agente recebe: peca + contexto marca + foco
   └─ Cada agente retorna: pontos fortes + atencao + sugestoes

6. Detectar divergencias
   ├─ Comparar recomendacoes contraditorias entre agentes
   └─ Se houver, invocar Juiz para arbitrar

7. Sintetizar
   ├─ Consolidar pontos fortes (sem duplicar)
   ├─ Consolidar pontos de atencao
   ├─ Priorizar sugestoes (CRITICO | ALTO | MEDIO | BAIXO)
   └─ Cross-skill references (skills citadas para corrigir)

8. Reportar (formato abaixo)
```

---

## Output formato

```
=== FRANK-MKT REVIEW QUALITATIVO ===
Peca: entregaveis/decks/pitch-v2.pptx
Tipo: Pitch Deck Series A
Foco: narrativa
Data: {{YYYY-MM-DD}}
Agentes invocados: Frank-MKT, frank-corporativo, ux-ui-revisor

---

[FRANK-MKT principal — Narrativa + Estrategia]

Pontos fortes:
- Big idea clara e ressoante: "infraestrutura de confianca para juridico"
- Storytelling segue Sequoia 10 slides com fidelidade
- Slide 3 (Problem) traz numero forte: "82% dos escritorios perdem prazo"

Pontos de atencao:
- Slide 4 (Why Now) fraco — falta urgencia objetiva (regulacao, timing)
- Slide 7 (Competition) desatualizado vs Magic Quadrant 2026
- Transicao slide 8 → 9 quebra arco emocional

Sugestoes:
- Slide 4: adicionar tres datadores ("LGPD 2020, CNJ 2024, IA 2026")
- Slide 7: substituir grid por matriz 2x2 (X: precco, Y: especializacao)
- Slide 8 → 9: adicionar bridge "e por isso que..."

---

[frank-corporativo — Tom institucional]

Pontos fortes:
- Tom equilibrado entre confianca e ambicao
- Logos de clientes enterprise bem posicionados (slide 6)

Pontos de atencao:
- Slide 12 (Team) mistura tom institucional com tom startup
- Linguagem de "disrupcao" em audiencia Series A pode soar imatura

Sugestoes:
- Slide 12: padronizar bios em formato "Nome — Cargo — 1 conquista"
- Substituir "disrupcao" por "transformacao" ou "evolucao categorica"

---

[ux-ui-revisor — Hierarquia visual]

Pontos fortes:
- Paleta consistente com brand guidelines
- Tipografia hierarquica (H1/H2/body) bem aplicada

Pontos de atencao:
- Slide 5 (Solution): densidade de texto excessiva (>180 palavras)
- Contraste insuficiente em legendas de grafico (slide 3)
- Falta de breathing room em slide 9 (Traction)

Sugestoes:
- Slide 5: cortar 50% do texto, mover detalhes para anexo
- Slide 3: aumentar contraste de #888 para #444 ou mais escuro
- Slide 9: aplicar grid 12 colunas com gutter

---

[Juiz — Divergencias arbitradas]

Divergencia 1:
- Frank-MKT sugere reduzir slide 7 (competition) — "ja e foco em slide 5"
- frank-corporativo sugere expandir slide 7 — "audiencia enterprise valoriza"
→ Juiz decide: REDUZIR + mover detalhe para apendice
  Justificativa: Frank-MKT principal tem precedencia em decisoes
  estrategicas de narrativa; preocupacao do frank-corporativo e atendida
  via apendice acessivel sem quebrar arco.

Divergencia 2:
- (nenhuma outra detectada)

---

[Recomendacoes priorizadas]

1. CRITICO
   - Corrigir scarcity falsa no slide pricing (se houver)
     cross-skill: gatilhos-eticos (anti-pattern #5)
   - Atualizar Magic Quadrant slide 7 (dado errado mata credibilidade)

2. ALTO
   - Reescrever slide 4 (Why Now) com tres datadores objetivos
     cross-skill: storytelling (framework "Why Now")
   - Slide 5: cortar 50% do texto + mover para apendice
     cross-skill: ux-ui-revisor (regra densidade)

3. MEDIO
   - Padronizar bios slide 12 (formato Nome — Cargo — Conquista)
   - Substituir "disrupcao" por "transformacao" (slide 1 e 12)
   - Aumentar contraste legendas slide 3

4. BAIXO
   - Melhorar bridges entre slides 8 → 9
   - Aplicar grid 12 colunas slide 9

---

[Proximos passos sugeridos]

- Iterar peca aplicando correcoes 1-3 (CRITICO + ALTO + MEDIO)
- Re-review pos-correcao: `/frank-mkt:review entregaveis/decks/pitch-v3.pptx narrativa`
- Audit final pre-entrega: `/frank-mkt:audit entregaveis/decks/pitch-v3.pptx`
- Validar narrativa com 2-3 advisors antes do D-day

---

[Cross-skill references]

Skills citadas neste review:
- gatilhos-eticos (anti-pattern #5 scarcity)
- storytelling (framework Why Now)
- ux-ui-revisor (regra densidade)
- vies-cognitivo (autoridade vs. autoridade falsa)

Para aprofundar correcoes especificas, ative as skills citadas.

=== FIM REVIEW ===
```

---

## Comportamento por tipo de peca (resumo)

### Copy / Landing
Foco em **conversao + clareza + persuasao etica**. Avalia headline,
sub-headline, hierarquia de beneficios, prova social, CTA, friction.

### Post Social
Foco em **hook 3 segundos + algoritmo + tom de marca**. Avalia primeira
linha, formato (carrossel/single/video), hashtags, CTA contextual.

### Deck
Foco em **arco narrativo + densidade + credibilidade**. Avalia
storytelling (problema → solucao → traction → ask), densidade por slide,
visual hierarchy, transicoes.

### Briefing
Foco em **clareza de objetivos + ICP definido + KPIs mensuraveis**.
Avalia gaps de pesquisa, premissas nao validadas, escopo nebuloso.

### Plano de Midia
Foco em **alinhamento funil + budget split + KPIs por canal**. Avalia
TOFU/MOFU/BOFU coverage, LTV/CAC, organic vs paid balance.

### Naming / Tagline
Foco em **memorabilidade + ressonancia + fit arquetipo**. Avalia ritmo,
aliteracao, distinctividade, alinhamento com identidade.

### Email
Foco em **subject + preview + CTA + deliverability**. Avalia open rate
potential, spam triggers, segmentacao, jornada.

---

## Multi-agent invocation pattern

Este comando segue o padrao **fan-out + judge** do frank-mkt:

```
                    [Frank-MKT principal]
                            |
              fan-out → [especialista 1]
                        [especialista 2]
                        [especialista N]
                            |
              divergencia? → [Juiz arbitra]
                            |
                    [Sintese final]
```

- **Fan-out paralelo**: cada agente analisa a peca independentemente,
  sem ver output dos outros (evita anchoring bias entre agentes).
- **Juiz**: invocado SOMENTE se houver recomendacoes contraditorias.
  Justifica decisao com criterio explicito (quem tem precedencia, em
  que dimensao).
- **Sintese**: consolida sem duplicar, prioriza por impacto x esforco.

---

## Cross-skill references

Reviews **sempre** citam skills relevantes para correcoes especificas.
Isso permite que o usuario aprofunde sem precisar relembrar quais skills
existem. Exemplos:

- "scarcity falsa" → cita `gatilhos-eticos`
- "headline fraco" → cita `redator-hacker`
- "densidade excessiva" → cita `ux-ui-revisor`
- "tom inconsistente" → cita `voice-tone-keeper`
- "premissa nao validada" → cita `investigador`
- "ICP vago" → cita `perfilador-mercado`

---

## Limitacoes conhecidas

- **PPTX/Key**: leitura limitada — extrai texto, nao layout exato.
  Para review visual completo, complementar com screenshot ou export PDF.
- **Imagens em landing**: nao analisa imagens diretamente — avalia alt
  text e contexto.
- **A/B test prediction**: review e qualitativo, nao prediz CTR. Para
  decisao final, rodar A/B real ou usar `/frank-mkt:audit`.
- **Cliente-especifico**: depende de `.frank-mkt/marca/` e
  `.frank-mkt/persona/` estarem preenchidos para contexto.
  Se vazios, review fica generico.

---

## Erros comuns

| Erro                                  | Causa provavel                       | Solucao                              |
|---------------------------------------|--------------------------------------|--------------------------------------|
| "Tipo de peca nao detectado"          | Extensao + frontmatter ambiguos      | Adicionar `type:` no frontmatter     |
| "Contexto de marca insuficiente"      | `.frank-mkt/marca/` vazio            | Rodar `/frank-mkt:init` antes        |
| "Review generico, sem profundidade"   | Falta foco-area + arquivo curto      | Passar foco-area como 2o argumento   |
| "Divergencias nao resolvidas"         | Juiz nao foi invocado                | Verificar logs — bug, reportar       |

---

## Exemplos de uso

```bash
# Review completo de pitch deck
/frank-mkt:review entregaveis/decks/pitch-v2.pptx

# Review focado em narrativa
/frank-mkt:review entregaveis/decks/pitch-v2.pptx narrativa

# Review de landing focado em persuasao
/frank-mkt:review entregaveis/copy/landing-home.md persuasao

# Review de post LinkedIn
/frank-mkt:review entregaveis/social/post-linkedin-launch.md

# Review de briefing recebido
/frank-mkt:review .frank-mkt/cliente.md geral

# Review de plano de midia focado em compliance
/frank-mkt:review entregaveis/midia/plano-q2-2026.md compliance
```

---

## Integracao com outros comandos

Sequencia recomendada para uma peca nova:

```
1. Criar peca (skill especifica)
        |
        v
2. /frank-mkt:review <peca>           ← analise qualitativa, iterar
        |
        v
3. Iterar peca (aplicar sugestoes)
        |
        v
4. /frank-mkt:review <peca-v2>        ← re-review pos correcoes
        |
        v
5. /frank-mkt:audit <peca-v2>         ← gate mecanico final
        |
        v
6. Entregar ao cliente
```

---

## Notas finais

- **Nao e veredito**: review e opiniao tecnica aplicada, nao garantia.
- **Iterativo**: rode multiplas vezes ao longo da criacao.
- **Multi-agente**: forca contraditorio explicito, evita pensamento unico.
- **Cross-skill**: integra com ecossistema 92 skills do frank-mkt.
- **Disclaimer**: validar com cliente, A/B test ou metricas de mercado.

> Para auditoria mecanica PASS/FAIL → use `/frank-mkt:audit`.
> Para snapshot do projeto → use `/frank-mkt:stack`.
> Para inicializar projeto → use `/frank-mkt:init`.
