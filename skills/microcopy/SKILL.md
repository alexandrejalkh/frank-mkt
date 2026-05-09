---
name: microcopy
description: Microcopy estrategico (button labels + error messages + form labels + empty states + onboarding + 404 pages + voice/tone UI) para UX writers/PMs/designers/founders, com cobertura Kinneret Yifrah Microcopy book canonico, Mailchimp Voice & Tone foundational, Atlassian/Shopify/Stripe content guidelines, Brasil 2026 (PT-BR localization + tu vs voce + tom voz), 2026 trends (AI UX writing + voice interfaces + dark patterns avoidance ethical microcopy). 2a SKILL Bloco UX/UI.
volatility: medium
last_review: 2026-05-09
next_review: 2026-11-09
languages: [pt-BR]
audience: [UX-writers, PMs, designers, founders, content-strategists, product-marketers]
ascii_only: true
---

# Skill: microcopy

## Decaimento Temporal

> Ultima verificacao: 2026-05-09 | Proxima revisao: 2026-11-09 | Volatility: **medium** (6 meses)
> Microcopy = disciplina consolidada por Kinneret Yifrah (book "Microcopy: The Complete Guide" 1st ed 2017, 2nd ed 2019) + Mailchimp Voice & Tone (2014+) + Atlassian/Shopify/Stripe content guidelines. Fundamentos timeless (4 Cs: clear/concise/conversational/contextual). Tendencias 2026 (AI UX writing emergence + voice interfaces + dark patterns regulamentadas EU AI Act + LGPD UX implications BR) requerem revisao semestral. Style guides de produto sao atualizados continuamente — re-validar referencias a cada 6 meses.
>
> **Re-validar a cada 6 meses:**
> - Microcopy Book (Kinneret Yifrah) — https://www.microcopybook.com/
> - Mailchimp Content Style Guide — https://styleguide.mailchimp.com/
> - Atlassian Design System — Voice & Tone — https://atlassian.design/content/voice-and-tone
> - Shopify Polaris — Content guidelines — https://polaris.shopify.com/content
> - UX Writing Hub — https://uxwritinghub.com/
> - NN/g Tone of Voice — https://www.nngroup.com/articles/tone-of-voice-dimensions/
> - GOV.BR Padroes Writing — https://www.gov.br/ds/padroes/writing/microcopy
>
> **Acionamento:** redesign de produto (botoes + forms + erros + estados vazios + 404 + onboarding); criacao de style guide voice & tone para nova marca; revisao de copy de UI antes de release; correcao de erros frequentes em forms (drop-off alto); design de empty states para feature nova; onboarding de usuarios novos; pagina 404 com personalidade; review de pop-ups + tooltips + helper text; tradumigracao PT-BR de produto SaaS internacional; auditoria de dark patterns + microcopy etico; padronizacao de mensagens de erro em codebase legado; brief para UX writer dedicado; mentoria de designer/PM em writing skills basicas.
>
> **Skills relacionadas:** `ux-heuristicas` (anterior bloco UX/UI — fundamentos heuristicos onde microcopy aplica); `acessibilidade-wcag` (proxima bloco — labels acessiveis, ARIA, screen readers); `design-system-basico` (proxima bloco — tokens de copy, componentes com microcopy padronizado); `branding` + `posicionamento-marca` (bloco Marketing & Estrategia — voice deriva da identidade de marca); `redacao-publicitaria` + `copywriting-conversao` (bloco Copy & Redacao — irmas mas com objetivos distintos: copy = vendas, microcopy = navegacao/uso); `tecnicas-ia-claude-gemini-mkt` (AI UX writing + drafting + variantes de microcopy).
>
> **Pre-requisito:** brand voice documentada (ou em construcao); persona/ICP definidos; jornada de produto mapeada; design system (mesmo basico) com componentes principais; analytics ativo (Hotjar/UXcam/PostHog/Amplitude) para identificar friction points; stakeholders (PM + designer + dev + UX writer + legal/compliance + acessibilidade champion).
>
> **STATUS BLOCO:** esta skill e a **2a** do **Bloco UX/UI** — junto com `ux-heuristicas` (1a) e proximas (`acessibilidade-wcag`, `design-system-basico`, etc.) **2/N do bloco**.

---

## Visao Geral

Microcopy = **textos pequenos da interface** que guiam o usuario, reduzem friccao, previnem erros e dao personalidade ao produto. NAO e advertising copy (vendas) NEM long-form content (artigos). E **a voz do produto em uso** — botoes, mensagens de erro, labels de forms, estados vazios, tooltips, paginas 404, dialogos de confirmacao, helper text, onboarding tooltips, notificacoes.

Diferenca critica vs outras disciplinas de copy:

```
COPY x MICROCOPY x CONTENT

ADVERTISING COPY (redacao publicitaria)
   Objetivo: brand awareness, memorabilidade, vendas
   Formato: anuncios, slogans, manifestos
   Persona: redator publicitario (Bernbach, Ogilvy)
   Tom: emocional, aspiracional, persuasivo

DIRECT RESPONSE COPY (copywriting conversao)
   Objetivo: acao imediata (lead, compra, clique)
   Formato: landing pages, emails de venda, ads
   Persona: copywriter direto (Schwartz, Halbert)
   Tom: persuasivo, urgencia, beneficio claro

MICROCOPY (UX writing)
   Objetivo: navegacao + reducao friccao + uso eficaz
   Formato: botoes, erros, labels, estados, tooltips
   Persona: UX writer (Yifrah, Mailchimp content team)
   Tom: claro, conciso, contextual, conversacional

CONTENT MARKETING (long-form)
   Objetivo: educacao + autoridade + SEO
   Formato: artigos, guias, white papers
   Persona: content writer
   Tom: explicativo, didatico, profundo
```

Esta skill cobre **8 fundacoes** + Brasil 2026 + 5 audiencias de aplicacao MKT.

### Acionamento

| Gatilho | Exemplo |
|---------|---------|
| Redesign produto | "Refazer copy de UI antes do release" |
| Style guide novo | "Voice & tone para marca nova" |
| Erro alto em form | "20% drop-off no signup — revisar erros" |
| Empty state desenhado | "Dashboard vazio precisa de copy + CTA" |
| Onboarding inicial | "Primeiros 60s — tooltips + tour" |
| Pagina 404 | "404 generica — criar versao com personalidade" |
| Pop-ups + tooltips | "Tooltip aparece tarde demais — revisar timing + texto" |
| Localizacao PT-BR | "Produto SaaS USA traduzido sem contexto BR" |
| Dark patterns audit | "Botao cinza vs azul, copy enviesado — revisar etica" |
| Padronizacao codebase | "10 mensagens de erro diferentes para mesmo erro" |
| Mentoria designer/PM | "Designer escrevendo copy sem framework" |
| Acessibilidade copy | "Screen reader le labels confusos" |

### Pre-requisitos

- [ ] **Brand voice documentada** (ou esta skill ajuda construir).
- [ ] **Persona/ICP** definidos (tom muda por audiencia).
- [ ] **Jornada de produto** mapeada (copy contextual por etapa).
- [ ] **Design system basico** (tokens + componentes onde copy vive).
- [ ] **Analytics ativo** (Hotjar/PostHog/Amplitude/UXcam) para identificar friccao.
- [ ] **Stakeholders** (PM + designer + dev + UX writer + legal + a11y champion).
- [ ] **Backlog priorizado** por impacto (forms criticos primeiro, 404 depois).

> **Cristal C0 — NAO CHUTAR.** Microcopy ruim = drop-off mensuravel, frustracao do usuario, suporte sobrecarregado, marca corroida. Disclaimer educacional desta skill: aplicar com **5-10 user interviews + usability testing + A/B test + acessibilidade review (screen readers + WCAG) + legal/LGPD review + senior UX writer review** antes de publicar mudancas em copy de UI critico.

---

## Fundacao 1 — Microcopy Foundations (Yifrah + Mailchimp + UX Writing emergence + 4 Cs)

### Origem e canone

```
TIMELINE MICROCOPY DISCIPLINA

2009  Joshua Porter — termo "microcopy" cunhado
      (post Bokardo — copy pequeno aumenta conversao)

2014  Mailchimp Content Style Guide publicado (open-source)
      Voice & Tone como modelo seminal industria

2017  Kinneret Yifrah — "Microcopy: The Complete Guide" 1st ed
      Israel; primeira sistematizacao academica/pratica

2017  Google publica UX Writing Guidelines internas
      "Clear, concise, useful" — 3 Cs

2018  Surge titulo "UX Writer" em job boards (Google, Apple,
      Dropbox, Atlassian, Shopify)

2019  Yifrah — 2nd ed "Microcopy: The Complete Guide"
      + Mailchimp atualiza Voice & Tone

2020  UX Writing Hub (Yael Ben-David) — primeira escola dedicada

2022+ AI Writing tools (Frontitude, Writer.com, Grammarly Business)
      ajudam consistency em escala

2024+ Justice Dept USA exige WCAG 2.1 AA — microcopy clear =
      requisito legal para sites governamentais

2026  AI UX Writing: 1st draft de microcopy rotineiro automatizado;
      humano = strategy + voice + edge cases + ethics
```

### Definicao operacional (Yifrah)

```
"Microcopy is the words, phrases, and small pieces of text
that help users navigate a product. Buttons, error messages,
hint text, descriptions, instructional copy."

(Kinneret Yifrah, Microcopy: The Complete Guide, 2nd ed, 2019)
```

Yifrah divide o livro em **3 partes**:

1. **Voice & tone + persona** — definir personalidade da marca + barreiras mentais do usuario.
2. **Microcopy que motiva acao** — CTAs, signups, conversoes em UI.
3. **Microcopy que aumenta usabilidade** — erros, helper text, empty states.

### Os 4 Cs do bom microcopy

```
4 Cs DO MICROCOPY EFETIVO

CLEAR (claro)
   Vocabulario simples, sem jargao
   Frases curtas (1 ideia por frase)
   Voz ativa
   Verbos > adjetivos
   "Fazer login" > "Realizar autenticacao"

CONCISE (conciso)
   Cada palavra ganha o lugar
   Sem redundancias ("clique aqui para clicar")
   Sem "muito", "bastante", "realmente"
   Botao 2-4 palavras ideal
   Helper text 1 frase ideal

CONVERSATIONAL (conversacional)
   Como conversa entre pessoas
   "Voce" / "voce esta" / "vamos"
   Contracoes ("nao da" > "nao e possivel" em casos)
   Empatia ("tudo bem" > "erro fatal")

CONTEXTUAL (contextual)
   Mesma acao, palavras diferentes por contexto
   Onboarding: encorajador
   Erro: empatico + acionavel
   Confirmacao destrutiva: serio + claro
   Empty state: motivador + acionavel
```

### Voice vs Tone (Mailchimp model)

```
VOICE = QUEM A MARCA E (consistente sempre)
   Mailchimp: "Fun but not silly. Confident but not cocky.
   Smart but not stuffy. Informal but not sloppy."

TONE = COMO A MARCA SOA (varia por contexto + emocao usuario)
   Welcome page: enthusiastic
   Error message: empathetic, calm
   Confirmation destrutiva: serious, clear
   Onboarding: encouraging, helpful
   Marketing email: playful

REGRA DE OURO MAILCHIMP
   Voice never changes; tone changes with situation
```

NN/g (Nielsen Norman Group) define **4 dimensoes de tom**:

```
4 DIMENSOES DE TONE OF VOICE (NN/g)

1. FORMAL    <-->  CASUAL
   Stripe = formal-ish    /    Slack = casual
   B2B financeiro = formal /   B2C entretenimento = casual

2. SERIOUS   <-->  FUNNY
   Banco = serious        /    Mailchimp = playful
   Saude = serious        /    Duolingo = funny

3. RESPECTFUL <--> IRREVERENT
   LinkedIn = respectful  /    Wendy's Twitter = irreverent
   Govt = respectful      /    Cards Against Humanity = irreverent

4. MATTER-OF-FACT <--> ENTHUSIASTIC
   Wikipedia = matter-of-fact  /  Mailchimp = enthusiastic
   Documentation = matter-of-fact / Marketing = enthusiastic
```

Marca define posicao em cada eixo (1-5). Posicao = voice. Variacao por contexto = tone.

---

## Fundacao 2 — Button Labels + CTAs Microcopy

### Anatomia de um botao perfeito

```
ANATOMIA DO BOTAO

VERBO DE ACAO (action verb) > nome generico
   SIM: "Salvar", "Enviar pedido", "Comecar teste gratis"
   NAO: "OK", "Submeter", "Click aqui"

ESPECIFICIDADE > genericidade
   SIM: "Baixar PDF do contrato"
   NAO: "Download"

PRIMEIRA PESSOA OPCIONAL (depende do tom)
   "Quero começar" (Yifrah favorita — 1a pessoa do usuario)
   "Comecar agora" (imperativo neutro)
   "Comece agora" (imperativo direto)

LENGTH IDEAL
   Botao primario: 2-4 palavras
   Botao secundario: 1-3 palavras
   Botoes mobile: max 2-3 palavras

PALAVRA-CHAVE NO INICIO
   "Baixar PDF" > "PDF para baixar"
   Eyetracking: usuario le primeira palavra primeiro
```

### Hierarquia visual + verbal

```
HIERARQUIA DE BOTOES

PRIMARIO (acao desejada)
   Visual: solid color, contrast alto
   Copy: verbo forte + objeto claro
   Ex: "Criar conta gratis", "Confirmar compra"

SECUNDARIO (alternativa)
   Visual: outline ou ghost
   Copy: verbo neutro
   Ex: "Saiba mais", "Cancelar"

TERCIARIO / LINK (escape route)
   Visual: text-only, underline
   Copy: discreto
   Ex: "Voltar", "Pular esta etapa"

DESTRUTIVO (perigo)
   Visual: red ou warning
   Copy: explicito + verbo forte
   Ex: "Excluir conta permanentemente"
   (NAO: "Confirmar")
```

### Padroes 2026 — botoes que convertem

```
PADROES COMPROVADOS (Shopify 2026 + UX Writing Hub)

START FREE TRIAL > SUBMIT
   Especifico (free + trial) + verbo ativo (start)
   +30-50% CTR vs "Submit" generico (cases agregados)

KEEP READING > READ MORE
   "Keep" implica que ja comecou (continuacao)
   "More" implica esforco extra (efeito custo)

GET YOUR QUOTE > GET A QUOTE
   "Your" = personalizacao + posse
   "A" = generico

YES, I WANT X / NO, I DONT > OK / CANCEL
   Yifrah: "Tom dialogico" > "tom robotico"
   Aumenta engagement + recall

ANTI-PATTERNS BOTAO
   "Click here" — vago
   "Submit" — sem contexto
   "OK" — sem informacao
   "Continue" — para onde?
   "Yes/No" sem contexto na pergunta
```

### Cases iconicos

| Empresa | Botao | Por que funciona |
|---------|-------|------------------|
| Spotify | "Get Premium Free" | Tres beneficios em 3 palavras |
| Netflix | "Start Your Free Month" | Posse (Your) + tempo (Month) |
| Dropbox | "Try Dropbox free" | Acao simples + CTA gratis |
| Airbnb | "Become a host" | Identidade aspiracional |
| Slack | "Try Slack" | Baixa friccao (try) |
| Notion | "Get Notion free" | Get + free |
| Trello | "Sign up — its free" | Microcopy ao lado do CTA reforca |
| Mailchimp | "Sign up free" | 3 palavras + valor |

### Brasil — botoes em PT-BR

```
PT-BR BOTOES — ARMADILHAS COMUNS

ARMADILHA 1: TRADUCAO LITERAL
   "Submit" -> "Submeter" (errado — formal demais)
   "Submit" -> "Enviar" / "Salvar" / "Confirmar"
   (depende do contexto)

ARMADILHA 2: GERUNDIO
   "Loading..." -> "Carregando..." (OK, mas explore alternativas)
   "Carregando seu pedido..." (especifico melhor)

ARMADILHA 3: VOCE vs TU
   Maioria do BR = voce
   Sul (RS, parte SC, PR) = tu informal
   Marca jovem-RJ pode usar tu ("Volte" -> "Volta")
   DECIDIR EARLY + DOCUMENTAR no style guide

ARMADILHA 4: IMPERATIVO MASCULINO
   "Bem-vindo" exclui mulher (gendered)
   "Bem-vindo(a)" feio + acessibilidade ruim
   "Que bom te ver" / "E um prazer" (neutro)

EXEMPLOS BONS PT-BR
   "Comecar agora" / "Quero comecar"
   "Criar conta gratis" / "Criar minha conta"
   "Salvar alteracoes" / "Salvar"
   "Cancelar pedido" (sempre explicito em destrutivo)
   "Voltar para inicio" > "Voltar"
```

---

## Fundacao 3 — Error Messages (Yifrah + Mailchimp + Baymard)

### Os 3 ingredientes de uma mensagem de erro boa

```
FORMULA YIFRAH PARA ERROR MESSAGES

1. WHAT HAPPENED (o que aconteceu)
   Estado tecnico claro, sem jargao
   "Nao conseguimos processar seu pagamento"
   (NAO: "Error 500")

2. WHY (por que aconteceu — quando util)
   Causa provavel
   "O cartao foi recusado pelo banco"
   (NAO: "Database connection failed")

3. WHAT TO DO (o que fazer)
   Acao especifica do usuario
   "Tente outro cartao ou ligue para 0800-XXX"
   (NAO: deixar usuario perdido)
```

Exemplo bom:

```
"Nao conseguimos processar seu pagamento. O cartao foi recusado
pelo banco emissor. Voce pode tentar outro cartao ou ligar
para 0800-XXX para entender o motivo."

[Tentar outro cartao] [Falar com suporte]
```

Exemplo ruim:

```
"Erro ao processar pagamento. Tente novamente."
```

### Anti-blame — NUNCA culpar o usuario

```
EVITAR LINGUAGEM DE CULPA

RUIM: "Voce digitou um email invalido"
       (acusatorio, frustra)

BOM:  "Esse email parece nao ter @ ou ponto. Pode verificar?"
       (descritivo + acionavel)

RUIM: "Senha incorreta. Voce errou."
       (humilha)

BOM:  "Senha nao confere. Tente novamente ou redefina."
      [Esqueci minha senha]

RUIM: "Voce nao preencheu o campo obrigatorio"
       (negativo)

BOM:  "Falta preencher o nome para continuar"
      (positivo + acionavel)
```

### Mailchimp model — empatia + tom suave

```
MAILCHIMP ERROR MODEL

EMPATIA PRIMEIRO
   "Ops!" / "Hmm." / "Que pena"
   (humano > robotico)

CONTEXTO CLARO
   "Algo deu errado ao salvar sua campanha"
   (especifico do que falhou)

ACAO PROXIMA
   "Tente atualizar a pagina ou voltar em alguns minutos"
   (acionavel)

ESCAPE PATH
   "Se persistir, fale com a gente: support@..."
   (suporte humano disponivel)
```

### Inline validation — onde fazer diferenca

CXL research: inline form validation + mensagens especificas = **+22% taxa de sucesso, -42% tempo de preenchimento**.

```
INLINE VALIDATION — REGRAS

QUANDO MOSTRAR
   - On blur (saiu do campo) — padrao seguro
   - On type real-time — apenas para formato (email, CEP)
   - Submit-time — fallback obrigatorio

ONDE MOSTRAR
   - Logo abaixo do campo (proximidade)
   - Cor consistente (vermelho ou laranja, nao rosa)
   - Icone + texto (acessibilidade — nao so cor)

O QUE MOSTRAR
   - Especifico ("Senha precisa de 8+ caracteres com 1 numero")
   - Nao apenas "Invalido"
   - Confirmacao positiva quando OK ("Email valido")

ARMADILHA
   - Validar email antes de terminar de digitar (frustra)
   - "Required" sem dizer o que e required
   - Validar duro em campos opcionais
```

### 404 + erros sistemicos

```
404 PAGES — FORMULA

ELEMENTO 1: Reconhecimento empatico
   "Pagina nao encontrada"
   "Esta pagina nao existe"
   "Hmm, parece que essa pagina sumiu"

ELEMENTO 2: Explicacao curta
   "Pode ter sido movida ou o link estar errado"

ELEMENTO 3: Acoes claras (3-4 max)
   - "Voltar a pagina inicial" (CTA primario)
   - "Buscar no site" (search box)
   - "Falar com suporte" (escape)
   - "Ver paginas populares" (alternativa)

ELEMENTO 4: Personalidade + brand voice
   GitHub: octocato perdido (tema marinheiro)
   Slack: "It's not you, it's us"
   Pixar: ilustracao tematica
   Mailchimp: monkey perplexo

ANTI-PATTERN 404
   "Error 404" cru
   Sem CTA
   Sem busca
   Sem brand voice
```

### Brasil — erros em PT-BR

```
ERROS PT-BR — PADROES BONS

CARTAO RECUSADO
   "Seu cartao foi recusado. Pode tentar outro ou
   conferir os dados acima?"

EMAIL JA EXISTE
   "Esse email ja tem cadastro. Quer entrar com ele?"
   [Entrar] [Recuperar senha]

SENHA FRACA
   "Sua senha precisa de 8+ caracteres com numeros e
   simbolos. Que tal tentar de novo?"

SEM CONEXAO
   "Sem internet. Conecte-se e tentamos de novo."

LIMITE DE TENTATIVAS
   "Muitas tentativas seguidas. Aguarde 5 minutos para
   tentar novamente."

LGPD CONSENT
   "Para continuar, precisamos do seu OK em compartilhar
   alguns dados. Voce pode revisar antes." [Revisar]
```

---

## Fundacao 4 — Form Labels + Helper Text + Validation + Acessibilidade

### Label > Placeholder (sempre)

```
LABEL VS PLACEHOLDER — REGRA

LABEL (sempre visivel)
   - Acima do campo (Material Design + best practice)
   - Sempre presente (mesmo apos preenchimento)
   - Acessivel a screen readers
   - Curto e direto: "Email", "Nome completo"

PLACEHOLDER (texto cinza dentro do campo)
   - Some ao digitar (perde contexto)
   - Confunde com valor preenchido
   - Acessibilidade RUIM (screen readers as vezes ignoram)
   - Contraste cinza fraco (a11y issue)

USO COMBINADO IDEAL
   Label fixo: "Email"
   Placeholder vazio OU exemplo: "voce@empresa.com"
   Helper text: "Usamos para enviar atualizacoes"

ANTI-PATTERN
   So placeholder, sem label visivel
   (a11y violation + UX ruim apos preenchimento)
```

### Helper text — quando e como

```
HELPER TEXT (HINT TEXT) — REGRAS

QUANDO USAR
   - Formato esperado (CPF, CEP, telefone)
   - Por que pedimos (privacy reassurance)
   - Restricoes (8+ chars, sem espaços)
   - Beneficio (usado para X)

ONDE
   - Abaixo do campo, fonte menor (12-14px)
   - Cor cinza secundario (mas legivel — a11y)

EXEMPLOS BONS PT-BR
   Campo: CPF
   Helper: "Apenas numeros, sem pontos ou tracos"

   Campo: Email
   Helper: "Usamos para login e recuperacao de senha"

   Campo: Telefone
   Helper: "Com DDD. Usamos so se houver problema na entrega"

   Campo: Senha
   Helper: "Minimo 8 caracteres, com 1 numero e 1 simbolo"

ANTI-PATTERN
   Helper text obvio: "Digite seu email" abaixo de label "Email"
   Helper text que nunca some (e na verdade label)
```

### Required vs Optional — quem marcar

```
REQUIRED VS OPTIONAL

PADRAO MAIORIA
   Marcar OPTIONAL (campo opcional explicito)
   Resto subentende-se obrigatorio

POR QUE
   Forms em geral pedem 80%+ campos obrigatorios
   Marcar todos com asterisco = ruido visual
   Marcar OPTIONAL = clareza no minoritario

EXCECAO
   Forms longos (15+ campos) com mistura 50/50
   = marcar required com *
   + nota: "* campos obrigatorios"

ACESSIBILIDADE
   ARIA: aria-required="true"
   Texto: " (obrigatorio)" ou " (opcional)"
   NAO so cor (a11y)
```

### Validacao em tempo real — patterns

```
VALIDACAO TIMING

ON-TYPE (real-time)
   Apenas formato basico
   - Email: ver "@" presente
   - CEP: 8 digitos
   - Telefone: numero correto digits
   NAO: validar dominio + dns durante digitacao

ON-BLUR (saiu do campo)
   Validacao completa do campo
   - Email: dominio existe?
   - CPF: digito verificador
   - Senha: forca

ON-SUBMIT
   Validacao final + erros agregados
   - Foco no primeiro erro
   - Mensagem proxima ao campo

ON-SERVER (apos submit)
   Validacoes que dependem de backend
   - Email ja cadastrado
   - CPF ja existe
```

### Acessibilidade WCAG em forms

```
A11Y FORMS — CHECKLIST WCAG 2.1 AA

LABELS
   - Toda input tem <label for=> ou aria-label
   - Label clicavel foca o campo (UX + a11y)

ERROS
   - aria-invalid="true" no campo com erro
   - aria-describedby aponta para mensagem
   - Texto + icone + cor (nao so cor)
   - Anuncio para screen reader (aria-live)

GRUPOS
   - <fieldset> + <legend> para radios/checkboxes
   - aria-labelledby para grupos custom

KEYBOARD
   - Tab order logico
   - Enter envia form
   - Esc fecha modais

CONTRAST
   - Texto: 4.5:1 minimo (AA)
   - Helper text cinza: 4.5:1 (nao apenas 3:1)
   - Erros: contraste alto + nao so cor

CROSS-SKILL
   Ver `acessibilidade-wcag` (proxima skill UX/UI bloco)
```

---

## Fundacao 5 — Empty States + Onboarding + 404 + Confirmation Dialogs

### Empty States — o moment teachable de NN/g

```
EMPTY STATE FORMULA YIFRAH (3 elementos)

1. HEADING
   Diz o que falta + por que e bom
   "Voce ainda nao tem alertas configurados"
   (NAO: "Sem dados")

2. MOTIVATION
   Explica por que essa funcao importa
   "Alertas avisam voce sobre mudancas em tempo real, sem
   precisar checar manual"

3. CALL-TO-ACTION
   Acao clara para sair do empty state
   [Criar primeiro alerta]

EXEMPLO COMPLETO
   "Sua caixa de entrada esta vazia"
   "Quando alguem te enviar mensagem, ela aparece aqui."
   [Convidar amigos] [Importar contatos]
```

### Padroes Slack + Mailchimp + Dropbox

```
EMPTY STATE CASES

SLACK CHANNEL VAZIO
   Heading: "This channel is for #general — be the first
            to say hello"
   Action: integrated message composer
   Personalidade: tom convidativo

MAILCHIMP NOVA CAMPANHA
   Heading: "Lets create something great"
   Subhead: "Choose a campaign type to get started"
   Actions: 4 cards com tipos de campanha + descricao

DROPBOX PASTA VAZIA
   Heading: "Drop files here, or click to upload"
   Visual: ilustracao + dashed border drop zone
   Action: button "Upload files" + drag-and-drop

PADRAO COMUM
   - Heading curto (5-10 palavras)
   - 1 frase explicando valor
   - 1-2 CTAs (primario + secundario)
   - Ilustracao opcional (brand personality)
```

### Onboarding — patterns

```
ONBOARDING PATTERNS 2026

WELCOME SCREEN
   - Heading: "Bem-vindo ao [produto], [nome]!"
   - 1-2 frases sobre proximos passos
   - CTA claro (single, nao multipla)

PROGRESS INDICATOR
   - "Etapa 2 de 4"
   - Permite skip (volta depois)
   - Mostra valor por etapa (nao so contador)

TOOLTIP TOUR
   - Max 5 tooltips no primeiro tour
   - Cada tooltip 1-2 frases
   - "Pular tour" sempre visivel
   - Re-acionavel via menu help

EMPTY STATE COMO ONBOARDING
   - 1a vez na feature = empty state ensina
   - Sample data opcional ("Ver com dados de exemplo")
   - CTA "Criar primeiro X" gera o estado real

CHECKLIST
   - Lista 3-5 itens primeiros
   - Checkmark visual = dopamine
   - "Configurar perfil", "Convidar time", "Criar projeto"

ANTI-PATTERNS ONBOARDING
   - Tour com 15+ steps (drop-off >70%)
   - Forcar fluxo sem skip
   - Mostrar tudo de uma vez
   - Repetir tour ja feito
```

### Tooltips — quando + como

```
TOOLTIPS RULES

QUANDO USAR
   - Icone-only buttons (clarificar acao)
   - Termos especializados (definicao)
   - Contexto adicional opcional
   - Atalhos de teclado

QUANDO NAO USAR
   - Informacao critica (deve estar visivel)
   - Long-form content (use modal/page)
   - Validation errors (use inline)

PADROES
   - Aparece em hover/focus + 300-500ms delay
   - Some quando mouse sai
   - Position: top/bottom auto baseado em viewport
   - Max 1-2 frases (10-15 palavras)
   - Tab-able / focus-able (a11y)

ARIA
   role="tooltip"
   aria-describedby no elemento que aciona
   Visivel ao focus (nao so hover)

ANTI-PATTERN
   Tooltip com link/botao dentro (escapavel)
   Tooltip sem dismiss em mobile
   Tooltip aparece automatico/sem trigger
```

### Confirmation Dialogs — destrutivos

```
DESTRUCTIVE CONFIRMATION

ELEMENTO 1: Heading explicito
   "Excluir conta permanentemente?"
   (NAO: "Voce tem certeza?")

ELEMENTO 2: Consequencia clara
   "Sua conta, dados e historico serao apagados.
   Esta acao nao pode ser desfeita."

ELEMENTO 3: Botoes assimetricos
   [Cancelar] (botao secundario, neutro)
   [Excluir conta permanentemente] (vermelho, especifico)

ELEMENTO 4: Friction adicional para criticas
   - Digite "EXCLUIR" para confirmar
   - 2FA ou re-senha
   - Cooldown 24h antes de execucao real (Mailchimp)

EXEMPLOS PT-BR
   "Cancelar assinatura?"
   "Voce perdera acesso ao premium em 31/05. Pode reativar
    quando quiser."
   [Manter assinatura] [Cancelar mesmo assim]

ANTI-PATTERNS
   Botao "OK" sozinho (sem entender consequencia)
   Botao destrutivo cinza/igual ao cancelar (dark pattern)
   Friction zero em acao irreversivel
```

---

## Fundacao 6 — Brasil 2026 Especificidades (PT-BR + tom voce/tu + localizacao)

### PT-BR nao e traducao mecanica

```
ARMADILHAS LOCALIZACAO USA -> BR

ARMADILHA 1: STRUTURA SINTATICA
   EN: "Sign up to get started"
   PT-BR mecanico: "Inscreva-se para comecar"
   PT-BR natural: "Cadastre-se gratis" / "Criar conta"

ARMADILHA 2: METAFORAS CULTURAIS
   EN: "Welcome to the family"
   PT-BR mecanico: "Bem-vindo a familia"
   PT-BR adaptado: "Que bom te ver por aqui"
   (familia tem peso cultural diferente — usar com cuidado)

ARMADILHA 3: DATA + MOEDA + ENDERECO
   EN: 12/31/2026, $19.99, ZIP 90210
   PT-BR: 31/12/2026, R$ 19,99, CEP 90210-XXX
   (tools auto-traduzem texto, nao formato)

ARMADILHA 4: PRONOMES
   EN: "you" (neutro)
   PT-BR: voce / tu / o senhor (escolhas)
   Decisao early no style guide

ARMADILHA 5: GERUNDIO NA UI
   EN: "Loading..."
   PT-BR: "Carregando..." (OK mas overused)
   Variar: "Quase la", "Buscando dados", "Salvando..."
```

### Voce vs Tu — decisao de marca

```
VOCE x TU x SENHOR/A

VOCE (informal-neutro)
   Maioria do BR (Sudeste, NE, CO, Norte)
   Padrao SaaS (Magalu, iFood, Nubank, RD, Resultados Digitais)
   Mais flexivel para escala nacional

TU (informal-regional)
   RS, partes SC/PR (sul) + alguns PE/AM
   Conjugacao especifica ("tu vais", "te vejo")
   Marca regional ou jovem-RJ pode usar
   Cuidado: "tu vai" (errado) vs "tu vais" (correto)

O SENHOR / A SENHORA (formal)
   Banking tradicional, governo, juridico, saude tradicional
   Marca premium (concierge)
   Audiencia 60+ ou contexto B2B muito formal

DECISOES BRASIL 2026
   Nubank: voce (jovem urbano)
   Itau: voce (modernizou — antes "o Sr/Sra")
   Magalu Lu: voce (informal + emoji)
   iFood: voce (informal + jovem)
   Banco do Brasil: voce + senhor/a misto (audiencia ampla)
   Vivo: voce
   Petrobras: senhor/a (formal, governo)
```

### Tom de marcas brasileiras 2026

```
CASES BRASIL 2026

NUBANK
   Voice: simples, direto, anti-banco-tradicional
   Tone empty state: "Nada por aqui ainda. Que tal comecar?"
   Tone erro: "Eita, deu ruim aqui. A gente ja resolve."
   CTA: "Pronto" / "Bora" / "Continuar"

MAGALU (Lu da Magalu)
   Voice: amigavel, proxima, vendedora-conselheira
   Tone empty: "Nada na sua sacola ainda. Vem ver promocoes!"
   Tone erro: "Opa, nao deu. Bora tentar de novo?"
   CTA: "Comprar agora" / "Adicionar a sacola"

IFOOD
   Voice: jovem, urgente, com humor
   Tone empty: "Sem pedidos por aqui. Vai um lanchinho?"
   Tone erro: "Algo nao deu certo. Tenta de novo?"
   CTA: "Pedir agora" / "Continuar pedido"

ITAU
   Voice: confiavel, profissional, modernizou
   Tone empty: "Voce nao tem cartoes nesse momento."
   Tone erro: "Nao foi possivel completar a operacao."
   CTA: "Continuar" / "Confirmar"

PETROBRAS / GOV.BR
   Voice: institucional, formal-acessivel
   Tone empty: "Nenhum registro encontrado."
   Tone erro: "Nao foi possivel processar sua solicitacao."
   CTA: "Buscar" / "Enviar"
```

### LGPD — UX implications

```
LGPD UX MICROCOPY 2026

CONSENT BANNER
   - Nao usar dark patterns (botao "Aceitar" gigante,
     "Configurar" minusculo escondido)
   - Granularidade clara (cookies essenciais x analytics
     x marketing)
   - Linguagem clara, sem jargao juridico
   - Botao "Rejeitar todos" com mesmo peso visual de "Aceitar"
   - ANPD fiscaliza dark patterns desde 2024

EXEMPLO BOM PT-BR
   "Usamos cookies para melhorar sua experiencia. Voce decide
    o que aceitar. Saiba mais na nossa Politica de Privacidade."
   [Aceitar todos] [Rejeitar todos] [Personalizar]

DATA SUBJECT RIGHTS
   - Linguagem acessivel ao explicar direitos
     (acesso, correcao, exclusao, portabilidade, oposicao)
   - "Pedir meus dados" > "Direito de acesso"
   - "Apagar minha conta" > "Direito de exclusao"

SENSITIVE DATA UX
   - Avisos explicitos antes de coletar dado sensivel
     (saude, biometria, raca/etnia, orientacao)
   - "Por que pedimos isso?" link sempre disponivel
```

### GOV.BR Padrao Digital

GOV.BR Design System tem padroes oficiais para microcopy de governo BR:

```
GOV.BR MICROCOPY OFICIAL

VOICE GOV.BR
   - Direto e respeitoso (cidadao, nao "usuario")
   - "O Sr/A Sra" em interacoes formais
   - "Voce" em interacoes digitais novas

TONE
   - Sem jargao juridico/tecnico
   - Explicacao precede acao
   - "Voce precisa de" > "E necessario que voce"

EXEMPLOS GOV.BR
   "Para continuar, faca login com gov.br"
   "Sua solicitacao foi enviada. O numero do protocolo e XXX."
   "Aguarde ate 30 dias uteis para resposta."

REFERENCIA OFICIAL
   https://www.gov.br/ds/padroes/writing/microcopy
```

### Crescimento UX Writing BR 2026

```
MERCADO UX WRITING BR

DEMANDA (Vagas UX 2026 + Glassdoor BR)
   +340% job postings UX Writer entre 2020-2024
   Salarios pleno R$ 6.500 a R$ 12.000 (Sao Paulo, RJ)
   Senior R$ 13.000 a R$ 20.000+

EMPRESAS QUE CONTRATAM UX WRITER DEDICADO
   Nubank, iFood, Magalu, Mercado Livre, Itau, Bradesco,
   Vivo, Globo, Resultados Digitais, RD Station, GetNinjas,
   QuintoAndar, Loft, Grupo Boticario, Natura, Ambev

SENIORIDADES
   Junior: redator de peca + revisao
   Pleno: style guide + voice & tone + sub-areas
   Senior: strategy + cross-team + governanca
   Lead: head of content design / writing manager

FORMACAO BR
   Vagas UX (vagasux.com.br) + Tera + UX Unicorn
   Comunidade: UX Writing BR Slack + Meetups SP/RJ
   Podcasts: Ladrilho, MeMo
```

---

## Fundacao 7 — Mensuracao + Tools 2026

### KPIs microcopy

```
KPIS MICROCOPY (HIERARQUIA)

NIVEL 1 — IMPACTO BUSINESS
   - Conversion rate (signup, checkout, activation)
   - Drop-off rate por etapa do funil
   - Time-to-complete formularios
   - Customer support ticket volume (sobre UI)

NIVEL 2 — UX METRICS
   - Task success rate (usability testing)
   - Error rate por form
   - Recovery rate (% que conclui apos erro)
   - Tooltip dismissal rate
   - Empty state CTA click-through

NIVEL 3 — QUALITY METRICS
   - Reading grade level (Flesch-Kincaid)
   - Consistency score (style guide audit)
   - A11y score (WCAG checks automatizados)
   - Tone-of-voice adherence (manual + AI scoring)

NIVEL 4 — VOLUME METRICS
   - Strings totais no produto
   - % strings com fallback i18n
   - % cobertura PT-BR vs ingles
```

### A/B testing microcopy — quando vale

```
QUANDO A/B TESTAR COPY

ROI ALTO
   - Botoes em fluxo critico (signup, checkout)
   - Headlines de landing pages
   - Mensagens de erro com drop-off mensuravel

ROI MEDIO
   - Empty states com CTA
   - Onboarding tooltips (primeiros 5)
   - 404 com busca

ROI BAIXO
   - Helper text (mudancas pequenas dificil mensurar)
   - Tooltips secundarias
   - Microcopy raramente vista

REGRAS A/B COPY
   - 1 variavel por vez (texto OU posicao OU cor)
   - Sample size adequado (calc.minimum)
   - Sazonalidade considerada
   - Confidencia 95%+ antes de ship
   - Reverter se flat (nao manter variant)
```

### Tools 2026 — UX writers

```
TOOLS LANDSCAPE 2026

WRITING + DRAFTING
   - Frontitude (UX writing platform, design tokens)
   - Writer.com (enterprise content + style guide)
   - Grammarly Business (style + tone consistency)
   - ChatGPT/Claude/Gemini (drafting + variantes)
   - Hemingway Editor (readability)
   - Yoast (readability + SEO)

DESIGN INTEGRATION
   - Figma plugins (Lorem Husum, Content Reel,
     Frontitude plugin)
   - Sketch + Frontitude
   - Storybook (component library com microcopy)

STYLE GUIDE
   - Notion / Coda (lightweight)
   - Confluence (enterprise)
   - Frontitude (dedicado)
   - Lingo (visual style guide)

LOCALIZATION
   - Lokalise / Phrase / Crowdin
   - Smartling (enterprise)
   - DeepL Pro (translation + glossary)

ANALYTICS + USABILITY
   - Hotjar (heatmaps + session recording)
   - PostHog / Amplitude (funnel + drop-off)
   - UserTesting / Maze (usability testing)
   - UXcam (mobile session recording)

A11Y AUDIT
   - axe DevTools (WCAG automated)
   - Wave (acessibilidade)
   - Pa11y (CI/CD a11y check)

BR-SPECIFIC
   - SmartContent (LGPD + content audit BR)
   - Phrasee (AI subject lines + microcopy)
```

### Workflow ideal UX writer 2026

```
WORKFLOW UX WRITER 2026

1. RESEARCH
   - Read user research existente
   - Run 3-5 user interviews proprios
   - Audit copy atual (planilha + screenshots)
   - Competitive scan (3 concorrentes)

2. STRATEGY
   - Define voice & tone (style guide)
   - Map jornada + emotional moments
   - Priorize interventions (impacto x esforco)

3. DRAFT
   - AI-assisted 1st draft (Frontitude/ChatGPT)
   - Review humano (strategy + edge cases)
   - 3 variantes por copy critico

4. VALIDATE
   - Usability testing (5-10 users)
   - A/B test em copy de alto trafego
   - A11y review (screen readers)
   - Legal/LGPD review

5. SHIP
   - Design handoff (Figma + Frontitude)
   - Dev integration (i18n keys)
   - Documentation no style guide

6. MEASURE
   - Track KPIs (drop-off, conversion, support)
   - Iterate baseado em dados
   - Atualiza style guide com aprendizados
```

---

## Fundacao 8 — Aplicacao em Content MKT (5 audiencias)

### Audiencia 1 — UX Writers (interno + freelance)

```
PARA UX WRITERS

JOBS-TO-BE-DONE
   - Construir style guide do zero ou refatorar
   - Auditar produto existente (gap analysis)
   - Padronizar microcopy em codebase legado
   - Mentor designers/PMs em UX writing

DELIVERABLES TIPICOS
   - Voice & tone guide (15-30 paginas)
   - Microcopy inventory (planilha + Frontitude)
   - Component library copy (Storybook + design system)
   - Localization style guide PT-BR

KPI PROFISSIONAL
   - Time-to-publish (release velocity)
   - Consistency score
   - Drop-off reduction em fluxos criticos
   - Support ticket volume reducao

CONTENT MKT PARA UX WRITER
   - LinkedIn artigos sobre cases reais (anonimizados)
   - Talks em UX events (UX Writing Hub, Tera, Vagas UX)
   - Templates open-source no GitHub
   - Newsletter pessoal (Substack + Mailchimp)
```

### Audiencia 2 — PMs (Product Managers)

```
PARA PMS

POR QUE PM PRECISA SABER MICROCOPY
   - PM define product strategy + microcopy reflete strategy
   - Em times sem UX writer dedicado, PM filla o gap
   - Microcopy ruim afeta KPIs do PM diretamente

JOBS-TO-BE-DONE
   - Brief de feature inclui requisitos de copy
   - Review de copy antes de release
   - Decisoes de tom em releases sensitivos
   - Patrocinar contratacao de UX writer

DELIVERABLES TIPICOS
   - Spec de feature com copy guidelines
   - User stories incluem error cases + empty states
   - Release notes com tom consistente

CONTENT MKT PARA PM
   - Mind the Product / Product Hunt cases
   - Medium articles "How we improved X by Y%"
   - Twitter threads sobre product decisions
```

### Audiencia 3 — Designers (UI/UX/Product)

```
PARA DESIGNERS

POR QUE DESIGNER PRECISA SABER MICROCOPY
   - Copy + design = par inseparavel (Yifrah)
   - Designer escolhe copy quando UX writer nao tem
   - Design system inclui copy (Frontitude integration)

JOBS-TO-BE-DONE
   - Lorem ipsum eliminado (use real copy)
   - Variantes de copy nos comps Figma
   - A11y check inclui copy review
   - Hand-off com microcopy aprovada

DELIVERABLES TIPICOS
   - Figma files com copy real
   - Design system com tokens de copy
   - Component variants (default/empty/error/success)

CONTENT MKT PARA DESIGNER
   - Dribbble / Behance com cases focando copy
   - Smashing Magazine articles
   - Talks em design events (Front-end SP, BrazilJS)
```

### Audiencia 4 — Founders / Indie Hackers

```
PARA FOUNDERS

REALIDADE FOUNDERS EARLY-STAGE
   - Sem UX writer dedicado (orcamento)
   - Founder escreve copy inicial
   - Decisoes de voice afetam crescimento

JOBS-TO-BE-DONE
   - Voice & tone do produto MVP
   - Onboarding inicial (primeiros 60s = retention)
   - Empty states que ensinam
   - Erros que nao queimam usuario

QUICK WINS FOUNDERS
   - 1 pagina de voice & tone (manifesto)
   - 5 mensagens de erro padrao re-usaveis
   - 3 empty states criticos
   - 1 onboarding flow

CONTENT MKT PARA FOUNDER
   - Indie Hackers cases publicos
   - Twitter build-in-public
   - LinkedIn lessons learned
```

### Audiencia 5 — Content Strategists / Product Marketers

```
PARA CONTENT STRATEGISTS / PMM

POR QUE PARTICIPA DE MICROCOPY
   - Content strategy abrange website + produto
   - PMM alinhha brand voice com product voice
   - Launch comms reflete microcopy do produto

JOBS-TO-BE-DONE
   - Style guide cross-team (brand + produto)
   - Launch communications consistente
   - PR/comms coordenadas com UI changes

DELIVERABLES TIPICOS
   - Cross-channel style guide
   - Launch playbook com microcopy reviewable
   - Brand voice 360 (advertising + content + product)

CONTENT MKT PARA CONTENT STRAT
   - Content Marketing Institute
   - LinkedIn long-form
   - Newsletters (Lenny's, Reforge)
```

---

## Anti-Patterns 18

```
ANTI-PATTERNS MICROCOPY (18 erros recorrentes)

1. CLICK HERE
   "Click here to download"
   FIX: "Download relatorio anual 2026 (PDF)"

2. SUBMIT GENERICO
   "Submit"
   FIX: "Enviar pedido" / "Salvar alteracoes" / "Confirmar"

3. ERROR 500 RAW
   "Error 500: Internal Server Error"
   FIX: "Algo deu errado do nosso lado. Estamos consertando."

4. BLAME USER
   "Voce digitou errado"
   FIX: "Esse email parece nao ter @ ou ponto. Verifique?"

5. PLACEHOLDER COMO LABEL
   So placeholder cinza, sem label fixo
   FIX: Label sempre visivel + placeholder opcional como exemplo

6. JARGON TECNICO
   "Authentication failed"
   FIX: "Senha ou email incorretos. Tente novamente."

7. EMPTY STATE INVISIVEL
   Tela vazia sem texto ou CTA
   FIX: Heading + motivation + CTA (Yifrah formula)

8. 404 SEM ESCAPE
   "Error 404" sem busca, sem links, sem brand
   FIX: 404 com personalidade + busca + links + CTA

9. CONFIRMACAO VAGA
   "Voce tem certeza?"
   FIX: "Excluir conta permanentemente?" + consequencia

10. TOOLTIP COMO INFO CRITICA
    Info importante so em tooltip
    FIX: Info critica visivel + tooltip para extras

11. INCONSISTENCIA TONAL
    Onboarding amigavel + erros frios
    FIX: Style guide + tone matrix por contexto

12. LOADING SEM CONTEXTO
    "Loading..."
    FIX: "Salvando suas alteracoes..." / "Quase la..."

13. PAYWALL CRYPTIC
    "Premium feature"
    FIX: "Esta funcao esta no plano Pro. Veja vantagens."

14. NOTIFICACAO RUIDO
    Notificacao sem acao clara
    FIX: Notificacao com CTA inline

15. COPY VOLUMOSO
    Paragrafos em estados de UI
    FIX: 1-2 frases max + link "Saiba mais"

16. BR TRADUCAO MECANICA
    "Click here to learn more" -> "Clique aqui para aprender mais"
    FIX: "Saiba mais" (idiomatico PT-BR)

17. DARK PATTERN COPY
    "Aceitar tudo" verde gigante / "Rejeitar" cinza minusculo
    FIX: Botoes simetricos + linguagem neutra

18. FORM REQUIRED CONFUSO
    Asterisco em todos sem explicacao
    FIX: Marcar OPTIONAL ou nota "* obrigatorios"
```

---

## 18 Regras de Ouro

```
18 REGRAS DE OURO MICROCOPY

1. CONHECA SEU USUARIO (sem persona, copy chuta)
2. UMA VOZ, MUITOS TONS (Mailchimp model)
3. 4 Cs SEMPRE (clear + concise + conversational + contextual)
4. VERBOS > NOMES em botoes
5. ESPECIFICIDADE > GENERICIDADE em CTAs
6. NUNCA CULPE O USUARIO em erros
7. WHAT/WHY/WHAT-TO-DO em mensagens de erro
8. LABEL > PLACEHOLDER (sempre)
9. INLINE VALIDATION quando possivel
10. EMPTY STATE = TEACHABLE MOMENT (Yifrah heading+motivation+CTA)
11. ONBOARDING MAX 5 STEPS no primeiro tour
12. TOOLTIP NUNCA P/ INFO CRITICA
13. CONFIRMACAO DESTRUTIVA = friction proporcional
14. PT-BR NAO E TRADUCAO MECANICA do EN
15. DECIDIR VOCE/TU EARLY no style guide
16. TODA UI TEM SCREEN READER (a11y review obrigatorio)
17. A/B TEST COPY DE ALTO TRAFEGO antes de ship
18. STYLE GUIDE VIVO + iterar com aprendizados
```

---

## Exemplos Comportamentais

### Persona 1 — Carolina, UX Writer Senior (Nubank-like fintech BR)

```
CONTEXTO
   Carolina, 32, UX Writer senior em fintech BR (1500 funcs)
   Time content design 6 pessoas; product 200+ engs/designers
   Roadmap 2026: revamp app + entrar em PJ
   Brand: jovem, simples, anti-banco-tradicional

DESAFIO
   Plataforma PJ tem 47 telas com microcopy inconsistente:
   ora "voce", ora "o senhor"
   Erros tecnicos vazaram p/ UI ("CONSTRAINT_VIOLATION")
   Empty states sao quase todos "Sem dados"
   Onboarding tem 12 steps (drop-off 60%)

PLANO 90 DIAS

DIAS 1-15 — RESEARCH + AUDIT
   - Audit microcopy atual (planilha 47 telas + screenshots)
   - 8 user interviews (PJ owners pequenos)
   - 3 competitor scan (Conta Azul, Stone, PicPay PJ)
   - Map emotional moments na jornada

DIAS 16-30 — STRATEGY
   - Update style guide PJ (extension do BTC pessoal)
   - Define tone matrix (16 contextos)
   - Priorize 12 telas criticas (signup, KYC, transfer, error)

DIAS 31-60 — DRAFT + VALIDATE
   - Draft microcopy 12 telas criticas
   - Frontitude integration p/ design system
   - Usability test 8 users
   - A/B test em signup (CTA + erros)

DIAS 61-90 — SHIP + EXTEND
   - Ship 12 telas criticas
   - Mentoria 4 designers/PMs no novo style guide
   - Restantes 35 telas em backlog priorizado
   - Document aprendizados no style guide vivo

KPIS
   - Drop-off signup: 32% -> meta 22% (-31%)
   - Drop-off KYC: 18% -> meta 12% (-33%)
   - Onboarding 12 -> 5 steps
   - Support tickets sobre UI: -40% em 90d
   - Style guide adoption: 80% novos releases

RISCOS
   - Mudancas em massa = QA burden
   - Stakeholders de produto querem ship rapido
   - Localizacao i18n atrasa
   - A11y review descobre issues retroativos

DISCLAIMER
   Educational + consultivo. Aplicar com 5-10 user
   interviews + usability testing + a11y review
   (screen readers + WCAG) + legal/LGPD review +
   senior UX writer review antes de ship em
   produtos financeiros (BACEN/CVM regulam UX em
   alguns flows).
```

### Persona 2 — Bruno, PM em SaaS B2B (RD-like marketing automation)

```
CONTEXTO
   Bruno, 35, PM em SaaS B2B BR (350 funcs)
   Time produto 8 PMs; sem UX writer dedicado
   Audience: PMEs marketing managers
   Brand: confiavel, expert, "RD/HubSpot tropicalizado"

DESAFIO
   Product copy escrito por engs ha anos
   Tom inconsistente: ora formal, ora gerundio infinito
   Erros tecnicos visiveis ("DB constraint failed")
   Tooltip explicando feature critica (esconde info)
   Empty states genericos
   Onboarding quase inexistente

PLANO 60 DIAS

DIAS 1-10 — DIAGNOSTICO
   - Audit microcopy 30 telas top-views
   - Hotjar review session recordings 50 sessoes
   - 5 user interviews PMEs ativos
   - Identificar top 5 friction points

DIAS 11-25 — MVP STYLE GUIDE
   - Define voice & tone (1 pagina simples)
   - 5 mensagens de erro padrao reusaveis
   - 3 empty states criticos
   - Onboarding 4-step welcome

DIAS 26-45 — IMPLEMENT
   - Designer + Bruno + 1 eng implementam top 5
   - Review semanal stakeholders
   - Hotjar tracking pos-mudanca

DIAS 46-60 — MEASURE + ITERATE
   - Mensurar drop-off + activation rate
   - Iterate 2-3 ciclos
   - Business case para contratar UX writer dedicado

KPIS
   - Activation rate (1 campanha enviada em 7d): 28% -> 40%
   - Time-to-first-value: 14d -> 7d
   - Support tickets sobre UI: -25%
   - Onboarding completion: 35% -> 60%
   - Tooltip dismissal: tracking baseline

RISCOS
   - Sem UX writer = qualidade limitada
   - Eng/designer stretch demais
   - Nao ter style guide robusto = inconsistencias futuras
   - PMEs com baixa tolerancia a friccao

DISCLAIMER
   Aplicar com user interviews + usability testing +
   a11y review minimo + senior peer review em copy
   critico. Recomenda contratar UX writer dedicado pos-MVP.
```

### Persona 3 — Joana, Founder Indie Hacker SaaS

```
CONTEXTO
   Joana, 29, founder solo SaaS micro-empresa
   Produto: gerenciador de financas pessoais BR
   1500 users beta; 80 paying ($9/mes)
   Brand: pratico, amigavel, "Mint adaptado para BR"

DESAFIO
   Joana escreveu todo copy sozinha
   Onboarding inicial 8 steps com churn 70% antes de step 4
   Empty states "Sem dados" repetidos
   Erros tecnicos visiveis ("Stripe webhook failed")
   404 generica
   Sem voice documentada

PLANO 30 DIAS (FOUNDER REALITY)

DIAS 1-5 — VOICE & TONE MVP
   - 1 pagina manifesto: "Como falamos com nosso usuario"
   - 5 do's, 5 dont's
   - 3 example phrases por contexto

DIAS 6-15 — FIX CRITICAL
   - Onboarding 8 -> 4 steps com sample data
   - 5 erros padrao reusaveis (PT-BR humano)
   - 3 empty states com CTA + motivation
   - 404 com personalidade + busca

DIAS 16-25 — VALIDATE LIGHT
   - 5 calls com beta users
   - Hotjar free tier monitora
   - Iterate semanal

DIAS 26-30 — SHIP + DOCUMENT
   - Push fixes prod
   - Document voice em Notion (futuro UX writer)
   - Share progresso em build-in-public

KPIS
   - Churn 30d: 35% -> meta 22%
   - Activation (1 transacao registrada): 20% -> 45%
   - Conversion beta -> paid: 5% -> 8%
   - Support tickets: -50%

RISCOS
   - Founder solo = qualidade limitada
   - Sem A/B testing infra
   - Sem a11y review formal
   - Crescimento exige escala que founder nao escreve

DISCLAIMER
   Educational. Founder solo deve aplicar minimo
   user interviews 3-5 + screen reader spot check +
   peer review (community feedback) antes de ship
   em flows criticos (signup, billing).
```

### Persona 4 — Henrique, Content Strategist em Startup Scale-Up (iFood-tier)

```
CONTEXTO
   Henrique, 38, head of content design em scale-up BR
   Produto: marketplace mobile B2C (10M users)
   Times: content design 12 pessoas; 60+ UX writers/designers
   Brand: jovem, urgente, urbano, com humor

DESAFIO
   App + web + push notifs + emails inconsistentes
   Localizacao PT-BR -> ES + EN para expansao LATAM
   LGPD compliance UX (consent + data subject rights)
   Dark patterns audit interno (board pediu)
   Acessibilidade WCAG AA gap mensuravel

PLANO 6 MESES

MES 1 — AUDIT + STRATEGY
   - Audit 200+ strings cross-channel
   - Voice & tone refresh (10-pagina guide)
   - LGPD UX audit (consent + erros + DSR)
   - Dark patterns scan + remediation plan

MES 2 — STYLE GUIDE V2
   - Refresh style guide (15 contextos + tone matrix)
   - Localization guide PT-BR -> ES (+ glossario)
   - Frontitude integration design system

MES 3 — A11Y FOCUS
   - Screen reader audit em iOS/Android/web
   - Labels + ARIA + focus management copy
   - WCAG 2.1 AA target

MES 4 — DARK PATTERNS REMEDIATION
   - Consent banner re-design (LGPD-compliant)
   - Cancellation flow simplified
   - Comparacao precos transparente
   - "Free trial" clarity em billing

MES 5 — LOCALIZATION LATAM
   - Tradumigracao 200 strings core para ES
   - 5 user interviews ES-speakers (CO/MX)
   - QA in-context

MES 6 — MEASURE + GOVERN
   - Style guide governance (review board)
   - KPIs cross-channel
   - Training program (3 cohorts/ano)
   - Plan 2027 roadmap

KPIS
   - Consistency score: 60 -> 85
   - WCAG AA: 70% -> 95% strings
   - Dark pattern violations: 8 -> 0
   - LGPD UX compliance: 100%
   - LATAM ES: 80% strings localized
   - User research coverage: 30 sessions/quarter

RISCOS
   - Escala (10M users) = QA burden
   - Localizacao ES tem nuances dialetais (CO/MX/AR)
   - LGPD ANPD pode auditar a qualquer momento
   - Brand voice deve coexistir com a11y constraints

DISCLAIMER
   Aplicar com user interviews 30+ por trimester +
   usability testing + a11y review (screen readers
   + WCAG audit) + legal/LGPD review + senior content
   strategist + diversity review (LATAM cultural)
   antes de ship em produtos com 10M users.
```

---

## Checklist Contraditorio Interno (10 perguntas)

| # | Pergunta destruidora | O que busca |
|---|----------------------|-------------|
| 1 | Voice & tone esta **documentada** e usada como referencia ativa? | Style guide vivo |
| 2 | **4 Cs** (clear + concise + conversational + contextual) aplicados em cada copy? | Foundations Yifrah |
| 3 | Botao tem **verbo + objeto**, nao "Submit" generico? | CTA quality |
| 4 | Erros explicam **what + why + what-to-do**, sem culpar usuario? | Error pattern |
| 5 | Labels **sempre visiveis** (nao apenas placeholder)? | Form best practice |
| 6 | Empty state tem **heading + motivation + CTA** (Yifrah formula)? | Empty state quality |
| 7 | PT-BR nao e **traducao mecanica** do EN; idiomatico + voce/tu decidido? | Brasil 2026 |
| 8 | **Acessibilidade** (a11y) reviewed (screen readers + WCAG AA + ARIA)? | Cross-skill obrigatorio |
| 9 | **5-10 user interviews** + usability testing realizados antes de ship critico? | Validation |
| 10 | **Legal/LGPD review** + dark patterns audit em flows sensitivos (consent, billing, exclusao)? | Compliance + ethics |

---

## Referencias

### Foundational global

- Kinneret Yifrah — "Microcopy: The Complete Guide" 2nd ed (2019) — https://www.microcopybook.com/
- Microcopy Book — Amazon — https://www.amazon.com/Microcopy-Complete-Guide-Kinneret-Yifrah/dp/B07N1RD7W6
- Mailchimp Content Style Guide — https://styleguide.mailchimp.com/
- Mailchimp Voice and Tone — https://styleguide.mailchimp.com/voice-and-tone/
- Joshua Porter — Bokardo blog (cunhou termo "microcopy") — https://bokardo.com/
- Atlassian Design System — Voice and Tone — https://atlassian.design/content/voice-and-tone
- Shopify Polaris — Content guidelines — https://polaris.shopify.com/content
- Stripe Documentation Style Guide — https://docs.stripe.com/

### NN/g + UX Writing canon

- NN/g — Tone of Voice Dimensions — https://www.nngroup.com/articles/tone-of-voice-dimensions/
- NN/g — Tone of Voice Video — https://www.nngroup.com/videos/tone-of-voice-dimensions/
- NN/g — Empty States Pattern — https://www.nngroup.com/articles/empty-state-interface-design/
- UX Writing Hub — https://uxwritinghub.com/
- UX Writing Hub — Voice and Tone — https://uxwritinghub.com/ux-writing-voice-and-tone/
- UX Writing Hub — Microcopy in a Nutshell — https://uxwritinghub.com/what-is-microcopy/
- UX Writing Hub — Error Message Examples — https://uxwritinghub.com/error-message-examples/
- LogRocket — Tones of Voice in UX Writing — https://blog.logrocket.com/ux-design/tones-of-voice-ux-writing/
- LogRocket — Empty States Done Right — https://blog.logrocket.com/ux-design/empty-states-ux-examples/

### Error messages + form validation

- CXL — Error Messages Best Practices — https://cxl.com/blog/error-messages/
- Baymard Institute — Form Field Usability Research — https://baymard.com/
- IvyForms — Error Message Examples — https://ivyforms.com/blog/form-error-message-examples/
- Webdesign Tutsplus — Form Errors Microcopy — https://webdesign.tutsplus.com/best-practices-for-displaying-form-errors--CRS-200950c/use-microcopy
- Julia Clementson — Microcopy for Error Prevention — https://juliaclementson.com/blog/microcopy-for-error-prevention-how-to-design-for-fewer-mistakes
- ParallelHQ — UX Writing Best Practices — https://www.parallelhq.com/blog/ux-writing-best-practices
- FAQprime — UX Microcopy Form Field Templates — https://faqprime.com/en/how-to-write-ux-microcopy-for-form-field-texts-copy-paste-templates/

### Empty states + onboarding + 404

- Carbon Design System — Empty States — https://carbondesignsystem.com/patterns/empty-states-pattern/
- UXPin — Empty States Best Practices — https://www.uxpin.com/studio/blog/ux-best-practices-designing-the-overlooked-empty-states/
- Mobbin — Empty State Design Variants — https://mobbin.com/glossary/empty-state
- Setproduct — Empty State UI Design — https://www.setproduct.com/blog/empty-state-ui-design
- Eleken — Empty State UX Examples — https://www.eleken.co/blog-posts/empty-state-ux
- UserOnboard — Onboarding UX Patterns — https://www.useronboard.com/onboarding-ux-patterns/empty-states/
- Pencil & Paper — Empty States Examples — https://www.pencilandpaper.io/articles/empty-states

### Buttons + CTAs

- Shopify — Microcopy 2026 Guide — https://www.shopify.com/enterprise/blog/how-to-write-microcopy-that-influences-customers-even-if-they-don-t-read-it
- BrandVM — UX Writing for Conversion — https://www.brandvm.com/post/ux-writing-conversion-microcopy
- CorsoUX — 30 Microcopy Examples Boost Conversion — https://courseux.com/microcopy-examples/
- Bird — UX Writing Best Practices — https://bird.marketing/blog/digital-marketing/guide/ux-design-principles/ux-writing-best-practices/
- Frontitude Blog — Voice and Tone — https://www.frontitude.com/blog/defining-your-products-voice-and-tone-for-the-best-ux

### 2026 trends + AI UX writing

- Eric Wong Content Strategist — UX Writing 2026 AI — https://www.ericwongcontentstrategist.com/post/the-definitive-guide-to-ux-writing-2026-how-ai-is-changing-microcopy-forever
- Web Design Inspiration — 7 AI Tools UI/UX 2026 — https://www.webdesign-inspiration.com/article/7-ai-tools-that-are-actually-changing-ui-ux-design-in-2026/
- Medium Bootcamp — Microcopy in UX Design Importance — https://medium.com/design-bootcamp/the-importance-of-microcopy-in-ux-design-writing-effective-button-labels-error-messages-and-0a9c2c6eaa38
- Medium Ebabatunde — Microcopy in UX Writing 2026 — https://medium.com/@ebabatunde15/microcopy-in-ux-writing-8bdd44350c1b
- Medium Udeaniokeprecious — Microcopy Small Words — https://medium.com/@udeaniokeprecious/microcopy-in-ux-design-the-small-words-that-shape-big-experiences-98401eece4f4
- Ecommerce Fastlane — Microcopy Shopify 2026 — https://ecommercefastlane.com/writing-microcopy-a-2026-guide-for-ecommerce-ux-with-examples-shopify/

### Brasil PT-BR

- GOV.BR Padroes Writing Microcopy — https://www.gov.br/ds/padroes/writing/microcopy
- Alura — Como Melhorar UX com Microcopy — https://www.alura.com.br/artigos/como-melhorar-a-ux-com-microcopy
- Cabrun Conteudos — Microcopy UX Writing — https://www.cabrunconteudos.com.br/microcopy-entenda-o-que-e-esse-termo-de-ux-writing-e-os-impactos-no-usuario/
- Search One Digital — Microcopy e UX Writing — https://searchonedigital.com.br/blog/microcopy-e-ux-writing/
- Aintegrare Wiki MKT — Microcopy UX Writing — https://aintegrare.com.br/wiki/microcopy
- Vagas UX — Guia Product Designer Writing — https://vagasux.com.br/guia-do-product-designer/recursos/writing
- Busca Cliente Blog — Microcopy UX Writing — https://www.buscacliente.com.br/blog/microcopy-e-ux-writing-transformando-palavras-em-experiencias-digitais/
- Juliana Fajardini — UX Writing entendendo Microcopy — https://jufajardini.wordpress.com/2020/08/17/ux-writing-entendendo-mais-o-que-e-microcopy/

### Style guides empresas BR-relevantes

- Nubank — https://nubank.com.br/
- iFood — https://www.ifood.com.br/
- Magazine Luiza — Lu da Magalu — https://www.magazineluiza.com.br/
- Itau — https://www.itau.com.br/
- RD Station — https://www.rdstation.com/

### Tools 2026

- Frontitude — UX writing platform — https://www.frontitude.com/
- Writer.com — Enterprise content + style — https://writer.com/
- Grammarly Business — https://www.grammarly.com/business
- Hemingway Editor — https://hemingwayapp.com/
- Hotjar — https://www.hotjar.com/
- UXcam — https://uxcam.com/
- Maze — https://maze.co/
- UserTesting — https://www.usertesting.com/
- Lokalise — https://lokalise.com/
- axe DevTools — https://www.deque.com/axe/devtools/

### NN/g + voice/tone style guides

- LinkedIn — Voice and Tone Guidelines Advice — https://www.linkedin.com/advice/3/how-do-you-create-voice-tone-guidelines-ux-writing
- UX Design Institute — Tone of Voice — https://www.uxdesigninstitute.com/blog/tone-of-voice-for-ux-writing/
- Deliveroo Design — Voice and Tone UX Writing — https://medium.com/deliveroo-design/how-to-use-voice-and-tone-in-ux-writing-a66981c78d20
- Working In Content — Style Guides — https://workingincontent.com/resources/content-style-guides
- Medium Bootcamp Haley Hougardy — UX Writing 101 Tone — https://medium.com/design-bootcamp/ux-writing-101-a-beginners-guide-to-mastering-tone-of-voice-c2e81fba2651

### Acessibilidade + dark patterns

- WCAG 2.1 — https://www.w3.org/TR/WCAG21/
- Deceptive Patterns — https://www.deceptive.design/
- ANPD Brasil — https://www.gov.br/anpd/
- LGPD — Lei 13.709/2018 — http://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm

---

## Cross-Skill References

| Situacao | Skills relacionadas |
|----------|----------------------|
| Microcopy + heuristicas Nielsen | `microcopy` + `ux-heuristicas` (anterior bloco UX/UI) |
| Microcopy + acessibilidade WCAG | `microcopy` + `acessibilidade-wcag` (proxima bloco UX/UI) |
| Microcopy + design tokens / componentes | `microcopy` + `design-system-basico` (proxima bloco UX/UI) |
| Voice deriva de brand identity | `microcopy` + `branding` (bloco Marketing & Estrategia) |
| Tom + posicionamento mental | `microcopy` + `posicionamento-marca` (bloco Marketing & Estrategia) |
| Microcopy vs advertising copy | `microcopy` + `redacao-publicitaria` (bloco Copy & Redacao — diferenca critica) |
| Microcopy vs direct response | `microcopy` + `copywriting-conversao` (bloco Copy & Redacao — diferenca critica) |
| AI UX writing + drafting | `microcopy` + `tecnicas-ia-claude-gemini-mkt` |
| Funil + emotional moments | `microcopy` + `funil-jornada` |
| Persona dirige tom | `microcopy` + `persona-icp-deep` |
| Storytelling no produto | `microcopy` + `storytelling` |
| Email transacional + UI | `microcopy` + `email-marketing` |
| KPIs UX writing | `microcopy` + `metricas-marketing` |
| Localizacao PT-BR + escrita por publico | `microcopy` + `escrita-por-publico` |
| Persuasao etica em microcopy | `microcopy` + `persuasao-eticas` |

---

## Integracao Ecossistema Frank-MKT

- **Acoplamento com `ux-heuristicas` (anterior bloco UX/UI 1a)** — heuristicas Nielsen sao o framework geral; microcopy e a expressao verbal das heuristicas (visibility of system status = loading messages claras; help users recognize/recover errors = mensagens de erro Yifrah; help and documentation = helper text + tooltips).
- **Acoplamento com `acessibilidade-wcag` (proxima bloco UX/UI)** — labels acessiveis + ARIA + screen reader compatibility + contraste + nao depender so de cor sao requisitos WCAG que esta skill aplica em copy.
- **Acoplamento com `design-system-basico` (proxima bloco UX/UI)** — design system inclui tokens de copy (default/empty/error/loading/success states) integrados via Frontitude/Storybook; microcopy NAO mora apenas em codebase, mora em design system.
- **Acoplamento com `branding` (bloco Marketing & Estrategia)** — brand voice deriva da identidade de marca (arquetipo + valores + personalidade); microcopy operacionaliza essa voz em UI.
- **Acoplamento com `posicionamento-marca`** — positioning mental ("o banco simples") informa tom de microcopy ("simples como conversa entre amigos").
- **Acoplamento com `redacao-publicitaria` (bloco Copy & Redacao)** — distincao critica: microcopy NAO e advertising copy; redacao publicitaria mira awareness + memorabilidade, microcopy mira navegacao + reducao friccao. Voice consistente cross-disciplinas, tom adapta.
- **Acoplamento com `copywriting-conversao` (bloco Copy & Redacao)** — distincao critica: copy de conversao mira acao imediata (LP, ads, sales letter), microcopy mira uso eficaz do produto. Sobreposicao em CTAs de produto (signup, checkout) onde ambos contribuem.
- **Acoplamento com `tecnicas-ia-claude-gemini-mkt`** — Claude/Gemini/ChatGPT geram 1st draft de microcopy (botoes, erros, empty states, variantes); UX writer humano refina com strategy + voice + edge cases + ethics. AI = rascunho; humano = decisao.
- **Acoplamento com `funil-jornada`** — copy varia por etapa do funil + por emotional state do usuario (TOFU encorajador, MOFU explicativo, BOFU acionavel, retention empatico).
- **Acoplamento com `persona-icp-deep`** — persona define tom (jovem urbano = casual; B2B financeiro = formal; idoso = simples + grande font + linguagem direta).
- **Acoplamento com `storytelling`** — narrativa estrutura sequencias de microcopy (onboarding flow + empty state journey).
- **Acoplamento com `email-marketing`** — emails transacionais (signup, password reset, order confirmation) sao microcopy estendido; voice consistent com produto.
- **Acoplamento com `metricas-marketing`** — KPIs microcopy (drop-off, conversion, support tickets, task success, time-to-complete) sao subset de KPIs MKT mais amplos.
- **Acoplamento com `escrita-por-publico`** — microcopy adapta-se a publico (B2B vs B2C vs governo vs jovem urbano vs senior).
- **Acoplamento com `persuasao-eticas`** — Cialdini reciprocidade + autoridade aplicaveis em microcopy (helper text reciprocidade; "verificado por X" autoridade), MAS evitar dark patterns + manipulacao. Etica e core.
- **Acoplamento com `comunicacao-corporativa`** — voice institucional vs voice de produto: microcopy e voice de produto (mais conversacional); comunicacao corporativa e voice institucional (mais formal). Marca consistente, registros diferentes.
- **Acoplamento com o agente `auditor`** — auditor roda regras PASS/FAIL em microcopy (botao com verbo + objeto + nao generico; mensagem de erro com what/why/what-to-do + nao culpa usuario; label visivel + nao apenas placeholder; empty state com heading + motivation + CTA; PT-BR idiomatico + voce/tu decidido + nao traducao mecanica; a11y review feita; legal/LGPD review feita; dark patterns ausentes; user interviews 5-10 + usability testing realizados; consistencia voice & tone com style guide).
- **Memoria** — `.frank-mkt/microcopy/<projeto>/<release>/` (style guide, microcopy inventory planilha, design system tokens copy, validation user research + usability + a11y + legal, A/B test results, post-release KPIs + iteracoes).
- **Contraditorio interno** — Checklist Sec "Checklist Contraditorio Interno (10 perguntas)".
- **Decaimento temporal** — volatility `medium` (6 meses) — fundamentos Yifrah + Mailchimp + 4 Cs timeless; trends 2026 (AI UX writing + voice interfaces + dark patterns regulamentadas + LGPD UX) requerem revisao semestral; style guides de produto (Atlassian/Shopify/Stripe) atualizam continuamente.
- **STATUS BLOCO UX/UI** — esta skill e a **2a do Bloco UX/UI** — junto com `ux-heuristicas` (1a) + proximas (`acessibilidade-wcag`, `design-system-basico`, etc.) — **2/N do bloco em construcao**.
- **Regra de ouro para `frank-mkt`** — nenhum redesign de produto, lancamento de feature, refactor de copy de UI, novo style guide de marca, ou auditoria de dark patterns / LGPD UX sai do plugin sem passar por esta skill — incluindo verificacao 4 Cs + voice/tone documentada + Yifrah formula em empty states + erros what/why/what-to-do + label > placeholder + a11y review + PT-BR idiomatico + 5-10 user interviews + usability testing + legal/LGPD review.

---

> **Aviso:** o plugin `frank-mkt` e um assistente de analise educacional. Recomendacoes desta skill devem ser adaptadas a brand, audiencia, mercado, contexto cultural local (BR + global), e validadas com **5-10 user interviews + usability testing + acessibilidade review (screen readers + WCAG 2.1 AA + ARIA) + legal/LGPD review + senior UX writer review + dark patterns audit** antes de publicar mudancas em copy de UI critico (signup, checkout, billing, exclusao de conta, consent banner, formularios regulados). Esta skill e de volatility `medium` (6 meses) — fundamentos Yifrah + Mailchimp + 4 Cs timeless; tendencias 2026 (AI UX writing + voice interfaces + dark patterns regulamentadas + LGPD UX) atualizam semestralmente; style guides de produto industria atualizam continuamente.

---

*Plugin `frank-mkt` — skill `microcopy` (v0.1.0)*
*Ultima atualizacao: 2026-05-09*
*Status bloco: 2a do Bloco UX/UI — 2/N do bloco em construcao*
*Pesquisa de campo: 6 web searches em 2026-05-09 (microcopy 2026 framework UX writing button labels error messages; UX writing 2026 voice tone style guide content design; error messages microcopy 2026 best practices form validation; empty state UI design 2026 onboarding tooltips microcopy; microcopy Brasil 2026 portuguese UX writing PT-BR translations; Kinneret Yifrah Microcopy book UX writers 2026 frameworks)*
