---
description: Mostra estado atual do projeto frank-mkt (marca + persona + campanhas ativas + decisoes + ultimas entregas)
argument-hint: (sem args — le .frank-mkt/ do CWD) ou nome de secao (marca|persona|campanhas|decisoes|entregaveis|pesquisa)
allowed-tools: Read, Glob, Bash
---

# /frank-mkt:stack

Mostra um snapshot estruturado do estado atual do projeto de marketing
(frank-mkt), lendo a pasta `.frank-mkt/` no diretorio atual (CWD). Util
para retomar contexto em nova sessao, alinhar time, gerar handoff ou
identificar gaps de marca / campanha.

> Este comando NAO modifica arquivos. Apenas le, sintetiza e apresenta.
> Para inicializar o projeto, use `/frank-mkt:init` primeiro.

---

## O que este comando faz

Le a estrutura `.frank-mkt/` (criada via `/frank-mkt:init`) e apresenta
um relatorio estruturado em 6 blocos:

1. **Marca atual** — de `marca/identidade.md` + `marca/voice-tone.md` +
   `marca/visual.md` (se existirem)
2. **Persona ICP** — de `persona/icp.md` + `persona/jtbd.md` +
   `persona/dores-desejos.md`
3. **Campanhas ativas** — de `campanhas/*/` (status: em-andamento)
4. **Decisoes recentes** — ultimas 5 entradas de `decisoes/log.md`
5. **Entregaveis recentes** — ultimos 5 arquivos modificados em
   `entregaveis/`
6. **Pesquisa atual** — sintese de `pesquisa/concorrentes/` +
   `pesquisa/trends/`

---

## Estrutura esperada de `.frank-mkt/`

```
.frank-mkt/
├── cliente.md                    # nome cliente, briefing inicial
├── marca/
│   ├── identidade.md             # archetype, posicionamento, manifesto
│   ├── voice-tone.md             # voz, tom, do/dont
│   └── visual.md                 # paleta, tipografia, mood
├── persona/
│   ├── icp.md                    # ideal customer profile
│   ├── jtbd.md                   # jobs-to-be-done
│   └── dores-desejos.md
├── campanhas/
│   └── {nome-campanha}/
│       ├── briefing.md
│       ├── status.md             # status: em-andamento|pausada|encerrada
│       └── kpis.md
├── decisoes/
│   └── log.md                    # log cronologico (markdown)
├── entregaveis/
│   ├── copy/
│   ├── visual/
│   └── ads/
└── pesquisa/
    ├── concorrentes/
    └── trends/
```

Se a estrutura nao existir, o comando sugere `/frank-mkt:init`.

---

## Workflow

### Passo 1 — Verificar existencia de `.frank-mkt/`

```bash
# pseudo
if not exists(".frank-mkt/"):
    print("Nenhum projeto frank-mkt detectado no CWD.")
    print("Sugestao: rode /frank-mkt:init para inicializar.")
    exit
```

Use `Glob` em `.frank-mkt/**/*.md` para confirmar.

### Passo 2 — Ler arquivos chave

Para cada bloco do relatorio, faca `Read` dos arquivos relevantes.
Tolere ausencia (arquivo nao criado ainda) e marque como `(pendente)`.

Arquivos criticos (ler sempre se existirem):

- `.frank-mkt/cliente.md`
- `.frank-mkt/marca/identidade.md`
- `.frank-mkt/marca/voice-tone.md`
- `.frank-mkt/marca/visual.md`
- `.frank-mkt/persona/icp.md`
- `.frank-mkt/persona/jtbd.md`
- `.frank-mkt/decisoes/log.md`

Use `Glob` para descobrir:

- `campanhas/*/status.md` (filtrar status: em-andamento)
- `entregaveis/**/*.md` (ordenar por mtime desc, top 5)
- `pesquisa/concorrentes/*.md`
- `pesquisa/trends/*.md`

### Passo 3 — Sintetizar

Para cada bloco, extrair 1-3 linhas chave (nao copiar arquivo inteiro).
Exemplos de extracao:

- **Marca / archetype**: procurar linha tipo `Archetype: Sage` ou
  cabecalho `## Archetype` no `identidade.md`
- **Voice**: primeiro paragrafo de `voice-tone.md`
- **Persona principal**: cabecalho do ICP (nome + cargo)
- **Decisao recente**: ultimas 5 linhas com prefixo de data em
  `decisoes/log.md`
- **Entregaveis**: nome do arquivo + data de modificacao

### Passo 4 — Apresentar relatorio

Formato fixo abaixo. Se uma secao nao tiver dados, marcar
`(nenhum / pendente)` e sugerir skill responsavel.

### Passo 5 — Cross-skill suggestions

Ao final, sugerir 2-3 proximas acoes baseadas nos gaps detectados.

---

## Output formato (modelo)

```
=== FRANK-MKT STACK STATUS ===
Cliente: {{NOME_CLIENTE}}
CWD: {{ABSOLUTE_PATH}}
Ultima atividade: {{DATA_ULTIMO_ARQUIVO_MODIFICADO}}
Disclaimer: snapshot educacional — confirme com cliente antes de
publicar.

[MARCA]
Archetype: {{ARCHETYPE}} (ex: Sage, Hero, Outlaw)
Posicionamento: {{POSICIONAMENTO_1_LINHA}}
Voice: {{VOICE_3_ADJETIVOS}}
Visual: {{PALETA + TIPOGRAFIA_RESUMO}}
Status: completa | parcial | pendente

[PERSONA ICP]
Buyer principal: {{NOME_FICTICIO}}, {{CARGO}}, {{SEGMENTO}}
JTBD: {{FRASE_JTBD}}
Dores top: {{3_DORES}}
Desejos top: {{3_DESEJOS}}
Status: completa | parcial | pendente

[CAMPANHAS ATIVAS] ({{N}})
1. {{NOME_CAMPANHA}} — em andamento
   Skills: linkedin-organico + email-marketing
   KPIs: {{METRICAS_CHAVE}}
2. ...
(Se 0: sugerir invocar funil-jornada + posicionamento-marca)

[DECISOES RECENTES] (ultimas 5)
- 2026-05-09: Decidido posicionamento como Sage archetype
  (cross-skill: branding)
- 2026-05-08: Mudado canal principal de IG para LinkedIn
  (cross-skill: linkedin-organico)
- ...

[ENTREGAVEIS RECENTES] (ultimos 5 modificados)
- entregaveis/copy/landing-v3.md (2026-05-09)
- entregaveis/visual/og-image-campanha-x.md (2026-05-08)
- ...

[PESQUISA]
Concorrentes mapeados: {{N}} ({{LISTA_CURTA}})
Trends ativas: {{N}} ({{LISTA_CURTA}})
Status: atualizada | desatualizada (>30d) | inexistente

[CROSS-SKILL SUGGESTIONS]
- Marca incompleta -> rode skill: branding +
  posicionamento-marca
- Persona vaga -> rode skill: persona-icp-deep (se existir) ou
  funil-jornada
- Sem campanha ativa -> rode skill: funil-jornada + big-idea
- Pesquisa desatualizada -> rode skill: newsjacking-real-time +
  seo-keywords (refresh trends)
- Sem voice-tone -> rode skill: escrita-por-publico

=== FIM ===
```

---

## Argumentos

`$ARGUMENTS` opcional. Se fornecido, filtra para uma unica secao:

| arg          | mostra apenas                         |
|--------------|---------------------------------------|
| marca        | bloco [MARCA]                         |
| persona      | bloco [PERSONA ICP]                   |
| campanhas    | bloco [CAMPANHAS ATIVAS]              |
| decisoes     | bloco [DECISOES RECENTES]             |
| entregaveis  | bloco [ENTREGAVEIS RECENTES]          |
| pesquisa     | bloco [PESQUISA]                      |
| (vazio)      | relatorio completo (default)          |

Exemplos:

- `/frank-mkt:stack` -> relatorio completo
- `/frank-mkt:stack marca` -> apenas bloco de marca
- `/frank-mkt:stack campanhas` -> apenas campanhas ativas

Se `$ARGUMENTS` nao estiver na lista acima, avisar:
`Secao desconhecida. Validas: marca, persona, campanhas, decisoes,
entregaveis, pesquisa`.

---

## Cross-skill references

Este comando NAO executa skills, apenas SUGERE. As sugestoes mapeam
gaps detectados para skills do plugin frank-mkt:

| Gap detectado                          | Skill sugerida                           |
|----------------------------------------|------------------------------------------|
| `marca/identidade.md` ausente          | branding + posicionamento-marca          |
| `marca/voice-tone.md` ausente          | escrita-por-publico                      |
| `marca/visual.md` ausente              | composicao-visual + geracao-imagens-ia   |
| `persona/icp.md` ausente               | funil-jornada (etapa ICP)                |
| `persona/jtbd.md` ausente              | funil-jornada (JTBD)                     |
| Sem campanhas em andamento             | big-idea + funil-jornada                 |
| `pesquisa/trends/` >30d                | newsjacking-real-time + seo-keywords     |
| `pesquisa/concorrentes/` <3 mapeados   | seo-keywords + multi-platform-narrative  |
| Decisoes <3 no log                     | (nada — apenas sinaliza projeto novo)    |
| Sem KPIs em campanha                   | metricas-marketing                       |

---

## Heuristicas de status

Para classificar `Status: completa | parcial | pendente`:

- **completa**: todos os arquivos da secao existem E tem >20 linhas
  cada
- **parcial**: pelo menos 1 arquivo existe mas com <20 linhas OU
  algum arquivo da secao falta
- **pendente**: nenhum arquivo da secao existe

Para `Pesquisa atualizada | desatualizada`:

- **atualizada**: arquivos de `pesquisa/trends/` modificados
  nos ultimos 30 dias
- **desatualizada**: ultima modificacao >30 dias
- **inexistente**: pasta vazia ou ausente

---

## Disclaimer educational

Este comando apresenta um SNAPSHOT do projeto. Decisoes finais de
posicionamento, campanha e investimento devem ser:

1. Validadas com o cliente (briefing assinado)
2. Confrontadas com dados reais (analytics, CRM, pesquisa primaria)
3. Revisadas com o time (marketing + comercial + produto)

A sugestao de skills e orientativa — o profissional deve julgar a
ordem e prioridade conforme o contexto do cliente.

---

## Exemplos de uso

### Caso 1 — projeto novo, recem inicializado

```
/frank-mkt:stack
```

Output esperado: muitos `(pendente)`, sugestoes de invocar branding,
posicionamento-marca, funil-jornada.

### Caso 2 — projeto em andamento, retomada de sessao

```
/frank-mkt:stack
```

Output esperado: marca completa, persona completa, 2 campanhas
ativas, 5 decisoes recentes, entregaveis em copy/ e visual/.

### Caso 3 — alinhamento de campanha

```
/frank-mkt:stack campanhas
```

Output esperado: apenas bloco [CAMPANHAS ATIVAS] com KPIs e skills
envolvidas.

### Caso 4 — handoff entre profissionais

```
/frank-mkt:stack
```

Resultado serve como briefing rapido de 1 pagina para o proximo
profissional pegar o projeto.

---

## Casos de borda

| Cenario                                | Comportamento                            |
|----------------------------------------|------------------------------------------|
| `.frank-mkt/` nao existe               | Sugerir `/frank-mkt:init`                |
| `.frank-mkt/` existe mas vazio         | Mostrar todos blocos como `(pendente)`   |
| Arquivo malformado (yaml/md quebrado)  | Marcar `(erro de leitura)` + path        |
| `decisoes/log.md` vazio                | `(nenhuma decisao registrada)`           |
| `entregaveis/` vazio                   | `(nenhum entregavel ainda)`              |
| `$ARGUMENTS` invalido                  | Avisar e listar secoes validas           |
| Mais de 1 cliente em `cliente.md`      | Mostrar todos, sinalizar com warning     |
| Symlinks dentro de `.frank-mkt/`       | Seguir mas sinalizar `(symlink)`         |

---

## Notas de implementacao

- Usar `Glob` antes de `Read` para evitar falhas em arquivos ausentes
- Ordenar entregaveis por mtime descendente (mais recentes primeiro)
- Limitar log de decisoes a 5 ultimas entradas (parsear cabecalhos
  com data ISO `YYYY-MM-DD`)
- Truncar campos longos para max 80 chars, sufixo `...`
- Nao expor caminhos completos do filesystem alem do CWD inicial
- Output em markdown plano (sem ANSI colors) para portabilidade

---

## Saida sucinta

Apos apresentar o relatorio, terminar com:

```
Snapshot gerado. Para acoes sugeridas, invoque as skills indicadas
em [CROSS-SKILL SUGGESTIONS].
```

Nao atualizar nenhum arquivo — este comando e read-only.
