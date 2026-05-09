---
name: acessibilidade-wcag
description: Acessibilidade web (WCAG 2.2 + ADA + Brasil LBI 13.146/2015 + screen readers ARIA + keyboard nav + color contrast + assistive tech + inclusive design) para founders/devs/designers/PMs/agencias/juridico, com cobertura WCAG 2.2 W3C 2023 + 9 novos criterios + ADA Title III lawsuits 2024+ exploding, Brasil LBI obrigatoria sites publicos + comerciais + Decreto 9.296/2018, screen readers (NVDA + JAWS + VoiceOver + TalkBack), ARIA roles/states/properties, Microsoft Inclusive Design framework, Deque axe-core open-source. 3a SKILL Bloco UX/UI.
volatility: medium
last_review: 2026-05-09
next_review: 2026-11-09
languages: [pt-BR]
audience: [founders, devs, designers, PMs, agencias, juridico, DPO, accessibility-specialists]
ascii_only: true
---

# Skill: acessibilidade-wcag

> Acessibilidade nao e feature opcional. E direito humano (ONU CDPD), obrigacao legal (LBI Brasil + ADA EUA + EAA UE) e vantagem competitiva (1 bilhao+ pessoas com deficiencia globalmente, 18,6 milhoes no Brasil segundo IBGE 2022). Esta skill ensina como projetar, codar e auditar produtos digitais conforme WCAG 2.2 (W3C 2023), Lei Brasileira de Inclusao 13.146/2015 + Decreto 9.296/2018, ADA Title III (lawsuits batendo recordes 2024-2026) e principios de inclusive design. Foco operacional, nao apenas teorico.

---

## Decaimento Temporal

- **Volatilidade:** medium
- **last_review:** 2026-05-09
- **next_review:** 2026-11-09 (6 meses)
- **Triggers de re-review antecipado:**
  - Publicacao WCAG 2.3 (rascunho W3C esperado 2026-2027)
  - WCAG 3.0 Silver mover para Candidate Recommendation
  - Mudancas no Decreto 9.296/2018 ou regulamentacao e-MAG (governo federal)
  - Nova ISO/IEC 40500:2026 (WCAG 2.2 ratificado como ISO end of 2026)
  - DOJ ADA Title II prazos finais (2026-04-26 para entes <50k habitantes)
  - Lancamento NVDA major release / JAWS major / iOS major com mudancas VoiceOver
  - Tribunais brasileiros: STJ/STF jurisprudencia consolidada sobre LBI digital
  - ANPD se manifestando sobre interseccao LGPD x acessibilidade

**Por que medium:** Padroes WCAG sao estaveis (versao 2.2 publicada 2023-10, raras mudancas), mas legislacao (ADA lawsuits surge 37% YoY) e jurisprudencia brasileira (CGUs + MPF) estao em ciclo de amadurecimento 2025-2027. Ferramentas (axe, Lighthouse) atualizam a cada 3-6 meses.

---

## Visao Geral

Acessibilidade web e o desenho e desenvolvimento de produtos digitais que podem ser usados por pessoas com deficiencias permanentes (visual, auditiva, motora, cognitiva), temporarias (braco quebrado, otite, fadiga) e situacionais (sol forte na tela, ambiente barulhento, mao ocupada com bebe). Cobre 1 bilhao+ pessoas globalmente e ~25% da populacao adulta brasileira (IBGE 2022 PNAD).

**O que esta skill cobre:**
- WCAG 2.2 (W3C 2023): 4 principios POUR + 13 guidelines + 78 criterios + 9 novos 2.2
- ADA Title III (USA): lawsuits 4500+/ano em 2026, California + NY + FL hotspots
- Brasil: LBI 13.146/2015 + Decreto 9.296/2018 + e-MAG v3.1 (governo federal) + selo Acessibilidade Web
- EU: EAA (European Accessibility Act, vigente 2025-06)
- Screen readers: NVDA (Windows, gratuito, 30%+ market), JAWS (enterprise), VoiceOver (iOS/macOS nativo), TalkBack (Android)
- ARIA: roles, states, properties, landmarks, live regions
- Keyboard navigation: tab order, skip links, focus indicators, escape modal
- Color contrast: 4.5:1 AA / 7:1 AAA / 3:1 large text
- Inclusive design: framework Microsoft (recognize exclusion / solve for one / learn from diversity)
- Tools: axe DevTools, WAVE, Lighthouse, Stark, Pa11y, Siteimprove

**O que esta skill NAO cobre (ver outras skills):**
- UX heuristicas Nielsen ver `ux-heuristicas`
- Microcopy / writing acessivel ver `microcopy`
- Design system tokens ver `design-system-basico`
- LGPD / privacidade ver `dominio-juridico-mkt`
- Branding visual ver `branding`

---

## Fundacao 1 — WCAG 2.2 Foundations: POUR + 13 Guidelines + 78 Criterios + 9 Novos 2.2

A Web Content Accessibility Guidelines 2.2 foi publicada em **05/10/2023** pela W3C (WAI - Web Accessibility Initiative) e e o padrao de fato global para acessibilidade web. Em **dezembro 2024**, a versao final foi consolidada e deve se tornar **ISO/IEC 40500:2026** ate final de 2026.

### Estrutura: 4 Principios POUR

WCAG organiza tudo sob 4 principios chamados **POUR** (acronimo em ingles):

**1. Perceivable (Perceptivel)** — informacao e UI devem ser apresentadas de formas que usuarios possam perceber. Nao pode estar invisivel para todos os sentidos.

**2. Operable (Operavel)** — UI e navegacao devem ser operaveis. Usuario tem que conseguir acionar.

**3. Understandable (Compreensivel)** — informacao e operacao da UI devem ser entendiveis. Nao pode ser misterioso.

**4. Robust (Robusto)** — conteudo deve ser robusto o suficiente para ser interpretado por uma ampla variedade de user agents, incluindo tecnologias assistivas.

### 13 Guidelines

Sob os 4 principios, ha 13 guidelines:

- **1.1** Text Alternatives (alt text para imagens)
- **1.2** Time-based Media (legendas, audiodescricao)
- **1.3** Adaptable (estrutura semantica, ordem)
- **1.4** Distinguishable (contraste, redimensionamento)
- **2.1** Keyboard Accessible
- **2.2** Enough Time
- **2.3** Seizures and Physical Reactions (max 3 flashes/seg)
- **2.4** Navigable
- **2.5** Input Modalities
- **3.1** Readable
- **3.2** Predictable
- **3.3** Input Assistance
- **4.1** Compatible

### 3 Niveis de Conformidade: A / AA / AAA

- **Level A** (minimum) — barreiras mais criticas. Sem isso, site e inutilizavel para muitos.
- **Level AA** (standard global) — exigido por **maioria das leis**: ADA Title III, Section 508 USA, EN 301 549 UE, AODA Canada, LBI Brasil.
- **Level AAA** (maximum) — W3C admite que nem sempre e possivel atingir AAA para todo conteudo. Nao se exige conformidade total AAA.

### 78 Criterios de Sucesso (Success Criteria)

WCAG 2.2 tem **78 criterios testaveis** distribuidos:
- 32 criterios Level A
- 24 criterios Level AA
- 22 criterios Level AAA

### 9 Novos Criterios da Versao 2.2 (vs 2.1)

WCAG 2.2 adicionou **9 novos criterios** focados em usuarios com deficiencias cognitivas, motoras e baixa visao:

1. **2.4.11 Focus Not Obscured (Minimum)** [AA] — quando elemento recebe foco, nao pode estar totalmente coberto por overlay/sticky.
2. **2.4.12 Focus Not Obscured (Enhanced)** [AAA] — nao pode estar nem parcialmente coberto.
3. **2.4.13 Focus Appearance** [AAA] — indicador de foco com tamanho minimo + contraste.
4. **2.5.7 Dragging Movements** [AA] — toda funcionalidade de arrastar deve ter alternativa de clique simples.
5. **2.5.8 Target Size (Minimum)** [AA] — alvos clicaveis minimo 24x24 CSS pixels.
6. **3.2.6 Consistent Help** [A] — mecanismo de ajuda na mesma posicao em todas as paginas.
7. **3.3.7 Redundant Entry** [A] — nao exigir reentrar mesma informacao na mesma sessao.
8. **3.3.8 Accessible Authentication (Minimum)** [AA] — autenticacao sem teste cognitivo (sem captcha-puzzle).
9. **3.3.9 Accessible Authentication (Enhanced)** [AAA] — sem reconhecimento de objeto/imagem.

**Backwards-compatible:** site WCAG 2.2 conforme tambem e WCAG 2.1 e WCAG 2.0 conforme.

### Criterios Mais Quebrados (WebAIM Million 2024)

Top 6 falhas em 1 milhao de homepages:
1. Low contrast text (81% das paginas)
2. Missing alt text (54%)
3. Empty links (50%)
4. Missing form labels (49%)
5. Empty buttons (28%)
6. Missing document language (17%)

> 96% das homepages testadas tinham pelo menos uma falha WCAG. Acessibilidade nao e edge case — e regra.

---

## Fundacao 2 — ADA + Section 508 + International Laws (USA + UE + Canada)

### USA: ADA Title III + Title II + Section 508

**ADA (Americans with Disabilities Act) - 1990** e a lei federal que proibe discriminacao contra pessoas com deficiencia. Tem 5 Titles:
- **Title I:** emprego
- **Title II:** governos estaduais e locais
- **Title III:** **businesses (publicly accommodated)** — sites comerciais incluidos
- **Title IV:** telecomunicacoes
- **Title V:** miscellaneous

**ADA Title III + Web:** corte federal vem entendendo desde 2010s que sites de empresas publicamente acessadas (e-commerce, bancos, restaurantes, healthcare) sao "places of public accommodation" e portanto cobertos.

### Lawsuits ADA Title III: Explosao 2024-2026

- **2024:** 4500+ lawsuits federais
- **2025:** ~5500+ projetados (37% YoY increase)
- **2026 Q1:** 3500-4500 cases projetados
- **Pro se filings:** +40% em 2025 (individuos sem advogado, usando ChatGPT/Copilot/Gemini para redigir)
- **Hotspots geograficos:** California (3252 cases 2024), New York (2220), Florida (1627)
- **Padrao referenciado pelas cortes:** WCAG 2.1 AA (sera 2.2 AA em breve)

### Title II Final Rule (DOJ 2024)

Em **2024-04-08**, DOJ publicou regra final exigindo governos estaduais e locais (e suas terceiras partes) cumprirem **WCAG 2.1 AA** ate:
- **2026-04-24:** entes >=50k habitantes
- **2026-04-26 (extendido para 2027-04-26 em abril 2026):** entes <50k habitantes

### Section 508 (Federal USA)

**Section 508 of the Rehabilitation Act** exige que tecnologia federal (sites, software, hardware) seja acessivel. Atualizado em **2018 (508 Refresh)** para alinhar com **WCAG 2.0 AA** (sendo migrado para 2.1 AA / 2.2 AA gradualmente).

### Uniao Europeia: EAA + EN 301 549

**EAA (European Accessibility Act, Diretiva 2019/882)** entra em vigor **28/06/2025** e cobre:
- E-commerce websites
- Bank services
- Smartphones, computers, e-readers
- Self-service terminals (ATMs, ticket machines)
- Transportation services digital interfaces
- Audiovisual media services

**Padrao tecnico:** **EN 301 549 v3.2.1** (2021), que adota WCAG 2.1 AA (com expansao para WCAG 2.2 em revisao).

### Canada: AODA + ACA

- **AODA (Accessibility for Ontarians with Disabilities Act, 2005):** WCAG 2.0 AA exigido desde 2014 para sector privado >50 employees.
- **ACA (Accessible Canada Act, 2019):** federal, exige planos de acessibilidade publicados.

### Outros: Australia (DDA), Israel (IS 5568), Japao (JIS X 8341)

Maioria dos paises ocidentais adotou WCAG 2.0 AA ou 2.1 AA como referencia tecnica em suas leis nacionais.

### Settlements + Damages

ADA Title III nao prevê damages federais, MAS:
- California (Unruh Civil Rights Act): **$4000 minimo por visit** + attorney fees
- New York City Human Rights Law: dano emocional + punitive
- Settlements tipicos: $5k-$50k + remediacao tecnica + monitoring 1-2 anos
- Reincidencia: dobra/triplica

> Custo de prevencao (audit + remediacao) e ordens de magnitude menor que custo de litigation.

---

## Fundacao 3 — Screen Readers + ARIA: NVDA, JAWS, VoiceOver, TalkBack

### O Que Sao Screen Readers

Software que le conteudo da tela em voz alta + permite navegacao via teclado/gestos. Usado primariamente por:
- Pessoas cegas ou com baixa visao severa (~285 milhoes globalmente segundo OMS)
- Pessoas com dislexia severa (alguns)
- Pessoas com transtornos cognitivos (alguns)

### Os 4 Screen Readers Dominantes

**1. NVDA (NonVisual Desktop Access)**
- **Plataforma:** Windows
- **Custo:** **GRATUITO** (open-source, NV Access fundacao australiana)
- **Market share:** 30%+ (WebAIM Survey #10)
- **Browser pareado:** Firefox + Chrome (Edge tambem ok)
- **Uso recomendado:** standard para QA acessibilidade dev

**2. JAWS (Job Access With Speech)**
- **Plataforma:** Windows
- **Custo:** $1.475 USD home / $1.475 USD profissional + assinaturas SMA
- **Market share:** ~40% (declining vs NVDA)
- **Browser:** Chrome + Edge primariamente
- **Uso recomendado:** enterprise, governo, audits formais

**3. VoiceOver**
- **Plataforma:** macOS + iOS + iPadOS + watchOS (NATIVO Apple, gratuito)
- **Browser:** Safari (otimizado)
- **Uso recomendado:** mandatorio para QA mobile iOS + macOS

**4. TalkBack**
- **Plataforma:** Android (NATIVO Google, gratuito)
- **Browser:** Chrome
- **Uso recomendado:** mandatorio para QA mobile Android

### Matriz de Teste Recomendada

Para cobertura realista (Fundacao Deque 2025):
| Sistema | Screen Reader | Browser |
|---------|---------------|---------|
| Windows | NVDA | Firefox + Chrome |
| Windows | JAWS (se enterprise) | Chrome |
| macOS | VoiceOver | Safari |
| iOS | VoiceOver | Safari |
| Android | TalkBack | Chrome |

### ARIA (Accessible Rich Internet Applications)

**ARIA** e especificacao W3C que adiciona semantica acessivel a elementos HTML quando HTML nativo nao basta. Versao atual: **WAI-ARIA 1.2** (2023).

### 5 Regras de Ouro do ARIA (W3C)

**Regra #1:** Se voce pode usar HTML nativo, USE HTML NATIVO. ARIA e plano B.
- Errado: `<div role="button" tabindex="0" onclick="...">Submit</div>`
- Certo: `<button>Submit</button>`

**Regra #2:** Nao mude semantica nativa, exceto se obrigatorio.
- Errado: `<h1 role="button">` (quebra estrutura de cabecalhos)

**Regra #3:** Todo controle interativo ARIA deve ser operavel via teclado.

**Regra #4:** Nao use `role="presentation"` ou `aria-hidden="true"` em elementos focaveis.

**Regra #5:** Todo elemento interativo deve ter nome acessivel (accessible name).

### Tres Pilares ARIA: Roles, States, Properties

**Roles:** o que o elemento E. Ex: `role="button"`, `role="dialog"`, `role="navigation"`.

**States:** estado dinamico. Ex: `aria-expanded="true"`, `aria-checked="false"`, `aria-disabled="true"`.

**Properties:** caracteristicas mais estaticas. Ex: `aria-label="Fechar"`, `aria-labelledby="title-id"`, `aria-describedby="help-id"`.

### Landmarks: Navegacao Estrutural

Landmarks sao regioes semanticas que permitem ao usuario de screen reader pular direto para secoes:
- `<header>` ou `role="banner"` — topo da pagina
- `<nav>` ou `role="navigation"` — menus
- `<main>` ou `role="main"` — conteudo principal (so um por pagina)
- `<aside>` ou `role="complementary"` — sidebar
- `<footer>` ou `role="contentinfo"` — rodape
- `<form>` ou `role="form"` (com label) — formularios
- `<section>` (com label) ou `role="region"` — regioes nomeadas

**Atalhos de teclado para landmarks:**
- NVDA: `D` para landmarks
- JAWS: `R` para regions
- VoiceOver: `VO+U` (rotor) -> Landmarks

### Live Regions: Anuncio de Mudancas Dinamicas

Quando conteudo muda dinamicamente (ex: notificacao "5 novos emails", contador de carrinho), screen reader precisa ser avisado. Use `aria-live`:
- `aria-live="polite"` — espera usuario terminar de ler atual antes de anunciar
- `aria-live="assertive"` — interrompe imediatamente (use para urgencias!)
- `role="alert"` — atalho para `aria-live="assertive"` + `aria-atomic="true"`
- `role="status"` — atalho para `aria-live="polite"`

### Erros Frequentes ARIA

1. **`aria-label` em elemento que ja tem texto visivel** — viola WCAG 2.5.3 Label in Name. Screen reader le `aria-label` mas usuario de voice control diz texto visivel = mismatch.
2. **`role="button"` em `<div>` sem keyboard handler** — sem Enter/Space funciona, falha 2.1.1.
3. **`aria-hidden="true"` em elemento focavel** — usuario teclado tabula em elemento "invisivel" para screen reader.
4. **Multiplos `role="main"` na mesma pagina** — sempre 1 so.
5. **Modal sem `aria-modal="true"` + focus trap** — usuario sai do modal sem perceber.

---

## Fundacao 4 — Keyboard Navigation + Focus Management

Pessoas que nao podem usar mouse (cegas, motoras, dislexia severa, com tendinite, com mao quebrada) navegam por teclado. **TODA funcionalidade deve ser operavel via teclado** (WCAG 2.1.1 Keyboard, Level A).

### Teclas Essenciais

- **Tab:** avanca para proximo elemento focavel
- **Shift+Tab:** retrocede
- **Enter:** ativa link / botao
- **Space:** ativa botao / checkbox / scroll page
- **Arrow keys:** navega dentro de componentes (radio group, menu, listbox, slider, tabs)
- **Esc:** fecha modal, dropdown, dismiss
- **Home / End:** comeco / fim de campo ou lista

### Tab Order: Logico, Nao Visual

Tab order deve seguir leitura natural (top-to-bottom, left-to-right em LTR). Se tab pular pra lugar inesperado, e bug. **Nunca use `tabindex="2"` ou maior** — gera ordem confusa.

- `tabindex="0"` — elemento entra na tab order natural (use em divs interativas que voce DEVE tornar focaveis)
- `tabindex="-1"` — elemento NAO recebe Tab, mas pode receber `.focus()` programatico (use em modal heading para mover foco)

### Skip Links: Pular Cabecalho Repetido

Em todas as paginas internas, primeira tabulacao deve oferecer link "Pular para conteudo principal":

```html
<a href="#main-content" class="skip-link">Pular para conteudo principal</a>
...
<main id="main-content">...</main>
```

CSS deve esconder ate receber foco (NUNCA `display:none`):
```css
.skip-link {
  position: absolute;
  left: -9999px;
}
.skip-link:focus {
  left: 0;
  top: 0;
}
```

### Focus Indicators: WCAG 2.4.7 (AA) + 2.4.13 (AAA WCAG 2.2)

**NUNCA** remova outline sem substituir:
```css
/* RUIM - remove indicador */
*:focus { outline: none; }

/* BOM - estiliza melhor */
*:focus-visible {
  outline: 3px solid #0066cc;
  outline-offset: 2px;
}
```

WCAG 2.2 adicionou **2.4.13 Focus Appearance (AAA):** indicador minimo 2px de borda + contraste 3:1 entre indicador e estados.

### Focus Trap em Modais

Quando modal abre:
1. Mover foco para primeiro elemento focavel do modal (ou para heading com `tabindex="-1"`)
2. Travar Tab dentro do modal (loop entre primeiro e ultimo elemento)
3. Esc fecha + retorna foco para elemento que abriu o modal
4. Adicionar `aria-modal="true"` + `role="dialog"` + `aria-labelledby`

### Focus em SPA / Route Changes

Em SPAs (React, Vue, Angular), trocar de "pagina" via router NAO move foco automaticamente. Usuario de screen reader continua focado em link clicado. Solucao: mover foco para `<h1>` ou heading da nova pagina via `useEffect` + `ref.current.focus()`.

### WCAG 2.4.11 Focus Not Obscured (NOVO 2.2 AA)

Quando elemento recebe foco, nao pode estar **totalmente** coberto por sticky header/footer/overlay. Comum: input em form, ao receber foco, fica embaixo de cookie banner — falha.

### Keyboard Patterns por Componente (ARIA Authoring Practices)

W3C publica **ARIA Authoring Practices Guide (APG)** com 30+ padroes:
- Combobox: Arrow Down abre, Arrow keys navegam, Enter seleciona, Esc fecha
- Tabs: Arrow Left/Right entre tabs, Tab para conteudo
- Tree: Arrow Down/Up navegam, Right/Left expand/collapse
- Slider: Arrow keys + Home/End + PgUp/PgDown
- Datepicker: Arrow keys + PgUp (mes anterior) + Shift+PgUp (ano)

---

## Fundacao 5 — Color Contrast + Visual

Aproximadamente **2,2 bilhoes** de pessoas globalmente tem alguma deficiencia visual (OMS 2019). **8% dos homens** e **0,5% das mulheres** tem alguma forma de daltonismo (color blindness).

### WCAG 1.4.3 Contrast (Minimum) — Level AA

- **Texto normal:** contraste minimo **4,5:1**
- **Texto grande:** contraste minimo **3:1**
  - Texto grande = **18pt+ (24px+) regular** OU **14pt+ (18.66px+) bold**
- **UI components + graphical objects** (1.4.11): **3:1** (botoes, icones, bordas de input)

### WCAG 1.4.6 Contrast (Enhanced) — Level AAA

- **Texto normal:** contraste minimo **7:1**
- **Texto grande:** contraste minimo **4,5:1**

### Por Que 4,5:1 e 7:1?

- **4,5:1** compensa perda de sensibilidade equivalente a visao 20/40 (perda moderada)
- **7:1** compensa perda equivalente a visao 20/80 (perda severa)

### Ferramentas de Verificacao

- **WebAIM Contrast Checker** (gratis, web): https://webaim.org/resources/contrastchecker/
- **Stark** (Figma + Chrome ext): paid + free tier
- **axe DevTools** (Chrome ext): testa pagina inteira
- **Lighthouse** (Chrome DevTools): testa pagina inteira
- **APCA (Advanced Perceptual Contrast Algorithm):** algoritmo proximo (WCAG 3 Silver) que substitui 4,5:1 — ainda em rascunho

### Daltonismo: 4 Tipos

- **Deuteranomalia** (verde fraco): mais comum, 6% homens
- **Protanomalia** (vermelho fraco): 2% homens
- **Tritanomalia** (azul fraco): rara, ambos generos
- **Acromatopsia** (sem cor): muito rara

**Regra:** **NUNCA** use cor como UNICO meio de transmitir informacao (WCAG 1.4.1 Use of Color, Level A). Erro classico: "campos em vermelho sao obrigatorios" — invisivel para daltonicos. Use texto + icone + cor.

### Dark Mode Considerations

- Testar contraste tanto light quanto dark mode
- `prefers-color-scheme` media query
- Cuidado: cor mais comum de erro `#ff0000` tem contraste pessimo em fundo escuro

### Texto em Imagens (1.4.5)

Evite texto dentro de imagens. Texto real e:
- Selecionavel
- Pesquisavel
- Redimensionavel
- Traducivel
- Acessivel a screen readers

Excecao: logos.

### 1.4.10 Reflow (AA)

Conteudo deve ser usavel em viewport **320 CSS pixels** de largura sem scroll horizontal (exceto data tables, mapas).

### 1.4.12 Text Spacing (AA)

Usuario deve poder customizar:
- Line height: 1.5x font size
- Paragraph spacing: 2x font size
- Letter spacing: 0.12x font size
- Word spacing: 0.16x font size

Sem perda de funcionalidade. Testa: stylebot extension simulando.

### 1.4.13 Content on Hover or Focus (AA)

Tooltip ao hover deve ser:
- **Dismissable** (Esc fecha)
- **Hoverable** (mouse pode mover sobre o tooltip sem desaparecer)
- **Persistent** (nao some em 5 segundos arbitrarios)

---

## Fundacao 6 — Brasil 2026 LBI + Decreto 9.296/2018 + e-MAG + Compliance

### Lei Brasileira de Inclusao (LBI) - Lei 13.146/2015

Sancionada em **06/07/2015**, vigor desde **02/01/2016**, complementa a CDPD ONU (Convencao Internacional dos Direitos das Pessoas com Deficiencia, ratificada com status de emenda constitucional pelo Brasil em 2008).

### Artigo 63 — Acessibilidade Web Obrigatoria

**Texto literal (Art. 63):**

> "E obrigatoria a acessibilidade nos sitios da internet mantidos por empresas com sede ou representacao comercial no Pais ou por orgaos de governo, para uso da pessoa com deficiencia, garantindo-lhe acesso as informacoes disponiveis, conforme as melhores praticas e diretrizes de acessibilidade adotadas internacionalmente."

**Quem deve cumprir:**
- Orgaos de governo (federal, estadual, municipal)
- **TODA EMPRESA com sede no Brasil**
- TODA empresa com representacao comercial no Brasil

Nao ha excecao por porte. Microempresa, startup, e-commerce de bairro: todos cobertos.

### Artigo 63 §2 — Selo Nacional de Acessibilidade

Lei prevê **selo nacional de acessibilidade** (regulamentado parcialmente, em consolidacao final 2025-2026).

### Decreto 9.296/2018 — Regulamentacao

Decreto **9.296** de **01/03/2018** regulamenta acessibilidade dos sites do **governo federal**, exigindo conformidade com:
- **e-MAG** (Modelo de Acessibilidade em Governo Eletronico) - versao atual **3.1**
- e-MAG 3.1 esta alinhado com **WCAG 2.0 AA** (atualizacao para WCAG 2.1/2.2 em curso)

### e-MAG Modelo de Acessibilidade Governo Federal v3.1

Documento oficial mantido pelo **Ministerio da Gestao** (antes MPOG) e disponibilizado em:
- https://emag.governoeletronico.gov.br/
- Avaliador automatico **ASES** (Avaliador e Simulador de Acessibilidade de Sitios): https://asesweb.governoeletronico.gov.br/

ASES e ferramenta gratuita do governo brasileiro que gera relatorio de conformidade e-MAG.

### Decreto 5.296/2004 — Anterior, Mais Amplo

Decreto **5.296/2004** regulamentou Lei 10.098/2000 (acessibilidade fisica + comunicacao) e foi a primeira menca formal a acessibilidade web no Brasil. Continua vigente para aspectos nao revogados.

### Constituicao Federal — Art. 23 II

CF/88 estabelece competencia comum (Uniao + Estados + Municipios) para "cuidar da saude e assistencia publica, da protecao e garantia das pessoas portadoras de deficiencia". Base constitucional da LBI.

### Enforcement: MPF + MP Estaduais + Defensorias + ONGs

**2024-2026 Brasil:** ciclo de **maturidade de enforcement**.
- **2025:** aumento significativo de Acoes Civis Publicas pelos Ministerios Publicos (MPF + MPSP + MPRJ).
- Estados mais ativos: **Sao Paulo, Rio de Janeiro, Distrito Federal**.
- Defensoria Publica da Uniao tem propalado **TACs** (Termos de Ajustamento de Conduta) com grandes plataformas.
- **CGU** (Controladoria Geral) audita orgaos federais via ASES.
- ONGs: Movimento Web Para Todos, Acessibilidade Brasil, Mais Diferencas.

### Estatisticas Brasil

- **18,6 milhoes** de pessoas com deficiencia no Brasil (IBGE PNAD Continua 2022)
- **8,9%** da populacao adulta com 15+
- **3,4%** com deficiencia visual (cegos + baixa visao severa)
- **Web acessibilidade no Brasil:** **2% dos sites .gov.br** auditados em 2023 atingiram conformidade total (Movimento Web para Todos).

### LBI x LGPD: Interseccao

**LGPD** (Lei 13.709/2018) e **LBI** (13.146/2015) tem interseccao em:
- Consentimento acessivel (PCDs com deficiencia cognitiva precisam de termos legiveis)
- Direitos do titular acessiveis (formularios de exclusao precisam ser acessiveis)
- ANPD ainda nao se manifestou sobre acessibilidade especifica, mas e tendencia 2026-2027.

### Multas e Sancoes

LBI nao tem multa fixa para descumprimento de Art. 63, MAS:
- **MPF/MPE** pode entrar com Acao Civil Publica + dano moral coletivo (R$ 100k - R$ 1MM+)
- **TAC** com obrigacao de fazer + multa diaria por descumprimento
- **Procon** pode autuar por publicidade enganosa / vicio do servico
- **CDC** Art. 39: praticas abusivas
- **Reputacional:** midia + redes sociais penalizam

### Selo Nacional de Acessibilidade Web (Em Discussao)

Projeto de regulamentacao prevê 3 niveis:
- **Bronze:** WCAG A
- **Prata:** WCAG AA (esperado padrao default)
- **Ouro:** WCAG AAA + auditoria humana + testes com PCD

### Disclaimer Brasil

**ATENCAO:** Esta skill e educacional. Para aconselhamento juridico especifico sobre LBI, LGPD interseccao, contratos B2B com clausulas de conformidade ou processos administrativos, consulte advogado(a) especializado em Direito Digital + Acessibilidade. Esta skill **NAO substitui** consultoria juridica.

---

## Fundacao 7 — Mensuracao + Tools 2026

### Pirâmide de Testes Acessibilidade

```
                  Manual Testing + PCD
                  (~30-40% issues)
                /                    \
               /                      \
              / Manual Audit Especialista \
             /  (axe Pro + checklist humana)\
            /__________________________________\
           /                                    \
          /     Automated Tools (axe-core)        \
         /     (~30-40% das issues detectaveis)    \
        /__________________________________________\
```

**Realidade:** ferramentas automatizadas pegam **30-40%** dos issues de acessibilidade. Os outros **60-70%** requerem revisao humana + testes com PCD reais.

### Tools Open-Source / Free

**1. axe-core (Deque)** — engine open-source, base de quase tudo
- 3+ bilhoes de downloads
- 875k extensoes instaladas
- Microsoft contribuiu com regras Windows + Edge (parceria 2024)
- Engine usado em: axe DevTools, Lighthouse, Pa11y, jest-axe, cypress-axe

**2. axe DevTools (Chrome / Firefox / Edge ext)**
- Free tier
- Pro: $40/mo (intelligent guided tests, full-page scan)
- https://www.deque.com/axe/

**3. WAVE (WebAIM)**
- Free, web + Chrome ext
- Otimo para overview visual
- https://wave.webaim.org/

**4. Lighthouse (Chrome DevTools)**
- Built-in Chrome
- Score acessibilidade 0-100 (parcial, nao substitui audit completo)
- Roda axe-core por baixo

**5. Pa11y (CLI + CI)**
- Open-source CLI
- Integra CI/CD
- https://pa11y.org/

**6. Accessibility Insights (Microsoft)**
- Free, open-source
- FastPass + Assessment guiado
- Windows + Web + Android
- https://accessibilityinsights.io/

### Tools Comerciais

**1. Siteimprove**
- Enterprise SaaS
- Crawl site inteiro + dashboard + monitoring
- $$$ (talk to sales)

**2. Stark (Figma + Chrome)**
- Foco design phase (shift-left)
- $7-25/mo
- Color contrast + colorblind simulation + landmarks

**3. Level Access (antiga eSSENTIAL Accessibility)**
- Enterprise, audit + training + monitoring
- $$$$

**4. UserWay / accessiBe (Overlays)**
- **CONTROVERSO** — N�o sao recomendados pela comunidade!
- Adicionam widget JS que tenta "consertar" via overlay
- Cortes ADA tem rejeitado overlays como defesa
- Causam mais bugs do que resolvem para screen readers
- Muitos lawsuits ESPECIFICAMENTE contra sites usando overlays

### Tools Brasil

**ASES (Avaliador e Simulador de Acessibilidade de Sitios)**
- Governo federal, gratuito
- Avalia conformidade com e-MAG 3.1
- https://asesweb.governoeletronico.gov.br/

### Audits Manuais: O Que Pegar

Itens que **so testes humanos** detectam:
- Alt text "decorativo" usado para imagens informativas (vice-versa)
- Heading hierarchy quebrada (h1 -> h3 sem h2)
- Link text ambiguo: "clique aqui", "saiba mais", "leia mais"
- Tabela de dados sem `<th>` ou `scope`
- Animacoes sem opcao reduzir motion
- Form sem labels associadas (so placeholder)
- Modal sem focus trap
- Conteudo dinamico sem live region
- Logica de tab order
- Errors em forms sem aria-describedby

### CI/CD Integration

- **jest-axe** (Jest + RTL): testa acessibilidade em testes unitarios
- **cypress-axe / playwright-axe:** integra em E2E
- **pa11y-ci:** crawl + report no CI
- **GitHub Action axe-linter** ou **Pa11y Action**

Nao falhar build em qualquer violation (ruido), mas falhar em **critical + serious**.

### Testes com PCD Reais

Gold standard. Recrute via:
- **Fable Tech Labs** (Canada/USA, marketplace de testers PCD)
- **Applause** (com filtro PCD)
- **Movimento Web para Todos** (Brasil)
- **Mais Diferencas** (Brasil)

Nao substitui, complementa.

### KPIs de Acessibilidade

- **Conformance score** (% de criterios WCAG passando)
- **Critical + serious issues** (axe categoria)
- **Issues per 1000 elements**
- **Time to remediate** (issue criado -> closed)
- **Coverage** (% paginas auditadas)
- **User satisfaction** PCD (NPS especifico)

---

## Fundacao 8 — Aplicacao em Content MKT

Marketing digital tem **5 publicos** que essa skill atende:

### Audiencia 1: Founders / Empreendedores

**Sintoma:** "Preciso lancar MVP rapido, acessibilidade fica para depois."

**Argumento de risco:**
- Brasil: LBI 13.146/2015 Art. 63 cobre TODA empresa, sem excecao por porte
- USA: California $4k/visit minimo, settlement medio $5k-$50k
- UE: EAA 2025 cobre e-commerce, multas administrativas

**Argumento de oportunidade:**
- 18,6MM PCD Brasil + 1bn globalmente = mercado ignorado pelos competidores
- SEO: alt text + headings + semantica = melhor indexacao
- Velocidade: site acessivel e mais rapido (semantica reduz JS)

**Acao:** auditoria axe DevTools + corrigir top 3 (contraste + alt text + form labels) ja resolve ~40% issues.

### Audiencia 2: Devs

**Sintoma:** "Acessibilidade e responsabilidade do designer / QA."

**Argumento:**
- Acessibilidade nasce no codigo. CSS `outline:none` quebra. `<div onclick>` em vez de `<button>` quebra.
- Custo de retrofit: 10x maior que fazer certo desde o inicio
- jest-axe + cypress-axe em CI evita regressao

**Acao:** `npm i -D jest-axe @axe-core/playwright`. Add a 1 teste por componente.

### Audiencia 3: Designers

**Sintoma:** "Designer entrega Figma sem se preocupar com semantica."

**Argumento:**
- Stark plugin Figma checa contraste em tempo real
- Decisao de arquitetura visual (heading hierarchy, landmarks) acontece no design
- Designer precisa especificar estados focus/hover/active/disabled

**Acao:** Stark + dual-tone palette (primary + on-primary) com contraste 4.5:1+ ja documentado em design tokens.

### Audiencia 4: PMs / Product

**Sintoma:** "Acessibilidade nao esta no roadmap."

**Argumento:**
- Compliance e roadmap (LBI Brasil + ADA USA + EAA UE)
- Acessibilidade e ROI: 1bn pessoas + lawsuits evitados
- Defaults acessivos = menos retrabalho futuro

**Acao:** AC (acceptance criteria) de toda story inclui WCAG 2.2 AA. Definition of Done inclui axe + screen reader smoke test.

### Audiencia 5: Juridico / Compliance / DPO

**Sintoma:** "Acessibilidade nao e nosso escopo."

**Argumento:**
- LBI 13.146/2015 Art. 63 e responsabilidade do controlador (mesmo conceito da LGPD)
- ACP (Acao Civil Publica) MPF + MPSP em alta
- TAC com obrigacao de fazer + multa diaria
- Reputacional: virar manchete

**Acao:** clausula contratual em vendor (agencia + dev outsourcing) exigindo WCAG AA + e-MAG 3.1. Audits anuais + relatorio de conformidade publicado (transparencia art. 63 §2 LBI).

### Frameworks Microsoft Inclusive Design

**3 Principios Microsoft:**
1. **Recognize Exclusion** — quem fica de fora?
2. **Solve for One, Extend to Many** — solucao para PCD melhora produto pra todos. Closed captions ajuda em ambiente barulhento.
3. **Learn from Diversity** — diversidade gera melhores ideias.

**Persona Spectrum:**
- Permanent: 1 brazo, surdo congenito, cego
- Temporary: braco quebrado, otite, conjuntivite
- Situational: novo pai (1 brazo segurando bebe), bartender no barulho, sol no celular

Solver para Permanent atende Temporary + Situational. **Curb-cut effect:** rampa para cadeirantes ajuda carrinho de bebe + entregador + idoso.

---

## Anti-Patterns 18

### AP1: Overlay Widgets como Solucao (accessiBe / UserWay)

Widgets injetam JS que tenta "consertar" acessibilidade no client. Problemas:
- Quebram screen readers (mais ruido, anuncios duplicados)
- Cortes ADA rejeitam como defesa (50+ casos 2023-2025)
- Settlement ADA contra sites usando accessiBe esta crescendo
- Custo $500-$5000/ano para falsa sensacao de seguranca

**Faca:** corrige no codigo. Sem atalho.

### AP2: `<div onclick>` em Vez de `<button>`

```html
<!-- RUIM -->
<div class="btn" onclick="submit()">Enviar</div>
<!-- BOM -->
<button onclick="submit()">Enviar</button>
```

Sem button: nao recebe Tab, nao tem Enter/Space, nao tem `role`, screen reader nao anuncia como botao. Falha 4.1.2 + 2.1.1.

### AP3: Alt Text Generico ("imagem", "foto")

```html
<!-- RUIM -->
<img src="ceo.jpg" alt="imagem" />
<!-- BOM -->
<img src="ceo.jpg" alt="Ana Silva, CEO da Frank Tech, sorrindo em escritorio." />
<!-- BOM (decorativa) -->
<img src="ornament.svg" alt="" role="presentation" />
```

### AP4: `placeholder` Como Unico Label

```html
<!-- RUIM -->
<input type="email" placeholder="Email" />
<!-- BOM -->
<label for="email">Email</label>
<input id="email" type="email" placeholder="exemplo@dominio.com" />
```

Placeholder some quando usuario digita, contraste tipicamente <4.5:1, screen reader nao le como label.

### AP5: `outline: none` Sem Substituto

```css
/* RUIM */
*:focus { outline: none; }
/* BOM */
*:focus-visible { outline: 3px solid #0066cc; outline-offset: 2px; }
```

### AP6: Heading Hierarchy Quebrada

```html
<!-- RUIM -->
<h1>Pagina</h1>
<h3>Secao</h3>  <!-- pulou h2 -->
<!-- BOM -->
<h1>Pagina</h1>
<h2>Secao</h2>
<h3>Subsecao</h3>
```

Headings sao indice para screen reader (atalho `H` em NVDA). Hierarquia quebrada = indice quebrado.

### AP7: Cor Como Unica Sinalizacao

```html
<!-- RUIM: vermelho indicando erro, sem texto -->
<input style="border-color:red" />
<!-- BOM -->
<input aria-invalid="true" aria-describedby="email-error" />
<span id="email-error" role="alert">Email invalido. Use formato exemplo@dominio.com.</span>
```

### AP8: Modal Sem Focus Trap + Esc

Usuario tabula e sai do modal sem perceber. Esc nao fecha. Falha 2.1.2 + 2.4.3.

### AP9: Carousel Auto-Play Sem Pausar

WCAG 2.2.2 (A): qualquer animacao auto > 5s deve ter pause/stop/hide. Carousel rodando infinito = falha.

### AP10: Captcha-Puzzle (Selecione semaforos)

WCAG 2.2 novo criterio 3.3.8 Accessible Authentication (AA): autenticacao nao pode exigir teste cognitivo. Captcha de imagem = falha. Use:
- reCAPTCHA v3 (invisivel, score-based)
- hCaptcha com "I am human" simples
- Email magic link
- Passkeys

### AP11: `aria-hidden="true"` em Elemento Focavel

```html
<!-- RUIM: usuario teclado tabula em link "invisivel" para screen reader -->
<a href="..." aria-hidden="true">Link</a>
```

### AP12: `<table>` Para Layout

`<table>` e SOMENTE para dados tabulares. Layout: use Flexbox/Grid. Screen reader le `<table>` anunciando "tabela com 3 linhas e 4 colunas" — confunde.

### AP13: Link Generico ("Clique Aqui", "Leia Mais")

Screen reader tem comando "lista todos os links" — vira "leia mais, leia mais, leia mais". Use texto descritivo: "Leia mais sobre LBI no blog Frank".

### AP14: `aria-label` em Elemento com Texto Visivel

WCAG 2.5.3 Label in Name: nome acessivel deve conter texto visivel. Mismatch = usuario voice control diz "Comprar" mas comando registrado e "Adicionar ao carrinho".

### AP15: SVG Decorativo Sem `aria-hidden`

```html
<!-- RUIM: screen reader anuncia "graphic" inutil -->
<svg>...</svg>
<!-- BOM -->
<svg aria-hidden="true" focusable="false">...</svg>
```

### AP16: Form Sem `<label>` Associado

```html
<!-- RUIM -->
<input type="text" />
<!-- BOM (label visivel) -->
<label for="cpf">CPF</label>
<input id="cpf" type="text" />
<!-- BOM (label invisivel) -->
<input type="text" aria-label="Buscar produtos" />
```

### AP17: Auto-Submit em Form em Mudanca de Campo

WCAG 3.2.2 On Input: mudanca em campo de form NAO pode causar mudanca de contexto (submit, redirect) sem warning.

### AP18: Scroll Hijacking + Animacoes Forcadas

Sites que sequestram scroll (`scroll-snap`, parallax forcado) quebram leitores de tela + usuarios com vestibular disorder. WCAG 2.3.3 Animation from Interactions (AAA): respeite `prefers-reduced-motion`.

```css
@media (prefers-reduced-motion: reduce) {
  * { animation-duration: 0.01ms !important; transition: none !important; }
}
```

---

## 18 Regras de Ouro

1. **HTML semantico antes de ARIA.** `<button>`, `<nav>`, `<main>`, `<h1>` resolvem 80% dos casos sem tocar em ARIA.
2. **Toda imagem informativa precisa de `alt` descritivo.** Decorativa: `alt=""`. Logo: `alt="Frank-MKT, logo"`.
3. **Toda input precisa de `<label>` associado** (`for`/`id`) ou `aria-label` quando label visivel impossivel.
4. **Contraste minimo 4,5:1 (texto normal AA), 3:1 (texto grande AA), 7:1 (AAA).** UI components 3:1.
5. **Tab order logico, sem `tabindex` positivo.** `tabindex="0"` ou `"-1"` apenas.
6. **Focus visible em todos os elementos focaveis** (`:focus-visible` com outline >= 2px + contraste 3:1).
7. **Skip link como primeiro elemento focavel** ("Pular para conteudo principal").
8. **Modal: focus trap + Esc fecha + retorna foco + `aria-modal="true"`.**
9. **Live region (`aria-live` ou `role="alert"/"status"`) para notificacoes dinamicas.**
10. **NUNCA cor como unica sinalizacao** — sempre + texto/icone/padrao.
11. **Heading hierarchy: 1 `<h1>` por pagina, sem pular niveis.**
12. **Link text descritivo** — nao "clique aqui", nao "saiba mais".
13. **Respeite `prefers-reduced-motion`** + `prefers-color-scheme` + `prefers-contrast`.
14. **Form errors: `aria-invalid="true"` + `aria-describedby` apontando para mensagem com `role="alert"`.**
15. **WCAG 2.2 alvo minimo 24x24 CSS pixels** para clicaveis (excecao: inline link em paragrafo).
16. **Teste com NVDA + Firefox (Windows) + VoiceOver + Safari (macOS) + TalkBack + Chrome (Android) minimo.**
17. **CI/CD: jest-axe ou cypress-axe falhando em critical + serious.**
18. **Auditorias trimestrais + uma vez por trimestre teste com PCD real** (Fable, Applause, MWPT no Brasil).

---

## Exemplos Comportamentais

### Exemplo 1 — Founder de E-commerce SaaS Pre-IPO

**Contexto:** SaaS B2C brasileiro, $5MM ARR, planeja IPO B3. Auditoria pre-IPO levantou ZERO conformidade WCAG. Founder pergunta: "isso e blocker?"

**Como esta skill orienta:**
- LBI 13.146/2015 Art. 63 + Decreto 9.296/2018: **obrigatorio para todas empresas com sede no Brasil**, sem excecao por porte.
- Pre-IPO: due diligence compradores institucionais inclui ESG. Acessibilidade e pilar S (Social).
- Lawsuit risk: empresa de capital aberto e alvo. Brasil 2026: MPF + MPSP movendo ACPs. USA: se empresa atende clientes USA, ADA Title III aplica.
- Roadmap: 90 dias para WCAG AA basico (axe DevTools tier 1: contraste, alt text, form labels, focus). Audit terceirizada para validacao. Selo voluntario de conformidade publicado.
- Cross-skill: `dominio-juridico-mkt` para clausulas vendor + LGPD-LBI interseccao.

### Exemplo 2 — Dev Tech Lead Backend que "Nao Sabe Frontend"

**Contexto:** tech lead Python, time pequeno, frontend React. PR review pega `<div onclick>` em todo lugar. Junior dev pergunta: "tem alguma regra clara para isso?"

**Como esta skill orienta:**
- WCAG 2.1.1 Keyboard (Level A) + 4.1.2 Name Role Value (Level A): elementos interativos DEVEM ser nativos ou ter ARIA + keyboard handlers.
- 5 regras ARIA: regra 1 e "use HTML nativo se possivel". `<button>` e default.
- Checklist PR review:
  1. Todo `onClick` em `<button>` ou `<a>` (nao `<div>`)?
  2. Toda imagem com `alt`?
  3. Todo input com `<label>` ou `aria-label`?
  4. `outline:none` proibido sem `:focus-visible` substituto?
- CI integration: jest-axe em todo componente. cypress-axe em fluxos criticos. Falhar build em critical + serious.
- Cross-skill: `frank-dev:javascript-typescript` para hooks acessiveis.

### Exemplo 3 — Designer Senior em Agencia, Cliente Healthcare

**Contexto:** designer trabalhando em portal de telemedicina para hospital. Cliente pediu "look moderno" com cinza claro sobre branco para "elegancia". Designer pergunta: "isso passa?"

**Como esta skill orienta:**
- Healthcare = audiencia idosa (catarata, glaucoma, baixa visao) + visualmente debilitada. Aplique AAA quando possivel.
- Cinza `#cccccc` sobre branco `#ffffff` = contraste 1.6:1. **FALHA tudo** (AA exige 4.5:1).
- Stark plugin Figma: liga e mostra contraste em tempo real. Mude para `#595959` (contraste 7:1 = AAA).
- Healthcare bonus: prefers-contrast media query, dark mode, font-size 18px+ default.
- WCAG 2.5.5 Target Size 24x24 (2.2 AA) + 2.5.8 (AAA 44x44): botoes touch grandes.
- Cross-skill: `dominio-saude-mkt` para regulacao ANVISA + CFM telemedicina.

### Exemplo 4 — PM de Produto Edtech B2B, Procurement Enterprise

**Contexto:** PM de plataforma edtech B2B, prospect e universidade publica federal. Procurement enviou checklist com 47 items, **30 sao acessibilidade**. PM pergunta: "como respondo?"

**Como esta skill orienta:**
- Universidade federal = orgao publico federal = **Decreto 9.296/2018 + e-MAG 3.1 obrigatorios**.
- Padrao tecnico: **WCAG 2.0/2.1 AA** (e-MAG 3.1 alinhado).
- Validador oficial: **ASES** (governo). Rode ASES, anexe relatorio.
- Documente VPAT (Voluntary Product Accessibility Template) — declaracao formal de conformidade. Modelo ITI: https://www.itic.org/policy/accessibility/vpat
- Roadmap publico de acessibilidade + acessibilidade contact email + politica formal.
- Selo Acessibilidade Web (em consolidacao 2026) sera diferencial.
- Cross-skill: `dominio-juridico-mkt` para contrato com clausula compliance + auditoria anual.

---

## Checklist Contraditorio Interno (10 perguntas)

Antes de lancar produto/feature/landing, responda:

1. **Testei com pelo menos 2 screen readers** (NVDA + VoiceOver minimo)?
2. **Naveguei a feature inteira so com teclado** (sem mouse)? Tab + Shift+Tab + Enter + Esc + Arrow keys cobrem tudo?
3. **Todos contrastes >= 4,5:1** (texto normal) e **3:1** (UI components)? Validei com axe DevTools ou WebAIM?
4. **Todas imagens informativas tem `alt` descritivo** e decorativas tem `alt=""`?
5. **Todos inputs tem `<label>` associado** ou `aria-label` quando impossivel?
6. **Heading hierarchy esta correta** — 1 `<h1>`, sem pular niveis?
7. **Modal/dialog tem focus trap, Esc fecha, foco retorna ao trigger, `aria-modal="true"`?**
8. **Animacoes respeitam `prefers-reduced-motion`** + nao tem flash >3 vezes/segundo?
9. **CI/CD esta rodando jest-axe ou cypress-axe** com falha em critical + serious?
10. **Plano de testes manuais com PCD reais** existe (proximo trimestre)?

Se voce respondeu **NAO** a 3+ perguntas, pare e remediar antes de lancar.

---

## Referencias

### W3C / WAI / WCAG (oficial)

- [WCAG 2.2 — W3C Recommendation 2023-10-05](https://www.w3.org/TR/WCAG22/)
- [WCAG 2 Overview — Web Accessibility Initiative](https://www.w3.org/WAI/standards-guidelines/wcag/)
- [Requirements for WCAG 2.2](https://w3c.github.io/wcag/requirements/22/)
- [WCAG 2 Level A Conformance](https://www.w3.org/WAI/WCAG2A-Conformance)
- [WCAG 2 Level AA Conformance](https://www.w3.org/WAI/WCAG2AA-Conformance)
- [WCAG 2 Level AAA Conformance](https://www.w3.org/WAI/WCAG2AAA-Conformance)
- [Understanding SC 1.4.3 Contrast Minimum](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html)
- [Understanding SC 1.4.6 Contrast Enhanced](https://www.w3.org/WAI/WCAG21/Understanding/contrast-enhanced.html)
- [Techniques G18 — Contrast 4.5:1](https://www.w3.org/TR/WCAG20-TECHS/G18.html)
- [WAI-ARIA 1.2 Specification](https://www.w3.org/TR/wai-aria-1.2/)
- [ARIA Authoring Practices Guide (APG)](https://www.w3.org/WAI/ARIA/apg/)

### USA: ADA + Section 508

- [ADA.gov — Web Rule (DOJ, Title II)](https://www.ada.gov/resources/2024-03-08-web-rule/)
- [ADA Title III Blog — Seyfarth Shaw](https://www.adatitleiii.com/)
- [DOJ Extends ADA Title II Deadlines (2026-04)](https://www.adatitleiii.com/2026/04/doj-extends-ada-title-ii-website-accessibility-deadlines-for-governmental-entities-but-litigation-and-compliance-risks-remain/)
- [Federal Court Lawsuit Filings 2025 Bounce Back](https://www.adatitleiii.com/2026/03/federal-court-website-accessibility-lawsuit-filings-bounce-back-in-2025/)
- [Section 508 — Section508.gov](https://www.section508.gov/)
- [Section 508 ICT Refresh 2018](https://www.access-board.gov/ict/)
- [American Bar Association — Digital Accessibility Title III 2025](https://www.americanbar.org/groups/business_law/resources/business-law-today/2025-august/digital-accessibility-under-title-iii-ada/)
- [TestParty — Guide to ADA Lawsuits 2026](https://testparty.ai/blog/the-2026-guide-to-ada-website-lawsuits-what-to-do-when-you-get-sued-and-why-your)
- [Saul Ewing — ADA Website Risk](https://www.saul.com/insights/blog/ada-website-accessibility-risk)
- [Inclusive Web — Protect Your Business 2026](https://www.inclusiveweb.co/accessibility-resources/how-to-protect-your-business-from-ada-website-lawsuits-in-2026)

### Brasil: LBI + Decreto + e-MAG

- [Lei 13.146/2015 — Planalto](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13146.htm)
- [Decreto 9.296/2018 — Planalto](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/decreto/d9296.htm)
- [Decreto 5.296/2004 — Planalto](https://www.planalto.gov.br/ccivil_03/_ato2004-2006/2004/decreto/d5296.htm)
- [Lei 10.098/2000 — Planalto](https://www.planalto.gov.br/ccivil_03/leis/l10098.htm)
- [e-MAG Modelo de Acessibilidade](https://emag.governoeletronico.gov.br/)
- [ASES — Avaliador Acessibilidade Governo](https://asesweb.governoeletronico.gov.br/)
- [Movimento Web Para Todos](https://mwpt.com.br/)
- [Acessibilidade Brasil](http://www.acessibilidade.org.br/)
- [Mais Diferencas](https://maisdiferencas.org.br/)
- [EqualWeb Brasil — LBI Guia 2026](https://equalweb.com.br/o-guia-definitivo-da-acessibilidade-digital-pela-lbi-lei-brasileira-de-inclusao-para-2026/)
- [PNAD IBGE 2022 — Pessoas com Deficiencia](https://www.ibge.gov.br/estatisticas/sociais/saude/9171-pessoas-com-deficiencia.html)
- [Convencao ONU CDPD (Decreto 6.949/2009)](https://www.planalto.gov.br/ccivil_03/_ato2007-2010/2009/decreto/d6949.htm)

### Uniao Europeia + Internacional

- [European Accessibility Act (EAA Diretiva 2019/882)](https://eur-lex.europa.eu/eli/dir/2019/882/oj)
- [EN 301 549 v3.2.1](https://www.etsi.org/deliver/etsi_en/301500_301599/301549/03.02.01_60/en_301549v030201p.pdf)
- [AODA (Ontario Canada)](https://www.aoda.ca/)
- [Accessible Canada Act](https://laws-lois.justice.gc.ca/eng/acts/A-0.6/)

### Screen Readers + ARIA

- [NVDA — NV Access (gratuito)](https://www.nvaccess.org/)
- [JAWS — Freedom Scientific](https://www.freedomscientific.com/products/software/jaws/)
- [VoiceOver — Apple](https://www.apple.com/accessibility/vision/)
- [TalkBack — Google](https://support.google.com/accessibility/android/answer/6283677)
- [WebAIM Screen Reader Survey #10](https://webaim.org/projects/screenreadersurvey10/)
- [ARIA Authoring Practices Patterns](https://www.w3.org/WAI/ARIA/apg/patterns/)

### Tools

- [axe DevTools — Deque](https://www.deque.com/axe/)
- [axe-core open-source GitHub](https://github.com/dequelabs/axe-core)
- [WAVE — WebAIM](https://wave.webaim.org/)
- [Lighthouse — Chrome Developers](https://developer.chrome.com/docs/lighthouse/accessibility/)
- [Pa11y CLI](https://pa11y.org/)
- [Accessibility Insights — Microsoft](https://accessibilityinsights.io/)
- [Stark — Figma + Browser](https://www.getstark.co/)
- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
- [WebAIM Million 2024](https://webaim.org/projects/million/)

### Inclusive Design + Frameworks

- [Microsoft Inclusive Design](https://inclusive.microsoft.design/)
- [Microsoft Inclusive Design Toolkit](https://inclusive.microsoft.design/tools-and-activities/Inclusive101Guidebook.pdf)
- [Deque — axe-con 2026](https://www.deque.com/axe-con/)
- [Deque + Microsoft Partnership](https://www.deque.com/blog/deque-axe-and-microsoft/)
- [Inclusive Design Principles](https://inclusivedesignprinciples.org/)

### MDN + Recursos Educacionais

- [MDN — Color Contrast](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Understanding_WCAG/Perceivable/Color_contrast)
- [MDN — Accessibility](https://developer.mozilla.org/en-US/docs/Web/Accessibility)
- [WebAIM Contrast and Color](https://webaim.org/articles/contrast/)
- [A11Y Project](https://www.a11yproject.com/)
- [Smashing Magazine Accessibility Tag](https://www.smashingmagazine.com/category/accessibility/)

### VPAT / Procurement

- [ITI VPAT Template](https://www.itic.org/policy/accessibility/vpat)
- [Section 508 Buy Accessible Wizard](https://www.section508.gov/buy/)

### Testing com PCD

- [Fable Tech Labs (testers PCD)](https://makeitfable.com/)
- [Applause (com filtro PCD)](https://www.applause.com/)

### CI/CD Integration

- [jest-axe — GitHub](https://github.com/nickcolley/jest-axe)
- [@axe-core/playwright](https://www.npmjs.com/package/@axe-core/playwright)
- [cypress-axe](https://github.com/component-driven/cypress-axe)
- [Pa11y CI Action](https://github.com/pa11y/pa11y-ci)

---

## Cross-Skill References

- **`ux-heuristicas`** — Nielsen 10 heuristicas + WCAG: visibility of system status (3.2.1) + match real world (3.1.5) + error prevention (3.3.4).
- **`microcopy`** — link text descritivo, error messages acessiveis, instructions claras (WCAG 3.3.2 + 3.3.3).
- **`design-system-basico`** — design tokens com contraste 4.5:1 default + componentes acessiveis (Radix UI, Headless UI, Material Design A11y).
- **`branding`** — paletas com dual-tone (primary + on-primary) garantindo contraste em todos estados.
- **`posicionamento-marca`** — diferencial competitivo "acessibilidade by default" para concorrentes que ignoram.
- **`dominio-juridico-mkt`** — interseccao LBI 13.146/2015 + LGPD 13.709/2018 + clausulas vendor + ACP MPF.
- **`dominio-saude-mkt`** — healthcare exige AAA quando possivel + ANVISA + CFM telemedicina.
- **`frank-dev:javascript-typescript`** — hooks React acessiveis + Radix + Headless UI.
- **`frank-dev:html-css`** — semantica HTML5 + landmarks + form patterns.
- **`frank-dev:tailwind-css`** — Tailwind + headlessui + tokens contraste.
- **`frank-dev:react-native`** + **`frank-dev:dart-flutter`** — accessibility props mobile + VoiceOver + TalkBack mobile.

---

## Integracao Ecossistema Frank-MKT

**Posicionamento no Bloco UX/UI:**
- 1a SKILL: `ux-heuristicas` (Nielsen + foundations)
- 2a SKILL: `microcopy` (writing UX)
- 3a SKILL: **`acessibilidade-wcag`** (esta skill — WCAG + LBI + ARIA)
- 4a SKILL (futura): `design-system-basico`
- 5a SKILL (futura): `mobile-first-design`

**Sinergia com outros blocos:**
- **Bloco Juridico:** LBI cross-reference + clausulas vendor + auditoria.
- **Bloco Branding:** paletas acessiveis + dual-tone + design tokens.
- **Bloco Performance:** semantica HTML melhora SEO (alt text + headings).
- **Bloco Conversion:** sites acessiveis convertem MAIS (form labels claras + error handling + contraste = menos friction).

**Cobertura Frank-MKT:**
Esta skill expande cobertura legal-juridica do Frank-MKT alem da LGPD/CDC para LBI/ADA/EAA, criando passaporte para procurements enterprise + governo + healthcare + edtech + fintech.

---

## Disclaimer Educacional

Esta skill e **educacional**. Acessibilidade web envolve interseccao tecnica (WCAG / ARIA) + juridica (LBI Brasil / ADA USA / EAA UE) + organizacional (compliance / DPO / juridico).

**ATENCAO:**
- Para aconselhamento juridico especifico (contratos B2B, ACP MPF/MPSP, TAC, clausulas vendor, processos administrativos), consulte advogado(a) especializado em Direito Digital + Acessibilidade. Esta skill **NAO substitui consultoria juridica**.
- Para auditoria formal de conformidade (validacao em corte, due diligence pre-IPO, certificacao), contrate auditor(a) especializado(a) (Deque, Level Access, equivalentes Brasil).
- Estatisticas e datas citadas sao referencias publicas em **2026-05-09** e podem ter mudado. Sempre validar com fonte primaria.
- URLs sao referencias publicas; a skill nao garante disponibilidade futura.
- Conformidade WCAG **nao garante** imunidade a lawsuits. E primeira linha de defesa, nao escudo absoluto.

**Decaimento desta skill:** medium. Re-review obrigatorio em 2026-11-09 OU mediante triggers listados em "Decaimento Temporal".

---

*FIM SKILL acessibilidade-wcag — 3a SKILL Bloco UX/UI Frank-MKT*
