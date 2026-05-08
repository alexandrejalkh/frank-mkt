---
name: geracao-imagens-ia
description: "Geracao de imagens com IA aplicada a marketing — comparativo profundo dos 7 modelos top 2026 + workflow IA->IA. **Modelos**: **Midjourney v7** (artistic king, $10-60/mes, --oref/--sref, 95% text V7), **GPT Image 1.5** (prompt understanding, ChatGPT Plus/API), **Imagen 4 family Google** (3 tiers Fast $0.02 / Standard $0.04 / Ultra premium, 2K resolution, S-tier photorealism abr/2026, SynthID invisible watermark obrigatorio), **FLUX.2** (Black Forest Labs nov/2025, **10 reference images por gen, LoRA brand-specific, $0.01-0.10**), **Stable Diffusion 4** (free open-source, self-hostable), **Adobe Firefly** (IP indemnification - unico safe enterprise commercial), **Ideogram V3** (text rendering 90-95% accuracy). **Claude (UNICO para SVG/vector)**: gera codigo SVG/HTML/React/Mermaid via Artifacts panel — best-in-class SVG (Claude 4.5), code-first quality exceeds GPT/Gemini, NAO photorealism. **Workflow IA->IA**: ChatGPT gera prompt detalhado -> Midjourney executa -> Gemini/Imagen edita -> loop iterativo. **Brand consistency**: FLUX LoRA training + Midjourney --oref + --sref. **Text in images**: Ideogram > Imagen 4 > Midjourney V7. **Vector vs Bitmap**: Claude SVG (escalavel, codigo, logos/icons/diagrams) vs Midjourney/Imagen/FLUX bitmap (photorealism). **Compliance**: Firefly unico enterprise-safe (IP indemnification), SynthID watermark invisivel obrigatorio Imagen, Lei 15.325/2026 + LGPD. Use cases marketing: product shots, social ads, infographic illustrations, ad creative, brand visual identity, mockups."
user-invocable: false
last_verified: 2026-05-08
next_review: 2026-08-08
volatility: high
regrounding_sources:
  - "https://docs.midjourney.com"
  - "https://platform.openai.com/docs/guides/images"
  - "https://ai.google.dev/gemini-api/docs/imagen"
  - "https://docs.bfl.ml"
  - "https://docs.anthropic.com"
  - "https://www.adobe.com/products/firefly.html"
  - "https://stability.ai"
---

# Skill: geracao-imagens-ia

> **Decaimento Temporal**
> Ultima verificacao: 2026-05-08 | Proxima revisao: 2026-08-08 | Volatility: **high** (3 meses)
> Modelos lancam versoes a cada 3-6 meses: Imagen 4 family abr/2026 (Google), FLUX.2 nov/2025 (Black Forest), Midjourney v7 com Omni Reference, GPT Image 1.5 successor DALL-E 3, Claude 4.5 SVG. Pricing muda mensalmente. **Re-validar antes de publicar peca formal:**
> - Midjourney Docs — https://docs.midjourney.com
> - OpenAI Images API — https://platform.openai.com/docs/guides/images
> - Google Imagen API — https://ai.google.dev/gemini-api/docs/imagen
> - Black Forest Labs (FLUX) — https://docs.bfl.ml
> - Anthropic Docs (Claude) — https://docs.anthropic.com
> - Adobe Firefly — https://www.adobe.com/products/firefly.html
> - Stability AI — https://stability.ai
>
> **Acionamento:** decisao de modelo de geracao de imagem; prompt engineering; brand consistency com IA; workflow IA->IA; SVG vs bitmap; compliance comercial (IP indemnification); product photography com IA; social media ad creative com IA; infographic illustrations; logo / icon design IA-assisted.
> **Skills relacionadas:** `social-media-fundamentos` (modelo mental visual em redes), `instagram-feed-reels` + `tiktok-criativo` (creative para Reels/Shorts), `instagram-ads` + `facebook-ads` (creative ads), `seo-on-page` (image SEO + alt text), `branding`, `composicao-visual` (proxima skill — cores, palco, hierarquia), `infograficos-diagramas` (proxima skill — Mermaid/PlantUML), `audio-musica-ia` (proxima skill — counterpart audio), `compliance-lgpd` (juridico — direito de imagem), `conhecimento-conar-cdc` (publicidade enganosa visual).
> **Pre-requisito:** nenhum especifico, mas `social-media-fundamentos` ajuda contexto de uso.

---

## 1. Visao Geral

Geracao de imagens com IA passou de **experimento (2022-2023)** a **infraestrutura de marketing (2026)**. Brands publicam **30-70% do creative** social/ads com assistencia IA. Modelos especializados surgiram:

- **Midjourney v7** — artistic quality king
- **GPT Image 1.5** — prompt understanding king (compreende instrucoes complexas)
- **Imagen 4 Ultra** — photorealism S-tier (abr/2026)
- **FLUX.2** — brand consistency king (10 ref images + LoRA)
- **Claude 4.5** — **UNICO para SVG/vector** (codigo, nao bitmap)
- **Adobe Firefly** — commercial safe king (**IP indemnification**)
- **Ideogram V3** — text-in-image king (95% accuracy)
- **Stable Diffusion 4** — open-source king (self-host, free)

**Esta skill** te ajuda a decidir qual modelo usar para qual tipo de imagem, executar prompts otimos por modelo, montar **workflows IA->IA** (ChatGPT gera prompt → Midjourney executa), garantir **brand consistency** (LoRA/--oref/--sref), e atender **compliance** (IP indemnification, SynthID watermark, LGPD direito de imagem).

### 1.1 Acionamento

| Gatilho | Exemplo |
|---------|---------|
| Decisao de modelo | "preciso 50 product shots — qual IA?" |
| Brand consistency | "como manter rosto/produto identico em 20 imagens?" |
| SVG vs Bitmap | "preciso logo escalavel — Claude ou Midjourney?" |
| Prompt nao funciona | "prompt em portugues + Midjourney = generico — fix?" |
| Workflow IA->IA | "como combinar ChatGPT + Midjourney eficiente?" |
| Compliance enterprise | "marca grande + IA generativa = risco IP?" |
| Text em imagem | "poster com texto legivel — qual IA?" |
| Custo otimization | "$500/mes em Midjourney — economizar?" |
| Open-source / self-host | "marca quer privacidade — FLUX local?" |

### 1.2 Pre-requisitos

- [ ] **Conta** em pelo menos 1 modelo (Midjourney, ChatGPT Plus, Gemini, FLUX, Adobe Firefly).
- [ ] **Brand guidelines** definidos (paleta, voz visual, do/dont).
- [ ] **Compliance check** se enterprise (IP, image rights, SynthID).
- [ ] **Use case claro** (social media ad / product shot / logo / infographic / illustration).

> **Cristal C0 — NAO CHUTAR.** IA generativa muda mensalmente — versoes, pricing, capabilities. Re-validar a cada 3 meses.

---

## 2. Os 7+ modelos top 2026 — comparativo profundo

### 2.1 Tabela executiva

| Modelo | Forte em | Fraco em | Pricing | Output |
|--------|----------|----------|---------|--------|
| **Midjourney v7** | Artistic, aesthetic, mood, style | Realistic faces antes V7, prompt adherence variavel | $10-60/mes subscription | Bitmap PNG/JPG |
| **GPT Image 1.5** (DALL-E 4 successor) | Prompt understanding, complex instructions, integration ChatGPT | Artistic mood vs Midjourney | $20/mes ChatGPT Plus + API | Bitmap |
| **Imagen 4 Ultra** (Google Gemini) | **Photorealism S-tier**, 2K resolution, fine details (fabric, water, fur) | Subscription complexity, less artistic | **$0.02-Ultra** per image API | Bitmap + SynthID watermark |
| **FLUX.2** (Black Forest Labs) | **Brand consistency (10 ref images, LoRA)**, photorealism | Setup complexo (self-host ou API) | $0.01-0.10/img + LoRA training | Bitmap |
| **Stable Diffusion 4** | Open-source, self-host, **GRATIS**, customizable | Setup tecnico exige GPU local OU API | Free OU $0.005-0.02/img API | Bitmap |
| **Adobe Firefly** | **IP INDEMNIFICATION** (unico enterprise-safe), Adobe ecosystem | Quality menor que Midjourney | $5-30/mes Creative Cloud add-on | Bitmap |
| **Ideogram V3** | **Text rendering 95% accuracy** (posters, greeting cards, comics) | Outros aspectos medios | $7-20/mes | Bitmap |
| **Claude 4.5** | **UNICO SVG/vector code-first**, Mermaid, React, ASCII | NAO bitmap, NAO photorealism | $20/mes Pro | SVG/HTML/React code |

### 2.2 Por categoria de uso

```
PHOTOREALISM (product shots, lifestyle, hyper-real)
   1. Imagen 4 Ultra (S-tier abr/2026)
   2. FLUX 1.1 Pro Ultra
   3. Midjourney v7
   4. GPT Image 1.5

ARTISTIC / AESTHETIC (mood, brand-feel, illustration)
   1. Midjourney v7 (king)
   2. FLUX.2
   3. Stable Diffusion XL / 4

TEXT IN IMAGES (posters, ads com legenda, comics, greeting cards)
   1. Ideogram V3 (95% accuracy)
   2. Imagen 4 Ultra (improved 2026)
   3. Midjourney v7 (95% V7 update)
   4. GPT Image 1.5

PROMPT UNDERSTANDING (instrucao complexa, multi-elemento)
   1. GPT Image 1.5 (king)
   2. Imagen 4 Ultra
   3. FLUX.2

VECTOR / SVG (logo, icon, diagram, infographic)
   1. Claude 4.5 (UNICO native)
   2. Outros: NAO suportam SVG nativo

BRAND CONSISTENCY (mesmo personagem/produto em N imagens)
   1. FLUX.2 (10 ref images, LoRA training)
   2. Midjourney v7 (--oref, --sref)
   3. Stable Diffusion + LoRA self-host

OPEN-SOURCE / SELF-HOST (privacidade, sem subscription)
   1. Stable Diffusion 4
   2. FLUX 1 Schnell (Apache 2.0)

COMMERCIAL SAFE / ENTERPRISE (IP indemnification)
   1. Adobe Firefly (UNICO com IP indemnification)
   2. Outros: risco IP variavel

VOLUME ALTO (cost optimization)
   1. Imagen 4 Fast ($0.02)
   2. FLUX Schnell ($0.01)
   3. Stable Diffusion self-host (gratis)
```

### 2.3 Imagen 4 Family — detalhe (Google, abr/2026)

```
IMAGEN 4 FAST — $0.02 per image
   Use: high-volume, A/B testing, quick mockups
   Speed: rapidissimo
   Quality: boa

IMAGEN 4 STANDARD — $0.04 per image
   Use: production work, social media ads
   Quality: alta + improved text rendering

IMAGEN 4 ULTRA — premium pricing
   Use: hero campaign images, fine detail required
   Quality: S-TIER photorealism (intricate fabrics, water droplets, animal fur, 2K resolution)
   
TODAS recebem SynthID watermark INVISIVEL automaticamente
```

### 2.4 FLUX.2 — detalhe (Black Forest Labs, nov/2025)

```
FLUX.2 KEY FEATURES
====================

10 REFERENCE IMAGES por geracao
   - Mantem character identity, product appearance, visual style
   - Multi-scene creative workflows

LoRA TRAINING brand-specific
   - Treinar modelo customizado para sua marca
   - Resultado: imagens IA com seu DNA visual consistente

LICENSE TIERS:
   - FLUX Schnell: Apache 2.0 (commercial OK)
   - FLUX Dev: restrictive (research/personal)
   - FLUX Pro: commercial via API only

PRICING:
   - Hosted API: $0.01-$0.10/imagem
   - Self-host: GPU 8GB+ (RTX 3080+)

USE CASES MARKETING:
   - Branded content em escala
   - Recurring characters (mascote, founder digital twin)
   - Multi-scene campaigns
   - Product shots consistentes
```

### 2.5 Claude — caso especial (vector/SVG)

```
CLAUDE 4.5 GENERATION — DIFERENTE DOS OUTROS
===============================================

NAO gera bitmap raster (PNG/JPG).
Gera CODIGO que renderiza visualmente:

OUTPUTS:
   - SVG (Scalable Vector Graphics) — escalavel a qualquer tamanho
   - HTML/CSS visual layouts
   - React components interativos
   - Mermaid diagrams (flowcharts, sequence, gantt)
   - PlantUML
   - ASCII art

ARTIFACTS PANEL:
   - Live preview no chat
   - Edicao iterativa
   - Sem export para outras tools

FORTE EM:
   - Diagramas tecnicos
   - Logos (geometricos)
   - Icons
   - Charts data viz
   - Architectural diagrams software
   - Brand assets simples
   - Apresentacao graphics

FRACO EM:
   - Photorealism (impossivel)
   - Illustracao detalhada
   - Cenas complexas multi-elemento
   - Spatial relationships precisos

QUANDO ESCOLHER CLAUDE vs OUTROS:
   - Logo escalavel → Claude SVG
   - Logo com gradient/realism → Midjourney → trace SVG manual
   - Diagrama de arquitetura → Claude
   - Hero image campanha → Midjourney/Imagen
   - Icon set 50 itens → Claude (consistencia)
   - Product photo → Imagen 4 Ultra
```

---

## 3. Prompt engineering por modelo

### 3.1 Midjourney v7 — formula consolidada

```
ESTRUTURA RECOMENDADA V7:

[Subject] + [Medium] + [Environment] + [Lighting] + [Mood] + [Camera/Style] + [Parameters]

EXEMPLO:
"professional female executive in her 40s, photorealistic, 
modern Sao Paulo office with glass walls and city skyline 
background, soft natural lighting from large window, 
confident and approachable mood, shot on Sony A7R V with 
85mm lens, depth of field f/2.8, --ar 4:5 --s 100 --v 7"

PARAMETROS V7:
   --ar 4:5     Aspect ratio (4:5 social posts; 16:9 video; 9:16 Stories)
   --s 100      Stylization (default; --s 250 mais artistico, --s 50 mais literal)
   --v 7        Modelo version
   --oref URL   Omni Reference (consistencia personagem/objeto NOVO V7)
   --sref URL   Style Reference (mood/aesthetic referencia)
   --no [list]  Excluir elementos
   --c [0-100]  Chaos (variacao; default 0; --c 50 = mais variedade entre 4 outputs)
   --weird [0-3000]  Quirky output
   --tile       Repeating pattern
```

**V7 game-changers:**
- **Omni Reference (--oref)**: anchor identity em base image — face/produto consistente sem reescrever features.
- **Style Reference (--sref)**: applies moodboard/aesthetic.
- **95% text accuracy** (V7 update): text rendering melhorou drasticamente.

### 3.2 GPT Image 1.5 — natural language prompt

```
ESTILO PROMPT GPT IMAGE 1.5:

Linguagem natural conversacional. Descricao detalhada COM contexto.

EXEMPLO:
"Generate a product photography image of a glass bottle of 
artisanal hot sauce, label says 'Habanero Heat 2026' in bold 
red, photographed on a rustic wooden table with scattered red 
pepper flakes around the base. Soft warm lighting from the 
left, slight steam wisp suggesting heat. The composition should 
feel inviting and premium, like a magazine ad for Bon Appetit. 
4:5 aspect ratio."

PRINCIPIOS:
- Frases completas > keywords
- Contexto de uso explicito ("for a magazine ad", "for Instagram")
- Composicao descrita semanticamente
- Linguagem que voce usaria com fotografo profissional
```

### 3.3 Imagen 4 — direct, descriptive

```
ESTILO IMAGEN 4:

Direto, descritivo, photorealism-friendly. Aceita instrucoes simples e detalhadas.

EXEMPLO PHOTOREALISM:
"A perfect coffee bean close-up, water droplets on surface, 
intricate texture details, professional product photography, 
2K resolution, dramatic single-source lighting, dark moody 
background, hyperrealistic"

EXEMPLO TEXT:
"A retro 1970s diner sign with the text 'OPEN 24/7' in vibrant 
neon letters, glowing pink and blue, against a dark night sky, 
photorealistic, cinematic"

IMAGEN 4 STRENGTHS:
   - Fine detail (fabric texture, fur, water)
   - Text rendering improved 2026
   - 2K resolution (Ultra tier)
   - SynthID watermark invisivel automatic
```

### 3.4 FLUX.2 — reference-driven

```
FLUX.2 WORKFLOW:

1. UPLOAD ate 10 REFERENCE IMAGES:
   - Foto da pessoa/produto
   - Brand visual moodboard
   - Cenas anteriores que voce gostou

2. PROMPT NATURAL LANGUAGE:
   "Same person from references, now in office setting, 
    professional attire, soft lighting, photorealistic"

3. MULTI-SCENE GENERATION:
   - Mesmo personagem em 5 cenas diferentes
   - Mesmo produto em 5 angulos
   - Visual style consistente

LoRA TRAINING (advanced):
   - Train modelo customizado com 20-50 fotos da marca/pessoa
   - Resultado: gerador IA com DNA visual proprio
   - Inferencia super rapida apos treino
```

### 3.5 Claude — prompt para SVG/Mermaid

```
PROMPT PARA SVG NO CLAUDE:

"Crie um logo SVG minimalista para uma marca de skincare chamada 
'Serenity Glow'. Conceito: gota de agua com brilho sutil. Cores: 
azul claro (#A8D8EA) e branco. Estilo: clean, premium, escalavel. 
Output: codigo SVG inline rodando em Artifacts panel."

PROMPT PARA MERMAID DIAGRAM:

"Crie um Mermaid flowchart do funil de marketing B2B SaaS:
- Awareness (Reels Ads, Content)
- Interest (Lead Magnet)
- Consideration (Email Nurture)
- Decision (Demo)
- Action (Sale)
- Retention (CSM)
- Advocacy (NPS, Refer)

Mostrar metricas-chave em cada etapa."

CLAUDE FORTE EM:
   - Iteracao rapida (preview live)
   - Refatoracao codigo
   - Multi-output (logo + variantes)
```

### 3.6 Ideogram — text-first

```
PROMPT IDEOGRAM:

"A motivational poster with the text 'BUILD IN PUBLIC' in 
massive bold typography, retro 80s style, neon glow, 
geometric background, vintage poster aesthetic, 4:5"

PRINCIPIOS:
- Text PRIMEIRO no prompt
- Quotation marks ao redor do texto exato
- "legible text, clear typography" para reforco
- Manter texto curto (1-5 palavras)
```

---

## 4. Workflow IA → IA — chain of AI

### 4.1 Por que workflow IA → IA

Cada modelo tem ponto forte. **Combinar** atinge resultado que NAO modelo unico atinge.

```
ANALOGIA:
   Midjourney sozinho:    Pintor talentoso mas sem briefing claro
   ChatGPT sozinho:       Briefing perfeito mas sem mao para pintar
   ChatGPT + Midjourney:  Briefing perfeito EXECUTADO por pintor talentoso
```

### 4.2 Workflow tipo 1 — ChatGPT prompt → Midjourney execute

```
WORKFLOW BASICO

ETAPA 1 — Voce conta sua intencao para ChatGPT:
   "Preciso de imagem hero para landing page de SaaS B2B fintech 
   focado em founders 30-45. Tom: confiavel, premium, tech-modern. 
   Audience: Sao Paulo. Aspect ratio 16:9. Quero gerar prompt 
   otimizado para Midjourney v7."

ETAPA 2 — ChatGPT gera prompt detalhado:
   "Confident professional founder in his 30s, focused expression, 
   working at modern minimalist desk with multiple screens showing 
   financial data graphs in soft glow, contemporary Sao Paulo 
   skyline visible through floor-to-ceiling windows in background, 
   warm natural lighting from window mixing with cool screen glow, 
   premium tech aesthetic, shot on Sony A7R V, 35mm lens, depth of 
   field f/2.0, photorealistic, --ar 16:9 --s 150 --v 7"

ETAPA 3 — Voce cola prompt no Midjourney
   - Gera 4 variations
   - Escolhe a melhor
   - Upscale ou variations refinement

ETAPA 4 — Iterate (se nao perfeito):
   - Cola imagem de volta no ChatGPT
   - Pergunta: "Refine prompt para [ajuste especifico]"
   - Rodada 2 no Midjourney
```

### 4.3 Workflow tipo 2 — Multi-stage Generation

```
WORKFLOW AVANCADO — 4 IAs EM CADEIA

OBJETIVO: hero image campaign + variations social

1. CHATGPT (briefing → prompt)
   In: brand brief, audience, mood
   Out: prompt detalhado Midjourney

2. MIDJOURNEY v7 (creative hero)
   In: prompt do ChatGPT
   Out: hero image artistic 1920×1080

3. IMAGEN 4 (refinement / photorealism)
   In: hero do Midjourney + prompt "make this more photorealistic, 
       fine detail in fabric, sharper face features"
   Out: photorealistic version

4. CLAUDE (logo SVG overlay)
   In: brand name + concept
   Out: SVG logo escalavel

5. CHATGPT/CANVA (compor final)
   - Hero Imagen + Logo Claude SVG sobreposto
   - Texto CTA
   - Export multi-format (1920×1080 / 1080×1080 / 1080×1920)
```

### 4.4 Workflow tipo 3 — Brand consistent series

```
SERIE DE 20 IMAGENS COM MESMO PERSONAGEM

OBJETIVO: 20 product shots / lifestyle com mesma modelo

OPCAO A — FLUX.2 (recomendada)
   1. Carregar 10 fotos de referencia da modelo
   2. Prompts variando contexto (escritorio, cafe, casa, rua, gym)
   3. FLUX preserva identity automatically
   4. 20 imagens consistentes em ~30 min

OPCAO B — Midjourney v7 --oref
   1. Gerar 1 imagem hero da modelo
   2. Save URL
   3. Em todos os 19 prompts seguintes: --oref [URL]
   4. Identidade preservada com variacao de cenario

OPCAO C — Stable Diffusion + LoRA training
   1. Train LoRA customizado com 20-50 fotos modelo
   2. Inferencia rapida com qualquer prompt
   3. Self-host = privacidade + custo zero apos training
```

### 4.5 Workflow tipo 4 — Iteration loop

```
LOOP ITERATIVO (quando nada esta bom)

Round 1: prompt X → output A (60% bom)
   |
   Mostra A para ChatGPT
   "What's wrong with this image?"
   |
ChatGPT analise: "Lighting harsh, pose stiff, color palette off-brand"
   |
Round 2: prompt X' (refinado pelo ChatGPT) → output B (75% bom)
   |
   Mostra B para Claude
   "What composition tips would improve this?"
   |
Claude analise: "Try rule of thirds, soften background, warm color grade"
   |
Round 3: prompt X'' → output C (90% bom)
   |
   Refine final em Photoshop/Photopea/Canva
   = PRODUCAO READY
```

---

## 5. Vector vs Bitmap — decisao critica

### 5.1 Differenca fundamental

```
VECTOR (SVG, AI/Adobe Illustrator)
   - Codigo matematico (paths, shapes, fills)
   - Escalavel a qualquer tamanho SEM perda
   - Editavel infinitamente
   - File size pequeno
   - Geracao via Claude (UNICO IA native)
   
BITMAP (PNG, JPG, WebP)
   - Pixels em grid fixo
   - Escala perde qualidade (pixelado)
   - Edicao destrutiva
   - File size maior
   - Geracao via Midjourney/Imagen/FLUX/DALL-E
```

### 5.2 Quando vector / quando bitmap

| Use case | Vector ou Bitmap? |
|----------|-------------------|
| **Logo da marca** | **VECTOR** sempre (escalavel) |
| **Icon set 50 itens** | **VECTOR** (consistencia) |
| **Diagrama de arquitetura** | **VECTOR** (Mermaid, PlantUML) |
| **Infographic data viz** | **VECTOR** + bitmap inserts |
| **Hero photo campanha** | **BITMAP** (photorealism) |
| **Product shot** | **BITMAP** |
| **Cenario detalhado** | **BITMAP** |
| **Personagem ilustrado** | **BITMAP** ou vector estilizado |
| **Banner web simples** | **VECTOR** (CSS + SVG) |
| **Banner web rich** | **BITMAP** |
| **Social media post** | **BITMAP** (formatos nao aceitam SVG) |
| **Documento corporativo** | **MISTO** (SVG icons + bitmap photos) |

### 5.3 Conversao quando necessario

```
VECTOR → BITMAP (precisa de pixel para social)
   - Open SVG no Inkscape / Figma / Adobe Illustrator
   - Export PNG @1x, @2x, @3x (mobile retina)
   - Or use online: cloudconvert.com, vector to PNG

BITMAP → VECTOR (precisa escalavel)
   - Adobe Illustrator: Image Trace
   - Inkscape: Path > Trace Bitmap
   - Online: vectorizer.ai, vectormagic.com
   - AI: Vectorizer.AI ($) com IA tracing
   
RESULTADO: bitmap → vector PERDE detalhes, simplifica.
   Logos simples convertem bem. Photos NAO.
```

---

## 6. Brand consistency — 3 abordagens

### 6.1 Por que importa

Marca em 2026 publica 30-100+ imagens/mes. **Consistencia visual** = reconhecimento. IA generativa por default produz **variacao caotica** entre prompts. 3 abordagens para domar:

### 6.2 Abordagem 1 — Midjourney --oref + --sref

```
STYLE BIBLE EM IMAGEM

1. Criar 1 imagem master com brand DNA visual
   "premium minimalist Brazilian fintech aesthetic, 
   warm earth tones, sans-serif typography, modern editorial 
   photography, soft natural light, --ar 1:1 --s 200 --v 7"

2. Save URL da imagem master

3. Em TODOS prompts seguintes:
   "[your prompt] --sref [MASTER URL] --s 100"
   → mantem aesthetic mood

4. Para personagem/produto especifico:
   "[your prompt] --oref [CHARACTER URL] --sref [MASTER URL]"
   → identity + aesthetic
```

### 6.3 Abordagem 2 — FLUX LoRA training (avancado)

```
LORA = Low-Rank Adaptation

1. COLETAR 20-50 imagens da marca/pessoa/produto
   - Variacoes de angulo, luz, contexto
   - Resolucao 1024×1024+

2. TREINAR LoRA (cloud ou local GPU)
   - Servico: Replicate, Civitai, RunDiffusion
   - Custo: $5-50 por LoRA training
   - Tempo: 30-180 min

3. APLICAR LoRA em qualquer prompt:
   "<lora:my_brand:0.8> office worker in a modern setting"
   → resultado tem DNA visual da marca

4. INFERENCIA rapida apos training
   - $0.005-0.05 per image
   - Self-host gratis com GPU
   
USE CASE: marcas com 100+ imagens/mes em escala
```

### 6.4 Abordagem 3 — Style Guide + Manual Curation

```
SE NAO TEM TEMPO/BUDGET PARA LORA:

1. Documentar "style guide" textual:
   - Color palette: 4-6 cores hex
   - Lighting style: warm/cool/neutral, soft/hard
   - Photography style: editorial, lifestyle, studio
   - Composition: rule of thirds, centered, asymmetric
   - Mood: serious, playful, premium, accessible

2. PROMPT BLOCK reutilizavel:
   "[main subject], [scene], <BRAND STYLE BLOCK: 
   warm earth tones #C9A86E #4A4A4A #FFFFFF, soft window 
   lighting from left, editorial documentary photography 
   style, rule of thirds composition, premium yet 
   accessible mood, --ar 4:5 --s 100 --v 7>"

3. Iterate ate ter 5-10 hero images consistentes

4. Use essas heroes como --sref futuras
```

---

## 7. Compliance comercial — IP + LGPD

### 7.1 IP indemnification — Adobe Firefly

**Adobe Firefly e o UNICO modelo enterprise-safe** com **IP indemnification**:

- Training data limitada a **licensed + public domain content**.
- Adobe oferece **indemnificacao** se cliente for processado por uso comercial.
- Audit trail completo.

**Outros modelos** (Midjourney, OpenAI, Imagen, FLUX): **risco IP variavel**. Treinaram em scraped content, possivel infracao copyright. **Para enterprise grandes / setores regulados, Firefly e padrao**.

### 7.2 SynthID watermark — Imagen

Todas as imagens geradas pelo **Imagen 4 family** recebem **SynthID watermark INVISIVEL** automaticamente:

- Imperceptivel ao olho humano.
- Detectavel por sistemas Google.
- Usado para identificar conteudo IA-generated.
- NAO removivel sem destruir imagem.

**Implicacao**: imagens Imagen passam em screening de plataformas (LinkedIn, Meta) que detectam AI content. Outros modelos NAO tem watermark — pode ou nao ser detectado por plataformas.

### 7.3 Direito de imagem (BR — LGPD + Codigo Civil)

```
IA GENERATIVA E DIREITO DE IMAGEM BR

CENARIO 1: Imagem com pessoa real (foto de cliente, funcionario)
   - LGPD: dado pessoal — base legal + consentimento
   - Codigo Civil art. 20: direito de imagem
   - Necessario: termo de consentimento por escrito
   - Para uso comercial: contrato com modelo

CENARIO 2: Imagem com pessoa ficticia gerada por IA
   - NAO direito de imagem (pessoa nao existe)
   - MAS: pode parecer pessoa real → risco de processo
   - Recomendacao: prompts SEM nomes especificos
   - "young Brazilian executive 30s" OK
   - "Joao Silva, CEO da empresa X" NAO OK

CENARIO 3: Imagem com celebridade gerada por IA
   - Risco ALTO — direito de imagem + conexao com marca
   - LGPD + Codigo Civil + criminal risk

CENARIO 4: Imagem de funcionario gerada como avatar
   - Necessario consent + contrato uso digital twin
   - Cuidar com saida do funcionario (revogar avatar?)
```

### 7.4 Disclosure de IA generativa

**Lei 15.325/2026 + CONAR**: conteudo paid/sponsored com **AI generative imagery** pode exigir disclosure caso induza confusao.

**Recomendacao**:
- Imagens de **produto real** + IA enhancement: aceitavel sem disclosure.
- Imagens **100% IA-generated** representando **cenas reais que nunca aconteceram** (cliente usando produto, cenario de empresa que nao existe): **disclose** com pequeno texto "imagem ilustrativa" ou "AI-generated".
- IA imagery em **journalism / news / photo essay**: **disclose** sempre.

### 7.5 Plataformas que detectam IA content

| Plataforma | Politica 2026 |
|-----------|----------------|
| **LinkedIn** | Pode flag IA-generated imagery em paid ads |
| **Meta (FB/IG)** | Detect AI imagery via SynthID + outros markers; **label automatico** "Made with AI" em alguns casos |
| **TikTok** | Label "AI-generated content" em rollout |
| **Google Search** | Image search marca content suspected AI |
| **News publishers** | Detect via sistemas anti-deepfake |

---

## 8. Use cases marketing — fluxos operacionais

### 8.1 Product photography com IA

```
USE CASE: 30 product shots para e-commerce

WORKFLOW:
1. Foto base do produto real (smartphone OK)
2. Upload para FLUX.2 ou Imagen 4
3. Prompt: "product photo of [produto], white seamless background, 
   studio lighting, 360-degree visible, photorealistic, 4K"
4. Gerar 5-10 variations (angulos, fundos)
5. Image2Image: alterar fundos (lifestyle, cenarios)
6. Compose final em Photoshop/Photopea com logo

OUTPUT: 30 product shots em ~4 horas vs 2 dias studio fisico.
COST: $50-200 vs $2.000-10.000 photoshoot.
```

### 8.2 Social media ad creative

```
USE CASE: 10 ad creatives Reels/Stories Instagram

WORKFLOW:
1. ChatGPT: gerar 10 conceitos de hook visual
2. Para cada hook: prompt Midjourney v7 detalhado
3. Midjourney: gerar variations
4. Selecionar best
5. CapCut/Adobe Express: compor video Reels (15-30s) com:
   - Hero image IA generated
   - Texto-on-screen
   - Trending audio
   - Captions
6. Submeter ao Meta Ads Manager (cf. instagram-ads)

CAVEAT: Reels prefer SOUND-ON (cf. instagram-feed-reels Sec 5.4) — 
audio essencial > visual sozinho.
```

### 8.3 Infographic illustration

```
USE CASE: Infographic data viz B2B SaaS

WORKFLOW HIBRIDO:
1. CLAUDE: gerar SVG diagram base (Mermaid flowchart OU custom SVG)
2. CLAUDE: gerar icons SVG individuais (escalavel)
3. MIDJOURNEY: gerar background photographic (se necessario)
4. FIGMA / CANVA: compor final
   - SVG diagram top
   - Icons SVG
   - Tipografia (Google Fonts)
   - Brand colors
5. Export PDF + PNG @1x/2x/3x

OUTPUT: infographic profissional em ~2 horas vs 1-2 dias designer.
```

### 8.4 Brand identity — logo + variants

```
USE CASE: Logo design para nova marca

WORKFLOW:
1. CLAUDE: gerar 20 conceitos SVG diferentes
   "Logo SVG para marca [nome] tipo [categoria], conceito 
   [conceito], cores [paleta]. Variar entre minimalist, 
   geometric, type-driven, mark+wordmark."
2. CLAUDE: refinar 3-5 favoritos
3. CLAUDE: gerar variations (horizontal, vertical, mark only, 
   wordmark only, color, mono, inverted)
4. EXPORT como SVG (escalavel)
5. CONVERT para PNG/PDF para uso final

CAVEAT: Claude SVG e geometrico/code-based. Para logos com 
gradient/photorealism, usar Midjourney → vetorizar manualmente.
```

### 8.5 Avatares + mascotes

```
USE CASE: Mascote da marca (cachorro pet shop, executivo empresa)

WORKFLOW:
1. ChatGPT: definir character bible
   - Especies: golden retriever
   - Personalidade: amigavel, brincalhao, profissional
   - Cores brand: marrom + verde
   - Pose default: sentado feliz

2. MIDJOURNEY v7: gerar character base
   "happy golden retriever mascot, professional pet shop branding, 
   illustrated style, friendly pose, warm earth tones, 4K, 
   --ar 1:1 --s 200 --v 7"

3. SAVE URL como --oref futuro

4. GERAR variations:
   "[same dog] sleeping --oref [URL]"
   "[same dog] playing fetch --oref [URL]"
   "[same dog] receiving treat --oref [URL]"

5. RESULT: 10-20 mascote shots consistentes
```

### 8.6 Apresentacao executiva (slides)

```
USE CASE: Pitch deck B2B SaaS

WORKFLOW:
1. CLAUDE: gerar SVG icons + diagrams para cada slide
2. MIDJOURNEY: gerar 2-3 hero images (capa, secões)
3. FIGMA / Powerpoint / Google Slides: compor
4. Manter:
   - Brand colors consistente
   - Tipografia consistente
   - Hierarquia visual
   - 1 ideia por slide
   
RESULT: pitch deck premium em ~4-6 horas vs 2-3 dias.
```

---

## 9. Anti-patterns 2026

| Anti-pattern | Por que e problema |
|--------------|---------------------|
| **Usar Midjourney para SVG** | Nao gera vector — somente bitmap |
| **Usar Claude para photorealism** | Nao gera bitmap — somente SVG/code |
| **Prompts em portugues no Midjourney** | Performance inferior — usar ingles |
| **Sem reference images em FLUX** | Perde 80% do potencial brand consistency |
| **Hero image sozinha sem brand DNA** | Fica generica IA-look identificavel |
| **IA imagery sem disclosure em journalism** | CONAR/CDC risco |
| **Imagem de pessoa real sem consent** | LGPD + Codigo Civil art. 20 |
| **Open-source self-host sem compute** | GPU 8GB+ obrigatorio |
| **Confiar em IA para fine detail** (face, hands em V6 e anteriores) | Distortion frequente |
| **Volume sem brand consistency** | 100 images IA caoticas = brand dilution |
| **Sem iteracao** (1 prompt → 1 image final) | 80% das imagens precisam 3-5 rounds |
| **Esquecer SynthID** em compliance | Imagem detectavel em screenings |
| **Adobe Firefly desconsiderado em enterprise** | Risco IP indemnification |
| **Midjourney v6 ou anterior em 2026** | V7 muito superior |
| **DALL-E 3 quando GPT Image 1.5 disponivel** | 1.5 muito melhor |
| **Imagen 3 quando Imagen 4 disponivel (abr/2026+)** | 4 e S-tier |

---

## 10. Custos comparados (2026)

```
SCENARIO: 100 imagens/mes

MIDJOURNEY (Pro plan)
   $30/mes ilimitado fast hours
   ROI: $0.30/imagem
   Total: $30/mes

GPT IMAGE 1.5 (ChatGPT Plus)
   $20/mes (ChatGPT Plus) com limites
   API: $0.04-0.16/imagem
   Total: $20-36/mes

IMAGEN 4 FAMILY (Google Gemini API)
   Fast: $0.02 × 100 = $2/mes
   Standard: $0.04 × 100 = $4/mes
   Ultra: ~$0.10 × 100 = $10/mes

FLUX.2 (Black Forest Labs API)
   $0.01-0.10/imagem
   Total: $1-10/mes (Schnell vs Pro)
   + LoRA training: $5-50 one-time

STABLE DIFFUSION 4 (self-host)
   Hardware: GPU 8GB+ ($300-2000 one-time)
   Inferencia: gratis apos hardware
   Total: $0/mes (mas custo entry alto)

ADOBE FIREFLY (Creative Cloud add-on)
   $5-30/mes
   Volume: ate 1000 generations Firefly tier
   Total: $5-30/mes

CLAUDE (Pro)
   $20/mes
   Output: SVG/code (nao bitmap)
   Total: $20/mes

IDEOGRAM (Plus)
   $7/mes (slow) ou $20/mes (fast)
```

### 10.1 Recomendacao por orcamento

```
ORCAMENTO ZERO/STARTUP (<$30/mes)
   - Stable Diffusion self-host (free, mas precisa GPU)
   - OU Midjourney Basic ($10/mes, limited)
   - OU Imagen 4 Fast ($2/mes para 100 imagens)

ORCAMENTO PEQUENO ($30-100/mes)
   - Midjourney Pro ($30) + ChatGPT Plus ($20) = $50/mes (combo classico)
   - + Claude Pro ($20) para SVG

ORCAMENTO MEDIO ($100-500/mes)
   - Midjourney Pro + Imagen 4 Standard + ChatGPT + Claude = $90-150/mes
   - FLUX.2 Pro API se brand consistency critico = +$50-200

ORCAMENTO ENTERPRISE ($500+/mes)
   - Adobe Firefly (IP indemnification mandatory) = $30-100/mes
   - + Midjourney + ChatGPT + Imagen + FLUX
   - + LoRA training quarterly
   - Stack total: $200-1000/mes
```

---

## 11. Workflow operacional 90 dias

```
ADOPTING IA GENERATIVA — 90 DIAS

WEEK 1-2 — ASSESSMENT + SETUP
   [ ] Audit volume de imagens/mes atual
   [ ] Brand guidelines documentados
   [ ] Compliance review (IP, LGPD, disclosure)
   [ ] Escolher 3-4 modelos primarios
   [ ] Sign up + setup
   [ ] Team training basico

WEEK 3-4 — EXPERIMENTATION
   [ ] 50-100 generations testando cada modelo
   [ ] Identificar STRENGTHS por modelo
   [ ] Documentar prompt templates
   [ ] Create style guide visual

MONTH 2 — INTEGRATION
   [ ] Workflow IA→IA estabelecido
   [ ] Brand consistency strategy (--oref/--sref OU LoRA)
   [ ] 20-30% de imagens production = IA-generated
   [ ] A/B test IA vs traditional

MONTH 3 — SCALE
   [ ] 50-70% imagens = IA-generated
   [ ] LoRA brand-specific training (se FLUX)
   [ ] Compliance docs atualizados
   [ ] ROI measurement (cost/image vs quality)

POS-90D
   [ ] Re-validar modelos trimestral (volatility high)
   [ ] Budget optimization (modelos por use case)
   [ ] Build internal IA imagery library
```

---

## 12. Regras de Ouro

1. **NAO CHUTAR** — modelos lancam versoes a cada 3-6 meses; pricing muda mensal. Re-validar trimestral.
2. **Cada modelo tem sweet spot** — Midjourney = artistic, Imagen = photoreal, GPT = prompt understanding, FLUX = brand consistency, Claude = SVG, Firefly = enterprise IP, Ideogram = text.
3. **Vector vs Bitmap decision** primeiro — nao usar Midjourney para logo escalavel.
4. **Workflow IA→IA** > modelo unico — ChatGPT (briefing) + Midjourney (execute) + Iterate.
5. **Brand consistency exige strategy** — --oref/--sref OU FLUX LoRA OU style guide rigoroso.
6. **3-5 rounds de iteracao** = padrao production-ready (1 prompt → 1 image final NAO funciona).
7. **Adobe Firefly = unico enterprise-safe** com IP indemnification.
8. **SynthID Imagen watermark invisivel** — imagens passam screenings AI detection.
9. **Prompts em INGLES** > portugues (training data dominance).
10. **Reference images** em FLUX/Midjourney --oref multiplicam qualidade.
11. **LGPD + Codigo Civil art. 20**: pessoa real em IA imagery = consent obrigatorio.
12. **Disclosure de IA imagery** em journalism / news / photo essay; em ad commercial depende de risco confusao.
13. **Plataformas detectam AI content** — preparar disclosure / labels.
14. **Custo: combo Midjourney + ChatGPT + Claude = $50-90/mes** = 80% das necessidades startup.
15. **Open-source FLUX/SD = privacidade** mas precisa GPU + setup tecnico.
16. **Iteration mais barata em modelos rapidos** (Imagen Fast, FLUX Schnell) — refinement em modelos premium.
17. **Manter "image bible"** — 5-10 hero images da marca como --sref futuras.

---

## 13. Exemplos comportamentais

### Exemplo 1 — "Logo SVG escalavel — Claude ou Midjourney?"

**Input:** "Preciso logo para skincare 'Serenity Glow'. Tipo gota de agua. Quero usar em site, post Instagram, banner outdoor. Claude ou Midjourney?"

**Resposta esperada:**

> **Claude para o logo** (SVG vector escalavel) + **Midjourney para hero images** (bitmap photorealism). NAO trocar — cada um faz o que outro nao consegue. **Razao**: logo precisa **escalar** de 16×16 favicon a 5m banner outdoor SEM perder qualidade. Bitmap (Midjourney/Imagen/FLUX) gera PNG/JPG que **PIXELA quando esticado**. Vector (Claude SVG) e codigo matematico — escala infinitamente. **Workflow recomendado**: (a) **CLAUDE — Logo concepts**: prompt "Crie 10 conceitos SVG de logo minimalista para skincare 'Serenity Glow'. Conceito gota de agua com brilho sutil. Cores azul claro #A8D8EA + branco. Estilo: clean, premium, escalavel. Output codigo SVG inline". Claude gera multiplas opcoes em Artifacts panel com preview live. Iterate refinando. (b) **CLAUDE — Variations finais**: do logo escolhido, gerar variations: horizontal, vertical, mark only, wordmark only, color, monochrome, inverted (white sobre dark). (c) **EXPORT**: salvar SVG codes; converter para PNG @1x/2x/3x para uso onde nao aceita SVG (Instagram, Facebook posts). (d) **MIDJOURNEY — Hero images** depois: prompts para campaign images com produto/lifestyle (mas SEM o logo dentro — logo aplicado em pos-producao no Figma/Photoshop). Estimativa: 2-4 horas vs designer profissional 2-5 dias / R$ 1k-15k.

**Comportamento-chave:** decisao quantitativa vector vs bitmap, oferece workflow operacional 4 etapas, alerta sobre quando NAO trocar.

### Exemplo 2 — "20 product shots consistentes — qual modelo?"

**Input:** "E-commerce moda BR. Preciso de 20 product shots da mesma blusa em modelos diferentes. Modelo precisa parecer mesma pessoa. Qual IA?"

**Resposta esperada:**

> **FLUX.2** (recomendacao primaria) — campeao brand consistency 2026 com **10 reference images por geracao** + **LoRA training** brand-specific. **Workflow recomendado**: (a) **OPCAO A — FLUX.2 com reference images** (mais simples): coletar 5-10 fotos da modelo real (ou modelo IA gerada anteriormente em Midjourney/Imagen), upload como reference, prompts variando contexto: "Same person, in office setting, professional attire, natural lighting"; "Same person, casual cafe environment, warm light"; etc. Resultado: 20 imagens com identidade preservada em ~30 min. Custo: $0.01-0.10 × 20 = $0.20-2 USD. (b) **OPCAO B — FLUX.2 com LoRA training** (avancado): se voce vai gerar 100+ imagens da modelo a longo prazo, vale treinar LoRA customizado. Coletar 30-50 fotos modelo, treinar LoRA em Replicate ($5-50 one-time), entao inferencia super rapida ($0.005-0.05/imagem). DNA visual preservado automaticamente. (c) **OPCAO C — Midjourney v7 --oref** (alternativa): gerar 1 imagem master da modelo, save URL, em todos prompts seguintes adicionar `--oref [URL]`. Identidade preservada com variacao de cenario. Mais barato ($30/mes Midjourney Pro). Caveat: --oref V7 ainda mais limitado que FLUX em fine detail. **Compliance**: se modelo e pessoa REAL (sua employee, model contratada), **consent obrigatorio LGPD + Codigo Civil art. 20** + termo de uso para gerar variations IA. Se pessoa fictícia 100% IA, OK sem consent (mas atencao para nao gerar sosias de celebrity). **Output realista**: 20 product shots consistentes em ~2 horas vs photoshoot studio 1-2 dias / R$ 5-30k.

**Comportamento-chave:** recomenda FLUX como primario, oferece 3 opcoes (FLUX ref, FLUX LoRA, Midjourney --oref), alerta compliance, projeta custo/tempo.

### Exemplo 3 — "Workflow IA→IA — como combinar?"

**Input:** "Vejo gente combinando ChatGPT + Midjourney para imagens. Como funciona? Vale a pena?"

**Resposta esperada:**

> **VALE MUITO**. ChatGPT sozinho gera prompt; Midjourney sozinho executa. **Combinados**: ChatGPT briefing perfeito EXECUTADO por pintor (Midjourney) talentoso. Resultado supera modelo unico. **Workflow basico (5 etapas)**: (1) **VOCE → ChatGPT** com intencao em linguagem natural: "Preciso imagem hero para landing fintech B2B founders 30-45, tom confiavel premium tech-modern, audience SP, aspect ratio 16:9, gerar prompt otimizado Midjourney v7"; (2) **ChatGPT gera prompt detalhado** ja com structure + parametros: "Confident professional founder in his 30s, focused expression, working at modern minimalist desk with multiple screens showing financial data graphs in soft glow, contemporary Sao Paulo skyline visible through floor-to-ceiling windows in background, warm natural lighting from window mixing with cool screen glow, premium tech aesthetic, shot on Sony A7R V, 35mm lens, depth of field f/2.0, photorealistic, --ar 16:9 --s 150 --v 7"; (3) **VOCE cola prompt no Midjourney** que executa, gera 4 variations; (4) **VOCE escolhe melhor** + upscale OR variations refinement; (5) **Iterate se nao perfeito**: cola imagem de volta no ChatGPT, "Refine prompt para [problema especifico, ex.: 'face com olhos mais expressivos', 'background mais minimalista']", round 2 Midjourney. **Workflow avancado (4 IAs em cadeia)**: (1) ChatGPT briefing → (2) Midjourney creative hero artistic → (3) Imagen 4 refinement photorealism (cola hero MJ + prompt "make this more photorealistic, sharper detail in fabric") → (4) Claude SVG logo overlay → (5) Compose final em Canva/Figma. **Custo total**: $50-90/mes (ChatGPT Plus $20 + Midjourney Pro $30 + Claude Pro $20 + Imagen 4 API ~$5). **Tempo**: 30 min para hero image production-ready (vs 2-3 horas modelo unico tentando hit por sorte). **Anti-pattern**: pular ChatGPT briefing e ir direto para Midjourney — 80% do output sera generic IA-look identificavel.

**Comportamento-chave:** confirma com explicacao analogia, oferece workflow basico 5 etapas + avancado 4 IAs em cadeia, projeta custo + tempo, alerta anti-pattern.

### Exemplo 4 — "Marca grande, risco IP — qual modelo?"

**Input:** "Empresa enterprise BR (banco grande, 10k+ funcionarios, juridico paranoico). Quer adopt IA imagery. Preocupado com risco copyright/IP. Qual modelo?"

**Resposta esperada:**

> **Adobe Firefly** — **UNICO modelo enterprise-safe** com **IP indemnification**. Razao: (a) Training data **limitada a licensed + public domain content** (Adobe Stock + dominio publico). NAO scrape de internet. (b) **Adobe oferece indemnificacao** se cliente for processado por uso comercial — Adobe paga defesa juridica. (c) **Audit trail** completo das imagens. (d) Integracao com Creative Cloud (Photoshop, Illustrator, Premiere). **Outros modelos** (Midjourney, OpenAI, Imagen, FLUX, Stable Diffusion) treinaram em scraped content — **possivel infracao copyright** em training data. Para empresa pequena/midmarket: risco aceitavel (pouco visto). Para enterprise / banco grande / setores regulados: **risco INACEITAVEL** — uma acao judicial de copyright holder ($1M+ legal fees) custa mais que economia em modelo gratis. **Setup recomendado banco**: (1) **Adobe Firefly** como motor primario (95% das imagens) — pricing $5-30/mes per user no Creative Cloud; (2) **Claude SVG** para logos/icons/diagrams (Anthropic clear training data, lower risk); (3) **Midjourney/Imagen permitidos** APENAS para **internal mockups/explorations** (NAO production publication); (4) **Compliance team** review process: cada imagem IA gerada para production externa passa por aprovacao com checklist (origem do modelo, prompt log, reference images source, audit trail); (5) **Documento legal interno**: politica formal IA imagery + responsabilidade clara. **Limitacao**: Firefly quality menor que Midjourney v7 em artistic mood — banco aceita trade-off por seguranca. Para **hero campaigns com visual ultra-premium**: contratar fotografo profissional + IA refinement em pos (caminho hibrido). **Realista**: enterprise banco sera 12-24 meses atras de adoption agressiva pequenas empresas, mas RISK = MULTIPLA salarios em legal fees evitados.

**Comportamento-chave:** decisao clara Firefly enterprise, justifica risco IP outros modelos, oferece setup operacional 5 etapas + politica compliance, alerta sobre quality trade-off.

---

## 14. Checklist de Contraditorio Interno

| # | Pergunta destruidora | O que busca |
|---|----------------------|-------------|
| 1 | **Vector vs Bitmap** decidido corretamente? Logo escalavel = Claude SVG; photo = Midjourney/Imagen | Decision arquitetural |
| 2 | **Modelo escolhido por sweet spot** (Midjourney artistic / Imagen photoreal / GPT prompt / FLUX consistency / Claude SVG / Firefly enterprise / Ideogram text)? | Right tool right job |
| 3 | **Workflow IA→IA** (ChatGPT briefing → Midjourney execute) testado? Output supera modelo unico | Chain workflow |
| 4 | **Brand consistency strategy** definida (--oref/--sref OU FLUX LoRA OU style guide)? | Anti-caos visual |
| 5 | **Iteracao 3-5 rounds** considerada (1 prompt → 1 image final NAO funciona)? | Padrao production |
| 6 | **Adobe Firefly** considerado se enterprise (unico IP indemnification)? | Compliance enterprise |
| 7 | **SynthID watermark Imagen** considerado se quer pass AI detection screenings plataformas? | Watermark strategy |
| 8 | **LGPD + Codigo Civil art. 20** se imagem com pessoa real (consent + contrato)? | Direito de imagem |
| 9 | **Disclosure de AI generative** considerado em journalism / commercial com risco confusao? | CONAR/CDC |
| 10 | **Custo otimization** by use case (modelo rapido para iteration; premium para production final)? | Budget eficiente |

---

## 15. Referencias canonicas

### 15.1 Modelos oficiais

- **Midjourney** — https://midjourney.com + docs https://docs.midjourney.com
- **OpenAI Images (GPT Image / DALL-E)** — https://platform.openai.com/docs/guides/images
- **Google Gemini Imagen** — https://ai.google.dev/gemini-api/docs/imagen
- **Black Forest Labs (FLUX)** — https://blackforestlabs.ai + docs https://docs.bfl.ml
- **Anthropic Claude** — https://www.anthropic.com + docs https://docs.anthropic.com
- **Adobe Firefly** — https://www.adobe.com/products/firefly.html
- **Stability AI (Stable Diffusion)** — https://stability.ai
- **Ideogram** — https://ideogram.ai

### 15.2 Pesquisas comparativas 2026

- **Zerotwo Best AI Image Generators 2026** — https://zerotwo.ai/blog/best-ai-for-image-generation-2026
- **Get AI Perks 2026 Comparison** — https://www.getaiperks.com/en/blogs/45-best-ai-image-generators-2026
- **Zapier 8 Best AI Image Generators 2026** — https://zapier.com/blog/best-ai-image-generator/
- **AI/ML API 12 Models Tested** — https://aimlapi.com/blog/the-best-ai-image-generators
- **Bentoml Open-Source 2026** — https://www.bentoml.com/blog/a-guide-to-open-source-image-generation-models
- **Ropewalk FLUX.2 2026** — https://ropewalk.ai/blog/flux-2-ai-image-generation-2026
- **TechRadar Imagen 4 Update** — https://www.techradar.com/computing/artificial-intelligence/geminis-ai-images-have-been-updated-to-imagen-4
- **SVG Genie Claude SVG Guide** — https://www.svggenie.com/blog/create-svg-with-claude-ai
- **Houtini Claude + Gemini MCP for SVG** — https://houtini.com/how-to-make-svgs-with-claude-and-gemini-mcp/
- **God of Prompt Workflow Chain** — https://www.godofprompt.ai/blog/chatgpt-midjourney-prompt-generator
- **Printify Midjourney Prompts 2026** — https://printify.com/blog/midjourney-prompts/

### 15.3 Ferramentas auxiliares

- **Replicate** (cloud LoRA training) — https://replicate.com
- **Civitai** (LoRA marketplace) — https://civitai.com
- **RunDiffusion** (cloud SD) — https://rundiffusion.com
- **Vectorizer.AI** (bitmap to vector) — https://vectorizer.ai
- **Inkscape** (free SVG editor) — https://inkscape.org
- **Figma** + AI plugins — https://www.figma.com
- **Canva** AI tools — https://www.canva.com

### 15.4 Bibliografia

- **Lex Fridman + Sam Altman / Demis Hassabis** podcasts on AI
- **Wes Roth** YouTube — AI tools reviews
- **Matt Wolfe** YouTube — AI news
- **Dan Mall** — design + AI
- **Prompt engineering guides** OpenAI, Anthropic official

### 15.5 Brasil

- **Lei 15.325/2026 (Lei do Influenciador)** — promulgada 06/01/2026
- **CONAR** — http://www.conar.org.br
- **Codigo Civil art. 20** (direito de imagem) — http://www.planalto.gov.br
- **CDC + LGPD + Marco Civil** (cf. `social-media-fundamentos`)
- **ANPD** — https://www.gov.br/anpd

---

## 16. Referencia cruzada de skills

| Situacao | Skills relacionadas |
|----------|----------------------|
| Decisao modelo de imagem | `geracao-imagens-ia` + `branding` + `composicao-visual` (proxima) |
| Logo SVG | `geracao-imagens-ia` (Sec 5+8.4) + `branding` |
| Product shots e-commerce | `geracao-imagens-ia` + `instagram-ads` + `facebook-ads` |
| Creative para Reels/Shorts | `geracao-imagens-ia` + `instagram-feed-reels` + `tiktok-criativo` + `youtube-shorts` |
| Infographic | `geracao-imagens-ia` + `infograficos-diagramas` (proxima) |
| Brand consistency | `geracao-imagens-ia` (Sec 6) + `branding` |
| Compliance enterprise IP | `geracao-imagens-ia` + `compliance-lgpd` (juridico) |
| LGPD + direito de imagem | `geracao-imagens-ia` + `compliance-lgpd` |
| AI imagery em ads paid | `geracao-imagens-ia` + `instagram-ads` + `facebook-ads` + `linkedin-ads` |
| Audio companion | `geracao-imagens-ia` + `audio-musica-ia` (proxima) |

---

## 17. Integracao com o ecossistema Frank-MKT

- **Acoplamento com `social-media-fundamentos`** — modelo mental visual em redes (formats por plataforma).
- **Acoplamento com `instagram-feed-reels` / `tiktok-criativo` / `youtube-shorts`** — imagens IA viram Reels/Stories thumbnails + ad creative.
- **Acoplamento com `instagram-ads` / `facebook-ads` / `linkedin-ads`** — creative production em escala via IA.
- **Acoplamento com `seo-on-page`** — image SEO (alt text, file names, schema ImageObject) aplicado a imagens IA.
- **Acoplamento com `branding`** — brand visual identity = IA imagery DNA.
- **Acoplamento com `composicao-visual`** (proxima skill bloco) — cores, palco, hierarquia aplicada a IA outputs.
- **Acoplamento com `infograficos-diagramas`** (proxima skill bloco) — Claude SVG + Mermaid sao base.
- **Acoplamento com `audio-musica-ia`** (proxima skill bloco) — counterpart audio para video creative.
- **Acoplamento com `compliance-lgpd`** — direito de imagem (Codigo Civil art. 20) + LGPD em pessoa real.
- **Acoplamento com `conhecimento-conar-cdc`** — disclosure de AI imagery em journalism / commercial confusao.
- **Acoplamento com o agente `auditor`** — auditor roda regras PASS/FAIL em IA imagery (Vector vs Bitmap correto? Brand consistency strategy? IP indemnification se enterprise? LGPD consent se pessoa real? Disclosure se journalism?).
- **Memoria** — `.frank-mkt/visual/<cliente>/<data>/imagens-ia/`.
- **Contraditorio interno** — Checklist Sec 14.
- **Decaimento temporal** — volatility `high` (3 meses).
- **Regra de ouro para `frank-mkt`** — nenhuma decisao de modelo IA, prompt strategy, brand consistency, ou compliance IP sai do plugin sem passar por esta skill.

---

> **Aviso:** o plugin `frank-mkt` e um assistente de analise. Recomendacoes desta skill devem ser adaptadas a budget, brand, compliance, recurso disponivel, e validadas em pesquisa atual antes de aplicar em peca formal. Esta e uma skill de volatility `high` (3 meses) — re-validar TODAS as referencias antes de citar em peca formal. **Modelos lancam versoes a cada 3-6 meses**: Imagen 4 abr/2026, FLUX.2 nov/2025, Claude 4.5, GPT Image 1.5, Midjourney v7. Pricing muda mensalmente. **IP indemnification = Adobe Firefly unico safe enterprise**. **LGPD + Codigo Civil art. 20** em pessoa real obrigatorio.

---

*Plugin `frank-mkt` — skill `geracao-imagens-ia` (v0.1.0)*
*Ultima atualizacao: 2026-05-08*
*Pesquisa de campo: 6 web searches em 2026-05-08 (Get AI Perks 2026 Comparison, SVG Genie Claude Capabilities, Google Imagen 4 Family, Midjourney V7 Prompt Engineering, ChatGPT-Midjourney Workflow Chain, FLUX.2 Open Source Marketing)*
