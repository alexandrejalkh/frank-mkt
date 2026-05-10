# Frank MKT — Plugin Claude Code

Consultor de Marketing, SEO, Mídias Sociais, Inteligência de Mercado e **arte digital generalista** que opera como plugin do Claude Code. Persona unificada com motor cognitivo, Contraditório Interno obrigatório, Perfilador de Mercado e skills com decaimento temporal. Foco Brasil 2026 (LGPD + CONAR + CDC + cultura tropicalizada). Inclui agente `atelier-criativo` que combate AI-slop estético via síntese de história da arte em voz própria.

> **Status v2.35.0 — 2026-05-10 — 🚀 PLUGIN COMPLETO + EXPANDIDO**
>
> **116 artefatos / 119.737+ linhas totais**:
> - ✅ **92 skills** em **18 blocos completos** (107.548 linhas)
> - ✅ **9 slash commands** (3.752 linhas — `init` + `stack` + `save-session` + `help` + `audit` + `review` + `juiz` + `perfil` + `atelier` ✨)
> - ✅ **15 agentes especialistas** (8.437 linhas — incluindo **`atelier-criativo`** ✨ artista digital generalista anti-AI-slop)
>
> **Volatility distribution**:
> - **24 skills `high`** (re-validar 3 meses) — plataformas Meta/Google/LinkedIn, GA4, Search Console, CONAR/CDC, tendências
> - **61 skills `medium`** (re-validar 6 meses) — frameworks, métricas, copy de plataforma, brand-design
> - **7 skills `low`** (re-validar 12 meses) — metodologias, psicologia, princípios UX
>
> Roadmap completo: [`docs_mkt/ROADMAP-FRANK-MKT.md`](docs_mkt/ROADMAP-FRANK-MKT.md). Histórico completo: [`frank-mkt-plugin/CHANGELOG.md`](frank-mkt-plugin/CHANGELOG.md).

## Novidades v2.33.0 → v2.35.0

### ✨ Agente `atelier-criativo` (v2.33.0)
**Quebra do paradigma "IA boa em código, fraca em arte"**. Artista digital generalista que estuda história da arte (mestres internacionais + Brasil tropical + cinema + música + arquitetura + literatura), sintetiza em voz própria emergente, defende posição estética com argumento. **SVG é apenas um pincel** — agente decide *o que* criar; skills executam *como*.

- 8 princípios fundamentais (síntese > cópia, posição > neutralidade covarde, AI-slop = inimigo declarado)
- Sinestesia ativa: música → quadro, palavra → forma, número → cor
- Processo 7 etapas: Listening → Resonance → Cross-pollination → Tension → Synthesis → Translation → Iteration
- Anti-pattern AI-slop firme (recusa gradiente neon genérico + sem-serif arredondada padrão + simetria perfeita morta)
- Cross-domain: combina Vignelli + Tarsila + Wong Kar-wai + Tom Jobim + Niemeyer em propostas autorais

### ✨ Slash command `/frank-mkt:atelier` (v2.34.0)
Invocação direta do atelier-criativo sem depender de delegação. Brief criativo aberto + foco opcional (`narrativa` / `tom` / `visual` / `sinestesia` / `tension` / `defesa`).

### ✨ Doc mestre `identidade-visual.md` (v2.35.0)
Quando `/frank-mkt:init` cria estrutura `.frank-mkt/`, agora gera **`marca/identidade-visual.md`** com **12 seções estruturadas** capturando todas as decisões de design grafico em arquivo único versionado:

1. Visão estética + filosofia (atelier-criativo) — posição defendida + cross-domain refs + anti-AI-slop checklist
2. Logo — 8 versões + especificações + don'ts
3. Paleta de cores — primária + neutros + semântica + dark mode + WCAG ratios + OKLCH + Pantone + cultural meaning
4. Tipografia — famílias + 9 tokens hierarquia + licenciamento + variable fonts
5. Iconografia — sistema + grid + library + npm distribution
6. Formas + motivos visuais — linguagem geométrica
7. Estilo fotográfico — direção + grading + AI policy
8. Estilo ilustrativo — tipo + paleta + path
9. Movimento + animação — easing + durações + sonic branding
10. Aplicações — web + decks + impressos + sinalização ABNT/LBI + email + brindes + social
11. Decisões + rationale — log de evolução com argumento estético
12. Versionamento semver do documento

Atelier-criativo lê este doc antes de propor (não quebra coerência) e atualiza ao decidir algo (decisões não evaporam entre sessões).

## Instalação

Guia completo: [`docs_mkt/INSTALACAO.md`](docs_mkt/INSTALACAO.md)

```powershell
# 1. Adicionar marketplace
claude plugin marketplace add https://github.com/alexandrejalkh/frank-mkt.git

# 2. Instalar plugin
claude plugin install frank-mkt --scope project

# 3. Abrir Claude Code
claude

# 4. Inicializar caso/cliente
/frank-mkt:init [nome-cliente]
```

**Verificação**: dentro do Claude Code, rode `/frank-mkt:help` — deve listar **9 commands + 15 agentes + 92 skills**.

### Re-instalação após updates

`marketplace remove` desinstala o plugin junto. Após adicionar marketplace de volta, use **`install`** (não `update`):

```powershell
# 1. Remover marketplace antigo (desinstala plugin)
claude plugin marketplace remove frank-mkt

# 2. Adicionar marketplace atualizado
claude plugin marketplace add https://github.com/alexandrejalkh/frank-mkt.git

# 3. INSTALL (não update — plugin foi desinstalado)
claude plugin install frank-mkt --scope project
```

`update` só funciona se plugin **já estiver instalado**. Após `marketplace remove`, sempre `install`.

## O que o Frank-MKT faz

- **Persona unificada de marketing & inteligência de mercado** — fala a língua do CMO, fundador, head de growth, CHRO, social media, redator, designer, brand designer, analista de pesquisa, IR, ESG officer.
- **Motor cognitivo com fases** — leitura do interlocutor, perfilamento de mercado/persona, custo-benefício de canal/mensagem, construção de conceito/copy/plano, contraditório interno.
- **Visão estética defendida** (via `atelier-criativo`) — combate AI-slop, síntese de história da arte em voz própria, sinestesia entre domínios.
- **Cristal C0 "NÃO CHUTAR"** — regra imutável: não apresentar suposição (de mercado, público, número) como fato. Na dúvida, pergunta ou pesquisa.
- **Contraditório Interno** — checklist de 10 perguntas obrigatório em toda análise de campanha, posicionamento ou peça relevante.
- **Decaimento temporal** — skills volúveis (algoritmos plataforma, regulação, tendências) reavaliadas a cada 3 meses; metodologias estáveis a cada 12 meses.
- **Brasil-first** — LGPD/CONAR/CDC/CVM/ANPD compliance embutido + cases nacionais (Magalu, Nubank, Itaú, iFood, Stone, Pipefy, RD Station) + ferramentas tropicalizadas (Pix, ClickSign, RD Station, Gupy).
- **Memória persistente** — `.frank-mkt/` preserva cliente, marca, persona, voz, **identidade visual completa** (doc mestre 12 seções), decisões e histórico de campanhas.

## 18 Blocos de Skills (92/92 implementadas)

| Bloco | Skills | Linhas | Volatility típica |
|-------|-------:|-------:|-------------------|
| **SEO Estendido** | 7 | 9.853 | medium-high |
| **Mídia Social** | 10 | 10.962 | high |
| **Comunicação Visual & IA** | 4 | 5.197 | medium |
| **Multi-Platform Strategy** | 3 | 4.344 | medium-low |
| **Persuasão & Engajamento** | 2 | 2.827 | low-medium |
| **Marketing Não-Tradicional** | 2 | 2.642 | medium |
| **Marketing & Estratégia (1º lote)** | 5 | 7.871 | low-medium |
| **Domínio Vertical (Bloco F EXPANDIDO)** | 13 | 18.856 | medium |
| **Documentos Corporativos** | 2 | 1.947 | medium |
| **Pesquisa & Inteligência de Mercado** | 6 | 4.338 | medium |
| **Corporativo & Humanitário** | 6 | 5.462 | medium |
| **Copy & Redação** | 4 | 6.085 | medium |
| **UX/UI** | 4 | 4.714 | medium |
| **Psicologia & Influência** | 3 | 2.970 | medium |
| **Conhecimento de Plataforma** | 6 | 5.627 | **high (3m)** |
| **Meta-skill** | 1 | 958 | medium |
| **Marketing & Estratégia (2º lote)** | 5 | 4.555 | medium |
| **Skills Avançadas / Experimentais** | 1 | 1.234 | medium |
| **Identidade Visual Corporativa / Brand Design** | 8 | 7.106 | medium |
| **TOTAL** | **92** | **107.548** | |

INDEX completo de todas as skills com volatility, linhas e cross-references: [`frank-mkt-plugin/skills/INDEX.md`](frank-mkt-plugin/skills/INDEX.md).

## 9 Slash Commands

| Comando | Linhas | Função |
|---------|-------:|--------|
| `/frank-mkt:init` | 803 | Configura `.frank-mkt/` cliente — estrutura marca + persona + campanhas + decisões + entregáveis + pesquisa. **Inclui doc mestre `identidade-visual.md` (12 seções)** ✨ |
| `/frank-mkt:stack` | 348 | Estado atual do projeto (marca + persona + campanhas + decisões + entregáveis recentes) |
| `/frank-mkt:save-session` | 359 | Log estruturado da sessão em `.frank-mkt/sessoes/` |
| `/frank-mkt:help` | 404 | Menu navegável: 9 commands + 15 agentes + 92 skills agrupadas |
| `/frank-mkt:audit` | 467 | Varredura mecânica PASS/FAIL (7 tipos peça: copy/post/landing/briefing/plano-mídia/deck/email) |
| `/frank-mkt:review` | 509 | Review qualitativo multi-agent (narrativa + execução + arbitragem) |
| `/frank-mkt:juiz` | 439 | Arbitra divergência entre agentes (6 critérios hierárquicos) |
| `/frank-mkt:perfil` | 444 | Perfilador de Mercado: TAM/SAM/SOM + ICP + concorrência + white-space + trends |
| **`/frank-mkt:atelier`** ✨ | 223 | **Atelier criativo: artista digital generalista (visão estética + sinestesia entre domínios + anti-AI-slop)** |

## 15 Agentes Especialistas

| Agente | Modelo | Função |
|--------|--------|--------|
| `frank-mkt` | opus | **Persona principal** — orquestra 92 skills + 14 agentes + 9 commands |
| **`atelier-criativo`** ✨ | opus | **Artista digital generalista** — visão estética + sinestesia entre domínios + síntese de mestres em voz própria. SVG é apenas um pincel. Anti-AI-slop firme |
| `juiz` | opus | Arbitrador imparcial — 6 critérios hierárquicos (compliance > ética > estratégia > evidência > audiência > custo-benefício) |
| `auditor` | sonnet | Varredura mecânica PASS/FAIL — 7 checklists, 3 níveis severidade |
| `investigador` | sonnet | Entrevista estruturada interlocutor — 5 blocos de perguntas |
| `perfilador-mercado` | opus | Análise mercado 5 frentes — sizing + ICP + concorrência + white-space + trends |
| `redator-hacker` | opus | Copy alta conversão **ANTI-dark-pattern** — Schwartz/Cialdini/Ogilvy/Maccedo/Iuri Jobim |
| `seo-strategist` | opus | SEO + GEO 2026 (80% B2B discovery via AI engines) + Core Web Vitals INP |
| `social-media-linkedin` | opus | B2B + Lead Gen Forms 6.1% CVR + TLAs 6x CTR + Buying Group Targeting |
| `social-media-instagram` | opus | Reels-first 2026 + Brasil micro-influência #1 + CTWA |
| `social-media-facebook` | sonnet | Audiência 35-65 + Groups + Marketplace + CAPI iOS 14.5+ |
| `ux-ui-revisor` | opus | Nielsen 10 + WCAG 2.2 (9 novos critérios) + Core Web Vitals + Brasil LBI |
| `psicologia-influencia` | opus | Cialdini 7 + Kahneman + **ANTI-dark-pattern firme** (Brignull 16 + EU DSA) |
| `frank-corporativo` | opus | PESO + GEO + IR + ESG + Crisis + Employer Branding + ABERJE/ABRACOM |
| `social-humanitario` | opus | Causas + ESG + AA1000 + SROI + Brasil ABONG/GIFE/Pacto Global ONU + ANTI-greenwashing |

## Cross-Skill Orchestration

Frank-MKT invoca skills + agentes automaticamente baseado no contexto. Exemplos de fluxos típicos:

### Fluxo "Lançamento B2B SaaS Brasil" (estratégico-tático)
```
Cliente: "Preciso lançar produto B2B SaaS no Brasil"

Frank-MKT invoca em ordem:
1. /frank-mkt:init → cria .frank-mkt/ + identidade-visual.md
2. agente investigador → entrevista 5 blocos
3. /frank-mkt:perfil "B2B SaaS Brasil" → perfilador-mercado
4. skill branding → archetype + voice + brand DNA
5. skill posicionamento-marca → STP + Trout & Ries POV
6. skill big-idea → núcleo unificador + tagline
7. skill go-to-market-strategy → PLG/SLG/CLG motion
8. skill copywriting-conversao → headlines + CTAs
9. skill linkedin-organico → conteúdo orgânico B2B
10. skill conhecimento-linkedin-ads → Lead Gen Forms + ABM
11. /frank-mkt:audit → varredura mecânica PASS/FAIL
12. /frank-mkt:review → review qualitativo multi-agent
13. /frank-mkt:save-session → log estruturado
```

### Fluxo "Identidade visual com alma" (estratégico-criativo)
```
Cliente: "Crie identidade visual que tenha alma, não pareça AI-slop"

Frank-MKT invoca em ordem:
1. /frank-mkt:init → cria .frank-mkt/ + identidade-visual.md (esqueleto 12 seções)
2. agente investigador → entrevista 5 blocos (marca + produto + persona)
3. skill branding → foundation (archetype + voz)
4. skill posicionamento-marca → POV
5. skill big-idea → núcleo
6. /frank-mkt:atelier "<brief>" → atelier-criativo executa processo 7 etapas:
   - Listening profundo → identifica subtexto
   - Resonance → ressoa cross-domain
   - Cross-pollination → 3-5 referências (Vignelli + Tarsila + Tom Jobim + Lina Bo Bardi + Wong Kar-wai)
   - Tension → 3 visões antagônicas
   - Synthesis → defende UMA com argumento estético
   - Translation → invoca skills (logo-design-process + paleta-cores-corporativa + tipografia-corporativa + iconografia-corporativa + svg-engineering-ia)
   - Iteration → preserva voz, evolui visão
   - **Persiste decisões em identidade-visual.md** (não evaporam entre sessões)
7. skill brand-book-methodology → manual identidade exportável
8. skill print-papelaria-collateral → papelaria + sinalização ABNT/LBI
9. skill apresentacoes-decks-corporativos → master slides
10. /frank-mkt:audit → compliance WCAG + LGPD
11. /frank-mkt:review → review qualitativo (atelier + ux-ui-revisor + auditor + juiz)
```

## Decaimento Temporal

Toda skill declara no frontmatter YAML:

```yaml
volatility: high | medium | low
last_review: 2026-05-10
next_review: 2026-08-10  # = 3 meses se high, 6 meses se medium, 12 meses se low
```

**Tiers**:
- **high (3 meses)** — Plataformas Meta/Google/LinkedIn, GA4, Search Console, CONAR/CDC, tendências, AI search
- **medium (6 meses)** — Frameworks, métricas-padrão, copy de plataforma, brand-design
- **low (12 meses)** — Metodologias (Cialdini, Kahneman, Trout & Ries, Christensen JTBD), princípios UX

A skill `manutencao-skills` documenta o processo completo de re-validação + lifecycle (Creation → Update → Deprecation → Sunset).

## Regras imutáveis

- **NÃO CHUTAR** (cristal C0) — suposição de mercado/público/número nunca é fato
- **Não inventar** dado de mercado, share, CAC, LTV, métrica de plataforma, case real
- **Não criar** copy enganoso, dark pattern, prova social falsa, depoimento fabricado
- **Não orientar** greenwashing, pinkwashing, manipulação eleitoral, fake countdown, fake scarcity
- **Não gerar** peça que viole CDC, LGPD, CONAR, ANPD, regras de plataforma
- **Não produzir AI-slop estético** — gradiente neon genérico, sem-serif arredondada padrão, simetria perfeita morta (atelier-criativo combate firme)
- **Contraditório Interno** sempre ativo em peça relevante (10 perguntas)
- **Avisar decaimento temporal** de skill vencida ao carregá-la
- **Disclaimer educational mandatory** — content educacional, não substitui assessoria jurídica/regulatória/estratégica

## Brasil 2026 — specificidades embutidas

- **Regulação**: LGPD (Lei 13.709/2018) + ANPD agência plena (Lei 15.352/2026) + CONAR Anexo P influencers (Lei 15.325 Jan-2026) + CDC Art. 30/36/37/38 + CVM Resolução 193/2023 mandatory ESG Jan-2026 + ECA Digital Lei 15.211/2025 vigência 17-Mar-2026 + Lei E-Commerce + WCAG 2.2 + LBI 13.146/2015 + ABNT NBR 9050 + 16537 sinalização tátil
- **Mercado**: comunicação corporativa R$ 30 bi/ano (Aberje) + 95.1% empresas Brasil dificuldade qualificado (ManpowerGroup) + 800k+ ONGs + GIFE 130+ associados R$ 4 bi/ano + Pacto Global ONU 2.400+ signatários (segunda maior rede mundial)
- **Plataformas**: RD Station market leader B2B + Gupy ATS + ClickSign assinatura digital líder + Reclame Aqui ouro CI BR (17M reclamações)
- **Cases canônicos**: Magalu Lu 30+ anos + Nubank purple #820AD1 + Itaú orange #EC7000 + Stone door-to-door + iFood + Boticário rebrand 2024 + Pipefy global-first Curitiba + Natura Crer Para Ver R$ 30M+/ano 30+ anos
- **Linguagem artística BR** (atelier-criativo): arte indígena (grafismos kadiweu) + barroco mineiro (Aleijadinho) + modernismo (Tarsila + Anita Malfatti) + neoconcretismo (Lygia Pape + Lygia Clark + Hélio Oiticica) + tropicalismo + arquitetura (Niemeyer + Lina Bo Bardi + Burle Marx + Paulo Mendes da Rocha) + arte contemporânea (Ernesto Neto + Adriana Varejão + Beatriz Milhazes)

## Atualização

```powershell
# Atualizar plugin já instalado
claude plugin marketplace update frank-mkt
claude plugin update frank-mkt --scope project
```

⚠️ **Atenção**: `update` só funciona se plugin já estiver instalado. Se você fez `marketplace remove` antes, use `install` (não `update`).

## Remoção

```powershell
# Desabilitar (mantém arquivos do plugin)
claude plugin disable frank-mkt

# Desinstalar (remove plugin)
claude plugin uninstall frank-mkt

# Remover marketplace inteiro
claude plugin marketplace remove frank-mkt
```

O diretório `.frank-mkt/` permanece no projeto cliente — preserva contexto. Remover manualmente se desejado.

## Estrutura do repositório

Padrão Claude Code marketplace canônico (validado em 2026-05-09):

```
frank-mkt/                              # repo root (alexandrejalkh/frank-mkt)
├── .claude-plugin/
│   └── marketplace.json                # Marketplace manifest (source: ./frank-mkt-plugin)
├── README.md                           # Este arquivo
├── docs_mkt/
│   ├── ROADMAP-FRANK-MKT.md            # Roadmap detalhado
│   └── INSTALACAO.md                   # Guia instalação completo
└── frank-mkt-plugin/                   # Plugin em subpasta dedicada
    ├── .claude-plugin/
    │   └── plugin.json                 # Plugin manifest
    ├── CHANGELOG.md                    # Histórico v0.1.0 → v2.35.0
    ├── settings.json
    ├── skills/                         # 92 skills em 18 blocos
    │   ├── INDEX.md                    # Mapa completo
    │   └── <nome-skill>/SKILL.md
    ├── commands/                       # 9 slash commands
    │   ├── init.md (com doc mestre identidade-visual.md ✨)
    │   ├── atelier.md ✨
    │   └── <outros>.md
    ├── agents/                         # 15 agentes especialistas
    │   ├── frank-mkt.md (persona principal)
    │   ├── atelier-criativo.md ✨
    │   └── <outros>.md
    └── hooks/                          # Hooks (check-skills-vencidas)
```

**Por que plugin em subpasta dedicada?** Padrão Claude Code marketplace 2026 — `marketplace.json` na ROOT lista plugins com `source: "./pasta-plugin"`. Plugin direto na ROOT não funciona com `source: "."`.

## Estrutura `.frank-mkt/` no projeto cliente

Quando user roda `/frank-mkt:init`, é criada esta estrutura no projeto:

```
.frank-mkt/
├── README.md                           # Visão geral do projeto + índice
├── marca/
│   ├── identidade.md                   # Brand DNA (cross-skill: branding + posicionamento-marca)
│   ├── voice-tone.md                   # Voz + tom (cross-skill: branding)
│   └── identidade-visual.md ✨         # DOC MESTRE 12 seções: cores + tipografia + iconografia + logo + formas + estilo fotográfico + ilustração + animação + aplicações + decisões + versionamento
├── persona/
│   ├── icp.md                          # Ideal Customer Profile
│   └── jtbd.md                         # Jobs-to-be-Done
├── campanhas/
├── decisoes/
│   ├── adrs/                           # Architecture Decision Records adaptados para MKT
│   └── log.md                          # Log cronológico de decisões + rationale
├── entregaveis/
│   ├── copy/
│   ├── visual/                         # SVGs + imagens + mockups + logo/ + icons/ + illustrations/
│   ├── decks/
│   └── docs/
└── pesquisa/
    ├── concorrentes.md
    └── trends.md
```

## Versão

**v2.35.0** (2026-05-10) — 116 artefatos (92 skills + 9 commands + 15 agentes) / 119.737+ linhas. Inclui agente `atelier-criativo` (artista digital anti-AI-slop) + slash command `/frank-mkt:atelier` + doc mestre `identidade-visual.md` com 12 seções estruturadas. Ver [`frank-mkt-plugin/CHANGELOG.md`](frank-mkt-plugin/CHANGELOG.md) para histórico detalhado v0.1.0 → v2.35.0.

## Plugins SPKR/Frank compatíveis

Frank-MKT pode rodar **simultaneamente com outros plugins Frank** no mesmo projeto Claude Code (modulares + namespaceados):

- **[Frank Dev](https://github.com/microeetc/spkr-frank-dev-marketplace)** — Engenheiro de Software Senior (117 skills técnicas + Code Review + Guardian Anti-Lazy)
- **[Frank Pentest](https://github.com/alexandrejalkh/spkr-frank-pentest-marketplace)** — Auditor de Segurança AI-agentic (8 transversais + 14 especialistas)
- **[Frank Jurídico TI](https://github.com/microeetc/spkr-frank-juridico-marketplace)** — Consultor Jurídico/Comercial/Fiscal/TI (49 skills + Juiz + Auditor + ISO-Compliance)

Cenário típico — founder solo SaaS Brasil: Frank-Dev (code review + segurança) + Frank-MKT (marketing + brand identity) rodando juntos no mesmo projeto.

## Autor

**Alexandre Jalkh** — SPKR Serviços e Consultoria de Informática LTDA

## Licença

UNLICENSED — uso restrito conforme termos definidos pelo autor. Distribuição ou modificação requer autorização expressa.

## Filosofia

Marketing aplicado de verdade é onde imprecisão custa caro: copy enganoso vira ação do PROCON; campanha sem persona queima orçamento; SEO mal-feito leva anos para recuperar autoridade; post equivocado em rede social vira crise de marca em horas; identidade visual genérica AI-slop torna marca invisível.

Frank-MKT existe para traduzir essa complexidade sem perder ética. Antecipa armadilhas antes que custem dinheiro, tempo, reputação ou liberdade. Diz "essa promessa não se sustenta" quando o cliente quer ouvir o contrário — e diz "tem público real aqui" quando o mercado parece dizer "desista". E quando o cliente pede "algo com alma", o `atelier-criativo` recusa AI-slop, sintetiza história da arte em voz própria e defende posição estética com argumento.

**Precisão de mercado. Antecipação estratégica. Visão estética. Humanidade na entrega.**
