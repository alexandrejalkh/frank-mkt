# Frank MKT — Plugin Claude Code

Consultor de Marketing, SEO, Mídias Sociais e Inteligência de Mercado que opera como plugin do Claude Code. Persona unificada com motor cognitivo, Contraditório Interno obrigatório, Perfilador de Mercado e skills com decaimento temporal. Inspirado na arquitetura do Frank Jurídico TI.

> **Status (v0.6.0 — 2026-05-08):** **17 skills implementadas / 20.815 linhas totais**. **2 blocos principais COMPLETOS**.
>
> - ✅ **Bloco SEO completo** (7/7 skills, 9.853 linhas): `seo-fundamentos`, `seo-keywords`, `seo-on-page`, `seo-tecnico`, `seo-link-building`, `conteudo-evergreen`, `seo-ai-otimizacao`.
> - ✅ **Bloco Mídia Social COMPLETO** (10/10 skills, 10.962 linhas): `social-media-fundamentos`, `linkedin-organico`, `x-twitter`, `youtube-shorts`, `instagram-feed-reels`, `tiktok-criativo`, `facebook-organico`, `linkedin-ads`, `instagram-ads`, `facebook-ads`.
> - ⏸️ **Demais blocos não iniciados**: Infraestrutura (8 slash commands), Marketing & Estratégia (5), Copy & Redação (4), Pesquisa & Inteligência de Mercado (6), UX/UI (4), Psicologia & Influência (3), Conhecimento de Plataforma (6), Corporativo & Humanitário (6), Meta-skill (1).
> - ⏸️ **Agentes não iniciados**: 14 planejados (apenas placeholder `agents/README.md`).
>
> **12 skills com pesquisa de campo** (volatility `high`, re-validar a cada 3 meses): `seo-ai-otimizacao` + 11 mídia social. **5 skills volatility `medium`** (re-validar a cada 6 meses): SEO clássicas.
>
> Snapshot detalhado: [`../docs_mkt/SNAPSHOT-2026-05-07.md`](../docs_mkt/SNAPSHOT-2026-05-07.md).
> Roadmap: [`../docs_mkt/ROADMAP-FRANK-MKT.md`](../docs_mkt/ROADMAP-FRANK-MKT.md).

## Instalação

```bash
# 1. Adicionar o marketplace (ainda a definir)
claude plugin marketplace add <url-do-marketplace>

# 2. Instalar o plugin
claude plugin install frank-mkt@<marketplace> --scope project

# 3. Abrir Claude Code no projeto/cliente
claude

# 4. Configurar o caso/cliente
/frank-mkt:init
```

## O que o Frank-MKT vai fazer

- **Persona unificada de marketing & inteligência de mercado** — fala a língua do CMO, fundador, head de growth, social media, redator, designer e analista de pesquisa.
- **Motor cognitivo com fases** — leitura do interlocutor, perfilamento de mercado/persona, custo-benefício de canal/mensagem, construção de conceito/copy/plano, contraditório interno.
- **Cristal C0 "NÃO CHUTAR"** — regra imutável: não apresentar suposição (de mercado, de público, de número) como fato. Na dúvida, perguntar ou pesquisar.
- **Contraditório Interno** — obrigatório em toda análise de campanha, posicionamento ou peça relevante.
- **Perfilador de Mercado** — agente dedicado a sizing, persona, canal, concorrência e oportunidade.
- **Auditor de peças** — varredura mecânica PASS/FAIL em copy, post, landing, briefing, plano de mídia.
- **Decaimento temporal** — skills volúveis (algoritmos de plataforma, tendências, regras Meta/LinkedIn/Google) reavaliadas a cada 1–3 meses.
- **Memória persistente** — `.frank-mkt/` preserva cliente, marca, persona, voz, decisões, cristais e histórico de campanhas.

## Modos de Operação (planejados)

| Modo | Quando ativa | O que entrega |
|------|--------------|---------------|
| **Marketing** | Campanha, posicionamento, jornada, funil | Plano, big idea, copy, mensagem-chave |
| **SEO** | Conteúdo orgânico, ranking, autoridade | Estratégia de keywords, briefing SEO, auditoria on-page |
| **Mídia social** | LinkedIn, Instagram, Facebook, X, TikTok | Calendário editorial, post, carrossel, roteiro de vídeo |
| **Pesquisa de mercado** | Sizing, concorrente, persona, white-space | Relatório, framework, recomendação |
| **Corporativo** | Comunicação interna, employer branding, RP | Posicionamento, narrativa, peça institucional |
| **Empreendedorismo / impacto** | Negócio nascente, social/humanitário | Tese, MVP de comunicação, narrativa de propósito |

## Comandos (planejados)

| Comando | O que faz |
|---------|-----------|
| `/frank-mkt:init` | Configura `.frank-mkt/` do cliente/marca |
| `/frank-mkt:stack` | Exibe estado atual (marca, persona, campanhas) |
| `/frank-mkt:save-session` | Salva log estruturado da sessão |
| `/frank-mkt:help` | Lista comandos, agentes e skills |
| `/frank-mkt:audit [arq]` | Auditoria mecânica PASS/FAIL de peça |
| `/frank-mkt:review` | Review qualitativo de campanha/peça |
| `/frank-mkt:juiz` | Convoca Juiz para divergência entre modos |
| `/frank-mkt:perfil [mercado]` | Convoca Perfilador de Mercado |

## Agentes (planejados)

> Lista detalhada e priorizada em [`../docs_mkt/ROADMAP-FRANK-MKT.md`](../docs_mkt/ROADMAP-FRANK-MKT.md).

- `frank-mkt` — Principal (persona + motor cognitivo + contraditório)
- `juiz` — Arbitrador imparcial de divergência entre modos
- `auditor` — Varredura mecânica de peças (regras PASS/FAIL)
- `investigador` — Entrevista interlocutor, extrai fatos da marca/produto
- `perfilador-mercado` — Sizing, persona, concorrência, white-space
- `redator-hacker` — Copy de alta conversão + ética anti-dark-pattern
- `seo-strategist` — Conteúdo orgânico, keywords, autoridade
- `social-media-linkedin` — Foco em LinkedIn (B2B, employer brand, thought leadership)
- `social-media-instagram` — Foco em Instagram/Reels/Stories
- `social-media-facebook` — Foco em Facebook (orgânico + ads)
- `ux-ui-revisor` — Revisão de interface, hierarquia, acessibilidade
- `psicologia-influencia` — Gatilhos, viés cognitivo, ética
- `frank-corporativo` — Comunicação corporativa, RP, employer branding
- `social-humanitario` — Causas, propósito, ESG, terceiro setor

## Skills (planejadas)

> INDEX completo em [`skills/INDEX.md`](skills/INDEX.md).

Áreas:

- **Infra** — init, stack, save-session, help, audit, review, juiz, perfil.
- **Marketing & estratégia** — posicionamento, branding, funil, jornada, big idea.
- **Copy & redação** — copy de conversão, storytelling, headline, e-mail.
- **SEO** — keywords, on-page, técnico, link building, conteúdo evergreen.
- **Mídias sociais** — LinkedIn, Instagram, Facebook, TikTok, X — orgânico e ads.
- **Pesquisa & inteligência de mercado** — sizing, persona, concorrência, white-space.
- **UX/UI** — heurísticas, acessibilidade, microcopy, design system.
- **Psicologia & influência** — gatilhos éticos, viés cognitivo, prova social.
- **Conhecimento de plataforma** — Meta Ads, Google Ads, LinkedIn Ads, GA4, Search Console.
- **Corporativo & humanitário** — RP, employer branding, ESG, terceiro setor.
- **Meta-skill** — manutenção-skills (re-grounding, decaimento temporal).

## Decaimento Temporal

Toda skill declara no frontmatter YAML:

```yaml
last_verified: 2026-05-07
next_review: 2026-08-07
volatility: high | medium | low | very-low
regrounding_sources:
  - "https://..."
```

Tiers (proposta inicial — refinar por skill):

- **high** (1–3 meses): regras de plataforma (Meta, LinkedIn, Google), algoritmo de feed, política de ads, tendências de criativo.
- **medium** (6 meses): SEO técnico, GA4/Search Console, frameworks de pesquisa, métricas-padrão de plataforma.
- **low** (12 meses): metodologias (contraditório, perfilamento, jornada), psicologia da persuasão, princípios de UX.
- **very-low** (24 meses): infra do plugin (init, stack, audit, review, help, save-session, juiz).

### Hook SessionStart

A cada sessão aberta, `hooks/check-skills-vencidas.sh` verifica `next_review` de todas as skills e lista as vencidas. Silencioso quando nenhuma está vencida.

### Re-grounding é sob demanda

Frank avisa quando carrega skill vencida. Usuário decide se vale re-validar naquele caso concreto. Sem atualização automática proativa.

## Regras imutáveis (planejadas)

- **NÃO CHUTAR** (cristal C0) — suposição de mercado/público/número nunca é fato. Na dúvida, perguntar ou pesquisar.
- Não inventar dado de mercado, share, CAC, LTV, métrica de plataforma, case real.
- Não criar copy enganoso, dark pattern, prova social falsa, depoimento fabricado.
- Não orientar greenwashing, pinkwashing, manipulação eleitoral.
- Não gerar peça que viole CDC, LGPD, CONAR, regras de plataforma (Meta, LinkedIn, Google).
- Contraditório Interno SEMPRE ativo em peça relevante.
- Avisar decaimento temporal de skill vencida ao carregá-la.

## Atualização

```bash
claude plugin marketplace update <marketplace>
claude plugin update frank-mkt@<marketplace> --scope project
```

## Remoção

```bash
claude plugin disable frank-mkt@<marketplace>
# ou
claude plugin uninstall frank-mkt@<marketplace>
```

O diretório `.frank-mkt/` permanece no projeto — remover manualmente se desejado.

## Versão

**0.6.0** (2026-05-08) — 🎉 **17 skills implementadas, 20.815 linhas**. **2 blocos principais COMPLETOS**: SEO Estendido (7/7) + Mídia Social (10/10). Ver [CHANGELOG.md](CHANGELOG.md) para histórico detalhado.

## Autor

Alexandre Jalkh — SPKR Serviços e Consultoria de Informática LTDA

## Filosofia

Marketing aplicado de verdade é onde imprecisão custa caro: copy enganoso vira ação do PROCON; campanha sem persona queima orçamento; SEO mal-feito leva anos para recuperar autoridade; post equivocado em rede social vira crise de marca em horas.

Frank-MKT existe para traduzir essa complexidade sem perder ética. Antecipa armadilhas antes que custem dinheiro, tempo, reputação ou liberdade. Diz "essa promessa não se sustenta" quando o cliente quer ouvir o contrário — e diz "tem público real aqui" quando o mercado parece dizer "desista".

**Precisão de mercado. Antecipação estratégica. Humanidade na entrega.**
