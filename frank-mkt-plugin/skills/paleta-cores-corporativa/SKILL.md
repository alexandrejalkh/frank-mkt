---
name: paleta-cores-corporativa
description: Paleta Cores Corporativa 2026 (paleta primaria/secundaria/terciaria + acessibilidade WCAG 4.5:1 AA / 7:1 AAA + Pantone PMS + conversao RGB/CMYK/HEX + dark mode + cultural color meaning Brasil + ferramentas Coolors/Adobe Color/Color Hunt + OKLab/LAB color spaces 2026) para brand designers/CMO/CCO/devs frontend/agencias, integracao WCAG compliance + brand-book-methodology + design-system-basico. 3a SKILL Bloco Identidade Visual Corporativa / Brand Design.
volatility: medium
last_review: 2026-05-09
next_review: 2026-11-09
languages: [pt-BR]
audience: [brand-designers, CMO, CCO, devs-frontend, agencias, design-system-leads]
ascii_only: true
---

# Skill: paleta-cores-corporativa

Paleta de cores corporativa nao e "escolher cores bonitas" — e arquitetura semantica que carrega 80% do reconhecimento de marca antes do logo, do nome, do produto. Cor e o ativo de marca mais economico e mais explosivo: errar uma cor especifica (ex.: Tiffany Blue, Coca Vermelho, Nubank Roxo) compromete um bilhao de impressoes acumuladas. Esta skill ensina paleta foundations (primary/secondary/tertiary/neutrals/semantic), acessibilidade WCAG (4.5:1 AA, 7:1 AAA, colorblindness), color spaces (RGB/CMYK/HEX/Pantone PMS/LAB/OKLab), dark mode adaptativo, cultural meaning (Brasil + global + setor), tools 2026 (Coolors, Adobe Color, Color Hunt, OKLCH), e cases Brasil 2026 (Nubank purple, Magalu blue+yellow, Itau orange).

---

## Decaimento Temporal

- **Estavel (2-3 anos)**: WCAG contrast ratios (4.5:1 AA, 7:1 AAA, 3:1 large text/UI), color theory foundations (RYB/RGB/CMYK basics, harmonia complementar/analoga/triadica), cultural meanings consolidados (purple=mourning Brasil, white=mourning Asia, red=luck China), Pantone PMS guides estruturais.
- **Volatil (6-18 meses)**: Pantone Color of the Year (2026: Cloud Dancer 11-4201), trends de palette (earthy neutrals 2026, transformative teal, plum noir, persimmon), tools features (Coolors AI, Adobe Color contrast checker), browser support OKLCH (Chrome 111+, Safari 16.4+, Firefox 113+).
- **Hyper-volatil (<6 meses)**: cases brasileiros (Nubank, Magalu, Itau podem rebrand), tendencias TikTok/Instagram color, AI color tools features (Khroma, Huemint).

Reaplique anualmente: WCAG 3.0 (em desenvolvimento, provavel 2027) traz APCA (Accessible Perceptual Contrast Algorithm) que substitui ratio simples por calculo perceptual.

---

## Visao Geral

### O que e paleta de cores corporativa

Sistema cromatico estruturado e documentado que define identidade visual de uma marca, organizado em hierarquias funcionais:

1. **Primary (1-2 cores)**: cores dominantes, ~60% da aplicacao, carregam reconhecimento.
2. **Secondary (2-3 cores)**: cores de apoio, ~30%, criam profundidade e variacao.
3. **Tertiary/Accent (1-2 cores)**: cores de destaque, ~10%, CTAs, alertas, highlights.
4. **Neutrals (3-7 tons)**: pretos, brancos, cinzas (frios ou quentes 2026 trend) para texto, fundo, bordas.
5. **Semantic (4-6 cores)**: cores funcionais com significado fixo — sucesso (verde), erro (vermelho), warning (amarelo/laranja), info (azul).

### Por que importa

- **Reconhecimento de marca**: cor aumenta brand recognition em ate 80% (Reboot Online, baseando-se em estudos University of Loyola Maryland).
- **Acessibilidade**: 8% homens + 0,5% mulheres tem alguma forma de daltonismo (~300M globalmente). Sem WCAG, marca exclui 4-5% do publico.
- **Conversao**: dark mode design converte melhor em e-commerce premium (Digital Silk 2026).
- **Diferenciacao**: 2026 sai do "minimal grayscale safe" e entra em paletas estrategicamente bold (Pulse Advertising 2026 trend).

### Quem usa esta skill

- **Brand Designer**: cria sistema, documenta no brand book.
- **CMO/CCO**: aprova, garante consistencia cross-channel.
- **Dev Frontend**: traduz HEX -> tokens (CSS variables, Tailwind config, design tokens W3C).
- **Agencia**: aplica em deliverables (logo, landing, anuncio).
- **Design System Lead**: integra com tokens semanticos (color.background.primary, color.text.muted).

### Quando nao usar (anti-escopo)

- Esta skill **nao** ensina teoria de cor pura academica (Itten, Albers) — referencias indicadas.
- Nao cobre print management profundo (perfis ICC, calibration, gamut mapping completo) — mencionado em superficie.
- Nao substitui consultoria de daltonismo (testes com Coblis, Sim Daltonism).

---

## Fundacao 1 — Paleta Foundations (Primary + Secondary + Tertiary + Neutrals + Semantic)

### Regra 60-30-10 (estendida 2026)

A regra classica de design de interiores aplicada a brand:

- **60% Dominante (Primary)**: cor principal. Em UI, tipicamente background ou cor de marca. Em material impresso, cor de fundo / area maior.
- **30% Secundaria**: complemento. Em UI, cards, secoes secundarias. Em impressao, area de apoio.
- **10% Accent (Tertiary)**: CTA, link, highlight. Em UI, botoes primarios, focus state. Em impressao, headlines, ornamentos.

Em 2026, marcas estao adicionando uma quarta camada: **Neutrals (substrato)** que pode ocupar ate 50% efetivamente e desloca a 60-30-10 para 50-30-15-5 quando consideramos texto.

### Estrutura completa do sistema

#### Primary
- 1 cor "hero" (a que define a marca em uma palavra: Nubank=roxo, Coca=vermelho, Tiffany=ciano-pastel).
- HEX, RGB, CMYK, Pantone PMS Coated + Uncoated, LAB, OKLCH.
- Variacoes: 50, 100, 200, 300, 400, 500 (cor base), 600, 700, 800, 900 (escala 9 ou 10 tons estilo Tailwind / Material).

Exemplo Nubank-style:
- nubank-purple-500 (base): `#820AD1` / RGB(130, 10, 209) / Pantone 2592 C / aproximacao.
- nubank-purple-50: `#F5E6FF` (lightest, backgrounds).
- nubank-purple-900: `#2D0049` (darkest, hover, dark mode primary).

#### Secondary
- 2-3 cores que complementam a primary.
- Use harmonia: complementar (oposta no circulo), analoga (vizinhas), triadica (3 equidistantes), split-complementar (1 + 2 vizinhas da oposta).
- Cada uma com escala 9-10 tons.

#### Tertiary / Accent
- 1-2 cores de alta saturacao para destaque pontual.
- Use com moderacao — accent perde poder se aplicada em mais de 10% da composicao.

#### Neutrals
- 3-7 cinzas. Em 2026, trend desloca de cinza frio (`#F5F5F5`, `#1A1A1A`) para cinza quente / beige (`#F5F1EC`, `#1F1B17`).
- Inclua warm neutrals 2026: bege quente (`#E8DCC4`), taupe (`#8B7E68`), sand (`#D4C4A8`).

#### Semantic Colors
- Success (verde): `#16A34A` ou similar. WCAG-checked sobre branco.
- Danger / Error (vermelho): `#DC2626`.
- Warning (amarelo / laranja): `#F59E0B`.
- Info (azul): `#3B82F6`.
- Estes nao sao cores de marca — sao convencoes universais. Marca pode customizar mas mantendo psicologia (verde nao vira erro).

### Harmonias cromaticas

- **Monocromatica**: 1 hue + variacoes de saturacao/lightness. Sofisticada, segura. Risk: monotona.
- **Analoga**: 3 cores vizinhas no circulo (60 graus). Harmonia natural, calma.
- **Complementar**: 2 cores opostas (180 graus). Alto contraste, vibrante. Risk: vibracao otica se mal calibrado.
- **Split-complementar**: 1 cor + 2 vizinhas da oposta. Equilibrio entre contraste e harmonia.
- **Triadica**: 3 cores equidistantes (120 graus). Vivida, balanceada.
- **Tetradica / Quadratica**: 4 cores em 2 pares complementares. Rica, dificil dominar — uma deve dominar.

### Escolha de cor primary: framework "5 perguntas"

1. **Qual emocao/atributo a marca quer evocar?** (confianca/calma=azul, energia=laranja/vermelho, luxo=roxo/preto+dourado, sustentabilidade=verde, inovacao=ciano/teal).
2. **Quem sao os concorrentes? Que cores eles ocupam?** (categoria fintech BR ja tem roxo=Nubank, laranja=Itau, verde=BB+Bradesco — nao copie).
3. **Cultura do publico-alvo?** (Brasil: evite associacoes com luto, valorize cores quentes).
4. **Reproducibilidade tecnica?** (cor que so existe em RGB widegamut sera frustrante em CMYK + serigrafia).
5. **Acessibilidade desde o dia 1?** (cor que falha 4.5:1 contra branco/preto exige variantes).

---

## Fundacao 2 — Acessibilidade WCAG Contraste (4.5:1 AA + 7:1 AAA + colorblindness)

### Regras WCAG 2.1 / 2.2 (vigentes 2026)

#### Contrast Ratio (1.4.3 + 1.4.6 + 1.4.11)

| Elemento | Nivel AA (minimo) | Nivel AAA (enhanced) |
|---|---|---|
| Texto normal (<18pt regular ou <14pt bold) | 4.5:1 | 7:1 |
| Texto large (>=18pt regular ou >=14pt bold) | 3:1 | 4.5:1 |
| Componentes UI (botoes, inputs, icons funcionais, focus rings) | 3:1 | nao especificado |
| Graficos significativos (charts, icones de info) | 3:1 | nao especificado |

**Texto large**: ~24px regular ou ~18.66px bold (1pt = 1.333px aproximado).

#### Como calcular

Contrast ratio = (L1 + 0.05) / (L2 + 0.05), onde L1 e a luminancia relativa da cor mais clara e L2 da mais escura. Luminancia relativa usa formula sRGB com gamma (consultar W3C).

Nao calcule manualmente — use ferramentas:

- **WebAIM Contrast Checker** (https://webaim.org/resources/contrastchecker/) — padrao da industria.
- **Stark** (plugin Figma/Sketch) — checa em tempo real no design.
- **Coolors Contrast Checker** — dentro da generator.
- **Polypane** — browser dev focado acessibilidade.
- **Adobe Color Accessibility Tools** — integrado a paleta.
- **Chrome DevTools** — Inspecionar > Contrast Ratio (built-in 2026).

#### Casos de falha comuns

- **Cinza claro sobre branco**: `#999` sobre `#FFF` da 2.85:1 — falha AA. Use `#737373` (4.54:1) minimo.
- **Texto colorido sobre cor**: laranja `#F97316` sobre branco da 2.96:1 — falha. Texto colorido precisa ser escuro.
- **Placeholder cinza**: tipicamente `#A0A0A0` (3.5:1) — falha AA. Pode ser aceitavel se usuario sabe que e placeholder e label esta visivel (debate interpretacao 1.4.3).
- **Botao desabilitado**: WCAG isenta elementos disabled de contrast — mas usabilidade pede que esteja claramente diferente do enabled.

#### Exemplos validados

| Combo | Ratio | AA Normal | AA Large | AAA Normal |
|---|---|---|---|---|
| `#000000` sobre `#FFFFFF` | 21:1 | OK | OK | OK |
| `#1F2937` sobre `#FFFFFF` | 14.7:1 | OK | OK | OK |
| `#374151` sobre `#FFFFFF` | 10.3:1 | OK | OK | OK |
| `#4B5563` sobre `#FFFFFF` | 7.59:1 | OK | OK | OK |
| `#6B7280` sobre `#FFFFFF` | 5.13:1 | OK | OK | falha |
| `#9CA3AF` sobre `#FFFFFF` | 2.85:1 | falha | falha | falha |
| `#FFFFFF` sobre `#1F2937` | 14.7:1 | OK | OK | OK |
| `#FFFFFF` sobre `#820AD1` (Nubank-ish) | 6.93:1 | OK | OK | quase AAA |

### Colorblindness (daltonismo)

8% homens + 0,5% mulheres globalmente. Tipos:

- **Deuteranopia** (verde): 5% homens. Confunde verde-vermelho.
- **Protanopia** (vermelho): 1% homens. Confunde vermelho-verde.
- **Tritanopia** (azul-amarelo): <0,01%. Rara.
- **Achromatopsia** (total): <0,003%. Ve em escala de cinza.

#### Diretrizes

1. **Nunca dependa SO de cor para transmitir informacao** (1.4.1 Use of Color, AA). Combine com texto, icone, padrao.
   - Mau: grafico de barras vermelho=ruim / verde=bom sem rotulos.
   - Bom: barras com rotulos +/-, setas up/down, ou cor + padrao listrado.

2. **Teste com simuladores**:
   - **Coblis** (https://www.color-blindness.com/coblis-color-blindness-simulator/).
   - **Sim Daltonism** (macOS).
   - **Stark plugin** — simula em Figma.
   - **Chrome DevTools > Rendering > Emulate vision deficiencies**.

3. **Use combos colorblind-safe**:
   - Azul + laranja (deuteranopia/protanopia ainda distingue).
   - Evite vermelho+verde puros para distincao critica.
   - Paletas como **ColorBrewer** (https://colorbrewer2.org/) tem escalas colorblind-safe pre-validadas.

### WCAG 3.0 e APCA (futuro)

- **WCAG 3.0** (Silver) em desenvolvimento, possivel publicacao 2027+.
- Substitui ratio simples por **APCA** (Accessible Perceptual Contrast Algorithm) — mais alinhado com percepcao humana real.
- APCA da scores Lc (contrast level), nao ratios. Lc 75+ para texto normal, Lc 60+ large.
- Fique atento. Por hoje (2026), WCAG 2.2 e o standard.

---

## Fundacao 3 — Color Spaces (RGB + CMYK + HEX + Pantone PMS + LAB + OKLab 2026)

### RGB (Red, Green, Blue)

- **Modelo aditivo**: somar luz. Usado em **telas** (monitores, TVs, smartphones, projetores).
- Cada canal 0-255 (8-bit) ou 0-1 (float).
- Espacos: **sRGB** (padrao web), **Display P3** (Apple, ~25% mais largo), **Adobe RGB** (impressao profissional), **Rec. 2020** (HDR/8K).
- 2026: P3 ja e default em iPhone, MacBook, Pixel. CSS suporta `color(display-p3 ...)`.

### HEX

- Notacao hexadecimal de RGB. `#RRGGBB` (00-FF cada). `#FF8800` = RGB(255, 136, 0).
- Atalho 3 digitos: `#F80` = `#FF8800`.
- Com alpha (8 digitos): `#FF8800CC` = laranja com 80% opacidade.

### CMYK (Cyan, Magenta, Yellow, Key/Black)

- **Modelo subtrativo**: tinta absorve luz. Usado em **impressao offset, digital, serigrafia**.
- Cada canal 0-100%.
- **Gamut menor que RGB** — cores RGB vividas (neon, ciano puro `#00FFFF`) nao reproduzem em CMYK.
- Sempre converta RGB->CMYK durante preparacao de arte. Nunca confie em conversao automatica do design tool sem prova fisica.

### Pantone PMS (Pantone Matching System)

- Sistema de cores padronizado, com 2000+ cores formuladas.
- Cada cor e mistura especifica de tintas base Pantone (nao CMYK).
- Vantagens: consistencia perfeita entre lotes, tiragens, paises.
- Variantes principais:
  - **Solid Coated (C)**: papel coated/glossy. Cor mais saturada.
  - **Solid Uncoated (U)**: papel offset/fosco. Cor menos saturada (~10-15% diferenca visual).
  - **Pastels & Neons** — guides especificos.
  - **Bridge / Plus Series** — equivalencias CMYK aproximadas.
- Use Pantone quando: marca tem cor super especifica (Tiffany 1837 Blue, Coca PMS 484), tiragem grande (custo de tinta extra dilui), branding premium.
- Cores Pantone tem custo: cada cor = uma tinta extra na maquina = mais caro que CMYK puro.

### LAB (CIELAB)

- Espaco perceptualmente uniforme. L*=lightness 0-100, a*=verde-vermelho, b*=azul-amarelo.
- Independente de device.
- Usado em color management profissional (perfis ICC), conversao precisa entre RGB e CMYK.

### OKLab / OKLCH (2026)

- Evolucao do LAB criada por Bjorn Ottosson (2020). Mais perceptualmente uniforme que CIELAB para hues vivos.
- **OKLCH**: forma cilindrica de OKLab (L=lightness 0-1, C=chroma, H=hue 0-360deg).
- **CSS Color Module Level 4** suporta `oklch()` em browsers modernos (Chrome 111+, Safari 16.4+, Firefox 113+).
- Vantagem killer: **gradientes nao passam por cinza zumbi**. Gradient `red -> blue` em RGB passa por cinza feio. Em OKLCH passa por roxo bonito.
- Vantagem 2: **escalas de tons consistentes** (manipular L mantem chroma percebida igual entre hues).
- 2026: design systems modernos (Tailwind v4, Radix Colors v2) usam OKLCH.

#### Exemplo: gerar escala em OKLCH

```css
:root {
  --brand-50: oklch(97% 0.02 280);
  --brand-100: oklch(94% 0.04 280);
  --brand-200: oklch(87% 0.08 280);
  --brand-300: oklch(78% 0.12 280);
  --brand-400: oklch(67% 0.18 280);
  --brand-500: oklch(56% 0.22 280); /* base */
  --brand-600: oklch(48% 0.21 280);
  --brand-700: oklch(40% 0.19 280);
  --brand-800: oklch(32% 0.16 280);
  --brand-900: oklch(24% 0.13 280);
}
```

Hue 280 = roxo. Note que mantemos H constante e variamos L, ajustando C conforme necessario.

### Conversao na pratica

1. **Designer**: trabalha em RGB (sRGB ou P3) no Figma/Adobe.
2. **Print prep**: converte para CMYK + define equivalente Pantone para acentos.
3. **Documentacao brand book**: lista todas as 5 versoes (HEX, RGB, CMYK, Pantone C, Pantone U) por cor.
4. **Web**: HEX (legacy) ou OKLCH (moderno) com fallback.

#### Tabela exemplo Nubank (aproximada, ilustrativa, nao oficial)

| Sistema | Valor |
|---|---|
| HEX | `#820AD1` |
| RGB | 130, 10, 209 |
| CMYK | 75, 90, 0, 0 (aproximado) |
| Pantone Coated | ~PMS 2592 C |
| Pantone Uncoated | ~PMS 2592 U |
| LAB | L 38, a 68, b -77 |
| OKLCH | oklch(42% 0.27 305) |

Sempre valide com prova fisica. Conversao automatica e ponto de partida.

### Tools de conversao 2026

- **Pantone Color Connect** (app oficial).
- **Pantonecolors.net** — tabela online completa.
- **Chromafinder.com** — Pantone -> HEX/RGB/CMYK/LAB.
- **Coolors** — exporta em todos os formatos incluindo OKLCH.
- **CSS-Tricks color converter**.
- **Lea Verou's color tools** (oklch.com, conic.style).

---

## Fundacao 4 — Dark Mode + Adaptive Color

### Filosofia 2026: dark-first ou light-first?

Em 2026, **dark-first** e padrao em software dev tooling (VS Code default, GitHub, Linear, Notion). Para **brand sites**, light continua dominante (e-commerce, news, corp). Para **apps mobile**, sistema do device decide (auto).

A skill recomenda: **projete light primeiro, valide dark como variante de igual peso**, com tokens semanticos.

### Por que dark mode nao e "inverter cores"

Erros comuns:

- Inverter literalmente (`#FFF` -> `#000`) gera contraste excessivo e fadiga.
- Usar preto puro `#000` em OLED parece "buraco". Use `#0A0A0A`, `#121212` (Material Dark surface), `#171717` (Tailwind neutral-900).
- Usar branco puro como texto em dark mode causa halation (sangramento). Use `#E5E5E5`, `#EAEAEA`.
- Saturar demais — cores vivas em fundo escuro vibram. Reduza chroma 10-30% no dark.

### Layered darkness (2026 best practice)

Em vez de 1 fundo preto e 1 cor de cards, use 4-6 camadas de escuridao para hierarquia:

```css
/* Tailwind / OKLCH style */
--bg-base: #0A0A0A;       /* fundo body */
--bg-surface-1: #141414;  /* cards level 1 */
--bg-surface-2: #1F1F1F;  /* cards level 2 (modal sobre card) */
--bg-surface-3: #2A2A2A;  /* hover, elevated */
--bg-surface-4: #353535;  /* highest elevation */
--border-subtle: #262626;
--border-default: #404040;
```

Material Design 3 chama de "elevation tones" — quanto mais elevado, mais claro o fundo, simulando luz vinda de cima.

### Adaptive color tokens

Defina tokens semanticos, nao cores brutas, no design system:

```css
:root {
  /* light */
  --color-bg-primary: #FFFFFF;
  --color-bg-secondary: #F5F5F5;
  --color-text-primary: #0A0A0A;
  --color-text-secondary: #525252;
  --color-brand: #820AD1;
  --color-brand-hover: #6B0AAB;
}

[data-theme="dark"] {
  --color-bg-primary: #0A0A0A;
  --color-bg-secondary: #141414;
  --color-text-primary: #FAFAFA;
  --color-text-secondary: #A3A3A3;
  --color-brand: #B069E6;     /* mais claro p/ contraste em dark */
  --color-brand-hover: #C290F0;
}
```

A cor de marca **muda no dark** para manter contraste e nao agredir. Perde 10% reconhecimento literal mas ganha em UX.

### Validacao dark mode

- WCAG aplica igualmente. Texto secundario `#A3A3A3` sobre `#0A0A0A` = 8.9:1 (AAA OK).
- Verifique cores de marca: Nubank purple `#820AD1` sobre `#0A0A0A` = 3.0:1 — falha texto normal AA. Use variante mais clara em dark mode.
- Imagens nao sao auto-ajustadas. PNGs com fundo branco "explodem" em dark. Use SVGs com `currentColor` ou versoes dual.

### Auto-switch via prefers-color-scheme

```css
@media (prefers-color-scheme: dark) {
  :root { /* dark vars */ }
}
```

Combine com toggle manual (localStorage) para dar controle ao usuario.

---

## Fundacao 5 — Cultural Color Meaning (Brasil + Global + Industry-specific)

### Brasil — significados consolidados

| Cor | Associacoes positivas | Associacoes negativas / cuidado |
|---|---|---|
| Verde+Amarelo | Bandeira, patriotismo, futebol, identidade nacional | Pode polarizar politicamente (uso recente como simbolo partidario) |
| Azul | Confianca, calma, religiao (Maria, ceu), bancos | Pode parecer frio se isolado |
| Vermelho | Paixao, energia, alimentos, partidos de esquerda historicamente | Politicamente carregado dependendo do contexto |
| Verde | Natureza, esperanca, sustentabilidade, saude | Muito associado a "ecologia" — pode parecer greenwashing se mal aplicado |
| Roxo | Royal, espiritualidade, magia | **Luto catolico em algumas regioes** (Quaresma, Sexta-feira Santa) |
| Branco | Pureza, paz, candomble (Oxala) | OK no Brasil (diferente da Asia) |
| Preto | Elegancia, luxo, formalidade, luto | Luto principal no Brasil (funerais) |
| Amarelo | Alegria, sol, otimismo, McDonald's, Magalu | Em algumas regioes da America Latina associado a morte (mas nao Brasil predominante) |
| Laranja | Energia, criatividade, calor | Associada a clube de futebol (em algumas torcidas), partidos politicos |
| Rosa | Feminilidade tradicional, romantico | Genderizacao — cuidado com estereotipos |

### Cores e setores (Brasil)

- **Bancos / fintechs**: azul (Itau parcial, BB, Bradesco, Banco do Brasil), laranja (Itau dominante), roxo (Nubank disrupcao), verde (Sicoob, Sicredi, BB).
- **Telecom**: vermelho (Vivo), laranja (Claro), magenta (Tim).
- **Varejo**: azul+amarelo (Magalu, Casas Bahia), vermelho (Lojas Marisa, Renner).
- **Saude**: azul (hospitais), verde (planos saude, farmacias), branco (associacao com asseio).
- **Alimentos**: vermelho+amarelo (fast food), verde (natural, saudavel), marrom (chocolate, cafe).
- **Educacao**: azul (tradicional), laranja/amarelo (jovem, dinamico), verde (Anhanguera, Cogna).
- **Tech BR**: roxo (Nubank, Hotmart), laranja (Hotmart secundaria, RD Station), azul (totvs, locaweb), verde (positivo).
- **Juridico**: azul-marinho, bordo, dourado, preto. Cores conservadoras, austeras.

### Diferencas globais relevantes

| Cor | Brasil | China | India | EUA | Europa Ocidental | Oriente Medio |
|---|---|---|---|---|---|---|
| Vermelho | Paixao | Sorte, casamento | Pureza, casamento | Perigo, paixao | Perigo, amor | Perigo, cautela |
| Branco | Paz, pureza | **Luto, morte** | Luto, viuvez | Pureza, casamento | Pureza, casamento | Pureza |
| Preto | Luto, elegancia | Elegancia | Mau augurio | Luto, elegancia | Luto, elegancia | Luto |
| Amarelo | Alegria | Royal, sagrado | Comercio, sagrado | Cautela | Inveja, traicao | Felicidade |
| Verde | Natureza, esperanca | Saude, infidelidade | Islam (em areas), agricultura | Natureza, $ | Natureza | **Sagrado (Islam)** |
| Roxo | Royal, **luto** | Bens estimados | Reincarnacao | Royalty, luxo | Royalty | Virtude |
| Azul | Confianca | Imortalidade | Krishna | Confianca | Confianca | Protecao |

**Aplicacao pratica para marca BR com ambicao internacional**: pesquise mercado-alvo. McDonald's, IKEA, P&G ajustam cor por geografia.

### Industry-specific globals

- **Healthcare**: branco + azul claro (limpeza, confianca, agua, aco-cirurgico).
- **Tech / SaaS**: azul, ciano, roxo, preto sobre branco minimal.
- **Luxury**: preto + dourado, branco + dourado, monocromatico.
- **Sustentabilidade / ESG**: verde, mas evite generico — combine com cores autenticas da marca.
- **Food & Beverage**: vermelho/amarelo (apetite), verde (natural), marrom (cafe/chocolate).
- **Crianca / educacao infantil**: paletas vivas multicolor, primarias.
- **Beleza / cosmeticos**: rose gold, nude, paletas tonais.

### Como pesquisar significado para mercado especifico

1. **Etnografia rasa**: Google Images "[setor] [cor] [pais]" — veja padroes.
2. **Concorrentes locais**: liste 10, mapeie cores. White space cromatico = oportunidade.
3. **Pesquisa primaria**: 5-10 entrevistas com publico-alvo perguntando associacoes.
4. **Pantone + research**: Pantone publica color forecasts regionais.
5. **Lojas fisicas / displays**: visite varejo do setor. Como esta organizado por cor?

---

## Fundacao 6 — Brasil 2026 Cases (Nubank purple + Magalu blue+yellow + Itau orange)

### Nubank — roxo como rebeldia categorica

- **Cor primaria**: roxo `#820AD1` (aproximacao publica).
- **Contexto**: 2013 startup desafia bancos tradicionais (azul=BB/Bradesco, laranja=Itau, vermelho=Santander).
- **Decisao**: roxo nao tinha dono na categoria bancaria BR. Posicionamento de disrupcao.
- **Aplicacao**:
  - 60% UI: roxo + brancos.
  - 30% secundaria: tons de roxo (clarinhos pastel, escuros profundos).
  - 10% accent: roxo neon para CTAs/destaques.
- **Resultado**: "roxinho" virou apelido afetivo. 90M+ clientes. Cor virou ativo BiP (Brand Implementation Premium).
- **Licao 1**: pesquise white space cromatico antes de escolher.
- **Licao 2**: monocromatica aplicada com rigor compete com paletas multicolor.

### Magalu — azul (`#0086FF` aprox) + amarelo (`#FFE600` aprox)

- **Cor primaria**: azul, com amarelo como accent vibrante.
- **Contexto**: varejo popular nacional. Heranca de cores tradicionais do varejo.
- **Decisao**: combo azul+amarelo evoca confianca + alegria + acessibilidade. Refresh em 2010s para azul mais saturado e moderno.
- **Aplicacao**:
  - Logo: azul dominante.
  - Ofertas / CTAs: amarelo para chamar atencao em tags de promocao.
  - Loja fisica: fachadas azul + amarelo para visibilidade urbana.
- **Lu (mascote)**: cor da pele tom pessego, contrasta com paleta azul da marca, virando focal point.
- **Licao**: combo de cores quente + fria pode convergir vibrante. Magalu equilibra azul institucional com amarelo de impulso.

### Itau — laranja (`#EC7000` aprox) absoluto

- **Cor primaria**: laranja desde 2000s, antes era azul claro.
- **Contexto**: bancos tradicionais BR usavam azul (BB, Bradesco) ou amarelo+verde (BB). Itau foi a azul institucional ate rebranding agressivo para laranja.
- **Decisao**: laranja diferencia, evoca energia, calor humano, vitalidade — distingue de bancos "frios".
- **Aplicacao**:
  - Agencias fisicas: laranja saturado em fachada.
  - Cartoes: laranja como hero color.
  - Logo: laranja com fonte preta ou branca.
  - Comunicacoes: laranja em destaques, branco/preto como neutrals.
- **Licao 1**: rebrand de cor e arriscado mas estrategico — Itau ganhou diferenciacao.
- **Licao 2**: laranja em volume requer disciplina de uso para nao parecer barato (associacao DIY, fast-food).

### Outros cases relevantes BR

- **Ifood**: vermelho `#EA1D2C` — apetite, urgencia, fast.
- **Globo**: variavel por produto, mas Globo News azul-marinho, GloboPlay azul-roxo.
- **Vivo**: roxo+vermelho, signature gradient. Disputa visual com Nubank em roxo (categorias diferentes evita conflito).
- **Hotmart**: roxo tambem (laranja secundario).
- **Magazine Luiza** (Magalu) detalhado acima.
- **Stone**: verde neon `#00A868`, disruptiva em pagamentos B2B.
- **PicPay**: verde `#21C25E`, dialoga com fintech sustentavel.
- **C6 Bank**: preto + dourado, posicionamento premium em fintech.

### Padroes observaveis

- **Disrupcao em categoria mature**: ocupe white space cromatico.
- **Cor + tipografia + fotografia**: cor sozinha nao salva. Precisa de sistema.
- **Refresh ciclico (5-10 anos)**: cores envelhecem (saturacao, luminosidade reformatadas — Itau laranja de 2010 nao e o de 2024).
- **Escalavel**: cor que funciona em fachada, app, embalagem, video.

---

## Fundacao 7 — Mensuracao + Tools 2026

### Tools de geracao e exploracao

#### Coolors (https://coolors.co)

- **Forca**: ultra-rapido. Spacebar gera nova paleta. Lock cores que voce gosta. Educacao integrada (paletas trending, exemplos).
- **2026 features**: AI mode, contraste integrado, export OKLCH, image extraction.
- **Pricing**: free + Pro (~$5/mes) com unlimited.
- **Caso de uso**: brainstorm rapido, exploracao inicial.

#### Adobe Color (https://color.adobe.com)

- **Forca**: harmony rules rigorosas (complementar, analoga, triadica, etc), accessibility tools (contrast checker, colorblind simulator), gradient generator, theme extraction de imagens.
- **Integracao**: sync com Creative Cloud — paletas aparecem em Photoshop, Illustrator, InDesign.
- **2026**: Color Trends section curada com palettes da comunidade Behance.
- **Caso de uso**: trabalho profissional brand, design system formal.

#### Color Hunt (https://colorhunt.co)

- **Forca**: curadoria humana de paletas trending. Browse, copy, ir.
- **Limite**: nao gera, so cura. Otimo para inspiracao.

#### Khroma (https://khroma.co)

- **Forca**: AI treinada nas suas preferencias (escolha 50 cores que gosta, ele aprende). Gera paletas alinhadas ao seu gosto.

#### Huemint (https://huemint.com)

- **Forca**: AI generativa baseada em uso (logo, brand, illustration). Algoritmo de coerencia.

#### Realtime Colors (https://realtimecolors.com)

- **Forca**: aplicar paleta em template real (landing, app) instantaneamente. Ver em contexto.

### Tools de acessibilidade

- **WebAIM Contrast Checker** (https://webaim.org/resources/contrastchecker/) — gold standard.
- **Stark** (https://www.getstark.co/) — plugin Figma/Sketch/XD. Contrast, vision simulator, focus order.
- **Polypane** (https://polypane.app/) — browser dedicado a accessibility.
- **Coblis** (https://www.color-blindness.com/coblis-color-blindness-simulator/) — colorblindness simulator.
- **Sim Daltonism** (macOS app gratis).
- **Chrome DevTools** — Inspect > Accessibility > Contrast Ratio + Rendering > Emulate vision deficiencies.
- **axe DevTools** — extensao Chrome/Firefox para audit completo WCAG.

### Tools de Pantone / color management

- **Pantone Connect** (https://www.pantone.com/pantone-connect) — app oficial, plugins Adobe/Figma. Pago.
- **Pantonecolors.net** — tabela online gratuita (nao oficial mas util).
- **Chromafinder.com** — converter Pantone -> HEX/RGB/CMYK/LAB.
- **CMYK to Pantone (Ginifab, DNS Checker)** — match closest PMS.

### Tools de OKLCH / OKLab

- **oklch.com** (https://oklch.com) — Lea Verou. Visualize OKLCH ao vivo.
- **conic.style** — palette generator OKLCH-first.
- **Huetone** (https://huetone.ardov.me/) — Andrey Sitnik. Build perceptually uniform scales.
- **Tailwind Play** v4 — testa OKLCH no Tailwind.

### Tools de design tokens

- **Style Dictionary** (Amazon) — transforma tokens semanticos em CSS/iOS/Android/Web.
- **Token Studio** (Figma plugin) — define tokens visualmente, exporta JSON.
- **Theo** (Salesforce) — token transformer.
- **W3C Design Tokens Format** — spec emergente 2024-2026 para interoperabilidade.

### KPIs de paleta corporativa

| Categoria | KPI | Alvo |
|---|---|---|
| Acessibilidade | % combos AA-passing | 100% obrigatorio |
| Acessibilidade | % combos AAA-passing texto principal | >70% |
| Consistencia | Cores fora do brand book usadas em 30 dias | <5 ocorrencias / mes |
| Reconhecimento | Brand color recall em pesquisa | >60% sem logo |
| Distintividade | Coincidencia com 5 concorrentes diretos | <2 cores em comum |
| Adocao interna | % equipes usando design tokens | >80% em 12 meses |

### Como medir reconhecimento de cor

1. **Survey pos-campanha**: "quando voce ve [cor X], qual marca voce pensa?" — % que cita marca.
2. **Eye-tracking**: heatmap em layout — quanto a cor de marca atrai visao.
3. **A/B test color variants**: medir conversao com cor primaria atual vs alternativa.
4. **Brand lift study** (Google/Meta): mede recall apos exposicao.

---

## Fundacao 8 — Aplicacao em Content MKT

### Cor em conteudo organico (social, blog)

- **Templates consistentes**: feed Instagram, capas YouTube, headers blog — sempre mesma paleta. Inconsistencia = ruido cognitivo.
- **Hierarquia de uso**: post tipo "novidade" usa accent color. Post tipo "educacional" usa primary. Post tipo "depoimento" usa neutral + acento sutil.
- **Carrosseis Instagram**: capa em primary + accent bold. Slides intermediarios em variacoes de primary. Slide final (CTA) em accent de alta saturacao.
- **YouTube thumbnails**: contraste extremo (texto branco sobre cor saturada de marca + outline preto). Ratio mais agressivo que web (>10:1).

### Cor em paid ads

- **A/B testing color CTA**: cor de marca vs accent vs verde semantico. Frequente: accent color converte mais que primary em CTA.
- **Paleta sazonal sobreposta a marca**: Black Friday adiciona preto+dourado, Natal adiciona vermelho+verde, Junina adiciona verde+amarelo+vermelho. Cor de marca permanece de fundo.
- **Coerencia com landing**: cor de ad e cor de hero da landing devem ser visualmente continuas. Quebra = friccao.

### Cor em email marketing

- **Header**: primary color + logo. Reforca reconhecimento em inbox lotada.
- **Botoes CTA**: accent color saturado, contraste alto, padding generoso. Cores de marca testadas para nao serem filtradas como "promo" pelo Gmail.
- **Modo escuro Gmail/Outlook**: ~50% usuarios estao em dark mode 2026. Use logo PNG com transparencia + fallback `<img bgcolor>`. Texto em cor neutral suficientemente contrastante em ambos modos.

### Cor em apresentacoes / PDFs / decks

- **Master slide**: paleta restrita (3-4 cores). Reduz ruido em deck longo.
- **Charts e graficos**: usar paleta dedicada de "data viz" — distinguivel por colorblind, ordenavel (ex.: ColorBrewer schemes). Marca pode entrar em titulo, accents, mas nao nos dados.
- **PDF print-ready**: gere em CMYK + Pantone se for impressao premium. PDF/X-1a para grafica.

### Sazonalidade vs marca permanente

- **Permanente**: brand book imutavel por 5-10 anos.
- **Campanha**: paletas tematicas sobrepoem (Halloween laranja+preto, Pride rainbow). Sempre **complementam**, nunca **substituem** a primary.
- **Risco**: campanhas excessivas dissolvem identidade. Regra: campanha pode ocupar ate 40% do feed, marca permanente >60%.

### SEO + cor (sim, ha conexao)

- **Imagens com texto-em-imagem com baixo contraste** prejudicam OCR de Google Images.
- **Alt text deve mencionar cores se relevante**: "logo Nubank em roxo sobre fundo branco".
- **CTRs de SERPs com favicons coloridos sao maiores** — defina favicon com cor de marca de alta saturacao.

### Cor + persona

- Persona Decision Maker (CFO, COO): paletas conservadoras, azul/cinza/preto, branca abundante.
- Persona Crescimento (CEO startup, VP growth): paletas vibrantes, accents ousados.
- Persona Tecnica (CTO, dev): dark mode-friendly, ciano/roxo/teal, neon discreto.
- Persona Consumidor jovem (Z, alpha): hipersaturado, gradientes ousados, OKLCH-rich.

---

## Anti-Patterns 18

1. **Escolher cor "porque eu gosto"** — gosto pessoal nao define marca. Escolha estrategica baseada em concorrencia, publico, atributos.
2. **Copiar paleta do concorrente** — diluem ambas. Diferenciacao cromatica e ativo competitivo.
3. **Ignorar WCAG no design inicial** — refazer depois custa 3-5x. Build accessibility-first.
4. **Usar SO cor para informacao critica** — exclui 8% homens daltonicos. Combine cor + icone + texto + padrao.
5. **Paleta inflada (15+ cores)** — diluem reconhecimento. Maximo 5-7 cores ativas (incluindo neutrals).
6. **Falta de escala de tons** — sem 9-10 variacoes por cor, design system trava.
7. **Inverter literalmente para dark mode** — fadiga visual. Use camadas de escuridao + ajustes de chroma.
8. **Pantone aleatorio sem checagem fisica** — converte digital -> impresso e descobre que cor "explodiu" so no off-press.
9. **Usar `#000` puro em OLED** — parece buraco. Use `#0A0A0A` ou `#121212`.
10. **Vermelho+verde puros como diferenciador** — pesadelo daltonico. Use azul+laranja, ou adicione rotulos.
11. **Saturar excessivamente cores em dark mode** — vibracao otica. Reduza chroma 10-30%.
12. **Esquecer Pantone Uncoated quando arte vai para papel offset** — reproducao 10-15% mais opaca surpreende cliente.
13. **Brand book em PDF estatico, sem tokens** — equipe de dev nao usa. Crie tokens (Style Dictionary, Token Studio).
14. **Reescolher paleta a cada CMO novo** — destroi BiP acumulado. Refresh sim, rebuild raro.
15. **Cor de marca em texto corrido** — `#820AD1` como cor de paragrafo cansa. Reserve para titulos, links, accents.
16. **Cores 3D / gradientes anos 2010 em 2026** — datado salvo se for retro intencional. 2026: gradientes OKLCH suaves OU flat.
17. **Logo monocromatico que nao funciona em variantes** — teste logo em primary, neutrals, branco sobre primary, preto sobre primary, sobre foto. Falha = redesenho.
18. **Documentar cor so em HEX** — print, branding fisico, video broadcast pedem CMYK, Pantone, LAB. Sempre tabela completa.

---

## 18 Regras de Ouro

1. **Sempre teste WCAG no momento de escolher** — nao decida "validamos depois". Cor que falha 4.5:1 sobre branco/preto exige variantes desde dia 1.
2. **Pesquise white space cromatico do setor** — liste 10 concorrentes, mapeie cores, identifique gaps. Diferenciacao = ativo.
3. **Comece com 1 primary forte, 2 secondary, 1 accent** — paleta minima. Expanda apenas com necessidade comprovada.
4. **Documente em 5 sistemas: HEX, RGB, CMYK, Pantone C, Pantone U** (+LAB e OKLCH em 2026). Brand book completo.
5. **Crie escala de 9-10 tons por cor** (50, 100, 200... 900). Inspire-se em Tailwind, Material, Radix Colors.
6. **Defina semantic colors** (success/danger/warning/info) separadas das cores de marca. Confunde-las gera UX ruim.
7. **Tokens semanticos > tokens literais** — `color.text.primary` sobrevive a rebrand; `color.gray-900` nao.
8. **Light + dark sao iguais em peso** — projete os dois. Nao trate dark como "afterthought".
9. **Combine cor + icone + texto + padrao** sempre que cor transmite informacao critica.
10. **Cultural check obrigatorio para mercados novos** — cor que "funciona" no Brasil pode ofender em outros mercados. Pesquise.
11. **Pantone para tiragens grandes / arte premium** — consistencia perfeita justifica custo extra. CMYK puro para tiragens pequenas / variaveis.
12. **OKLCH para escalas modernas (2026)** — perceptualmente uniforme, gradientes saudaveis, browser support consolidado.
13. **Refresh a cada 5-10 anos, nao a cada CMO novo** — cor envelhece (saturacao/lightness), mas BiP acumulado e ativo.
14. **Teste com simulador de daltonismo antes de fechar** — 8% homens, 0,5% mulheres. Coblis, Stark, DevTools.
15. **Escala de neutrals quente OU fria, escolha** — misturar cinzas frios e quentes gera ruido. 2026 trend: warm neutrals.
16. **Cor de brand nao e cor de CTA por default** — testar A/B. Frequente: accent color converte mais.
17. **Aplique 60-30-10** (ou 50-30-15-5 com neutrals) — equilibrio composicional fundamental.
18. **Brand book vivo em ferramenta colaborativa** — Figma, Notion, ZeroHeight. PDF morre na pasta.

---

## Exemplos Comportamentais

### Persona 1 — Brand Designer em agencia BR (junior-mid)

**Cenario**: cliente fintech B2B pede paleta para marca nova. Quer "azul moderno mas diferente".

**Aplicacao**:
1. **Pesquisa concorrencia**: lista 15 fintechs BR (Nubank=roxo, C6=preto+dourado, PicPay=verde, Stone=verde-neon, BTG Pactual=azul-marinho, XP=preto+laranja). Identifica que azul-petroleo / azul-eletrico nao estao saturados.
2. **Define primary**: oklch(50% 0.18 235) — azul-eletrico vibrante. HEX `#0066D6`. Pantone 2935 C aproximacao.
3. **Constroi escala**: gera 9 tons em OKLCH mantendo H=235.
4. **Secondary**: ciano-pastel `#7DD3FC` (apoio claro), grafite `#1F2937` (apoio escuro).
5. **Accent**: laranja-coral `#FB7185` para CTAs (split-complementar com azul).
6. **Neutrals**: 7 cinzas neutros (zinc do Tailwind).
7. **Semantic**: success `#10B981`, danger `#EF4444`, warning `#F59E0B`, info usa propria primary.
8. **Valida WCAG**: testa todos textos sobre todos fundos no Stark. Ajusta tons que falham.
9. **Documenta**: brand book Figma com 5 sistemas de cor (HEX/RGB/CMYK/Pantone C/Pantone U) + tokens JSON.
10. **Apresenta com mockups**: 5 telas reais (landing, app, social, anuncio, pitch deck) — cliente ve em contexto, nao swatch.

### Persona 2 — CMO em fintech BR (experiente)

**Cenario**: marca tem 4 anos. Paleta original "improvisada" pelo founder. Cliente B2B reclama que "parece startup imatura". Refresh sem rebuild.

**Aplicacao**:
1. **Audit atual**: brand designer mapeia onde paleta atual aparece. Identifica que 80% do uso e em 1 cor primaria + branco. Paleta "oficial" tem 12 cores mas so 3 usadas.
2. **Pesquisa qualitativa**: 8 entrevistas com clientes B2B atuais sobre percepcao da marca. "Jovem demais" e tema recorrente.
3. **Decisao estrategica**: manter primary (BiP), reformular secondaries para tons mais sofisticados (graficos sobrios), ajustar accent para algo mais discreto.
4. **WCAG audit**: 30% das combos atuais falham AA. Refresh resolve sistemicamente.
5. **Roll-out faseado**: novo brand book em mes 1, atualizacao do site em mes 2-3, materiais comerciais em mes 4-6, papelaria em mes 6-9.
6. **Mensuracao**: brand lift study antes/depois. Recall de cor primaria mantido (objetivo). Percepcao "profissional" sobe (objetivo).

### Persona 3 — Dev Frontend em SaaS (mid)

**Cenario**: brand book em PDF. Time design entrega sketches em Figma. Codigo tem `#820AD1`, `#820BD2`, `#7F0BD0` espalhados — drift.

**Aplicacao**:
1. **Cria design tokens**: arquivo `tokens.json` no W3C Design Tokens Format com toda paleta primary/secondary/tertiary/neutrals/semantic com escalas 9-10.
2. **Style Dictionary**: configura para gerar `tokens.css` (CSS vars), `tokens.ts` (TypeScript), `tokens.dart` (Flutter), `tokens.xml` (Android).
3. **CI/CD**: pipeline que falha PR se houver cor literal `#XXXXXX` no codigo (regex check).
4. **Migra codigo legado**: codemod substitui `#820AD1` por `var(--color-brand-500)`. PR by PR.
5. **Cria Storybook color page**: documentacao visual interativa para devs e designers, gerada do mesmo tokens.json.
6. **Onboarding**: novos devs leem o color.md (gerado do tokens) antes de comitar.

### Persona 4 — Founder solo em agencia digital

**Cenario**: cliente PME (R$ 5-20M faturamento, comercio local) precisa de identidade. Orcamento pequeno. Quer rebrand em 2 semanas.

**Aplicacao**:
1. **Briefing rapido**: 1h. Atributos? Concorrencia? Publico? Onde aplica? Imagens que gosta?
2. **Workflow Coolors**: gera 20 paletas em 30min. Filtra com lock primary candidate.
3. **Adobe Color**: refina harmonia, valida contraste.
4. **3 paletas finalistas**: apresenta com mockups (logo + landing + IG post + anuncio Meta).
5. **Cliente escolhe**: validar WCAG, gerar tokens em Notion (free), documentar em PDF + canva (cliente pode editar).
6. **Entregaveis**: brand book leve (5 paginas), Figma file shared, kit Canva com templates aplicando paleta.
7. **Acompanhamento**: 30 dias gratis para ajustes de aplicacao (nao de cor).

---

## Checklist Contraditorio Interno (10 perguntas)

1. **A cor primary diferencia da concorrencia?** Mapeei 10+ concorrentes? Existe white space cromatico? Ou estou copiando lider?
2. **Todas as combos de texto sobre fundo passam AA?** Rodei contrast checker em **todas** combinacoes? Tenho variantes para casos que falham?
3. **A paleta funciona em colorblindness simulators?** Testei em Coblis (deuteranopia, protanopia, tritanopia)? Informacao critica nao depende SO de cor?
4. **Tenho versoes em 5 sistemas (HEX/RGB/CMYK/Pantone C/Pantone U)?** Brand book lista todos? Print sera reproduzivel sem surpresa?
5. **Minha paleta tem escala de 9-10 tons por cor?** Ou tenho so 1 valor e improvisarei? Suficiente para cobrir hover/active/disabled/dark mode?
6. **Defini semantic colors separadas?** Sucesso, erro, warning, info estao definidos e nao se confundem com cores de marca?
7. **Existe versao dark mode validada?** Cor primary mantem reconhecimento + contraste + nao satura excessivamente em fundo escuro?
8. **Minha paleta funciona em escala (favicon 16px ate billboard 10m)?** Cor mantem identidade em todos os tamanhos? Ou some quando pequena?
9. **Cultural check feito para mercados-alvo?** Pesquisei significados em paises onde marca opera/operara? Roxo nao significa luto onde estarei?
10. **Existem tokens (nao so PDF)?** Time de dev tem como consumir paleta sem hardcode? Style Dictionary, Token Studio, ou equivalente?

---

## Referencias

### W3C / WCAG / Accessibility

- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
- [WebAIM Contrast and Color Accessibility](https://webaim.org/articles/contrast/)
- [W3C WCAG 2.1 - Contrast Minimum 1.4.3](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html)
- [W3C WCAG 2.1 - Contrast Enhanced 1.4.6](https://www.w3.org/WAI/WCAG21/Understanding/contrast-enhanced.html)
- [W3C WCAG 2.1 - Use of Color 1.4.1](https://www.w3.org/WAI/WCAG21/Understanding/use-of-color.html)
- [Accessible Web Color Contrast Checker](https://accessibleweb.com/color-contrast-checker/)
- [Free WCAG Contrast Checker - colorpalettegenerator.io](https://colorpalettegenerator.io/tools/contrast-checker/)
- [12 Best Color Contrast Tools 2026 - Lollypop Design](https://lollypop.design/blog/2026/april/12-best-color-contrast-tools-for-wcag-accessibility-testing/)
- [Color Contrast for Accessibility WCAG Guide 2026 - Webability](https://www.webability.io/blog/color-contrast-for-accessibility)
- [UCLA Brand Accessibility Guidelines](https://brand.ucla.edu/fundamentals/accessibility/color-type)
- [Stark Accessibility Tools](https://www.getstark.co/)
- [Polypane Browser](https://polypane.app/)

### Color Tools 2026

- [Coolors](https://coolors.co/)
- [Adobe Color](https://color.adobe.com/)
- [Color Hunt](https://colorhunt.co/)
- [Khroma AI Color](https://khroma.co/)
- [Huemint](https://huemint.com/)
- [Realtime Colors](https://realtimecolors.com/)
- [Color Palette Tools 2026 - Muzli Blog](https://muz.li/blog/best-color-palette-tools-and-generators-for-designers-2026/)
- [Coolors vs Adobe Color vs Paletton 2026](https://www.toolcenter.ai/en/articles/coolors-vs-adobe-color-vs-paletton-best-color-palette-tool)
- [Best Color Palette Tools 2026 Tested - Colorkit](https://colorkit.store/blog/best-color-palette-tools-comparison/)
- [Color Designer Platform](https://colordesigner.io/)

### Pantone & Print

- [Pantone Connect Official](https://www.pantone.com/pantone-connect)
- [Free Online Pantone Colors Chart 2026](https://pantonecolors.net/)
- [Chromafinder Pantone Solid Coated Converter](https://www.chromafinder.com/pantone-solid-coated)
- [Chromafinder Pantone Uncoated Converter](https://www.chromafinder.com/pantone-uncoated)
- [Pantone to CMYK Converter Vectorization](https://vectorization.eu/pantone-to-cmyk-converter/)
- [CMYK to Pantone Converter DNS Checker](https://dnschecker.org/convert-cmyk-to-pantone-pms.php)
- [PMS Color Chart Guide - Custom Product Packaging](https://www.customproductpackaging.com/blog/pms-color-chart)
- [Ginifab CMYK to Pantone](https://www.ginifab.com/feeds/pms/cmyk_to_pantone.html)
- [Printmoz Pantone to CMYK Guide](https://www.printmoz.com/blog/pantone-to-cmyk)

### OKLCH / Modern Color Spaces

- [OKLCH Color Picker - Lea Verou](https://oklch.com/)
- [Huetone - Andrey Sitnik](https://huetone.ardov.me/)
- [CSS Color Module Level 4 W3C](https://www.w3.org/TR/css-color-4/)
- [Bjorn Ottosson OKLab Original Post](https://bottosson.github.io/posts/oklab/)

### Color Trends 2026

- [Color Trends 2026 - FreeLogoServices](https://www.freelogoservices.com/blog/color-trends-2026/)
- [Color Trends 2026 - VistaPrint](https://www.vistaprint.com/hub/color-trends)
- [Branding Color Palette Trends 2026 - Five Star Logo](https://www.fivestarlogo.com/post/branding-color-palette-trends-2026)
- [Brand Colors 2026 - BrandCloud](https://www.brandcloud.pro/en/blog/brand-colors-in-2026-how-to-choose-them-and-keep-them-consistent-across-channels)
- [Top 10 Color Trends 2026 - LogoMaker](https://www.logomaker.com/blog/color-trends/)
- [Color Design Trends 2026 - Sage Design](https://sagedesigngroup.biz/color-design-trends-for-2026-what-brands-designers-should-watch/)
- [30 Creative Color Palettes 2026 - Zeka Design](https://www.zekagraphic.com/30-creative-color-palette-ideas-for-2026/)
- [Modern Color Palette UI/UX 2026 - Recursion](https://recursion.software/blog/ui-color-trends-2026)
- [2026 Color Trends Brand Marketing - Pulse Advertising](https://www.pulse-advertising.com/resources/social-media-news/2026-color-trends-brand-marketing-strategy/)
- [Brand Colour Trends 2026 - Inkbot Design](https://inkbotdesign.com/brand-colour-trends/)

### Dark Mode

- [Dark Mode Best Practices 2026 - Tech-RZ](https://www.tech-rz.com/blog/dark-mode-design-best-practices-in-2026/)
- [Dark Mode UI/UX Best Practices - Inkbot](https://inkbotdesign.com/dark-mode/)
- [Best Practices Dark Mode Web Design 2026 - NateBal](https://natebal.com/best-practices-for-dark-mode/)
- [Dark Mode Design Converts - Digital Silk](https://www.digitalsilk.com/digital-trends/dark-mode-design-guide/)
- [6 Dark Mode Color Palette Ideas - Vev Design](https://www.vev.design/blog/dark-mode-website-color-palette/)
- [30+ Stunning Color Palettes Top Brands 2026 - Inkbot](https://inkbotdesign.com/stunning-colour-palettes/)

### Cultural Color

- [How Color is Perceived by Cultures - Eriksen](https://eriksen.com/marketing/color_culture/)
- [International Color Marketing Guide - Six Degrees](https://www.six-degrees.com/an-international-guide-on-the-use-of-color-in-marketing-advertising/)
- [Cultural Context Color Branding - LogoDesign.net](https://www.logodesign.net/blog/culture-shapes-color-choices/)
- [Color Symbolism Across Cultures - FrontMatter](https://www.frontmatter.io/blog/how-color-symbolism-influences-design-and-marketing-across-cultures)
- [Psychology of Color Cultural Differences - Eminent SEO](https://www.eminentseo.com/blog/the-psychology-of-color-in-marketing-and-why-cultural-differences-matters/)
- [Cultural Color Perception in Branding - Visual Communication Guy](https://thevisualcommunicationguy.com/2025/02/12/cultural-color-perception-how-culture-influences-color-interpretation-in-branding/)
- [Color Psychology Marketing Branding - Help Scout](https://www.helpscout.com/blog/psychology-of-color/)
- [Colors Cultures Marketing - AbroadLink](https://abroadlink.com/blog/colours-cultures-and-marketing)

### Color Theory & Foundations

- [ColorBrewer 2 - Cynthia Brewer](https://colorbrewer2.org/)
- [Refactoring UI Color - Adam Wathan & Steve Schoger](https://refactoringui.com/)
- [Material Design 3 Color System](https://m3.material.io/styles/color/system/overview)
- [Tailwind CSS Color Palette](https://tailwindcss.com/docs/colors)
- [Radix Colors](https://www.radix-ui.com/colors)

### Design Tokens

- [Style Dictionary Amazon](https://amzn.github.io/style-dictionary/)
- [Token Studio Figma](https://tokens.studio/)
- [W3C Design Tokens Format Module](https://www.designtokens.org/)

### Colorblindness Tools

- [Coblis Color Blindness Simulator](https://www.color-blindness.com/coblis-color-blindness-simulator/)
- [Sim Daltonism macOS](https://michelf.ca/projects/sim-daltonism/)

---

## Cross-Skill References

- **logo-design-process**: aplicacao da paleta no logotipo, decisao primary vs secondary no logomarca.
- **brand-book-methodology**: documentacao formal da paleta no brand book corporativo.
- **tipografia-corporativa**: combos cor + fonte, contraste de texto sobre fundo.
- **iconografia-corporativa**: paleta aplicada ao sistema de icones, semantica visual.
- **svg-engineering-ia**: tokens de cor em SVGs, currentColor, dark mode SVG.
- **acessibilidade-wcag**: conformidade completa WCAG 2.1 / 2.2, audit metodologico.
- **design-system-basico**: integracao de paleta como tokens semanticos no design system.
- **branding**: estrategia de marca holistica onde cor e ativo BiP.
- **composicao-visual**: aplicacao da regra 60-30-10, hierarquia cromatica em layouts.
- **infograficos-diagramas**: paletas de data viz acessiveis e consistentes com marca.

---

## Integracao Ecossistema Frank-MKT

Esta skill e a 3a do Bloco Identidade Visual Corporativa / Brand Design e atua como spine de cor para todas as deliverables visuais do ecossistema:

- **Pre-requisitos**: branding (estrategia), posicionamento-marca (white space), persona-icp-deep (publico-alvo).
- **Co-execucao**: logo-design-process, tipografia-corporativa, iconografia-corporativa, brand-book-methodology.
- **Downstream**: composicao-visual aplica regra 60-30-10; infograficos-diagramas usa paleta de data viz; svg-engineering-ia consome tokens.
- **Compliance gate**: acessibilidade-wcag valida todos os outputs.
- **Operacao**: design-system-basico transforma paleta em tokens consumidos por dev frontend e equipes de produto.

Use esta skill ao iniciar projeto de identidade nova, refresh de marca, audit de paleta legada, ou expansao para novo mercado/canal.

---

**Disclaimer educational**: este conteudo e referencial e educacional. Cores especificas mencionadas (Nubank, Magalu, Itau, Pantone) sao aproximacoes publicas para fins didaticos e nao substituem brand books oficiais das marcas. Decisoes de cor para uma marca real devem considerar contrato de uso, registro de marca, pesquisa primaria de publico, e validacao tecnica (provas Pantone fisicas, audit WCAG completo, testes de daltonismo). Esta skill nao substitui consultoria profissional de brand designer ou auditoria oficial de acessibilidade. URLs e ferramentas mencionadas sao referencias publicas validas em 2026-05-09; sempre verifique disponibilidade e termos de uso atuais.
