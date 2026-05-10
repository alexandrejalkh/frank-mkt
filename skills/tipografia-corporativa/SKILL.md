---
name: tipografia-corporativa
description: Tipografia Corporativa 2026 (escolha tipográfica + hierarquia display/heading/body/caption + licenciamento Google Fonts/Adobe Fonts/MyFonts/Type Foundries + variable fonts 2026 OpenType variations + fallbacks web + acessibilidade leitura + cases Apple Pro Display/IBM Plex/Stripe Sohne/Spotify Circular custom fonts) para brand designers/devs frontend/CMO/CCO/agências, integração brand-book-methodology + design-system-basico + acessibilidade-wcag. 4ª SKILL Bloco Identidade Visual Corporativa / Brand Design.
volatility: medium
last_review: 2026-05-09
next_review: 2026-11-09
languages: [pt-BR]
audience: [brand-designers, devs-frontend, CMO, CCO, agencias, type-designers]
ascii_only: true
---

# Skill: tipografia-corporativa

Skill Frank-MKT dedicada a **Tipografia Corporativa 2026** — escolha tipografica estrategica, hierarquia display/heading/body/caption, licenciamento (Google Fonts, Adobe Fonts, MyFonts, type foundries independentes, custom enterprise), variable fonts (OpenType Font Variations), implementacao web (WOFF2, fallbacks, FOUT/FOIT, font-display, subset, preload), acessibilidade (WCAG 2.2, contraste, line-height, tamanho minimo), cases brasileiros (Magalu, Nubank, Itau, Stone, O Boticario), cases globais (Apple SF Pro, IBM Plex, Stripe Sohne, Spotify Circular, Mailchimp Cooper Light, Slack Lato/Hack, Airbnb Cereal, Netflix Sans).

Esta e a **4a skill** do Bloco "Identidade Visual Corporativa / Brand Design", complementando logo-design-process, brand-book-methodology e paleta-cores-corporativa. Tipografia e o segundo elemento mais reconhecivel de uma marca, depois da cor (Sciencedirect/Pantone, varios estudos 2020-2025) — uma escolha tipografica errada destrói percepcao de qualidade independentemente da qualidade do logo.

## Decaimento Temporal

- **Volatilidade**: Media (medium).
- **last_review**: 2026-05-09.
- **next_review**: 2026-11-09 (6 meses).
- **Sinais de obsolescencia**:
  - Variable fonts ganham novos eixos padronizados (GRAD, opsz, MONO).
  - Google Fonts API v3+ muda contratos de subset/preload.
  - Mudancas em EULAs (clausulas anti-AI training virando padrao 2026+).
  - WCAG 3.0 (substituindo 2.2) entra em status W3C Recommendation.
  - Nova fonte custom de big tech (ex: OpenAI, Anthropic) lancada como referencia.
  - Browser support para `font-variation-settings` muda.
- **Quando atualizar**:
  - Big tech anuncia novo custom font corporativo.
  - Mudancas em politicas de licenciamento Adobe Fonts / Monotype.
  - Performance budgets web mudam (Core Web Vitals 2027+).
  - Novas pesquisas WCAG sobre fontes acessiveis para dislexicos.

## Visao Geral

**Por que tipografia corporativa importa**:

- **Reconhecimento de marca**: Tipografia carrega 30-40% da identidade visual depois da cor (Sciencedirect / "The role of typeface in brand perception", 2018).
- **Trust signal**: Fonte adequada aumenta percepcao de credibilidade (estudo Sasson 2008 — fontes mal escolhidas reduzem confianca em ate 30%).
- **Diferenciacao**: Custom fonts (Sohne, Circular, SF Pro, Plex) tornaram-se moat competitivo das big techs 2020-2026.
- **Performance web**: Fonte mal otimizada custa 200-500ms LCP (Largest Contentful Paint) — degrada Core Web Vitals.
- **Acessibilidade**: 5-10% da populacao tem dislexia (IDA — International Dyslexia Association); fontes mal escolhidas excluem usuarios.

**O que esta skill cobre**:

- 8 fundacoes (Type Foundations / Hierarquia / Variable Fonts / Licenciamento / Web Implementation / Brasil / Mensuracao / Aplicacao Content MKT).
- 18 anti-patterns + 18 regras de ouro.
- 4 personas (CMO startup, brand designer agencia, dev frontend, CCO enterprise).
- 50-70 referencias hyperlinks.

**O que esta skill NAO cobre**:

- Type design tecnico (criar fonte do zero — vide Glyphs/FontForge/Fontlab).
- Calligraphy / lettering manual (skill especifica futura).
- Tipografia editorial impressa (livros, jornais — skill editorial futura).

## Fundacao 1 — Type Foundations (Serif + Sans-serif + Display + Mono + Hierarchy)

### 1.1 Anatomia tipografica basica

Termos essenciais que todo brand designer + dev frontend deve dominar:

- **x-height**: Altura das letras minusculas (sem ascendentes/descendentes). Fontes com x-height alto (Inter, Roboto) sao mais legiveis em pequenos tamanhos.
- **Ascender / Descender**: Parte que sobe acima do x-height (b, d, h, k, l, t) / parte que desce abaixo da baseline (g, j, p, q, y).
- **Counter**: Espaco interno fechado (o, p, b, d).
- **Bowl**: Curva fechada (b, p, d).
- **Aperture**: Abertura entre counter e exterior (c, e, s) — apertures abertos = melhor legibilidade (Inter, Source Sans Pro).
- **Stroke contrast**: Diferenca entre traco fino e grosso (alto = serifas didone tipo Bodoni; baixo = grotesks tipo Helvetica).
- **Optical size (opsz)**: Variante otimizada para tamanho — texto em 8pt deve ser desenhado diferente de display 96pt.
- **Stroke terminal**: Como o traco termina (corte reto, gota, esfera).
- **Tracking / Letterspacing**: Espaco horizontal entre letras (CSS `letter-spacing`).
- **Kerning**: Ajuste de espaco entre pares especificos (AV, To, We). Browser usa kerning OpenType automaticamente se `font-feature-settings: "kern" 1` ou `font-kerning: normal`.
- **Leading / Line-height**: Espaco vertical entre baselines (CSS `line-height`).

### 1.2 Classificacao tipografica (5 grandes familias)

**Serif**:

- Caracteristica: Tem serifas (extremidades nos terminais).
- Subtipos:
  - **Old style / Humanist** (Garamond, Caslon, Sabon): organico, baixo contraste, eixo inclinado. Trust academico/editorial.
  - **Transitional** (Times New Roman, Baskerville, Mrs Eaves): contraste medio. Default seguro/conservador.
  - **Didone / Modern** (Bodoni, Didot, Playfair Display): alto contraste, eixo vertical. Luxo / fashion / editorial.
  - **Slab serif** (Rockwell, Roboto Slab, Arvo): serifas retangulares grossas. Tech retro / friendly.
- **Quando usar**: editorial, luxo, juridico, financeiro tradicional, livros, jornais, tese academica, marcas premium.

**Sans-serif**:

- Caracteristica: Sem serifas.
- Subtipos:
  - **Grotesque / Neo-grotesque** (Helvetica, Akzidenz Grotesk, Inter): minimalista, geometrico-organico, neutro. Default tech/corporate moderno.
  - **Geometric** (Futura, Avenir, Circular, Gotham): formas circulares puras, geometricas. Tech futurista, fashion moderno.
  - **Humanist** (Frutiger, Open Sans, Source Sans Pro, Noto Sans): proporcoes humanas (baseado em manuscrito), maior legibilidade UI. Default UI/web.
  - **Neo-humanist 2020s** (Inter, Sohne, Roobert, Aktiv Grotesk): hibrido humanist+grotesk, otimizado tela. Padrao 2020-2026 SaaS / fintech.
- **Quando usar**: UI, tech, SaaS, fintech, app mobile, e-commerce, default web 2020+.

**Display**:

- Caracteristica: Desenhada para tamanhos grandes (>24pt), nao funciona em body text.
- Exemplos: Bebas Neue, Playfair Display, Oswald, Anton, Abril Fatface.
- **Quando usar**: titulos hero, capas, posters, pacote, branding pesado. NUNCA body.

**Monospace (Mono)**:

- Caracteristica: Cada caractere ocupa mesma largura.
- Exemplos: IBM Plex Mono, JetBrains Mono, Fira Code, Roboto Mono, Source Code Pro, Cascadia Code, SF Mono, Operator Mono, Monaspace (GitHub 2023).
- **Quando usar**: codigo, tabelas numericas, dev tools, terminal, dados tecnicos.

**Script / Handwritten**:

- Caracteristica: Imita escrita manual / cursiva.
- Exemplos: Lobster, Pacifico, Dancing Script, Caveat, Sacramento.
- **Quando usar**: branding feminino/casual/artesanal, signature, eventos, casamento. Cuidado: pessima legibilidade — use APENAS em titulos curtos.

### 1.3 Quando escolher serif vs sans-serif (heuristica)

| Atributo | Serif | Sans-serif |
|----------|-------|------------|
| Tradicao / heritage | Forte | Fraca |
| Modernidade / tech | Fraca | Forte |
| Legibilidade impresso longo | Alta | Media |
| Legibilidade tela (UI) | Media (Inter Tight, IBM Plex Serif okay) | Alta |
| Trust / credibilidade | Alta (juridico, banco, editorial) | Media-alta (tech, fintech moderno) |
| Inovacao / startup | Baixa | Alta |
| Luxo (didone) | Muito alta | Media |
| Friendly / casual | Media (slab) | Alta (humanist) |

**Regra pratica 2026**: 70-80% das marcas modernas usam sans-serif primaria + serif secundaria (ou vice-versa). Sans-serif puro e ainda dominante em SaaS / fintech / mobile.

### 1.4 Pairing tipografico (combinacoes que funcionam)

**Combinacoes seguras** (testadas em centenas de brand-books):

- **Sans + Serif**: Inter + Lora / Roboto + Merriweather / Montserrat + Playfair Display.
- **Serif + Sans**: Playfair Display (heading) + Source Sans Pro (body) — classico editorial.
- **Sans + Sans (mesma familia)**: Roboto + Roboto Slab / IBM Plex Sans + IBM Plex Mono / Inter + Inter Tight.
- **Display + Body neutro**: Bebas Neue (heading hero) + Inter (body) — branding pesado.
- **Mono + Sans**: JetBrains Mono (codigo/labels) + Inter (UI body) — dev tools, GitHub-style.

**Anti-pairings** (evitar):

- Dois serifs muito similares (Times + Georgia) — confusao visual.
- Dois sans-serifs neutros (Helvetica + Arial) — sem contraste hierarquico.
- Display + Display — caos visual.
- Comic Sans + qualquer coisa.
- Papyrus + qualquer coisa em contexto corporativo.

### 1.5 Numero de fontes em um sistema

- **Minimo**: 1 (mesma familia em multiplas pesos — Inter Light/Regular/Medium/Bold).
- **Padrao**: 2 (heading + body — IBM Plex Sans heading + IBM Plex Serif body).
- **Maximo recomendado**: 3 (display + body + mono — Sohne Display + Sohne Body + Sohne Mono).
- **Acima de 3 fontes**: caos. Excecao: brands editoriais com sistema rico (jornais).

## Fundacao 2 — Hierarquia (Display + Heading + Body + Caption + Scale Modular)

### 2.1 Niveis hierarquicos canonicos

Sistema padronizado tipico (HTML semantic + design system):

| Nivel | Uso | Tamanho desktop tipico | Weight tipico | Exemplo |
|-------|-----|------------------------|---------------|---------|
| Display | Hero / capa | 64-128px | 700-900 | "Banking for everyone" (Stripe hero) |
| H1 | Titulo principal pagina | 40-56px | 600-700 | "Pricing" |
| H2 | Secao | 32-40px | 600-700 | "Standard plans" |
| H3 | Subsecao | 24-32px | 600 | "Enterprise" |
| H4 | Sub-subsecao | 20-24px | 500-600 | "FAQ" |
| H5 | Detalhe | 18-20px | 500 | "How it works" |
| Subtitle | Acompanha heading | 18-24px | 400 | "Powerful APIs..." |
| Body large | Paragrafo destaque | 18-20px | 400 | "Lead intro..." |
| Body | Paragrafo normal | 16px | 400 | Texto corrido |
| Body small | Secundario | 14px | 400 | Notas, footnotes |
| Caption | Legenda imagem | 12-14px | 400-500 | "Fig. 1: ..." |
| Overline | Label seccao | 12px UPPERCASE | 600-700 | "FEATURES" |
| Button | CTA | 14-16px | 500-600 | "Get started" |
| Code | Inline / block | 14-16px (mono) | 400 | `const x = 1;` |

### 2.2 Type scale modular (escala matematica)

**Razoes mais usadas**:

- 1.067 (minor second) — muito sutil, nao recomendado.
- 1.125 (major second) — sutil, bom para UI densas.
- 1.200 (minor third) — equilibrado, **default Tailwind**.
- 1.250 (major third) — bom para landing pages.
- 1.333 (perfect fourth) — dramatico, branding pesado.
- 1.500 (perfect fifth) — muito dramatico.
- 1.618 (golden ratio) — classico editorial.

**Exemplo escala 1.250 base 16px**:

- 16 -> 20 -> 25 -> 31 -> 39 -> 49 -> 61 -> 76 -> 95 (px).

**Ferramentas geradoras**:

- type-scale.com (Spencer Mortensen) — gera CSS direto.
- modularscale.com (Tim Brown / Scott Kellum) — visual.
- utopia.fyi (Andy Bell + James Gilyead) — fluid type scale com clamp().

### 2.3 Fluid typography (responsividade)

CSS moderno usa `clamp()` para escalar fontes entre min/max baseado no viewport:

```css
h1 { font-size: clamp(2rem, 4vw + 1rem, 4.5rem); }
body { font-size: clamp(1rem, 0.95rem + 0.25vw, 1.125rem); }
```

Vantagens: sem media queries, escala suave, melhor em mobile/desktop ao mesmo tempo. Ferramenta: utopia.fyi gera tudo automatico.

### 2.4 Line-height (leading)

- **Display / hero (>40px)**: 1.0-1.1 (compacto, dramatico).
- **Headings (24-40px)**: 1.1-1.3.
- **Body (14-18px)**: 1.5-1.65 (default web; WCAG recomenda >=1.5).
- **Captions (12-14px)**: 1.4-1.5.
- **Code mono**: 1.5-1.6.

### 2.5 Letter-spacing (tracking)

- **All-caps headings**: +50 a +100 unidades (CSS `letter-spacing: 0.05em` a `0.1em`).
- **Body normal**: 0 (default).
- **Display grande (>64px)**: -1 a -2% (negativo para compactar — tight).
- **Buttons CTA**: 0 a +0.5%.

### 2.6 Paragraph length (medida)

- **Ideal**: 50-75 caracteres por linha (incluindo espacos) — WCAG/legibilidade.
- **Maximo**: 90 caracteres.
- CSS: `max-width: 65ch` (unidade ch = largura char "0").

## Fundacao 3 — Variable Fonts 2026 (OpenType variations + axes weight/width/slant/optical)

### 3.1 O que sao variable fonts

**Variable Fonts** = especificacao OpenType 1.8 (lancada Set/2016 por Adobe, Apple, Google, Microsoft) que permite empacotar multiplas variacoes de uma fonte (peso, largura, slant, optical size) em um unico arquivo binario.

**Vantagens 2026**:

- 1 arquivo no lugar de 8-12 arquivos estaticos = menos requisicoes HTTP, menor bundle.
- Animacoes suaves entre variacoes (CSS transitions em `font-variation-settings`).
- Granularidade infinita (nao apenas Light/Regular/Bold; tambem 432, 467, 580...).
- Reducao bandwidth: tipicamente 40-60% economia vs static fonts.
- Carbon footprint menor (menos bytes transferidos).

### 3.2 Eixos OpenType Variations padrao (5 registered axes)

| Eixo | Tag | Range tipico | Significado |
|------|-----|--------------|-------------|
| Weight | `wght` | 100-900 | Peso (Thin -> Black) |
| Width | `wdth` | 50-200 | Largura (Condensed -> Expanded) |
| Slant | `slnt` | -15 a 0 | Inclinacao oblique (graus) |
| Italic | `ital` | 0 ou 1 | Italico verdadeiro (binary) |
| Optical Size | `opsz` | 6-144 | Otimizacao por tamanho (texto vs display) |

### 3.3 Eixos custom ("custom axes")

Type designers podem criar eixos proprios. Exemplos populares:

- **GRAD** (Grade): peso sem mudar avanco horizontal — preserva layout em hover/focus. Roboto Flex tem GRAD 25 a 200. **Tendencia 2026**: GRAD virando padrao em UI fonts.
- **MONO**: transicao proporcional -> monospaced (Recursive).
- **CASL** (Casual): formal -> casual (Recursive).
- **CRSV** (Cursive): non-cursive -> cursive (Recursive).
- **YOPQ** (Y opaque): contraste das hastes (Roboto Flex).
- **XTRA** (X transparent): ajuste fino contracounter horizontal (Roboto Flex).

### 3.4 CSS para variable fonts

```css
@font-face {
  font-family: 'Inter';
  src: url('/fonts/Inter.var.woff2') format('woff2-variations');
  font-weight: 100 900;
  font-style: normal;
  font-display: swap;
}

.heading {
  font-family: 'Inter';
  font-weight: 650; /* qualquer valor entre 100-900 */
  font-variation-settings: 'wght' 650, 'opsz' 32;
}

.heading-grad-hover:hover {
  /* Grade aumenta sem layout shift */
  font-variation-settings: 'wght' 650, 'GRAD' 100;
  transition: font-variation-settings 0.15s ease;
}
```

### 3.5 Variable fonts essenciais 2026

**Open source / Google Fonts**:

- **Inter** (Rasmus Andersson) — UI default. wght variavel.
- **Inter Tight** — versao mais compacta, headings.
- **Roboto Flex** (Font Bureau / Google) — 13 eixos (incluindo GRAD, opsz, XTRA, YOPQ).
- **Recursive** (Stephen Nixon / Arrow Type) — 5 eixos (wght, slnt, MONO, CASL, CRSV).
- **Source Sans 3 Variable** (Adobe).
- **Source Serif 4 Variable** (Adobe).
- **IBM Plex Sans Variable** (IBM / Bold Monday).
- **Noto Sans Variable** (Google) — 1000+ idiomas suportados.
- **Crimson Pro** — serif variable.
- **Public Sans** (USWDS).
- **Manrope** — geometric sans variable.
- **DM Sans Variable** (Indian Type Foundry / Google).
- **Bricolage Grotesque** (variable) — populares em landings 2024-2026.

**Comerciais / foundries**:

- **Sohne Variable** (Klim Type Foundry) — usado pela Stripe, OpenAI 2023+, varias fintechs.
- **GT America** (Grilli Type) — variable.
- **Aktiv Grotesk** (Dalton Maag).
- **Object Sans** (Pangram Pangram).
- **Neue Haas Grotesk Variable** (Linotype).

### 3.6 Browser support 2026

Variable fonts suportadas em 95%+ browsers desde 2020. Em 2026: Chrome, Safari, Firefox, Edge — todos full support. Pode-se usar sem fallback estatico.

## Fundacao 4 — Licenciamento (Google Fonts free + Adobe Fonts subscription + MyFonts + Type Foundries + Custom Enterprise)

### 4.1 Modelos de licenciamento

**Tipos comuns de license**:

- **Desktop license**: instalar em maquina, usar em apps (Word, Photoshop). Cobranca por seat/usuario.
- **Webfont license**: usar em sites. Geralmente cobranca por pageview/mes ou unlimited.
- **App license**: embutir em app mobile/desktop. Cobrada separadamente.
- **ePub / e-book license**: embutir em livros digitais.
- **Server license**: rodar em servidor (ex: gerar PDFs dinamicos).
- **Broadcast license**: TV/cinema/video.
- **Open source / Libre license**: gratuito, geralmente OFL (SIL Open Font License) ou Apache 2.0.

### 4.2 Google Fonts (free)

- **Site**: https://fonts.google.com/ — 1500+ fontes em 2026.
- **License**: SIL Open Font License (OFL) — uso comercial e pessoal livre, redistribuicao permitida, NAO se pode vender a fonte sozinha.
- **Pros**: gratis, CDN gratis (fonts.googleapis.com), uso ilimitado, integracao com Adobe Fonts, popular = familiar.
- **Contras**: nao customizavel, todo mundo usa (Roboto, Open Sans, Lato sao comoditizados), CDN tem implicacoes LGPD/GDPR (IP do usuario vai para Google — caso 2022 Munique multou site por usar Google Fonts via CDN; recomenda-se self-host).
- **Self-host**: usar google-webfonts-helper (gwfh.mranftl.com) para baixar arquivos e servir do proprio dominio (recomendado por LGPD/GDPR).

**Top Google Fonts 2026** (por uso):

- Roboto, Open Sans, Lato (comoditizados — evitar branding).
- Inter, IBM Plex, Source Sans 3 (modernos, melhores).
- Playfair Display, Lora, Merriweather (serifs populares).
- Montserrat, Poppins (geometric sans).
- JetBrains Mono, Fira Code (mono dev).

### 4.3 Adobe Fonts (subscription)

- **Site**: https://fonts.adobe.com/ — 25.000+ fontes em 2026, 150+ foundries (Monotype, Linotype, ITC, FontFont, MTI, e foundries independentes).
- **License**: incluso em qualquer plano Creative Cloud (Photoshop, Illustrator, todos planos $20+/mes em 2026). Web fonts unlimited pageviews.
- **Pros**: integracao CC, sync automatico desktop, web fonts servidos via CDN (use.typekit.net), curadoria.
- **Contras**: NAO se pode embutir em apps/jogos/produto fisico (precisa licensiar separadamente da foundry); se cancelar CC, perde acesso e site quebra (se hospedado via Adobe CDN).
- **Estrategia**: usar Adobe Fonts para prototipagem/explore; se vai usar em producao long-term, comprar webfont license direto da foundry.

### 4.4 MyFonts (Monotype) — marketplace

- **Site**: https://www.myfonts.com/ — 130.000+ fontes, marketplace de centenas de foundries.
- **License**: pay-per-license, tipicamente desktop $30-50, webfont 250k pageviews ~$50-200, app/server precos custom.
- **Pros**: maior catalogo unico do mundo, foundries pequenas + grandes, frequentes promos 70-90% off.
- **Contras**: precos somam (cada peso = licenca separada em algumas fontes; webfont cobranca por pageview).
- **Owned by Monotype** (desde 2014).

### 4.5 Type Foundries independentes (premium)

Foundries independentes de qualidade premium 2026:

- **Klim Type Foundry** (NZ — Kris Sowersby) — Calibre, National 2, Tiempos, Sohne (usada por Stripe, OpenAI 2023+, MailerLite). klim.co.nz.
- **Grilli Type** (CH) — GT America, GT Walsheim, GT Sectra. grillitype.com.
- **Pangram Pangram Foundry** (CA) — Object Sans, PP Mori, PP Editorial New, varios free para personal. pangrampangram.com.
- **Dinamo** (CH) — ABC Diatype, ABC Whyte, ABC Favorit. abcdinamo.com.
- **OH no Type Co** (US — James Edmondson) — Obviously, Vulf Sans, Hobeaux. ohnotype.co.
- **Lineto** (CH) — Akkurat, LL Brown, LL Riforma. lineto.com.
- **Commercial Type** (US/UK) — Graphik, Marian, Publico (NYT, Guardian usam). commercialtype.com.
- **Schick Toikka** (DE/FI) — Apoc, Soehne (com Klim originalmente), Vincente. schick-toikka.com.
- **Production Type** (FR) — Surt, Mokoko, Search. productiontype.com.
- **Hoefler & Co.** (US, agora "Monotype Studio") — Gotham, Mercury, Whitney, Operator. hoeflerco.com.
- **Frere-Jones Type** (US) — Mallory, Pilcrow, Empirica. frerejones.com.
- **TypeTogether** (CZ/AR) — Bree, Karmina, Adelle. type-together.com.
- **Bold Monday** (NL) — IBM Plex (com IBM), Productype. boldmonday.com.

### 4.6 Custom enterprise fonts (top-tier)

Big techs encomendam fontes custom como moat de diferenciacao:

- **Apple SF Pro** (Apple — Antonio Cavedoni / Apple Type Team) — desde 2015 substituiu Helvetica Neue. SF Pro Display (>20pt) + SF Pro Text (<19pt) + SF Mono + SF Compact (Watch). License: Apple Developer License (gratuito mas restrito a apps Apple).
- **IBM Plex** (IBM — Mike Abbink + Bold Monday, 2017) — open source SIL OFL. Sans + Serif + Mono + Sans Condensed. Usada em IBM, mas tambem por outras empresas (gratuita).
- **Stripe Sohne** (Stripe — usa Sohne da Klim Type Foundry desde 2020, antes usava Camphor) — license comercial Klim. Stripe pagou desenvolvimento de variantes.
- **Spotify Circular** (Spotify — Lineto Circular Pro custom desde 2014) — encomenda exclusiva. Lineto desenvolveu pesos extras.
- **Mailchimp Cooper Light** (Mailchimp — usa ITC Cooper Black/Light retro) — licensiada, nao custom mas escolha distinctive.
- **Slack Lato (atual: Slack-Sans / Hack)** — Slack mudou de Lato (2014-2018) para custom 2019+ "Slack-Sans" (baseado em Larsseit) e Hack para mono.
- **Airbnb Cereal** (Airbnb — Dalton Maag, 2018) — custom variable font, 6 pesos. NAO publica.
- **Netflix Sans** (Netflix — Dalton Maag, 2018) — custom para reduzir custos de licenciamento Gotham (que pagavam milhoes/ano).
- **Google Sans** / **Product Sans** (Google — Google Type Team, baseado em Futura) — custom para Google. **Google Sans Flex** liberada como Google Sans em 2025 (variable, open).
- **YouTube Sans** (YouTube — Saffron Type Foundry / Bold Monday) — custom 2017+.
- **Uber Move** (Uber — MCKL, 2018) — custom variable, substituiu Clan Pro.
- **Intercom Sharp Grotesk** (Intercom — Sharp Type, 2019) — custom.
- **Coinbase Coinbase Display + Sans** (Coinbase — custom 2022).
- **OpenAI usa Sohne** (Klim) — nao custom, mas distinctive 2023+.
- **Anthropic** — usa Tiempos (Klim) + Söhne para a marca Claude.
- **Notion Sans** (Notion — interno).
- **Discord uses Whitney** (Hoefler & Co.) — licensiada.

**Custo de custom font corporativa**: $50k-500k+ desenvolvimento + manutencao. Justifica para top 1000 marcas globais (saving longo prazo + brand differentiation).

### 4.7 Mudancas EULA 2026: AI training clauses

**Tendencia 2026**: Major foundries (Monotype, Hoefler & Co., Lineto, Klim) atualizaram EULAs para proibir explicitamente uso da fonte como training data para AI generativa. Algumas clausulas tipicas:

- "Licensee shall not use the Font Software, in whole or in part, as input data, training data, or for any other use in the development, training, fine-tuning, or operation of any artificial intelligence, machine learning, or generative model."
- Em alguns casos isso retroage e cobre tambem agentes que geram designs com a fonte.

**Impacto Frank-MKT**: ao usar fontes em assets gerados por IA (Midjourney, Imagen, GPT-image), checar se EULA permite. Open source OFL geralmente permite, comerciais geralmente proibem.

### 4.8 Subscription vs comprar (decision matrix)

| Criterio | Adobe Fonts | Comprar foundry | Custom enterprise |
|----------|-------------|------------------|-------------------|
| Custo | $20-50/mes | $300-3000 once | $50k-500k+ |
| Tempo / disponibilidade | Imediato | Imediato | 6-18 meses |
| Flexibilidade modificacao | Nenhuma | Nenhuma (ou +$$) | Total |
| Risco lock-in | Alto (cancelou = some) | Baixo (perpetuo) | Nenhum |
| Diferenciacao marca | Baixa | Media | Maxima |
| Indicado para | Prototipo / startup early | SaaS scaleup / agencia | Top 1000 marcas |

## Fundacao 5 — Web Implementation (Fallbacks + FOUT/FOIT + Variable + Subset + WOFF2)

### 5.1 Formatos de web fonts (2026)

| Formato | Status 2026 | Comprimento bytes vs TTF | Uso |
|---------|-------------|--------------------------|-----|
| TTF / OTF | Legacy (nao usar web) | 100% (baseline) | Desktop apps |
| EOT | Morto (IE) | 100% | Nao usar |
| WOFF | Quase morto | ~70% (gzipado) | Compatibilidade IE9-11 (so se precisar) |
| WOFF2 | **Padrao 2026** | ~50% (Brotli) | **USAR SEMPRE** |
| SVG fonts | Deprecated | Grande | Nao usar |

WOFF2 e o unico formato que importa em 2026. Suporte: 99%+ browsers desde 2020.

### 5.2 @font-face moderno (2026)

```css
@font-face {
  font-family: 'Inter';
  src: url('/fonts/Inter-roman.var.woff2') format('woff2-variations');
  font-weight: 100 900;
  font-style: normal;
  font-display: swap;
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC,
                 U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC,
                 U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
}
```

### 5.3 font-display values

| Valor | Comportamento | Quando usar |
|-------|---------------|-------------|
| `auto` | Browser decide (geralmente FOIT) | Default; nao recomendado |
| `block` | FOIT 3s, depois fallback | Fontes display/branding criticas |
| `swap` | Fallback imediato, swap no load | **Padrao recomendado** |
| `fallback` | FOIT 100ms, swap se carregar em 3s | Body text intermediario |
| `optional` | Browser decide carregar ou nao | Lazy/optional decorative |

**Regra ouro 2026**: usar `swap` para body, `optional` para fontes nao-criticas, `block` so se branding for absolutamente prioridade (raro).

### 5.4 FOUT vs FOIT

- **FOUT** (Flash of Unstyled Text): texto aparece em fallback, "pisca" para custom font quando carrega. CSS `font-display: swap`.
- **FOIT** (Flash of Invisible Text): texto invisivel ate fonte carregar. CSS `font-display: block`.
- **FOFT** (Flash of Faux Text): variante onde browser sintetiza bold/italic ate fonte real chegar.

**Mitigation strategies**:

1. **System font stack fallback** que combine metricas:

```css
body {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}
```

2. **size-adjust descriptor** (CSS Fonts L4) ajusta fallback para metricas similares a custom font, eliminando layout shift:

```css
@font-face {
  font-family: 'Inter Fallback';
  src: local('Arial');
  size-adjust: 107%;
  ascent-override: 90%;
  descent-override: 22%;
  line-gap-override: 0%;
}
```

3. **fontaine** / **next/font** (Next.js) — automatizam isso.

### 5.5 Preload critical fonts

```html
<link rel="preload" href="/fonts/Inter.var.woff2" as="font" type="font/woff2" crossorigin>
```

Reduz LCP em 100-300ms para fonte hero. Limitar a 1-2 preloads (cada preload custa banda inicial).

### 5.6 Subsetting

Reduzir bytes carregando apenas glyphs necessarios:

- **glyphhanger** (Filament Group) — analisa site e gera subset.
- **pyftsubset** (fonttools Python) — CLI subsetting.
- **fonttools-merge** — merge multiple fonts.
- **Wakamai Fondue** (wakamaifondue.com) — analisa fonte online.
- **Google Fonts** ja faz subset automatico via `?text=` ou via subset CSS.

**Estrategia tipica pt-BR**:

- Subset Latin (basico) + Latin Extended-A (acentos pt-BR completos: a a a a a c e e e i i o o o u u).
- Reduz Inter Variable de ~600KB para ~80KB.

### 5.7 Self-host vs CDN

**CDN (Google Fonts, Adobe Typekit)**:

- Pros: zero setup, cache compartilhado historicamente.
- Contras: privacidade (LGPD/GDPR — IP usuario vai para terceiro), single point of failure, browser cache shared eliminado em 2020+ (cache partitioning Chrome 86).

**Self-host (recomendado 2026)**:

- Pros: privacidade, controle total, performance (mesmo dominio = HTTP/2 multiplexing), no third-party.
- Contras: mais setup.
- Tools: google-webfonts-helper para baixar, coloca em `/fonts/`, configura `@font-face`.

### 5.8 next/font (Next.js 13+) e Astro fonts

`next/font` e o melhor framework de webfont 2024-2026:

```jsx
import { Inter } from 'next/font/google';
const inter = Inter({ subsets: ['latin', 'latin-ext'], variable: '--font-inter' });
```

Auto: subset, self-host, preload, fallback metric matching, CSS variable. Zero CLS (Cumulative Layout Shift).

Astro tem `@astrojs/font` (2024+) similar.

## Fundacao 6 — Brasil 2026 (cases nacionais + portuguese accent characters + tipografia tropical)

### 6.1 Acentos pt-BR (caracteres especificos)

Caracteres essenciais para portugues brasileiro que TODA fonte usada deve suportar:

- **Acento agudo**: a e i o u A E I O U.
- **Acento circunflexo**: a e o A E O.
- **Til (tilde)**: a o A O.
- **Cedilha**: c C.
- **Acento grave** (raro mas existe): a A (e.g., "as" vs "as").
- **Trema** (eliminado pelo Acordo 2009 mas ainda em nomes proprios): u U.

**Unicode block**: Latin Extended-A (U+0100 a U+017F) cobre 99% pt-BR. Latin-1 Supplement (U+0080 a U+00FF) cobre os acentos comuns.

**Verificar suporte**: usar wakamaifondue.com ou abrir TTF em FontDrop.info — listar glyphs.

**Pegadinha comum**: fontes "Latin only" do Google Fonts as vezes nao incluem c, e, e (raro mas ja vimos). Sempre baixar `subsets: ['latin', 'latin-ext']`.

### 6.2 Type design brasileiro (foundries + designers)

**Foundries / designers BR de destaque 2026**:

- **Fabio Haag Type** (Fabio Haag, gaucho, Buenos Aires) — Aller, Brasilica, custom para marcas. fabiohaagtype.com. Top BR.
- **Tipos do aCASO** (Lais de Carvalho) — fontes display, identidades regionais.
- **PampaType** (Diego Maldonado, RS) — fontes brasileiras como Brava, Sansita One. pampatype.com.
- **Plau** (Rodrigo Saiani, RJ + globais) — Plau (display experimental), Lector, varias para branding. plau.co.
- **Bossanova Foundry** (Tony de Marco) — Folha Serif (1994/95 — pioneira BR), Serpa, Notisans. bossanovafoundry.com.
- **Henrique Beier** — fontes para identidades (Plau, Setimo).
- **Naipe Foundry** (Crystian Cruz) — display brasileiras. naipefoundry.com.
- **Seg Type Foundry** (Igor Bastos / Seg) — fontes vernaculas brasileiras. segtypefoundry.com.

### 6.3 Tipografia vernacular brasileira

Vernacular = letterforms espontaneas, populares (placas de feira, carrocas, bares, kombi). Movimento "Pintores de Letras" documentou isso 2010+.

**Caracteristicas**:

- Pesos extremos (muito bold, condensados).
- Cores saturadas.
- Geometria irregular charmosa.
- Sombras dramaticas.
- Influencia futbol clube, samba, baile funk.

**Fontes inspiradas**: Brasilica (Fabio Haag), Cabaret, Trocchi, varios projetos Behance. Brasil 2026 World Cup kit font usa elementos vernaculares modernizados.

### 6.4 Cases marcas brasileiras 2026

**Magalu / Magazine Luiza**:

- Tipografia sans-serif moderna friendly (semelhante a Poppins / Avenir Next).
- Heading bold + body regular.
- Lu (mascote) tem typography distintiva.

**Nubank**:

- Graphik (Commercial Type) para print/branding.
- Sans-serif geometric humanist para UI app.
- Rebrand 2021 manteve filosofia "minimalismo roxo" + tipografia clean.

**Itau**:

- Itau Display + Itau Text — fontes custom desenvolvidas pelo banco.
- Investimento em type custom desde anos 2010s.

**Stone**:

- Visual identity moderna pos-IPO 2018, sans-serif geometric (similar Aktiv Grotesk / Sohne).
- Heading bold + verde Stone iconico.

**O Boticario**:

- Identidade reformulada 2010s, sans-serif moderna.

**Banco do Brasil**:

- BB Sans (custom desenvolvido).

**Globo**:

- Globotype (custom Bossanova Foundry / Tony de Marco) — uso editorial.

**Folha de S. Paulo**:

- Folha Serif (Tony de Marco, 1994/1995) — primeira fonte exclusiva de jornal BR.

**Estadao / O Estado de S. Paulo**:

- Custom serif desde 2010s.

**Petrobras**:

- Tipografia institucional moderna pos-rebrand 2018.

### 6.5 Particularidades pt-BR em web type

- **Tamanho medio palavras pt-BR > en-US**: portugues brasileiro tem palavras 15-20% mais longas em media (vs ingles). Layouts traduzidos de en para pt-BR frequentemente quebram. Considerar `max-width: 70ch` (vs 65 em).
- **Hyphenation**: CSS `hyphens: auto` + `lang="pt-BR"` no HTML melhora muito quebra de linha em pt-BR (palavras longas).
- **Acentos em uppercase**: muitas fontes tem problemas com acentos em CAPS (CAFE, AMERICA). Verificar se fonte tem `case-sensitive forms` (OpenType `case`).
- **C (cedilha) em uppercase**: CONFIRMACAO — algumas fontes nao suportam C maiusculo bem. Testar.

## Fundacao 7 — Mensuracao + Tools 2026

### 7.1 KPIs de tipografia em produto digital

- **Performance**:
  - Bytes de fonts no carregamento inicial (alvo: <100KB).
  - LCP impact (alvo: fontes nao bloqueiam LCP — preload + swap).
  - CLS impact (alvo: 0 — usar size-adjust ou next/font).
  - FCP impact (alvo: <1.5s).
- **UX / Legibilidade**:
  - Tempo medio em pagina (mais tempo = mais leitura = legibilidade boa).
  - Scroll depth (chega ao final = engajamento de leitura).
  - Bounce rate (alto = problema de legibilidade ou tipografia errada).
- **Brand recall**:
  - Pesquisa qualitativa (usuarios reconhecem marca pela tipografia?).
  - A/B test custom font vs Google Font generico.
- **Acessibilidade**:
  - WCAG audit pass rate (Lighthouse, axe-core).
  - Contraste WCAG AA / AAA.

### 7.2 Ferramentas 2026

**Discovery / specimen**:

- **Fonts In Use** (fontsinuse.com) — base de dados onde cada fonte e usada.
- **Identifont** (identifont.com) — identifica fonte por caracteristicas.
- **WhatTheFont** (myfonts.com/WhatTheFont) — upload imagem, identifica.
- **Fontjoy** (fontjoy.com) — gerador pairings com IA.

**Type scale / hierarchy**:

- **type-scale.com** — escala modular com CSS.
- **modularscale.com** — visual.
- **utopia.fyi** — fluid type clamp() generator.
- **typescale.com** — preview multi-fontes.

**Performance / web**:

- **google-webfonts-helper** (gwfh.mranftl.com) — baixa GFonts + gera @font-face.
- **wakamaifondue.com** — analisa qualquer fonte (axes, glyphs, OpenType features).
- **fontdrop.info** — preview fonte browser.
- **glyphhanger** — subsetting CLI.
- **fonttools** (Python) — toolkit completo.
- **fontaine** (npm) — auto-fallback metrics.

**Variable fonts playground**:

- **v-fonts.com** — catalogo + playground.
- **variablefonts.io** — explicacao + exemplos.
- **axis-praxis.org** (Laurence Penney) — original variable font playground.

**Testing**:

- **Lighthouse** (Chrome DevTools) — perf + a11y.
- **WebPageTest** — analise detalhada.
- **axe DevTools** — a11y audit.
- **Chrome DevTools Network** — bytes / waterfall.

**Type design pro**:

- **Glyphs** (glyphsapp.com) — Mac, padrao foundries.
- **FontLab 8** — Mac/Win, profissional.
- **FontForge** — open source, multi-OS.
- **Robofont** — Mac, profissional.

### 7.3 Audit de tipografia (checklist mensuracao)

1. Site usa quantas fontes? (alvo: 1-2, max 3).
2. Bytes total fonts? (alvo: <150KB).
3. WOFF2? Variable? (sim para ambos).
4. Subset latin + latin-ext (pt-BR)?
5. Preload critical?
6. font-display: swap?
7. CLS = 0?
8. Body >= 16px? Line-height >= 1.5?
9. Contraste >= 4.5:1 (body) / 3:1 (large)?
10. Suporte a a a c e i o u completo?
11. Self-host (LGPD/GDPR)?
12. Brand book documenta tipografia? Pesos? Sizes? Cases?
13. Fontes licenciadas legalmente? EULA inclui webfont + uso atual?
14. Variable font ou static? (variable preferido).
15. Fonte funciona em pt-BR uppercase com acentos?

## Fundacao 8 — Aplicacao em Content MKT

### 8.1 Tipografia em landing pages

- **Hero headline**: Display ou H1, 56-96px desktop, 36-48px mobile. Variable font para fluid scaling.
- **Subheadline**: Body large, 18-24px, weight 400.
- **Body**: 16-18px, line-height 1.6.
- **CTA button**: 14-16px, weight 500-600, letter-spacing 0.02em.
- **Microcopy / labels**: 12-14px, weight 500.

### 8.2 Tipografia em blog posts (legibilidade longa)

- **Body**: 18-20px (maior que landing — leitura prolongada).
- **Line-height**: 1.65-1.75 (mais aerado).
- **Max-width**: 65-70ch.
- **Pull quotes**: serif italic 24-32px.
- **Code blocks**: mono 14-16px, line-height 1.6.
- **Imagens com captions**: caption serif italic ou sans-serif menor.

### 8.3 Tipografia em email marketing

- **Web fonts limitados em email**: muitos clients (Outlook desktop) nao suportam @font-face.
- **System font stack**: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif.
- **Tamanho**: 16-18px body (maior que web — telas mobile).
- **Line-height**: 1.5+.
- **Subject line**: maximo 50 caracteres ou trunca em mobile.

### 8.4 Tipografia em apresentacoes / decks

- **Display heading**: 60-120pt.
- **Body**: 24-32pt (Powerpoint / Keynote / Google Slides).
- **Maximo 6 linhas por slide**.
- **Fontes consistentes com brand book**.

### 8.5 Tipografia em social media

- **Instagram**: bold display em images, body curto em captions.
- **LinkedIn**: serif heading + sans body em artigos longos.
- **Twitter/X**: emoji + sans condensed em images.
- **TikTok**: motion typography, kinetic type.

### 8.6 Tipografia em packaging / impressos

- **Print typography** segue regras diferentes (CMYK, registro, paper texture).
- **Tamanho minimo**: 6-8pt para legalese, 9-12pt body.
- **Fontes serif funcionam melhor em letreiro impresso** (vs sans em tela).
- **Avoid**: pesos abaixo de Light (200) para print pequeno.

## Anti-Patterns 18

1. **Usar 5+ fontes diferentes em um site/marca** — caos visual, falta de hierarquia, marca esquizofrenica.
2. **Comic Sans / Papyrus em contexto corporativo** — destruir credibilidade instantaneamente. Excecao: ironia explicita.
3. **Fonte sem suporte a acentos pt-BR** — site quebra com c, a, e (renderiza como caixa branca/glyph faltante).
4. **Body text < 14px** — viola WCAG e degrada UX leitura. Min 16px desktop, 14px mobile so para captions.
5. **Line-height < 1.4 em body** — texto compactado, ilegivel. Min 1.5 (WCAG).
6. **Letter-spacing 0 em all-caps** — CAPS PRECISAM letter-spacing >= 0.05em para legibilidade.
7. **Display font em body text** — Bebas Neue, Playfair Display, Oswald nao foram desenhadas para texto longo. Cansam leitor.
8. **CDN externa (Google Fonts) sem self-host em mercado UE/BR** — viola LGPD/GDPR (IP usuario para Google). Multas 2022+ em Munique, Berlin.
9. **Nao usar font-display** — FOIT por 3s default. Usar `swap` ou `optional`.
10. **Usar TTF/OTF em vez de WOFF2** — 2x mais bytes, sem ganho.
11. **Cancelar Adobe Creative Cloud com site em producao** — license expira, site quebra (se usa Adobe Fonts via use.typekit.net).
12. **Comprar fonte para "site pessoal" e usar em corporate** — viola license. Webfont license enterprise tem outro tier.
13. **Embutir fonte em app sem app license** — apps mobile (iOS/Android) precisam app license, nao webfont.
14. **Hierarchy plana** (todos H1-H6 com sizes muito proximos) — usuario nao distingue secoes. Type scale modular fix.
15. **Color contraste < 4.5:1 (body)** — viola WCAG AA. Usar contrastchecker / WebAIM.
16. **Fontes "trendy" em marcas long-term** (ex: brush script de moment) — vai envelhecer mal. Marca precisa fonte timeless.
17. **Variable font como static fallback** — usar variable e desperdicar = 1 arquivo grande sem aproveitar eixos.
18. **Nao documentar tipografia em brand book** — designer novo entra, escolhe fonte aleatoria, marca degrada gradualmente.

## 18 Regras de Ouro

1. **Hierarquia clara**: Display > H1 > H2 > H3 > Body > Caption. Type scale modular (ratio 1.20-1.333).
2. **Maximo 2-3 fontes**: heading + body (+ mono se tech). Mais que 3 = caos.
3. **Body 16-18px desktop, line-height 1.5-1.65** — WCAG + legibilidade.
4. **Variable fonts em 2026**: 1 arquivo, multiplos pesos, performance. Use sempre que possivel.
5. **WOFF2 + font-display: swap + preload critical** — performance default.
6. **Self-host fonts em mercado pt-BR/UE** — LGPD/GDPR compliance.
7. **Subset latin + latin-ext** para pt-BR — completar acentos.
8. **Contraste WCAG AA minimo (4.5:1 body / 3:1 large)** — acessibilidade obrigatoria.
9. **Documentar em brand book**: familias, pesos, sizes, line-heights, casos de uso.
10. **Pairing testado**: Sans + Serif ou Sans (heading bold) + Sans (body regular). Nao inventar.
11. **Tipografia consistente entre touch points**: web, app, print, email, social.
12. **Custom enterprise font apenas se top 1000 marcas** — investimento $50k-500k+ justifica diferenciacao.
13. **Acordar com brand book de cor (paleta-cores-corporativa) e logo (logo-design-process)** — sistema unificado.
14. **Test em dispositivos reais**: desktop / tablet / mobile / dark mode / print.
15. **Acessibilidade dyslexia-friendly**: x-height alto, apertures abertos, espacamento generoso.
16. **Fluid typography com clamp()** — sem media queries, escala suave.
17. **Mensurar performance**: bytes fonts, LCP, CLS antes/depois.
18. **Volatility: revisar tipografia a cada 6-12 meses** — mudancas EULA, novas fontes, performance, acessibilidade.

## Exemplos Comportamentais

### Persona 1 — CMO startup SaaS B2B (Brasil)

**Cenario**: CMO de SaaS B2B early-stage (Series A) precisa definir tipografia para rebrand pos-funding. Time pequeno (1 designer), budget tipografia <$5k/ano.

**Como usar esta skill**:

- Ler Fundacoes 1, 2, 4 (foundations + hierarquia + licenciamento).
- Decisao: usar **Inter Variable** (Google Fonts open source SIL OFL) como heading + body — gratis, moderna, suporte completo pt-BR.
- Pairing: Inter (sans) + JetBrains Mono (codigo em docs/dashboard) — GFonts.
- Self-host via google-webfonts-helper (LGPD).
- Variable: 1 arquivo Inter.var.woff2 ~80KB subset.
- Implementar `font-display: swap`, `<link rel="preload">`, `next/font/google` se Next.js.
- Documentar no brand book emergente: Inter 100-900, body 16px line-height 1.6, headings 24/32/40/56 px.
- Custo: $0 fontes, 4-8h dev integracao.

**Output esperado**: tipografia profissional indistinguivel de IBM/Stripe (que usam fontes premium custom), zero custo recorrente, performance Lighthouse 95+.

### Persona 2 — Brand Designer agencia (atende marcas medias BR)

**Cenario**: Designer senior em agencia de branding (10-30 pessoas) cria identidade para marca de varejo BR (mid-market, 50M-500M revenue). Cliente pode investir $5-30k em type.

**Como usar esta skill**:

- Ler Fundacoes 1, 2, 4, 6 + 18 regras de ouro.
- Decisao: pairing premium customizado.
  - Heading: **GT America Mono** ou **Sohne** (Klim) — distinctive, ~$3-5k webfont license.
  - Body: **Source Sans 3 Variable** (Adobe / open source) ou **IBM Plex Sans** — gratis.
  - Servir: webfont license direto Klim para Sohne; self-host Plex.
- Brand book: documentar 4 pesos (Light/Regular/Medium/Bold), tipos de heading (Display 96/H1 56/H2 40), body 18px, caption 14px, line-height por nivel.
- Garantir suporte acentos pt-BR (Sohne tem; Plex tem completo).
- Apresentar diferenciacao (vs concorrentes que usam Roboto generico).

**Output esperado**: marca distinctiva, type system documentado, webfont license em ordem, brand book entregue.

### Persona 3 — Dev frontend (implementa brand book existente)

**Cenario**: Dev frontend recebe brand book com fontes definidas (ex: IBM Plex Sans + IBM Plex Serif + IBM Plex Mono). Precisa implementar em Next.js 14 com Tailwind, performance maxima.

**Como usar esta skill**:

- Ler Fundacoes 3, 5, 7 (variable + web implementation + measurement).
- Implementar com `next/font/google`:

```jsx
import { IBM_Plex_Sans, IBM_Plex_Serif, IBM_Plex_Mono } from 'next/font/google';
const plexSans = IBM_Plex_Sans({
  subsets: ['latin', 'latin-ext'],
  weight: ['300', '400', '500', '600', '700'],
  variable: '--font-plex-sans',
  display: 'swap',
});
```

- Tailwind config:

```js
theme: { fontFamily: {
  sans: ['var(--font-plex-sans)', 'system-ui', 'sans-serif'],
  serif: ['var(--font-plex-serif)', 'Georgia', 'serif'],
  mono: ['var(--font-plex-mono)', 'ui-monospace', 'monospace'],
}}
```

- Type scale: ratio 1.250 base 16px — Tailwind ja vem perto.
- Lighthouse audit: bytes <100KB, LCP <2s, CLS = 0.
- A11y: contraste check (Tailwind colors + brand colors), body 16px, line-height 1.6.

**Output esperado**: site implementa brand book fielmente, performance 95+, zero CLS.

### Persona 4 — CCO enterprise (Itau-scale)

**Cenario**: CCO de banco/fintech grande (>5000 funcionarios) avalia se vale custom enterprise font ($300-500k investimento + manutencao).

**Como usar esta skill**:

- Ler Fundacoes 4 + 8 + cases big tech.
- Avaliar:
  - **Saving licenciamento longo prazo**: se paga $50-200k/ano em webfont licenses Sohne/Graphik/Aktiv, custom paga em 3-5 anos.
  - **Diferenciacao brand**: top concorrentes (BB usa BB Sans; Itau ja tem Itau Display/Text). Manter relevante = atualizar custom.
  - **Cobertura cross-channel**: web + app + ATM + cartao + comunicacao impressa + TV. Custom cobre tudo, sem licenses fragmentadas.
- Processo:
  - RFP para 3-5 type foundries (Klim, Dalton Maag, Sharp Type, Bold Monday, Grilli, Bossanova BR).
  - Briefing: voice/tone, casos uso, idiomas (pt-BR + en + es + outros), variants (Display + Text + Mono + UI), variable axes.
  - Timeline: 12-18 meses do briefing ao deploy.
  - Maintenance contract: 5-10% custo dev/ano.
- Cases referencia: Netflix Sans (Dalton Maag) substituiu Gotham e economizou milhoes/ano; Airbnb Cereal idem; Uber Move idem.

**Output esperado**: business case aprovado, RFP, contrato com foundry, custom font em deploy 12-18 meses.

## Checklist Contraditorio Interno (10 perguntas)

Antes de finalizar o sistema tipografico, responder honestamente:

1. **A tipografia escolhida sera relevante em 5-10 anos?** Ou e tendencia 2026 que envelhece em 2 anos?
2. **A fonte tem suporte completo a pt-BR?** Testou a a a a a c e i o u em uppercase + lowercase + numerais?
3. **A licenca cobre 100% dos casos de uso atuais E projetados?** Web + app + impresso + video + ad networks + apresentacoes?
4. **A performance impacta Core Web Vitals negativamente?** Mediu LCP / CLS / bytes antes e depois?
5. **A tipografia atende WCAG 2.2 AA (minimo) ou AAA (ideal)?** Body >= 16px? line-height >= 1.5? contraste >= 4.5:1?
6. **A hierarquia e clara?** Usuario consegue distinguir Display / H1 / H2 / Body / Caption a primeira vista?
7. **O brand book documenta tipografia explicitamente?** Pesos, sizes, line-heights, casos de uso, do/dont?
8. **A tipografia funciona em dark mode?** Testou contraste em fundo escuro?
9. **Funciona em mobile (viewport pequeno)?** Fluid typography ou media queries adequadas?
10. **A tipografia esta alinhada com cor (paleta-cores-corporativa) e logo (logo-design-process)?** Sistema unificado ou ilhas isoladas?

## Referencias

### Type design + theory

- [WebAIM: Typefaces and Fonts](https://webaim.org/techniques/fonts/)
- [Section 508: Accessible Fonts and Typography](https://www.section508.gov/develop/fonts-typography/)
- [MDN: Variable Fonts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts/Variable_fonts)
- [MDN: @font-face](https://developer.mozilla.org/en-US/docs/Web/CSS/@font-face)
- [MDN: font-display](https://developer.mozilla.org/en-US/docs/Web/CSS/@font-face/font-display)
- [Variable Fonts](https://v-fonts.com/)
- [Variable Fonts io](https://variablefonts.io/about-variable-fonts/)
- [Axis Praxis (Laurence Penney)](https://www.axis-praxis.org/)
- [Wakamai Fondue](https://wakamaifondue.com/)
- [FontDrop](https://fontdrop.info/)
- [Typographica](https://typographica.org/)
- [Fonts In Use](https://fontsinuse.com/)
- [Identifont](https://www.identifont.com/)

### Foundries + plataformas

- [Google Fonts](https://fonts.google.com/)
- [Adobe Fonts](https://fonts.adobe.com/)
- [MyFonts](https://www.myfonts.com/)
- [Klim Type Foundry](https://klim.co.nz/)
- [Grilli Type](https://www.grillitype.com/)
- [Pangram Pangram Foundry](https://pangrampangram.com/)
- [Dinamo (ABC fonts)](https://abcdinamo.com/)
- [OH no Type Co](https://ohnotype.co/)
- [Lineto](https://lineto.com/)
- [Commercial Type](https://commercialtype.com/)
- [Hoefler & Co.](https://www.typography.com/)
- [Frere-Jones Type](https://frerejones.com/)
- [TypeTogether](https://www.type-together.com/)
- [Bold Monday](https://www.boldmonday.com/)
- [Production Type](https://productiontype.com/)

### Web typography + tools

- [google-webfonts-helper](https://gwfh.mranftl.com/fonts)
- [Type Scale](https://typescale.com/)
- [type-scale.com](https://type-scale.com/)
- [Modular Scale](https://www.modularscale.com/)
- [Utopia.fyi (fluid type)](https://utopia.fyi/)
- [Fontjoy (pairing AI)](https://fontjoy.com/)
- [glyphhanger (subsetting)](https://github.com/zachleat/glyphhanger)
- [fontaine (npm)](https://github.com/danielroe/fontaine)
- [next/font docs](https://nextjs.org/docs/app/api-reference/components/font)

### Custom enterprise fonts (cases)

- [IBM Plex Sans (Google Fonts)](https://fonts.google.com/specimen/IBM+Plex+Sans)
- [IBM Plex (GitHub)](https://github.com/IBM/plex)
- [Apple Developer: SF Pro Fonts](https://developer.apple.com/fonts/)
- [Spotify Brand: Circular](https://newsroom.spotify.com/company-info/) (info via brand pages)
- [Airbnb Cereal (Dalton Maag)](https://www.daltonmaag.com/work/airbnb-cereal.html)
- [Netflix Sans (Dalton Maag)](https://www.daltonmaag.com/work/netflix-sans.html)
- [Uber Move (MCKL)](https://mckltype.com/blog/uber-move)
- [Stripe usa Sohne (Klim)](https://klim.co.nz/blog/searching-for-soehne/)

### Brasil — type design + foundries

- [Fabio Haag Type](https://fabiohaagtype.com/)
- [Plau](https://plau.co/)
- [Bossanova Foundry (Tony de Marco)](https://bossanovafoundry.com/)
- [PampaType (Diego Maldonado)](https://www.pampatype.com/)
- [Naipe Foundry (Crystian Cruz)](https://naipefoundry.com/)
- [Behance Tipografia Brasileira](https://www.behance.net/search/projects/tipografia%20brasileira)
- [Tipografia Vernacular Brasileira (Rafael Hoffmann)](https://www.rafaelhoffmann.com/textos/tipografia_vernacular_brasileira.html)
- [Pintores de Letras (Medium)](https://medium.com/@pintoresdeletras/tipografia-vernacular-brasileira-4d9a8791dae0)

### Acessibilidade + WCAG

- [WCAG 2.2 (W3C)](https://www.w3.org/TR/WCAG22/)
- [WCAG SC 1.4.3 Contrast Minimum](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html)
- [WCAG SC 1.4.4 Resize Text](https://www.w3.org/WAI/WCAG22/Understanding/resize-text.html)
- [WCAG SC 1.4.12 Text Spacing](https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html)
- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
- [accessiBe: ADA-compliant fonts 2026](https://accessibe.com/blog/knowledgebase/ada-compliant-fonts)

### Articles 2026

- [Brand Typography Trends 2026 — memorable.design](https://memorable.design/brand-typography-trends/)
- [The Importance of Typography in Branding 2026 — Neue World](https://www.neue.world/insights/the-importance-of-typography-in-branding)
- [Brand Typography Guide 2026 — Shopify](https://www.shopify.com/blog/brand-typography)
- [Variable Fonts Explained 2026 — Inkbot Design](https://inkbotdesign.com/variable-fonts/)
- [Typography Trends 2026 — DesignMonks](https://www.designmonks.co/blog/typography-trends-2026)
- [Web Font Optimization 2026 — Enepsters](https://www.enepsters.com/2026/03/web-font-optimization-in-2026-balancing-performance-accessibility-and-design/)
- [Best Fonts for Readability 2026 — webability.io](https://www.webability.io/blog/best-font-for-readability)
- [Font Licensing 2026 — Inkbot Design](https://inkbotdesign.com/font-licensing/)
- [Typography Trends 2026 — Boomer.pt](https://boomer.pt/raiodoblog/tendencias-de-tipografia-e-type-design-em-2026-letras-que-sentem-mexem-e-contam-historias/)
- [Typography Trends 2026 — IK Agency](https://www.ikagency.com/graphic-design-typography/typography-trends-2026/)
- [Typography Trends 2026 — TheInkorporated](https://www.theinkorporated.com/insights/future-of-typography/)

### Specs

- [OpenType Font Variations Spec (Microsoft)](https://learn.microsoft.com/en-us/typography/opentype/spec/otvaroverview)
- [SIL Open Font License (OFL)](https://openfontlicense.org/)
- [Apache License 2.0 (used by Google Fonts)](https://www.apache.org/licenses/LICENSE-2.0)
- [W3C CSS Fonts Module Level 4](https://www.w3.org/TR/css-fonts-4/)

## Cross-Skill References

Esta skill integra com outras do Frank-MKT:

- **logo-design-process**: tipografia logotype + wordmark depende de fonte custom ou bem licenciada; tipografia institucional vem em conjunto com logo.
- **brand-book-methodology**: tipografia e capitulo essencial de qualquer brand book; documentar familias, pesos, sizes, line-heights, casos uso.
- **paleta-cores-corporativa**: cor + tipografia + logo formam triade visual; testar contraste tipografia vs background colors WCAG.
- **iconografia-corporativa**: pesos de iconografia stroke-width devem dialogar com pesos tipograficos (Inter Bold + icon stroke 2px).
- **svg-engineering-ia**: SVGs com texto integrado precisam fontes embutidas ou outlines (`<text>` vs `<path>`).
- **acessibilidade-wcag**: contraste body 4.5:1, large text 3:1, tamanho minimo 16px, line-height 1.5+, hyphens auto.
- **design-system-basico**: tokens tipograficos (font-family, font-size scale, font-weight scale, line-height, letter-spacing) sao fundacao de DS.
- **microcopy**: estilo de microcopy depende de tom da fonte (serif formal vs sans casual).
- **ux-heuristicas**: hierarquia visual (Lei de Pragnanz, F-pattern reading) depende de tipografia.
- **dataviz-corporativa**: tipografia em dataviz (chart titles, axis labels, tooltips) deve seguir mesma hierarquia.
- **slide-deck-corporativo**: tipografia em decks segue mesma type scale ajustada para projecao.

## Integracao Ecossistema Frank-MKT

**Posicao no ecossistema**:

- Bloco: Identidade Visual Corporativa / Brand Design.
- Skill #4 do bloco (depois de logo-design-process, brand-book-methodology, paleta-cores-corporativa).
- Pre-requisitos: brand-book-methodology (entender contexto onde tipografia se insere).
- Complementa: paleta-cores-corporativa (sistema visual unificado), iconografia-corporativa (pesos visuais alinhados).

**Fluxo tipico de uso**:

1. CMO ou brand designer recebe brief de marca.
2. Usa **logo-design-process** para definir logotype.
3. Usa **paleta-cores-corporativa** para definir cores.
4. Usa **tipografia-corporativa (esta skill)** para definir sistema tipografico.
5. Documenta tudo em **brand-book-methodology**.
6. Implementa em **design-system-basico** (tokens tipograficos).
7. Auditoria via **acessibilidade-wcag** (contraste + sizes + line-height).
8. Aplica em landings/blogs/decks via **slide-deck-corporativo** + content workflows.

**Trigger desta skill**:

- Usuario pergunta sobre escolha tipografica.
- Usuario menciona "fonte", "typeface", "tipografia", "font", "Google Fonts", "Adobe Fonts", "variable font", "WOFF2", "@font-face", "FOUT", "FOIT".
- Usuario faz brand book ou design system.
- Usuario tem problema de performance web relacionado a fonts.
- Usuario tem problema de acessibilidade tipografica.
- Usuario quer audit de fonts existente.

**Outputs tipicos**:

- Recomendacao de pairing tipografico (heading + body + mono).
- Decisao licenciamento (Google Fonts vs Adobe Fonts vs comprar foundry vs custom).
- Type scale modular (sizes + line-heights + weights).
- Codigo CSS / next/font / Tailwind config.
- Audit de tipografia existente (gaps + recomendacoes).
- Brief para custom enterprise font (top tier).

---

**Disclaimer educacional**: Esta skill apresenta panorama 2026 de tipografia corporativa baseado em fontes publicas, articles trade press, documentacao W3C/WCAG, foundries publicas, e cases publicamente documentados (IBM Plex github, Apple SF Pro developer docs, Klim/Stripe articles, Dalton Maag case studies). NAO constitui aconselhamento legal sobre licenciamento de fontes especificas — sempre consultar EULA da foundry diretamente e advogado de IP para uso enterprise. Precos mencionados sao estimativas baseadas em pesquisas publicas e podem variar. Custom enterprise fonts (Apple SF, Spotify Circular, etc) sao mencionadas como cases educacionais — uso requer license direta com Apple Developer / Lineto / etc. Estatisticas citadas (15-20% palavras pt-BR mais longas, 5-10% populacao com dislexia) provem de fontes academicas / trade (IDA, Sciencedirect) — consultar fontes originais para precisao. Volatilidade media: revisar a cada 6 meses dado movimento de variable fonts, mudancas EULA AI-training, e evolucao W3C CSS Fonts Level 4/5.
