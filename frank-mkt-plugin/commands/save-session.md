---
description: Salva log estruturado da sessao Frank-MKT em .frank-mkt/sessoes/ — decisoes + skills invocadas + entregaveis + proximos passos
argument-hint: [titulo-sessao] (opcional)
allowed-tools: Read, Write, Bash, Glob
---

# /frank-mkt:save-session

Salva log estruturado da sessao Frank-MKT atual em `.frank-mkt/sessoes/<data>-<slug>.md`. Captura decisoes tomadas, skills invocadas, entregaveis criados e proximos passos para retomar contexto na proxima sessao.

ASCII PT-BR sem acentos (compatibilidade com Windows/encoding).

---

## O que faz

Cria arquivo `.frank-mkt/sessoes/YYYY-MM-DD-<slug-titulo>.md` contendo:

1. **Cabecalho**: data + titulo + duracao estimada + cliente
2. **Contexto**: o que foi trabalhado nesta sessao (3-8 linhas)
3. **Decisoes tomadas**: lista com rationale (por que, nao apenas o que)
4. **Skills invocadas**: lista das skills Frank-MKT utilizadas + cross-skill bridge
5. **Entregaveis**: arquivos criados/atualizados (paths absolutos)
6. **Proximos passos**: TODO list para proxima sessao
7. **Riscos / pendencias**: itens em aberto que podem virar bloqueio
8. **Decisoes adiadas**: o que foi parqueado para depois

Ao final, atualiza `.frank-mkt/decisoes/log.md` com resumo de 5-10 linhas (append-only).

---

## Argumentos

`$ARGUMENTS` = titulo da sessao (opcional, formato livre).

- Se vazio: usar `sessao-HH-MM` (hora local) como default.
- Slug: lowercase, sem acentos, espacos viram hifen, max 50 chars.

Exemplos:
- `/frank-mkt:save-session "branding cliente acme"` → `2026-05-09-branding-cliente-acme.md`
- `/frank-mkt:save-session "iteracao copy v3"` → `2026-05-09-iteracao-copy-v3.md`
- `/frank-mkt:save-session` (vazio) → `2026-05-09-sessao-14-30.md`

---

## Workflow do comando

### Passo 1 — Verificar estrutura

```bash
# Verificar se .frank-mkt/ existe (criar se nao)
mkdir -p .frank-mkt/sessoes
mkdir -p .frank-mkt/decisoes

# Se .frank-mkt/decisoes/log.md nao existe, inicializar
[ -f .frank-mkt/decisoes/log.md ] || echo "# Log de Decisoes Frank-MKT" > .frank-mkt/decisoes/log.md
```

### Passo 2 — Capturar contexto da sessao

Claude resume a conversa atual extraindo:

- **Cliente / projeto** trabalhado (se mencionado)
- **Skills Frank-MKT acionadas** (procurar referencias a `skills/<nome>/SKILL.md` ou comandos `/frank-mkt:*`)
- **Entregaveis criados** (arquivos em `entregaveis/`, `outputs/`, ou paths mencionados)
- **Decisoes estrategicas** (escolhas de posicionamento, tom de voz, canal, etc.)
- **Pendencias** (itens marcados como TODO, "depois", "validar", "iterar")

### Passo 3 — Estruturar conforme template

Aplicar o template abaixo. Preencher campos com base no contexto capturado.

### Passo 4 — Salvar arquivo

Path: `.frank-mkt/sessoes/YYYY-MM-DD-<slug>.md`

Se ja existe arquivo do dia com mesmo slug, anexar sufixo `-v2`, `-v3`, etc.

### Passo 5 — Atualizar log de decisoes

Append em `.frank-mkt/decisoes/log.md`:

```markdown
## YYYY-MM-DD — <titulo>

- Cliente: <nome> | Duracao: <X>h
- Decisoes-chave: <2-3 bullets>
- Skills: <lista resumida>
- Link sessao: ./sessoes/YYYY-MM-DD-<slug>.md
```

### Passo 6 — Reportar

Output do comando (no chat):

```
[OK] Sessao salva em: .frank-mkt/sessoes/2026-05-09-<slug>.md
[OK] Log atualizado:    .frank-mkt/decisoes/log.md

Resumo:
- <X> decisoes registradas
- <Y> skills invocadas
- <Z> entregaveis listados
- <N> itens em proximos passos

Para retomar na proxima sessao:
  /frank-mkt:resume-session 2026-05-09-<slug>
```

---

## Template do arquivo gerado

```markdown
# Sessao {{TITULO}}

**Data**: {{YYYY-MM-DD}}
**Hora inicio**: {{HH:MM}}
**Duracao estimada**: {{DURACAO}}
**Cliente / projeto**: {{NOME_CLIENTE}}
**Operador**: {{NOME_USUARIO}}

---

## Contexto

{{Resumo de 3-8 linhas do que foi trabalhado.
Inclui: objetivo da sessao, ponto de partida, escopo,
restricoes conhecidas. Sem rodeios.}}

---

## Decisoes tomadas

- **{{Decisao 1}}** — Rationale: {{por que esta escolha e nao outra}}
- **{{Decisao 2}}** — Rationale: {{...}}
- **{{Decisao 3}}** — Rationale: {{...}}

> Tag cada decisao com [REVERSIVEL] ou [IRREVERSIVEL] quando aplicavel.

---

## Skills Frank-MKT invocadas

Skills foundation:
- {{branding}} — usada para {{...}}
- {{posicionamento-marca}} — usada para {{...}}

Skills POV / estrategia:
- {{...}}

Skills tatica / canal:
- {{...}}

Skills conhecimento:
- {{...}}

> Cross-skill bridge: {{como as skills se complementaram nesta sessao}}

---

## Entregaveis criados / atualizados

Copy:
- `entregaveis/copy/{{arquivo}}.md` — {{descricao curta}}

Visual:
- `entregaveis/visual/{{arquivo}}.svg` — {{descricao}}

Estrategia:
- `entregaveis/estrategia/{{arquivo}}.md` — {{descricao}}

Outros:
- `{{path}}` — {{descricao}}

---

## Proximos passos

Curto prazo (proxima sessao):
- [ ] {{item 1}}
- [ ] {{item 2}}
- [ ] {{item 3}}

Medio prazo (1-2 semanas):
- [ ] {{item}}

Longo prazo (mes+):
- [ ] {{item}}

---

## Skills sugeridas para proxima sessao

Com base nas pendencias acima, ativar:
- `/frank-mkt:{{skill-1}}` — para resolver {{pendencia}}
- `/frank-mkt:{{skill-2}}` — para resolver {{pendencia}}

---

## Riscos / pendencias em aberto

- **{{Risco 1}}** — Impacto: {{alto/medio/baixo}} | Mitigacao: {{...}}
- **{{Pendencia 1}}** — Bloqueio: {{quem/o que estamos esperando}}

---

## Decisoes adiadas para proxima sessao

- {{Decisao parqueada 1}} — Por que adiou: {{razao}}
- {{Decisao parqueada 2}} — Por que adiou: {{razao}}

---

## Notas livres

{{Observacoes que nao se encaixam nas secoes acima.
Insights, links uteis, referencias, screenshots mencionados,
trechos de conversa relevantes.}}

---

## Disclaimer

Este log e de uso educacional e organizacional para o operador Frank-MKT.
Nao constitui contrato, nao substitui aprovacao formal de cliente,
e nao deve ser compartilhado externamente sem revisao.

Decisoes registradas aqui refletem a leitura do operador na data,
podendo ser revisadas em sessoes futuras.
```

---

## Cross-skill: o que fazer depois desta sessao

Apos salvar a sessao, considerar:

- **`/frank-mkt:resume-session`** — para retomar contexto na proxima vez (le o ultimo arquivo de `.frank-mkt/sessoes/`)
- **`/frank-mkt:status-cliente`** — agrega todas as sessoes de um cliente em painel unico
- **`/frank-mkt:export-deck`** — se a sessao gerou material apresentavel ao cliente
- **`/frank-mkt:audit-decisoes`** — revisar decisoes [IRREVERSIVEL] da semana

Skills relacionadas que podem aparecer nos proximos passos:

- `branding`, `posicionamento-marca`, `big-idea` — fundacao
- `funil-jornada`, `metricas-marketing` — ativacao + medicao
- `copywriting-conversao`, `storytelling` — execucao copy
- `composicao-visual`, `design-system-basico`, `brand-book-methodology` — execucao visual
- `analise-concorrencia`, `white-space-analysis`, `trendwatching` — pesquisa
- `manutencao-skills` — meta (atualizar skills com aprendizados)

---

## Estrutura de pastas esperada

```
projeto-cliente/
+-- .frank-mkt/
|   +-- sessoes/
|   |   +-- 2026-05-08-kickoff.md
|   |   +-- 2026-05-09-branding-cliente-acme.md
|   |   +-- 2026-05-10-iteracao-copy.md
|   |   +-- ...
|   +-- decisoes/
|   |   +-- log.md                 (append-only, resumo de cada sessao)
|   |   +-- arquivadas.md          (decisoes revertidas, com motivo)
|   +-- entregaveis-index.md       (opcional, mapa de todos entregaveis)
+-- entregaveis/
|   +-- copy/
|   +-- visual/
|   +-- estrategia/
+-- ...
```

---

## Boas praticas ao usar este comando

1. **Rodar no fim de cada sessao**, nao depois de varios dias acumulados (memoria fresca = log util).
2. **Titulo descritivo**: prefira `iteracao copy landing v3` a `sessao 12`.
3. **Decisoes com rationale**: anotar so o "o que" perde valor; o "por que" e o ouro.
4. **Tag [IRREVERSIVEL]**: marca decisoes que custam caro reverter (ex: nome de marca registrado, dominio comprado).
5. **Cross-skill bridge**: quando 2+ skills se complementaram, registre — ajuda a refinar fluxos no `manutencao-skills`.
6. **Proximos passos acionaveis**: cada item deve ter verbo + objeto. Evitar `pensar sobre X`. Preferir `definir paleta para X` ou `validar copy v3 com cliente`.
7. **Nao commitar `.frank-mkt/`** em repos de cliente sem confirmar — pode conter info sensivel. Adicionar a `.gitignore` por padrao.

---

## Casos de uso

### Caso 1 — Sessao de branding inicial

```
/frank-mkt:save-session "kickoff branding acme"
```

Log captura:
- Skills: `branding` + `posicionamento-marca` + `analise-concorrencia`
- Decisoes: arquetipo escolhido, posicionamento POV, tom de voz draft
- Entregaveis: `entregaveis/estrategia/posicionamento-v1.md`
- Proximos: validar com cliente, iterar paleta de cores

### Caso 2 — Iteracao de copy

```
/frank-mkt:save-session "copy landing v3 pos-feedback"
```

Log captura:
- Skills: `copywriting-conversao` + `gatilhos-eticos` + `microcopy`
- Decisoes: nova hierarquia de promessa, CTA reposicionado
- Entregaveis: `entregaveis/copy/landing-v3.md`
- Proximos: A/B test setup, definir metrica primaria

### Caso 3 — Pesquisa de mercado

```
/frank-mkt:save-session "white space analysis vertical juridica"
```

Log captura:
- Skills: `pesquisa-mercado-fundamentos` + `white-space-analysis` + `trendwatching`
- Decisoes: 3 angulos nao explorados pela concorrencia
- Entregaveis: `entregaveis/estrategia/white-space-juridico.md`
- Proximos: validar hipotese com 5 entrevistas

---

## Limitacoes

- Nao substitui CRM ou project management formal.
- Nao captura automaticamente arquivos modificados fora do diretorio do projeto.
- Resumo da sessao depende da janela de contexto disponivel do Claude — sessoes muito longas podem ter detalhes omitidos.
- Sem integracao automatica com Notion/Linear/Jira (rodar export manual se necessario).

---

## Disclaimer educational

Este comando e parte do plugin Frank-MKT e tem proposito educacional + organizacional.

O log gerado e do operador, para o operador. Decisoes estrategicas de marketing
devem sempre passar por validacao com cliente antes de execucao em producao.

Frank-MKT nao substitui:
- Aprovacao formal de marca pelo cliente
- Revisao juridica (CONAR, CDC, LGPD) antes de publicar
- Validacao de claims com area tecnica/produto
- Briefing assinado quando aplicavel

Ao salvar uma sessao, voce esta documentando seu raciocinio — nao
emitindo um documento contratual. Use com criterio.

---

**Versao**: v1.0.0
**Skill relacionada**: `manutencao-skills` (para refinar fluxo apos N sessoes)
**Plugin**: frank-mkt
