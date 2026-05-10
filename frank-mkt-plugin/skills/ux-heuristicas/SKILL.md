---
name: ux-heuristicas
description: Heuristicas UX (Nielsen 10) + UX research methods + usability testing + cognitive walkthrough + heuristic evaluation + UX metrics SUS para founders/PMs/UX designers/product marketers/agencias, com cobertura Nielsen Norman Group canonico, Krug "Don't Make Me Think", ISO 9241-11 usability, SUS benchmarks 68 average/80+ great, Brasil 2026 (UX Conference Brasil + Cardume + cases nacionais), 2026 trends (AI-assisted UX research + voice UX + AR/VR heuristics). 1ª SKILL Bloco UX/UI.
volatility: medium
last_review: 2026-05-09
next_review: 2026-11-09
languages: [pt-BR]
audience: [founders, PMs, UX-designers, product-marketers, agencias, researchers]
ascii_only: true
---

# Skill: ux-heuristicas

> **1ª SKILL do Bloco UX/UI**. Predecessoras: 10 Blocos previos completos (Pesquisa & Inteligencia 6/6 fechado).
> **Volatility: medium (6 meses)** — Heuristicas Nielsen 1994 sao foundational, MAS aplicacao 2026 desloca: AI-assisted UX research, voice UX, AR/VR, LGPD UX, agentic interfaces (Claude Computer Use + ChatGPT Agents) reescrevendo "Match real world" e "User control".

---

## Decaimento Temporal

| Campo | Valor |
|---|---|
| Volatility | medium |
| Cadencia revisao | 6 meses |
| Ultima validacao | 2026-05-09 |
| Proxima revisao | 2026-11-09 |

**Por que medium e nao high**: Heuristicas Nielsen tem 30+ anos e seguem relevantes (NN/G confirma 2026 — fundamento psicologico humano nao mudou). SUS Brooke 1986, ISO 9241-11 1998, Krug 2000 sao classicos consolidados. **MAS** aplicacao 2026 desloca rapidamente: (a) AI-assisted UX research (Maze AI + Dovetail AI + UserTesting AI Insights) muda rotina de analise; (b) voice UX e conversational interfaces forcam reinterpretacao de "visibility of status"; (c) agentic interfaces (Claude Code, ChatGPT agents, Gemini CLI) reescrevem heuristica 3 (User control) — quem controla quando o agente age sozinho; (d) AR/VR heuristics (Oculus, Vision Pro) adicionam dimensao espacial; (e) LGPD compliance UX no Brasil cria nova heuristica de "consent transparency"; (f) SUS benchmarks de 2026 mostram rebound de uso apos slump. Por isso revisao a cada 6 meses.

**O que provavelmente NAO muda 1 ano**: Os 10 itens nominais de Nielsen, regra dos 5 usuarios, escala SUS 0-100 com media 68, severidade 0-4 de Nielsen, ISO 9241-11 (efetividade + eficiencia + satisfacao).

**O que pode mudar antes de 6 meses**: Heuristicas para agentic AI (NN/G publicou drafts 2025), benchmarks SUS por categoria (digital health, voice, AR), prevalencia AI-moderated testing.

---

## Visao Geral

**O que esta skill faz**:
- Frame para produzir CONTEUDO MKT educational sobre **heuristicas UX**: Nielsen 10 + ISO 9241-11 + cognitive walkthrough + heuristic evaluation + usability testing + UX research methods + UX metrics + SUS.
- 5 audiencias: (a) **founders pre-Series A** ($0-2M ARR) decidindo onde investir UX research escasso; (b) **PMs B2B SaaS** rodando ciclos de descoberta-validacao; (c) **UX designers** em agencia que precisam vender heuristic eval para clientes; (d) **product marketers** transformando insights UX em copy e posicionamento; (e) **researchers** consolidando metodos qualitativos e quantitativos.
- **NAO substitui** auditoria UX profissional NN/G/Forrester, nem certificacao Nielsen Norman Group, nem consultoria de pesquisa de campo.

**O que NAO faz** (limites duros):
- NAO produz heuristic evaluation real do produto do leitor (orienta como rodar uma).
- NAO substitui certificacao NN/G UX Master (700+ horas treinamento).
- NAO substitui pesquisa qualitativa profissional (UserVoice, UserTesting, Aela).
- NAO substitui auditoria de acessibilidade WCAG (skill irma `acessibilidade-wcag`).
- NAO produz design system pronto (skill irma `design-system-basico`).
- NAO substitui legal review LGPD (apenas indica heuristica de consent transparency).
- NAO inventa estatisticas — toda metrica e referenciada com fonte.

**Forma de uso pelo Claude no Frank-MKT**:
1. Founder pergunta "como sei se meu onboarding tem problema?" -> Claude usa esta skill para guiar heuristic eval rapida + usability test 5-user.
2. PM pede "preciso justificar UX research budget" -> Claude usa esta skill para construir argumentacao baseada em SUS + ROI Nielsen.
3. Agencia pede "como vendo heuristic eval para cliente" -> Claude usa esta skill para deck + entregaveis.
4. Product marketer pede "como traduzo bug UX em mensagem de feature update" -> Claude usa esta skill cross com `microcopy`.

---

## Fundacao 1 — Nielsen 10 Heuristicas (1994 + Atualizacao Cognitiva 2024)

**Origem**: Jakob Nielsen, "Enhancing the explanatory power of usability heuristics", CHI 1994. Refinadas por NN/G ao longo de 30 anos. Em 2024 NN/G publicou guia atualizado mantendo os 10 itens originais mas reinterpretando exemplos para mobile, voice, AR e AI.

**Heuristica 1 — Visibility of System Status**
Sistema deve sempre informar o usuario sobre o que esta acontecendo, com feedback apropriado em tempo razoavel.
Exemplos 2026: spinner de "AI gerando resposta" no ChatGPT, progress bar em upload, breadcrumbs em e-commerce, badge "online" em chat.
Falha classica: botao clicado sem feedback (usuario clica 5 vezes).

**Heuristica 2 — Match Between System and Real World**
Linguagem do usuario, nao do sistema. Convencoes do mundo real, ordem natural.
Exemplos 2026: icone de lixeira, pasta de arquivo, "carrinho" em e-commerce.
Falha 2026: bots juridicos usando termos como "peticionar EAD" sem traducao para leigo.

**Heuristica 3 — User Control and Freedom**
Usuario precisa de "saidas de emergencia" claras (undo, redo, cancel, voltar).
Exemplos 2026: Cmd+Z, "Desfazer envio" do Gmail (10s grace), botao Cancel em wizard.
Tensao 2026: agentic AI — quando Claude Computer Use ou ChatGPT Agent age, o usuario PRECISA de pause/abort imediato. NN/G chamou isso "human-in-the-loop heuristic".

**Heuristica 4 — Consistency and Standards**
Usuarios nao deveriam adivinhar se palavras/situacoes diferentes significam a mesma coisa. Seguir convencoes da plataforma.
Exemplos 2026: iOS HIG (Human Interface Guidelines), Material Design 3, Apple Vision Pro guidelines, Brasil — Gov.br Design System.
Falha: cada pagina do produto com botao "Salvar" em cor diferente.

**Heuristica 5 — Error Prevention**
Melhor que mensagens de erro e prevenir o erro acontecer. Confirmacoes em acoes destrutivas.
Exemplos 2026: confirmacao "Tem certeza que quer excluir conta?", auto-save Google Docs, validacao inline em forms.
Brasil 2026: confirmacao dupla em transferencia PIX > R$ 5k (Bacen).

**Heuristica 6 — Recognition Rather Than Recall**
Minimize carga de memoria do usuario tornando objetos, acoes e opcoes visiveis.
Exemplos 2026: dropdown autocompletar, historico recente, "voce visitou" em e-commerce, tags sugeridas.
Falha classica: comando CLI sem auto-complete; campo "digite o codigo de 12 digitos enviado".

**Heuristica 7 — Flexibility and Efficiency of Use**
Aceleradores para experts (atalhos, customizacao) sem prejudicar iniciantes.
Exemplos 2026: Cmd+K palette (Linear, Notion, Vercel), atalhos VSCode, Gmail keyboard shortcuts.
Brasil 2026: aplicativos bancarios com "favoritos PIX" (frequentes destacados).

**Heuristica 8 — Aesthetic and Minimalist Design**
Interfaces nao deveriam conter informacao irrelevante ou raramente necessaria.
Exemplos 2026: Stripe checkout, Linear kanban, Notion home, Apple defaults.
Falha: dashboard com 47 metricas onde so 5 importam.

**Heuristica 9 — Help Users Recognize, Diagnose, Recover from Errors**
Mensagens de erro em linguagem clara, indicar problema E sugerir solucao.
Exemplos 2026: "Cartao recusado — tente outro metodo de pagamento" + botao direto Pix; Stripe error API com error_code + actionable message.
Falha: "Error 500" sem contexto.

**Heuristica 10 — Help and Documentation**
Mesmo que melhor seja sistema usavel sem documentacao, as vezes documentacao e necessaria. Deve ser facil de buscar, focada em tarefa do usuario, listar passos concretos.
Exemplos 2026: Stripe Docs (gold standard), Linear method docs, ChatGPT Help Center, Notion Help.
Brasil 2026: Help do Nubank em portugues claro, sem jargao bancario.

**Severidade 0-4 (Nielsen scale)**:
- 0: Nao e problema usabilidade.
- 1: Cosmetico — nao precisa fix se nao tiver tempo.
- 2: Menor — baixa prioridade.
- 3: Maior — alta prioridade, fix antes release.
- 4: Catastrofico — bloqueia uso, fix imediato.

---

## Fundacao 2 — UX Research Methods (Discovery + Generative + Evaluative)

**Taxonomia 3 eixos** (NN/G + User Interviews):
- Generative (descobrir): user interviews, diary studies, ethnography, contextual inquiry.
- Descriptive (categorizar): card sorting, tree testing, surveys, analytics.
- Evaluative (validar): usability testing, A/B testing, heuristic eval, cognitive walkthrough.

**User Interviews**:
- Tipo: 1:1, 30-60min, 5-8 participantes por segmento (regra Nielsen — 80% problemas surgem com 5).
- Quando: descoberta inicial, problem-space, validacao de persona.
- Tecnica: nao-leading questions; "5 whys"; "tell me about the last time you...".
- Output: transcript + tematic analysis + journey map.

**Diary Studies**:
- Duracao: 1-4 semanas.
- Quando: comportamento longitudinal, adoption, satisfacao prolongada.
- Output: timeline com momentos de friccao + emocao + contexto.
- Ferramentas 2026: dscout, Indeemo, Maze diary mode.

**Card Sorting**:
- Open card sort: usuario cria categorias.
- Closed card sort: categorias pre-definidas.
- Hybrid: misto.
- Quando: arquitetura de informacao (IA), navegacao, taxonomia.
- Sample: 15-30 participantes (saturacao em 30 segundo Spencer 2009).
- Ferramentas 2026: Optimal Workshop, UXtweak, Maze.

**Tree Testing**:
- Validacao reversa do card sort — usuario navega arvore para encontrar item.
- Metrica: success rate + directness.
- Benchmark: > 70% success = bom; > 80% = otimo.

**Ethnographic / Contextual Inquiry**:
- Observacao no ambiente real do usuario.
- Quando: comportamentos que usuario nao verbaliza ou nao percebe.
- Custo: alto (campo).

**Surveys**:
- Quantitativo, escala. Sample > 100 para significancia.
- Ferramentas 2026: Typeform, Lyssna (ex-UsabilityHub), Google Forms.
- Cuidado: viesses (leading questions, social desirability).

**Analytics**:
- GA4, Hotjar, FullStory, PostHog.
- Quando: comportamento real em escala.
- Limitacao: diz O QUE acontece, nao POR QUE.

---

## Fundacao 3 — Usability Testing (Moderated vs Unmoderated, Remote vs In-Person)

**Regra dos 5 usuarios** (Nielsen 2000 — "Why You Only Need to Test with 5 Users"):
- 5 usuarios encontram ~85% dos problemas de usabilidade.
- Lei do retorno decrescente: 6o, 7o, 8o usuario repetem achados.
- Excecao: produtos com personas muito heterogeneas — 5 por persona.

**Moderated Testing**:
- Pesquisador presente (live).
- Pode aprofundar com follow-up.
- Custo: alto (1-2 horas por sessao + analise + recrutamento).
- Quando: prototipos early-stage, fluxos complexos.
- Ferramentas 2026: Lookback, UserTesting, Userlytics, Zoom + screen share.

**Unmoderated Testing**:
- Participante sozinho, prompts pre-definidos.
- Custo: baixo (resultados em 24h).
- Quando: validacao rapida, A/B de alternativas, smoke test.
- Ferramentas 2026: Maze, UserTesting Quick Answers, UXtweak, Useberry, Lyssna.

**Remote vs In-Person**:
- Remote (2026 default): mais participantes, mais barato, viesses geograficos reduzidos.
- In-person: tarefas com hardware especifico (POS, kiosks, AR/VR), populacoes que nao usam computador, observacao de body language.

**Think-Aloud Protocol**:
- Participante verbaliza o que pensa enquanto usa.
- Concurrent (durante) vs retrospective (depois com video).
- Vies: pode mudar comportamento.

**Sample size por tipo de estudo**:
| Estudo | N min | N otimo |
|---|---|---|
| User interview qualitativo | 5 | 5-8 por persona |
| Usability test qualitativo | 5 | 5 por persona |
| Card sort | 15 | 30 |
| Tree test | 30 | 50 |
| Survey | 100 | 384 (95% IC ±5%) |
| SUS benchmark | 20 | 50 para comparacao |

---

## Fundacao 4 — Cognitive Walkthrough + Heuristic Evaluation

**Heuristic Evaluation (Nielsen 1990)**:
- Avaliadores expertos (3-5) revisam interface contra lista de heuristicas (geralmente Nielsen 10).
- Cada um INDIVIDUAL primeiro, depois consolida.
- 5 avaliadores acham ~75% dos problemas (Nielsen). 3 ja acham 60%.
- Output: lista de problemas + heuristica violada + severidade 0-4 + screenshot + recomendacao.

**Processo Heuristic Eval (NN/G)**:
1. Definir escopo (quais telas/fluxos).
2. Recrutar 3-5 avaliadores (idealmente UX practitioners).
3. Brief: heuristicas + escopo + persona.
4. Avaliacao individual (2-4h por avaliador).
5. Consolidacao: agregar duplicates, atribuir severidade.
6. Report: problema + heuristica + severidade + recomendacao + esforco fix.

**Cognitive Walkthrough (Wharton et al. 1994)**:
- Simula primeira experiencia do usuario.
- Avaliador segue passo-a-passo perguntando 4 perguntas em CADA acao:
  1. O usuario tentaria esta acao?
  2. O usuario perceberia que esta acao e possivel?
  3. O usuario associaria a acao correta com seu objetivo?
  4. Apos a acao, o usuario veria progresso para o objetivo?

**Quando usar qual** (MeasuringU 2024):
- Heuristic eval: produto maduro, foco em conformidade de boas praticas, audit geral.
- Cognitive walkthrough: produto novo ou fluxo critico, foco em LEARNABILITY (primeiro uso), checkout, onboarding.
- Combinar ambos: cobertura mais ampla — heuristicas pegam consistency, walkthrough pega learnability.

**Severidade Nielsen 0-4 (revisitada)**:
- 4 (catastrofica): usuario abandona, perde dados, vaza LGPD.
- 3 (maior): perda de conversao, friccao alta, mas usuario consegue.
- 2 (menor): irrita mas nao bloqueia.
- 1 (cosmetica): visual, nice-to-fix.
- 0 (nao problema): preferencia subjetiva.

---

## Fundacao 5 — UX Metrics + SUS (System Usability Scale)

**ISO 9241-11 (1998 — base teorica)**:
- Usabilidade = Efetividade + Eficiencia + Satisfacao em CONTEXTO especifico.
- Nao existe "usavel para todos" — sempre contextual.

**SUS — System Usability Scale (Brooke 1986)**:
- 10 perguntas, escala Likert 1-5.
- Score 0-100. Media historica: **68**.
- Benchmark: > 80 = excelente; 68-80 = aceitavel; < 50 = problemas serios.
- Curve grading (Sauro & Lewis 2016, 241 estudos):
  - A+: 84.1+ (top 5%)
  - A: 80.8 (top 10%)
  - A-: 78.9 (top 15%)
  - B: 74.1 (top 30%)
  - C: 68 (media)
  - D: 51 (bottom 25%)
  - F: < 51

**SUS — formula calculo**:
- Itens impares (1,3,5,7,9): subtrair 1 da resposta.
- Itens pares (2,4,6,8,10): subtrair resposta de 5.
- Somar e multiplicar por 2.5.

**SUS — sample size**:
- Minimo 20 respostas para media confiavel.
- 50+ para comparar segmentos.
- 2026 trend (Tandfonline meta-analysis): SUS rebound apos slump 2023-2024.

**Outras metricas usabilidade**:
- **NPS (Net Promoter Score)**: lealdade — recomendaria? -100 a +100.
- **CSAT (Customer Satisfaction)**: satisfacao 1-5 ou 1-7.
- **CES (Customer Effort Score)**: facilidade — esforco para resolver tarefa.
- **Task success rate**: % usuarios completam tarefa. > 78% = bom (NN/G).
- **Time on task**: segundos medianos para completar.
- **Error rate**: erros por tarefa.
- **PURE (Pragmatic Usability Rating by Experts)**: 1 expert avalia tarefas em escala 1-3.
- **UMUX-Lite**: SUS reduzida 2 perguntas.
- **TAM (Technology Acceptance Model)**: percepcao de utilidade + facilidade.

**Quantitative vs Qualitative — quando usar cada**:
- Qual: descoberta, "por que".
- Quant: validacao, "quanto".
- Mixed methods (2026 default): qual primeiro, quant valida.

---

## Fundacao 6 — Brasil 2026 Especificidades

**Eventos UX Brasil 2026**:
- **UX Conference Brasil** — evento anual da comunidade UX BR, palestras + workshops, formato hibrido.
- **Cardume UX** — comunidade brasileira de UX research, encontros mensais e materiais em portugues.
- **Aela Institute** — escola de UX/Design Strategy fundada por Sabrina Garcia, cursos em portugues.
- **Mergo** — agencia UX/UI brasileira, blog com cases nacionais.
- **Mente Estrategista** — Fabricio Teixeira (co-host UX Collective), conteudo em portugues.
- **UX Collective BR** — Medium publication, em portugues.
- **Interaction Design Foundation BR community** — IxDF chapter local.

**Cases nacionais 2026 (referencia)**:
- **Nubank**: design system "Aleatorio" open-source, microcopy em portugues claro, onboarding 5min, SUS reportado > 80 (interno).
- **Itau**: app super-app com 30M MAU, redesign 2024 com UX research extensiva (Caio Braga ex-Head Design).
- **Magalu (Magazine Luiza)**: jornada omnichannel "Compre e Retire", LIA chatbot.
- **iFood**: usability testing semanal com 100+ usuarios, A/B testing infra propria.
- **Mercado Livre**: pesquisa quantitativa em escala (>1000 N por estudo), tree testing para taxonomia.
- **Stone**: PMaker B2B com onboarding TDD-driven UX.
- **PicPay**: redesign onboarding 2024 com SUS de 62 -> 76.

**LGPD UX implicacoes (2026)**:
- Consent UX: heuristica nova de transparencia — usuario precisa entender em 1 frase O QUE consente, COMO usar, COM QUEM compartilhar, POR QUANTO tempo.
- Direito de portabilidade: botao "Exportar meus dados" visivel em < 3 cliques.
- Direito de exclusao: botao "Excluir conta" sem labirinto de friccao.
- Cookie banner: ANPD orienta NAO usar dark patterns ("Aceitar todos" destacado vs "Recusar" escondido).
- Microcopy LGPD: "Seus dados sao usados para X" em portugues acessivel, nao juridiques.

**Especificidades culturais BR**:
- Mobile-first absoluto: > 75% trafego BR e mobile.
- WhatsApp-first: jornada B2C frequentemente termina em WhatsApp.
- Pix UX: ja consolidado, mas heuristicas de seguranca (confirmacao, valor maximo, conta receptora visivel) viraram standard.
- Linguagem regional: BR portugues NAO e PT-PT — atencao a ferramentas que so suportam europeu.
- Acessibilidade: 24% brasileiros tem alguma deficiencia (IBGE 2022) — WCAG nao e opcional.
- Nivel digital heterogeneo: mesma persona pode incluir power user de Notion E pessoa que primeira vez usa app bancario aos 65 anos.

---

## Fundacao 7 — Mensuracao + Tools 2026

**Stack UX Research 2026 (categorias)**:

**Usability testing platforms**:
- **Maze** (popular B2B SaaS) — unmoderated + moderated + AI insights. Plano free + pro $99/mo.
- **UserTesting** (gold standard enterprise) — panel proprio + AI Insights + moderated + unmoderated.
- **Lookback** — moderated, video sync, ferramenta classica.
- **Userlytics** — panel proprio em 50+ idiomas inclusive PT-BR.
- **UXtweak** — alternativa europeia, plano free generoso, card sort + tree test + heatmaps.
- **Useberry** — prototipo testing rapido, integra Figma.
- **Lyssna** (ex-UsabilityHub) — surveys + 5-second tests + first-click + preference test.
- **PlaybookUX** — moderated + unmoderated.

**Diary studies + ethnographic**:
- **dscout** — diary studies movel, panel US.
- **Indeemo** — diary studies global.
- **Sticktrue** — alternativa BR (early stage).

**Behavioral analytics + heatmaps**:
- **Hotjar** — heatmaps + recordings + surveys + funnels.
- **FullStory** — session replay + analytics.
- **PostHog** — open-source alternative, autohospedavel.
- **Mixpanel** — product analytics.
- **Amplitude** — product analytics, free ate 10M eventos.
- **Microsoft Clarity** — heatmaps gratis, alternativa Hotjar.

**Survey tools**:
- **Typeform** — UX bonita, pago.
- **Tally** — alternativa free, hospedavel BR.
- **Google Forms** — gratis, basico.
- **SurveyMonkey** — enterprise.
- **Qualtrics** — enterprise + research.

**Repository + analysis**:
- **Dovetail** — research repository + AI tagging + transcript.
- **Condens** — alternativa Dovetail europeia.
- **Notion** — DIY repository, baixo custo.
- **EnjoyHQ** (now UserTesting Insights Hub) — research ops.

**Recruiting**:
- **User Interviews** — recruiting US.
- **Respondent** — recruiting profissional.
- **Prolific** — academic + research.
- **Userlytics panel** — global inclusive BR.
- BR especifico: comunidades Facebook + LinkedIn DM + clientes proprios.

**AI-assisted UX research 2026**:
- Maze AI: gera insights de unmoderated automaticamente.
- Dovetail AI: tematic analysis + summary.
- UserTesting AI Insights: video summarization + sentiment.
- Notably AI: research synthesis.
- Marvin: transcricao + analise.
- Cuidado: AI summary perde nuances; sempre revisar fontes primarias.

**Heatmap tools BR-friendly**:
- Microsoft Clarity (free, dados em servidores Azure).
- Hotjar (HQ Malta, GDPR/LGPD compliant).
- PostHog (autohospedavel — solucao LGPD).

---

## Fundacao 8 — Aplicacao em Content MKT

**5 audiencias e angulos editoriais**:

**1. Founder pre-Series A**:
- Dor: "preciso de UX research mas tenho budget zero e prazo apertado".
- Conteudo: "Como fazer heuristic eval em 1 dia com 0 budget"; "Os 3 testes UX que cabem em 1 sprint"; "Por que o regra-dos-5 salva tempo".
- Canal: LinkedIn long-form, Twitter thread, YouTube Shorts.
- CTA: download checklist heuristic eval Nielsen 10.

**2. PM B2B SaaS**:
- Dor: "como justifico research budget para CFO".
- Conteudo: "ROI de UX research — case Nubank/Itau/iFood"; "SUS como metrica de health do produto"; "Continuous discovery (Teresa Torres) + heuristics".
- Canal: LinkedIn, Substack, Mind The Product community.
- CTA: template SUS + dashboard Mixpanel.

**3. UX designer agencia**:
- Dor: "como vendo heuristic eval para cliente cetico".
- Conteudo: "Deck heuristic eval que fecha contrato"; "Severidade 0-4 traduzida em $ perdidos"; "Case real — heuristic eval -> +18% conversao".
- Canal: LinkedIn, Behance, Dribbble.
- CTA: template proposal + Figma kit.

**4. Product marketer**:
- Dor: "como traduzo bug UX em mensagem feature update".
- Conteudo: "Microcopy + heuristica 9 (recover errors)"; "Release notes que reducem churn"; "Como anunciar redesign sem perder users".
- Canal: ProductHunt, LinkedIn, blog corporativo.
- CTA: framework comunicacao UX changes.

**5. Researcher**:
- Dor: "como organizo 10 estudos por trimestre sem virar caos".
- Conteudo: "Research repository (Dovetail/Notion)"; "Triangulacao quant+qual"; "Atomic research (Tomer Sharon)".
- Canal: ResearchOps community, UX Research Conference, Cardume.
- CTA: template repository + taxonomia tags.

**Formato editorial recomendado**:
- LinkedIn carousel 8-10 slides com Nielsen 10 (visual + 1 caso BR por heuristica).
- YouTube long-form 12-20min "Como rodar heuristic eval do zero".
- Newsletter semanal com 1 heuristica + 1 case BR + 1 anti-pattern.
- Twitter thread 12-15 tweets com SUS step-by-step.

---

## Anti-Patterns 18

1. **"Heuristic eval substitui usability test"**. Errado — sao complementares. Eval pega problemas obvios; test pega problemas reais com usuario.
2. **"5 usuarios e pouco — preciso de 50"**. Errado para qualitativo. Lei retorno decrescente — 5 ja entrega 85% problemas.
3. **"SUS abaixo de 68 e fracasso"**. 68 e MEDIA historica generica — varia por categoria (digital health < produtividade SaaS < e-commerce).
4. **"Heuristic eval sozinho — sem severidade"**. Lista sem severidade vira backlog infinito. SEMPRE 0-4 + esforco fix + impacto.
5. **"Pular cognitive walkthrough porque heuristic eval ja foi feito"**. Walkthrough pega LEARNABILITY (1o uso), heuristic pega CONFORMIDADE. Diferentes.
6. **"Persona criada sem entrevistar 1 usuario real"**. Buyer persona fictional viola heuristica 2 (match real world) na origem.
7. **"Contratar so 1 avaliador para heuristic eval"**. NN/G — minimo 3 avaliadores; 1 acha so 35% problemas.
8. **"Usar Nielsen 10 sem adaptar para AR/VR/voice"**. Heuristicas precisam adaptacao para modalidade.
9. **"Ignorar LGPD em UX research"**. Consent de gravacao e mandatorio; transcricoes sao dados pessoais.
10. **"AI-assisted summary substitui leitura de transcript"**. Summary perde nuances; sempre validar com fonte.
11. **"Confundir UX research com user testing"**. Research e amplo (discovery + descriptive + evaluative); testing e so evaluative.
12. **"Pesquisa qualitativa em escala (n=200)"**. Saturacao acontece em ~12-15 entrevistas (Guest et al 2006); mais e desperdicio.
13. **"Pesquisa quantitativa com n=10"**. Sem significancia. Min 100; ideal 384 (95% IC ±5%).
14. **"Microcopy traduzido sem context"**. PT-BR != PT-PT, e nao basta Google Translate. Validar com falante nativo.
15. **"Heuristica 5 (error prevention) virando friccao excessiva"**. Confirmar TUDO afasta usuario expert. Balancear com heuristica 7 (efficiency).
16. **"Aceitar SUS auto-reportado como verdade absoluta"**. SUS mede percepcao, nao realidade. Triangular com task success + analytics.
17. **"Inventar estatisticas sem fonte"**. "75% dos usuarios..." sem citar e jornalismo lixo. SEMPRE referenciar NN/G/MeasuringU/etc.
18. **"Auditar heuristicas sem medir antes/depois"**. Sem baseline (SUS/conversao) antes do fix, ROI nao mensuravel.

---

## 18 Regras de Ouro

1. **Triangule SEMPRE 3 fontes**: heuristic eval (expert) + usability test (user) + analytics (real). Nunca confie em uma so.
2. **Severidade 0-4 obrigatoria** em todo achado. Sem severidade nao ha priorizacao.
3. **5 usuarios para qualitativo, 100+ para quantitativo, 20+ para SUS**. Memorize.
4. **Combine heuristic eval + cognitive walkthrough** quando produto critico (checkout, onboarding, signup).
5. **Mida SUS antes E depois** de qualquer redesign. Sem baseline, sem ROI.
6. **Recrute 3-5 avaliadores** para heuristic eval, todos UX practitioners. Solo eval pega < 40%.
7. **Documente metodo** — quem, quando, n, criterios recrutamento. Sem isso nao reproduz.
8. **Use Nielsen 10 como ponto de partida**, mas adapte para sua modalidade (AR/voice/agentic).
9. **LGPD compliance em research**: consent escrito de gravacao, anonimizacao de transcript, data retention policy.
10. **Mixed methods 2026 default**: qual primeiro (descobrir), quant depois (validar).
11. **Continuous discovery** (Teresa Torres) — research nao e fase, e habito semanal.
12. **Atomic research** (Tomer Sharon): 1 fato + 1 evidencia + 1 insight, taggeado em repository.
13. **Defina contexto** ISO 9241-11: usuario + tarefa + ambiente. Sem contexto, "usavel" nao tem sentido.
14. **PT-BR nao e PT-PT** — valide microcopy com falante nativo brasileiro.
15. **Mobile-first BR**: 75%+ trafego mobile. Teste prioritariamente em iPhone SE / Android budget (1280x720, 4G lento).
16. **Acessibilidade nao e opcional**: 24% brasileiros tem alguma deficiencia. Cross-skill `acessibilidade-wcag`.
17. **Disclaimer legal**: heuristic eval educational, nao substitui auditoria UX profissional NN/G/Forrester.
18. **Iteracao curta**: research insights -> design changes -> test -> iterate. Ciclos de 2-4 semanas, nao 6 meses.

---

## Exemplos Comportamentais

### Persona 1 — Founder pre-Series A (B2B SaaS, 18 funcionarios, $800k ARR)

**Contexto**: Carolina, fundadora de SaaS de gestao para clinicas odontologicas (Sao Paulo). 80 clinicas pagantes. Churn rate 4.5% mensal (alto). Investidores apontaram "onboarding fraco" no due diligence. Budget research = R$ 0. Time = 1 PM, 2 devs, 1 designer half-time.

**Diagnostico**:
- Heuristica 1 (visibility) violada — onboarding tem 12 passos sem progress bar.
- Heuristica 6 (recognition vs recall) violada — usuario precisa decorar codigo de procedimento odontologico.
- Heuristica 9 (recover errors) violada — erro generico "Falha ao salvar" sem acao.
- SUS estimado < 60 (sem benchmark formal ainda).
- Cognitive walkthrough: nas 4 perguntas Wharton, na acao 3 e 5 do onboarding usuario PROVAVELMENTE NAO tentaria.

**Recomendacao plano (4 semanas)**:
- Semana 1: heuristic eval interna com 3 avaliadores (Carolina + designer + 1 PM consultivo amigo). Lista 30 problemas, severidade 0-4. Foco em severidade 3-4.
- Semana 2: usability test moderated com 5 dentistas reais (clientes existentes). 30min sessao via Zoom. Tarefa = onboarding completo + cadastrar 1 paciente. Maze ou Lookback (free trial).
- Semana 3: SUS survey com 30 clientes existentes. Baseline.
- Semana 4: priorizar top 5 fixes severidade 4. Implementar. Re-test SUS apos 2 semanas.

**KPIs**:
- SUS antes vs depois — meta + 10 pontos.
- Onboarding completion rate — meta + 15pp.
- Churn 4.5% -> 3.5% em 90 dias.
- Tickets suporte sobre onboarding — meta -50%.

**Riscos**:
- Avaliadores nao-experts em UX podem nao identificar todos problemas — Carolina compensa lendo NN/G + buscando 1 mentor UX.
- N=5 nao detecta problemas raros — aceitavel para 1a iteracao.
- Implementacao pode introduzir novos bugs — testes regressivos.

**Disclaimer**: Esta orientacao e educational. Para due diligence formal de investidor recomenda-se auditoria UX profissional (Aela, Mergo, NN/G).

---

### Persona 2 — PM B2B SaaS (Series B, 200 funcionarios, $40M ARR)

**Contexto**: Rafael, Senior PM de plataforma de e-commerce HQ Sao Paulo. Time produto 12 pessoas. Cliente CFO pressionando para reduzir custos research (atualmente $80k/ano). Rafael precisa demonstrar ROI.

**Diagnostico**:
- Stack atual: UserTesting ($30k), Maze ($12k), Dovetail ($15k), recruiting Respondent ($15k), tools heatmap Hotjar ($8k). Total $80k.
- 6 estudos por trimestre, mas 30% nao foram usados em decisao de produto (research debt).
- Sem KPI de research impact.
- SUS medido so em 2024 (74), nao revalidado.

**Recomendacao plano (1 trimestre)**:
- Mes 1: auditoria de research debt — quais studies foram acionados, ROI por estudo. Cortar 30% nao acionavel.
- Mes 2: implementar continuous discovery (Torres). Weekly user touchpoints. SUS quarterly como north star metric.
- Mes 3: research repository consolidado (Dovetail). Atomic research taxonomy. Cross-team access.

**Stack otimizado** (proposta CFO):
- UserTesting -> Maze (substituir): -$18k.
- Dovetail manter: +$15k.
- Hotjar -> Microsoft Clarity (free): -$8k.
- Total novo: $46k. Reducao 42% mantendo capacidade.

**KPIs**:
- SUS baseline -> + 4pts em 12 meses.
- % de studies acionados em decisao de produto: 70% -> 90%.
- Time-to-insight: 14d -> 7d.
- Research budget / ARR ratio: 0.2% -> 0.11%.

**Riscos**:
- CFO pode cortar mais — Rafael apresenta caso ROI por estudo.
- Maze tem menos panel BR que UserTesting — compensar com recruiting interno (clientes).
- Atomic research exige treino de time — 1 workshop com Tomer Sharon course (Sudden Compass).

**Disclaimer**: Recomendacoes baseadas em frameworks publicos. Decisoes finais de stack devem considerar contratos vigentes + compliance LGPD especifico do produto.

---

### Persona 3 — UX Designer em Agencia (Belo Horizonte, 8 designers)

**Contexto**: Larissa, Senior UX Designer em agencia digital BH. Cliente novo (rede de farmacias regional, 40 lojas, e-commerce 2 anos) pediu "redesign do site". Larissa quer vender HEURISTIC EVAL antes do redesign para basear escopo. Cliente cetico — "quero ver mockups".

**Diagnostico**:
- Site cliente: SUS auto-estimado por equipe = 55. Conversao mobile 0.8% (benchmark farma BR ~1.8%).
- Heuristica 4 (consistency) violada — 3 estilos de botao "comprar" diferentes.
- Heuristica 5 (error prevention) violada — carrinho perde itens em troca de CEP.
- Heuristica 9 (recover errors) violada — "Endereco nao encontrado" sem sugestao alternativa.

**Recomendacao plano (proposta de 6 semanas)**:
- Semana 1-2: heuristic eval + cognitive walkthrough (3 avaliadores Larissa + 2 colegas). Output: relatorio 30-50 problemas.
- Semana 3: usability test moderated com 8 usuarios (4 desktop + 4 mobile). Tarefa = comprar 3 produtos diferentes + buscar farmacia mais proxima.
- Semana 4: SUS survey com 50+ clientes existentes (email blast). Baseline numerico.
- Semana 5-6: deck final com problemas priorizados + roadmap fix + estimativa de uplift conversao.

**Entregaveis**:
- Relatorio heuristic eval (30 paginas).
- Video highlights usability test (8 sessoes editadas em 15min cada).
- SUS baseline report.
- Roadmap priorizado severidade 3-4.
- Proposta redesign Fase 2.

**KPIs do projeto**:
- 30+ problemas identificados, classificados 0-4.
- Top 10 fixes com estimativa esforco + impacto.
- SUS meta pos-redesign: 75 (de 55).
- Conversao mobile meta: 1.5% (de 0.8%).

**Riscos**:
- Cliente impaciente — Larissa apresenta deck com cases (Magalu/iFood).
- N=8 usability test pode nao representar persona idosa (heavy em farma) — recrutar especificamente 2 acima de 60 anos.
- Recommendation gap: avaliacao identifica problemas, redesign e Fase 2 separada (escopo + budget).

**Disclaimer**: Heuristic eval e cognitive walkthrough sao tecnicas estabelecidas. Proposta comercial deve ser validada por contrato + escopo formal. Larissa nao substitui auditoria UX certificada NN/G.

---

### Persona 4 — Agencia Brasileira de Performance + UX (Sao Paulo, 25 funcionarios)

**Contexto**: Agencia "PerfX" atende 12 clientes B2C brasileiros (varejo, fintech, edtech). CMO da agencia quer adicionar servico de UX research como upsell. Time atual: 18 performance, 4 design, 3 dev. 0 UX researcher dedicado.

**Diagnostico**:
- Demanda latente: 8 dos 12 clientes mencionaram "queria mais user research" em pesquisa NPS interna.
- Concorrentes BR (Aela, Mergo) cobram R$ 30-80k por estudo.
- PerfX nao tem researcher senior — gap.
- Stack atual: GA4 + Hotjar + ClickUp.

**Recomendacao plano (6 meses)**:
- Mes 1: contratar 1 UX researcher senior (R$ 12-18k mes pleno BR 2026) + investir em treinamento Aela (R$ 5k/colaborador para 2 designers).
- Mes 2: pacote piloto "UX Audit" para 2 clientes ancora — heuristic eval + 5-user usability test + SUS baseline. Preco R$ 15k cada (50% margin pos-CAC).
- Mes 3: case study + portfolio. Lancamento publico do servico.
- Mes 4-6: meta 4 contratos UX Audit. Upsell research continuo (Maze + Dovetail) para clientes ancora.

**Stack PerfX UX (proposta)**:
- Maze ($99/mes) — usability testing.
- Dovetail ($79/mes) — repository.
- Microsoft Clarity (free) — heatmaps.
- Recruiting via base clientes existentes (cost-effective BR).
- Lyssna ($75/mes) — surveys + 5-second test.
- Total stack: ~$3k/ano.

**KPIs**:
- 4 contratos UX Audit em 6 meses (R$ 60k receita).
- 2 contratos research continuo (R$ 8k/mes recorrente cada).
- NPS clientes existentes: 42 -> 55.
- Hire researcher senior + 2 designers treinados.

**Riscos**:
- Researcher senior escasso BR — networking Cardume + UX Conference Brasil.
- Clientes B2C podem nao priorizar research vs media — case ancora (ROI 6x em 12 meses) e essencial.
- Concorrencia Aela/Mergo + freelancers — diferencial PerfX = integracao com performance media (0 hand-off).

**Disclaimer**: Recomendacoes mercadologicas. Salarios e precos referencia BR 2026 — variam por regiao + senioridade + contexto. Validar com consultoria comercial especializada.

---

## Checklist Contraditorio Interno (10 perguntas)

Antes de publicar conteudo educational sobre UX heuristicas, Claude deve responder honestamente:

1. **Estou inventando estatisticas?** Toda numero deve ter fonte (NN/G, MeasuringU, IBGE, ISO). Se nao tenho fonte, NAO uso o numero.
2. **Estou confundindo heuristic eval com usability test?** Sao tecnicas distintas. Eval = expert review. Test = user real.
3. **Estou aplicando Nielsen 10 sem adaptar contexto?** Voice, AR/VR, agentic AI exigem reinterpretacao.
4. **Estou ignorando LGPD em research methods?** Consent gravacao + anonimizacao + retention.
5. **Estou prometendo ROI sem caveat?** Resultados variam por produto, mercado, time, baseline.
6. **Estou tratando 5 usuarios como dogma absoluto?** Funciona para qualitativo unica persona; produtos heterogeneos exigem 5 por persona.
7. **Estou esquecendo BR especificidades?** Mobile-first 75%, WhatsApp-first, Pix UX, PT-BR != PT-PT.
8. **Estou misturando severidade Nielsen 0-4 com WCAG conformance levels (A, AA, AAA)?** Sao escalas diferentes.
9. **Estou recomendando ferramentas sem caveat de custo + LGPD?** Maze, UserTesting tem servidores internacionais.
10. **Estou substituindo legal review LGPD ou auditoria profissional NN/G?** NUNCA. Skill educational, nao consultoria certificada.

---

## Referencias

### Nielsen Norman Group (NN/G) — fonte canonica
- [10 Usability Heuristics for User Interface Design (NN/G)](https://www.nngroup.com/articles/ten-usability-heuristics/)
- [How to Conduct a Heuristic Evaluation (NN/G)](https://www.nngroup.com/articles/how-to-conduct-a-heuristic-evaluation/)
- [Severity Ratings for Usability Problems (NN/G)](https://www.nngroup.com/articles/how-to-rate-the-severity-of-usability-problems/)
- [Why You Only Need to Test with 5 Users (NN/G)](https://www.nngroup.com/articles/why-you-only-need-to-test-with-5-users/)
- [Remote Usability Tests (NN/G)](https://www.nngroup.com/articles/remote-usability-tests/)
- [Cognitive Walkthroughs (NN/G)](https://www.nngroup.com/articles/cognitive-walkthroughs/)
- [User Interviews 101 (NN/G)](https://www.nngroup.com/articles/user-interviews/)
- [The Definition of User Experience (UX) (NN/G)](https://www.nngroup.com/articles/definition-user-experience/)
- [Usability 101 Introduction to Usability (NN/G)](https://www.nngroup.com/articles/usability-101-introduction-to-usability/)
- [Card Sorting (NN/G)](https://www.nngroup.com/articles/card-sorting-definition/)
- [Tree Testing (NN/G)](https://www.nngroup.com/articles/tree-testing/)
- [Diary Studies (NN/G)](https://www.nngroup.com/articles/diary-studies/)

### MeasuringU (Sauro & Lewis) — metricas + SUS
- [Measuring Usability with the System Usability Scale SUS (MeasuringU)](https://measuringu.com/sus/)
- [Heuristic Evaluation vs Cognitive Walkthrough (MeasuringU)](https://measuringu.com/he-cw/)
- [SUS A Quick and Dirty Usability Scale Brooke 1986 (PDF)](https://digital.ahrq.gov/sites/default/files/docs/survey/systemusabilityscale%2528sus%2529_comp%255B1%255D.pdf)
- [System Usability Scale Wikipedia](https://en.wikipedia.org/wiki/System_usability_scale)
- [System Usability Scale Meta-Analysis Workload Task Time Error Rate (Tandfonline 2026)](https://www.tandfonline.com/doi/full/10.1080/10447318.2026.2625260)
- [SUS Benchmarking Digital Health Apps Meta-analysis (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9437782/)
- [System Usability Scale ScienceDirect](https://www.sciencedirect.com/topics/computer-science/system-usability-scale)

### Heuristic Evaluation deep
- [Nielsens 10 Usability Heuristics Heurio](https://www.heurio.co/nielsens-10-usability-heuristics)
- [Nielsens 10 Usability Heuristics Examples Blog UX](https://blog-ux.com/en/jakob-nielsen-s-10-usability-heuristics/)
- [UX Audit Checklist Nielsen 10 Heuristics Eleken](https://www.eleken.co/blog-posts/a-checklist-for-ux-design-audit-based-on-jakob-nielsens-10-usability-heuristics)
- [Heuristic Evaluation vs Cognitive Walkthrough Gaps Studio](https://gapsystudio.com/blog/cognitive-walkthrough-vs-heuristic-evaluation/)
- [Cognitive Walkthrough Wikipedia](https://en.wikipedia.org/wiki/Cognitive_walkthrough)
- [Comparative Study Heuristic Evaluation Cognitive Walkthrough E-Government Springer 2025](https://link.springer.com/article/10.1007/s13369-025-09980-4)
- [Heuristic Evaluation Cognitive Walkthrough Health Information System PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9206256/)

### UX Research Methods — guias 2026
- [UX Research Methods Complete 2026 Guide Userlytics](https://www.userlytics.com/resources/blog/ux-research-methods/)
- [UX Research Methods 2026 Limeup](https://limeup.io/blog/ux-research-methods/)
- [UX Research Methods Lyssna](https://www.lyssna.com/guides/ux-research/ux-research-methods/)
- [10 Essential UX Research Tools 2026 Qualtrics](https://www.qualtrics.com/articles/strategy-research/ux-research-tools/)
- [UX Research Tools Map 2026 User Interviews](https://www.userinterviews.com/ux-research-tools-map)
- [UX Research Method Selection Tool User Interviews](https://www.userinterviews.com/which-ux-research-methods)
- [Qualitative UX Testing Methods Greenbook](https://www.greenbook.org/insights/qualitative-market-research/from-interviews-to-usability-tests-qualitative-ux-methods-explained)
- [Diary Studies UX Research User Interviews](https://www.userinterviews.com/ux-research-field-guide-chapter/diary-studies)
- [Card Sorting User Interviews](https://www.userinterviews.com/ux-research-field-guide-chapter/card-sorting)
- [UX Research Methods Discovery User Interviews](https://www.userinterviews.com/ux-research-field-guide-module/discovery-methods)

### Usability Testing 2026
- [Usability Testing Guide 2026 Methods Research Plans Parallel](https://www.parallelhq.com/blog/how-to-do-usability-testing)
- [Moderated vs Unmoderated Usability Testing Maze](https://maze.co/guides/usability-testing/moderated-vs-unmoderated/)
- [Moderated vs Unmoderated Usability Testing UserTesting](https://www.usertesting.com/blog/moderated-vs-unmoderated-usability-testing)
- [What Is Usability Testing Remote Moderated Unmoderated UserTesting](https://help.usertesting.com/hc/en-us/articles/11880447418781-What-Is-Usability-Testing-for-Remote-Moderated-and-Remote-Unmoderated-Tests)
- [Usability Testing Tools 12 Best Unmoderated 2026 CleverX](https://cleverx.com/blog/usability-testing-tools-12-best-unmoderated-platforms-for-2026/)
- [16 Best Unmoderated Usability Testing Tools 2026 Trymata](https://trymata.com/blog/unmoderated-usability-testing-tools/)
- [Unmoderated Usability Testing Tools Benefits Lyssna](https://www.lyssna.com/blog/unmoderated-usability-testing/)
- [Usability Testing Moderated vs Unmoderated Nick Babich Medium](https://medium.com/thinking-design/usability-testing-moderated-vs-unmoderated-adbccc37404b)

### UX Conferences + Comunidades
- [UX Design Conferences 2026 IxDF](https://ixdf.org/literature/article/ux-conferences-calendar)
- [List UX UI Conferences 2026 Qubika](https://qubika.com/blog/list-of-ux-ui-conferences-2026/)
- [UX Conference Guide 2026 Condens](https://condens.io/guides/ux-conference-guide-2026/)
- [PUSH UX Conference 2026 Europe](https://push-conference.com/)
- [UX Research Conference UXinsight Festival 2026](https://uxinsight.org/ux-research-conference-festival/)
- [Top UI UX Design Conferences 2026 DesignRush](https://www.designrush.com/agency/ui-ux-design/trends/ui-ux-conferences)
- [11 Best UX Conferences 2026 CPO Club](https://cpoclub.com/product-design/best-ux-conferences/)
- [UX Conferences 2026 UIUX Trend](https://uiuxtrend.com/events/category/ux-conferences-2026/)

### Brasil + Latam
- [UX Collective BR Medium](https://uxdesign.cc/)
- [Aela Institute UX Design Strategy](https://aela.io/)
- [Mergo UX Design Brasil](https://www.mergo.com.br/)
- [Cardume UX Comunidade Brasileira UX Research](https://www.linkedin.com/company/cardume-ux/)
- [Mente Estrategista Fabricio Teixeira](https://menteestrategista.com.br/)
- [Interaction Design Foundation Sao Paulo Local](https://www.interaction-design.org/community/local-groups)

### Frameworks classicos
- [Krug Steve Don't Make Me Think 3rd Edition](https://sensible.com/dont-make-me-think/)
- [ISO 9241-11 Ergonomics Usability Definition](https://www.iso.org/standard/63500.html)
- [Cognitive Walkthrough Wharton et al 1994 Original](https://en.wikipedia.org/wiki/Cognitive_walkthrough)
- [Nielsen Heuristics 1994 Original Paper CHI](https://dl.acm.org/doi/10.1145/191666.191729)
- [Norman Don Design of Everyday Things](https://www.basicbooks.com/titles/don-norman/the-design-of-everyday-things/9780465050659/)
- [Continuous Discovery Habits Teresa Torres](https://www.producttalk.org/continuous-discovery-habits/)
- [Atomic Research Tomer Sharon](https://www.useberry.com/blog/atomic-research/)

### Ferramentas modernas — Maze + Dovetail + Hotjar + UserTesting
- [Maze Usability Testing Platform](https://maze.co/)
- [UserTesting Platform](https://www.usertesting.com/)
- [Lookback Moderated Testing](https://www.lookback.com/)
- [Userlytics Panel Multilingual](https://www.userlytics.com/)
- [UXtweak European Alternative](https://www.uxtweak.com/)
- [Useberry Prototype Testing](https://www.useberry.com/)
- [Lyssna Surveys 5-Second Tests](https://www.lyssna.com/)
- [Hotjar Heatmaps Behavior Analytics](https://www.hotjar.com/)
- [FullStory Session Replay](https://www.fullstory.com/)
- [Microsoft Clarity Free Heatmaps](https://clarity.microsoft.com/)
- [PostHog Open Source Product Analytics](https://posthog.com/)
- [Dovetail Research Repository](https://dovetail.com/)
- [Optimal Workshop Card Sort Tree Test](https://www.optimalworkshop.com/)
- [User Interviews Recruiting Field Guide](https://www.userinterviews.com/)
- [Respondent Recruiting Professional](https://www.respondent.io/)

### LGPD + Acessibilidade BR
- [LGPD Lei 13709 2018 Texto Oficial Planalto](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm)
- [ANPD Autoridade Nacional Protecao Dados](https://www.gov.br/anpd/pt-br)
- [WCAG 2.2 W3C](https://www.w3.org/WAI/standards-guidelines/wcag/)
- [Gov.br Design System](https://gov.br/ds/)

---

## Cross-Skill References

### Bloco UX/UI (irmas)
- `microcopy` — heuristica 9 (recover errors), 2 (match real world), 6 (recognition) atravessam microcopy.
- `acessibilidade-wcag` — WCAG 2.2 nao e opcional BR (24% deficiencia). Heuristica 4 (consistency) + 9 (recover errors) cruzam.
- `design-system-basico` — heuristica 4 (consistency) e nucleo de design system. Tokens + componentes + patterns reduzem inconsistencia.

### Bloco Pesquisa & Inteligencia (predecessor)
- `persona-icp-deep` — personas alimentam usability testing. JTBD informa task definition em cognitive walkthrough.
- `pesquisa-mercado-fundamentos` — UX research e subset de market research. Mesma rigor metodologico.
- `analise-concorrencia` — heuristic eval competitiva = comparar nosso produto vs concorrente em mesmo set de heuristicas.

### Bloco Branding + Posicionamento
- `posicionamento-marca` — heuristica 2 (match real world) deve refletir tom de voz da marca.
- `branding` — design system aplicado a marca; heuristica 4 (consistency) e fundacao.
- `big-idea` — landing pages testadas com heuristic eval + 5-second test antes lancamento.

### Bloco Funil + Jornada
- `funil-jornada` — usability test mapeia friccoes em cada stage do funil. SUS por stage.
- `metricas-marketing` — SUS, NPS, CSAT cruzam com metricas marketing (CAC, LTV, churn).
- `copywriting-conversao` — A/B testing de copy + heuristic eval de CTA.

### Bloco IA + Tecnicas
- `tecnicas-ia-claude-gemini-mkt` — Claude pode ajudar em research synthesis; cuidado com vies de summary.

### Bloco Vertical (mercados)
- `dominio-juridico-mkt` — UX research em SaaS juridicos exige adaptar regulamentacao OAB.
- `dominio-financeiro-mkt` — UX em fintechs exige cuidados extras (Bacen, LGPD, segurança).

### Bloco Conteudo
- `conteudo-evergreen` — guias UX heuristics sao evergreen (10+ anos relevancia).
- `storytelling` — usability test highlights = storytelling do usuario.

---

## Integracao Ecossistema Frank-MKT

**Esta skill e a 1a do Bloco UX/UI** dentro do Frank-MKT (plugin Claude Code para marketing). Sequencia recomendada:

1. **Comecar aqui (`ux-heuristicas`)** para entender fundamentos.
2. Avancar para `microcopy` (linguagem em interface).
3. Avancar para `acessibilidade-wcag` (compliance BR + ETHICS).
4. Avancar para `design-system-basico` (consistencia em escala).

**Trigger no Claude Code**: usuario pergunta sobre "UX", "usabilidade", "Nielsen", "SUS", "heuristic", "user research", "usability test", "cognitive walkthrough" -> Claude carrega esta skill.

**Output recomendado pelo Claude usando esta skill**:
- Heuristic eval template em Markdown (10 heuristicas + severidade 0-4 + screenshot placeholder + recomendacao).
- SUS calculator template (Google Sheets formula).
- Usability test script template (intro + tarefas + post-task questions + SUS).
- Cognitive walkthrough worksheet (4 perguntas Wharton por acao).
- Research repository structure (Notion ou Dovetail).

**Nao-objetivos do Claude com esta skill**:
- NAO substituir auditoria UX certificada NN/G/Forrester.
- NAO substituir pesquisa profissional Aela/Mergo/UserVoice.
- NAO produzir compliance LGPD review (aponta caminhos, nao certifica).
- NAO substituir certificacao Nielsen Norman Group UX Master.

**Cadencia esperada de uso**:
- Founder/PM: 2-4 vezes por mes (planejar research + analisar resultados).
- UX designer agencia: semanal (proposals + execution).
- Product marketer: mensal (interpretar findings para messaging).
- Researcher: diario (operacional).

---

## Disclaimer Educational

Esta skill e **educational**. Conteudo apresenta frameworks publicos (Nielsen 10, ISO 9241-11, SUS Brooke 1986, Cognitive Walkthrough Wharton, regra dos 5 usuarios) com aplicacao pratica para founders, PMs, UX designers, product marketers e researchers atuando no contexto Brasil 2026.

**NAO substitui**:
- Auditoria UX profissional certificada Nielsen Norman Group, Forrester, ou equivalente.
- Consultoria UX research especializada (Aela Institute, Mergo, UserVoice, ou equivalentes).
- Certificacao formal NN/G UX Master (700+ horas treinamento).
- Compliance review LGPD por advogado especializado em direito digital.
- Auditoria de acessibilidade WCAG por especialista certificado.

**Decisoes baseadas nesta skill devem ser validadas com**:
- Profissional UX senior em sua organizacao ou consultoria.
- Compliance officer LGPD em sua organizacao.
- Especialista em acessibilidade WCAG (parceiros como SerProDigital, MovimentoWeb).
- Mentor ou consultor com experiencia em produto similar (B2B SaaS, B2C e-commerce, fintech, healthtech, etc).

**Estatisticas e benchmarks** apresentados sao referenciados a fontes publicas (NN/G, MeasuringU, ISO, IBGE, papers academicos). Numeros sem fonte explicita NAO devem ser usados em deck investidor sem validacao independente.

**Atualizacao**: skill revisada a cada 6 meses. Verificar campo `last_review` antes de uso em conteudo publicado. Heuristicas para agentic AI (Claude Computer Use, ChatGPT Agents) e voice/AR/VR estao em evolucao rapida 2024-2026.

Conteudo desta skill e para fins educativos. Nao constitui aconselhamento profissional, juridico ou compliance regulatorio.
