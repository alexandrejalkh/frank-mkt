# Frank MKT — Plugin Claude Code

Consultor de Marketing, SEO, Mídias Sociais e Inteligência de Mercado que opera como plugin do Claude Code. Persona unificada com motor cognitivo, Contraditório Interno obrigatório, Perfilador de Mercado e skills com decaimento temporal. Foco Brasil 2026 (LGPD + CONAR + CDC + cultura tropicalizada).

> **Status v2.32.0 — 2026-05-09 — 🚀🚀🚀 PLUGIN 100% COMPLETO**
>
> **114 artefatos / 119.089 linhas totais**:
> - ✅ **92 skills** em **18 blocos completos** (107.548 linhas)
> - ✅ **8 slash commands** (3.529 linhas)
> - ✅ **14 agentes especialistas** (8.012 linhas)
>
> **Volatility distribution**:
> - **24 skills `high`** (re-validar 3 meses) — plataformas Meta/Google/LinkedIn, GA4, Search Console, CONAR/CDC, tendências
> - **61 skills `medium`** (re-validar 6 meses) — frameworks, métricas, copy de plataforma, brand-design
> - **7 skills `low`** (re-validar 12 meses) — metodologias, psicologia, princípios UX
>
> Roadmap completo: [`docs_mkt/ROADMAP-FRANK-MKT.md`](docs_mkt/ROADMAP-FRANK-MKT.md). Histórico: [`CHANGELOG.md`](CHANGELOG.md).

## Instalação

Guia completo: [docs_mkt/INSTALACAO.md](docs_mkt/INSTALACAO.md)

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

**Verificação**: dentro do Claude Code, rode `/frank-mkt:help` — deve listar 8 commands + 14 agentes + 92 skills.

**Re-instalação após updates**: se já tinha versão anterior do marketplace adicionado, force refresh:
```powershell
claude plugin marketplace remove frank-mkt
claude plugin marketplace add https://github.com/alexandrejalkh/frank-mkt.git
claude plugin install frank-mkt --scope project
```

## O que o Frank-MKT faz

- **Persona unificada de marketing & inteligência de mercado** — fala a língua do CMO, fundador, head de growth, CHRO, social media, redator, designer, brand designer, analista de pesquisa, IR, ESG officer.
- **Motor cognitivo com fases** — leitura do interlocutor, perfilamento de mercado/persona, custo-benefício de canal/mensagem, construção de conceito/copy/plano, contraditório interno.
- **Cristal C0 "NÃO CHUTAR"** — regra imutável: não apresentar suposição (de mercado, público, número) como fato. Na dúvida, pergunta ou pesquisa.
- **Contraditório Interno** — checklist de 10 perguntas obrigatório em toda análise de campanha, posicionamento ou peça relevante.
- **Decaimento temporal** — skills volúveis (algoritmos plataforma, regulação, tendências) reavaliadas a cada 3 meses; metodologias estáveis a cada 12 meses.
- **Brasil-first** — LGPD/CONAR/CDC/CVM/ANPD compliance embutido + cases nacionais (Magalu, Nubank, Itaú, iFood, Stone, Pipefy, RD Station) + ferramentas tropicalizadas (Pix, ClickSign, RD Station, Gupy).
- **Memória persistente** — `.frank-mkt/` preserva cliente, marca, persona, voz, decisões e histórico de campanhas.

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

INDEX completo de todas as skills com volatility, linhas e cross-references: [`skills/INDEX.md`](skills/INDEX.md).

## 8 Slash Commands

| Comando | Linhas | Função |
|---------|-------:|--------|
| `/frank-mkt:init` | 560 | Configura `.frank-mkt/` cliente — estrutura marca/persona/campanhas/decisões/entregáveis/pesquisa |
| `/frank-mkt:stack` | 348 | Estado atual do projeto (marca + persona + campanhas + decisões + entregáveis recentes) |
| `/frank-mkt:save-session` | 359 | Log estruturado da sessão em `.frank-mkt/sessoes/` |
| `/frank-mkt:help` | 403 | Menu navegável: 8 commands + 14 agentes + 92 skills agrupadas |
| `/frank-mkt:audit` | 467 | Varredura mecânica PASS/FAIL (7 tipos peça: copy/post/landing/briefing/plano-mídia/deck/email) |
| `/frank-mkt:review` | 509 | Review qualitativo multi-agent (narrativa + execução + arbitragem) |
| `/frank-mkt:juiz` | 439 | Arbitra divergência entre agentes (6 critérios hierárquicos) |
| `/frank-mkt:perfil` | 444 | Perfilador de Mercado: TAM/SAM/SOM + ICP + concorrência + white-space + trends |

## 14 Agentes Especialistas

| Agente | Modelo | Função |
|--------|--------|--------|
| `frank-mkt` | opus | **Persona principal** — orquestra 92 skills + 13 agentes + 8 commands |
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

Frank-MKT invoca skills automaticamente baseado no contexto. Exemplo de fluxo típico:

```
Cliente: "Preciso lançar produto B2B SaaS no Brasil"

Frank-MKT invoca em ordem:
1. /frank-mkt:init → cria .frank-mkt/ estrutura
2. agente investigador → entrevista 5 blocos (marca + produto + persona + interlocutor + objetivos)
3. /frank-mkt:perfil "B2B SaaS Brasil" → perfilador-mercado (TAM/SAM/SOM + ICP + concorrência + trends)
4. skill branding → archetype + voice + brand DNA
5. skill posicionamento-marca → STP + Trout & Ries POV
6. skill big-idea → núcleo unificador + tagline
7. skill go-to-market-strategy → PLG/SLG/CLG motion + GTM canvas
8. skill copywriting-conversao → headlines + CTAs + frameworks
9. skill linkedin-organico → conteúdo orgânico B2B
10. skill conhecimento-linkedin-ads → Lead Gen Forms + ABM
11. /frank-mkt:audit → varredura mecânica PASS/FAIL pré-entrega
12. /frank-mkt:review → review qualitativo multi-agent
13. /frank-mkt:save-session → log estruturado
```

## Decaimento Temporal

Toda skill declara no frontmatter YAML:

```yaml
volatility: high | medium | low
last_review: 2026-05-09
next_review: 2026-08-09  # = 3 meses se high, 6 meses se medium, 12 meses se low
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
- **Contraditório Interno** sempre ativo em peça relevante (10 perguntas)
- **Avisar decaimento temporal** de skill vencida ao carregá-la
- **Disclaimer educational mandatory** — content educacional, não substitui assessoria jurídica/regulatória/estratégica

## Brasil 2026 — specificidades embutidas

- **Regulação**: LGPD (Lei 13.709/2018) + ANPD agência plena (Lei 15.352/2026) + CONAR Anexo P influencers (Lei 15.325 Jan-2026) + CDC Art. 30/36/37/38 + CVM Resolução 193/2023 mandatory ESG Jan-2026 + ECA Digital Lei 15.211/2025 vigência 17-Mar-2026 + Lei E-Commerce + WCAG 2.2 + LBI 13.146/2015
- **Mercado**: comunicação corporativa R$ 30 bi/ano (Aberje) + 95.1% empresas Brasil dificuldade qualificado (ManpowerGroup) + 800k+ ONGs + GIFE 130+ associados R$ 4 bi/ano + Pacto Global ONU 2.400+ signatários (segunda maior rede mundial)
- **Plataformas**: RD Station market leader B2B + Gupy ATS + ClickSign assinatura digital líder + Reclame Aqui ouro CI BR (17M reclamações)
- **Cases canônicos**: Magalu Lu 30+ anos + Nubank purple #820AD1 + Itaú orange #EC7000 + Stone door-to-door + iFood + Boticário rebrand 2024 + Pipefy global-first Curitiba + Natura Crer Para Ver R$ 30M+/ano 30+ anos

## Atualização

```bash
claude plugin marketplace update https://github.com/alexandrejalkh/frank-mkt.git
claude plugin update frank-mkt --scope project
```

## Remoção

```bash
claude plugin disable frank-mkt
# ou
claude plugin uninstall frank-mkt
```

O diretório `.frank-mkt/` permanece no projeto — remover manualmente se desejado.

## Estrutura do repositório

Padrão Claude Code marketplace canônico (validado em 2026-05-09):

```
frank-mkt/                              # repo root
├── .claude-plugin/
│   └── marketplace.json                # Marketplace manifest
├── README.md                           # Este arquivo
├── docs_mkt/
│   ├── ROADMAP-FRANK-MKT.md            # Roadmap detalhado
│   └── INSTALACAO.md                   # Guia instalação completo
└── frank-mkt-plugin/                   # Plugin em subpasta dedicada
    ├── .claude-plugin/
    │   └── plugin.json                 # Plugin manifest
    ├── CHANGELOG.md
    ├── settings.json
    ├── skills/                         # 92 skills em 18 blocos
    │   ├── INDEX.md                    # Mapa completo
    │   └── <nome-skill>/SKILL.md
    ├── commands/                       # 8 slash commands
    │   └── <nome-command>.md
    ├── agents/                         # 14 agentes especialistas
    │   └── <nome-agente>.md
    └── hooks/                          # Hooks (check-skills-vencidas)
```

**Por que plugin em subpasta dedicada?** Padrão Claude Code marketplace 2026 — `marketplace.json` na ROOT lista plugins com `source: "./pasta-plugin"`. Plugin na ROOT direta não funciona com `source: "."`.

## Versão

**v2.32.0** (2026-05-09) — 🚀 **PLUGIN 100% COMPLETO**: 114 artefatos (92 skills + 8 commands + 14 agentes) / 119.089 linhas. Ver [CHANGELOG.md](CHANGELOG.md) para histórico detalhado v0.1.0 → v2.32.0.

## Autor

**Alexandre Jalkh** — SPKR Serviços e Consultoria de Informática LTDA

## Licença

UNLICENSED — uso restrito conforme termos definidos pelo autor. Distribuição ou modificação requer autorização expressa.

## Filosofia

Marketing aplicado de verdade é onde imprecisão custa caro: copy enganoso vira ação do PROCON; campanha sem persona queima orçamento; SEO mal-feito leva anos para recuperar autoridade; post equivocado em rede social vira crise de marca em horas.

Frank-MKT existe para traduzir essa complexidade sem perder ética. Antecipa armadilhas antes que custem dinheiro, tempo, reputação ou liberdade. Diz "essa promessa não se sustenta" quando o cliente quer ouvir o contrário — e diz "tem público real aqui" quando o mercado parece dizer "desista".

**Precisão de mercado. Antecipação estratégica. Humanidade na entrega.**
