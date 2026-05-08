---
name: composicao-visual
description: "Composicao visual aplicada a marketing — fundacao para `geracao-imagens-ia` + `infograficos-diagramas`. **Teoria de cores** (color wheel, complementares/analogas/triadicas, psicologia: blue trust/red urgency/green growth/black luxury — +80% brand recognition com cor consistente; **2026 trend earth tones autenticos** > bright greens em sustentabilidade; geo-targeting cultural BR/Asia/EU diferente). **Tipografia 2026**: variable fonts = baseline (1 file multi-weight), serif return premium/editorial, typography como hero image (nao neutral carrier), kinetic/3D/expressive, **acessibilidade > ornamentacao**. **Hierarquia visual**: size + contrast + alignment + white space + proximity + cues; mobile exige prioritizacao mais forte. **Fotografia**: rule of thirds (9 segments equal), **golden ratio 1:1.618** (unequal natural), golden spiral (nautilus-like), framing, leading lines, simetria, perspectiva. **Gestalt principles** (proximity, similarity, closure, continuity, figure/ground, symmetry/Pragnanz). **Vector vs Bitmap profundo**: SVG (escalavel codigo) vs PNG (loseless raster) vs JPG (lossy compressao) vs WebP (Google modern) vs AVIF (best compression 2026). **Avatares + mascotes 2026** — **Duolingo case** ($100M+ value, 3D + personality > aesthetics, internet-native, consistente). Brand consistency: 60-30-10 paleta, 2-3 fontes max. Acessibilidade WCAG 2.x (contrast 4.5:1 normal, 3:1 large). Mobile-first composition. Anti-patterns: 5+ cores ruido, 4+ fontes Frankenstein, ignorar mobile breakpoints, mascote sem personalidade."
user-invocable: false
last_verified: 2026-05-08
next_review: 2026-11-08
volatility: medium
regrounding_sources:
  - "https://www.w3.org/WAI/standards-guidelines/wcag/"
  - "https://material.io/design/color"
  - "https://www.figma.com/resource-library/gestalt-principles/"
  - "https://ixdf.org/literature/topics/visual-hierarchy"
  - "https://www.fontfabric.com/blog/10-design-trends-shaping-the-visual-typographic-landscape-in-2026/"
  - "https://memorable.design/brand-typography-trends/"
---

# Skill: composicao-visual

> **Decaimento Temporal**
> Ultima verificacao: 2026-05-08 | Proxima revisao: 2026-11-08 | Volatility: **medium** (6 meses)
> Principios fundamentais (Gestalt, rule of thirds, hierarquia) sao estaveis ha decadas. Trends visuais (cores, tipografia) ciclicos. WCAG atualiza periodicamente. **Re-validar antes de publicar peca formal:**
> - WCAG (acessibilidade) — https://www.w3.org/WAI/standards-guidelines/wcag/
> - Material Design (Google) — https://m3.material.io
> - Figma Resource Library — https://www.figma.com/resource-library
> - Interaction Design Foundation — https://ixdf.org
> - Fontfabric Trends 2026 — https://www.fontfabric.com/blog/10-design-trends-shaping-the-visual-typographic-landscape-in-2026/
> - Memorable Design Typography 2026 — https://memorable.design/brand-typography-trends/
>
> **Acionamento:** decisao paleta cores brand; tipografia brand; hierarquia visual em landing/post/email; composicao fotografia/foto IA-gen; mascote/avatar criacao; WCAG acessibilidade; mobile vs desktop layout; vector vs bitmap decision profundo; design system cores+fonts.
> **Skills relacionadas:** `geracao-imagens-ia` (anterior — bitmap/vector + brand consistency), `infograficos-diagramas` (anterior — Mermaid/PlantUML + visual builders), `audio-musica-ia` (proxima — counterpart audio), `seo-on-page` (image SEO + WCAG accessibility), `instagram-feed-reels` + `linkedin-organico` (visual identity em social), `branding`, `compliance-lgpd` (acessibilidade WCAG e tema regulatory).
> **Pre-requisito:** `geracao-imagens-ia` ajuda contexto de output IA; `infograficos-diagramas` ajuda contexto data viz.

---

## 1. Visao Geral

Composicao visual e a **fundacao oculta** de marketing visual em 2026 — IA gera imagens, mas e composicao que distingue **marca premium** de **marca generica**. Brands com cores+tipografia+hierarquia consistentes tem **+80% brand recognition**. **Duolingo Duo** virou ativo de **$100M+ valuation** porque mascote + personalidade + composicao foram trabalhados com rigor por anos.

Esta skill cobre 6 fundacoes:

1. **Teoria de cores** + psicologia + cultura BR.
2. **Tipografia 2026** — variable fonts, serif return, type-as-hero.
3. **Hierarquia visual** — size, contrast, alignment, white space, proximity.
4. **Fotografia** — rule of thirds, golden ratio, golden spiral, framing.
5. **Gestalt principles** — proximity, similarity, closure, continuity, figure/ground, symmetry.
6. **Vector vs Bitmap profundo** — SVG/PNG/JPG/WebP/AVIF + quando cada.

Mais 2 aplicacoes praticas:

7. **Avatares + mascotes** — Duolingo case + design 2026.
8. **Acessibilidade WCAG 2.x** — contrast ratios, color blindness, mobile-first.

### 1.1 Acionamento

| Gatilho | Exemplo |
|---------|---------|
| Definir paleta brand | "marca novo SaaS B2B fintech — paleta?" |
| Tipografia brand | "tipografia para fintech premium — qual?" |
| Hierarquia landing page | "landing converte mal — diagnosticar visual" |
| Mascote/avatar | "criar mascote pet shop estilo Duolingo" |
| Vector vs bitmap | "logo escalavel VS social post — qual?" |
| WCAG accessibility | "contrast ratio do CTA esta OK?" |
| Mobile breakpoints | "layout quebra em mobile — fix?" |
| Design system | "documentar tokens cores+fonts da marca" |
| Brand audit | "marca parece generica — audit visual?" |

### 1.2 Pre-requisitos

- [ ] **Brand brief minimo** (segmento, audiencia, valores).
- [ ] **Ferramentas**: Figma (free tier OK), Adobe Color (color palette), Coolors.co, Google Fonts.
- [ ] **WCAG checker** — WebAIM Contrast Checker (free).
- [ ] **Mobile testing** — Chrome DevTools responsive mode.
- [ ] **Geracao de imagens IA** se applicavel (cf. `geracao-imagens-ia`).

> **Cristal C0 — NAO CHUTAR.** Cor "bonita" sem proposito = vaidade. Tipografia "moderna" sem readability = fail acessibilidade. Hierarquia "criativa" sem prioritizacao = caos. Re-validar com dados (heatmap, A/B test, WCAG checker).

---

## 2. Teoria de cores aplicada

### 2.1 Color wheel basico

```
PRIMARIAS:    Vermelho - Azul - Amarelo
SECUNDARIAS:  Verde (azul+amarelo) - Laranja (vermelho+amarelo) - Roxo (azul+vermelho)
TERCIARIAS:   Misturas vizinhas
```

### 2.2 Esquemas de cor

| Esquema | Como funciona | Uso |
|---------|---------------|-----|
| **Monocromatico** | 1 cor + variacoes (claro/escuro/saturacao) | Minimalist, premium, calmo |
| **Analogo** | 3 cores adjacentes no wheel | Harmonia natural, suave |
| **Complementar** | 2 cores opostas | Alto contraste, vibrante (cuidado: cansativo se excesso) |
| **Triadico** | 3 cores equidistantes | Vibrante balanceado |
| **Split-complementar** | 1 base + 2 vizinhas da complementar | Contraste sem stress |
| **Tetradico** | 4 cores em retangulo | Rich palette (dificil balancear) |
| **Quadrado** | 4 cores equidistantes | Maxima diversidade |

### 2.3 Psicologia de cores — fundamentos

```
COR        EMOCAO PRIMARIA            USO TIPICO
=========  ========================   ========================
VERMELHO   Urgencia, paixao, perigo   Sales, food (apetite), CTA "Compre"
AZUL       Confianca, calma, tech     Bancos, SaaS B2B, healthcare
VERDE      Crescimento, natureza,$    Fintech, sustainability, money
AMARELO    Otimismo, atencao, energia Children, fast food, deals
LARANJA    Entusiasmo, criatividade   Brand jovem, food, sports
ROXO       Luxo, mistério, criativo   Beauty premium, mistico
ROSA       Feminino, romantic, fun    Beauty, fashion, gen Z
PRETO      Luxo, poder, sofisticacao  Luxury brands, fashion alta
BRANCO     Pureza, simplicidade       Apple, minimalist, healthcare
CINZA      Neutralidade, tech         Background, body text
MARROM     Terra, autenticidade       Eco brands, food artisan
```

### 2.4 Trends 2026 — cores especificas

```
EARTH TONES AUTENTICOS substituem bright greens em sustentabilidade
   - Bege #C9A86E
   - Verde-musgo #6B8E4E
   - Marrom-terra #7D5A3C

DIGITAL LAVENDER (Pantone influence)
   - #B57EDC, #E0AAFF — feminino moderno

BOLD GRADIENTS (multi-color flows)
   - Instagram-style gradients
   - Spotify Wrapped aesthetic

DARK MODE FRIENDLY
   - Cores que funcionam tanto light quanto dark
   - Avoid pure white (#FFFFFF) → preferir off-white #FAFAFA
   - Avoid pure black (#000000) → preferir near-black #1A1A1A
```

### 2.5 Cor + cultura (geo-targeting)

```
MESMA COR, EMOCAO DIFERENTE POR CULTURA

VERMELHO
   Asia: sorte, prosperidade (China, Japao)
   Ocidente: perigo, paixao
   Africa do Sul: luto

BRANCO
   Ocidente: pureza, casamento
   Asia: luto

VERDE
   Ocidente: natureza, dinheiro (USA)
   Islam: cor sagrada
   Brasil: relacao com bandeira (positivo)

ROXO
   Brasil: luto (catolico)
   Tailandia: viuvas
   Ocidente: realeza, luxo

CONTEXTO BRASIL
   - Verde + amarelo = bandeira (cuidado nacionalismo)
   - Azul + branco + vermelho = patriotico genérico
   - Verde-musgo (terra) emergente em sustentabilidade
   - Magenta/rosa choque = popular pos-2020 (Y2K revival)
```

### 2.6 Paleta brand — formula 60-30-10

```
ESTRUTURA PALETA SAUDAVEL

60% COR PRIMARIA (background, body text)
   - Tipicamente neutral (white/off-white/gray/black)

30% COR SECUNDARIA (sections, accents grandes)
   - Brand color principal

10% COR ACCENT (CTA, highlights)
   - Cor mais vibrante que chama acao

EXEMPLO B2B SaaS premium:
   60% #FAFAFA (off-white background)
   30% #1A2E4F (azul navy — brand color)
   10% #FF6B35 (laranja vibrante — CTAs)

EXEMPLO Skincare clean:
   60% #F5F0E8 (cream)
   30% #4A6741 (verde-sage)
   10% #D4A574 (gold — premium)

EXEMPLO Fintech jovem:
   60% #FFFFFF
   30% #6C5CE7 (purple-tech)
   10% #00CEC9 (teal — accent)
```

### 2.7 Color blindness consideration

8% homens + 0.5% mulheres tem alguma forma. **Mais comum**: deuteranomaly (vermelho-verde).

```
NAO CONFIAR APENAS EM COR PARA TRANSMITIR INFO

Ruim: "Click no botao verde para confirmar"
Bom: "Click no botao verde 'Confirmar'" (texto + cor)

Ruim: Grafico com bars vermelha/verde sem labels
Bom: Bars com labels + texturas diferentes
```

Tools: Coblis (Color Blindness Simulator), Stark (Figma plugin).

---

## 3. Tipografia 2026

### 3.1 Trends 2026

```
1. VARIABLE FONTS = BASELINE EXPECTATION
   - 1 arquivo, multiplos weights/widths/styles
   - Performance web superior (download menor)
   - Animacao smooth de weight (kinetic type)
   - Ex.: Inter Variable, Roboto Flex, Recursive

2. SERIF RETURN
   - Confianca, autoridade, editorial
   - Premium branding 
   - Ex.: Editorial New, Newsreader, Source Serif Pro
   - vs sans-serif "tech" overuse 2010-2020

3. TYPOGRAPHY AS HERO IMAGE
   - Type nao e mais "neutral carrier" — e o protagonista
   - Bold, oversized, expressive
   - Substitui hero photo em alguns casos

4. KINETIC + 3D + ANIMATED
   - Web animacoes type-driven (CSS + variable fonts)
   - 3D rendered text para social
   - Subtle hover states em web

5. RESPONSIVE TYPOGRAPHY
   - Fluid font sizes (clamp() CSS)
   - Adaptam a viewport sem breakpoints rigidos
   
6. ACESSIBILIDADE > ORNAMENTACAO
   - Mobile-readability mandatory
   - Min 16px body text web
   - Min 14pt body print
```

### 3.2 Sistema tipografico saudavel

```
SISTEMA MINIMO 2-3 FONTES MAX

OPCAO A — Mono-typeface (1 familia variable):
   Inter Variable (display + body + UI)

OPCAO B — Pair classico (2 famílias):
   - Display: serif premium (Newsreader)
   - Body: sans-serif legivel (Inter)

OPCAO C — Triade (3 famílias):
   - Display: serif/script
   - Body: sans-serif
   - Mono: codigo/dados (JetBrains Mono, Fira Code)

NUNCA: 4+ fontes diferentes (Frankenstein)
```

### 3.3 Type scale

```
SISTEMA 1.250 (Major Third) — comum web

H1: 48px (3rem)
H2: 38px (2.4rem)
H3: 30px (1.9rem)
H4: 24px (1.5rem)
H5: 20px (1.25rem)
Body: 16px (1rem)
Small: 13px (0.8rem)

MOBILE — escalar para baixo:
H1: 32px
H2: 26px
... etc
```

### 3.4 Pairing fonts — regras

```
COMBINAR FONTES — 3 abordagens

1. CONTRASTE FORTE (display vs body)
   Display: Serif chunky (Caslon, Editorial New)
   Body: Sans-serif clean (Inter, Helvetica Now)

2. MESMA FAMILIA (variable font)
   Display: Inter Bold 800
   Body: Inter Regular 400
   = consistencia maxima

3. SUPERFAMILY (mesmo designer, escalas combinadas)
   IBM Plex Sans + IBM Plex Serif + IBM Plex Mono
   = perfeitamente coerentes
```

### 3.5 Fontes recomendadas 2026 (Google Fonts gratis)

```
SANS-SERIF (body + UI):
   - Inter, Inter Variable (mais usado em SaaS)
   - Manrope (round, warm)
   - DM Sans (clean, popular)
   - Plus Jakarta Sans (modern, elegant)
   - Geist (Vercel-popular)

SERIF (display + premium):
   - Newsreader (variable, modern serif)
   - Editorial New (premium feel)
   - Source Serif Pro (Adobe, classic)
   - Fraunces (variable, expressive)

DISPLAY/BRAND:
   - Bricolage Grotesque (variable, contemporary)
   - Space Grotesque (geometric)
   - Clash Display (chunky display)

MONO (code/data):
   - JetBrains Mono
   - Fira Code (with ligatures)
   - IBM Plex Mono
```

### 3.6 Acessibilidade tipografica

```
WCAG 2.x REQUIREMENTS

LINE HEIGHT:
   - Body: 1.5x font size minimo
   - Headings: 1.2x

LINE LENGTH:
   - Body: 50-75 caracteres (~ 8-12 palavras/linha)
   - Mais que 75 = dificulta scan visual

PARAGRAFO SPACING:
   - Min 1.5x line-height entre paragrafos
   - White space respira

TEXT CONTRAST (Sec 8 abaixo):
   - Body text: 4.5:1 contraste com fundo
   - Large text (18pt+): 3:1
   - UI text: 4.5:1

NUNCA:
   - Justify text em web (gaps irregulares)
   - All caps em paragrafos longos
   - Italic blocks longos (cansa leitura)
   - Centered text em paragrafos (so headings)
```

---

## 4. Hierarquia visual

### 4.1 Os 6 principios de hierarquia

```
1. SIZE
   Maior = mais importante
   H1 > H2 > H3 > body

2. CONTRAST
   Cor diferente = focal point
   CTA vs background

3. ALIGNMENT
   Estrutura = ordem cognitiva
   Left-align text scan natural

4. WHITE SPACE (negative space)
   Vazio = respiro = hierarquia
   Premium brands usam BASTANTE white space

5. PROXIMITY
   Coisas relacionadas juntas
   (ver Gestalt Sec 6)

6. CUES (visual cues)
   Setas, icones, lines
   Guiam olhar
```

### 4.2 F-pattern + Z-pattern (eye scanning)

```
F-PATTERN — texto-heavy (artigos, blogs)
   _____________
   |1111111111|       Lê primeira linha completa
   |2222         |    Pula meio na esquerda
   |3____        |    Scan vertical esquerda
   |4_           |
   |5            |
   _____________

Z-PATTERN — landing pages (visual + text)
   _____________
   |1__________2|     Top esquerda → top direita
   |    \    /  |
   |     \  /   |     Diagonal centro
   |      \/    |
   |3__________4|     Bottom esquerda → bottom direita
   _____________

COLOCAR ELEMENTOS-CHAVE NESTES PONTOS:
   - Logo top-left (1)
   - CTA principal top-right (2) ou bottom-right (4)
   - Value prop centro (Z) ou esquerda (F)
```

### 4.3 Mobile vs Desktop

```
MOBILE EXIGE PRIORITIZACAO MAIS FORTE

Desktop:               Mobile:
- 5-7 elementos OK   - 1-3 elementos por viewport
- Sidebars OK        - Single column
- Hover states       - Touch targets 44×44px min (iOS) / 48×48px (Android)
- Larger spacing     - Menor spacing mas SUFICIENTE
- Multi-column       - Stack vertical

VIEWPORTS COMUNS 2026:
- Mobile: 320-414px (iPhone Mini → iPhone Plus)
- Tablet: 768-1024px (iPad)
- Desktop small: 1280-1440px
- Desktop large: 1920px+
- Ultra-wide: 2560px+
```

### 4.4 Anti-patterns hierarquia

| Anti-pattern | Por que falha |
|--------------|---------------|
| Tudo bold | Nada se destaca |
| Tudo grande | Sem hierarquia |
| Tudo colorido | Caos visual |
| Sem white space | Pesado, cansativo |
| Multiplos CTAs same prominence | Usuario nao sabe escolher |
| Centralized everything | F-pattern quebrado |
| Mobile sem prioritizacao | Scroll infinito ou pinch zoom |

---

## 5. Composicao em fotografia

### 5.1 Rule of Thirds (regra dos tercos)

```
DIVIDIR FRAME EM 9 PARTES IGUAIS

   |     |     |
   1     2     3
   |     |     |
---+-----+-----+---
   |     |     |
   4     5     6
   |     |     |
---+-----+-----+---
   |     |     |
   7     8     9
   |     |     |

POSICIONAR ELEMENTOS-CHAVE NAS 4 INTERSECCOES
   - Olho de retrato em interseccao superior
   - Horizonte em linha 1/3 (não centralizado)
   - Subject em 1/3 esquerda ou direita
   - Evitar centralizar TUDO

WORKS WITH:
   - Smartphones (grid built-in nas cameras)
   - DSLR
   - Frame composition de IA-generated images
```

### 5.2 Golden Ratio (1:1.618)

```
DIVISAO MAIS NATURAL/ORGANICA

Phi (φ) = 1.618...

Encontrado na natureza:
   - Concha de nautilus
   - Espiral de DNA
   - Petalas de flores
   - Galaxias

vs Rule of Thirds:
   Rule of Thirds: divisoes iguais (mais simples)
   Golden Ratio:   divisoes desiguais (mais natural)

GOLDEN SPIRAL:
   - Espiral gerada por golden ratio
   - Coloca subject no "olho do furacao"
   - Cria sensacao de movimento e profundidade
```

### 5.3 Outros frameworks

```
LEADING LINES (linhas guia)
   Linhas naturais (estrada, rio, escada) que LEVAM o olho ao subject

FRAMING (enquadramento dentro do frame)
   Subject visto atraves de janela/arco/galhos
   Cria moldura natural

SYMMETRY (simetria)
   Reflexo, formacao mirror
   Forte impacto visual mas pode ser estatico

PERSPECTIVA (depth)
   Foreground + middleground + background
   Adicionar dimensao 3D em foto 2D

NEGATIVE SPACE (espaco negativo)
   Subject pequeno em vasta area vazia
   Premium feel, minimalist

PATTERNS + REPETITION
   Repeating elements (windows, columns, leaves)
   Visual rhythm

FILL THE FRAME
   Subject dominate frame (close-up)
   Intimidade, detalhe
```

### 5.4 Aplicacao em IA-generated images

```
PROMPT MIDJOURNEY/IMAGEN COM REGRA COMPOSICAO

EXEMPLO RULE OF THIRDS:
"Female founder, rule of thirds composition, subject at 
left-third intersection, soft natural light from window 
right, modern office background"

EXEMPLO GOLDEN RATIO:
"Product photography of perfume bottle, golden ratio 
spiral composition, bottle at focal point, gradient 
background"

EXEMPLO LEADING LINES:
"Aerial shot of road through mountains, leading lines 
guide eye to distant city in horizon, dramatic sky"

PARAMETROS MIDJOURNEY UTEIS:
   --ar 16:9 (paisagem)
   --ar 4:5 (Instagram feed)
   --ar 9:16 (Stories/Reels)
   --ar 1:1 (square classic)
```

---

## 6. Gestalt Principles

### 6.1 Os 6 principios fundamentais

#### Proximity (proximidade)

```
ELEMENTOS PROXIMOS = RELACIONADOS

Forma intuitiva de agrupar:
   Form fields agrupados por seçao
   Botoes "Cancel + OK" juntos
   Card components com label proximo

EXEMPLO:
   ❌ Label muito longe do input field
   ✅ Label colado ao input field

WHITE SPACE entre grupos = separacao
WHITE SPACE dentro do grupo = unidade
```

#### Similarity (similaridade)

```
ELEMENTOS PARECIDOS = MESMO GRUPO

Cor, shape, size, texture:
   Itens menu mesma cor = navegacao
   Cards mesma altura = produtos
   Icons mesmo style = funcionalidades

EXEMPLO:
   ❌ Botoes com cores aleatorias
   ✅ Primary buttons todos azuis, secondary todos cinza
```

#### Closure (fechamento)

```
CEREBRO COMPLETA SHAPES INCOMPLETOS

Brain fills in the gaps:
   Logos com partes faltantes (Adidas trefoil, IBM)
   Icons abstratos
   Loading spinners (circulo nao-fechado)

EXEMPLO:
   Logo da WWF (panda formado por shapes pretas e brancas)
   Logo NBC (paveao com 6 cores)
```

#### Continuity (continuidade)

```
OLHO SEGUE CAMINHO MAIS FACIL

Linhas, curvas, alinhamentos:
   Texto numa linha (nao quebra meio)
   Charts conectam pontos
   Carrossel de fotos

EXEMPLO:
   ❌ Lista bagunçada com items deslocados
   ✅ Lista alinhada esquerda, scan visual rapido
```

#### Figure/Ground (figura/fundo)

```
SEPARACAO ENTRE OBJETO + FUNDO

Foreground vs background:
   Subject claro contra fundo escuro
   CTA destacado contra background neutro
   Modal sobre overlay escuro

EXEMPLO:
   ❌ Texto dark sobre photo dark = ilegivel
   ✅ Texto dark sobre overlay claro/branco
```

#### Symmetry / Pragnanz (simplicidade)

```
CEREBRO PREFERE SIMPLES E SIMETRICO

Lei de Pragnanz: organizamos visualmente para mais simples possivel

EXEMPLO:
   Logo abstrato e LEMBRADO mais facil que detalhado
   UI simetrica = balanced, professional
   Asymetric pode ser dynamic mas exige cuidado
```

### 6.2 Aplicacao em UI

```
PROXIMITY → form sections
SIMILARITY → consistent buttons / cards
CLOSURE → minimalist logos / icons
CONTINUITY → flows + lists alignment
FIGURE/GROUND → CTA destaque
SYMMETRY → simple, memorable design
```

---

## 7. Vector vs Bitmap profundo

(Cross-ref `geracao-imagens-ia` Sec 5)

### 7.1 Vector formats

| Formato | Caracteristicas | Use case |
|---------|-----------------|----------|
| **SVG** | XML-based, scalable, browser-native | Web, logos, icons, charts |
| **AI** (Adobe Illustrator) | Editavel pro, .ai proprietary | Professional design |
| **EPS** | PostScript-based, print legacy | Print pre-production |
| **PDF** | Misto vector+bitmap+text | Print + digital docs |

**SVG e o REI 2026** — universal, browser-native, editavel via codigo, animavel via CSS/JS.

### 7.2 Bitmap formats

| Formato | Compressao | Best for | File size |
|---------|------------|----------|----------|
| **PNG** | Loseless | Graphics, transparency, screenshots | Maior |
| **JPG/JPEG** | Lossy | Fotos, sem transparency | Medio |
| **WebP** (Google) | Lossy/Loseless | Web modern, transparency | Menor que PNG |
| **AVIF** | Lossy/Loseless | Web 2026 best, transparency | **Menor 30-50% vs WebP** |
| **GIF** | Lossy | Animacao simples (legacy) | Variavel |
| **HEIF/HEIC** | Lossy modern | iPhone photos | Menor que JPG |

### 7.3 AVIF — vencedor 2026

```
AVIF vs WEBP vs JPG (mesma imagem photo)

JPG:    100 KB
WebP:   60 KB (40% menor)
AVIF:   30 KB (70% menor, 50% menor que WebP)

QUALIDADE:
   AVIF qualidade superior em mesmo file size
   
SUPORTE 2026:
   Chrome, Firefox, Safari ✅
   IE, navegadores legacy ❌

WORKFLOW:
   <picture>
     <source srcset="hero.avif" type="image/avif">
     <source srcset="hero.webp" type="image/webp">
     <img src="hero.jpg" alt="Hero">
   </picture>
```

### 7.4 Decision matrix completa

| Use case | Formato recomendado |
|----------|---------------------|
| Logo brand | **SVG** |
| Icon set | **SVG** |
| Hero photo web | **AVIF** + WebP fallback + JPG legacy |
| Product photo e-commerce | **AVIF** ou WebP |
| Screenshot UI | **PNG** (loseless) ou WebP |
| Photo Instagram post | **JPG** (Instagram converte) |
| Photo print | **PDF** ou TIFF (high quality) |
| Animacao simples | **WebP animado** ou **APNG** (legacy GIF) |
| Animacao complexa | **MP4 video** |
| Diagrama tecnico | **SVG** (Mermaid output) |
| Chart data viz | **SVG** (escalavel) |
| Avatar profile | **AVIF** + WebP fallback |

### 7.5 Compressao bitmap — quando

```
LOSELESS — manter cada pixel original
   - Screenshots UI
   - Logos PNG
   - Texto em imagem
   - Necessario fidelidade absoluta

LOSSY — remove dados imperceptiveis para reduzir size
   - Fotos em geral
   - Hero images
   - Backgrounds
   - File size critico
   
QUALITY SETTING (JPG/WebP):
   95-100: maximum, file gigante
   80-90: high quality, balanced
   70-80: medium, social media OK
   50-70: low, evitar
   <50: pixelated artifacts visiveis
```

---

## 8. Acessibilidade visual — WCAG 2.x

### 8.1 Contrast ratios obrigatorios

```
WCAG 2.1 AA (padrao moderno)

NORMAL TEXT:
   Body: 4.5:1 minimo
   
LARGE TEXT (18pt+ ou 14pt+ bold):
   3:1 minimo

UI COMPONENTS + GRAPHICAL OBJECTS:
   3:1 minimo

WCAG 2.1 AAA (mais rigoroso):
   Normal: 7:1
   Large: 4.5:1

TOOLS:
   - WebAIM Contrast Checker (free)
   - Stark plugin Figma
   - Chrome DevTools Lighthouse
```

### 8.2 Examples

```
PASS:
   #FFFFFF background + #1A1A1A text = 17.85:1 (AAA)
   #1A2E4F navy + #FFFFFF text = 11.5:1 (AAA)
   #6C5CE7 purple + #FFFFFF text = 5.7:1 (AA)

FAIL:
   #FAFAFA background + #CCCCCC text = 1.6:1 ❌
   #6C5CE7 + #FFD43B yellow text = 2.1:1 ❌
```

### 8.3 Color blindness — testar

```
TIPOS COMUNS:
   Deuteranomaly (verde-vermelho fraco) — 6% homens
   Protanomaly (vermelho fraco) — 1%
   Tritanomaly (azul-amarelo) — raro
   
TESTAR:
   - Coblis Color Blindness Simulator (free online)
   - Stark plugin Figma
   - Chrome DevTools "Emulate vision deficiencies"

REGRA:
   NUNCA confiar APENAS em cor para transmitir info
   - Adicionar texto labels
   - Adicionar icons/symbols
   - Adicionar texturas/patterns
```

### 8.4 Mobile-first composition

```
PRIORIZACAO MAX EM MOBILE:

VIEWPORT ~375px (iPhone SE/Mini):
   - 1-3 elementos por viewport
   - CTA grande (44×44 minimo iOS, 48×48 Android)
   - Body 16px+ (NUNCA abaixo)
   - Headings escaladas para mobile
   - White space generoso (not crowded)
   - Single column layout
   - Sticky CTA / nav considerado

DESKTOP ~1440px:
   - Multi-column OK
   - Sidebars OK
   - Hover states
   - Larger imagery OK
```

---

## 9. Avatares + mascotes — Duolingo case

### 9.1 Por que mascotes voltaram

```
2010-2020: minimalist trend, mascotes desapareceram
2020-2026: brand personality return, mascotes RIPPING IT

Razoes:
   - Social media exige personalidade memoravel
   - AI/generic content = brands precisam diferencial humano
   - Gen Z valoriza autenticidade e quirkiness
   - Memes precisam character recognizable
```

### 9.2 Duolingo Duo case (US$ 100M+ value mascote)

```
EVOLUCAO DUO

2011: 2D simple owl mascot (bird basic)
   ↓
2018: Refresh — friendlier, dynamic
   ↓
2022: 3D, full-bodied, brighter colors
   ↓
2024: Internet-native personality (passive-aggressive owl meme)
   ↓
2026: "More famous than Mickey Mouse" (Fast Company)
   - Worth hundreds of millions to company
   - Cross-platform consistency (TikTok, IG, X)
   - Memes self-perpetuated
   - Killed mascot stunt (2025) viral globally
```

### 9.3 Componentes de mascote 2026 vencedor

```
1. PERSONALITY > AESTHETICS
   Duo: passive-aggressive, threatening, lovable contradition
   Geico Gecko: posh British charm
   M&M characters: distinct personalities per cor
   
2. CONSISTENCY ACROSS YEARS
   Reconhecivel mesmo com refreshes visuais
   
3. INTERNET-NATIVE
   Funciona em meme format
   Reage a trends do momento
   Postar em redes como pessoa real
   
4. EMOTIONAL ATTACHMENT
   Audiencia "sente" o mascote
   Defesa do mascote em controversia
   
5. STORY-DRIVEN
   Backstory, evolution, milestones
   Episodes (TikTok narratives)
```

### 9.4 Quando vale criar mascote

```
SIM SIM:
   - Brand precisa personalidade distinta
   - Audiencia jovem (16-40)
   - Categoria saturated (precisa diferencial)
   - Budget para sustentar character por anos
   - Time interno disposto a evoluir
   - Setor onde personality = differentiator

NAO:
   - B2B enterprise super-formal (banco, advocacia)
   - Sem budget para sustentar (mascote abandoned = pior que nenhum)
   - Brand muito jovem (foco em product-market fit primeiro)
   - Cultura interna avessa a quirkiness
```

### 9.5 Workflow criar mascote

```
1. CHARACTER BIBLE (3-5 dias)
   - Especies/tipo (animal, humano, abstrato?)
   - Personalidade (3 traits primarios)
   - Voz (formal? casual? sarcastic?)
   - Backstory
   - Brand connection

2. VISUAL DESIGN (2-4 semanas)
   - Style guide (color palette, proportions)
   - Multiple poses (5-10 inicial)
   - Multiple expressions (feliz, triste, surpreso, irritado)
   - Multiple outfits (diferentes cenarios)
   - 3D modeling se aplicavel (Blender)

3. CONTENT STRATEGY (continuous)
   - 2-3 posts/semana onde mascote aparece
   - Calendario seasonal (Halloween, Black Friday, etc.)
   - Reactivos a trends
   - UGC potential (fans criam content)

4. EVOLUTION (anos)
   - Refreshes visuais a cada 3-5 anos
   - Personalidade se aprofunda
   - Backstory expands
   - Cross-media (animação, video, podcast)
```

### 9.6 Tools 2026 para mascote

```
GERACAO INICIAL:
   - Midjourney v7 com --oref para character consistency
   - DALL-E / GPT Image 1.5
   - Adobe Firefly (IP indemnification)
   
MODELING 3D:
   - Blender (free)
   - Cinema 4D
   - Spline (web-based 3D)

ANIMACAO:
   - After Effects (industry standard)
   - Cavalry (motion design)
   - Rive (interactive web animations)

VOICE/AUDIO:
   - ElevenLabs (voz consistent character)
   - Murf.ai
   - Eleven Voice Lab (treinar voice proprio)
```

---

## 10. Anti-patterns composicao

| Anti-pattern | Por que falha |
|--------------|---------------|
| **Paleta com 5+ cores** | Visual noise, sem foco |
| **4+ fontes Frankenstein** | Quebra coerencia brand |
| **Tudo bold** | Nada destaca |
| **Hover em mobile** (no touch) | Funcionalidade invisivel |
| **CTAs <44×44px touch target** | iOS rejeita por acessibilidade |
| **Body text <16px web** | Mobile-unreadable |
| **Contrast <4.5:1 body** | Falha WCAG AA |
| **Cor sozinha para info** | Color blindness fail |
| **Justify text web** | Gaps irregulares feiosos |
| **All caps em body longo** | Cansa leitura |
| **Italic block longo** | Cansa leitura |
| **Photo sem alt text** | SEO + acessibilidade fail |
| **JPG para logo** | Perde qualidade scaling — usar SVG |
| **PNG para photo grande** | File enorme — usar AVIF/WebP |
| **Mascote one-shot sem evolucao** | Wasted investment |
| **Mascote inconsistente entre canais** | Confusao brand |
| **Centralizar TUDO** | F/Z pattern quebrado |
| **No white space** | Pesado, premium-killer |
| **Cores fluorescentes em B2B premium** | Mismatch tom |

---

## 11. Workflow operacional — design system

```
CRIAR DESIGN SYSTEM (4-8 SEMANAS)

WEEK 1 — DISCOVERY
   [ ] Brand audit visual existente
   [ ] Persona/audiencia review
   [ ] Competitor visual benchmarking
   [ ] Mood board (Pinterest/Figma)

WEEK 2-3 — CORES
   [ ] Color palette 60-30-10
   [ ] Tokens (primary, secondary, accent, neutral, semantic)
   [ ] Dark mode variations
   [ ] Acessibility WCAG check todas combinacoes
   [ ] Document em Figma + JSON tokens

WEEK 3-4 — TIPOGRAFIA
   [ ] Pair fonts (display + body)
   [ ] Type scale (H1-H6 + body + caption)
   [ ] Mobile vs desktop scales
   [ ] Line-heights, letter-spacing
   [ ] Responsive (clamp() CSS)

WEEK 5-6 — COMPONENTS
   [ ] Buttons (primary, secondary, tertiary, danger)
   [ ] Form fields (input, select, checkbox, radio)
   [ ] Cards
   [ ] Navigation
   [ ] Modals
   [ ] Estados (default, hover, focus, disabled, error)

WEEK 7-8 — DOCUMENTATION + ROLLOUT
   [ ] Design system docs (Storybook, Zeroheight)
   [ ] Code tokens (CSS variables, Tailwind config)
   [ ] Migration plan paginas existentes
   [ ] Team training
```

### 11.1 Tokens example (CSS variables)

```css
:root {
  /* COLORS — 60/30/10 */
  --color-primary-bg: #FAFAFA;
  --color-secondary: #1A2E4F;
  --color-accent: #FF6B35;
  --color-text-default: #1A1A1A;
  --color-text-muted: #666666;
  --color-success: #10B981;
  --color-warning: #F59E0B;
  --color-danger: #EF4444;
  
  /* TYPOGRAPHY */
  --font-display: 'Newsreader', serif;
  --font-body: 'Inter Variable', sans-serif;
  --font-mono: 'JetBrains Mono', monospace;
  
  /* TYPE SCALE */
  --text-xs: 0.75rem;
  --text-sm: 0.875rem;
  --text-base: 1rem;       /* 16px */
  --text-lg: 1.25rem;
  --text-xl: 1.5rem;
  --text-2xl: 1.875rem;
  --text-3xl: 2.25rem;
  --text-4xl: 3rem;
  
  /* SPACING (8pt grid) */
  --space-1: 0.5rem;       /* 8px */
  --space-2: 1rem;         /* 16px */
  --space-3: 1.5rem;       /* 24px */
  --space-4: 2rem;         /* 32px */
  
  /* RADIUS */
  --radius-sm: 0.25rem;
  --radius-md: 0.5rem;
  --radius-lg: 1rem;
  --radius-full: 9999px;
}
```

---

## 12. Templates rapidos

### 12.1 Paleta brand B2B SaaS premium

```
PRIMARY:    #1A2E4F (azul navy — trust)
SECONDARY:  #00B894 (verde-tech — growth)
ACCENT:     #FF6B35 (laranja — CTA)
NEUTRAL:    #FAFAFA (background)
TEXT:       #1A1A1A (body)
MUTED:      #6B6B6B (captions)
SUCCESS:    #10B981
WARNING:    #F59E0B
DANGER:     #EF4444
```

### 12.2 Paleta brand B2C lifestyle (skincare)

```
PRIMARY:    #F5F0E8 (cream — clean)
SECONDARY:  #4A6741 (verde-sage — natural)
ACCENT:     #D4A574 (gold — premium)
NEUTRAL:    #FFFFFF
TEXT:       #2C2C2C
MUTED:      #888888
```

### 12.3 Type pair classico

```
DISPLAY: Newsreader (serif premium)
BODY:    Inter Variable (sans-serif clean)
MONO:    JetBrains Mono (codigo/dados)

H1: Newsreader 48px / line 56px
H2: Newsreader 36px / line 44px
H3: Inter Bold 24px / line 32px
H4: Inter SemiBold 18px / line 28px
Body: Inter Regular 16px / line 24px
Caption: Inter Regular 14px / line 20px
```

### 12.4 Hero section template

```
[LOGO TOP-LEFT]                    [NAV TOP-RIGHT]

         [HEADLINE ENORME 48px]
         [Subhead 18px]
         
         [PRIMARY CTA]  [secondary]

         [Hero image right OU centered OU bg]

[Trust badges row]
```

---

## 13. Regras de Ouro

1. **NAO CHUTAR** — cor "bonita" sem proposito = vaidade. Tipografia "moderna" sem readability = fail. Hierarquia "criativa" sem prioritizacao = caos.
2. **60-30-10 paleta** — 60% neutral + 30% brand + 10% accent (CTA).
3. **2-3 fontes max** — variable fonts ideal (1 file multi-weight).
4. **Body text 16px+ web** — abaixo = mobile-unreadable.
5. **WCAG contrast 4.5:1 body, 3:1 large** — sempre validar com WebAIM checker.
6. **NUNCA cor sozinha para transmitir info** — color blindness affects 8% homens.
7. **Touch targets 44×44 (iOS) / 48×48 (Android)** — mobile-first.
8. **Rule of thirds default** — golden ratio para premium/organicos.
9. **Gestalt: proximity > color > size** para grupos visuais.
10. **SVG para vector (logo, icon, chart)** — AVIF/WebP para photo.
11. **Mobile exige prioritizacao mais forte** — desktop pode comportar mais.
12. **White space respira** — premium brands usam BASTANTE.
13. **Trends 2026**: variable fonts, serif return, earth tones autenticos, kinetic type.
14. **Mascote requer commitment de anos** — Duolingo case ($100M+).
15. **F-pattern texto / Z-pattern landing** — colocar elementos-chave nestes points.
16. **Cor + cultura BR**: verde+amarelo nacionalismo, magenta Y2K revival, terra autenticidade.
17. **Design system tokens** desde dia 1 — facilita scale.
18. **Iterate** — primeiro draft nunca production.

---

## 14. Exemplos comportamentais

### Exemplo 1 — "Definir paleta brand fintech B2B"

**Input:** "Vou lancar SaaS B2B fintech para founders. Que paleta de cores?"

**Resposta esperada:**

> Paleta recomendada baseada em **psicologia de cores fintech B2B 2026** + persona founder. **Razao quantitativa**: blue evokes trust + calm = ideal para financial; +80% brand recognition com cor consistente. **Paleta recomendada (60-30-10)**: (a) **PRIMARY BG 60% — #FAFAFA off-white**: clean, profissional, premium feel (vs #FFFFFF puro que e cold/Apple-overused); (b) **SECONDARY 30% — #1A2E4F navy blue**: trust + tech + sophisticated; mais distintivo que #1976D2 generic Material blue; alinhado fintech enterprise (vs sky-blue =startup pequeno); (c) **ACCENT 10% — #FF6B35 vibrant orange** OR **#00B894 emerald-green**: orange = urgency + energy (otimo CTA "Open Account") | green = growth + money + validation (alinhado fintech). Recomendo orange para CTAs, green para success states; (d) **TEXT — #1A1A1A near-black** (NAO #000000 puro — softer); (e) **MUTED — #6B6B6B** para captions/secondary text; (f) **SEMANTIC**: #10B981 success, #F59E0B warning, #EF4444 danger, #3B82F6 info. **Validacao**: (1) WCAG contrast — primary BG + text = 17.85:1 ✅ AAA; secondary navy + white text = 11.5:1 ✅ AAA; orange CTA + white text = 5.7:1 ✅ AA; (2) Color blindness test: simular Coblis — orange/green nao conflitam (orange dominant CTA, green semantic only); (3) Cultura BR: navy = patriotic-friendly mas nao chauvinist; orange = energy moderna; verde = positive (sem conflito politico). **Anti-padroes evitar**: 5+ cores ruido (your case 6 cores semantic OK porque 4 deles sao semantic-only nao decorative); fluorescent yellow/pink que parecem "B2C app gratuito" desalinhado fintech B2B premium. **Output entregave**l: design tokens em CSS variables (cf. Sec 11.1 desta skill) + Figma file com all components + paleta exportada Coolors.co/Adobe Color para refresh futuro.

**Comportamento-chave:** confirma com psicologia, oferece paleta 60-30-10 com hex codes especificos + razao por cor, validacao WCAG + color blindness + cultura BR, anti-patterns.

### Exemplo 2 — "Vale criar mascote tipo Duolingo?"

**Input:** "Pet shop em Sao Paulo. Vale criar mascote estilo Duolingo Duo?"

**Resposta esperada:**

> SIM com criterios — pet shop e categoria PRIME para mascote. **Razao**: (a) audiencia emocional (donos de pet); (b) categoria saturada (mascote = differentiator); (c) Duolingo Duo case prova ROI ($100M+ value); (d) social media demand personalidade; (e) UGC potential alto (fans postam fotos com mascote). **Workflow recomendado** (3-6 meses para character estabelecido): (1) **CHARACTER BIBLE** (1-2 semanas): especies — golden retriever (warm, family-friendly) OU mascote pet generico (gato + cachorro + passaro mascot family); personalidade 3 traits — amigavel, curioso, brincalhao; voz — entusiasta, kid-friendly mas NAO infantil (adultos compram); backstory — "encontramos esse pet de rua, virou mascote da loja"; nome memoravel curto (Duo = perfect, 1 silaba); (2) **VISUAL DESIGN** (3-4 semanas): style guide cores brand (rosa+amarelo+verde lifestyle pet?), 5-10 poses iniciais, 5+ expressoes (feliz/triste/curioso/dormindo/comendo), 3-5 outfits seasonal (Natal hat, Halloween costume, Cao do dia), considerar 3D modeling (Blender free) para flexibilidade futura, gerar via Midjourney v7 com --oref para character consistency; (3) **CONTENT STRATEGY** (continuous): 2-3 posts/sem onde mascote aparece (Stories TikTok rate +60% engagement com mascote vs sem), calendario seasonal (Mes do Pet, dia mundial dos animais), reativo a trends (mascote dancando trend TikTok); (4) **EVOLUTION** anos: refreshes a cada 3-5 anos, personality deepens, backstory expands; (5) **CROSS-PLATFORM**: mesmo mascote IG + TikTok + WhatsApp Status + site + brindes; (6) **UGC**: hashtag dedicada #[NomeMascote] para fans postarem com seus pets imitando poses. **Investimento realista**: R$ 5-15k design inicial + 3-5h/sem ongoing content management; **ROI esperado**: 12-24 meses para reconhecimento local solido; recall +40% vs marca sem mascote (estudos brand awareness). **NAO**: criar mascote sem commitment ANOS (mascote abandoned = piuor que nenhum); mascote inconsistente entre canais; mascote sem personality (so visual = generico); copiar Duo exatamente (legal risk + sem differentiation).

**Comportamento-chave:** confirma com criterios + Duolingo case ROI, oferece workflow 6 etapas, projeta investimento+ROI BR, lista anti-patterns.

### Exemplo 3 — "Hierarquia landing page convertendo mal"

**Input:** "Landing SaaS tem 1k visitas/dia mas conversao 0.5%. Suspeito visual. Como diagnosticar?"

**Resposta esperada:**

> Diagnostico hierarquia + heatmap em 5 etapas. **Hipotese principal**: hierarquia visual quebrada — usuario nao sabe **o que fazer next** em 3 segundos = bounce. Conversao SaaS B2B saudavel = 2-5% (your 0.5% e 4-10x abaixo). **Diagnostico tecnico**: (1) **Hotjar/Microsoft Clarity heatmap** (free tier suficiente) — instalar 7 dias, ver onde clicks acontecem vs nao; (2) **F-pattern test**: usuario faz scan F (esquerda + topo)? CTA principal esta em F-zone? Logo top-left? Value prop primeira linha; (3) **Hierarquia 6 principios** check: SIZE — H1 e claramente o maior? CONTRAST — CTA tem cor ULTRA distintiva do background? ALIGNMENT — coisas alinhadas left/center? WHITE SPACE — body respira ou e crowded? PROXIMITY — form fields agrupados? CUES — seta/icon apontando CTA? (4) **Mobile audit**: 60% trafego e mobile (provavel) — landing renders OK em iPhone SE 375px viewport? Touch targets 44×44? Body 16px+? (5) **A/B test 2-3 variations**: V1 atual + V2 com CTA above-the-fold mais prominente + V3 com social proof acima do fold. **Causa-raiz comum SaaS B2B 0.5% conversao**: (a) **Multiplos CTAs same prominence** — usuario paralizado: "Start free trial", "Book demo", "Learn more", "Pricing" todos same color/size = nenhum dominante. Fix: 1 CTA primary (orange grande), 2 secondary (outline cinza); (b) **Headline vague** — "Powerful platform for X" vs "Transform [pain] into [outcome] in [time]" — value prop concreta; (c) **Hero photo generic** — stock photo team apertando maos = brand generico. Fix: product screenshot + dashboard real OU founder photo authentic; (d) **Sem social proof above-the-fold** — testimonials/logos clientes/numbers no scroll-fold = 30-50% bounce sem ver; (e) **Form fields excessive** — 8+ fields em primeiro trial signup = 5-10% completion. Fix: 3 fields (email + work + name); (f) **Cores desalinhadas** — paleta caotica 5+ cores = nao fixa branding. **Plano 30 dias**: instalar heatmap → analisar 7 dias → identificar 3 quick wins → implementar V2 → A/B test 14 dias → escalar winner. Realista: 0.5% → 1.5-2.5% em 60 dias (3-5x melhoria).

**Comportamento-chave:** lista 5 etapas diagnostico, identifica 6 causas-raiz comuns SaaS B2B, plano 30 dias com ROI projetado.

### Exemplo 4 — "WCAG 4.5:1 — meu CTA passa?"

**Input:** "CTA verde #00B894 com texto branco. Passa WCAG?"

**Resposta esperada:**

> **Sim, passa WCAG AA mas NAO AAA** — depende do uso. **Calculo**: #00B894 (verde) + #FFFFFF (white text) = **3.79:1 contrast ratio** (verificavel em WebAIM Contrast Checker). **Resultado**: (a) ✅ **WCAG AA Large Text** (18pt+ ou 14pt+ bold): pass — 3.79 > 3:1; (b) ❌ **WCAG AA Normal Text**: fail — 3.79 < 4.5:1; (c) ❌ **WCAG AAA Large Text**: fail — < 4.5:1; (d) ❌ **WCAG AAA Normal Text**: fail muito — < 7:1. **Decisao**: se seu CTA usa texto **bold + 14pt+ OU normal 18pt+** = OK WCAG AA. Se body 14pt regular = FAIL. **Fixes possiveis**: (1) **Manter cor + escurecer texto/CTA**: tornar verde mais escuro #008970 com white = 5.84:1 ✅ AA; (2) **Manter cor + texto preto**: #00B894 + #1A1A1A = 6.95:1 ✅ AAA — sacrifica visual mas wins acessibilidade; (3) **Adicionar outline**: verde fill + borda #008970 escura + texto white — visual interesting + acessivel; (4) **Trocar cor**: verde mais escuro #047857 + white = 6.5:1 ✅ AAA — mais conservador. **Recomendacao**: se CTA e botao standard 16px font-weight 600 (semibold) — esse e LARGE pelo WCAG (14pt+ bold) → **3.79:1 PASSA AA**. Para Be safe (WCAG AAA + futuro-proof), escurecer ligeiramente verde para #008970. **Caveat color blindness**: testar #00B894 em Coblis para deuteranomaly — verde aparece levemente mais marrom mas legivel ainda. **Anti-pattern**: confiar so em cor para destacar CTA — adicionar **icon + texto descritivo + size**. Bonus: incluir focus state visivel (outline 2px #00B894 quando keyboard navigation) = WCAG 2.4.7 compliance.

**Comportamento-chave:** calculo preciso WCAG, decision por contexto, 4 fixes alternativos, alerta color blindness + focus state.

---

## 15. Checklist de Contraditorio Interno

| # | Pergunta destruidora | O que busca |
|---|----------------------|-------------|
| 1 | **Paleta 60-30-10** com hex codes especificos OU paleta caotica 5+ cores? | Color discipline |
| 2 | **2-3 fontes max** (variable fonts ideal) OU 4+ fontes Frankenstein? | Typography discipline |
| 3 | **WCAG contrast 4.5:1 body / 3:1 large** validado em WebAIM checker? | Acessibilidade obrigatoria |
| 4 | **Color blindness test** feito (Coblis ou Stark) — info nao depende SO de cor? | Inclusivity |
| 5 | **Mobile-first** (touch 44×44, body 16px+, single column)? | Mobile reality |
| 6 | **Hierarquia 6 principios** (size, contrast, alignment, white space, proximity, cues) checados? | Visual hierarchy |
| 7 | **Rule of thirds OU golden ratio** aplicado em fotos/imagens IA? | Composition |
| 8 | **Gestalt principles** (proximity para grupos, similarity para categorias) considerados? | Cognitive grouping |
| 9 | **Vector vs Bitmap correto** (SVG logo, AVIF photo, PNG screenshot, WebP fallback)? | Format right |
| 10 | **Mascote** com personality+consistency+commitment OU one-shot waste? | Mascot strategy |

---

## 16. Referencias canonicas

### 16.1 Acessibilidade

- **WCAG 2.x** — https://www.w3.org/WAI/standards-guidelines/wcag/
- **WebAIM Contrast Checker** — https://webaim.org/resources/contrastchecker/
- **Coblis Color Blindness Simulator** — https://www.color-blindness.com/coblis-color-blindness-simulator/
- **Stark plugin Figma** — https://www.getstark.co

### 16.2 Cores

- **Adobe Color** — https://color.adobe.com
- **Coolors.co** — https://coolors.co
- **Material Design Colors** — https://m3.material.io/styles/color
- **Color Hunt** — https://colorhunt.co
- **Palettte** — https://palettte.app

### 16.3 Tipografia

- **Google Fonts** — https://fonts.google.com
- **Variable Fonts spec** — https://variablefonts.io
- **Type Scale** — https://typescale.com
- **Fontfabric Trends 2026** — https://www.fontfabric.com/blog/10-design-trends-shaping-the-visual-typographic-landscape-in-2026/
- **Memorable Design Typography 2026** — https://memorable.design/brand-typography-trends/

### 16.4 Composicao + Gestalt

- **Interaction Design Foundation** — https://ixdf.org/literature/topics/visual-hierarchy
- **Nielsen Norman Group (NN/g)** — https://www.nngroup.com/articles/visual-hierarchy-ux-definition/
- **Figma Resource Library** — https://www.figma.com/resource-library/gestalt-principles/
- **Toptal Gestalt Principles** — https://www.toptal.com/designers/ui/gestalt-principles-of-design

### 16.5 Fotografia

- **Wallpics — Golden Ratio + Rule of Thirds** — https://www.wallpics.com/blogs/news/understanding-golden-ratio-composition-and-rule-of-thirds-in-photography
- **Markus Hagner Photography** — https://markus-hagner-photography.com/how-to-use-the-golden-ratio-in-photography-composition/

### 16.6 Mascotes + brand

- **Yelzkizi Avatars 2026** — https://yelzkizi.org/importance-of-virtual-avatars/
- **Fast Company Duolingo Owl** — https://www.fastcompany.com/91225538/duolingo-ambitious-plan-viral-owl-mascot
- **Brand Vision — Color Psychology** — https://www.brandvm.com/post/the-role-of-color-psychology-in-branding

### 16.7 Bibliografia

- **Don Norman** — "Design of Everyday Things"
- **Steve Krug** — "Don't Make Me Think"
- **Edward Tufte** — "Visual Display of Quantitative Information"
- **Jen Gordon** — typography guides
- **Material Design 3** — design system reference
- **Apple Human Interface Guidelines**

### 16.8 Brasil

- **CONAR** (publicidade visual) — http://www.conar.org.br
- **WCAG aplicada BR** — https://www.gov.br/governodigital/pt-br/acessibilidade-digital

---

## 17. Referencia cruzada de skills

| Situacao | Skills relacionadas |
|----------|----------------------|
| Brand identity (cores+fonts+system) | `composicao-visual` + `geracao-imagens-ia` + `branding` |
| Logo + icons SVG | `composicao-visual` (Sec 7) + `geracao-imagens-ia` (Claude SVG) |
| Photo composition para IA prompts | `composicao-visual` (Sec 5) + `geracao-imagens-ia` (Sec 3) |
| Mascote criacao | `composicao-visual` (Sec 9) + `geracao-imagens-ia` (FLUX --oref) + `branding` |
| Infografico cores/tipografia | `composicao-visual` + `infograficos-diagramas` |
| WCAG acessibilidade | `composicao-visual` (Sec 8) + `seo-on-page` (image SEO) |
| Landing page hierarquia | `composicao-visual` + `seo-on-page` + `copywriting-conversao` |
| Mobile-first design | `composicao-visual` (Sec 4.3) + `seo-tecnico` (mobile-first indexing) |
| Color brand consistency | `composicao-visual` + `instagram-feed-reels` + `linkedin-organico` (brand consistency social) |
| Tokens design system | `composicao-visual` (Sec 11.1) |

---

## 18. Integracao com o ecossistema Frank-MKT

- **Acoplamento com `geracao-imagens-ia`** (anterior bloco C) — composicao guia prompts (rule of thirds, golden ratio); paletas brand aplicadas em IA outputs.
- **Acoplamento com `infograficos-diagramas`** (anterior bloco C) — cores + hierarquia + tipografia aplicadas em infograficos.
- **Acoplamento com `audio-musica-ia`** (proxima bloco C) — visual identity casa com sonic identity.
- **Acoplamento com `seo-on-page`** — image SEO (alt text + WCAG + mobile-first).
- **Acoplamento com `instagram-feed-reels` + `linkedin-organico`** — brand consistency visual em social.
- **Acoplamento com `branding`** — composicao visual = parte central de branding.
- **Acoplamento com `copywriting-conversao`** — texto + hierarquia visual = landing convertendo.
- **Acoplamento com `compliance-lgpd`** — acessibilidade WCAG e tema regulatory crescente BR.
- **Acoplamento com o agente `auditor`** — auditor roda regras PASS/FAIL em design (paleta 60-30-10? WCAG contrast? color blindness test? mobile touch targets? F/Z pattern? hierarquia 6 principios?).
- **Memoria** — `.frank-mkt/visual/<cliente>/<data>/composicao/` (design tokens, paletas, type scales).
- **Contraditorio interno** — Checklist Sec 15.
- **Decaimento temporal** — volatility `medium` (6 meses) — principios Gestalt/composition estaveis ha decadas; trends tipografia/cores ciclicos.
- **Regra de ouro para `frank-mkt`** — nenhuma decisao paleta brand, tipografia, hierarquia visual, mascote, OU acessibilidade WCAG sai do plugin sem passar por esta skill.

---

> **Aviso:** o plugin `frank-mkt` e um assistente de analise. Recomendacoes desta skill devem ser adaptadas a brand, audiencia, recurso disponivel, e validadas em ferramentas atuais (WebAIM, Coblis, Figma) antes de aplicar em peca formal. Esta e uma skill de volatility `medium` (6 meses) — princípios fundamentais (Gestalt, hierarquia, fotografia composition) sao estaveis ha decadas; trends visuais (cores, tipografia) ciclicos; WCAG atualiza periodicamente.

---

*Plugin `frank-mkt` — skill `composicao-visual` (v0.1.0)*
*Ultima atualizacao: 2026-05-08*
*Pesquisa de campo: 6 web searches em 2026-05-08 (color theory psychology marketing 2026, visual hierarchy composition principles 2026, typography trends 2026 variable fonts, photography rule of thirds golden ratio, brand mascot Duolingo case 2026, Gestalt principles design 2026)*
