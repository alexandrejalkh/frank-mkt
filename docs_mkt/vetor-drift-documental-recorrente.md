# Vetor: Drift Documental Recorrente em Plugin Markdown Agentic

> **Audiencia primaria**: `frank-pentest` -- absorver como novo vetor de auditoria ou expansao do vetor #6 (drift de protocolo) + #15 (cross-Markdown drift) + #18 (aspirational design).
>
> **Audiencia secundaria**: arquitetos de plugins Claude Code (ou similares) que mantem N artefatos correlatos com metadados duplicados.
>
> **Status**: documento descritivo + reprodutivel + actionable. Escrito apos 5 ciclos consecutivos de drift documental detectados em uma sessao de 2026-05-11, com 8 releases publicadas.

---

## Sumario Executivo

Em uma sessao de trabalho de ~6 horas, ao evoluir o plugin **frank-mkt** (Claude Code, 93 skills + 10 commands + 16 agentes = 119 artefatos Markdown) de v2.35.0 para v2.39.2, foram detectados **5 ciclos consecutivos de drift documental** entre arquivos correlatos. O padrao foi mecanicamente identico em todos os ciclos:

1. Implementacao de feature nova (ou correcao de bug).
2. Bump de versao em apenas alguns dos arquivos correlatos com metadados duplicados (`plugin.json`, `marketplace.json`, `INDEX.md`, `help.md`, `INSTALACAO.md`, `ROADMAP.md`, `agents/README.md`, `agents/frank-mkt.md`, `README.md` raiz).
3. Auditoria pos-release pelo `frank-pentest:lost-in-middle` detecta drift.
4. Patch de correcao criado.
5. **Proxima release introduz drift novo**, frequentemente em arquivos *diferentes* dos corrigidos antes.

O padrao se repetiu mesmo apos:
- Documentar o problema em CHANGELOG.
- Salvar como memory persistente (`feedback_remote_check_critico.md`, `feedback_audit_pre_mudanca.md`).
- Implementar CI lint cross-artifact dedicado em v2.39.0.

A v2.39.0 (a release que adicionou o lint anti-drift) **introduziu drift que o proprio lint nao detectava** -- meta-ironia que validou empiricamente que **disciplina humana + memory + checklist nao previnem esse vetor**. Apenas validacao mecanica automatizada com cobertura abrangente o faz, e mesmo essa precisa de auto-testes para prevenir bugs no proprio validador.

**Tese central**: drift documental cross-artifact em plugins Markdown agentic e **endemico estrutural**, nao um bug a corrigir uma vez. Requer infraestrutura de validacao continua + testes do validador + cobertura iterativamente expandida conforme novos padroes de drift sao detectados em producao.

---

## 1. Contexto: O Plugin

**frank-mkt** e um plugin Claude Code que entrega consultoria de Marketing/SEO/Midias Sociais/Inteligencia de Mercado para o mercado brasileiro 2026. Em v2.39.2 (estado final da sessao):

- **93 skills** distribuidas em 19 blocos tematicos
- **10 slash commands** (init, stack, save-session, help, audit, review, juiz, perfil, atelier, gerar-infografico)
- **16 agentes** especialistas (incluindo atelier-criativo, renderer-visual)
- **1 hook** SessionStart
- **CI lint cross-artifact** + **suite de 7 testes unitarios**

**Volume documental**: ~121.000 linhas Markdown distribuidas entre os 119 artefatos. Cada artefato tem frontmatter YAML + corpo. Metadados duplicados (contagens totais, versao, descricoes) aparecem em **9 arquivos correlatos**:

```
.claude-plugin/marketplace.json (raiz)
README.md (raiz)
docs_mkt/INSTALACAO.md
docs_mkt/ROADMAP-FRANK-MKT.md
frank-mkt-plugin/.claude-plugin/plugin.json
frank-mkt-plugin/CHANGELOG.md
frank-mkt-plugin/agents/README.md
frank-mkt-plugin/agents/frank-mkt.md (persona principal)
frank-mkt-plugin/skills/INDEX.md
frank-mkt-plugin/commands/help.md
```

**Cada release com adicao de artefato exige atualizacao manual em 9 lugares**. Esse e o nucleo do problema.

---

## 2. Anatomia do Vetor de Drift

### 2.1. Definicao formal

**Drift documental cross-artifact**: divergencia entre declaracoes do mesmo metadado em arquivos correlatos do mesmo projeto, originada de atualizacao parcial durante uma operacao que afeta N arquivos.

**Tipos detectados na sessao**:

| Tipo | Exemplo concreto |
|---|---|
| **Drift de versao** | `plugin.json: "2.37.0"` mas `INSTALACAO.md: "v2.36.0"` |
| **Drift de contagem** | `INDEX.md: "92 skills"` mas filesystem tem 93 skills |
| **Auto-contradicao mid-file** | `help.md:19 "9 commands"` + `help.md:42 "8 commands"` (mesmo arquivo!) |
| **Drift narrativo** | `marketplace.json: "v2.39.0 adiciona X"` em release v2.39.1 (deveria narrar v2.39.1) |
| **Drift de soma** | `INDEX.md: "61 medium + 24 high + 7 low" = 92` mas total declara 93 |
| **Drift entre ground truth e declaracao** | `help.md: "18 blocos"` mas headers `### Bloco 1` a `### Bloco 19` |
| **Drift hardcoded em texto historico** | `INDEX.md: "MILESTONE 17 BLOCOS COMPLETOS"` (texto v2.28.0 nao atualizado) |
| **Drift em subsection header congelado** | `INDEX.md:41 "## Agentes (16/16 — v2.37.0)"` enquanto plugin esta v2.39.0 |
| **Drift em celula de tabela** | `INDEX.md tabela: "orquestra 93 skills + 15 agentes"` mas tem 16 agentes |

### 2.2. Por que arquivos Markdown sao especialmente vulneraveis

Drift cross-artifact e classico em qualquer codebase com metadados duplicados. Mas plugins Markdown agentic tem caracteristicas que **amplificam** o vetor:

1. **Sem compiler estatico**: codigo em Python/TypeScript/Go quebra em build se contagens divergirem (constante hardcoded vs import vs valor calculado). Markdown nunca "quebra" -- so fica errado em runtime ou para o leitor humano.

2. **Sem assertions runtime**: ao contrario de codigo, Markdown nao tem assertions que falham quando metadados batem invariantes.

3. **N >= 7 arquivos correlatos**: quanto maior N, maior probabilidade combinatoria de esquecer ao menos um arquivo em update.

4. **Convencao de redundancia documental**: plugins Claude Code seguem padroes onde mesmo metadado aparece em README + INDEX + help + frontmatter de agente principal + plugin.json. Redundancia e proposital (cada doc serve um leitor), mas vira passivo de manutencao.

5. **Persona principal carrega contagens**: no frank-mkt, `agents/frank-mkt.md` (persona principal carregada toda interacao) declara "X agentes + Y skills + Z commands" no proprio system prompt. Drift aqui afeta runtime comportamento do agente.

6. **Texto historico em arquivos vivos**: `INDEX.md` mantem "MILESTONE 17 BLOCOS COMPLETOS" como texto historico de v2.28.0 misturado com declaracoes de estado atual. Leitor casual nao distingue passado de presente.

7. **Auto-contradicao mid-file invisivel a humano**: `help.md` declarando "9 commands" no workflow (linha 19) e "8 commands" no heading (linha 42) e literalmente invisivel para revisao humana acima de ~50 linhas de distancia. Auditor tem que estar olhando o arquivo inteiro com regex.

### 2.3. Por que disciplina humana falha

Tres razoes empiricamente validadas na sessao:

1. **Memory cap**: humano (ou LLM) tem capacidade limitada de tracking simultaneo. Um release que toca 9 arquivos correlatos excede o working memory tipico. Mesmo com checklist, pulamos itens.

2. **False confidence apos correcao parcial**: apos corrigir 7 de 9 arquivos, sensacao de "feito" sobrepora a verificacao dos 2 restantes. Cada ciclo da sessao tinha esse padrao.

3. **Drift acumulativo entre sessoes**: o frank-mkt evoluiu de v0.5.0 a v2.39.2 em ~30 versoes. Cada versao herdou drift residual da anterior. Em v2.32.0, ja havia drift acumulado de v0.5.0->v2.30.0 que ninguem notava. Quando v2.36.0 reparou o drift de v2.32->v2.35, varios drifts mais antigos foram tambem corrigidos sem que ninguem soubesse que estavam la.

---

## 3. Os 5 Ciclos Consecutivos (Cronologia Detalhada)

### Ciclo 1: v2.32.0 -> v2.35.0 (drift acumulativo nao-detectado)

**O que aconteceu**: o plugin chegou a v2.35.0 com 3 releases consecutivas (v2.33, v2.34, v2.35) que adicionaram agentes/commands/docs sem atualizar TODOS os arquivos correlatos. Drift acumulou silencioso.

**Quando detectado**: auditoria `frank-pentest:lost-in-middle` no inicio da sessao 2026-05-11, antes de qualquer mudanca nova. Auditoria foi feita porque user pediu para avaliar mudancas propostas em outro doc (`aprendizado_infografico.md`) -- nao para detectar drift.

**Drifts encontrados (7 HIGH + 3 MEDIUM)**:

| Arquivo | Linha | Drift |
|---|---|---|
| `CHANGELOG.md` | top | Parou em v2.32.0 (faltam entradas v2.33/v2.34/v2.35) |
| `INDEX.md` | 5,37 | "v2.32.0 -- 114 artefatos" mas plugin.json declara v2.35.0 |
| `help.md` | 38 | Hardcoded "v2.21.0" (14 versoes atrasadas!) |
| `help.md` | 19,42 | Auto-contradicao "9 commands" + "8 commands" no mesmo arquivo |
| `agents/frank-mkt.md` | 3,14 | Persona principal diz "13 agentes + 8 commands" (real 15+9) |
| `marketplace.json` | 13 | Plugin entry description "8 commands + 14 agentes = 114 artefatos" |
| `INSTALACAO.md` | 66,67,162 | "14 agentes / 9 commands / v2.32.0" |
| `ROADMAP.md` | 6 | "v0.5.0 / 58 skills previstas" (30 versoes atrasadas) |

**Como resolvido**: release v2.36.0 ("DRIFT REPAIR") sincronizou 8 arquivos. Commit unico, sem mudanca em runtime. Tag `v2.35.0-pre-drift-fix` criada como restore point.

**Custo**: 8 arquivos modificados, +169 linhas / -43 linhas.

### Ciclo 2: v2.36.0 -> v2.37.0 (drift introduzido por feature nova)

**O que aconteceu**: v2.37.0 adicionou feature substancial (render-loop visual SVG) com 3 novos artefatos: skill `render-loop-svg` (1065 linhas) + agente `renderer-visual` (296 linhas) + command `/frank-mkt:gerar-infografico` (320 linhas). Total +1816 linhas.

**Quando detectado**: auditoria pos-release com 4 agentes (`lost-in-middle`, `arquiteto`, `source-auditor`, `guardian`). Lost-in-middle reportou: *"Repetimos o erro"*.

**Drifts encontrados (7 NOVOS, mesmo padrao classe que v2.32->v2.35)**:

1. `INSTALACAO.md` ficou em v2.36.0 (esquecido no bump v2.37.0)
2. `ROADMAP.md` ficou em v2.36.0
3. `INDEX.md` L33: TOTAL SKILLS 92/92 + 107.548 linhas (auto-contradicao com header L5 que dizia 93)
4. `INDEX.md` L30: Skills Avancadas 2.299 linhas vs real 2.301 (off-by-2)
5. `frank-mkt.md` L48: "92 skills em 18 BLOCOS" (real 93)
6. `frank-mkt.md` L180: "Total: 92 skills mapeadas"
7. `frank-mkt.md` L184: "Stack de agentes especialistas (14)" mas lista 15

**Plus**: 5 violacoes Guardian (typos + Unicode em-dashes violando `ascii_only: true`) + 2 findings MEDIUM IA-typical (numero "8 dimensoes" fabricado + generalizacao N=1 de "85% paridade").

**Como resolvido**: release v2.37.1 ("POST-AUDIT FIX") -- 14 issues corrigidas em commit unico.

**Custo**: 11 arquivos modificados, +126 / -61 linhas.

### Ciclo 3: v2.37.1 -> v2.38.0 (drift em release de hardening)

**O que aconteceu**: v2.38.0 adicionou **hardening operacional** (NAO features novas) -- fingerprint de iteracao para detectar loop A->B->A circular + fallback chain executavel bash/PowerShell. Total +332 linhas.

**Quando detectado**: auditoria pos-release. Lost-in-middle reportou: *"TERCEIRA RECORRENCIA do mesmo drift docs_mkt. CI lint cross-artifact nao e opcional, e bloqueador para parar a recorrencia"*.

**Drifts encontrados (4 NOVOS)**:

1. `INSTALACAO.md` ainda em v2.37.1 (esquecido pela terceira vez)
2. `ROADMAP.md` ainda em v2.37.1
3. `agents/frank-mkt.md` description+identidade "14 agentes especialistas + 1 atelier + 1 renderer" -- semanticamente equivalente a 16 mas inconsistente com outros arquivos que dizem "16 agentes"
4. `agents/README.md` header v2.37.0 (stale)

**Como resolvido**: release v2.38.1 ("POST-AUDIT FIX #2") + commitment de implementar CI lint na proxima release. Plus correcoes do arquiteto: bash usa `[ -s ]` (>0 bytes) enquanto PowerShell `>1024 bytes` -- inconsistencia de protocolo. Fallback chain reduzido de 5 niveis para 3 (source-auditor MEDIUM).

**Custo**: 12 arquivos modificados, +262 / -139 linhas.

### Ciclo 4: v2.38.1 -> v2.39.0 (drift na release que adiciona o lint anti-drift)

**O que aconteceu**: v2.39.0 IMPLEMENTOU o CI lint cross-artifact. Script Python `scripts/lint-cross-artifact.py` (~340 linhas) + GitHub Action `.github/workflows/lint.yml`. Validacao: contagens filesystem + versao plugin.json + 5 arquivos correlatos.

**Quando detectado**: auditoria pos-release. Lost-in-middle: *"Drift detectado. Pior: o proprio lint nao detecta os drifts"*.

**Drifts encontrados (4 NOVOS + meta-finding)**:

1. `INDEX.md:41` subsection "## Agentes (16/16 -- v2.37.0)" congelado em v2.37.0 -- **lint v2.39.0 so olhava o primeiro match do regex `## Status (v...)`, ignorando subsection headers**
2. `INDEX.md:63` subsection "## Slash Commands (10/10 -- v2.37.0)" congelado -- mesma causa
3. `INDEX.md:35` soma "61 medium + 24 high + 7 low" = 92, mas plugin.json declara 93 skills -- **lint v2.39.0 nao validava soma por tier**
4. `INDEX.md:45` celula de tabela "frank-mkt | 447 | orquestra 93 skills + 15 agentes + 10 commands" (real 16 agentes) -- **regressao do fix v2.38.1**, **lint v2.39.0 nao checava celulas de tabela**

**Meta-finding**: o lint TINHA BURACOS que coincidiam EXATAMENTE com os drifts introduzidos. A release que prometia "quebrar o ciclo" provou empiricamente que cobertura inicial era insuficiente.

**Como resolvido**: release v2.39.1 ("META-FIX") -- corrige drifts + ENDURECE o proprio lint. Novos checks:
- `_check_all_version_mentions()` itera TODOS matches (nao so `[0]`)
- Subsection headers `## Agentes (X/X -- vY)` validados
- Celulas de tabela `orquestra X skills + Y agentes` validadas
- Soma volatility tiers (`high + medium + low == total`) validada
- Auto-contradicao em help.md generalizada para "skills" (alem de "slash commands" e "agentes")
- Defensive default `mp.get("plugins", [{}])[0]` substituido por erro HIGH explicito

**Custo**: 12 arquivos modificados, +241 / -128 linhas.

### Ciclo 5: v2.39.1 -> v2.39.2 (drift em release que endurece o lint)

**O que aconteceu**: v2.39.1 endureceu o lint para cobrir os 4 buracos detectados em v2.39.0. Mas... o endurecimento ainda nao cobria tudo.

**Quando detectado**: auditoria pos-release. Lost-in-middle: *"v2.39.1 NAO fecha tudo. 3 drifts encontrados que o lint v2.39.1 ainda nao detecta"*.

**Drifts encontrados (3 NOVOS)**:

1. **HIGH**: `README.md` raiz CONGELADO em v2.35.0 (4 releases atrasadas) -- visivel no GitHub publico, ponto de entrada para visitantes. **VERSION_FILES no lint omitia README.md raiz**
2. **HIGH**: `help.md` declara "18 blocos" mas headers `### Bloco 1` a `### Bloco 19` existem -- auto-contradicao mid-file. **Lint nao checava count de blocos vs declaracoes**
3. **LOW**: `marketplace.json:13` description menciona "v2.39.0 adiciona" em release v2.39.1 -- drift narrativo

**Como resolvido**: release v2.39.2 ("META-META-FIX") -- corrige + adiciona testes do proprio lint:

- `README.md` raiz adicionado ao `VERSION_FILES` + 2 checks
- Nova funcao `check_block_count_consistency()` conta `### Bloco N` headers vs declaracoes "X blocos completos"
- Texto historico INDEX.md "MILESTONE 17 BLOCOS COMPLETOS" atualizado para 19 (preservando contexto)
- Regex refinado para evitar falsos positivos ("5 blocos perguntas" do investigador, "9 BLOCOS COMPLETOS plugin Frank-MKT" historico)
- **`scripts/test_lint.py`**: 7 testes unitarios com fixture sintetica `make_fixture_known_good()`. Stdlib unittest, 0 deps externas. Rodam em ~80ms. Validam: known-good fixture passa, drift de versao/contagem/blocos detectado, defensive default funciona, frontmatter check funciona.
- GitHub Action step novo "Run unit tests" antes do lint principal.

**Custo**: 13 arquivos modificados, +599 / -42 linhas (test_lint.py = ~360 linhas novas).

**Validacao recursiva**: `python3 scripts/test_lint.py` -> 7/7 PASS. `python3 scripts/lint-cross-artifact.py` -> 0 HIGH + 34 MEDIUM + 39 LOW (debito legado).

---

## 4. Padroes IA-Typical Identificados

Source-auditor detectou padroes especificos de codigo gerado por LLM nas sessoes. Listados aqui como referencia para outros auditores:

### 4.1. Fabricacao de numeros canonicos a partir de N=1

Em v2.37.0, ao escrever a skill `render-loop-svg`, foi criado um "checklist de 8 dimensoes" para avaliacao visual. **Esse numero "8" foi inventado** -- o aprendizado original (`aprendizado_infografico.md`) listava criterios nao numerados. Dimensoes 7 e 8 (Fidelidade vs referencia + Coerencia interna) foram preenchimento para chegar em 8 (numero esteticamente agradavel + paralelo a "8 Fundacoes" do template).

Tambem: "+45 pontos de paridade visual" e "~85% paridade" sao numeros legitimos do caso Gestuum (N=1) mas foram **generalizados como universais** ("teto realista de SVG-via-LLM"). Source-auditor: *"Honestidade cientifica exigiria 'observado em 1 caso documentado, replicar para validar'"*. Corrigido em v2.37.1.

**Heuristica de deteccao**: numero canonico declarado em N lugares sem citacao de fonte primaria + paralelismo simetrico forcado (8 dimensoes / 18 anti-patterns / 18 regras).

### 4.2. Repeticao estrutural nao-extraida em codigo

No `lint-cross-artifact.py`: 3 blocos quase-identicos em `check_count_consistency()` para validar cmd/agt/skl em help.md, e 2 blocos espelhados em `check_auto_contradiction()` para Slash Commands/Agentes. Source-auditor: *"50 linhas duplicadas. Helper trivial reduziria a 15"*.

**Heuristica**: 3+ blocos com mesma estrutura sintatica diferindo apenas em strings literais.

### 4.3. Dead code introducido por correcao parcial

Em v2.39.1, ao corrigir Finding #10 do source-auditor (defensive default mascarando erro), foi criado helper `_check_count_in_file()` para uso futuro. **Mas o helper nunca foi chamado** em nenhum call site. Source-auditor v2.39.1 reportou: *"Vetor #45 classico: IA lembrou de criar helper mas esqueceu de aplicar"*. Removido em v2.39.2.

**Heuristica**: funcao declarada com docstring completa + 0 call sites no mesmo arquivo.

### 4.4. Auto-referencia circular skill <-> agente

A skill `render-loop-svg/SKILL.md` declarava "ver `agents/renderer-visual.md` para detalhamento". O agente `renderer-visual.md` declarava "ver skill `render-loop-svg` para detalhamento canonico". **Cada lado declarava o outro como canonico** -- ping-pong de referencia. Resolvido em v2.38.1: skill explica **PORQUE** (taxonomia), agente tem **COMO** (scripts executaveis). Especializacao por papel.

**Heuristica**: 2+ artefatos referenciando-se mutuamente como "fonte canonica" sem distincao clara de papel.

### 4.5. Defensive default mascarando erro

`mp.get("plugins", [{}])[0]` silencia caso `marketplace.json` nao tenha chave `plugins` (estrutura quebrada). Validacao passa quando deveria falhar. Padrao IA-typical: prefere evitar exception com default que vira bug latente.

**Heuristica**: `dict.get(key, default)` onde `default` mascara estado invalido.

### 4.6. Regex frageis com caracteres Unicode literais

Regex de validacao usando em-dash `—` (U+2014) literal: `r"## Agentes \(\d+/\d+ — v[\d.]+\)"`. Se algum arquivo futuro usar hifen ASCII `-` (mais limpo, mais compativel com `ascii_only: true`), regex falha silenciosamente. **Drift do proprio validador**.

**Heuristica**: regex contendo caracteres non-ASCII em arquivos que declaram `ascii_only: true`.

### 4.7. Estrutura simetrica forcada pelo template

Template do plugin prescreve "8 Fundacoes + 16-19 Anti-Patterns + 18 Regras de Ouro + 4 Exemplos". Ao gerar SKILL.md, LLM atende fielmente -- mas alguns campos sao **preenchimento para chegar no numero**. Anti-patterns redundantes, Regras de Ouro com mesmo conteudo de Anti-Patterns invertido.

**Heuristica**: numero canonico do template + lista com items 90% redundantes entre si.

---

## 5. Por que Disciplina Humana + Memory Falharam

A sessao validou empiricamente que nenhum dos seguintes mecanismos foi suficiente:

### 5.1. Memory persistente

`MEMORY.md` continha:
- `feedback_remote_check_critico.md` -- verificar `git remote -v` antes de push (multi-projeto working dirs)
- `feedback_audit_pre_mudanca.md` -- usar auditores antes de Edit em projeto nao-mapeado
- `feedback_restore_point_antes_mudanca.md` -- tag anotada antes de mudanca grande
- `project_frank_mkt_estado_v2.md` -- estado atualizado a cada release

**Memory nao previniu drift**. O LLM lembrava do padrao mas reproduziu o erro pela 3a, 4a, 5a vez consecutivas.

### 5.2. Checklist humano

Apos cada release, o LLM podia listar mentalmente os 9 arquivos correlatos e marcar cada um. Era discipllina simples. **Mesmo assim falhou cada release**. Working memory exceeded.

### 5.3. Documentacao do problema

A propria sessao registrou em CHANGELOG da v2.37.1: *"CAUSA RAIZ: contagens hardcoded em N arquivos sem CI/lint cross-artifact para validar"*. Em v2.38.1: *"v2.37.0 -> v2.38.1 mostra que sem CI mecanico, drift continua"*. Em v2.39.0: *"Promessa: ciclo quebrado"*. Em v2.39.1: *"Promessa: ciclo finalmente quebrado"*.

**3 promessas explicitas + 3 quebras consecutivas**. Documentacao do problema nao gerou solucao automatica.

### 5.4. Apos correcao, falsa confianca

Cada release de "POST-AUDIT FIX" criou sensacao de "agora esta certo". Mas a proxima release reproduzia o erro -- frequentemente em arquivos **diferentes** dos corrigidos antes. v2.36.0 corrigiu INSTALACAO + ROADMAP, v2.37.0 esqueceu... INSTALACAO + ROADMAP. Padrao identico, 3 ciclos.

### 5.5. Auditores externos detectavam, mas detectacao manual nao escala

`frank-pentest:lost-in-middle` foi confiavel em todos os 5 ciclos. Auditoria custou ~$X tokens por execucao. Mas **rodar auditor a cada release manual nao escala** -- depende de disciplina humana de chamar o auditor, que falha pelo mesmo motivo que falha lembrar de atualizar arquivos.

---

## 6. A Solucao Iterativa: CI Lint Cross-Artifact

### 6.1. Filosofia

Substituir disciplina humana por **validacao mecanica automatizada** que:

1. **Roda automaticamente** em push/PR via GitHub Action -- sem depender de humano lembrar de invocar
2. **Falha o build** se drift HIGH detectado -- bloqueia merge ate fix
3. **Filesystem + plugin.json = ground truth** -- nao confiar em metadados duplicados como fonte de verdade
4. **Cobertura iterativamente expandida** -- cada drift detectado em producao vira novo check
5. **Testes unitarios do proprio lint** -- previnem regressao quando lint crescer

### 6.2. Arquitetura

```
.github/workflows/lint.yml
├── Step 1: Setup Python 3.11
├── Step 2: Run unit tests (test_lint.py)
│   └── 7 fixtures sinteticas -> 7 assertions
│       Falha aqui = bug no proprio lint
└── Step 3: Run cross-artifact lint (lint-cross-artifact.py)
    ├── Ground truth: count_skills/agents/commands + plugin.json["version"]
    ├── 9 checks atualmente (cresceu de 5 em v2.39.0)
    │   ├── check_version_consistency (7 arquivos correlatos)
    │   ├── check_count_consistency (description fields + INDEX header + INDEX tabela + soma volatility + help patterns)
    │   ├── check_block_count_consistency (### Bloco N vs "X blocos" declarations)
    │   ├── check_auto_contradiction (help.md workflow vs heading)
    │   ├── check_skill_frontmatter (campos obrigatorios)
    │   ├── check_cross_refs (skills/agents referenciados existem)
    │   └── check_ascii_compliance (en-dashes em arquivos ascii_only:true)
    ├── Severidades: HIGH (bloqueia) / MEDIUM (warn) / LOW (info)
    └── Output limitado: HIGH lista todos, MEDIUM/LOW listam 10 + "... N more"
```

### 6.3. Anatomia de um check

Cada check segue padrao consistente:

```python
def check_X_consistency(...) -> None:
    """Docstring explicando motivacao + referencia ao drift que motivou criacao."""
    # 1. Ground truth (filesystem ou plugin.json)
    expected = ...

    # 2. Para cada arquivo correlato:
    for file in correlated_files:
        # 2.1. Extrair declaracao via regex
        matches = grep_line_numbers(file, pattern)
        # 2.2. Comparar com ground truth
        for line_no, content in matches:
            found = parse_match(content)
            if found != expected:
                errors.append(LintError(
                    severity, file, line_no,
                    f"L{line_no} diz {found}, ground truth tem {expected}"
                ))
```

### 6.4. Iteracao da cobertura ao longo dos ciclos

```
v2.39.0 (5 checks):
├── version_consistency (7 arquivos)
├── count_consistency (descriptions + INDEX agregado + help.md patterns)
├── auto_contradiction (so help.md)
├── skill_frontmatter
└── cross_refs (5 arquivos hardcoded)

v2.39.1 (8 checks, +3 cobertura):
├── + INDEX subsection headers (## Agentes / Slash Commands com versao)
├── + INDEX celulas de tabela (orquestra X skills + Y agentes)
├── + INDEX soma volatility tiers
├── + auto_contradiction generalizada para "skills" (alem de slash/agentes)
└── + INSTALACAO.md valida TODAS mencoes (nao so a ultima)

v2.39.2 (9 checks + 7 testes, +1 cobertura + auto-validacao):
├── + check_block_count_consistency (### Bloco N vs "X blocos")
├── + README.md raiz no VERSION_FILES + 2 checks
└── + test_lint.py: 7 fixtures sinteticas validam cada check
```

### 6.5. Por que testes unitarios do lint importam

Sem testes do proprio validador, cada endurecimento do lint pode introduzir bug que silenciosamente faz check virar no-op. Cenario real: regex frageis em v2.39.1 podiam quebrar com pequenas variacoes de markdown.

Fixtures sinteticas garantem:
- **Regression**: se alguem mudar o lint, fixture conhecida-boa ainda deve passar
- **Specification**: cada teste documenta um cenario de drift que o lint detecta
- **Refactor safety**: helpers podem ser extraidos com confianca de que comportamento e preservado

Custo: ~360 linhas Python stdlib. ~80ms execucao. Zero dependencias externas.

---

## 7. Proposta de Vetor frank-pentest

### 7.1. Nome proposto

**Vetor #6b: Drift Documental Cross-Artifact Recorrente em Plugins Markdown Agentic**

(Subset/expansao do vetor #6 -- drift de protocolo -- aplicado especificamente a plugins Markdown agentic com N artefatos correlatos)

### 7.2. Definicao

Divergencia recorrente entre declaracoes de metadados duplicados em arquivos correlatos de plugin Markdown agentic, originada de atualizacao parcial durante releases, com caracteristica de **recorrencia entre releases consecutivas** mesmo apos remediacao manual.

### 7.3. Indicadores diagnosticos

Auditor deve buscar **simultaneamente**:

1. **Contagens duplicadas em N >= 5 arquivos** (skills/commands/agentes totalizados em multiplos lugares)
2. **Versao plugin.json + version em outros arquivos correlatos** (marketplace.json, INDEX, help, INSTALACAO, ROADMAP, agents/README)
3. **Frontmatter de agente principal carregando contagens** (afeta runtime se persona principal tem dados stale)
4. **Auto-contradicao mid-file** -- mesmo arquivo declarando 2 valores distintos para mesmo metadado
5. **Texto historico misturado com declaracoes atuais** (MILESTONE 17 BLOCOS COMPLETOS em arquivo que descreve estado v2.39.2)
6. **Celulas de tabela em INDEX/help** repetindo contagens declaradas em headers
7. **Soma por tier/categoria** (volatility, severidade) que deve casar com total agregado
8. **Comentarios e exemplos inline** com contagens (`/frank-mkt:help skills -> 92 skills`)

### 7.4. Severidades sugeridas

| Severidade | Criterio |
|---|---|
| **HIGH** | Drift que afeta runtime do plugin OU visivel publicamente (README, INSTALACAO publica, persona principal) |
| **MEDIUM** | Drift entre metadados internos sem afetar runtime mas confundindo manutenedor |
| **LOW** | Drift cosmetico (formato, narrativa, debito legado documentado) |

### 7.5. Tecnica de deteccao

**Passo 1**: identificar a **fonte de verdade unica** (geralmente filesystem + plugin.json/package.json/Cargo.toml).

**Passo 2**: listar **arquivos correlatos** que declaram metadados duplicados. Para plugins Markdown agentic, tipicamente:
- Marketplace manifest (raiz)
- Plugin manifest (subdirectory)
- README raiz
- INDEX/inventario de skills/components
- help/menu user-facing
- Persona principal (agente default)
- Docs publicos (INSTALACAO, ROADMAP)
- CHANGELOG

**Passo 3**: para CADA metadado correlato (versao, total counts, soma por categoria), aplicar regex em CADA arquivo e comparar com ground truth.

**Passo 4**: detectar auto-contradicao mid-file -- mesmo arquivo com 2 patterns que divergem.

**Passo 5**: validar coerencia entre headers e ground truth (`### Bloco N` count em help vs declaracao "X blocos" em INDEX).

### 7.6. Pseudo-codigo de check generico

```python
def check_drift_cross_artifact(plugin_root: Path) -> list[LintError]:
    errors = []

    # Ground truth
    truth = {
        "version": load_manifest(plugin_root / "plugin.json")["version"],
        "skills": count_dirs(plugin_root / "skills"),
        "agents": count_md_files(plugin_root / "agents", exclude=["README.md"]),
        "commands": count_md_files(plugin_root / "commands"),
    }

    # Arquivos correlatos
    correlated = [
        plugin_root.parent / ".claude-plugin" / "marketplace.json",
        plugin_root.parent / "README.md",
        plugin_root / "skills" / "INDEX.md",
        plugin_root / "commands" / "help.md",
        plugin_root / "agents" / "README.md",
        plugin_root / "agents" / "frank-mkt.md",  # persona principal
        plugin_root.parent / "docs_mkt" / "INSTALACAO.md",
        plugin_root.parent / "docs_mkt" / "ROADMAP-FRANK-MKT.md",
    ]

    # Para cada arquivo, para cada metadado, validar
    for file in correlated:
        if not file.exists():
            continue
        validate_version_mentions(file, truth["version"], errors)
        validate_count_mentions(file, truth, errors)
        validate_no_auto_contradiction(file, errors)

    return errors
```

### 7.7. Indicador de cronicidade

Vetor #6b e **especialmente perigoso quando reincidente**. Sintomas:

- Mesmo arquivo aparece em N >= 3 auditorias consecutivas com mesmo tipo de drift
- CHANGELOG menciona "DRIFT REPAIR" em 2+ releases consecutivas
- Documentacao do projeto contem promessa "ciclo quebrado" seguida de evidencia de nao-quebra

Quando isso ocorre, auditor deve reportar **HIGH com escalacao**: o projeto precisa de validacao automatizada antes da proxima release. Disciplina manual nao escala.

### 7.8. Falsos positivos comuns

Padroes que parecem drift mas sao legitimos:

1. **Texto historico em CHANGELOG/INDEX**: "MILESTONE 17 BLOCOS COMPLETOS" descrevendo v2.28.0 -- deve ser preservado como historia, nao corrigido para estado atual
2. **Contagens parciais descritivas**: "5 blocos de perguntas" do agente investigador -- nao e total do plugin
3. **Exemplos inline com numeros antigos**: "version 1.0.0" em exemplo de codigo -- nao e declaracao real
4. **Documentacao narrativa**: descricao da jornada do plugin pode mencionar contagens historicas

Auditor deve refinar regex para apenas pegar declaracoes totalizantes inequivocas:
- `r"\((\d+) blocos\)"` -- entre parens (declaracao estrutural)
- `r"(\d+) blocos completos"` -- com palavra "completos"
- `r"\*\*(\d+) skills\*\*"` -- em formatacao bold (destaque)

### 7.9. Mitigacao recomendada

Auditor deve sugerir **CI lint cross-artifact dedicado** como mitigacao primaria. Pseudo-spec minima:

```yaml
# .github/workflows/lint.yml minimum spec
name: Cross-Artifact Lint
on: [push, pull_request]
jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
      - run: python3 scripts/lint-cross-artifact.py
        # Exit 1 se HIGH detectado, bloqueia merge
```

Plus: **testes unitarios do proprio lint** com fixtures sinteticas que validam cada check. Sem isso, o lint vira SPOF (Single Point of Failure) -- bug no validador = drift escapa silenciosamente.

---

## 8. Anti-Patterns Enumerados (referencia rapida)

Esses sao anti-patterns observados durante a sessao. Documentados para incluir em frank-pentest ou em manutencao-skills do plugin:

1. **Confiar em disciplina humana para manter N >= 5 arquivos sincronizados** -- falha empiricamente em 5/5 ciclos
2. **Memory persistente nao previne drift** -- registra padrao mas reproduce erro
3. **Declarar "ciclo quebrado" antes de implementar validacao mecanica** -- 3 promessas falsas consecutivas
4. **Implementar lint cross-artifact sem auto-testes** -- lint vira SPOF
5. **Adicionar lint mas nao incluir todos os arquivos correlatos** -- README.md raiz omitido em v2.39.0
6. **Validar so o primeiro match de um regex** -- subsection headers escapam
7. **Defensive default `dict.get(key, default)` em JSON cuja chave e invariante** -- mascara estado quebrado
8. **Helper criado mas nunca chamado** -- dead code introducido por correcao parcial
9. **Regex com caracteres Unicode literais** em arquivos que declaram `ascii_only: true`
10. **Texto historico misturado com declaracoes atuais** sem distincao tipografica
11. **Auto-referencia circular skill <-> agente** -- ambos declaram o outro como canonico
12. **Numero canonico fabricado a partir de N=1** generalizando como universal
13. **Estrutura simetrica forcada** -- preencher items para chegar no numero do template
14. **Repeticao estrutural nao-extraida** -- 3+ blocos com mesma estrutura sintatica
15. **CHANGELOG narrando o "diff esperado" sem validar diff real** -- documentacao aspiracional

---

## 9. Metricas Concretas da Sessao

Numeros para calibrar magnitude do problema:

| Metrica | Valor |
|---|---|
| Duracao da sessao | ~6 horas |
| Releases publicadas | 8 (v2.36.0 a v2.39.2) |
| Tags GitHub | 9 (incluindo restore point) |
| Ciclos de drift consecutivos | 5 |
| Total de drifts detectados | 25+ (entre as 5 auditorias) |
| Arquivos correlatos mantidos | 9 (com metadados duplicados) |
| Linhas do plugin antes | ~119.000 |
| Linhas do plugin depois | ~121.500 |
| Novos artefatos adicionados | 5 (1 skill + 1 agente + 1 command + 1 lint + 1 test_lint) |
| Auditores externos invocados | 4 (lost-in-middle, arquiteto, source-auditor, guardian) |
| Numero de auditorias rodadas | 5 rodadas x 4 agentes = 20 invocacoes |
| Tempo de execucao do CI lint | <2s |
| Tempo de execucao dos testes unitarios | ~80ms |
| Falsos positivos detectados em primeiras versoes do lint | ~4 (corrigidos com regex refinado) |
| Crescimento do lint v2.39.0 -> v2.39.2 | 5 checks -> 9 checks (+80% cobertura) |

---

## 10. Reproduzindo o Vetor em Outro Plugin

Para auditores que querem verificar se um plugin Markdown agentic similar tem esse vetor:

### 10.1. Checklist diagnostico rapido

```bash
# 1. Identificar arquivos correlatos com metadados duplicados
find . -type f -name "*.md" -o -name "*.json" | head -20

# 2. Contar artefatos reais (ground truth)
ls plugin-dir/skills/ | wc -l    # skills count
ls plugin-dir/agents/*.md | wc -l    # agents count
ls plugin-dir/commands/*.md | wc -l  # commands count

# 3. Grep contagens declaradas
grep -rn "X skills" .   # substituir X pela contagem real
grep -rn "Y agentes" .
grep -rn "Z commands" .

# 4. Verificar se declaracoes batem com ground truth
# Se houver divergencia: drift confirmado

# 5. Verificar versao
cat plugin-dir/.claude-plugin/plugin.json | grep version
grep -rn "v[0-9]\+\.[0-9]\+\.[0-9]\+" --include="*.md" .

# Comparar todas as ocorrencias com plugin.json version
```

### 10.2. Sintomas para escalar como HIGH

- 3+ arquivos com versoes diferentes
- 2+ arquivos com contagens diferentes para o mesmo metadado
- Auto-contradicao no mesmo arquivo (regex pattern aparecendo com 2 valores distintos)
- Persona principal de agente declarando contagens stale (afeta runtime!)

### 10.3. Recomendacao final ao auditor

Quando detectar vetor #6b em um plugin:

1. **Reportar todos os drifts encontrados** com paths + line numbers + valores
2. **Reportar count vs ground truth** -- mostrar diferenca explicita
3. **Detectar reincidencia**: olhar CHANGELOG dos ultimos 3-5 releases. Se mencionar "DRIFT REPAIR" ou "POST-AUDIT FIX" mais de uma vez, escalar para HIGH com nota "vetor recorrente"
4. **Sugerir mitigacao mecanica**: nao se contentar com fix manual. Recomendar CI lint cross-artifact + testes unitarios
5. **Confirmar com lint posterior**: depois do fix, rodar audit novamente. Se ainda houver drift, e sinal de cobertura insuficiente do fix

---

## 11. Licoes Generalizaveis

Aplicaveis alem de plugins Markdown agentic:

### 11.1. Metadados duplicados sao passivo de manutencao

Qualquer codebase com mesmo dado declarado em N >= 5 lugares precisa de validacao automatica. Disciplina humana nao escala.

### 11.2. Filesystem (ou banco) e a unica fonte de verdade

Numero declarado em metadado pode mentir. Numero derivado de filesystem nao mente. Validacao deve sempre comparar declaracoes contra ground truth derivado, nao contra outras declaracoes.

### 11.3. Auditoria pos-release > auditoria pre-release

Frank-pentest:lost-in-middle detectou drift que humano + IA tinham introducido na release anterior. Drift e mais facil de detectar quando ja existe do que prevenir antes de existir. **Padrao: release rapido + auditoria + fix rapido**, em vez de tentar evitar drift na primeira vez.

### 11.4. Lint sem testes vira SPOF

Validador automatizado e tao bom quanto seus testes. Sem suite de regression que valida o validador, qualquer endurecimento futuro pode silenciosamente quebrar checks existentes. Testar o testador nao e overkill -- e fundacao.

### 11.5. Cobertura iterativa > cobertura ideal

Lint inicial em v2.39.0 cobriu ~70% dos padroes de drift conhecidos. Cada auditoria subsequente revelou novos padroes que viraram novos checks. **Filosofia**: nao tentar antecipar 100% no primeiro design. Aceitar que cobertura cresce iterativamente conforme novos padroes sao descobertos em producao.

### 11.6. Documentar a recorrencia honestamente

Cada CHANGELOG mencionou explicitamente "Nth recorrencia do mesmo vetor". Sem honestidade sobre falhas anteriores, padrao se mascara. **Padrao: contar ciclos. Recorrencia + 1 a cada falha**.

### 11.7. Restore points sao baratos -- usar abundantemente

A sessao publicou 9 tags GitHub (1 restore point inicial + 8 releases). Qualquer mudanca podia ser revertida em comando unico. Custo: zero. Beneficio: confianca para fazer mudancas grandes sem medo de quebrar estado conhecido-bom.

---

## 12. Apendice: Comandos para Reproduzir

### 12.1. Rodar lint cross-artifact no frank-mkt

```bash
cd D:/4NK/frank-mkt
python3 frank-mkt-plugin/scripts/lint-cross-artifact.py
# Exit 0 = PASS / PASS WITH WARNINGS
# Exit 1 = HIGH detectado, build bloqueado
```

### 12.2. Rodar testes unitarios do lint

```bash
cd D:/4NK/frank-mkt
python3 frank-mkt-plugin/scripts/test_lint.py
# Deve mostrar "Ran 7 tests in 0.060s -- OK"
```

### 12.3. Aplicar mesma estrutura em outro plugin

```bash
# 1. Copiar lint script
cp frank-mkt/frank-mkt-plugin/scripts/lint-cross-artifact.py target-plugin/scripts/

# 2. Adaptar paths das constantes no topo do script
# (SKILLS_DIR, AGENTS_DIR, COMMANDS_DIR, INDEX_MD, etc)

# 3. Adaptar lista VERSION_FILES para arquivos correlatos do target-plugin

# 4. Copiar test_lint.py + adaptar fixture sintetica

# 5. Copiar .github/workflows/lint.yml

# 6. Rodar lint local antes de push -- corrigir drifts existentes

# 7. Commit + push -- CI Action passa a rodar automaticamente
```

### 12.4. Reverter caso drift novo seja detectado

```bash
git tag -l "v*"   # lista tags disponiveis
git reset --hard <tag-anterior>   # reverte para release boa
git push --force origin main      # so se necessario; cuidado
```

---

## 13. Referencias

### 13.1. Vetores frank-pentest correlatos

- **#6 Drift de protocolo** -- generalizacao deste vetor
- **#15 Cross-Markdown drift** -- caso especifico de drift entre Markdown files
- **#16 Negative-rule-mid-prompt** -- auto-contradicao mid-file
- **#18 Aspirational design** -- dead code declarando intencao nao implementada
- **#45 Memory-auto-update sem audit** -- IA "lembrou" mas esqueceu de aplicar

### 13.2. Auditores chave usados na sessao

- `frank-pentest:lost-in-middle` -- detectou todos os 25+ drifts
- `frank-pentest:arquiteto` -- validou design de cada release + recomendacoes
- `frank-pentest:source-auditor` -- detectou padroes IA-typical no codigo
- `frank-dev:guardian-agent` -- validou Guardian compliance

### 13.3. Commits e tags chave

```
2167a89  v2.35.0 (estado inicial)
8c951f8  Commit doc aprendizado_infografico.md (input que motivou sessao)
c1a0706  v2.36.0 DRIFT REPAIR (ciclo 1 fix)
1f0e99b  v2.37.0 Render-loop feature
872f1d9  v2.37.1 POST-AUDIT FIX (ciclo 2 fix)
a8ee7cf  v2.38.0 Hardening operacional
f039aae  v2.38.1 POST-AUDIT FIX #2 (ciclo 3 fix)
0bf8a3b  v2.39.0 CI lint inicial
6788068  v2.39.1 META-FIX (ciclo 4 fix - lint endurecido)
0122a02  v2.39.2 META-META-FIX (ciclo 5 fix - testes do lint)
```

### 13.4. Arquivos canonicos a auditar em qualquer plugin similar

- `<plugin-root>/.claude-plugin/plugin.json` -- versao + description
- `<repo-root>/.claude-plugin/marketplace.json` -- marketplace manifest
- `<repo-root>/README.md` -- ponto de entrada GitHub publico
- `<plugin-root>/CHANGELOG.md` -- historico de releases
- `<plugin-root>/skills/INDEX.md` -- inventario de skills
- `<plugin-root>/commands/help.md` -- menu user-facing
- `<plugin-root>/agents/README.md` -- inventario de agentes
- `<plugin-root>/agents/<persona-principal>.md` -- system prompt do agente default
- `<repo-root>/docs_mkt/INSTALACAO.md` (ou similar) -- guia de instalacao publico
- `<repo-root>/docs_mkt/ROADMAP*.md` -- roadmap historico

---

## 14. Conclusao

O vetor de **drift documental cross-artifact recorrente** em plugins Markdown agentic e **endemico estrutural**, nao um bug pontual. Caracteriza-se por:

1. **N >= 5 arquivos correlatos** com metadados duplicados
2. **Falha consistente de disciplina humana + memory** para manter sincronizado
3. **Recorrencia entre releases consecutivos** mesmo apos remediacao
4. **Detectavel mecanicamente** com CI lint cross-artifact + testes unitarios

A solucao validada empiricamente em 5 ciclos consecutivos:

1. **Auditor automatico** (frank-pentest:lost-in-middle ou equivalente) detecta drift apos cada release
2. **CI lint cross-artifact** integrado ao GitHub Actions falha build se drift HIGH
3. **Testes unitarios** do proprio lint previnem regressao quando lint crescer
4. **Cobertura iterativa**: cada drift novo detectado em producao vira novo check

O frank-mkt v2.39.2 termina a sessao com infraestrutura completa para preveni drift futuro **mecanicamente**, validada por suite de testes do proprio validador. Estado documentado como referencia replicavel para outros plugins similares.

**Para o frank-pentest**: considerar incorporar este documento como expansao do vetor #6 ou criar vetor #6b especifico para plugins Markdown agentic. Heuristicas de deteccao + tecnicas de auditoria + mitigacao recomendada estao formalizadas na secao 7.

---

*Documento escrito por: Claude Opus 4.7 (1M context), Claude Code CLI*
*Sessao: 2026-05-11 / 8 releases publicadas / 5 ciclos de drift consecutivos*
*Plugin auditado: frank-mkt (alexandrejalkh/frank-mkt) v2.35.0 -> v2.39.2*
*Para: frank-pentest absorver como vetor + arquitetos de plugins similares*
*HEAD final: 0122a02*
