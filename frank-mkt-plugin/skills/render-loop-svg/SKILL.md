---
name: render-loop-svg
description: Operacionalizacao de feedback visual real para geracao de SVG/HTML por LLM — Write SVG -> Bash headless browser -> Read PNG multimodal -> Edit corrige. Resolve o problema de output cego: LLM gera SVG denso, declara sucesso, mas nunca viu o resultado. Cobre commands cross-platform (Edge headless Windows/macOS/Linux + Playwright + Puppeteer + Resvg-js + Inkscape CLI + ImageMagick), pitfalls (race conditions, file:// URL, viewBox vs window-size, font fallbacks), criterios de avaliacao visual 8-dimensoes, stop conditions iterativas, fallback chain quando tooling ausente, custo de tokens por iteracao. Skill complementar a svg-engineering-ia (que cobre markup tecnico). Agente operacional: renderer-visual.
volatility: medium
last_review: 2026-05-11
next_review: 2026-11-11
languages: [pt-BR]
audience: [llm-engineers, claude-power-users, designers, devs-frontend, plugin-developers, ai-engineers]
ascii_only: true
regrounding_sources:
  - https://developer.chrome.com/docs/chromium/new-headless
  - https://playwright.dev/docs/api/class-page
  - https://github.com/yisibl/resvg-js
  - https://inkscape.org/doc/inkscape-man.html
  - https://docs.anthropic.com/en/docs/claude-code/sub-agents
---

# Skill: render-loop-svg

## Decaimento Temporal

**Volatility: MEDIUM (6 meses).**

**Justificativa do decaimento moderado:**

Render-loop e tecnica operacional baseada em ferramentas com ciclo de evolucao moderado:

- **Headless browsers (Chrome/Edge):** API headless mode estabilizou em 2023 com flag `--headless=new` (Chrome 109+). Mudancas em 2026 sao incrementais (suporte WebGPU em headless, perf tuning), nao breaking. Re-validar 6m para captar novas flags.
- **Multimodal Read (Claude tool):** capability core do Claude Code desde 2024. Limites de tamanho/resolucao podem mudar — re-validar 6m.
- **Playwright / Puppeteer:** releases mensais mas API estavel. Major bumps trazem novidades opcionais, nao breaks.
- **Resvg-js:** Rust-based, releases trimestrais. Cobertura SVG cresce gradual.
- **OS environments:** Edge pre-instalado em Windows 11 desde 2021. macOS via DMG. Linux apt/dnf — caminhos podem mudar entre distros.

**Implicacoes praticas:**
- Esta skill deve ser revisada a cada 6 meses (next_review: 2026-11-11).
- Commands testados em Windows 11 + Edge (versao May 2026). Validar em macOS Sonoma+ + Linux Ubuntu 24.04 + a cada major OS release.
- Se Claude Code mudar interface de tool Read (limites de imagem, formatos suportados), re-validar imediatamente.

**Quando esta SKILL precisar de revisao acelerada (antes de 6 meses):**

1. Anthropic publica nova spec de multimodal Read (suporte video, audio, PDF, novos limites).
2. Chrome/Edge depreciam `--headless=new` ou introduzem novo modo headless.
3. Surge ferramenta dominante de feedback visual integrada ao Claude Code (Code Interpreter style).
4. Mudanca em politica de execucao de Bash em agentes Claude Code (sandbox, permissions).
5. Pesquisa academica publica benchmark de render-loop que muda recomendacoes.

---

## Visao Geral

`render-loop-svg` operacionaliza o **feedback visual real** para LLMs que geram SVG/HTML. Resolve um problema documentado em sessao de teste 2026-05-11 (`docs_mkt/aprendizado_infografico.md`): LLM gera SVG denso, declara sucesso, mas **nunca viu o resultado**. Output cego.

A skill `svg-engineering-ia` previa render-loop como tecnica conceitual (Fundacao 6: Auto-Validacao IA Sem Visao + linhas 530-543 do SKILL.md), mas nao operacionalizava. Esta skill complementar fornece **o COMO operacional**: commands prontos por OS, criterios de avaliacao, stop conditions, fallback chain.

### O problema concreto

LLMs sao **multimodais na entrada** (Claude Read tool pode ler imagens) mas **text-only na saida** (geram codigo SVG, nao pixels diretos). Sem mecanismo explicito de loop, o LLM:

1. Gera SVG complexo (>200 linhas, ilustracoes, formulas, infograficos)
2. Tenta "ver mentalmente" via calculo de bounding boxes — limitado
3. Declara sucesso baseado em heuristicas internas
4. Entrega ao usuario
5. Usuario abre e ve gaps obvios (mao virou silhueta, formula ilegivel, densidade 70% em vez de 95%)

**Custo real medido (poster Gestuum, 2026-05-11):**
- V1 sem render-loop: ~40% paridade visual com referencia (Imagen Gemini)
- V2 com render-loop: ~85% paridade visual

Diferenca de **+45 pontos** veio do loop, nao de prompt melhor.

### A arquitetura do loop

```
┌─────────────────────────────────────────────────────────────┐
│                    RENDER-LOOP SVG/HTML                      │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  [1] LLM gera arquivo:                                       │
│      Write tool -> arquivo.svg / arquivo.html                │
│                                                              │
│  [2] LLM renderiza via headless browser:                    │
│      Bash/PowerShell -> msedge --headless --screenshot       │
│                                                              │
│  [3] Browser produz PNG do arquivo:                          │
│      filesystem -> arquivo.png                                │
│                                                              │
│  [4] LLM le PNG com tool multimodal:                         │
│      Read(arquivo.png) -> imagem entra no contexto           │
│                                                              │
│  [5] LLM AVALIA visualmente o output                         │
│      (modelo e multimodal na entrada)                       │
│                                                              │
│  [6] LLM edita SVG (Edit tool) e volta para [2]             │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### Quando esta skill se aciona

- SVG > 200 linhas (densidade ou complexidade visual)
- Ilustracoes (figura humana, objeto 3D, mao, rosto)
- Formulas matematicas com hierarquia (radical, fracao, integral, somatorio)
- Infograficos densos (multiplas zonas, mini-charts, layout multi-coluna)
- Cartazes / posters cientificos
- Logos com sintese visual (nao so wordmark)
- Capas de relatorio com layout complexo
- Quando user fornece **referencia visual** (PNG/URL) para replicar

### Quando NAO acionar

- SVG simples (logo wordmark, 1 forma, 1 cor) — overhead nao compensa
- HTML estatico sem layout dinamico
- Skill auto-suficiente sem visual complexo
- Ambiente sem Bash ou sem headless browser disponivel — usar caminho hibrido (gerar + entregar + pedir human validate)

---

## Fundacao 1 — Headless Browsers 2026 (Edge / Chrome / Playwright / Alternatives)

### Edge headless (recomendado padrao Windows + cross-platform)

**Pre-instalado:**
- Windows 11: `C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe`
- macOS: `/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge`
- Linux: pacote `microsoft-edge-stable` via apt/dnf/yum

**Flags canonicas:**

```powershell
& $edge `
    --headless=new `       # modo moderno (Chrome/Edge 109+)
    --disable-gpu `        # estabilidade em headless
    --no-sandbox `         # CI/CD context (cuidado em prod)
    --window-size=W,H `    # viewport
    --hide-scrollbars `    # remove barras laterais no screenshot
    --screenshot="$out" `  # saida PNG
    "file:///$svg"         # input file (forward slashes)
```

**Por que `--headless=new`:** modo moderno introduzido em 2022 (Chrome 109), promovido a default em 2023. Modo legacy (`--headless` sem `=new`) ainda funciona mas tem **render diferente** para SVG complexos. Sempre usar `=new` para SVG nao-trivial.

### Chrome headless (alternativa Linux + Mac)

Mesmas flags do Edge (compartilham engine Chromium). Caminhos:

- Linux: `google-chrome` ou `chromium-browser` no PATH
- macOS: `/Applications/Google Chrome.app/Contents/MacOS/Google Chrome`
- Windows: `C:\Program Files\Google\Chrome\Application\chrome.exe`

### Playwright (Node) — quando precisar de controle fino

Quando usar:
- SVG com **fontes web custom** (Playwright pode preload via `addStyleTag`)
- SVG com **animacoes** (Playwright espera animations terminarem antes de screenshot)
- SVG complexo com **wait for specific element** (Playwright `waitForSelector`)
- Cross-browser matrix (testar Firefox + WebKit alem de Chromium)

Setup:

```bash
npm init -y
npm i playwright
npx playwright install chromium  # ou firefox / webkit
```

Script minimal:

```javascript
// render.js
const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1024, height: 1536 } });
  await page.goto('file:///D:/path/arquivo.svg');
  await page.screenshot({ path: 'arquivo.png', omitBackground: false });
  await browser.close();
})();
```

Execucao:

```powershell
node render.js
```

### Puppeteer (Node) — similar Playwright

API parecida com Playwright. Historicamente focado em Chrome. Playwright e mantido por ex-time Puppeteer (saiu da Google para Microsoft) e adicionou cross-browser. Em 2026, **Playwright e preferido** salvo legacy.

### Resvg-js (Rust + Node wrapper)

Quando usar:
- SVG **puro** (sem HTML+CSS externo, sem fontes web)
- Quer fidelidade vetor-determinstica (Chromium pode renderizar inconsistente filters aninhados)
- Performance critica (Resvg e ~10x mais rapido que Chromium para SVG puro)
- CI/CD sem precisar de Chromium instalado

Setup:

```bash
npm i @resvg/resvg-js
```

Script:

```javascript
const { Resvg } = require('@resvg/resvg-js');
const fs = require('fs');
const svg = fs.readFileSync('arquivo.svg', 'utf8');
const resvg = new Resvg(svg, { fitTo: { mode: 'width', value: 1024 } });
const png = resvg.render().asPng();
fs.writeFileSync('arquivo.png', png);
```

Limitacoes: nao executa CSS animations, nao executa JavaScript, suporte parcial para `<foreignObject>`.

### Inkscape CLI

Quando usar:
- Fidelidade vetor maxima (Inkscape e referencia em SVG)
- Conversao SVG -> PDF / EPS / outros formatos
- Print pre-press

Setup: instalar Inkscape (https://inkscape.org/release/).

Comando:

```bash
inkscape arquivo.svg --export-type=png --export-filename=arquivo.png --export-width=1024
```

Limitacoes: nao renderiza HTML+CSS externo, mais lento que Chromium.

### ImageMagick (`convert`)

**Nao recomendado** para SVG complexo. Cobertura SVG fraca historicamente. Usar como ultimo recurso.

### Tabela comparativa 2026

| Ferramenta | Install | Fidelidade SVG | HTML+CSS | Animations | Custom fonts | Perf |
|---|---|---|---|---|---|---|
| Edge headless | pre-Win, free Mac/Linux | alta | sim | sim | sim | media |
| Chrome headless | free todos | alta | sim | sim | sim | media |
| Playwright | npm | alta | sim | sim | sim (preload) | media |
| Puppeteer | npm | alta | sim | sim | sim (preload) | media |
| Resvg-js | npm | alta SVG puro | nao | nao | nao | alta |
| Inkscape CLI | DMG/apt | maxima | nao | nao | sim | baixa |
| ImageMagick | apt/brew | baixa | nao | nao | nao | media |

**Recomendacao operacional:**
- **Default**: Edge headless (pre-instalado Windows, equivalente outros OS)
- **CI/CD sem browser**: Resvg-js (Rust binary, rapido)
- **Animations + fontes web**: Playwright
- **Print pre-press**: Inkscape CLI

---

## Fundacao 2 — Comandos Cross-Platform Validados

### Windows 11 + PowerShell + Edge

```powershell
# Variaveis
$svg  = "D:\caminho\arquivo.svg"
$out  = "D:\caminho\arquivo.png"
$edge = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

# Render
& $edge `
    --headless=new `
    --disable-gpu `
    --no-sandbox `
    --window-size=1024,1536 `
    --hide-scrollbars `
    --screenshot="$out" `
    "file:///$($svg.Replace('\','/'))" 2>&1 | Out-Null

# Espera race condition browser fechar vs Read tentar abrir
Start-Sleep -Milliseconds 1200
```

**Notas tecnicas Windows:**
- `--no-sandbox` e necessario em ambientes nao-elevados; remover em prod com user account proprio.
- `file:///` URL com **forward slashes** — daI o `Replace('\','/')`.
- `2>&1 | Out-Null` silencia stderr ruidoso (Edge loga muito em headless).
- `Start-Sleep` 1200ms e empirico — abaixo de 800ms aparece race em discos lentos.

### macOS + bash + Edge

```bash
SVG="/Users/alexa/path/arquivo.svg"
OUT="/Users/alexa/path/arquivo.png"
EDGE="/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge"

"$EDGE" \
  --headless=new \
  --disable-gpu \
  --window-size=1024,1536 \
  --hide-scrollbars \
  --screenshot="$OUT" \
  "file://$SVG"

sleep 1.2
```

**Notas macOS:**
- macOS aceita path absoluto sem `file:///` (basta `file://`).
- Forward slashes nativos.

### Linux + bash + Chrome

```bash
SVG="/home/alexa/path/arquivo.svg"
OUT="/home/alexa/path/arquivo.png"

google-chrome \
  --headless=new \
  --disable-gpu \
  --no-sandbox \
  --window-size=1024,1536 \
  --hide-scrollbars \
  --screenshot="$OUT" \
  "file://$SVG"

sleep 1.2
```

**Notas Linux:**
- `--no-sandbox` quase sempre necessario em container/CI.
- Substituir `google-chrome` por `chromium-browser` em distros sem Chrome instalado.

### Cross-platform Playwright (Node)

```javascript
// render.js — funciona Windows/macOS/Linux com mesma sintaxe
const { chromium } = require('playwright');

(async () => {
  const svgPath = process.argv[2];           // ex: D:/path/arquivo.svg
  const pngPath = process.argv[3];           // ex: D:/path/arquivo.png
  const width  = parseInt(process.argv[4]) || 1024;
  const height = parseInt(process.argv[5]) || 1536;

  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width, height } });
  await page.goto(`file://${svgPath.replace(/\\/g, '/')}`);
  await page.waitForLoadState('networkidle');  // espera fontes carregarem
  await page.screenshot({ path: pngPath, omitBackground: false });
  await browser.close();
  console.log(`Rendered ${svgPath} -> ${pngPath}`);
})().catch(err => {
  console.error(err);
  process.exit(1);
});
```

Execucao:

```bash
node render.js D:/path/arquivo.svg D:/path/arquivo.png 1024 1536
```

### Validacao pos-render

Sempre confirmar PNG foi criado antes de tentar Read:

```powershell
# PowerShell
if (-not (Test-Path $out)) {
  Write-Error "Render falhou — PNG nao foi criado em $out"
  exit 1
}
$size = (Get-Item $out).Length
if ($size -lt 1024) {
  Write-Warning "PNG suspeitosamente pequeno ($size bytes) — render pode ter falhado silenciosamente"
}
```

```bash
# bash
if [ ! -f "$OUT" ]; then
  echo "Render falhou — PNG nao foi criado em $OUT" >&2
  exit 1
fi
size=$(stat -f%z "$OUT" 2>/dev/null || stat -c%s "$OUT")
if [ "$size" -lt 1024 ]; then
  echo "PNG suspeitosamente pequeno ($size bytes) — render pode ter falhado" >&2
fi
```

---

## Fundacao 3 — Workflow Operacional (5 passos com gates)

### Passo 1 — Setup e validacao do input

Entrada esperada:
- `svg_path`: caminho absoluto do SVG
- `output_path` (opcional, default `<svg_path_basename>_render.png`)
- `width` x `height` (default 1024 x 1536 portrait A4-like)
- `reference_png` (opcional)

Validacoes:
- Arquivo SVG existe e e legivel
- Extension e `.svg` ou `.html`
- viewBox declarado se SVG (Glob `viewBox`)
- Output dir tem permissao de escrita

### Passo 2 — Render via headless browser

Selecionar comando apropriado ao OS:
- Windows: PowerShell + Edge
- macOS: bash + Edge
- Linux: bash + Chrome ou Chromium

Aguardar 1.2s pos-comando (race condition).

Verificar PNG foi criado + tem tamanho razoavel (>1KB).

Em falha: tentar fallback chain (Chrome -> Playwright se Node disponivel -> Resvg-js -> Inkscape -> reportar AUSENCIA de tooling).

### Passo 3 — Read multimodal do PNG

Invocar tool Read em `<output_path>.png`. O PNG e injetado no contexto multimodal.

Se `reference_png` foi fornecido, ler tambem — ambos no contexto para comparacao direta.

**Limite pratico**: Read tool aceita imagens ate ~20 MB. PNGs renderizados ficam tipicamente 50KB-2MB. Sem problema em 99% dos casos.

### Passo 4 -- Avaliacao visual sistematica (checklist heuristico)

Aplicar checklist heuristico: **6 dimensoes objetivas + 2 condicionais**:

> NOTA -- Origem do checklist: derivado da sessao de teste 2026-05-11 com poster Gestuum (`docs_mkt/aprendizado_infografico.md`). NAO e framework academico validado em N casos -- e proposta operacional. Replicar em mais casos para validar/refinar.

**6 dimensoes objetivas (sempre aplicaveis):**

#### Dim 1: Alinhamento
- Elementos respeitam grid declarado?
- Margens consistentes entre elementos repetidos?
- Texto alinhado a baseline?
- Verticais e horizontais paralelos onde deveriam?

#### Dim 2: Overlap
- Elementos sobrepostos indevidamente?
- Texto sobre forma escura (legibilidade)?
- Icones colidem com texto?

#### Dim 3: Legibilidade de texto
- Fontes lendaveis no tamanho renderizado?
- Hierarquia clara (h1 > h2 > h3 > body)?
- Espacamento de linha adequado (1.4-1.6 body)?
- Texto pequeno (<10px) ainda lendavel?

#### Dim 4: Contraste de cor
- Texto em fundo com contraste adequado (heuristico, nao audit WCAG formal)?
- Acento de cor visivel sem dominar?
- Paleta declarada respeitada?

#### Dim 5: Hierarquia visual
- Caminho de leitura claro (top->bottom, left->right ou outro padrao estabelecido)?
- Elemento dominante onde deveria estar?
- Ritmo visual mantido (rest + emphasis + rest)?

#### Dim 6: Densidade de informacao
- Area aproveitada vs vazia?
- Default alvo 70-95% (mais baixo: minimal calmo; mais alto: poster denso).
- Vazio respira ou parece bug?

**2 dimensoes condicionais (quando dados disponiveis):**

#### Dim 7: Fidelidade vs referencia (SO se reference_png fornecido)
- Paridade comunicacional: conteudo essencial presente?
- Paridade estetica: aparencia geral compativel?
- Gap especifico: o que mudou?

#### Dim 8: Coerencia interna (SO se SVG ≥ 200 linhas ou multi-elemento)
- Stroke widths consistentes (set inteiro 2px)?
- Paleta respeitada (sem cores fora do brief)?
- Estilo unificado (nao mistura flat com gradient sem proposito)?

Para cada dimensao aplicavel: PASS / WARN / FAIL + observacao especifica.

### Passo 5 — Decisao + reporte

Output estruturado:

```markdown
[RENDER-LOOP — iteracao N]

Renderizado: arquivo.svg -> arquivo_render.png (1024x1536, 0.8s)

Findings por dimensao:
- Alinhamento:  PASS
- Overlap:      WARN — texto "DTW" sobre forma escura na zona 3
- Legibilidade: PASS — todas as fontes lendaveis no zoom 100%
- Contraste:    WARN — coral #EA7E58 sobre paper #FBF6EC = ratio 2.8:1 (abaixo 4.5:1 AA)
- Hierarquia:   PASS
- Densidade:    PASS — 92%
- Fidelidade:   PASS — 85% paridade comunicacional, 80% estetica
- Coerencia:    PASS

Issues criticos:
- (nenhum)

Issues medios:
1. Texto "DTW" sobre forma escura — zona 3 — sugerir clear background
2. Contraste coral/paper abaixo WCAG AA — sugerir escurecer coral OU usar acento em outra cor

Issues cosmeticos:
- (nenhum)

Recomendacao: ITERAR (1 mudanca de markup + 1 ajuste de cor)
Iteracao: 1/5
Convergencia: nao aplicavel ainda (precisa baseline)
```

---

## Fundacao 4 — Stop Conditions e Loop Iterativo

### Stop conditions canonicas

Loop para quando QUALQUER uma:

1. **ACEITAR alcancado**: todos PASS / WARN cosmeticos
2. **Convergencia detectada**: 3 iteracoes consecutivas com mudanca <10% (avaliacao subjetiva do agente)
3. **Cap maximo**: 5 iteracoes totais (custo de tokens significativo apos)
4. **Limitacao tooling**: ambiente nao permite render (sem Edge, sem Node, etc.)
5. **User intervention**: usuario humano pede parar
6. **LOOP CIRCULAR detectado**: fingerprint de issue dominante repetiu (mesmo issue aparece em iter N e tambem em iter K para algum K <= N-2). Indica que agentes nao resolvem via iteracao incremental -- issue exige redesign OU caminho hibrido OU revisor humano. **Operacionalizacao no agente `renderer-visual`** (secao "Fingerprint de iteracao + deteccao A->B->A circular").

### Fingerprint de issue dominante (operacionaliza stop condition #6)

A cada iteracao N, o agente `renderer-visual` gera fingerprint determistico do issue mais critico:

- Formato canonico: `<tipo>+<localizacao>+<elemento>` (snake_case ASCII, sem prefixos auxiliares)
- Tipos validos: `overlap`, `contraste`, `densidade`, `legibilidade`, `paleta`, `alinhamento`, `hierarquia`, `coerencia`
- Exemplos: `overlap+zona3+DTW`, `contraste+coral+paper+ratio<4.5`, `densidade+global+<80%`
- Append em `.frank-mkt/entregaveis/<slug>/render-loop-log.yaml`

Stop condition checa: `fingerprint_N == fingerprint_K para algum K em [1, N-2]`. Janela `[1, N-2]` (nao apenas `N-1`) pega oscilacao 2-ciclo (A em iter par, B em iter impar -- match entre N=3 e N=1). Limitacao conhecida: oscilacao 3-ciclo (A-B-C-A) escapa porque janela termina antes -- improvavel em loops curtos cap=5 mas possivel.

Operacionalizacao executavel (formato fingerprint canonico + caso de borda + schema YAML completo + implementacao no fluxo) e CANONICA no agente `renderer-visual.md`. Esta secao da skill explica APENAS o conceito + integracao com stop condition.

### Quando aceitar antes de convergir

Mesmo sem todos PASS, aceitar pode fazer sentido se:

- Issues remanescentes sao **esteticos subjetivos** (vs objetivos)
- Gap vs referencia ja em **85%+ paridade comunicacional** (valor observado em N=1 — caso Gestuum 2026-05-11; replicar para validar como benchmark generalizavel)
- Iteracao adicional traria custo > beneficio (lei dos retornos decrescentes)
- Issue critico exige redesign (atelier-criativo decide), nao iteracao incremental

### Quando descartar e redesenhar

Reset total quando:

- Issue critico exige **filosofia estetica diferente** (ex: cliente quer hand-drawn warmth; SVG-via-LLM produz geometrico preciso — limite duro)
- Estrutura base esta errada (viewBox, paleta, layout fundamental)
- Apos 5 iteracoes nenhuma dimensao saiu de FAIL — base do SVG nao funciona

Caminho de redesign:
- Voltar ao `atelier-criativo` para nova visao
- Caminho hibrido: gerar ilustracao critica via Imagen/Midjourney (raster) + embutir em SVG via `<image>`

### Custo por iteracao

Cada iteracao consome aproximadamente:

| Item | Custo |
|---|---|
| Bash render | 2-5s wall-clock |
| PNG criado (50KB-2MB) | armazenamento desprezivel |
| Read PNG multimodal | ~3-5k tokens (depende resolucao) |
| Edit SVG | 500-2k tokens (depende mudanca) |
| LLM analise visual | 1-3k tokens output |
| **Total por iteracao** | **~6-10k tokens** |

5 iteracoes = ~30-50k tokens. Para projeto critico, isso e investimento. Para projeto casual, pode ser overhead — usar caminho hibrido (gerar v1 + entregar + pedir human valide).

---

## Fundacao 5 — Pitfalls Operacionais

### Pitfall 1 — Race condition entre browser e Read

Sintoma: Read retorna "file not found" ou PNG corrompido.

Causa: Edge fechou processo mas filesystem ainda nao flush.

Fix: `Start-Sleep -Milliseconds 1200` (PowerShell) ou `sleep 1.2` (bash). Em disco lento (HDD vs SSD), aumentar para 2s.

### Pitfall 2 — file:// URL com backslashes (Windows)

Sintoma: Edge abre janela mas screenshot fica vazio ou retorna erro 404.

Causa: `file:///D:\path\arquivo.svg` nao e URL valida; precisa forward slashes.

Fix: `$svg.Replace('\','/')` em PowerShell. Comando final: `"file:///$($svg.Replace('\','/'))"`.

### Pitfall 3 — viewBox vs window-size mismatch

Sintoma: SVG aparece minusculo no centro ou cortado nas bordas.

Causa: SVG `viewBox="0 0 800 600"` mas `--window-size=1024,1536` — proporcoes nao batem.

Fix:
- Opcao A: SVG ter `viewBox` proporcional ao window-size desejado
- Opcao B: SVG ter `preserveAspectRatio="xMidYMid meet"` (centra + escala para fit)
- Opcao C: window-size matching viewBox (ex: viewBox 800x600 -> window-size 1600,1200 para 2x)

### Pitfall 4 — Font fallbacks silenciosos

Sintoma: Texto renderizado com metricas diferentes do esperado (overflow, hierarquia quebrada).

Causa: SVG declara `font-family="Inter"` mas Inter nao esta instalada no sistema headless. Browser cai em fallback (Arial, sans-serif default).

Fix:
- Opcao A: Usar `<defs><style>@font-face { src: url('https://...'); }</style></defs>` (Playwright esperar carregar via `waitForLoadState('networkidle')`)
- Opcao B: Usar fontes pre-instaladas no SO target (Arial, Helvetica, Times, Courier)
- Opcao C: Embedar fonte base64 inline no SVG

Reportar quando suspeitar fallback (texto mais largo/estreito que esperado).

### Pitfall 5 — Background transparente vs branco

Sintoma: PNG sai com fundo preto ou transparente quando voce queria branco.

Causa: SVG sem `<rect fill="white">` background explicito.

Fix:
- Opcao A: Adicionar `<rect width="100%" height="100%" fill="white"/>` como primeiro elemento dentro do `<svg>`
- Opcao B: Playwright `screenshot({ omitBackground: false })` (default) — preserva default branco
- Opcao C: Para PNG transparente, declarar explicitamente + usar `omitBackground: true`

### Pitfall 6 — Filters SVG aninhados (turbulence + displacementMap + blur)

Sintoma: Renders inconsistente entre Edge headless, Chrome headless e Resvg-js.

Causa: Chromium e Resvg implementam filters levemente diferente. Filters aninhados acentuam divergencia.

Fix:
- Validar em ambos renderers se filters sao criticos
- Simplificar filters (1-2 max) ou usar caminho hibrido (PNG raster pronto + embutir)
- Aceitar diferenca como limitacao

### Pitfall 7 — Permissions / sandbox no CI/CD

Sintoma: `Operation not permitted` ou `Failed to launch chrome` em pipeline.

Causa: container sem permissoes de sandbox (default Chromium).

Fix: `--no-sandbox` flag (ja incluso nos templates acima). Em prod com user account proprio, remover.

### Pitfall 8 — Edge versao incompativel com `--headless=new`

Sintoma: Flag ignorada, comportamento de headless legacy.

Causa: Edge versao < 109 (raro em 2026).

Fix: Atualizar Edge OU usar Chrome OU usar Playwright (auto-gerencia browser).

---

## Fundacao 6 — Avaliacao Visual Avancada (alem do checklist basico)

### Comparacao lado-a-lado com referencia

Quando user fornece `reference_png`, ler ambos PNGs no contexto. Comparar:

1. **Layout macro** — zonas equivalentes? Proporcoes batendo?
2. **Hierarquia tipografica** — escala modular reconhecivel?
3. **Paleta** — cores extraidas batem? (Sim, voce pode ler hex codes visiveis em swatches)
4. **Densidade comparativa** — proxima ou distante?
5. **Elementos especificos** — ex: "mao com 5 dedos" presente em ambos?

Reportar **paridade quantificada**:
- Paridade comunicacional: X% (conteudo essencial coberto)
- Paridade estetica: Y% (aparencia geral compativel)

Observado em N=1 caso documentado (Gestuum, 2026-05-11): SVG-via-LLM atingiu ~85% paridade estetica vs Imagen-via-diffusion. **NAO e teto universal validado** — e amostra unica. Acima disso pode exigir caminho hibrido. Replicar em mais casos antes de tratar como benchmark.

### Heuristicas de qualidade alem do checklist

- **Anti-AI-slop check** — SVG renderizado tem gradientes neon genericos? Sem-serif arredondada padrao Material? Simetria perfeita calma? Reportar como WARN.
- **Brasileiridade** — se cliente pediu Brasil tropical, paleta + tipografia + forma evocam isso ou e gringo cego?
- **Originalidade** — output e pastiche obvio de Vignelli/Tarsila ou tem voz propria?
- **Coerencia narrativa** — partes do SVG contam historia coerente ou e colage?

Essas heuristicas pertencem mais ao `atelier-criativo`, mas voce pode reportar observacoes para alimentar iteracao.

### Mensuracao de mudanca entre iteracoes

Para detectar convergencia, comparar iteracao N com N-1:

- Findings novos vs mantidos vs resolvidos
- % de PASS aumentou ou estagnou?
- Densidade subiu, manteve ou caiu?
- Issue critico foi resolvido ou ainda presente?

Se 3 iteracoes consecutivas trazem mudanca <10% no checklist, convergencia. Parar.

---

## Fundacao 7 -- Fallback Chain Quando Tooling Falta

Esta secao explica **PORQUE** cada ferramenta + ordem racional. A **operacionalizacao executavel** (script bash + PowerShell prontos para copy-paste) e CANONICA em `agents/renderer-visual.md` secao "Fallback chain executavel" (v2.38.1 simplificou para 3 niveis automatic + 2 manuais). Use esta secao para entender taxonomia + escolha consciente; use o agente para execucao.

### Hierarquia de fallback (3 niveis automatic + 2 manuais em v2.38.1)

**Nivel 1: Chromium-family** (cobre 95% dos casos)

1. **Edge headless** (default Windows): pre-instalado em Windows 11 desde 2021; binario tambem disponivel macOS/Linux. Mesma engine Chromium do Chrome, mas distribuicao corporativa em ambientes com policy MS.
2. **Chrome headless**: engine identica ao Edge. Caminhos `/Applications/Google Chrome.app/...` macOS, `google-chrome` Linux apt, `C:\Program Files\Google\Chrome\...` Windows.
3. **Chromium**: Linux distros sem Chrome (Debian/Ubuntu pacote `chromium-browser`). Todos 3 testados no mesmo bloco do script bash/PS porque sao engine-equivalente.

**Nivel 2: Playwright** (Node disponivel + casos especificos)

4. **Playwright** (Node): quando precisa de fontes web custom (preload via `addStyleTag`), animacoes (espera `networkidle`), wait for specific element. `npm i playwright; npx playwright install chromium`. Script auto-detecta `node_modules/playwright`.

**Nivel 3: AUSENCIA reportada** + sugestao install + alternativas manuais

5. **AUSENCIA**: nivel 1+2 falharam. Reportar sugestao de install + listar alternativas manuais (abaixo).

**Opcoes manuais (NAO no fallback automatico)**

6. **Resvg-js** (Node, Rust+JS): SVG puro sem CSS animations. ~10x mais rapido que Chromium para SVG puro. Bom para CI/CD sem Chromium instalado. `npm i @resvg/resvg-js`. NAO esta no fallback automatico porque audiencia (Node dev) tipicamente tambem tem Playwright disponivel; cobertura sobreposta.
7. **Inkscape CLI** (DMG/apt install): fidelidade vetor maxima. Bom para print pre-press / PDF / EPS. Nao renderiza HTML+CSS externo. NAO esta no fallback automatico porque caso de uso (print pre-press) e distinto do render-loop tipico (web/social/screen).
8. **Puppeteer** (Node): legacy. Playwright e preferido salvo codigo herdado. NAO no fallback automatico v2.38.1.

### Quando declarar ausencia honesta

Se passos 1-7 falharam, NAO inventar avaliacao. Reportar:

```
[RENDER-LOOP — limitacao ambiental]

Tooling ausente: tentei Edge, Chrome, Playwright, Resvg, Inkscape — nenhum disponivel
neste ambiente. Sem render real, validacao visual e PARCIAL (so heuristica de markup).

Caminhos:
1. Instalar Edge (https://microsoft.com/edge) — recomendado, zero-config Windows
2. Instalar Node + Playwright (`npm i playwright; npx playwright install chromium`)
3. Voce pode renderizar manualmente no browser (abrir arquivo.svg) e enviar screenshot
4. Aceitar SVG como v1 nao-validado visualmente + revisar voce mesmo

Status: SVG entregue mas NAO VALIDADO via render-loop.
```

### Caminho hibrido — gerar via Imagen + embutir

Quando limitacao for **estetica** (hand-drawn warmth, ilustracao organica, rosto humano), nao tooling, considerar caminho hibrido:

1. Gerar ilustracao critica via Imagen/Midjourney/DALL-E (skill `geracao-imagens-ia`) como PNG transparente
2. Embutir no SVG via `<image href="ilustracao.png" x="100" y="200" width="400" height="300"/>`
3. Manter resto do SVG (texto, formas geometricas, grid) vetorial puro
4. Render-loop valida composicao final

Trade-off: perde escalabilidade vetor pura no elemento raster. Ganha qualidade artistica que LLM-text-only nao atinge.

---

## Fundacao 8 — Aplicacao em Content MKT

### Use case 1: Founder pre-Series A precisa pitch deck

Cenario: founder solo, R$ 0 orcamento agencia, precisa investor deck visual.

Fluxo:
1. `atelier-criativo` define visao (cross-pollination + paleta + tipografia)
2. Skill `apresentacoes-decks-corporativos` orquestra estrutura slides
3. Para cada slide com visual complexo: skill `svg-engineering-ia` gera SVG
4. Agente `renderer-visual` + esta skill validam cada slide
5. Loop ate 85%+ paridade
6. Deck exportado PDF via Inkscape

Custo estimado: 5 slides x 3 iteracoes x ~8k tokens = 120k tokens. Vs $5-15k em agencia para deck premium.

### Use case 2: CMO Series C revisa material agencia

Cenario: agencia entregou identidade visual; CMO quer validar antes de aprovar.

Fluxo:
1. Upload SVG da agencia
2. `renderer-visual` renderiza + le multimodal
3. Reporta findings em 8-dimensoes
4. CMO revisa findings + decide aprovar / pedir ajuste

Valor: segunda opiniao objetiva sem custo de outra agencia.

### Use case 3: Equipe interna gerando infografico semanal

Cenario: marketing team gera 5-10 infograficos por semana para LinkedIn/Instagram.

Fluxo:
1. Skill `infograficos-diagramas` define estrutura
2. Skill `svg-engineering-ia` gera markup
3. `renderer-visual` em loop ate aceitar
4. Auto-export PNG para post

Valor: consistencia visual + economia de designer junior para tarefa repetitiva.

### Use case 4: Cientista publica poster academico

Cenario: pesquisador precisa replicar poster cientifico (formula matematica + ilustracao + grid + referencias) em SVG editavel + acessivel.

Fluxo:
1. Referencia PNG (poster anterior ou similar)
2. `atelier-criativo` define layout + paleta
3. Skill `svg-engineering-ia` gera markup com formulas (Cambria Math + tspan dy)
4. `renderer-visual` valida via render-loop ate 85%+ paridade
5. Export SVG + PNG renderizado

Caso real: poster Gestuum (Science Fair 2026) atingiu 85% paridade com Imagen via este workflow.

---

## Anti-Patterns 16

1. **Declarar render OK sem ter executado Bash.** Mesma raiz do output cego que esta skill resolve. NUNCA pular o passo.

2. **Skip Read pos-render.** Render sem Read = LLM gerou PNG mas nao viu. Inutil.

3. **Avaliar sem checklist 8-dimensoes.** "Esta bom" e juizo, nao avaliacao. Sistematizar.

4. **Loop infinito sem cap.** Sempre respeitar 5 iteracoes max.

5. **Ignorar convergencia.** Se 3 iteracoes consecutivas trazem mudanca <10%, parar.

6. **Falsificar render quando tooling falta.** Reportar AUSENCIA, nao inventar.

7. **Comparar com referencia que nao existe.** Se user nao deu reference_png, nao inventar mental.

8. **Confiar render mental.** Calcular bounding box mental NAO substitui pixel real.

9. **Esquecer Start-Sleep / sleep.** Race condition silenciosa = PNG vazio = falso negativo.

10. **viewBox vs window-size mismatch.** Sempre validar proporcoes.

11. **Backslashes em file:// URL Windows.** Forward slashes obrigatorio.

12. **Background transparente quando queria branco.** Adicionar `<rect>` explicito.

13. **Confiar render unico para SVG critico.** Em producao, validar em 2+ renderers (Edge + Resvg) se filters complexos.

14. **Esquecer fallback chain.** Falha em Edge nao significa parar; tentar Chrome -> Playwright -> Resvg -> Inkscape.

15. **Loop quando ja convergiu.** Aceitar 85% paridade se gap remanescente e estetico subjetivo.

16. **Esconder limitacao "hand-drawn warmth".** Caminho hibrido (Imagen + embed) e legitimo. Nao tentar mascarar limite de SVG-via-LLM.

---

## 18 Regras de Ouro

1. **Sempre executar Bash render antes de declarar SVG pronto.** Sem excecao.

2. **Sempre Read PNG pos-render.** Multimodal e o ponto inteiro.

3. **Sempre Start-Sleep 1200ms pos-comando.** Race condition silenciosa quebra tudo.

4. **Sempre forward slashes em file://.** Backslashes nao funcionam.

5. **Sempre validar PNG criado + tamanho >1KB.** Falha silenciosa de render e comum.

6. **Sempre aplicar checklist 8-dimensoes.** Sistematico > juizo vago.

7. **Sempre respeitar cap de 5 iteracoes.** Custo de tokens cresce rapido.

8. **Sempre detectar convergencia (<10% mudanca em 3 iteracoes).** Parar economiza tokens.

9. **Sempre reportar AUSENCIA de tooling honestamente.** Inventar render mental e crime.

10. **Sempre tentar fallback chain antes de desistir.** Edge -> Chrome -> Playwright -> Resvg -> Inkscape.

11. **Sempre quantificar paridade quando referencia fornecida.** "X% comunicacional / Y% estetica".

12. **Sempre alertar font fallback quando suspeitar.** Texto com metricas diferentes = clue.

13. **Sempre considerar caminho hibrido para hand-drawn.** SVG-via-LLM tem teto ~85% estetica.

14. **Sempre `--headless=new`, nunca `--headless` legacy.** Renders diferentes para SVG complexo.

15. **Sempre `--disable-gpu` em headless.** Estabilidade.

16. **Sempre validar viewBox vs window-size.** Mismatch = SVG cortado ou centrado minusculo.

17. **Sempre delegar correcao estetica para atelier-criativo.** Render-loop reporta, agente esteta decide.

18. **Sempre delegar correcao de markup para svg-engineering-ia.** Render-loop reporta, skill markup corrige.

---

## Exemplos comportamentais

### Exemplo 1 — SVG simples passa primeira iteracao

User invoca via agente atelier-criativo:
"Renderize esse logo wordmark + simbolo geometrico"

Acao:
1. Renderizar via Edge headless 800x800
2. Read PNG
3. Avaliar 8 dimensoes
4. Todos PASS — wordmark legivel, simbolo simetrico, paleta respeitada, contraste OK
5. Densidade 60% — adequada para logo (vazio respira)

Output:
```
[RENDER-LOOP iteracao 1/5]
Renderizado: logo.svg -> logo_render.png (800x800)
Findings: 8 dimensoes PASS
Recomendacao: ACEITAR
```

### Exemplo 2 — Poster denso converge em 3 iteracoes

User invoca via comando `/frank-mkt:gerar-infografico`:
"Replicar poster cientifico Gestuum baseado em referencia.png"

Iteracao 1:
- Renderizar v1 (atelier + svg-engineering primeira passada)
- Findings: 5 PASS, 2 WARN (densidade 70%, contraste coral/paper baixo), 1 FAIL (mao virou silhueta)
- Reportar para atelier-criativo + svg-engineering-ia

Iteracao 2:
- Versao corrigida (mao com 5 dedos via path mais elaborado, densidade subiu para 88%)
- Findings: 6 PASS, 2 WARN
- Reportar para nova correcao (contraste coral)

Iteracao 3:
- Coral escurecido para passar 4.5:1 ratio
- Findings: 7 PASS, 1 WARN (densidade 92% mas referencia tinha 95%, gap menor)
- Convergencia detectada (mudanca <10% vs iteracao 2)

Output:
```
[RENDER-LOOP — convergencia detectada em iteracao 3/5]
Paridade vs referencia: 85% comunicacional / 80% estetica
Issues remanescentes: 1 WARN (densidade 92% vs 95% referencia — gap minor)
Recomendacao: ACEITAR (lei retornos decrescentes)
```

### Exemplo 3 — Ambiente sem Edge, fallback Playwright

User invoca em Linux container CI/CD sem browser instalado.

Acao:
1. Tentar `google-chrome` — falha (not installed)
2. Tentar `chromium-browser` — falha
3. Detectar Node + npm disponivel
4. Sugerir install Playwright OU usar Resvg-js se SVG puro

Output:
```
[RENDER-LOOP — fallback ativado]
Edge/Chrome ausentes. Detectei Node 20 disponivel.
Para continuar, executar uma vez:
  npm i playwright
  npx playwright install chromium

Apos instalar, re-invocar render-loop. Alternativa imediata: Resvg-js para SVG puro
sem CSS animations:
  npm i @resvg/resvg-js
```

### Exemplo 4 — SVG com filters complexos diverge entre renderers

User invoca para SVG com turbulence + displacementMap + Gaussian blur aninhado.

Acao:
1. Render via Edge headless — output A
2. User pediu validar em 2 renderers — render tambem via Resvg-js — output B
3. Comparar A vs B no contexto multimodal
4. Detectar: turbulencia visivel em A mas suave em B

Output:
```
[RENDER-LOOP — divergencia entre renderers]
Edge: turbulencia + displacement visiveis (textura grunge)
Resvg: turbulencia suave (filter simplificado pelo engine)

Conclusao: producao para web (Chrome/Edge) = output Edge.
Producao para PDF/print (Resvg ou Inkscape) = output Resvg.
Recomendacao: aceitar variacao OU simplificar filters para consistencia.
```

---

## Checklist de Contraditorio Interno (10 perguntas)

Antes de declarar render-loop completo:

1. Executei Bash render real, ou estou inferindo do markup?
2. Read PNG entrou no contexto multimodal — eu **vi** o resultado?
3. Apliquei checklist 8-dimensoes ou avaliei vago?
4. Race condition (Start-Sleep) foi respeitada?
5. Validei PNG criado + tamanho >1KB?
6. Se referencia fornecida, comparei lado-a-lado explicitamente?
7. Quantifiquei paridade quando aplicavel (X% comunicacional / Y% estetica)?
8. Reportei AUSENCIA de tooling honestamente quando faltou?
9. Respeitei cap de 5 iteracoes / detectei convergencia?
10. Delegacao de correcao foi clara (atelier para estetica, svg-engineering para markup)?

Se qualquer resposta levantar duvida grave, voltar uma etapa.

---

## Referencias canonicas

### Headless browsers
- Chrome new headless mode (Eric Bidelman, 2022): https://developer.chrome.com/docs/chromium/new-headless
- Microsoft Edge command-line flags: https://learn.microsoft.com/en-us/microsoft-edge/web-platform/
- Playwright docs: https://playwright.dev/
- Puppeteer docs: https://pptr.dev/

### Rendering engines alternativos
- Resvg-js (yisibl, Rust+JS): https://github.com/yisibl/resvg-js
- librsvg + rsvg-convert: https://wiki.gnome.org/Projects/LibRsvg
- Inkscape CLI man page: https://inkscape.org/doc/inkscape-man.html

### SVG specification
- W3C SVG 2.0: https://www.w3.org/TR/SVG2/
- MDN SVG reference: https://developer.mozilla.org/en-US/docs/Web/SVG
- SVG.dev community: https://svg.dev/

### Multimodal LLM capability
- Claude tool use docs: https://docs.anthropic.com/en/docs/agents-and-tools/tool-use
- Claude Code sub-agents: https://docs.anthropic.com/en/docs/claude-code/sub-agents
- Anthropic Skills spec: https://www.anthropic.com/news/skills (2025-2026)

### Pesquisa academica relevante (2024-2026)
- VGBench: Vector Graphics Benchmark for LLMs
- SVGenius: SVG generation benchmarks
- Chat2SVG (Stanford 2024)
- LLM4SVG family (multiple papers)

### Brasil 2026 — contexto MKT
- LGPD Marco Civil: artefatos visuais com dados pessoais embutidos
- CONAR Anexo P: disclosure de criacao via IA em publicidade
- Lei 15.325/2026 do Influenciador: AI-generated content disclosure

---

## Referencia cruzada de skills

| Skill | Quando consultar |
|---|---|
| `svg-engineering-ia` | Markup tecnico W3C 2.0 + LLM patterns. Esta skill cobre OPERACAO; aquela cobre MARKUP. |
| `composicao-visual` | Fundamentos Gestalt + hierarquia + grid antes de gerar SVG. |
| `tipografia-corporativa` | Hierarquia tipografica + escala modular + escolha de fonte. |
| `paleta-cores-corporativa` | WCAG contraste + extracao de hex de referencia + dark mode. |
| `iconografia-corporativa` | Sistema de icones inline reutilizaveis no SVG. |
| `infograficos-diagramas` | Mermaid + PlantUML para parte dos mini-charts (alternativa raster). |
| `geracao-imagens-ia` | Caminho hibrido — Imagen para ilustracao hand-drawn + embed em SVG. |
| `acessibilidade-wcag` | Audit formal WCAG 2.2 + LBI Brasil 13.146 (esta skill so heuristica). |
| `logo-design-process` | Processo brand design + variacoes + entregaveis (.svg/.png/.pdf/.eps). |
| `brand-book-methodology` | Manual de identidade + governance + Figma/Frontify/Zeroheight. |
| `manutencao-skills` | Meta-skill — cristal "skills visuais sem feedback visual = output cego" capturado aqui. |

---

## Integracao com o ecossistema Frank-MKT

### Agentes que invocam esta skill

```
atelier-criativo (visao estetica)
       v
[gera SVG via svg-engineering-ia]
       v
renderer-visual (Bash + Read multimodal)  <-- ESTA SKILL E A REFERENCIA TECNICA DESSE AGENTE
       v
[loop iterativo]
       v
[aceitar OU iterar OU descartar]
       v
entrega ao usuario
```

### Commands que usam esta skill

- `/frank-mkt:gerar-infografico` — workflow obrigatorio inclui render-loop

### Cross-pollination com outras skills visuais

Quando voce esta gerando infografico, fluxo tipico:

1. `composicao-visual` (Fundacao 1 — definir grid)
2. `paleta-cores-corporativa` (extrair hex de referencia ou definir)
3. `tipografia-corporativa` (hierarquia)
4. `iconografia-corporativa` (icons inline)
5. `svg-engineering-ia` (markup)
6. **`render-loop-svg`** (validacao operacional — voce esta aqui)
7. `acessibilidade-wcag` (audit final formal)

Disclaimer educational mandatory: Este conteudo e educacional e nao substitui designer senior humano para producao comercial. Render-loop reduz output cego mas nao elimina necessidade de revisao humana. Para projeto com risco/budget alto, sempre acoplar designer humano senior revisando output final. Cross-skill complementar: svg-engineering-ia, composicao-visual, tipografia-corporativa, paleta-cores-corporativa, iconografia-corporativa, geracao-imagens-ia, acessibilidade-wcag, infograficos-diagramas. Agente operacional dedicado: renderer-visual. Comando wrapper: /frank-mkt:gerar-infografico.
