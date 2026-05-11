# Aprendizado · Geração de Infográficos SVG com Render-Loop Visual

> **Audiência deste documento:** outro Claude (provavelmente Opus 4.7) responsável por evoluir o plugin `frank-mkt`. Este texto é um *transfer brief* técnico end-to-end, escrito após uma sessão real de teste onde o Alex (operador humano) pediu para replicar um poster científico complexo (`gestuum_matematica.png`) gerado pelo Gemini como SVG editável, e o resultado evoluiu de "fraco" para "competitivo" depois que um insight arquitetural foi destravado.
>
> **Resultado da sessão em uma frase:** Claude **pode** sim gerar SVG no nível visual de modelos multimodais (Imagen/DALL-E) **desde que** opere com loop de feedback visual via headless browser + leitura multimodal do PNG renderizado, e **desde que** orquestre múltiplas skills do `frank-mkt` (não só `svg-engineering-ia` isolada).
>
> **Objetivo deste documento:** te dar todo o contexto para você criar/atualizar skills, agentes, hooks e processo do plugin de forma que esse fluxo se torne nativo, repetível e descobrível para qualquer invocação futura de Claude trabalhando com geração de infográfico/SVG.

---

## 0. Contexto operacional (estado do sistema antes do teste)

- **Plugin instalado:** `frank-mkt` (ativado no projeto `D:\4nk\teste_mkt`)
- **Skills relevantes já existentes** (do `frank-mkt`):
  - `svg-engineering-ia` — engenharia de SVG via IA, W3C SVG 2.0, técnicas para LLM gerar SVG complexo, render-loop como conceito ("PSS metric + heuristics + render-loop")
  - `composicao-visual` — fundamentos de grid, proporção, hierarquia
  - `tipografia-corporativa` — escala modular, pareamento de famílias
  - `paleta-cores-corporativa` — harmonia perceptual OKLab, contraste WCAG
  - `iconografia-corporativa` — sistema de ícones (Lucide/Heroicons/Phosphor)
  - `infograficos-diagramas` — Mermaid, PlantUML, infografia editorial
  - `geracao-imagens-ia` — prompting para Imagen/Midjourney (caminho raster)
- **Agente disponível:** `frank-mkt:atelier-criativo` — descrito como artista digital com processo (listening + resonance + cross-pollination + tension + synthesis + translation + iteration). Tem acesso a `Read, Write, Edit, Glob, Grep, WebSearch, WebFetch, Agent` — **MAS NÃO TEM BASH**, esse é um ponto crítico que voltaremos.
- **Tools nativas do Claude principal nesta sessão:** Read (multimodal: lê PNG/JPG visualmente), Write, Edit, Bash/PowerShell, Glob, Grep, Agent, WebSearch, WebFetch.
- **Ambiente:** Windows 11, PowerShell 5.1, Edge instalado em `C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe`, Chrome também disponível.

---

## 1. O problema concreto (o que o usuário pediu)

Alex tinha dois posters PNG gerados pelo **Gemini** (provavelmente via Imagen), parte de um projeto de Science Fair chamado **Gestuum** (um wearable que traduz gestos em palavras):

- `gestuum_dispositivo_comunicacao.png` (6.112 KB) — explica os 4 protocolos de comunicação
- `gestuum_matematica.png` (6.779 KB) — explica DTW, distância ponderada, grid 3D, assinatura orbital com 8 features matemáticos, referências acadêmicas

Pedido: **replicar o nível de qualidade do PNG do Gemini, mas em SVG vetorial**.

Premissa explícita do usuário, *literalmente*:
> *"por baixo os 2 são código vetoriais?"*

**Essa premissa está errada e é importante desmontá-la primeiro.** Imagen (modelo de difusão do Google) gera raster pixel-a-pixel via processo de difusão aprendido. Não há código vetorial por baixo. O PNG é a saída final, não um produto secundário. Comparar SVG-gerado-por-LLM com PNG-gerado-por-diffusion é comparar duas tecnologias muito diferentes — uma é geração textual de instruções vetoriais, a outra é amostragem pixel-a-pixel de uma distribuição visual aprendida.

---

## 2. A jornada (V0 → V1 → V2): o que falhou, o que destravou

### V0 — Tentativa direta do Claude principal (sem agente, sem skills explícitas)

Tema: infográfico explicando o ecossistema de plugins do Claude Code. Resultado salvo em `claude-plugins-infografico.svg`. Funcionou estruturalmente mas o Alex disse "ficou mais ou menos". Era um exercício mais simples (texto + tabela + barra), não testava o limite da capacidade SVG.

### V1 — Delegação ao `atelier-criativo` SEM render-loop, sem orquestração de skills

Brief enviado ao agente pedia para usar `svg-engineering-ia`. Resultado: `gestuum_matematica.svg` (28.8 KB).

**Quando renderizei o V1 via Edge headless e LI o PNG com multimodal Read, vi:**
- A "mão" virou silhueta de manga + retângulo wearable — visualmente sumiu como elemento dominante
- Fórmula da distância ponderada ilegível
- Bloco DTW aparentando vazio
- 8 mini-gráficos de Assinatura Orbital eram símbolos abstratos genéricos, não comunicavam o conceito de cada feature
- Densidade muito menor que o original (~70% da área aproveitada vs 95% do Gemini)

**O agente havia entregado declarando sucesso porque nunca viu o resultado.**

### Insight crítico do Alex (turno 7 da conversa)

Alex perguntou:
> *"me devolve screenshot — vc não consegue gerar o pdf e analisar, ou html final?"*

Essa pergunta destravou o caminho. **Eu tinha rejeitado a possibilidade cedo demais.** Reality check:
- Tenho tool **Bash/PowerShell** → posso rodar Edge headless
- Tenho tool **Read** que é **multimodal na entrada** → posso ler PNG e *ver* visualmente
- Logo: posso fechar o loop **gerar SVG → renderizar → ver → corrigir**

Foi o **single biggest unlock** da sessão.

### V2 — Refazer com render-loop validado + brief multi-skill explícito

Brief atualizado ao `atelier-criativo`:
1. Comando exato de render-loop incluído no prompt
2. Lista nominal das skills a invocar: `composicao-visual` + `tipografia-corporativa` + `paleta-cores-corporativa` + `iconografia-corporativa` + `svg-engineering-ia`
3. Construção obrigatoriamente em **8 camadas**, com instrução para renderizar entre elas
4. Critérios visuais específicos por zona (mão com 5 dedos, fórmula com radical/sigma/fração, 8 mini-gráficos comunicativos)
5. Densidade alvo 95%+

Resultado: `gestuum_matematica.svg` reescrito (44.6 KB, 766 linhas). Renderização salva em `_render_v2.png`.

**Quando renderizei o V2 e li o PNG, vi:**
- Mão com 5 dedos individuais, articulações, wearable detalhado com bezel + tela + LED + 3 eixos vetoriais
- Fórmula da distância ponderada com radical horizontal sobre radicando, Σ tipográfico, fração linha-num-den, exponente em superscript — legível
- Bloco DTW preenchido com fórmula de recorrência
- 8 mini-gráficos cada um comunicando seu conceito real: onda senoidal com amplitude marcada, pico destacado em coral, vetores em ângulo + cosseno, plano paralelogramo hachurado + normal, zigzag vs linha suave, arco rotacional, vetor com magnitude+ângulo, gráfico de barras crescente
- Densidade ~95%

**Avaliação honesta V2 vs Gemini original:** ~85% de paridade visual. O gap remanescente é estético-artístico (mão geométrica vs hand-drawn warmth, ausência de sombras suaves, cubo 3D flat vs sombreado), não capacitivo.

### A limitação que descobri no agente

O `atelier-criativo` no relatório final do V2 admitiu: *"sem Bash tool no meu contexto não pude gerar `_render_v2.png` nem fazer render-loop visual real para validar o output"*. Ou seja, **a frontmatter do agente lista `Read, Write, Edit, Glob, Grep, Agent, WebSearch, WebFetch` mas NÃO `Bash`**. Ele iterou apenas mentalmente (cálculos absolutos de bounding boxes). Quem fechou o loop foi o Claude principal (eu, que tenho Bash).

Essa é uma **observação importante para você (próximo Claude) atualizar a definição do agente.**

---

## 3. Arquitetura técnica do render-loop

### 3.1. Componentes

```
┌─────────────────────────────────────────────────────────────┐
│                    RENDER-LOOP SVG/HTML                      │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  [1] Claude gera arquivo:                                    │
│      Write tool → arquivo.svg / arquivo.html                │
│                                                              │
│  [2] Claude renderiza via headless browser:                  │
│      Bash/PowerShell → msedge --headless --screenshot       │
│                                                              │
│  [3] Browser produz PNG do arquivo:                          │
│      filesystem → arquivo.png                                │
│                                                              │
│  [4] Claude lê PNG com tool multimodal:                      │
│      Read(arquivo.png) → imagem é injetada no contexto      │
│                                                              │
│  [5] Claude AVALIA visualmente o output                      │
│      (model é multimodal na entrada)                        │
│                                                              │
│  [6] Claude edita SVG (Edit tool) e volta para [2]          │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### 3.2. Comando concreto que funciona (validado em Windows 11 + Edge)

```powershell
$svg  = "D:\caminho\arquivo.svg"
$out  = "D:\caminho\arquivo.png"
$edge = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

& $edge `
    --headless=new `
    --disable-gpu `
    --no-sandbox `
    --window-size=1024,1536 `
    --hide-scrollbars `
    --screenshot="$out" `
    "file:///$($svg.Replace('\','/'))" 2>&1 | Out-Null

Start-Sleep -Milliseconds 1200  # crítico: dar tempo do Chromium fechar arquivo
```

**Notas técnicas:**
- `--headless=new` é o modo headless moderno do Chromium (Chrome 109+, Edge 109+). `--headless` legacy também funciona mas tem diferenças de rendering.
- `--window-size` define o viewport. O SVG deve ter `viewBox="0 0 LARG ALT"` matching, ou usar `preserveAspectRatio`.
- `file:///` URL precisa de barras forward, daí o `.Replace('\','/')`.
- O `Start-Sleep` evita race condition entre o browser fechar e o Read tentar abrir o PNG.

### 3.3. Alternativas testáveis

| Ferramenta | Disponível Windows 11 padrão | Vantagens | Desvantagens |
|---|---|---|---|
| **Edge headless** | ✅ Sim, vem com OS | Zero install | Bug ocasional em SVGs muito complexos |
| **Chrome headless** | ✅ Sim, se instalado | Idêntico ao Edge | Idem |
| **Playwright** (Node) | ❌ Requer `npm i playwright` | API completa, fontes embedáveis | Setup pesado |
| **Puppeteer** (Node) | ❌ Requer `npm i puppeteer` | Idem | Idem |
| **Inkscape CLI** | ❌ Requer install | Fidelidade vetor-puro | Não renderiza HTML+CSS |
| **rsvg-convert** | ❌ Requer install | Rápido, leve | Cobertura SVG limitada |
| **ImageMagick** | ❌ Requer install | Multi-formato | Rasterização SVG fraca |

**Recomendação:** padronizar em **Edge headless** porque vem pré-instalado em Windows (e tem caminho equivalente em macOS via `/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge` e Linux via `microsoft-edge`).

### 3.4. Variação Linux/macOS

```bash
# macOS
"/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge" \
  --headless=new --disable-gpu --window-size=1024,1536 \
  --screenshot="/tmp/out.png" "file:///path/to/arquivo.svg"

# Linux (chrome instalado via apt)
google-chrome --headless=new --disable-gpu --window-size=1024,1536 \
  --screenshot="/tmp/out.png" "file:///path/to/arquivo.svg"
```

---

## 4. Skills do `frank-mkt` que foram usadas (e como)

### 4.1. `svg-engineering-ia` — núcleo técnico
**Como invoquei:** brief explícito ao `atelier-criativo` mencionando a skill nominalmente. O agente já tinha a skill carregada via plugin.
**O que entregou:** estrutura SVG válida W3C 2.0, uso correto de `<defs>` + `<symbol>` + `<marker>`, CSS embutido via `<style><![CDATA[...]]></style>`, escape correto de caracteres especiais.
**Gap:** a própria skill menciona "auto-validacao IA sem visao (PSS metric + heuristics + render-loop)" — ou seja, ELA JÁ PREVIA o render-loop como técnica, mas não estava operacionalizada. O agente tentou substituir por "render-loop mental".

### 4.2. `composicao-visual`
**Aplicação V2:** definição de grid de 7 zonas verticais com pesos diferentes, ritmo de margens, hierarquia espacial (header 12% / zonas centrais 75% / footer 13%).

### 4.3. `tipografia-corporativa`
**Aplicação V2:** escala modular implícita (118px título → 30px h1 → 18px h2 → 14px h3 → 13px body → 11px small → 9.5px micro), pareamento de 3 famílias (Inter sans display + Cambria Math fórmulas + JetBrains Mono código).

### 4.4. `paleta-cores-corporativa`
**Aplicação V2:** extração da paleta exata do PNG referência (#173A5C navy + #EA7E58 coral + #04404A teal + #B5C5E8 light-blue + #D2A2CA mauve + #FBF6EC paper) e distribuição 60/30/10 entre tinta dominante / acento / detalhe.

### 4.5. `iconografia-corporativa`
**Aplicação V2:** ao invés de desenhar ícones do zero, o agente usou paths inline estilo Lucide para setas, marcadores de eixo, ícones de seção. Reduziu erro de coordenada significativo.

### 4.6. `infograficos-diagramas` (NÃO foi usada, deveria ter sido)
**Aplicação que faltou:** essa skill cobre Mermaid + PlantUML + builders. Para os 8 mini-gráficos da Assinatura Orbital, parte deles poderia ter sido construída via Mermaid e embutida — economizando tempo e dando consistência visual.

### 4.7. `geracao-imagens-ia` (caminho alternativo não tomado)
**Quando usar:** se o gap "hand-drawn warmth" for crítico, essa skill ajuda a montar prompt para Imagen/Midjourney gerar APENAS a ilustração da mão como PNG transparente, e embutir no SVG via `<image>`. **Caminho híbrido** que combina o melhor dos dois mundos.

---

## 5. Padrões que funcionaram

### 5.1. Brief de agente com **render-loop embutido**

O turning-point foi adicionar literalmente no prompt do agente:

> *"NOVA REGRA OPERACIONAL — você TEM acesso a render-loop visual: \[comando PowerShell\]. Depois do comando, espere 1 segundo, leia o PNG com a tool Read (você é multimodal, vai VER o resultado)."*

Mesmo que o agente atual não tenha Bash, isso instrui o Claude principal a fechar o loop por ele.

### 5.2. Construção em camadas com pontos de validação

Em vez de "escreva tudo de uma vez", o brief listou 8 camadas e sugeriu render entre elas. Isso permite identificar erros cedo (camada 2 quebrada não contamina camada 6).

### 5.3. Critérios visuais ESPECÍFICOS, não genéricos

V1 brief disse "ilustração da mão estilizada/simplificada — silhueta + setas". V2 brief disse "path SVG mais elaborado com 5-8 segmentos curve, dedos individuais, articulações marcadas, manga separada". A diferença de granularidade do brief mudou drasticamente o output.

### 5.4. Mostrar o erro renderizado ao agente

V2 brief incluiu: *"Veja `_render_v1.png` — abra e veja com seus próprios olhos antes de começar"*. Agente que vê o próprio erro anterior corrige melhor.

### 5.5. Paleta extraída por hex code do PNG referência

O agente notou no PNG original que havia color swatches visíveis com hex codes impressos no canto. Extraiu fielmente. **Patterns para skills:** sempre que o referência tiver paleta visível, extrair e citar hex codes literalmente no SVG.

---

## 6. Padrões que falharam

### 6.1. Confiar que "agente tem skill X carregada" basta

Não basta. **Tem que invocar a skill nominalmente no brief.** A presença passiva da skill no contexto do agente não garante uso ativo.

### 6.2. Esperar que o agente saiba que pode renderizar

Mesmo se o agente tivesse Bash, ele não tentaria render-loop espontaneamente. Tem que estar no brief.

### 6.3. Submeter SVG sem ter visto

Em todo arquivo SVG complexo (>200 linhas), há ~30% de chance de erros invisíveis (sobreposição, coordenada errada, escape mal feito). Não dá pra entregar sem render + visual review.

### 6.4. Pedir "fidelidade pixel-perfect"

Não dá. Mesmo com render-loop, fontes podem fallback em headless, fonts métricas variam levemente, blend de cor difere de Imagen vs vetor puro. Critério realista é **paridade comunicacional + 85% paridade estética**, não 100% pixel.

---

## 7. Limitações remanescentes

### 7.1. Hand-drawn organic feel
SVG via LLM produz formas geométricas precisas. O "warmth" de desenho à mão livre do Gemini é difícil de replicar — requer simulação de variação de peso de linha + jitter controlado + texturas. Possível via `<filter>` com turbulence + displacementMap, mas custoso.

### 7.2. Sombras suaves e ruído de papel
Possível via filters SVG mas o LLM raramente acerta os parâmetros sem visão real. Render-loop ajuda mas exige ~5+ iterações por filter.

### 7.3. Ilustrações orgânicas (rosto humano, objeto 3D realista)
Limite duro. Caminho realista: gerar via Imagen/Midjourney e embutir como `<image>` no SVG. Híbrido raster-dentro-de-vetor.

### 7.4. Render-loop é caro em tokens
Cada iteração: Bash (renderiza) + Read PNG (~200KB image input) + análise + Edit. Para um poster denso, 5-8 iterações custam significativamente. Não é grátis.

### 7.5. Browser headless tem inconsistências
Edge/Chrome ocasionalmente renderiza SVGs muito complexos de forma inconsistente (especialmente filters + masks aninhados). Resvg (resvg-cli via Rust) é mais determinístico para SVG puro, mas requer install.

---

## 8. Recomendações para o plugin `frank-mkt` (acionáveis)

### 8.1. Atualizar `atelier-criativo` (agente)

**Adicionar Bash à frontmatter de tools do agente:**

```yaml
# atual:
tools: Read, Write, Edit, Glob, Grep, WebSearch, WebFetch, Agent

# proposto:
tools: Read, Write, Edit, Glob, Grep, WebSearch, WebFetch, Agent, Bash
```

Justificativa: sem Bash, o agente não consegue fechar o render-loop sozinho. Precisa do Claude principal como intermediário, o que adiciona latência e quebra a delegação clean.

### 8.2. Criar nova skill: `render-loop-svg`

Proposta de skill nova no plugin (`frank-mkt:render-loop-svg`):

```markdown
---
name: render-loop-svg
description: Geração iterativa de SVG/HTML com feedback visual real via headless browser. Renderiza SVG → PNG → lê com multimodal → ajusta. Cobre cross-platform (Windows Edge / macOS Edge / Linux Chrome), commands prontos, troubleshooting de race conditions, fonte fallbacks, complex filters. Para qualquer infográfico SVG denso onde "ver o resultado" é necessário antes de declarar pronto.
when_to_use: Sempre que gerar SVG com mais de ~200 linhas ou complexidade visual (ilustrações, fórmulas matemáticas, mini-charts, layout multi-zona). Combinar com svg-engineering-ia (técnica de markup) e composicao-visual (estrutura).
---

# Conteúdo:
- Commands prontos Edge/Chrome headless Windows/Mac/Linux
- Pitfalls: race condition Start-Sleep, file:// URL com barras, viewBox vs window-size
- Estratégia incremental (camadas + render entre elas)
- Como ler PNG com Read multimodal e o que observar
- Critérios de avaliação visual: alinhamento, overlap, legibilidade de texto pequeno, contraste de cor, densidade de informação
- Loop de no máximo N iterações antes de aceitar (~5 iterações)
- Quando desistir e migrar pra híbrido raster-em-vetor
```

### 8.3. Atualizar skill `svg-engineering-ia`

A skill já menciona "render-loop" conceitualmente mas não tem operacionalização. Adicionar seção:

```markdown
## Render-loop visual (operacional)
Toda geração de SVG não-trivial DEVE seguir:
1. Write SVG inicial
2. Bash → Edge headless → PNG
3. Read PNG (multimodal)
4. Avaliar: alinhamento, overlap, legibilidade, hierarquia
5. Edit SVG corrigindo problema mais crítico (1 por iteração)
6. Voltar para 2
Stop condition: aceitar quando 3 iterações consecutivas trouxerem mudança <10%, ou quando atingir 5 iterações totais.
```

### 8.4. Criar hook `PreToolUse` que injeta render-loop quando detecta Write em `.svg`

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Write",
        "filePattern": "*.svg",
        "command": "echo 'LEMBRETE: depois de escrever esse SVG, renderize via Edge headless e leia o PNG antes de declarar pronto. Comando: msedge --headless=new --window-size=W,H --screenshot=OUT.png file:///PATH.svg'"
      }
    ]
  }
}
```

Isso emite uma reminder no contexto sempre que Claude escreve um SVG, forçando consciência do loop.

### 8.5. Skill complementar: `infografico-poster-cientifico`

Domínio específico que se beneficia: poster científico denso (Tufte / Vignelli / Aicher / Edward Tufte's "Beautiful Evidence"). Inclui:
- Padrões de zona (header / body multi-coluna / footer-quote)
- Layout A4/A3 portrait com viewBox 1024×1536
- Sistema typo 4-níveis hierárquicos
- Inclusão de fórmulas matemáticas em SVG (técnica `<tspan dy>` + Cambria Math)
- Inclusão de mini-gráficos esquemáticos (path de onda, barras, vetores)
- Inclusão de referências acadêmicas formatadas
- Quando preferir HTML+CSS rasterizado vs SVG puro

### 8.6. Atualizar `atelier-criativo` para invocar skills companheiras

Atualmente o agente carrega muitas skills mas escolhe sozinho qual usar. Adicionar à descrição do agente:

```markdown
Para tarefa de infográfico SVG complexo, OBRIGATORIAMENTE invocar nesta ordem:
1. composicao-visual (estrutura)
2. tipografia-corporativa (sistema typo)
3. paleta-cores-corporativa (cor)
4. iconografia-corporativa (ícones reutilizáveis)
5. svg-engineering-ia (markup)
6. render-loop-svg (validação visual) — NOVA
```

### 8.7. Command de slash novo: `/frank-mkt:gerar-infografico`

Workflow guiado:
1. Pergunta tema + referência visual (PNG/URL)
2. Pergunta dimensão + paleta
3. Roda atelier-criativo com brief multi-skill montado
4. Renderiza
5. Mostra ao user
6. Loop de ajustes guiados

### 8.8. Adicionar ao `manutencao-skills` (meta-skill)

Documentar essa lição como padrão: *"Skills que prescrevem técnica visual SEM operacionalização de feedback visual real produzem output cego. Sempre incluir render-loop em skills que geram artefatos visuais."*

---

## 9. Apêndice A — Arquivos gerados na sessão (referência)

```
D:\4nk\teste_mkt\docs\
├── gestuum_matematica.png            (6.779 KB, REFERÊNCIA Gemini)
├── gestuum_matematica.svg            (44.6 KB, V2 final do Claude)
├── gestuum_matematica_preview.html   (wrapper de visualização)
├── gestuum_dispositivo_comunicacao.png (6.112 KB, poster irmão)
├── claude-plugins-infografico.svg    (V0, exercício simples)
├── claude-plugins-infografico.html
├── _render_v1.png                    (V1 renderizada, fraca)
├── _render_v2.png                    (V2 renderizada, ~85% paridade)
├── _comparacao.html                  (lado a lado V0/V1/V2/Gemini)
└── aprendizado_infografico.md        (este documento)
```

## 10. Apêndice B — Comparação quantitativa

| Métrica | Gemini PNG | Claude V1 SVG | Claude V2 SVG |
|---|---|---|---|
| Tamanho do arquivo | 6.779 KB | 28.8 KB | 44.6 KB |
| Linhas de código | n/a | ~480 | 766 |
| Editável | ❌ | ✅ | ✅ |
| Escalável sem perda | ❌ | ✅ | ✅ |
| Texto indexável (SEO/screen-reader) | ❌ | ✅ | ✅ |
| Versionável (git diff) | ❌ | ✅ | ✅ |
| Localizável (i18n string-swap) | ❌ | ✅ | ✅ |
| Animável | ❌ | ✅ | ✅ |
| Densidade informacional vs original | 100% | ~70% | ~95% |
| Fidelidade visual vs original | 100% | ~40% | ~85% |
| Tempo de geração | ~30s (Imagen) | ~5min (LLM) | ~12min (LLM + render-loop) |
| Custo de tokens (estimado) | n/a | ~20k | ~60k |

## 11. Apêndice C — Padrão de brief que funcionou (template reutilizável)

```markdown
Tarefa: gerar SVG vetorial replicando [REFERÊNCIA_PNG].

**Antes de começar:**
1. Leia o PNG referência: [PATH]
2. Leia tentativas anteriores (se houver): [PATHS]
3. Anote o que está faltando ANTES de escrever uma linha

**Render-loop visual (REGRA OPERACIONAL):**
Use este comando Bash/PowerShell após cada camada significativa:
[COMANDO_RENDER]
Depois espere 1.2s, leia o PNG gerado com Read (multimodal), avalie e corrija.

**Skills companheiras a invocar nominalmente:**
- composicao-visual (grid, hierarquia)
- tipografia-corporativa (escala, pareamento)
- paleta-cores-corporativa (extrair hex do PNG)
- iconografia-corporativa (ícones inline reutilizáveis)
- svg-engineering-ia (markup técnico)
- render-loop-svg (validação visual)

**Construção em camadas:**
Camada 1: background + header → render → ver → ajustar
Camada 2: zona [N] → render → ver → ajustar
... (1 zona por iteração)
Final: render completo → comparar com referência → honestamente reportar gaps

**Critérios visuais específicos (não genéricos):**
[LISTAR POR ZONA — ex: "mão com 5 dedos individuais, articulações, wearable com bezel + tela + LED"]

**Densidade alvo:** ≥95% da área ocupada (medir mental ou via grid)

**Stop conditions:**
- 3 iterações consecutivas com mudança <10%
- 5 iterações totais máximo
- Aceitar quando paridade comunicacional 100% e estética ≥80%

**Entregáveis:**
1. [PATH].svg — vetor final
2. [PATH].html — preview wrapper minimalista
3. [PATH]_render.png — renderização final para o operador humano

**Relatório final:**
- Quantas iterações de render-loop
- Lado-a-lado: o que bateu, o que não bateu
- Tamanho do SVG
- Limitações persistentes
```

---

## 12. Conclusão para o próximo Claude

Três ações de impacto alto que você (próximo Claude trabalhando o plugin) deveria priorizar:

1. **Adicionar `Bash` à frontmatter de tools do `atelier-criativo`** — destrava autonomia real
2. **Criar skill `render-loop-svg`** com commands prontos cross-platform — operacionaliza o que `svg-engineering-ia` só menciona conceitualmente
3. **Atualizar `svg-engineering-ia` com seção "render-loop operacional"** — torna o feedback visual obrigatório para SVGs não-triviais

Três ações de impacto médio:

4. **Hook `PreToolUse` em `Write *.svg`** que lembra do loop
5. **Skill `infografico-poster-cientifico`** especializada
6. **Command `/frank-mkt:gerar-infografico`** com workflow guiado

Princípio metodológico geral que emergiu da sessão e que vale registrar no `manutencao-skills`:

> **"Skills que prescrevem técnica visual sem operacionalizar feedback visual real produzem output cego. Todo skill que gera artefato visual deve incluir loop de validação."**

Este é o aprendizado central. Os comandos e skills concretas seguem deste princípio.

---

*Documento escrito por: Claude Opus 4.7 (1M context), Claude Code CLI, 2026-05-11*
*Sessão de teste: Alex Jalkh (`alexjalkh@gmail.com`), projeto `teste_mkt`, plugin `frank-mkt` v2.x*
*Para: Claude responsável pela manutenção do plugin frank-mkt*
