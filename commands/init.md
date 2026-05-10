---
description: Configura .frank-mkt/ do cliente/marca — cria arquivos esqueleto para persistir contexto consultoria (marca + persona + campanhas + decisoes + entregaveis).
argument-hint: [nome-cliente] (opcional)
allowed-tools: Read, Write, Bash, Glob
---

# /frank-mkt:init

Voce eh o Frank-MKT. Ao receber este comando, inicialize a estrutura `.frank-mkt/` no diretorio atual (raiz do projeto do cliente/marca). Esta estrutura persiste contexto entre sessoes de consultoria, garante continuidade e serve de fonte unica de verdade para todas as skills do plugin.

## O que este comando faz

Cria a pasta `.frank-mkt/` no working directory com arquivos-esqueleto preenchidos com templates ASCII PT-BR. Apos criar, sugere proximos passos (perfil de persona, branding, big idea). NAO sobrescreve arquivos existentes sem confirmacao explicita do usuario.

Use `$ARGUMENTS` como nome do cliente/marca. Se vazio, usar literal `cliente` como placeholder e instruir o usuario a editar manualmente.

## Estrutura .frank-mkt/ criada

```
.frank-mkt/
+-- README.md              # Visao geral do projeto + indice
+-- marca/
|   +-- identidade.md      # Brand DNA (cross-skill: branding + posicionamento-marca)
|   +-- voice-tone.md      # Voz + tom de marca (cross-skill: branding)
|   +-- visual.md          # Identidade visual (cross-skill: logo-design-process + brand-book-methodology + paleta-cores-corporativa + tipografia-corporativa)
+-- persona/
|   +-- icp.md             # Ideal Customer Profile (cross-skill: persona-icp-deep)
|   +-- jtbd.md            # Jobs-to-be-Done (cross-skill: persona-icp-deep)
+-- campanhas/
|   +-- README.md          # Lista de campanhas ativas + arquivadas
+-- decisoes/
|   +-- adrs/              # Architecture Decision Records adaptados para marketing
|   |   +-- 0000-template.md
|   +-- log.md             # Log cronologico de decisoes + rationale
+-- entregaveis/
|   +-- copy/              # Pecas de copy (anuncios, posts, landing pages)
|   +-- visual/            # SVGs + imagens + mockups
|   +-- decks/             # Apresentacoes corporativas
|   +-- docs/              # Briefings + relatorios + propostas
+-- pesquisa/
    +-- concorrentes.md    # Cross-skill: competitive-intelligence + analise-concorrencia
    +-- trends.md          # Cross-skill: trendwatching
```

## Workflow de execucao

1. **Verificar pre-existencia**: usar `Glob` em `.frank-mkt/**` para detectar instalacao previa.
   - Se ja existir: perguntar ao usuario se deseja sobrescrever, manter ou abortar. NAO sobrescrever sem confirmacao.
   - Se nao existir: prosseguir.
2. **Capturar nome do cliente**: usar `$ARGUMENTS`. Se vazio, default = `cliente` e avisar.
3. **Criar estrutura de pastas** via `Bash` (mkdir -p) ou `Write` direto (Write cria pastas implicitamente).
4. **Escrever arquivos-esqueleto** preenchendo placeholders `{{NOME_CLIENTE}}` e `{{DATA}}` (data atual ISO 8601).
5. **Reportar estrutura criada** com tree summary + paths absolutos dos arquivos principais.
6. **Sugerir proximos passos**:
   - Invocar `/frank-mkt:perfil` para definir persona/ICP em profundidade.
   - Skill `branding` para foundation (brand DNA + arquitetura).
   - Skill `posicionamento-marca` para POV + diferenciacao.
   - Skill `big-idea` para nucleo unificador da marca.

## Templates dos arquivos

### `.frank-mkt/README.md`

```markdown
# Projeto Frank-MKT — {{NOME_CLIENTE}}

> Estrutura de consultoria de marketing persistida em `.frank-mkt/`.
> Frank-MKT plugin para Claude Code.

## Indice

- `marca/` — Brand DNA, voz, identidade visual
- `persona/` — ICP + Jobs-to-be-Done
- `campanhas/` — Campanhas ativas e arquivadas
- `decisoes/` — ADRs + log cronologico
- `entregaveis/` — Copy, visual, decks, docs
- `pesquisa/` — Concorrentes, trends

## Status

- Cliente/marca: {{NOME_CLIENTE}}
- Inicializado em: {{DATA}}
- Versao plugin: ver CHANGELOG.md do plugin
- Etapa atual: discovery / kickoff

## Como usar

1. Preencher `marca/identidade.md` (skill: branding).
2. Preencher `persona/icp.md` (skill: persona-icp-deep ou comando /frank-mkt:perfil).
3. Documentar decisoes em `decisoes/log.md`.
4. Versionar `.frank-mkt/` no Git do cliente.

## Disclaimer

Conteudo gerado por LLM com apoio do plugin Frank-MKT. Conteudo educational, nao substitui parecer profissional especializado (juridico, contabil, ANVISA, CONAR, LGPD). Validacao humana obrigatoria antes de publicacao.
```

### `.frank-mkt/marca/identidade.md`

```markdown
# Identidade da Marca — {{NOME_CLIENTE}}

> Brand DNA. Cross-skill: branding + posicionamento-marca + big-idea.

## Proposito (Why)

[Por que esta marca existe alem do lucro?]

## Missao (How)

[Como a marca cumpre o proposito no dia a dia?]

## Visao (Where)

[Para onde a marca vai em 3-5 anos?]

## Valores

- Valor 1: [definicao + comportamento observavel]
- Valor 2:
- Valor 3:

## Posicionamento (POV)

- Categoria: [em qual mercado/categoria competimos]
- Publico-alvo: [resumo persona — detalhe em persona/icp.md]
- Promessa unica: [o que so nos entregamos]
- Razao para crer (RTB): [evidencias que sustentam a promessa]

## Big Idea / Nucleo Unificador

[Frase unica que conecta todas as comunicacoes da marca. Cross-skill: big-idea.]

## Arquitetura de marca

- Tipo: [monolitica / endossada / casa-de-marcas / hibrida]
- Sub-marcas / produtos: [se aplicavel]

## Concorrentes diretos

[Lista resumida — detalhe em pesquisa/concorrentes.md]

## Diferenciais defensaveis

1.
2.
3.
```

### `.frank-mkt/marca/voice-tone.md`

```markdown
# Voz e Tom — {{NOME_CLIENTE}}

> Cross-skill: branding + escrita-por-publico + microcopy.

## Voz (constante)

- Personalidade: [3-5 adjetivos]
- Atitude: [especialista / amigo / mentor / desafiador / curador / outro]
- Vocabulario: [registro formal/informal, jargao permitido, palavras-fetiche]

## Tom (varia por contexto)

| Contexto | Tom | Exemplo |
|---|---|---|
| Onboarding | acolhedor | "Que bom ter voce aqui." |
| Erro tecnico | direto + empatico | "Algo deu errado. Tente novamente." |
| Vendas | confiante | "Resolvemos isto desde 20XX." |
| Crise | sobrio + transparente | "Reconhecemos a falha. Plano de acao:" |

## Diretrizes de escrita

- Voz ativa: SIM
- Frases curtas: SIM (max 20 palavras)
- Emojis: [permitidos / proibidos / contextuais]
- CAPS LOCK: [permitido / proibido]
- Pontuacao expressiva (!!!, ???): [politica]

## Palavras a evitar

- [palavra 1] — motivo
- [palavra 2] — motivo

## Frases-assinatura

- "[frase 1]"
- "[frase 2]"
```

### `.frank-mkt/marca/visual.md`

```markdown
# Identidade Visual — {{NOME_CLIENTE}}

> Cross-skill: logo-design-process + brand-book-methodology + paleta-cores-corporativa + tipografia-corporativa + iconografia-corporativa.

## Logo

- Versao principal: [path para SVG em entregaveis/visual/]
- Variacoes: horizontal / vertical / monograma / favicon
- Area de respiro: [X = altura da letra principal]
- Tamanho minimo: [px digital / mm impresso]
- Usos proibidos: [stretch, rotacao, cores nao oficiais, sombra]

## Paleta de cores

| Nome | HEX | RGB | CMYK | Pantone | Uso |
|---|---|---|---|---|---|
| Primaria | #XXXXXX | | | | CTA, links |
| Secundaria | #XXXXXX | | | | apoio |
| Neutra escura | #XXXXXX | | | | texto |
| Neutra clara | #XXXXXX | | | | bg |
| Acento | #XXXXXX | | | | destaque |

## Tipografia

- Fonte primaria: [nome] — usos: titulos
- Fonte secundaria: [nome] — usos: corpo
- Fallbacks web: [stack CSS]
- Hierarquia (H1-H6 + body + caption): [tamanhos + line-height]

## Iconografia

- Estilo: [outline / filled / duotone / hybrid]
- Grid: [24x24 / 32x32]
- Stroke width: [Xpx]

## Imagens / Fotografia

- Estilo: [editorial / corporativo / lifestyle / abstrato]
- Tratamento: [color grading / B&W / duotone]
- Bibliotecas autorizadas: [Unsplash / Pexels / banco proprio]

## Aplicacoes

- Web: [link CSS tokens]
- Apresentacoes: [link template em entregaveis/decks/]
- Impressos: [link template em entregaveis/visual/]
```

### `.frank-mkt/persona/icp.md`

```markdown
# ICP — Ideal Customer Profile — {{NOME_CLIENTE}}

> Cross-skill: persona-icp-deep. Para deep dive use /frank-mkt:perfil.

## Persona principal: [Nome ficticio]

### Demografia

- Idade:
- Genero:
- Localizacao:
- Renda:
- Estado civil:
- Escolaridade:

### Profissional (B2B/B2C)

- Cargo / ocupacao:
- Segmento / setor:
- Tamanho da empresa:
- Tempo de carreira:

### Psicografia

- Valores:
- Aspiracoes:
- Medos:
- Frustracoes:

### Comportamento digital

- Plataformas que frequenta:
- Conteudo que consome:
- Influenciadores que segue:
- Horarios de atividade:

### Dores principais

1.
2.
3.

### Objecoes a venda

1.
2.
3.

### Gatilhos de decisao

- Racionais:
- Emocionais:

## Anti-persona

[Quem NAO eh nosso cliente — para focar discovery]
```

### `.frank-mkt/persona/jtbd.md`

```markdown
# Jobs-to-be-Done — {{NOME_CLIENTE}}

> Cross-skill: persona-icp-deep + funil-jornada.

## Job principal

> "Quando [situacao], eu quero [motivacao], para que eu possa [resultado esperado]."

[Preencher]

## Jobs funcionais

1.
2.
3.

## Jobs emocionais

1.
2.
3.

## Jobs sociais

1.
2.

## Forces of Progress

- **Push** (o que empurra para mudanca): [insatisfacao com status quo]
- **Pull** (o que atrai a solucao): [beneficio percebido]
- **Anxiety** (o que gera medo da nova solucao): [risco percebido]
- **Habit** (o que prende ao comportamento atual): [inercia / custos de troca]

## Solucoes contratadas hoje (concorrencia ampla)

- Direta: [produto X]
- Indireta: [solucao Y caseira / planilha / nao-consumo]
```

### `.frank-mkt/campanhas/README.md`

```markdown
# Campanhas — {{NOME_CLIENTE}}

## Ativas

| ID | Nome | Objetivo | Periodo | Owner | Status |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

## Arquivadas

| ID | Nome | Periodo | Resultado | Aprendizados |
|---|---|---|---|---|
|  |  |  |  |  |

## Estrutura por campanha

Para cada campanha, criar pasta `campanhas/<id-slug>/` com:

- `brief.md` — objetivo, KPI, publico, big idea, peca-chave
- `plano.md` — canais, cronograma, orcamento
- `criativos/` — copy + visual
- `resultados.md` — metricas + retro

> Cross-skill: metricas-marketing + funil-jornada + go-to-market-strategy.
```

### `.frank-mkt/decisoes/log.md`

```markdown
# Log de Decisoes — {{NOME_CLIENTE}}

> Cronologico. Decisoes estruturais (estrategia, posicionamento, big idea, arquitetura de marca) viram ADR em `decisoes/adrs/`.

## {{DATA}} — Inicializacao do projeto

- **Decisao**: Adotar estrutura `.frank-mkt/` para persistir contexto da consultoria.
- **Rationale**: Continuidade entre sessoes, fonte unica de verdade, versionavel em Git.
- **Alternativas consideradas**: docs soltos / Notion / Confluence.
- **Trade-offs**: requer Git + Markdown literacy do time.
- **Owner**: [nome]

---

## [Data] — [Titulo da decisao]

- **Decisao**:
- **Rationale**:
- **Alternativas consideradas**:
- **Trade-offs**:
- **Owner**:
```

### `.frank-mkt/decisoes/adrs/0000-template.md`

```markdown
# ADR-0000 — [Titulo curto da decisao]

- **Status**: proposto / aceito / depreciado / substituido por ADR-XXXX
- **Data**: AAAA-MM-DD
- **Owner**: [nome]
- **Contexto-skill**: [skill(s) Frank-MKT envolvidas]

## Contexto

[Qual problema/situacao motivou esta decisao? Restricoes? Hipoteses?]

## Decisao

[O que foi decidido, em frase ativa.]

## Consequencias

### Positivas

-
-

### Negativas / Trade-offs

-
-

### Riscos

-

## Alternativas consideradas

### Alternativa A
- Pros:
- Contras:
- Por que NAO foi escolhida:

### Alternativa B
- Pros:
- Contras:
- Por que NAO foi escolhida:

## Referencias

- [link / arquivo / skill]
```

### `.frank-mkt/pesquisa/concorrentes.md`

```markdown
# Pesquisa de Concorrentes — {{NOME_CLIENTE}}

> Cross-skill: competitive-intelligence + analise-concorrencia + white-space-analysis.

## Concorrentes diretos

| Nome | Site | Posicionamento declarado | Publico | Faixa de preco | Diferencial percebido | Pontos fracos |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

## Concorrentes indiretos / substitutos

| Nome | Por que compete | Risco |
|---|---|---|

## Mapa de posicionamento

[2 eixos relevantes — preco vs qualidade, tradicional vs disruptivo, etc. Plotar concorrentes e nos.]

## White space identificado

[Cross-skill: white-space-analysis. Onde existe espaco nao ocupado?]

## Aprendizados aplicaveis

1.
2.

## Atualizacao

- Ultima revisao: {{DATA}}
- Proxima revisao: [data]
```

### `.frank-mkt/pesquisa/trends.md`

```markdown
# Pesquisa de Trends — {{NOME_CLIENTE}}

> Cross-skill: trendwatching + newsjacking-real-time.

## Macro trends (3-5 anos)

| Trend | Fonte | Impacto na marca | Janela de oportunidade |
|---|---|---|---|
|  |  |  |  |

## Micro trends (3-12 meses)

| Trend | Fonte | Acao sugerida | Risco de fadiga |
|---|---|---|---|

## Sinais fracos a monitorar

-
-

## Newsjacking — eventos previsiveis

| Evento | Data | Angulo da marca |
|---|---|---|

## Atualizacao

- Ultima revisao: {{DATA}}
- Cadencia recomendada: mensal
```

### Pastas vazias

Para `entregaveis/copy/`, `entregaveis/visual/`, `entregaveis/decks/`, `entregaveis/docs/`, criar arquivo `.gitkeep` vazio em cada uma para garantir versionamento.

## Argumentos

- `$ARGUMENTS` = nome do cliente/marca (opcional).
- Se vazio: usar literal `cliente` como `{{NOME_CLIENTE}}` e avisar usuario para editar manualmente o `README.md` da estrutura.
- Sanitizar: aceitar caracteres ASCII + espacos. Slug de pasta nao eh necessario — `.frank-mkt/` eh fixo.

## Comportamentos especiais

- **Idempotencia**: se `.frank-mkt/` ja existir e usuario pedir para manter, NAO criar nada. Se pedir merge, criar so arquivos faltantes (preservar existentes).
- **Validacao de path**: confirmar que cwd nao eh raiz de disco nem pasta de sistema antes de criar.
- **Encoding**: UTF-8 sem BOM. ASCII PT-BR (sem acentos) no conteudo dos templates.
- **Linha final**: cada arquivo termina com `\n`.

## Cross-skill suggestions (output final do comando)

Apos criar a estrutura, exibir ao usuario:

```
Estrutura .frank-mkt/ inicializada para {{NOME_CLIENTE}}.

Proximos passos sugeridos:
1. /frank-mkt:perfil           — definir persona/ICP em profundidade
2. skill: branding             — preencher marca/identidade.md
3. skill: posicionamento-marca — refinar POV + diferenciacao
4. skill: big-idea             — nucleo unificador da marca
5. skill: persona-icp-deep     — aprofundar persona/icp.md + jtbd.md
6. skill: competitive-intelligence — alimentar pesquisa/concorrentes.md

Versionar .frank-mkt/ no Git do cliente para preservar historico de decisoes.
```

## Disclaimer educacional

Este comando cria templates de consultoria de marketing. Conteudo gerado por LLM e templates do plugin Frank-MKT sao educacionais. NAO substituem parecer profissional especializado (juridico, contabil, ANVISA, CONAR, LGPD, regulacao setorial). Antes de publicar qualquer entregavel derivado desta estrutura: revisao humana obrigatoria por profissional habilitado da area aplicavel. O plugin nao se responsabiliza por uso indevido, alegacoes nao comprovadas ou descumprimento regulatorio.
