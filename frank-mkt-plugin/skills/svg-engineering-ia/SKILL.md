---
name: svg-engineering-ia
description: Engenharia de SVG via IA (Claude/LLMs) — geracao programatica de imagens vetoriais complexas + W3C SVG 2.0 + LLMs gerando SVG (estado da arte 2026 VGBench/SVGenius/LLM4SVG/Chat2SVG/OmniSVG) + bitmap-vetor (Potrace/AutoTrace/AI tracing) + rasterizacao (Resvg/Sharp/Headless Chrome) + composicao complexa (paths/transforms/symbols/masks/clipPaths/filters) + auto-validacao IA sem visao (PSS metric + heuristics + render-loop) + tooling hibrido (Inkscape/Figma/Boxy SVG + SVGO + D3/GSAP/p5.js 2.0). SKILL INOVADORA — trata o gap real LLM-texto vs geracao vetorial complexa. Skills Avancadas / Experimentais.
volatility: medium
last_review: 2026-05-09
next_review: 2026-11-09
languages: [pt-BR]
audience: [designers, brand-designers, devs-frontend, founders, agencias-design, prompt-engineers, ai-engineers, generative-artists]
ascii_only: true
---

# Skill: svg-engineering-ia

## Decaimento Temporal

- volatility: medium
- last_review: 2026-05-09
- next_review: 2026-11-09
- Justificativa: Fundamentos SVG (W3C 2.0 specification + path commands + viewBox + transforms) sao **estaveis decadas**. MAS estado da arte LLM-gerando-SVG evolui rapido (VGBench EMNLP 2024 + SVGenius 2025 + LLM4SVG CVPR 2025 + Chat2SVG CVPR 2025 + OmniSVG + Claude Design Apr-2026 todos publicados em 18 meses). Tooling IA-hybrid (resvg + p5.js 2.0 + SVGO) tambem evolui. Revisar semestral para atualizar benchmarks LLM, novos modelos VLM, novas tecnicas auto-validacao.

## Visao Geral

Esta skill resolve um **gap real** que NENHUMA outra skill do plugin frank-mkt aborda: como fazer Claude (e LLMs em geral) **gerar SVG complexo + esteticamente correto** sem ter visao do que cria. SVG e formato textual XML — perfeito para LLMs em teoria — mas LLMs sao "text models doing visual tasks" (Praeclarum 2023) e enfrentam fraqueza estrutural em **raciocinio espacial e geometrico**.

**Estado da arte 2026** (VGBench EMNLP 2024 + SVGenius 2025 + LLM4SVG CVPR 2025): LLMs sao **strong em high-level vector languages** (TikZ + Graphviz) mas **weak em low-level SVG**, especialmente em tarefas que exigem reasoning matematico ou construcao precisa de coordenadas. Pelican-on-bicycle benchmark (Simon Willison Nov-2025) virou folclore como teste-de-Turing visual para LLMs.

**Solucoes hibridas** emergem: Chat2SVG (CVPR 2025) combina LLM (semantic templates) + image diffusion (SDEdit + ControlNet) + Score Distillation Sampling (SDS) bridging raster→SVG via PyDiffVG. OmniSVG (2025) usa Vision-Language Models (VLMs) end-to-end para Text-to-SVG + Image-to-SVG + Character-Reference. **Claude Design** (Anthropic Labs Apr-17-2026) gera prototypes/decks/slides/UI mockups via Opus 4.7.

Esta skill organiza 4 frentes:
1. **Fundamentos SVG W3C** (paths + transforms + viewBox + composition primitives)
2. **LLMs gerando SVG 2026** (capacidades + limitacoes + tecnicas prompting)
3. **Conversao bitmap-vetor** (Potrace/AutoTrace + AI tracing) + **rasterizacao** (Resvg/Sharp/Headless Chrome)
4. **Auto-validacao IA sem visao** (PSS metric + heuristics geometricas + render-loop self-correction)

Esta skill e para **founders bootstrapando logos/icones simples** via Claude Artifacts (R$ 0 budget, MVP visual), **brand designers** que querem hybrid workflow (Claude draft → Illustrator refine → SVGO optimize → deploy), **devs frontend** integrando D3/GSAP com SVG programatico, **agencias** entregando icon systems escalaveis, **prompt engineers/AI engineers** construindo pipelines visual-com-IA, e **artistas generativos** explorando p5.js 2.0 + creative coding.

Skill INOVADORA porque:
- (a) trata um gap pratico real LLM-texto vs visual nao coberto por outras skills do plugin;
- (b) sintetiza estado da arte academico (4 papers CVPR/EMNLP 2024-2025) com pratica industrial (Anthropic Claude Design + 8 ferramentas comerciais 2026);
- (c) traz framework auto-validacao para Claude validar criticamente seus proprios SVGs sem visao;
- (d) base ferramental para skills brand-design futuras (logo-design-process + iconografia-corporativa em construcao).

## Fundacao 1 — SVG Foundations + W3C Specification 2.0

**SVG (Scalable Vector Graphics) 2.0** e W3C Recommendation — linguagem XML para descrever graficos 2D vetoriais e mistos vetor/raster. Especificacao oficial: [w3.org/TR/SVG2](https://www.w3.org/TR/SVG2/).

### Estrutura raiz

```xml
<svg xmlns="http://www.w3.org/2000/svg"
     viewBox="0 0 100 100"
     width="200"
     height="200"
     role="img"
     aria-labelledby="title-id desc-id">
  <title id="title-id">Logo Empresa X</title>
  <desc id="desc-id">Logotipo composto por circulo azul e simbolo abstrato.</desc>
  <!-- conteudo aqui -->
</svg>
```

**Atributos criticos**:
- `xmlns="http://www.w3.org/2000/svg"` — MANDATORY (sem isto, browsers podem tratar como XML generico)
- `viewBox="min-x min-y width height"` — define **sistema de coordenadas internas**; permite escalabilidade independente de width/height absolutos
- `width` + `height` — dimensoes fisicas (pixels, em, %, etc); pode-se omitir e deixar viewBox controlar via CSS
- `role="img"` + `aria-labelledby` — acessibilidade

### Path element (mais poderoso)

`<path d="...">` — elemento dominante (todas icon libraries Lucide/Heroicons/Phosphor usam paths sob o capo). Comandos `d`:

| Comando | Significado | Sintaxe |
|---------|-------------|---------|
| `M x y` | moveto (move ponto sem desenhar) | `M 10 10` |
| `L x y` | lineto (linha reta ate x,y) | `L 90 90` |
| `H x` | linha horizontal ate x | `H 90` |
| `V y` | linha vertical ate y | `V 90` |
| `C x1 y1, x2 y2, x y` | cubic bezier (2 control points) | `C 20 20, 40 20, 50 10` |
| `S x2 y2, x y` | smooth cubic (control1 reflection) | `S 60 0, 70 10` |
| `Q x1 y1, x y` | quadratic bezier (1 control point) | `Q 30 5, 50 10` |
| `T x y` | smooth quadratic (control reflection) | `T 70 10` |
| `A rx ry rotation large-arc sweep x y` | elliptical arc | `A 25 25 0 0 1 50 50` |
| `Z` | closepath (fecha shape ligando ao M inicial) | `Z` |

**Maiusculas = absolutas; minusculas = relativas** ao ponto atual (importante para parametrizacao).

**Cubic Bezier intuicao** (Josh W. Comeau Interactive Guide):
- `C x1 y1, x2 y2, x y` — curva inicia direcao **(x1,y1)** e chega na direcao **(x2,y2)**, terminando em **(x,y)**
- Control points NAO sao tocados pela curva — sao "imas" que puxam a curva

**Elliptical Arc** (Smashing Magazine Jun-2025): `A rx ry rotation large-arc-flag sweep-flag x y` — browser **inventa elipse hipotetica** que contem ponto inicial + final na circunferencia. `large-arc-flag` (0/1) = arco menor/maior; `sweep-flag` (0/1) = direcao horario/anti-horario.

### Basic shapes (atalho para casos simples)

- `<rect x y width height rx ry/>` — retangulo (rx, ry para corner radius)
- `<circle cx cy r/>` — circulo
- `<ellipse cx cy rx ry/>` — elipse
- `<line x1 y1 x2 y2/>` — linha
- `<polyline points="..."/>` + `<polygon points="..."/>` — multi-linhas / poligonos

**Conversao mental**: rect → 4 lineto + close; circle → 2 elliptical arcs (truque: nao ha "circle command" em path, usa-se A com large-arc+sweep para meio circulo cada).

### Transforms

`transform="translate(x y) rotate(deg cx cy) scale(sx sy) skewX(deg) skewY(deg) matrix(a b c d e f)"`

- Aplicacao **da direita pra esquerda** (translate ultimo aplica primeiro)
- `transform-origin` para mudar pivot (CSS svg only)
- Aninhar `<g transform="...">` para grupos transformaveis

### Text

`<text x y font-family font-size fill>...texto...</text>` + `<tspan>` para sub-spans + `<textPath href="#path-id">` para texto seguindo path.

**Cuidado fonts**: SVG nao embute font automaticamente. Use **font-family Web-safe** (Arial/Helvetica/Times) ou embed via `@font-face` em `<style>` interno, ou converta texto em paths (mais portavel mas perde editabilidade).

### Coordenadas e precisao

ViewBox define **dominio coordenado abstrato**. Convencao 2026:
- Icons **24x24** (Lucide/Heroicons) ou **32x32** (Phosphor)
- Logos **100x100** ou **200x200** (precisao decimal flexivel)
- Illustrations **800x600** ou maiores

**Precisao decimal**: 2 casas decimais (`12.34`) tipico. Mais que 4 casas e poluicao (SVGO trim default = 3 casas).

### Referencias W3C + tutoriais

- [W3C SVG 2 Specification](https://www.w3.org/TR/SVG2/) — normative
- [W3C Paths](https://www.w3.org/TR/SVG/paths.html) — paths chapter
- [SVG Working Group Paths Editor's Draft](https://svgwg.org/specs/paths/) — features dropped from SVG 2 + futuro
- [MDN SVG Tutorial Paths](https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorials/SVG_from_scratch/Paths)
- [Josh W. Comeau Interactive Guide to SVG Paths](https://www.joshwcomeau.com/svg/interactive-guide-to-paths/) — visualizacao interativa
- [Smashing Magazine Decoding SVG Path Element](https://www.smashingmagazine.com/2025/06/decoding-svg-path-element-curve-arc-commands/) — curve + arc deep-dive
- [SSSVG Interactive SVG Reference (fffuel)](https://www.fffuel.co/sssvg/)

## Fundacao 2 — LLMs Gerando SVG: Estado da Arte 2026

### Limitacao fundamental

LLMs sao **text models doing visual tasks**. Geram SVG como sequencia de caracteres baseada em padroes de treinamento — **NAO veem** o que criam. Implicacoes:
- **Fraqueza estrutural em raciocinio espacial e geometrico** (VGBench EMNLP 2024)
- Erros tipicos: paths nao fechados, coordenadas erradas, viewBox incompativel com conteudo, simetria quebrada, proporcoes off
- "Common-sense" reasoning quando nao prompted explicitamente para mostrar trabalho passo-a-passo

### Benchmarks academicos (2024-2026)

**VGBench (EMNLP 2024)** — primeiro benchmark abrangente vector graphics: 4279 multi-choice QA + 5845 VG-caption pairs. Achado: LLMs **strong em high-level VG languages** (TikZ + Graphviz) mas **weak em low-level SVG**, especialmente reasoning. Paper: [aclanthology.org/2024.emnlp-main.213](https://aclanthology.org/2024.emnlp-main.213.pdf) | Site: [vgbench.github.io](https://vgbench.github.io/).

**SVGenius (2025)** — benchmark canonico LLM SVG (understanding + editing + generation). Paper: [arxiv.org/html/2506.03139v1](https://arxiv.org/html/2506.03139v1). Introduz **PSS (Path-Structure Similarity Score)** — extrai e compara comandos path + atributos + organizacao hierarquica para avaliar alinhamento geometrico-sintatico.

**LLM4SVG (CVPR 2025)** — Empowering LLMs to Understand and Generate Complex Vector Graphics. Paper: [openaccess.thecvf.com CVPR2025](https://openaccess.thecvf.com/content/CVPR2025/papers/Xing_Empowering_LLMs_to_Understand_and_Generate_Complex_Vector_Graphics_CVPR_2025_paper.pdf). Tecnica: structured SVG semantic representation que LLMs entendem melhor.

**Pelican-on-Bicycle Benchmark** (Simon Willison Nov-2025) — folclore: testar LLMs pedindo "Generate an SVG of a pelican riding a bicycle". Reveals coordinate-system construction skills + Bezier parameter understanding. Sem reasoning correto → unclosed paths + wrong coordinates. Disponivel: [simonwillison.net/2025/Nov/25/llm-svg-generation-benchmark/](https://simonwillison.net/2025/Nov/25/llm-svg-generation-benchmark/).

### Hybrid LLM + Diffusion approaches

**Chat2SVG (CVPR 2025)** — hybrid framework: LLM gera **semantic templates** + image diffusion (SDEdit + ControlNet) refina + **Score Distillation Sampling (SDS)** bridges raster→SVG via **PyDiffVG**. Site: [chat2svg.github.io](https://chat2svg.github.io/) | Code: [github.com/kingnobro/Chat2SVG](https://github.com/kingnobro/Chat2SVG).

**OmniSVG** — unified framework Vision-Language Models (VLMs) end-to-end multimodal SVG generation: Text-to-SVG + Image-to-SVG + Character-Reference. Site: [omnisvg.github.io](https://omnisvg.github.io/).

**PyTorch-SVGRender** — open-source differentiable rendering: text-to-SVG + Image-to-SVG + SVG Editing. [github.com/ximinng/PyTorch-SVGRender](https://github.com/ximinng/PyTorch-SVGRender).

### Claude SVG capabilities (Anthropic 2026)

- **Claude Artifacts** — gera SVG visual diretamente em chat (logos simples, brand graphics, icones)
- **Claude Design (Apr-17-2026)** — Anthropic Labs research preview: prototypes + pitch decks + slides + one-pagers + UI mockups via Opus 4.7. Disponivel Pro/Max/Team/Enterprise. [buildfastwithai.com](https://www.buildfastwithai.com/blogs/claude-design-anthropic-guide-2026)
- **MCP integrations** — Claude conecta image generators externos (DALL-E + Midjourney + Stable Diffusion) via Model Context Protocol
- **Limitacoes 2026**: Claude (como GPT-4) gera SVG como texto, sem visao. Para producao comercial seria, **hybrid workflow** (Claude draft → human refine) e padrao.

### GPT-4 vs Claude

GPT-4 (per VGBench): stronger em high-level VG languages (TikZ, Graphviz) que low-level SVG. Inferior em low-level SVG tasks especialmente reasoning. Quando nao prompted para mostrar trabalho, "common-sense" reasoning falha.

Claude (Opus 4.7+) — performance similar com nuances: ASCII clean output + structured XML + boa capacidade decomposicao em sub-tarefas. Mas mesma limitacao fundamental: **nao ve**.

### Tecnicas de prompting que funcionam (para Claude/GPT)

1. **Decomposicao explicita** (Comeau-style): em vez de "Generate logo of company X", quebrar em:
   - "Create a circle, centered at 50,50 with radius 40, fill blue"
   - "Add a triangle inside, equilateral, centered, fill white"
   - "Adjust triangle so it's visually centered (note: equilateral triangle centroid is at 1/3 height from base)"

2. **Show-your-work / chain-of-thought**: prompt explicito "Before writing SVG code, calculate coordinates step by step"

3. **viewBox-first**: especificar viewBox antes do conteudo. "viewBox 0 0 100 100. Place element at center (50,50)..."

4. **Reference templates**: fornecer SVG-template existente como starting point. LLM edita > LLM gera do zero (LLM4SVG insight).

5. **Constrained vocabulary**: solicitar apenas paths simples (M, L, C, Z) inicialmente; A (arc) e filters depois quando estrutura geometric correta.

6. **Explicit symmetry**: "the design must be symmetric across vertical axis x=50". Reforca constraint que LLM tende a violar.

7. **Iteracao com feedback humano**: render → observar gap → re-prompt com correcao especifica ("the eye is too far right, move x from 60 to 55").

8. **Self-validation embedded** (Fundacao 6): pedir LLM verificar geometricamente antes finalizar.

### Quando NAO usar LLM puro para SVG

- **Foto realista** ou **ilustracao complexa multi-elemento** com ~20+ shapes — usar **vetorizacao via Potrace/AI tracing** de imagem raster gerada por DALL-E/Midjourney/Stable Diffusion (Fundacao 3)
- **Producao comercial seria** — sempre hybrid (LLM draft → Illustrator/Inkscape refine humano)
- **Animation complexa** — usar GSAP ou D3 programaticamente, nao gerar SMIL via LLM (deprecated + dificil)
- **Charts data-driven** — D3.js bind data → SVG, NAO gerar via LLM (D3 e otimo nisso)

## Fundacao 3 — Bitmap → SVG (Vetorizacao)

Quando geracao SVG-direta via LLM falha (foto, ilustracao complexa), **vetorize**: gere imagem raster (DALL-E/Midjourney/Stable Diffusion) → converta para SVG via algoritmo.

### Potrace (canonico open-source)

[Potrace](https://potrace.sourceforge.net/) por Peter Selinger — converte bitmap → vector preservando formas suaves.

- **Input**: PBM, PGM, PPM, BMP (1-bit ou grayscale)
- **Output**: SVG, PDF, EPS, PostScript, DXF, GeoJSON, PGM, Gimppath, XFig
- **Ideal para**: line art, logos, scans, handwriting, simbolos
- **Algoritmo**: detecta boundaries de pixels + ajusta para Bezier curves suaves
- **Limitacao**: 1-bit (preto/branco). Para color, usar **Imagetracer.js** ou Inkscape's "Trace bitmap"

```bash
# CLI usage
potrace input.pbm -s -o output.svg

# Com Imagemagick para conversao previa
convert input.png -threshold 50% input.pbm
potrace input.pbm -s -o output.svg
```

### AutoTrace (multi-formato)

[AutoTrace](https://github.com/autotrace/autotrace) — Input: PNG, BMP, TGA, PNM (+ ImageMagick: JPEG, TIFF, GIF). Output: SVG, EPS, PDF, AI, DXF, CGM, EMF, MIF, ER, Fig.

```bash
autotrace -output-format svg -output-file output.svg input.png
```

### Modern AI tracing (CNN-based)

Algoritmos tradicionais (Potrace, Inkscape Trace, early Adobe Image Trace) detectam color boundaries e geram Bezier — **pixel-by-pixel**. Modern AI tracing usa **CNN trained on design datasets** que entendem **design intent** vs pixel edges:
- Reconhece que canto arredondado de letra "B" deve ser smooth circular curve, NAO poligono irregular
- Limpa noise + suaviza
- Detecta repeated elements (icon system inference)

### Ferramentas comerciais 2026

- **VectoSolve** — top-pick AI image-to-SVG 2026 (rapido, qualidade, accessible). [vectosolve.com](https://vectosolve.com/blog/best-ai-svg-generators-text-to-vector-2026)
- **Vectorizer.AI** — comercial, alta fidelidade
- **SVG Genie** — purpose-built vectorization + AI fix suggestions
- **Adobe Illustrator Image Trace** — industry standard, profundamente integrado workflow Adobe
- **Inkscape "Trace Bitmap"** — open-source, gratuito, multiple algorithms

### Workflow LLM + vetorizacao

```
1. Generate raster via DALL-E/Midjourney/Stable Diffusion (foto realista possivel)
2. Vetorize via VectoSolve / Adobe Illustrator / Potrace
3. Refine in Illustrator/Inkscape (limpar noise + ajustar paths)
4. SVGO optimize
5. Deploy
```

### Limitacoes vetorizacao

- **Fotos realistas** → vetor produz **enormes paths** (megabytes, perde escalabilidade real)
- **Gradientes complexos** → aproximam mal (mesh gradients raros)
- **Texto em foto** → fica como path curva (perde editabilidade textual)
- **Ideal**: line art, logos preto-branco, simbolos, ilustracoes flat-design 2D

## Fundacao 4 — SVG → Bitmap (Rasterizacao)

Operacao inversa: SVG → PNG/JPEG/WebP/AVIF. Use cases: Open Graph images social, thumbnails, PDF embedding, email (que nao suporta SVG inline confiavel), legacy systems.

### Resvg (Rust, leader 2026)

[Resvg](https://github.com/RazrFalcon/resvg) — performante server-side rasterizer Rust, 2017+. **Surpassed librsvg em qualidade + performance ja em 2021** (per MediaWiki SVG benchmarks).

- **resvg-js** — bindings JavaScript via WASM. Producao node-friendly.
- Renders quase 100% spec-compliant
- Standalone binary (sem deps de browser ou Cairo)

```javascript
// Exemplo resvg-js
const { Resvg } = require('@resvg/resvg-js');
const svg = `<svg ...>...</svg>`;
const resvg = new Resvg(svg, { fitTo: { mode: 'width', value: 800 } });
const pngBuffer = resvg.render().asPng();
```

### librsvg + rsvg-convert

GNOME project — rasterizer C historico. **rsvg-convert** CLI: faithful gradients, filters, transforms (mais preciso que ImageMagick para SVG).

```bash
rsvg-convert -w 800 -o output.png input.svg
```

### ImageMagick

Industry standard but **limited advanced SVG** (filters, complex gradients podem renderizar errado). Bom para basico, ruim para SVG sofisticado.

```bash
magick convert input.svg -density 300 output.png
```

### Sharp (Node.js)

[Sharp](https://sharp.pixelplumbing.com/) — popular Node.js image processing. Usa librsvg via libvips. Usado em production stacks (Next.js, Vercel, etc).

```javascript
const sharp = require('sharp');
sharp('input.svg').png().toFile('output.png');
```

### Headless Chrome + Puppeteer (highest fidelity)

Para SVG com **CSS + animations + filters complexos**, headless browser e ouro:
- Loads SVG em DOM real
- Renderiza com **mesma engine que browsers reais**
- Captura via screenshot
- Latencia maior (~300-1000ms cold start)

```javascript
const puppeteer = require('puppeteer');
const browser = await puppeteer.launch();
const page = await browser.newPage();
await page.setContent(`<html><body>${svg}</body></html>`);
const png = await page.screenshot({ omitBackground: true });
```

### Comparacao tools

| Tool | Performance | Spec compliance | Animations | CSS support |
|------|-------------|-----------------|------------|-------------|
| Resvg | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ❌ (no SMIL) | Limited |
| rsvg-convert | ⭐⭐⭐ | ⭐⭐⭐⭐ | ❌ | Limited |
| ImageMagick | ⭐⭐⭐⭐ | ⭐⭐ | ❌ | ❌ |
| Sharp (libvips) | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ❌ | Limited |
| Headless Chrome | ⭐⭐ (slow) | ⭐⭐⭐⭐⭐ | ✅ | ✅ Full CSS |

**Recomendacao 2026**: Resvg-js para 95% casos production. Headless Chrome para SVG com CSS animations / filters complexos.

## Fundacao 5 — Composicao Complexa

SVG nao e so paths simples — composicoes profissionais usam transforms aninhados, symbols reusables, masks/clipPaths, filters.

### Groups e transforms aninhados

```xml
<g transform="translate(50 50)">
  <g transform="rotate(45)">
    <rect x="-10" y="-10" width="20" height="20" fill="red"/>
  </g>
</g>
```
Aplicacao right-to-left: rotate primeiro, translate ultimo. **Quadrado 20x20 rotacionado 45° centrado em (50,50)**.

### Symbols + use (DRY)

```xml
<defs>
  <symbol id="star" viewBox="0 0 24 24">
    <path d="M12 2L15 9L22 9L17 14L19 21L12 17L5 21L7 14L2 9L9 9Z"/>
  </symbol>
</defs>

<use href="#star" x="0" y="0" width="48" height="48" fill="gold"/>
<use href="#star" x="60" y="0" width="48" height="48" fill="silver"/>
<use href="#star" x="120" y="0" width="48" height="48" fill="bronze"/>
```

Symbol pode ter **proprio viewBox** + ser referenciado N vezes via `<use>`. Padrao para **icon libraries** (Lucide/Heroicons fazem assim).

### ClipPath vs Mask

**Distincao critica** (W3C SVG 1.1 Masking + MDN):

- **clipPath** — **hard mask**: pixel ou totalmente visivel ou totalmente invisivel (binary, com anti-aliasing nas bordas). Performance melhor.
- **mask** — **soft mask**: pixel pode ser parcialmente transparente (gradients de transparencia possiveis). Mais flexivel, mais caro.

```xml
<!-- ClipPath (hard) -->
<defs>
  <clipPath id="circle-clip">
    <circle cx="50" cy="50" r="40"/>
  </clipPath>
</defs>
<image href="photo.jpg" width="100" height="100" clip-path="url(#circle-clip)"/>

<!-- Mask (soft, com gradient) -->
<defs>
  <linearGradient id="fade-mask" x2="1" y2="0">
    <stop offset="0%" stop-color="white"/>
    <stop offset="100%" stop-color="black"/>
  </linearGradient>
  <mask id="fade-out">
    <rect width="100" height="100" fill="url(#fade-mask)"/>
  </mask>
</defs>
<image href="photo.jpg" width="100" height="100" mask="url(#fade-out)"/>
```

**Regra**: clipPath para crop binary, mask para fade/transparency gradient.

### Filters

`<filter>` + filter primitives — vao dentro de `<defs>`. Primitivas comuns:

- `<feGaussianBlur stdDeviation="3"/>` — blur
- `<feOffset dx="2" dy="2"/>` — desloca (combinado para drop-shadow)
- `<feMerge><feMergeNode/></feMerge>` — combina inputs
- `<feComposite operator="in|out|over|atop|xor"/>` — composicao Porter-Duff
- `<feColorMatrix type="matrix" values="..."/>` — transforma cores (grayscale, sepia, hue rotate)
- `<feFlood flood-color="..."/>` — preenchimento solido
- `<feMorphology operator="dilate|erode" radius="2"/>` — dilata/erode shapes

**Drop-shadow classico**:
```xml
<filter id="drop-shadow">
  <feGaussianBlur in="SourceAlpha" stdDeviation="3"/>
  <feOffset dx="2" dy="2" result="offsetblur"/>
  <feMerge>
    <feMergeNode/>
    <feMergeNode in="SourceGraphic"/>
  </feMerge>
</filter>
```

### Gradientes

- `<linearGradient>` — linear (x1/y1/x2/y2 + stops)
- `<radialGradient>` — radial (cx/cy/r/fx/fy + stops)
- `<pattern>` — texturas repetidas

```xml
<defs>
  <linearGradient id="purple-blue" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%" stop-color="purple"/>
    <stop offset="100%" stop-color="blue"/>
  </linearGradient>
</defs>
<rect width="100" height="100" fill="url(#purple-blue)"/>
```

### Animation

- **SMIL animation** (`<animate>`, `<animateTransform>`) — **DEPRECATED** em browsers modernos (Chrome considerou remover). Evitar.
- **CSS animation** — recomendado para 90% casos
- **GSAP** — performance + DX best-in-class para animation complexa
- **D3 transitions** — para data viz

```css
/* CSS */
.spin {
  animation: rotate 2s linear infinite;
  transform-origin: center;
}
@keyframes rotate {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}
```

```javascript
// GSAP
gsap.to('.element', { rotation: 360, duration: 2, repeat: -1, ease: 'none' });
```

### Referencias composicao

- [MDN Clipping and masking](https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorials/SVG_from_scratch/Clipping_and_masking)
- [W3C SVG 1.1 Masking + Compositing](https://www.w3.org/TR/SVG11/masking.html)
- [Motion Tricks SVG Masks and clipPaths](https://www.motiontricks.com/svg-masks-and-clippaths/)
- [SSSVG fffuel.co](https://www.fffuel.co/sssvg/) — referencia interativa

## Fundacao 6 — Auto-Validacao IA Sem Visao (INOVACAO METODOLOGICA)

**Problema central** desta skill: como Claude/LLMs validam SVG que geram, dado que nao veem? Esta fundacao propoe **framework auto-validacao** combinando metricas + heuristicas + render-loop.

### Metricas formais (estado da arte 2026)

**PSS — Path-Structure Similarity Score** (SVGenius 2025):
- Extrai comandos path (M/L/C/A/Z) + atributos (fill/stroke/transform) + organizacao hierarquica (nesting groups)
- Compara estrutura SVG-gerado vs SVG-referencia
- Captura **visual plausibility + syntactic correctness**
- Reproducible across LLMs

**Self-evaluating LLMs** — trend 2026: modelos engineered para score outputs proprios baseados em criteria internos. Permite real-time internal feedback.

### Checklist heuristico Claude pode aplicar (sem visao)

Antes de finalizar SVG, Claude verifica auto-criticamente:

#### 1. Estrutura sintatica
- [ ] `<svg xmlns="http://www.w3.org/2000/svg">` declarado?
- [ ] `viewBox` definido com 4 valores numericos validos?
- [ ] Tags abertas todas fechadas (validar via XML lint)?
- [ ] Atributos com valores validos (cores HEX 6 digitos ou named CSS, numeros)?
- [ ] Sem caracteres ASCII invalidos (apenas a-z + numeros + simbolos comuns)?

#### 2. Geometria
- [ ] **Paths fechados (Z)** onde shape deve ser preenchido (fill≠none)?
- [ ] Coordenadas dentro do viewBox (sem escapar abruptamente)?
- [ ] **Simetria**: se design declarado simetrico, pontos espelhados em torno do eixo declarado?
- [ ] **Proporcoes**: razoes (ex: golden ratio 1.618, regra dos tercos)?
- [ ] Bezier control points geram curva intencional (control1 + control2 nao colinear se curva pretendida)?

#### 3. Composicao
- [ ] Z-order correto (elementos posteriores aparecem por cima)?
- [ ] Transforms aninhados aplicados na ordem certa (right-to-left)?
- [ ] `<defs>` antes de uso via `<use>` ou `url(#id)`?
- [ ] IDs unicos no documento?

#### 4. Acessibilidade
- [ ] `<title>` definido (curto, descritivo)?
- [ ] `<desc>` definido para SVGs complexos?
- [ ] `role="img"` (decorativo: `aria-hidden="true"` em vez)?
- [ ] `aria-labelledby` referenciando title+desc IDs?

#### 5. Performance / Otimizacao
- [ ] Sem comments desnecessarios?
- [ ] Sem editor metadata (Inkscape, Adobe namespaces)?
- [ ] Decimal precision adequada (2-3 casas, nao 15)?
- [ ] Paths nao redundantes (linha quase igual repetida)?
- [ ] Estilos inline minimizados (preferir CSS interno se complexo)?

#### 6. Estetica heuristica (limitada sem visao)
- [ ] Paleta de cores declarada e respeitada?
- [ ] Espacamentos consistentes (margens iguais entre elementos repetidos)?
- [ ] Stroke-widths consistentes (icon set inteiro com 2px stroke)?
- [ ] Typography hierarchy se texto presente?

### Render-loop self-correction pattern

Claude (em ambiente que permite render) executa loop:

```
1. Gerar SVG draft
2. (Idealmente) renderizar via Resvg/Sharp em Code Interpreter
3. Compare resultado renderizado vs intencao declarada
4. Identificar gap: "objeto deslocado", "desproporcao", "cor errada"
5. Re-prompt self: "the eye is at x=60 but should be at x=55, regenerate"
6. Iterar ate convergir (max 3-5 iteracoes para nao loop infinito)
```

Sem capacidade render: **delegar render para humano** + apresentar SVG como "v1, valide visualmente e me diga gaps especificos".

### Decomposicao em sub-tarefas (Comeau-style)

Em vez de gerar logo complexo em 1 prompt, decompor:

```
Step 1: viewBox e cores definidas?
   → Ok: viewBox=0 0 100 100, primary=#1A2E5C, accent=#F5A623

Step 2: forma base (circle, rect, polygon)?
   → Ok: <circle cx=50 cy=50 r=40 fill=#1A2E5C/>

Step 3: elemento secundario interno?
   → Ok: <path d=M30,50 Q50,30 70,50 fill=#F5A623/>

Step 4: detalhe ou texto?
   → Ok: ...

Step 5: validar checklist heuristico (estrutura + geometria + composicao + acessibilidade + otimizacao)
   → Ok: tudo passa.

Step 6: SVGO mental (estimativa de optimizacao)
   → Ok: ~80 chars / pode reduzir 20% com float trim.
```

### Validators externos (pos-geracao humana ou code interpreter)

- [W3C Markup Validation Service](https://validator.w3.org/) — SVG XML/XHTML validation
- [SVG Genie Validator](https://www.svggenie.com/tools/svg-validator) — AI-powered fix suggestions, client-side
- [SVG Sanitizer Test](https://svg.enshrined.co.uk/) — security focus (XSS, scripts injetados)
- [svgcheck PyPI](https://pypi.org/project/svgcheck/) — RFC 7996 schema compliance
- [CodeBeautify XML Validator](https://codebeautify.org/xmlvalidator) — multi-format

### Limitacoes desta fundacao

- Heuristicas ajudam **estrutura + sintaxe + geometria** — mas **estetica + composicao visual** exigem visao real
- Sem render loop em ambiente, validacao e parcial
- Decomposicao funciona melhor em SVGs **com 5-15 elementos**; SVGs muito simples (1 forma) — overkill; muito complexos (50+ elementos) — quebra

**Recomendacao**: para producao, **sempre** acoplar humano (designer ou cliente) revisando v1 + iterando. Auto-validacao reduz iteracoes mas nao elimina.

## Fundacao 7 — Tooling Hibrido + Workflow IA-Humano

### Editors profissionais 2026

| Editor | Tipo | Preco | Forte | Fraco | Output SVG quality |
|--------|------|-------|-------|-------|---------------------|
| [Adobe Illustrator](https://www.adobe.com/products/illustrator.html) | Desktop | Subscription R$ 30-100/mes | Industry standard, plugin ecosystem | Subscription, output bloated | Medio (precisa SVGO) |
| [Affinity Designer](https://affinity.serif.com/designer/) | Desktop | One-time R$ 250 | Alternative Illustrator, sem assinatura | Plugin ecosystem menor | Bom |
| [Inkscape](https://inkscape.org/) | Desktop | Free open-source | Native SVG, virtually all SVG features | Performance + UX | Excelente (native) |
| [Figma](https://www.figma.com/) | Web/Desktop | Free / R$ 30/mes | Collab + UI design | Output 62% maior que Boxy SVG | Medio |
| [Boxy SVG](https://boxy-svg.com/) | Web/Chromium | R$ 50 one-time | Web devs, clean output | Recursos limitados vs Illustrator | Excelente (62% menor) |
| [Sketch](https://www.sketch.com/) | Mac | R$ 50/mes | Mac-only, UI design | Mac only | Bom |

**Recomendacao 2026 por audiencia**:
- **Designer profissional Brasil** → Illustrator (industry standard) ou Affinity Designer (sem subscricao)
- **Brand design enterprise** → Illustrator + Inkscape (free fallback) + Figma (collab)
- **Web dev / Icon system** → Boxy SVG (output limpo) ou Inkscape
- **Founder/MVP** → Figma (free + collab) ou Inkscape (free + completo)

### Optimization

[SVGO](https://github.com/svg/svgo) — Node.js CLI + 50+ plugins. Default config remove editor metadata + comments + empty groups + redundant attributes + excess decimal precision = **30-60% reduction**.

```bash
npx svgo input.svg -o output.svg
npx svgo --multipass input.svg # multiple passes ate idempotente
```

[SVGOMG](https://jakearchibald.github.io/svgomg/) — web GUI por Jake Archibald. Idem SVGO engine + visual diff + plugin toggles. **40-80% reduction**. Combinado com Gzip/Brotli no servidor: **80-90% reducao total**.

### Libraries JavaScript (SVG programatico)

| Library | Foco | Weekly downloads | Stars | Use case |
|---------|------|-----------------|-------|----------|
| [D3.js](https://d3js.org/) | Data visualization | 4.4M | 111k | Charts, dashboards, geo viz |
| [GSAP](https://gsap.com/) | Animation | 965k | 22k | Hero animations, scroll-trigger |
| [Snap.svg](http://snapsvg.io/) | SVG manipulation | ~50k | 14k | DOM manipulation moderna |
| [SVG.js](https://svgjs.dev/) | SVG manipulation | ~70k | 11k | Lightweight DOM SVG |
| [Two.js](https://two.js.org/) | 2D graphics renderer | ~20k | 8k | Cross-renderer (SVG + Canvas + WebGL) |
| [Paper.js](http://paperjs.org/) | Vector graphics | ~10k | 14k | Bezier-heavy, scripting language |

**Recomendacao 2026**:
- **Data viz** → D3 (dominante absoluto)
- **Animation** → GSAP (60 FPS guaranteed, 20x faster que jQuery)
- **Generative art** → Paper.js ou p5.js + p5.svg

### Generative coding 2026

- **p5.js 2.0 (Apr-2025)** — variable fonts, JS shaders, LAB/OKLab color spaces, unified pointer events. [p5js.org](https://p5js.org/)
- **p5.js SVG library** — substitui canvas renderer por SVG renderer, exporta vetor de qualquer sketch
- **Processing** (parent project) — Java-based, 20+ anos
- **OpenProcessing** — community sketches
- Livro 2024: **"Generative Art with JavaScript and SVG"** (David Matthew, Springer/Apress) — coding + design

### Workflow LLM + Human hybrid (recomendado producao)

```
┌─────────────────────────────────────────────┐
│ FASE 1: BRIEF + IDEACAO                    │
│ - Brief textual + reference moodboard      │
│ - LLM (Claude) gera 5-10 SVG drafts        │
│ - Human seleciona 2-3 promissores          │
└─────────────────────────────────────────────┘
                  ↓
┌─────────────────────────────────────────────┐
│ FASE 2: REFINEMENT HUMANO                   │
│ - Designer abre em Illustrator/Inkscape    │
│ - Ajusta proporcoes + cores + detalhes     │
│ - Adiciona detalhes que LLM nao consegue   │
│ - Itera 3-5x ate aprovacao                 │
└─────────────────────────────────────────────┘
                  ↓
┌─────────────────────────────────────────────┐
│ FASE 3: VARIATIONS                          │
│ - LLM gera variacoes (cores, escalas)      │
│ - Logo system (primary, monochrome,        │
│   reverse, scale-down)                     │
└─────────────────────────────────────────────┘
                  ↓
┌─────────────────────────────────────────────┐
│ FASE 4: OPTIMIZE + DELIVERABLES             │
│ - SVGO/SVGOMG run (60-80% reduction)       │
│ - Export PNG/PDF/EPS para entregaveis      │
│ - Acessibilidade (title + desc + role)     │
│ - QA cross-browser + cross-device          │
└─────────────────────────────────────────────┘
                  ↓
┌─────────────────────────────────────────────┐
│ FASE 5: DEPLOY                              │
│ - Inline SVG (HTML) > <img src="..."> >    │
│   background-image (escolha por contexto)  │
│ - CDN serving + cache headers              │
│ - Brand book documentando uso              │
└─────────────────────────────────────────────┘
```

## Fundacao 8 — Aplicacao em Content MKT (Founder/Brand Designer/Dev/Agencia/Brand Manager)

### Audiencia 1 — Founder bootstrap MVP visual (R$ 0 budget)

**Cenario**: Marina founder FoodTech pre-Series A, 18 funcionarios, R$ 0 budget designer. Precisa logo + 5 icones para LP + favicon.

**Stack recomendado**:
- Claude Artifacts (gera SVG draft conversacionalmente)
- Inkscape (free, refine humano)
- SVGOMG (optimize)
- Lucide Icons como inspiracao (open-source 1500+ icones)

**Workflow** (4 horas):
1. Brief Claude: "Logo for FoodTech B2B, target restaurant chains, evoke trust + freshness, viewBox 0 0 100 100, palette navy + lime"
2. Claude gera 3 variacoes via Artifacts
3. Marina escolhe 1, abre Inkscape, refina
4. Roda SVGOMG (40-60% size reduction)
5. Exporta PNG variations (favicon 32x32, social 800x800)
6. Acessibilidade: adiciona `<title>FoodTech Brasil</title>` + `<desc>Logo navy with lime accent...</desc>`

**Anti-padroes Marina**:
- Comprar logo em fiverr R$ 500 sem brief estrategico (cross-skill: `branding` + `logo-design-process` futuro)
- Usar Canva template generico (nao escala para identidade real)

### Audiencia 2 — Brand Designer agencia (workflow profissional)

**Cenario**: Carla brand designer agencia premium, cliente B3-listed enterprise. Logo redesign + brand book + icon system 50+ icones.

**Stack recomendado**:
- Claude (ideation + variations)
- Adobe Illustrator (refine + master files)
- Figma (collab review com cliente)
- Boxy SVG (output limpo final)
- SVGO + SVGOMG (optimize)
- Frontify ou Zeroheight (brand book deploy)

**Workflow** (6-8 semanas):
1. Brief estrategico cliente + research (cross-skill `branding` + `posicionamento-marca`)
2. Claude gera 30+ direcoes ideativas (broad exploration)
3. Carla seleciona 5 finalistas, refina em Illustrator (master files)
4. Apresenta cliente em Figma (collab feedback)
5. Cliente escolhe 1 final + 2 alternativas
6. Carla finaliza variations (primary, monochrome, reverse, simplified, social media)
7. Icon system: Claude gera 50 icones grid 24x24 + Carla refina + uniformiza stroke 2px + alinha grid
8. SVGO + Boxy SVG export
9. Brand book Frontify com tudo documentado

**Custo cliente**: R$ 80-300k tipico Brasil enterprise.

### Audiencia 3 — Dev frontend SaaS (geracao programatica)

**Cenario**: Bruno dev frontend B2B SaaS, 200 funcionarios. Quer integrar charts dinamicos + generated SVG icones para feature dashboard.

**Stack recomendado**:
- D3.js (data viz charts)
- GSAP (animations dashboard)
- Lucide Icons (npm package, tree-shakable)
- Resvg-js (server-side rasterization para Open Graph images)
- Sharp (image pipeline geral)

**Workflow**:
1. Charts: D3 bindings data → SVG paths dinamicos
2. Icons: import Lucide React components (icone individuais SSR-friendly)
3. Hero animations: GSAP ScrollTrigger
4. OG images: backend Node.js gera SVG dinamico per-page → Resvg-js converte PNG → cache CDN
5. Build: SVGO em build pipeline (vite/webpack plugin)

**Anti-padroes Bruno**:
- Gerar SVG via Claude em runtime (latencia + cost API; usar build-time)
- Inline SVG enormous em HTML (use sprite + use, ou external SVG file)
- SMIL animations (use GSAP/CSS)

### Audiencia 4 — Agencia design entregando icon systems (escala)

**Cenario**: Estela agencia entrega icon system 100+ icones para cliente fintech.

**Workflow**:
1. Brief cliente: domains (banking + investment + crypto + cards) + style (line, 2px stroke, rounded corners)
2. Claude gera 100 icones via batch (10 por domain x 10 domains)
3. Junior designer revisa cada um (uniformiza stroke + grid + nomenclatura)
4. Senior designer aprova (consistency check)
5. Boxy SVG export limpo
6. Storybook documenta library
7. Distribute via npm package (cliente integra como `@cliente/icons`)
8. Versioning semver (cada nova bateria de icones = minor version)

**Vantagem usar Claude vs full-manual**: 10x velocidade ideacao + 30-50% reducao tempo total. Mas qualidade exige sempre passe humano.

### Audiencia 5 — Frank-MKT integration (cross-skill ecosystem)

**Cenario**: Frank-MKT consultor virtual recebe pedido "preciso identidade visual para minha empresa".

**Orchestration cross-skill**:
1. Frank-MKT invoca `branding` (foundation: archetype + voice + posicionamento)
2. `posicionamento-marca` (Trout & Ries POV)
3. `big-idea` (nucleo unificador)
4. **`svg-engineering-ia`** (esta skill) — methodology + tooling
5. `logo-design-process` (futuro — fechara processo design)
6. `iconografia-corporativa` (futuro — sistema icones)
7. `composicao-visual` (existente)
8. `geracao-imagens-ia` (existente)
9. `acessibilidade-wcag` (compliance visual)

Output cross-skill: estrategia + execucao via IA + governance.

### Brasil 2026 specificity

- **Cases para inspiracao**: Lu Magalu icon evolution (mascot SVG simplificado decadas) + Nubank purple + cubo Itau + iFood logo simplificacao 2024
- **Tools tropicalizadas**: maioria global (Illustrator + Figma + Inkscape), mas Boxy SVG ascendente comunidade Brasil dev
- **Designers BR referencia**: Crama Studios + WeBrand + Tátil Design + Greco Design + Estudio Yes
- **Comunidades**: BR Design + UX Brasil + Design Conferences (Cardume, UX Conference Brasil)
- **LGPD impacto**: SVGs com texto personalizavel (nome usuario, etc) + servidor-side rendering devem respeitar dados pessoais

### Disclaimers para conteudo MKT

- Esta skill e **metodologica e tecnica** — design senior humano e mandatory para identidade comercial seria
- Claude/LLMs SVG e ferramenta-de-apoio, nao substituicao designer
- Brand identity completa exige `logo-design-process` + `brand-book-methodology` + `paleta-cores-corporativa` + `tipografia-corporativa` + `iconografia-corporativa` (skills brand-design em construcao)

## Anti-Patterns 18

1. **Achar que LLM "ve" o SVG que gera** — fundamental: LLMs sao text models doing visual tasks (Praeclarum, VGBench EMNLP 2024). Sempre delegate render+visual review para humano ou code-interpreter.
2. **Gerar SVG complexo em 1 prompt monolitico** — fracassa. Use decomposicao Comeau-style: viewBox → forma base → detalhes → validacao.
3. **Nao validar geometricamente** — paths nao fechados, viewBox incompativel, coordenadas escapando — defeitos invisiveis ao LLM mas catastroficos visualmente.
4. **Ignorar acessibilidade** — sem `<title>`, `<desc>`, `role="img"`, `aria-labelledby`. Falha WCAG. Cross-skill `acessibilidade-wcag`.
5. **Cores hardcoded sem semantica** — em vez de `fill="#1A2E5C"`, use `fill="var(--color-primary)"` ou `fill="currentColor"` para flexibilidade.
6. **Usar SMIL animations** — deprecated em browsers modernos. Use CSS animations ou GSAP.
7. **Pular SVGO/SVGOMG** — file size 60-80% maior. Editor metadata + comments + redundancy nao otimizados.
8. **Vetorizar foto realista esperando bom resultado** — Potrace/AutoTrace funcionam para line art + logos. Foto realista produz paths enormes (megabytes) sem qualidade real.
9. **Confiar em Claude Artifacts para producao comercial sem refinamento humano** — Artifacts e MVP/draft, nao final delivery.
10. **Omitir viewBox** — perde escalabilidade real. SVG vira raster fixo, contradiz proposito.
11. **Inline styles em vez de `<style>` interno ou classes** — manutenibilidade ruim em SVGs grandes.
12. **Texto SVG sem fallback fonts** — render diferente em sistemas sem fonte custom. Use `font-family: 'Custom', Arial, sans-serif`.
13. **Stroke sem unit consistente + sem stroke-width** — render imprevisivel. Sempre declare stroke-width + cap + linejoin.
14. **Mask quando devia ser clipPath** — overhead computacional. Use clipPath para crop binary, mask so para gradient transparency.
15. **Nao testar em multiplos renderers** — Chrome render diferente de Resvg diferente de Inkscape. SVG production deve QA em Chrome + Firefox + Safari + iOS Safari + headless.
16. **Coordenadas com decimal precision excessiva** — `12.34567890123` em vez de `12.35`. Poluicao + file size +30%.
17. **Nao usar `<symbol>` + `<use>` para icones repetidos** — duplica path code N vezes. Symbol pattern e DRY.
18. **Esquecer `xmlns="http://www.w3.org/2000/svg"`** — browsers podem tratar como XML generico, perde renderizacao.

## 18 Regras de Ouro

1. **Sempre defina `viewBox` + `xmlns`** — base mandatory toda SVG.
2. **Paths fechados com `Z`** onde shape preenche (fill≠none).
3. **Decompor SVG complexo em sub-elementos** ANTES de gerar (Comeau-style: viewBox → forma → detalhes → validacao).
4. **Validar geometricamente** via checklist heuristico (Fundacao 6) antes de visualizar.
5. **Acessibilidade mandatory**: `<title>` + `<desc>` + `role="img"` + `aria-labelledby` (decorativo: `aria-hidden="true"`).
6. **SVGO/SVGOMG sempre antes deploy** — 60-80% size reduction.
7. **Use `<symbol>` + `<use>`** para icones repetidos.
8. **Cores via CSS variables** ou `currentColor` para flexibilidade tema.
9. **Animation: CSS ou GSAP**, nao SMIL (deprecated).
10. **Stroke-width relative units** + cap + linejoin consistentes.
11. **Test em multiplos renderers** (Chrome + Firefox + Safari + Resvg).
12. **Inline SVG (HTML)** > `<img>` > background-image, conforme contexto (CSS interaction precisa inline).
13. **Vetorize line art** (Potrace), **gere SVG diretamente** para abstract/geometric (logos simples).
14. **Hybrid pipeline producao**: LLM draft → human refine → SVGO → deploy.
15. **Render-loop self-validation** quando ambiente permite (Code Interpreter + render).
16. **Coordenadas com precision adequada** (2-3 casas decimais default; mais so se justificado).
17. **Documentar viewBox semantics em comment** se nao-padrao (ex: `<!-- viewBox 0 0 24 24 — Lucide grid standard -->`).
18. **Disclaimer educational mandatory**: skill e metodologica, design comercial exige humano sênior.

## Exemplos Comportamentais

### Exemplo 1 — Founder Marina FoodTech, logo MVP via Claude (4 horas, R$ 0)

**Contexto**: Marina founder solo R$ 8M ARR, 18 funcionarios, pre-Series A. Logo atual e Canva template generico. Precisa logo proprietario + favicon + 5 icones para nova LP. Budget R$ 0 para designer.

**Frank-MKT diagnostic**: Founder pre-Series A com R$ 0 budget — Claude + Inkscape + SVGOMG e o stack certo. NAO contratar Fiverr R$ 500 (sem brief estrategico vira logo generico). Stack proposto: 4 horas para logo + 5 icones decentes.

**Recomendacao plan 4h**:

1. **Brief Claude (15 min)**:
   ```
   Logo for FoodTech Brasil B2B, ICP: restaurant chain operations managers,
   evoke: trust + freshness + tech competence,
   archetype: Sage (cross-skill `branding` 12 archetypes Jung),
   palette: navy #1A2E5C primary, lime #C5E063 accent, white background,
   viewBox 0 0 100 100,
   constraints: works at 16x16 favicon scale, monochrome variant possible,
   format: SVG inline-ready with <title> + <desc> + role="img"
   ```
2. **Claude gera 5 variacoes via Artifacts (30 min)** — Marina seleciona 2 promissoras
3. **Inkscape refine (90 min)** — abre cada uma, ajusta proporcoes, alinha grid, simplifica paths
4. **A/B test interno (30 min)** — 5 funcionarios votam (informal, gut check)
5. **Final escolhido (60 min)** — Marina cria 5 variations: primary horizontal + primary vertical + monochrome black + monochrome white + favicon 16x16
6. **Icon set (60 min)** — Claude gera 5 icones (restaurant + delivery + analytics + customer + settings) viewBox 0 0 24 24, stroke 2px, line style; Marina uniformiza
7. **SVGOMG optimize (15 min)** — 50-60% size reduction
8. **Acessibilidade (15 min)** — adiciona `<title>` + `<desc>` em cada
9. **Deploy** — uploads para LP, atualiza favicon, atualiza social media

**KPIs 4h**:
- Logo proprietario funcional (vs template Canva)
- Favicon 16x16 reconhecivel
- 5 icones consistentes (stroke + grid)
- File sizes <2KB each (post-SVGO)
- Acessibilidade WCAG AA

**Riscos**:
- Logo Claude pode ter quirks geometricos sutis (Marina passa em Inkscape mas pode nao detectar todos)
- Icons podem ter inconsistencia stroke (uniformizar via SVGO + Inkscape OK)
- Sem brand designer review, pode ter problemas legibilidade scale-down extreme

**Disclaimer**: este e MVP — Marina deve revisitar com designer profissional ate Series A close. Logo e first iteration, brand identity completa exige `logo-design-process` + `brand-book-methodology` (skills futuras).

### Exemplo 2 — Brand Designer Carla agencia premium, logo redesign + icon system (6-8 semanas, R$ 80-150k)

**Contexto**: Carla brand designer agencia Sao Paulo top-tier, 8 anos experiencia. Cliente B3-listed enterprise R$ 8 bi market cap quer logo redesign pos-M&A + icon system 50 icones.

**Frank-MKT diagnostic**: Projeto profissional serio. Claude entra como aceleradora ideacao + variation, mas master files sao Illustrator + workflow agencia padrao. Stack: Claude + Illustrator + Figma + Boxy SVG + Frontify.

**Recomendacao plan 6-8 semanas**:

**Semana 1-2: Discovery + Strategy**
- Cross-skill `branding` + `posicionamento-marca` + `big-idea` (workshop estrategico)
- Brief escrito + moodboard + competitive analysis (cross-skill `competitive-intelligence`)

**Semana 3-4: Ideation broad**
- Claude prompts: 30-50 direcoes ideativas amplas (text-based variations)
- Carla manualmente esboca + complementa em Illustrator
- Apresenta 8 finalistas para cliente (Figma collab review)

**Semana 5-6: Refinement**
- Cliente escolhe 3 finalistas
- Carla refina cada em Illustrator master file
- Iteracoes 3-5x ate aprovacao final
- Cliente escolhe 1 winner

**Semana 7: Variations + System**
- Logo variations: primary horizontal + primary vertical + monochrome + reverse + favicon scales (16/32/64/128/256/512)
- Icon system: Claude gera 50 icones grid 24x24 line style — Carla refina cada (uniformiza stroke 2px + alinha grid + nomenclatura semantica)

**Semana 8: Delivery + Documentation**
- SVGO/SVGOMG optimize todos arquivos
- Boxy SVG export final clean
- Frontify brand book (cross-skill `brand-book-methodology` futuro): logo usage do/dont, colors, typography, applications
- Versions all formats: SVG, PNG (multiple sizes), PDF, EPS, AI

**KPIs**:
- Logo aprovado cliente em 5 iteracoes max (qualidade)
- 50 icones uniformes (stroke + grid + nomenclatura)
- Brand book Frontify deployable
- All optimized (50-70% size reduction post-SVGO)
- Cross-platform tested (web + print + mobile)

**Riscos**:
- M&A cultural friction (cliente pode pivotar mid-project)
- Claude variations podem influenciar Carla overcorrect (perda direcao estrategica)
- Icon system 50 icones e maraton — risco fadiga juniors da agencia

**Custo cliente**: R$ 80-150k tipico Brasil enterprise tier.

**Disclaimer**: Claude e ferramenta-de-apoio. Senior designer judgment + iteration humana sao mandatory.

### Exemplo 3 — Dev Bruno B2B SaaS, charts dinamicos + icon system programatico

**Contexto**: Bruno staff engineer B2B SaaS Series C ($35M ARR), produto analytics dashboard. Quer integrar charts D3 + 200+ icones (lib propria) + Open Graph images dinamicos.

**Frank-MKT diagnostic**: Caso DEV, NAO design. Claude como ferramenta auxiliar; foco em libraries + build pipeline + production ops.

**Recomendacao stack tecnico**:

**Charts data-driven**:
- D3.js v7 (binding data → SVG paths)
- GSAP transitions (animations smooth)
- Cypress component tests (visual regression)

**Icon system**:
- Lucide React npm package (tree-shakable, 1500+ icones gratuitos)
- Custom icones (~20) gerados via Claude em build script + designer review uma vez
- Storybook documentacao
- @cliente/icons npm internal package

**Open Graph images dinamicos**:
- Next.js API route gera SVG dinamico per-page (titulo + autor + preview)
- @resvg/resvg-js converts SVG → PNG em runtime
- Cache em Cloudflare R2 + CDN
- Latency target <500ms p95

**Build pipeline**:
- Vite plugin SVGO (auto-optimize todos SVGs build-time)
- Imagemin (raster fallbacks)
- TypeScript types para icon library

**Production checks**:
- Sentry monitoring SVG parse errors
- Lighthouse CI (acessibilidade SVG + performance)
- Bundle size budget (<5KB per icon component)

**KPIs**:
- Icon bundle size <50KB total (200 icones tree-shaken)
- OG image generation latency <500ms p95
- Charts rendering 60 FPS
- Acessibilidade Lighthouse 100% (WCAG AA)

**Riscos**:
- D3 learning curve (Bruno team pode precisar 2-3 sprints)
- OG images dinamicos podem ter cache misses caros
- Custom icones via Claude precisam designer review (nao pular)

**Disclaimer**: tech stack — design judgment ainda exige humano. Skill complementa expertise dev, nao substitui.

### Exemplo 4 — Frank-MKT consultor cross-skill orchestration

**Contexto**: Empresa Brasil mid-market R$ 50M ARR consulta Frank-MKT: "preciso identidade visual nova". Founder + CMO sem time design interno.

**Frank-MKT orchestration cross-skill**:

```
Step 1: Cross-skill `branding` (foundation strategy)
  → output: archetype + voice + brand DNA

Step 2: Cross-skill `posicionamento-marca` (POV)
  → output: positioning statement + STP

Step 3: Cross-skill `big-idea` (nucleo unificador)
  → output: tagline + manifesto

Step 4: Cross-skill `svg-engineering-ia` (esta skill — tooling + methodology)
  → output: workflow proposal LLM + designer + tools

Step 5: Cross-skill `logo-design-process` (futuro)
  → output: logo system entregaveis

Step 6: Cross-skill `iconografia-corporativa` (futuro)
  → output: icon system

Step 7: Cross-skill `paleta-cores-corporativa` (futuro)
  → output: paleta acessivel WCAG

Step 8: Cross-skill `tipografia-corporativa` (futuro)
  → output: hierarquia tipografica

Step 9: Cross-skill `brand-book-methodology` (futuro)
  → output: manual identidade Frontify/Zeroheight

Step 10: Cross-skill `acessibilidade-wcag` (existente)
  → output: compliance visual review
```

**Output cross-skill (consolidado para cliente)**:
- Identidade visual completa (logo + variations + icon system + colors + typography + applications)
- Brand book deployable (Frontify ou similar)
- Production-ready files (SVG optimized + PNG/PDF/EPS variants)
- Roadmap evolucao 12-24 meses
- Custo: R$ 50-150k (mid-market) ou R$ 150-400k (enterprise) — combinacao Frank-MKT recomendacao + agencia / freelancer humano sênior contratado

**Disclaimer**: Frank-MKT orquestra metodologia + ferramentas, mas execucao premium para identidade corporativa **exige humano senior** (brand designer, illustrator, art director). Skill é multiplicador de produtividade, não substituto.

## Checklist Contraditorio Interno (10 perguntas)

Antes de finalizar SVG gerado por IA, perguntar honestamente:

1. **viewBox + xmlns presentes?** Sem isto, render falha.
2. **Paths fechados (Z) onde fill≠none?** Paths abertos podem render imprevisivel.
3. **Coordenadas dentro do viewBox?** Conteudo escapando = cropping inesperado.
4. **Decomposicao foi feita** (Comeau-style) ou prompt monolítico que pode falhar?
5. **Acessibilidade**: title + desc + role + aria-labelledby presentes?
6. **SVGO/SVGOMG rodado?** Sem otimizacao, file size 60-80% maior.
7. **Render visualmente verificado** (humano ou code interpreter)? Sem render, IA pode ter falhado silenciosamente.
8. **Animation usa CSS/GSAP** (nao SMIL)?
9. **Cross-renderer testado** (Chrome + Resvg + Firefox)?
10. **Disclaimer educational**: comunicado que producao comercial exige design senior humano + cross-skill brand-design (logo-design-process + brand-book-methodology + paleta-cores-corporativa + tipografia-corporativa + iconografia-corporativa em construcao)?

## Referencias

### W3C + fundamentos SVG
- [W3C SVG 2 Specification](https://www.w3.org/TR/SVG2/) — normative recommendation
- [W3C Paths](https://www.w3.org/TR/SVG/paths.html) — paths chapter
- [W3C SVG Working Group Paths Editor's Draft](https://svgwg.org/specs/paths/)
- [W3C SVG 1.1 Masking + Compositing](https://www.w3.org/TR/SVG11/masking.html)
- [W3C Markup Validation Service](https://validator.w3.org/)
- [MDN SVG Tutorial Paths](https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorials/SVG_from_scratch/Paths)
- [MDN Clipping and Masking](https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorials/SVG_from_scratch/Clipping_and_masking)
- [Josh W. Comeau Interactive Guide to SVG Paths](https://www.joshwcomeau.com/svg/interactive-guide-to-paths/)
- [Smashing Magazine Decoding SVG Path Element 2025](https://www.smashingmagazine.com/2025/06/decoding-svg-path-element-curve-arc-commands/)
- [SSSVG Interactive Reference fffuel.co](https://www.fffuel.co/sssvg/)
- [Eric Eastwood Curves and Arcs SVG implementations](https://ericeastwood.com/blog/curves-and-arcs-quadratic-cubic-elliptical-svg-implementations/)

### LLMs gerando SVG (papers academicos)
- [VGBench EMNLP 2024](https://aclanthology.org/2024.emnlp-main.213.pdf) | [vgbench.github.io](https://vgbench.github.io/)
- [SVGenius Benchmarking LLMs SVG arxiv 2506.03139](https://arxiv.org/html/2506.03139v1)
- [LLM4SVG Empowering LLMs CVPR 2025](https://openaccess.thecvf.com/content/CVPR2025/papers/Xing_Empowering_LLMs_to_Understand_and_Generate_Complex_Vector_Graphics_CVPR_2025_paper.pdf)
- [Chat2SVG site CVPR 2025](https://chat2svg.github.io/) | [GitHub Chat2SVG](https://github.com/kingnobro/Chat2SVG)
- [OmniSVG Unified Framework](https://omnisvg.github.io/)
- [PyTorch-SVGRender open-source](https://github.com/ximinng/PyTorch-SVGRender)
- [Simon Willison LLM SVG Benchmark Pelican Bicycle Nov 2025](https://simonwillison.net/2025/Nov/25/llm-svg-generation-benchmark/)
- [LLM-Visualization Paper List GitHub](https://github.com/zengxingchen/LLM-Visualization-Paper-List)
- [IEEE VIS 2024 LLMs Low-Level Visual Analytic SVG](https://ieeevis.org/year/2024/program/paper_v-short-1186.html)

### Claude / Anthropic SVG
- [Claude Design 2026 Buildfast Guide](https://www.buildfastwithai.com/blogs/claude-design-anthropic-guide-2026)
- [Anthropic Prompt Engineering Overview](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview)
- [Anthropic Prompting Best Practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- [Anthropic Prompt Generator Console](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prompt-generator)
- [What Is Claude Design MindStudio](https://www.mindstudio.ai/blog/what-is-claude-design-anthropic)

### GPT / Outros LLMs SVG
- [How to Create SVGs with ChatGPT 2026 SVG Genie](https://www.svggenie.com/blog/create-svg-with-chatgpt)
- [Probing Compositional Understanding ChatGPT SVG Medium](https://evanthebouncy.medium.com/probing-compositional-understanding-of-chatgpt-with-svg-74ec9ca106b4)
- [Generating SVG with ChatGPT Praeclarum 2023](https://praeclarum.org/2023/04/03/chatsvg.html)
- [GPT Image Generation Models Prompting Guide](https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide)

### Bitmap → SVG (Vetorizacao)
- [Potrace official sourceforge](https://potrace.sourceforge.net/)
- [Potrace mirror GitHub](https://github.com/skyrpex/potrace)
- [Potrace Wikipedia](https://en.wikipedia.org/wiki/Potrace)
- [AutoTrace GitHub](https://github.com/autotrace/autotrace)
- [Inkscape Tracing Bitmaps Tutorial](https://inkscape.org/doc/tutorials/tracing/tutorial-tracing.html)
- [VectoSolve Best AI SVG Generators 2026](https://vectosolve.com/blog/best-ai-svg-generators-text-to-vector-2026)
- [VectorWitch AI SVG Guide 2026](https://vectorwitch.com/blog/the-complete-guide-to-ai-powered-svg-generation-in-2026)
- [SVG Genie AI SVG Creation Guide](https://www.svggenie.com/blog/ai-svg-creation-guide)
- [Top 10 AI SVG Tools 2026 SVGMaker](https://svgmaker.io/blogs/top-10-ai-svg-generation-tools-in-2026-compared)
- [Free SVG Converter AI Image Vector](https://freesvgconverter.com/blog/ai-image-to-vector)

### SVG → Bitmap (Rasterizacao)
- [Resvg-js SourceForge](https://sourceforge.net/projects/resvg-js.mirror/)
- [SVG Snapshots Converting Vector to Raster O'Reilly](https://oreillymedia.github.io/Using_SVG/extras/ch04-rasterizers.html)
- [MediaWiki SVG Benchmarks (Resvg vs librsvg)](https://www.mediawiki.org/wiki/SVG_benchmarks)
- [Wikimedia T40010 Re-evaluate librsvg](https://phabricator.wikimedia.org/T40010)
- [Sharp Node.js Image Processing](https://sharp.pixelplumbing.com/)
- [ImageMagick Convert SVG Raster makandracards](https://makandracards.com/makandra/506738-imagemagick-converting-svg-raster-image-formats-like)
- [Wealthfront Converting Dynamic SVG to PNG node.js](https://eng.wealthfront.com/2011/12/22/converting-dynamic-svg-to-png-with-node-js-d3-and-imagemagick/)

### Optimization
- [SVGO GitHub](https://github.com/svg/svgo)
- [SVGOMG Jake Archibald](https://jakearchibald.github.io/svgomg/)
- [SVG Optimization Vectosolve 60% reduction](https://vectosolve.com/blog/svg-optimization-guide-reduce-file-size-2026)
- [SVG Optimizer Compresto 80%](https://compresto.app/blog/svg-optimizer)
- [SitePoint Three Ways Decreasing SVG File Size SVGO](https://www.sitepoint.com/three-ways-decreasing-svg-file-size-svgo/)
- [SiteLint Best practices optimizing SVG code](https://www.sitelint.com/blog/best-practices-for-optimizing-svg-code)
- [LetCompress SVG Compression Principle](https://letcompress.com/blog/svg-compression-principle-how-images-shrink-smartly)

### Validation
- [SVG Genie Validator Free](https://www.svggenie.com/tools/svg-validator)
- [SVG Sanitizer Test enshrined.co.uk](https://svg.enshrined.co.uk/)
- [Tool Plaza Validate SVG](https://toolplaza.app/en/tools/validate/svg)
- [svgcheck PyPI](https://pypi.org/project/svgcheck/)
- [CodeBeautify XML Validator](https://codebeautify.org/xmlvalidator)
- [the new code Validating SVG](https://thenewcode.com/513/validating-svg)
- [Online SVG Code Editor editsvgcode](https://editsvgcode.com/)

### Composition + Filters
- [W3C Clipping Masking Compositing 1.0](https://www.w3.org/TR/2000/CR-SVG-20000802/masking.html)
- [LinkedIn How to use SVG masks clipping paths](https://www.linkedin.com/advice/1/how-do-you-use-svg-masks-clipping-paths-create-complex)
- [Motion Tricks SVG Masks clipPaths](https://www.motiontricks.com/svg-masks-and-clippaths/)
- [razrfalcon Clip paths Notes SVG parsing](https://razrfalcon.github.io/notes-on-svg-parsing/clip-paths.html)
- [redev.rocks Introduction to SVG Paths](https://redev.rocks/articles/05-intro-to-paths/)
- [CS559 Computer Graphics SVG6 Paths Curves](https://pages.graphics.cs.wisc.edu/559-sp21/tutorials/svg/svg6/)

### Accessibility
- [A11Y Collective Implementing Accessible SVG Elements](https://www.a11y-collective.com/blog/svg-accessibility/)
- [Vispero TPGI Using ARIA SVG](https://www.tpgi.com/using-aria-enhance-svg-accessibility/)
- [Deque Creating Accessible SVGs](https://www.deque.com/blog/creating-accessible-svgs/)
- [Unimelb Accessible SVGs](https://www.unimelb.edu.au/accessibility/techniques/accessible-svgs)
- [European Data Accessible SVG ARIA](https://data.europa.eu/apps/data-visualisation-guide/accessible-svg-and-aria)
- [Orange A11Y SVG accessibility](https://a11y-guidelines.orange.com/en/articles/accessible-svg/)
- [W3C ACT SVG Accessible Name](https://www.w3.org/WAI/standards-guidelines/act/rules/7d6734/proposed/)

### Libraries + Generative
- [D3.js Official](https://d3js.org/)
- [GSAP GreenSock](https://gsap.com/)
- [Snap.svg](http://snapsvg.io/)
- [SVG.js](https://svgjs.dev/)
- [Two.js](https://two.js.org/)
- [Paper.js](http://paperjs.org/)
- [p5.js Official](https://p5js.org/)
- [Generative Art with JavaScript and SVG (Springer 2024 David Matthew)](https://link.springer.com/book/10.1007/979-8-8688-0086-3)
- [Awesome Creative Coding GitHub](https://github.com/terkelg/awesome-creative-coding)

### Editors
- [Inkscape Official](https://inkscape.org/)
- [Figma](https://www.figma.com/)
- [Boxy SVG](https://boxy-svg.com/)
- [Affinity Designer Serif](https://affinity.serif.com/designer/)
- [Adobe Illustrator](https://www.adobe.com/products/illustrator.html)
- [Comparison Vector Graphics Editors Wikipedia](https://en.wikipedia.org/wiki/Comparison_of_vector_graphics_editors)
- [Vectosolve Best Free SVG Editors 2026](https://vectosolve.com/blog/best-free-svg-editors-comparison-2026)

## Cross-Skill References

**Skills Avancadas / Experimentais sister (em construcao)**:
- (esta e a unica skill da categoria — futuras experimentais aqui)

**Skills Brand Design (em construcao — usaram esta como base)**:
- `logo-design-process` — Paul Rand + Saul Bass + processo design (consome esta skill para LLM workflow + entregaveis SVG)
- `brand-book-methodology` — manual identidade (referencia esta para SVG specifications)
- `paleta-cores-corporativa` — cores acessiveis WCAG (cross-ref para accessibilidade SVG aqui)
- `tipografia-corporativa` — fontes corporativas (cross-ref texto SVG aqui)
- `iconografia-corporativa` — sistema de icones (consome esta skill para geracao + composicao + symbols)
- `templates-corporativos-comerciais` — templates visuais (usa esta para diagramas + ilustracoes spot)
- `apresentacoes-decks-corporativos` — pitch/sales decks (usa esta para visualizacoes spot)
- `print-papelaria-collateral` — papelaria (mais print-focused mas SVG export base)

**Skills Comunicacao Visual & IA existentes**:
- `geracao-imagens-ia` — IA generativa raster (complementar: raster→SVG via vetorizacao Fundacao 3)
- `composicao-visual` — composicao visual fundamentos (princiopios design aplicaveis SVG composition)
- `infograficos-diagramas` — diagramas (forma de SVG complexa estruturada)
- `audio-musica-ia` — IA criativa audio (paralelo metodologico: IA criativa generative)

**Outras skills relevantes**:
- `acessibilidade-wcag` — WCAG compliance (cross-ref Fundacao SVG accessibility)
- `design-system-basico` — design tokens + components (icones SVG + Lucide/Phosphor referenced)
- `tecnicas-ia-claude-gemini-mkt` — IA aplicada MKT (esta skill estende para SVG specifically)
- `dominio-juridico-mkt` — LGPD compliance content (relevant for SVGs com dados pessoais embutidos)
- `branding` + `posicionamento-marca` + `big-idea` — foundation strategic (precede execucao SVG)

## Integracao Ecossistema Frank-MKT

`svg-engineering-ia` e a **primeira skill da categoria Skills Avancadas / Experimentais** e serve como **base ferramental** para todo o bloco brand-design futuro (8 skills em construcao).

### Posicao no ecossistema

```
ESTRATEGIA (existente, completa)
├── branding (foundation)
├── posicionamento-marca (POV)
└── big-idea (nucleo)
                ↓
EXECUCAO BRAND-DESIGN (em construcao, 8 skills futuras)
├── logo-design-process ─┐
├── iconografia-corporativa ─┼──► consome svg-engineering-ia (esta skill)
├── brand-book-methodology │
├── paleta-cores-corporativa
├── tipografia-corporativa
├── templates-corporativos-comerciais ─┐
├── apresentacoes-decks-corporativos ─┼──► consome svg-engineering-ia (visuals embedded)
└── print-papelaria-collateral ────┘
                ↓
COMPLIANCE (existente)
└── acessibilidade-wcag (validacao final)
```

### Papel desta skill

- **Ferramentas comuns**: tooling (Inkscape + Illustrator + Figma + Boxy SVG), libraries (D3/GSAP/Snap.svg), optimizers (SVGO/SVGOMG)
- **Metodologia geracao IA**: prompting techniques + decomposicao + auto-validacao + render-loop
- **State-of-art research**: papers academicos (VGBench/SVGenius/LLM4SVG/Chat2SVG/OmniSVG)
- **Workflow hybrid**: LLM draft → human refine → SVGO → deploy

### Use cases Frank-MKT integrados

**Founder pre-Series A** (R$ 0 budget):
- Frank-MKT invoca `svg-engineering-ia` (workflow Claude+Inkscape+SVGOMG) + `branding` (foundation) — bootstrap visual identity ate Series A close

**CMO Series C** (R$ 100-300k budget):
- Frank-MKT invoca esta skill (tooling map + workflow) + `branding` + `posicionamento-marca` + futuras `logo-design-process` + `iconografia-corporativa` — orchestrate agencia/freelancer humano sênior

**Agencia design entregando icon system**:
- Frank-MKT invoca esta skill (tecnica core) + futuras `iconografia-corporativa` + `brand-book-methodology` — pipeline completo

**Dev frontend integrando charts**:
- Frank-MKT invoca esta skill (libraries + build pipeline) + `acessibilidade-wcag` + `design-system-basico`

**Disclaimer educacional mandatory**: "Este conteudo e educacional e nao substitui design senior humano para identidade comercial. Esta skill e ferramental + metodologica + state-of-art research; producao comercial seria exige `logo-design-process` + `brand-book-methodology` + `paleta-cores-corporativa` + `tipografia-corporativa` + `iconografia-corporativa` (em construcao) + designer humano sênior. Cross-skill complementar: branding, posicionamento-marca, big-idea, composicao-visual, geracao-imagens-ia, acessibilidade-wcag, design-system-basico, tecnicas-ia-claude-gemini-mkt."
