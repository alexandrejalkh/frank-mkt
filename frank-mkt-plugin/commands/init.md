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
|   +-- identidade-visual.md  # DOC MESTRE de identidade visual: cores + tipografia + iconografia + logo + formas + estilo fotografico + ilustracao + animacao + aplicacoes + decisoes (cross-skill: 8 skills Bloco Brand Design + atelier-criativo agente)
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

- `marca/`
  - `identidade.md` — Brand DNA + posicionamento + big idea
  - `voice-tone.md` — Voz + tom de marca
  - `identidade-visual.md` — **DOC MESTRE de design**: cores + tipografia + iconografia + logo + formas + estilo fotografico + ilustracao + animacao + aplicacoes + decisoes
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

1. Preencher `marca/identidade.md` (skill: branding + posicionamento-marca + big-idea).
2. Preencher `persona/icp.md` (skill: persona-icp-deep ou comando /frank-mkt:perfil).
3. **Construir `marca/identidade-visual.md` ao longo do projeto** (atualizar a cada decisao de design via agente atelier-criativo + 8 skills Bloco Brand Design).
4. Documentar decisoes em `decisoes/log.md` com rationale.
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

### `.frank-mkt/marca/identidade-visual.md`

> DOC MESTRE de identidade visual. Tudo decidido sobre design grafico vai para ca. Atualizado por: agente `atelier-criativo` (visao + sintese), 8 skills Bloco Brand Design (rigor tecnico), agente `frank-corporativo` (compliance institucional). Uma fonte unica de verdade — quando algo muda, atualizar este arquivo + adicionar entrada em `decisoes/log.md` com rationale.

```markdown
# Identidade Visual — {{NOME_CLIENTE}}

> Documento mestre. Cross-skill: logo-design-process + brand-book-methodology + paleta-cores-corporativa + tipografia-corporativa + iconografia-corporativa + print-papelaria-collateral + apresentacoes-decks-corporativos + templates-corporativos-comerciais + svg-engineering-ia + composicao-visual + agente atelier-criativo.

**Status**: [discovery | concept | refining | approved | production]
**Ultima atualizacao**: {{DATA}}
**Owner**: [brand designer / atelier-criativo / aprovador final]
**Versao**: v0.1.0 (incrementar a cada mudanca substantiva)

---

## 1. Visao estetica + filosofia (atelier-criativo)

> Antes de qualquer especificacao tecnica, capturar **a posicao estetica defendida**.

- **Posicao estetica em 1 frase**: [ex: "rigor de grid Vignelli + paleta tropical Tarsila aplicada com restricao"]
- **Referencias cross-domain** (3-5 de dominios diferentes):
  - Designer/movimento: [ex: Massimo Vignelli — minimalismo italiano]
  - Cinema: [ex: Wong Kar-wai — cor saturada lirica]
  - Musica: [ex: Tom Jobim — sintese sofisticada]
  - Arquitetura: [ex: Lina Bo Bardi — popular elevado]
  - Brasil: [ex: Tarsila — modernismo antropofagico]
- **Subtexto emocional**: [o que cliente sente ao ver/usar o material]
- **Anti-AI-slop checklist**: [Evitamos: gradiente neon generico? sem-serif arredondada padrao? simetria perfeita calma?]

---

## 2. Logo

> Cross-skill: logo-design-process. Arquivos finais em `entregaveis/visual/logo/`.

### Versoes
- Principal (color): [path .svg + .pdf + .eps + .png 512px]
- Horizontal: [path]
- Vertical: [path]
- Monograma/icone: [path]
- Favicon (16/32/64px): [path]
- Monocromatico positivo (preto): [path]
- Monocromatico negativo (branco): [path]
- Reverso (sobre fundo escuro): [path]

### Especificacoes tecnicas
- **Construcao**: [grid + proporcoes baseadas em X = altura letra principal]
- **Area de respiro minima**: [X em todas direcoes]
- **Tamanho minimo digital**: [Xpx — abaixo disto nao usar]
- **Tamanho minimo impresso**: [Xmm]
- **Cores tecnicas**: [HEX + Pantone + CMYK declarados em secao 3]

### Don'ts (5-7 violacoes proibidas)
1. Stretch horizontal/vertical
2. Rotacao alem de 90/180/270 graus
3. Aplicacao de sombra/contorno/gradiente nao especificados
4. Substituicao de cores fora da paleta oficial
5. Aplicacao sobre fundo de baixo contraste (<4.5:1 WCAG AA)
6. [adicionar conforme caso]

---

## 3. Paleta de cores

> Cross-skill: paleta-cores-corporativa. WCAG 2.2 contrast 4.5:1 AA / 7:1 AAA.

### Paleta principal

| Nome semantico | HEX | RGB | CMYK | Pantone | OKLCH | Uso |
|----------------|-----|-----|------|---------|-------|-----|
| Primary | #XXXXXX | r,g,b | c,m,y,k | XXX C | L% C h | CTA, links, destaque |
| Primary-dark | #XXXXXX | | | | | hover, active |
| Primary-light | #XXXXXX | | | | | bg subtil |
| Secondary | #XXXXXX | | | | | apoio narrativo |
| Accent | #XXXXXX | | | | | acento isolado |

### Neutros

| Nome | HEX | Uso |
|------|-----|-----|
| Black-95 (texto principal) | #0A0A0A | corpo de texto |
| Gray-70 (texto secundario) | #4A4A4A | metadata, captions |
| Gray-40 (borders) | #B0B0B0 | divisores, borders |
| Gray-15 (bg subtle) | #E8E8E8 | bg alternativo |
| White (bg principal) | #FFFFFF | bg primario |

### Cores semanticas (UI)

| Token | HEX | Uso |
|-------|-----|-----|
| Success | #XXXXXX | confirmacao, validacao |
| Warning | #XXXXXX | atencao, alerta leve |
| Error | #XXXXXX | erro critico, recusa |
| Info | #XXXXXX | informacao neutra |

### Dark mode

| Token | Light HEX | Dark HEX |
|-------|-----------|----------|
| bg-primary | #FFFFFF | #0A0A0A |
| text-primary | #0A0A0A | #F5F5F5 |
| Primary | #XXXXXX | #XXXXXX (ajustado) |
| ... | | |

### WCAG contrast ratios validados

| Combinacao | Ratio | Nivel |
|------------|-------|-------|
| Black-95 sobre White | 19:1 | AAA |
| Primary sobre White | X:1 | [AA / AAA] |
| White sobre Primary | X:1 | [AA / AAA] |
| Gray-70 sobre White | X:1 | [AA / AAA] |

### Cultural meaning + rationale
- **Por que esta paleta**: [argumento estetico defendido — ex: "primary roxo profundo evoca autoridade Itau ao mesmo tempo modernidade Nubank, sem cair no cliche de nenhum dos dois"]
- **Cores explicitamente evitadas**: [ex: "verde-amarelo bandeira generico", "purple Nubank exato", "orange Itau exato"]

---

## 4. Tipografia

> Cross-skill: tipografia-corporativa. Licenciamento + fallbacks + variable fonts.

### Familias

| Funcao | Fonte | Variantes usadas | Licenca | Fallback web |
|--------|-------|------------------|---------|--------------|
| Display | [nome] | Light/Regular/Bold | [Google Fonts free / Adobe Fonts / Custom] | system-ui, -apple-system, sans-serif |
| Heading | [nome] | Regular/Bold | | |
| Body | [nome] | Regular/Italic/Bold | | |
| Mono (codigo) | [nome] | Regular | | ui-monospace, monospace |

### Hierarquia (modular scale)

| Token | Tamanho | Line-height | Tracking | Peso | Uso |
|-------|---------|-------------|----------|------|-----|
| display | 64px | 1.05 | -0.02em | 700 | hero |
| h1 | 48px | 1.1 | -0.01em | 700 | titulo principal |
| h2 | 36px | 1.15 | -0.005em | 600 | secao |
| h3 | 28px | 1.2 | 0 | 600 | subsecao |
| h4 | 22px | 1.3 | 0 | 500 | bloco |
| body-lg | 18px | 1.6 | 0 | 400 | leitura confortavel |
| body | 16px | 1.6 | 0 | 400 | corpo padrao |
| caption | 14px | 1.5 | 0.01em | 400 | metadata |
| small | 12px | 1.5 | 0.02em | 400 | legendas, footer |

### Decisoes tipograficas
- **Por que esta combinacao**: [argumento — ex: "Inter Variable porque suporta acentos pt-BR perfeitamente + variable axes para fluidez + open-source (zero custo licenca)"]
- **Tipografia explicitamente evitada**: [ex: "sans-serif arredondada padrao AI-slop tipo Plus Jakarta sem motivo"]

---

## 5. Iconografia

> Cross-skill: iconografia-corporativa + svg-engineering-ia. Sistema consistente.

- **Estilo**: [outline / filled / duotone / hybrid]
- **Grid base**: [24x24 / 32x32 px]
- **Stroke weight**: [1.5px / 2px / 2.5px] (consistente em todo set)
- **Cantos**: [round / sharp / hybrid] — radius [Xpx]
- **Library base** (se aplicavel): [Lucide / Heroicons / Phosphor / Tabler / custom]
- **Custom set count**: [N icones proprios alem da library]
- **Path**: [`entregaveis/visual/icons/`]
- **Distribuicao**: [npm package / Figma library / static SVG files]

### Exemplos de aplicacao
- Botao primary com icone left: [path icone + tamanho]
- Botao icon-only: [tamanho minimo touch target 44x44]
- Icone em texto (inline): [tamanho 1em + alinhamento baseline]

---

## 6. Formas + motivos visuais

> Linguagem geometrica recorrente — alem de logo+icones. NOVO em 2026 — patterns estao voltando.

- **Forma assinatura** (se houver): [ex: arco curvo Niemeyer + linha Vignelli combinados em motivo proprio]
- **Padroes geometricos**: [path para SVG]
- **Texturas**: [aplicacao + uso]
- **Grid de pagina**: [12 colunas web / 6 mobile / margens / gutters]
- **Proporcoes**: [golden ratio / regra dos tercos / modular scale 1.25x / 1.333x / 1.5x]

---

## 7. Estilo fotografico

> Cross-skill: composicao-visual + geracao-imagens-ia.

- **Direcao geral**: [editorial / corporativo / lifestyle / abstrato / documental]
- **Color grading**: [warm / cool / desaturated / saturated / B&W / duotone]
- **Composicao tipica**: [centro / regra dos tercos / simetrica / assimetrica]
- **Iluminacao**: [natural / studio / golden hour / dramatica chiaroscuro]
- **People**: [diversidade obrigatoria + faixas etarias + contextos]
- **Objetos**: [estilo + ambiente]
- **Bibliotecas autorizadas**: [Unsplash / Pexels / Getty / banco proprio cliente]
- **Bibliotecas proibidas**: [stock photo generico AI-gerado]
- **AI generation policy**: [Midjourney v6+ permitido / DALL-E 3 OK / proibido para faces humanas reais]

---

## 8. Estilo ilustrativo

- **Tipo**: [flat / 3D isometrico / line art / collage / hand-drawn / vector minimal]
- **Paleta usada em ilustracao**: [paleta principal / variacao com cores adicionais / monocromatica]
- **Personagens**: [estilo + diversidade + traços]
- **Cenarios**: [abstrato / realista / hibrido]
- **Inspiracao**: [referencias declaradas]
- **Path**: [`entregaveis/visual/illustrations/`]

---

## 9. Movimento + animacao

> Cross-skill: composicao-visual + audio-musica-ia (sonic branding). NAO usar SMIL — use CSS/GSAP.

- **Tipo**: [GSAP / CSS animations / Framer Motion / Lottie]
- **Easing padrao**: [cubic-bezier(0.4, 0.0, 0.2, 1) — Material standard / custom]
- **Duracoes**: [microinteracao 150ms / transicao 300ms / hero 600-1000ms]
- **Mood**: [snappy / smooth / bouncy / linear classico]
- **Sonic branding** (se aplicavel): [logo audio + microsounds UI]

---

## 10. Aplicacoes

> Como a identidade vive em cada medium. Cross-skill: print-papelaria-collateral + apresentacoes-decks-corporativos + templates-corporativos-comerciais.

### Web
- **CSS tokens**: [path tokens.css ou design-tokens.json]
- **Sistema componentes**: [Storybook / Figma library / custom]
- **Responsive breakpoints**: [mobile <640 / tablet 640-1024 / desktop >1024]

### Apresentacoes
- **Master slides**: [path em `entregaveis/decks/`]
- **Templates**: [pitch / sales / investor / board / training]
- **Plataforma**: [PowerPoint / Keynote / Google Slides / Pitch.com / Tome]

### Impressos
- **Cartao visita**: [path artwork em `entregaveis/visual/print/`]
- **Papel timbrado**: [path]
- **Folder/flyer/banner**: [paths]
- **Especificacoes producao**: [bleed 3mm + safety + CMYK + 300dpi + paper Couche/Triplex]

### Sinalizacao (se aplicavel)
- **Interna/externa**: [especificacoes]
- **ABNT NBR 9050 + 16537** compliance: [LBI Brasil — sinalizacao tatil, braille, altura]

### Email
- **Signature HTML**: [path template]
- **Newsletter template**: [path]

### Brindes corporativos
- **Itens**: [caneta / caneca / camiseta / squeeze / eco-friendly]
- **Aplicacao logo**: [posicao + tamanho + tecnica de impressao]

### Social media
- **Templates por plataforma**: [path em `entregaveis/visual/social/`]
- **Formatos**: [LinkedIn 1200x627, Instagram 1080x1080/1080x1920, Facebook 1200x630]

---

## 11. Decisoes + rationale (log de evolucao)

> Toda mudanca neste documento tambem deve ter entrada em `decisoes/log.md` com argumento estetico.

| Data | Decisao | Rationale | Quem aprovou |
|------|---------|-----------|--------------|
| {{DATA}} | Inicializacao do documento | Setup inicial via /frank-mkt:init | sistema |
| | | | |

---

## 12. Versionamento

- **v0.1.0** ({{DATA}}): documento criado, esqueleto preenchido com placeholders
- **v0.2.0** (a definir): primeira definicao de paleta + tipografia + logo concept
- **v1.0.0** (a definir): aprovado para producao + brand book exportado

---

## Disclaimer

Conteudo gerado por LLM com apoio do plugin Frank-MKT (skills Brand Design + agente atelier-criativo). Conteudo educational, nao substitui designer humano senior em projeto comercial seria. Validacao humana obrigatoria antes de publicacao. Cross-skill complementar: logo-design-process + brand-book-methodology + paleta-cores-corporativa + tipografia-corporativa + iconografia-corporativa + print-papelaria-collateral + apresentacoes-decks-corporativos + templates-corporativos-comerciais + svg-engineering-ia + composicao-visual + geracao-imagens-ia + audio-musica-ia + acessibilidade-wcag + branding + posicionamento-marca + big-idea + agente atelier-criativo + agente frank-corporativo.
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
