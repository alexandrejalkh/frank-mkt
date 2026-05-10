---
name: iconografia-corporativa
description: Iconografia Corporativa 2026 (sistema icones consistente + grid 24/32px + Stroke vs Fill + line weight 1.5/2/2.5px + Lucide 1500+ icons / Heroicons 296 / Phosphor 7000+ / Tabler 5400+ / Iconify 200k+ universal + custom icon set process + integracao svg-engineering-ia + nomenclatura semantic + Storybook docs + npm distribution) para brand designers/devs frontend/agencias/design-system-leads, integracao brand-book-methodology + svg-engineering-ia + design-system-basico. 5a SKILL Bloco Identidade Visual Corporativa / Brand Design.
volatility: medium
last_review: 2026-05-09
next_review: 2026-11-09
languages: [pt-BR]
audience: [brand-designers, devs-frontend, agencias, design-system-leads, illustrators]
ascii_only: true
---

# Skill: iconografia-corporativa

> Sistema de iconografia corporativa coesa em 2026: grid + line weight + stroke/fill discipline + bibliotecas open source maduras (Lucide/Heroicons/Phosphor/Tabler/Iconify) + processo custom set + geracao via IA (Claude/SVG) + nomenclatura semantica + distribuicao npm + Storybook docs. Audiencia: brand designers, devs frontend, agencias, design-system-leads, illustrators.

---

## Decaimento Temporal

- volatility: medium
- last_review: 2026-05-09
- next_review: 2026-11-09 (6 meses)
- gatilhos de revisao antecipada:
  - lancamento de nova versao major Lucide/Heroicons/Phosphor/Tabler/Iconify
  - mudanca em recomendacoes de grid/line weight de Material Design 3 / IBM Carbon / Polaris / Pajamas
  - novas restricoes de licenca (MIT -> outra) em libraries citadas
  - evolucao de tooling Claude/MCP para geracao SVG em escala
  - mudanca em padroes de bundle size / tree-shaking / svgo / svg-sprite

Fundamentos (grid 24/32px, stroke vs fill, semantic naming) sao estaveis ha decadas. O que muda rapido: bibliotecas, tooling de IA, padroes de distribuicao npm, build pipelines.

---

## Visao Geral

Iconografia corporativa NAO e "escolher icones bonitos no Figma". E sistema visual de mesma ordem de importancia que tipografia e paleta:

- icones aparecem em alta densidade (UI, decks, e-mail, app, social) e qualquer inconsistencia (line weight diferente, fill vs stroke misturado, grid quebrado) e percebida instantaneamente como amadorismo;
- a decisao primaria e estilo (stroke / fill / duotone) antes de quantidade;
- a decisao secundaria e biblioteca base (Lucide / Heroicons / Phosphor / Tabler / Iconify) vs custom vs hibrido;
- a decisao terciaria e ferramental: como mantemos cobertura, naming, versionamento, distribuicao (npm / sprite / IconFont legacy);
- 2026 traz IA (Claude SVG, MCPs de icones, skills) que mudam a economia de criar custom set: o que custava semanas custa horas, mas a manutencao da coesao continua sendo o gargalo.

Esta skill cobre: 8 fundacoes (foundations -> open source libs -> custom process -> IA generation -> naming/storybook -> Brasil 2026 -> mensuracao/tools -> aplicacao MKT), 18 anti-patterns, 18 regras de ouro, 4 personas, checklist contraditorio, ~60 referencias.

Cross-skill critico: `svg-engineering-ia` (base ferramental), `logo-design-process`, `brand-book-methodology`, `paleta-cores-corporativa`, `tipografia-corporativa`, `design-system-basico`, `microcopy`, `acessibilidade-wcag`.

---

## Fundacao 1 — Icon System Foundations (Grid + Stroke vs Fill + Line Weight + Sizes)

### 1.1 Grid: 24x24 vs 32x32 vs hibridos

- **24x24** e o padrao de fato em UI (Lucide, Heroicons, Tabler, Material Symbols, Feather, IBM Carbon, Polaris). Live area tipica 20x20 com 2px de padding/safe area;
- **32x32** e padrao Phosphor e usado quando o icone tem mais detalhe (illustration-friendly) ou em densidades grandes de marketing/print;
- **48x48 / 64x64** sao tamanhos de illustration / app icon, NAO de UI icon — outra disciplina;
- corporativos serios fixam UM grid base e DERIVAM os multiplos (16, 20, 24, 32) com regras de optical scaling — nao basta `transform: scale(0.66)` em um icone 24px para chegar em 16px (linhas ficam tortas);
- fixe o grid no brand book com keylines (circulo, quadrado, retangulo, area "live"); reproduza Material/Carbon/Polaris se nao tiver designer dedicado.

### 1.2 Stroke vs Fill vs Duotone: o eixo politico

- **Stroke (outline)**: linhas abertas, peso fixo. Default de Lucide, Heroicons-outline, Tabler, Feather. Combina com tipografia leve, marcas tech-friendly, dashboards. Risco: em tamanhos < 16px, a linha desaparece;
- **Fill (solid)**: silhuetas preenchidas. Default de Heroicons-solid, Material Symbols Filled, Phosphor Fill. Combina com mobile, alta densidade, alertas, estados ativos;
- **Duotone**: dois tons (geralmente cor + transparencia). Phosphor Duotone, Iconoir alternates. Boa para landing pages, decks, marketing — RUIM para UI dense;
- regra de ouro: escolha UM estilo dominante (>= 80% dos usos) e UM secundario (estados ativos, alertas). NUNCA mix > 2 estilos no mesmo viewport.

### 1.3 Line weight: 1.5 / 2.0 / 2.5px

- **1.5px** = elegante, premium, tipo Phosphor Light, Iconoir, alguns banks. Risco em monitores low-DPI;
- **2.0px** = padrao Lucide / Heroicons-outline / Tabler. Equilibrio default;
- **2.5-3px** = bold, mobile-first, Phosphor Bold, marcas brasileiras energetizadas. Risco de saturar UI dense;
- escolha um peso e fixe — todos os icones do sistema, do menor (16px) ao maior (48px), devem ter o MESMO line weight aparente. Em 16px o stroke pode precisar ser optical-tuned para 1.75px renderizado.

### 1.4 Tamanhos canonicos (SISTEMA OPTICAL SCALING)

| Tamanho | Uso tipico | Live area | Stroke aparente |
|---|---|---|---|
| 12px | inline text, badges | 10x10 | 1.25px |
| 16px | dense UI, formularios | 14x14 | 1.5px |
| 20px | UI default | 18x18 | 1.75px |
| 24px | UI default (Lucide) | 20x20 | 2px |
| 32px | toolbar, mobile | 28x28 | 2px |
| 48px | empty states | 42x42 | 2px |
| 64px+ | hero, illustration | 56x56+ | 2-2.5px |

Optical scaling: NAO redimensione o mesmo SVG — desenhe variantes 16/20/24 ou use bibliotecas com optical sizes (Material Symbols tem optical sizes 20/24/40/48 por design).

### 1.5 Padding e bounding box

- mantenha um padding/safe area de 1-2px em torno do live area (em grid 24, area viva 20x20);
- NUNCA encoste tracos no bounding box — quebra alinhamento quando icones ficam lado a lado;
- bounding box deve ser sempre QUADRADO no SVG, mesmo que o desenho nao seja — para preservar baseline.

---

## Fundacao 2 — Open Source Libraries (Lucide + Heroicons + Phosphor + Tabler + Iconify)

Comparativo neutro das 5 bibliotecas mais usadas em 2026. Sempre **valide a licenca atual** no momento da escolha.

### 2.1 Lucide (~1500+ icons, MIT)

- fork open source mantido do Feather, com comunidade ativa;
- grid 24x24, stroke 2px, padrao "clean & geometric";
- **default do shadcn/ui** — quando voce roda `npx shadcn add button`, o componente importa Lucide;
- pacotes: `lucide-react`, `lucide-vue-next`, `lucide-svelte`, `lucide-angular`, `lucide-static` (SVG puros);
- tree-shakeable (cada icone e um modulo) — bundle pequeno se importado individualmente;
- ideal para: SaaS, dashboards, ferramentas tech, projetos shadcn/ui;
- limite: variedade menor que Phosphor; sem variantes weight (so um peso).

### 2.2 Heroicons (296 icons, MIT)

- mantido pelo time Tailwind UI (Tailwind Labs);
- grid 24x24 (outline + solid) e 20x20 (mini, solid only) e 16x16 (micro, solid only);
- 4 estilos: `outline`, `solid`, `mini`, `micro` — todos no mesmo set;
- **default para projetos Tailwind UI / Headless UI**;
- pacotes: `@heroicons/react`, `@heroicons/vue`;
- limite: cobertura limitada (~300 icons) — voce VAI precisar complementar com custom para verticais especificas (juridico, saude, agro, etc);
- ideal para: marketing site + SaaS Tailwind, design system enxuto.

### 2.3 Phosphor Icons (~7000+ icons, MIT)

- a biblioteca mais variada em 2026: 6 weights (thin, light, regular, bold, fill, duotone) por icone;
- grid 32x32 (nao 24!);
- `@phosphor-icons/react`, `@phosphor-icons/web`, integracoes Vue/Svelte;
- ideal para: produtos consumer onde icone e diferencial (apps, marketing-heavy), illustrators, marcas que precisam de duotone;
- bundle maior se importar tudo — sempre tree-shake;
- comparativo: Lucide e ~16x mais popular em downloads npm, mas Phosphor e ~5x mais variado em cobertura.

### 2.4 Tabler Icons (~5400+ icons, MIT)

- grid 24x24, stroke 2px, "outline" como padrao + "filled" alternativo;
- forte cobertura para dashboards, admin, finance, healthcare;
- pacotes: `@tabler/icons-react`, `@tabler/icons-vue`, `@tabler/icons` (static SVG);
- ideal para: admin panels, ERPs, dashboards densos, B2B verticals.

### 2.5 Iconify (200k+ icons, multiple licenses)

- NAO e biblioteca, e META-LIBRARY: agrega 100+ icon sets sob uma API unica;
- inclui Lucide, Heroicons, Phosphor, Tabler, Material Symbols, Bootstrap Icons, Font Awesome (free), Simple Icons (logos), e dezenas de sets nicho;
- SSR-friendly via `@iconify/react`, `@iconify/vue`, web component `iconify-icon`;
- escolha por icone individual: `<Icon icon="lucide:chevron-right" />` ou `<Icon icon="phosphor:user-bold" />`;
- **CUIDADO LICENCA**: cada set tem sua licenca — Simple Icons e CC0 mas exige permissao das marcas para uso em produto; Font Awesome free nao inclui Pro icons; alguns sets sao GPL e podem contaminar bundles;
- ideal para: prototipagem rapida, projetos multi-vertical, fallback quando icone especifico falta na lib principal.

### 2.6 Sumario — quando escolher cada uma

| Cenario | Primeira escolha | Justificativa |
|---|---|---|
| Projeto shadcn/ui | Lucide | Default oficial, integracao zero atrito |
| Projeto Tailwind UI | Heroicons | Estilo casa, mantido pelo mesmo time |
| Marca consumer com personalidade | Phosphor | Variedade + duotone + weights |
| Admin/dashboard B2B | Tabler ou Lucide | Cobertura para finance/CRM/ops |
| Prototipo / multi-set | Iconify | API unica, troca-fica facil |
| Marca com identidade unica | Custom set hibrido | Estilo proprio (ver Fundacao 3) |

NAO existe "melhor lib em absoluto" — existe "melhor lib para ESTE produto, ESTA equipe, ESTE estilo de marca".

---

## Fundacao 3 — Custom Icon Set Process (Design + IA + Refine + Uniformize)

Quando criar um set proprio? Quando:
1. a marca tem personalidade visual forte (line weight, corner radius, terminations) que NENHUMA lib captura;
2. o vertical e nicho (juridico-tributario, agro, energia, blockchain) e libs genericas cobrem < 60%;
3. existe budget de design system (>= 1 designer dedicado por 4-8 semanas);
4. o produto vive longo prazo (>= 24 meses) — custom abaixo disso raramente paga.

### 3.1 Etapa 1 — Audit + Inventory

- liste TODOS os icones que aparecem hoje no produto (UI, marketing, app, deck);
- categorize por funcao (action, navigation, status, object, brand);
- identifique duplicatas semanticas ("home" vs "dashboard" vs "house" — escolha um);
- prioritize: 80% do uso vem de ~50 icones (regra Pareto). Comece por esses.

### 3.2 Etapa 2 — Style Spec (CONTRATO VISUAL)

Documente ANTES de desenhar:
- grid base (24 ou 32);
- live area / padding;
- line weight (1.5 / 2 / 2.5);
- corner radius (0 / 1px / 2px / circular);
- terminations (round / square / butt);
- joins (round / miter / bevel);
- fill rule e estilo dominante (stroke / fill / duotone);
- paleta minima (currentColor / 2 cores duotone / fixa);
- como tratar inside cuts e negative space.

Esta spec vira input para IA (Fundacao 4) e para revisores humanos.

### 3.3 Etapa 3 — Concept / Master Icons

- desenhe 10-15 icones "master" (home, user, settings, search, plus, close, check, arrow, chevron, more, edit, delete, share, download, upload);
- desses sai a "DNA visual": como um "home" desse set e diferente de um "home" Lucide?
- valide com 3-5 stakeholders BLIND (sem dizer qual e o seu) — eles escolhem qual encaixa na marca.

### 3.4 Etapa 4 — Expansao + IA-Assisted

- com a spec + master icons, use IA (Claude com skill `svg-engineering-ia`, IcoGenie, icon-set-generator) para gerar lotes;
- prompts incluem a spec EXPLICITA: "grid 24, stroke 2px, round caps, round joins, currentColor, 2px padding";
- fornecer 3-5 master icons como referencia visual (Claude nao gera com 100% de coerencia em batch grande — voce VAI iterar);
- gere em LOTES de 10-20, nunca 100+ de uma vez (drift de estilo).

### 3.5 Etapa 5 — Refine (Manual)

- IA produz 70-80% pronto; os 20-30% restantes sao manuais:
  - alinhar pixel-perfect ao grid;
  - corrigir line weight aparente em curvas (curva tem que ser ~10% mais grossa que reta para parecer igual);
  - terminations e joins consistentes;
  - resolver ambiguidades semanticas (icone esta lendo "documento" ou "pagina"?).

### 3.6 Etapa 6 — Uniformizacao

- abra TODOS os icones lado a lado (Figma frame, Storybook grid);
- caca de inconsistencia: peso visual diferente, baseline desalinhado, padding inconsistente, terminations divergentes;
- itere ate o set parecer "feito pela mesma pessoa no mesmo dia" (mesmo se foi IA + 3 designers + 2 meses).

### 3.7 Etapa 7 — Test in Context

- teste em fundo claro E escuro;
- teste em 12, 16, 20, 24, 32, 48px;
- teste com tipografia da marca lado a lado;
- teste em UI real, nao em grid isolado;
- teste com usuarios: associacao livre — mostre o icone, pergunte "o que e?". Se < 70% acerta, redesenhe.

---

## Fundacao 4 — Integracao svg-engineering-ia (Geracao via Claude + symbols+use)

Esta secao depende fortemente da skill **`svg-engineering-ia`** — ela cobre fundamentos de SVG (viewBox, stroke, fill, path, transforms, optimization). Aqui foco em iconografia especificamente.

### 4.1 Por que SVG (e nao PNG / IconFont) em 2026

- escala sem perda;
- color via `currentColor` (herda CSS);
- acessibilidade (`<title>`, `aria-label`);
- bundle pequeno por icone (< 1KB apos svgo);
- sem CORS/font-loading issues (IconFont morreu — paz a sua alma);
- animacao via CSS / SMIL / JS;
- compativel com tree-shaking quando empacotado como modulo JS.

### 4.2 SVG canonico para icone de UI

```xml
<svg
  xmlns="http://www.w3.org/2000/svg"
  viewBox="0 0 24 24"
  width="24"
  height="24"
  fill="none"
  stroke="currentColor"
  stroke-width="2"
  stroke-linecap="round"
  stroke-linejoin="round"
  aria-hidden="true"
  focusable="false"
>
  <!-- paths aqui, pixel-perfect no grid 24 -->
</svg>
```

Pontos:
- `viewBox="0 0 24 24"` (ou 32);
- `fill="none"` + `stroke="currentColor"` para herdar cor do CSS;
- `stroke-width="2"` (ou peso escolhido);
- `stroke-linecap="round"` e `stroke-linejoin="round"` (ou square/miter conforme spec);
- `aria-hidden="true"` quando icone e decorativo (acompanha texto); `aria-label="..."` quando icone e interativo standalone;
- `focusable="false"` para evitar focus em IE legacy / Edge antigo (irrelevante em 2026, mas barato).

### 4.3 Geracao via Claude — best practices

- alimente Claude com SPEC explicita (grid, weight, caps, joins);
- forneca 3-5 SVGs MASTER como reference;
- gere 5-10 por turno, nunca 50+ (drift);
- valide: cada SVG gerado deve passar `svgo --multipass` sem warnings serios;
- valide: cada SVG deve renderizar em 16/24/48px sem artefatos;
- skills/tools 2026: Logo Creator skill, Icon Set Generator skill, IcoGenie MCP server, svg-engineering-ia skill (deste plugin);
- limitacao conhecida: drift de estilo em conversas longas — quebre em sessoes de 10-20 icones.

### 4.4 Distribuicao via SVG sprite (`<symbol>` + `<use>`)

Para apps com 50+ icones, sprite SVG e DRY e cacheable:

```xml
<!-- sprite.svg -->
<svg xmlns="http://www.w3.org/2000/svg" style="display:none">
  <symbol id="icon-home" viewBox="0 0 24 24">
    <path d="M3 12 12 3l9 9..."/>
  </symbol>
  <symbol id="icon-user" viewBox="0 0 24 24">
    <path d="M..."/>
  </symbol>
</svg>
```

Uso:
```html
<svg class="icon" aria-hidden="true">
  <use href="/sprite.svg#icon-home" />
</svg>
```

Vantagens: 1 HTTP cacheado, escalavel, currentColor funciona. Desvantagens: tree-shaking e manual (voce inclui tudo ou separa em sprites por rota).

Ferramentas: `svg-sprite`, `svgo`, `svg-symbol-sprite-loader` (webpack), `vite-plugin-svg-icons`.

### 4.5 Distribuicao via npm package

Ideal para empresas com produtos multiplos:

```
@empresa/icons/
├── package.json
├── src/
│   ├── icons/
│   │   ├── home.svg
│   │   ├── user.svg
│   │   └── ...
│   ├── react/
│   │   ├── Home.tsx (componente)
│   │   └── index.ts (exports)
│   └── vue/
└── README.md
```

- versionamento semver (breaking change = major);
- export por icone individual (tree-shake);
- types TypeScript;
- changelog;
- publicacao npm privada (GitHub Packages, Verdaccio) ou publica.

---

## Fundacao 5 — Nomenclatura Semantica + Versioning + Storybook

### 5.1 Naming convention (kebab-case + verb-noun ou category-noun)

- **kebab-case** para arquivos e tokens: `arrow-right.svg`, `user-circle.svg`;
- **PascalCase** para componentes React/Vue: `ArrowRight`, `UserCircle`;
- **prefixo opcional por categoria** quando o set e grande:
  - `action-edit`, `action-delete`, `action-share`
  - `nav-home`, `nav-back`, `nav-menu`
  - `status-success`, `status-error`, `status-warning`
  - `obj-document`, `obj-folder`, `obj-image`
  - `social-twitter`, `social-linkedin` (CUIDADO: marcas registradas);
- **variantes** com sufixo:
  - `chevron-right` (outline default)
  - `chevron-right-fill` (variante preenchida)
  - `chevron-right-bold` (variante peso bold);
- **NAO use**: nomes vagos (`icon1`, `misc-thing`), nomes baseados em uso (`pricing-card-icon` — uso muda, nome vira mentira), nomes de cor (`blue-arrow` — cor muda).

### 5.2 Naming: o que mostra vs o que representa

- nomeie pelo que MOSTRA, nao pelo que representa;
- icone de cronometro = `stopwatch`, NAO `speed`;
- icone de nuvem = `cloud`, NAO `backup`;
- representacao (uso) muda por contexto; o que mostra e estavel.

### 5.3 Versionamento (semver)

- **major** (1.x.x -> 2.0.0): icone removido, renomeado, mudanca visual breaking (ex: home virou "house" diferente);
- **minor** (1.0.x -> 1.1.0): icone novo adicionado, variante nova;
- **patch** (1.0.0 -> 1.0.1): otimizacao SVG, correcao pixel-perfect, refactor sem mudanca visual.

### 5.4 Aliases e deprecation

- ao renomear `home` -> `house`, mantenha `home` por 1-2 majors com warning de deprecation;
- adicione changelog claro: "v2.0: `home` deprecated, use `house`. Removed in v3.0.";
- nunca quebre silenciosamente — codigo cliente nao detecta.

### 5.5 Storybook como source of truth

- documente cada icone com:
  - preview em 16/24/48px;
  - codigo de import;
  - nome semantico;
  - tags / categorias;
  - aliases / deprecated;
  - exemplo de uso em contexto;
- Storybook addons relevantes: `@storybook/addon-docs`, `@whitespace/storybook-addon-html`;
- alternativas: site dedicado (ex: `lucide.dev`, `phosphoricons.com`, `heroicons.com`) — copie a estrutura.

---

## Fundacao 6 — Brasil 2026 (cases nacionais Magalu/Nubank/Stone + tropicalizacao)

### 6.1 Cenario brasileiro

- design systems brasileiros mapeados em listas como `designsystemsbrasileiros.com` (Marcos Pagano e outros) — DS Caixa, Pan Mahoe, Globo Hero, iFood, Magalu, Nubank, Stone, Banco do Brasil, governo (Gov.br), e dezenas de healthtechs/edtechs;
- maioria adota Lucide / Heroicons / Phosphor como base + custom set para a marca (logo de produto, cobranca, juridico-fiscal);
- mercado brasileiro tem necessidades especificas:
  - icones fiscais (NF-e, NFS-e, MEI, Simples Nacional, DARF, ISS);
  - icones bancarios locais (PIX, boleto, TED, DOC, Open Finance);
  - icones juridicos (peticao, processo, OAB, Lex);
  - icones agro (commodity, safra, soja, cafe);
  - emojis culturais (regionalismos);
- esses icones raramente existem nas libs globais — exigem custom OU sets brasileiros.

### 6.2 Tropicalizacao consciente

NAO basta traduzir nomes. Tropicalizacao real:
- cone de PIX deve ser RECONHECIVEL (use o simbolo oficial do BCB como referencia, nao reinvente);
- icone de boleto deve mostrar o codigo de barras (mental model brasileiro);
- icone de "documento fiscal" varia por contexto (NF-e B2B vs cupom B2C);
- evite stereotypes (sol, palmeira, samba para "Brasil") — soa cafona em B2B/fintech serio.

### 6.3 Referencias publicas brasileiras

- DS Gov.br tem icones publicos com licenca aberta (verificar termos atuais);
- DS Magalu (publico parcial), DS Nubank Aphrodite (parcial), DS Stone Jadu — costumam citar Phosphor ou Lucide como base;
- DS Pan Mahoe, DS Globo Hero, DS iFood Pomodoro — todos citados em compilados publicos;
- valide licenca em cada caso — nem todo DS publico libera os icones.

### 6.4 LGPD e direitos de imagem em icones

- icones que retratam pessoas reais (rostos, fotos) nao sao iconografia — sao avatares (skill `marca-pessoal-personal-branding` cobre);
- icones de marcas terceiras (Twitter/X, Meta, Google, Apple, PIX) tem trademarks — uso requer:
  - PIX: marca do BCB, uso permitido em contexto de fluxo PIX, logo precisa seguir manual oficial;
  - X (Twitter): proibido alterar logo, uso em links de share permitido com regras;
  - Meta/Facebook/Instagram/WhatsApp: brand guidelines publicas;
  - sempre baixe o logo OFICIAL da brand page do dono — nunca invente.

---

## Fundacao 7 — Mensuracao + Tools 2026 (npm distribution + bundle size + tree-shaking)

### 7.1 Bundle size matters

- `lucide-react` instalado: ~600KB unzipped, mas tree-shake reduz para ~3-5KB com 20-30 icones;
- `phosphor-react` instalado: ~12MB unzipped (todas as weights), tree-shake essencial;
- `@heroicons/react`: ~500KB, tree-shake-friendly;
- regra: SEMPRE importe icone individual:
  - ruim: `import { Home, User, Settings } from 'lucide-react/all'`
  - bom: `import { Home } from 'lucide-react'`
- valide com `webpack-bundle-analyzer`, `rollup-plugin-visualizer`, ou `next build` (Next.js).

### 7.2 Tree-shaking checklist

- bundler suporta ES modules (Webpack 5+, Rollup, Vite, esbuild, Bun);
- biblioteca tem `"sideEffects": false` no package.json;
- imports nomeados (nao `import * as Icons`);
- nao reexport via barrel files que impedem tree-shake;
- production build com minify ativo.

### 7.3 Tooling 2026

- **svgo**: otimiza SVG (remove metadata, comprime paths, mantem viewBox);
- **svg-sprite** / **svg-sprite-loader**: gera sprite a partir de pasta de SVGs;
- **vite-plugin-svg-icons**: integra sprite no Vite com HMR;
- **figma-icons-export** / **figma-export-icons**: exporta icones do Figma em batch;
- **iconify-tools**: build/import sets para Iconify;
- **storybook-addon-svg-icons**: catalogo Storybook;
- **icogenie**: MCP server para gerar SVG via Claude inside IDE;
- **icon-set-generator skill**: Claude skill para gerar sets coerentes;
- **figma plugins**: Iconify Figma, Lucide Figma, Phosphor Figma, SVG Export, Icon Resizer.

### 7.4 Metricas de saude do icon system

- cobertura: % de UIs que usam icones do set oficial vs ad-hoc (meta >= 95%);
- consistencia visual: % de paginas onde 2+ estilos de icone coexistem (meta = 0%);
- bundle size: KB de icones por rota (meta < 10KB por rota tipica);
- tempo de descoberta: quanto demora um dev encontrar o icone certo na docs (meta < 60s);
- frequencia de PRs adicionando custom icons one-off (meta -> baixar ao longo do tempo).

---

## Fundacao 8 — Aplicacao em Content MKT

Iconografia em conteudo MKT (decks, blog, e-mail, social, ads) e diferente de UI:

### 8.1 Decks e apresentacoes

- 1-2 icones por slide max — caso contrario vira ruido;
- tamanho minimo 32px em projecao (auditorios pequenos) ou 48px+ (auditorios medios);
- duotone funciona BEM em deck (chama atencao sem competir com texto);
- evite icone gigante "decorativo" no canto — trate icone como informacao, nao ornamento.

### 8.2 Blog e long-form

- icones inline ao lado de bullets melhoram scan (especialmente em listas longas);
- nao misture estilos: outline NA UI + fill no texto = inconsistencia;
- icones em ilustracoes editoriais (hero do post) sao OUTRA disciplina — nao reutilize do icon system.

### 8.3 E-mail marketing

- e-mail clientes (Gmail, Outlook) tem suporte SVG inconsistente — fallback PNG sempre;
- icones em e-mail devem ser >= 24px (alguns clients down-render);
- color scheme dark-mode quebra em e-mail — teste com Litmus / Email on Acid.

### 8.4 Social media e ads

- Instagram/Facebook: icones em creatives nunca menores que 64px (telas pequenas, scroll rapido);
- LinkedIn: icones em carousels devem reforcar marca (paleta, line weight) — mistura de set generic + custom soa amador;
- ads pagos: icones afetam CTR — teste A/B (mesmo creative, icones diferentes).

### 8.5 Brand book + uso de iconografia em material publicitario

- documentar no brand book: WHEN to use ICON vs ILLUSTRATION vs PHOTO;
- iconografia = informacao funcional;
- illustration = emocao / narrativa;
- photo = realidade / pessoas;
- usar icone onde deveria ser foto = fricciona empatia; usar foto onde deveria ser icone = poluicao visual.

---

## Anti-Patterns 18

1. **Misturar 2-3 bibliotecas no mesmo viewport** ("vou pegar esse de Lucide e esse de Phosphor"). Estilos divergem — fica feio em segundos.
2. **Icone IA-gerado direto no produto sem refine humano**. Drift de estilo, line weight tortos, semantica errada.
3. **PNG em vez de SVG em 2026**. Indefensavel — escala ruim, sem currentColor, sem a11y, peso maior.
4. **IconFont (Font Awesome legacy)**. Acessibilidade ruim, sem currentColor por glifo, FOIT, dependencia de carregar fonte. Morto desde ~2020.
5. **Stroke 2px desenhado em escala maior + scale CSS**. Linhas borradas em 16px, line weight aparente nao bate com texto.
6. **Mix de fill + outline sem regra**. Default outline + active state fill e OK; aleatorio nao.
7. **Naming descritivo de cor ou contexto**. `blue-button-icon`, `pricing-card-icon` — uso muda, nome vira mentira.
8. **Pular custom set e improvisar**. Quando libs nao cobrem 30%+ dos casos, devs sairao colando SVGs aleatorios da internet.
9. **Custom set sem style spec documentada**. Cada designer interpreta — set vira colcha.
10. **Logos de terceiros sem permissao**. Trademarks nao sao iconografia — Twitter/X, Meta, Google etc tem brand guidelines OBRIGATORIAS.
11. **Nao testar em dark mode**. Icones desenhados so em light viram silhueta ilegivel no dark.
12. **Importar `lucide-react/all`**. Bundle 600KB+ por rota — kill performance.
13. **Sprite SVG sem cache headers**. Sprite carrega em toda navegacao — anula vantagem.
14. **Confundir icone de UI com illustration**. Icone 24px com 50 paths e detalhes 1px — buga em renderizacao mobile.
15. **Acreditar que Iconify "resolve tudo"**. Cada set tem licenca e estilo proprio — escolher random vira frankenstein.
16. **Skip de a11y**. Sem `aria-label` em icone interativo, sem `aria-hidden` em decorativo. Screen readers leem coisa errada ou nao leem.
17. **Promover IA-gerado direto a producao**. IA acerta 80%, mas o 20% restante e o que distingue marca pro de marca medio.
18. **Esquecer optical scaling**. Mesmo SVG em 16/24/48 fica torto. Fontes ja resolveram isso ha 30 anos (optical sizes).

---

## 18 Regras de Ouro

1. **Escolha UMA biblioteca primaria**. Custom set complementa, nao substitui.
2. **Documente style spec ANTES de desenhar custom**. Grid, weight, caps, joins, terminations.
3. **24x24 e default para UI**. So mude se tiver razao (ex: voce escolheu Phosphor 32 conscientemente).
4. **currentColor sempre**. NUNCA hardcode `stroke="#000"` em icones de sistema.
5. **Tree-shake import por icone individual**. Nunca `import * as`.
6. **Stroke 2px (ou 1.5/2.5) consistente** para todo o set.
7. **Outline como default, fill para active state**, nada mais.
8. **Naming kebab-case + semantico (mostra-nao-representa)**.
9. **Versionamento semver com aliases** em renomes/removes.
10. **Storybook ou site dedicado como source of truth**.
11. **A11y: aria-label se interativo, aria-hidden se decorativo, sempre**.
12. **Teste em 16/24/48px e em dark mode**.
13. **Optical scaling**: desenhe variantes 16/20/24 ou use lib com optical sizes.
14. **IA gera 80%, humano refina 20%**. Sem refine, set nao pro.
15. **Brand book documenta when ICON vs ILLUSTRATION vs PHOTO**.
16. **Marcas terceiras: siga brand guidelines do dono**, nao reinvente.
17. **Mensure cobertura, consistencia, bundle size**.
18. **Revise o sistema a cada major do produto**: icones obsoletos saem, novos entram com criterio.

---

## Exemplos Comportamentais

### Persona 1 — Renata, Brand Designer Senior em FinTech (B2C)

Renata acabou de assumir o sistema visual de uma fintech serie B. O produto usa um mix caotico: alguns icones do Material, outros do Heroicons, alguns custom de uma agencia antiga. Ela vai:

1. fazer audit + inventory (Fundacao 3.1) — listar TODOS os icones por tela;
2. escolher Phosphor como biblioteca base (variedade + duotone como diferencial visual da marca);
3. complementar com 30-40 icones custom para verticais financeiros BR (PIX, boleto, MEI, DARF, Open Finance);
4. style spec: grid 32, stroke 2px, round caps/joins, currentColor, duotone reservado para empty states + marketing;
5. usar Claude com skill `svg-engineering-ia` para gerar lotes de 10 icones por sessao a partir de master concepts;
6. publicar como `@fintech/icons` em GitHub Packages, versao 1.0;
7. Storybook docs com paginas por categoria + tags;
8. checklist: 95% das telas migradas em 12 semanas, bundle por rota < 8KB.

### Persona 2 — Marcos, Dev Frontend Senior em SaaS B2B

Marcos integra um SaaS (CRM B2B) usando Next.js + shadcn/ui + Tailwind. O time produto pediu "padronizar icones, porque cada PR usa um diferente". Marcos:

1. ja usa shadcn/ui — Lucide e default; adota Lucide oficialmente;
2. cria utility `Icon.tsx` que envolve Lucide e adiciona aria-label automatico baseado em prop `label`;
3. lint rule (ESLint custom) que proibe `import * from 'lucide-react'` e proibe importar de outras icon libs;
4. documenta no Storybook quais icones do Lucide estao "endorsed" (lista de ~80 que cobrem 95% dos casos);
5. para os 5% remanescentes (icones B2B nicho de CRM), pede ao designer 10-15 customs no estilo Lucide (grid 24, stroke 2px) e adiciona em `src/icons/custom/`;
6. mensura bundle size por rota com Next analyzer — meta 5KB.

### Persona 3 — Patricia, Lider de Design System em Agencia

Patricia atende 8 clientes em verticais variados (saude, agro, juridico, fintech). Ela:

1. NAO tenta um icon system unico para todos — cada cliente recebe seu;
2. processo standard:
   - workshop com cliente: stroke vs fill, weight, mood;
   - escolher biblioteca base (Lucide/Heroicons/Phosphor/Tabler) por mood;
   - definir 30-50 icones custom para o vertical do cliente;
   - usar IA (Claude + svg-engineering-ia) para acelerar;
3. cliente saude: Phosphor base (variedade alta — sintomas, anatomia, exames) + customs;
4. cliente agro: Tabler base + customs (commodities, safra, maquinario);
5. cliente juridico: Heroicons base (set enxuto, mood serio) + customs (peticao, OAB, processo);
6. entrega: package npm privado + Storybook + brand book section sobre iconografia + rules ESLint para devs do cliente.

### Persona 4 — Joao, Founder Tecnico em Startup Pre-Seed

Joao tem 0 designer, esta sozinho construindo MVP. Decisao de iconografia em 30 minutos:

1. usa shadcn/ui + Tailwind por default — entao Lucide vem junto (zero atrito);
2. NAO tenta custom set — pre-product-market-fit, custom e overkill;
3. para os 2-3 icones especificos que faltam (vertical da startup), usa Iconify como fallback escolhendo de Phosphor regular (mais proximo de Lucide visualmente);
4. quando virar serie A (1+ designer dedicado), revisita com processo Fundacao 3.

---

## Checklist Contraditorio Interno (10 perguntas)

Antes de fechar o sistema:

1. **Voce tem UMA biblioteca primaria documentada, ou 2+ misturadas sem regra?**
2. **Sua style spec (grid, weight, caps, joins) esta escrita ou mora "na cabeca"?**
3. **Voce testou os 10 icones mais usados em 16/24/48px e em dark mode?**
4. **Importacoes sao tree-shaken (icone individual) ou voce esta empacotando a lib inteira?**
5. **Cada icone interativo tem `aria-label` e cada decorativo tem `aria-hidden`?**
6. **Naming e semantico (mostra-nao-representa) ou descritivo (cor, contexto)?**
7. **Storybook / site / brand book documenta o set, ou descobrir um icone exige caca em pasta?**
8. **Versionamento e semver com aliases em renomeacoes, ou breaking change silencioso?**
9. **Marcas terceiras (PIX, X/Twitter, Meta, etc) seguem brand guidelines oficiais ou foram inventadas?**
10. **Existe metrica de cobertura (% UI usando set oficial) ou voce nao mede consistencia?**

Se 3+ respostas sao "nao", o sistema nao e profissional ainda — itere antes de declarar pronto.

---

## Referencias

### Bibliotecas open source

- [Lucide Icons](https://lucide.dev/) — fork open source de Feather, MIT
- [Lucide GitHub](https://github.com/lucide-icons/lucide)
- [Heroicons by Tailwind Labs](https://heroicons.com/) — MIT
- [Heroicons GitHub](https://github.com/tailwindlabs/heroicons)
- [Phosphor Icons](https://phosphoricons.com/) — MIT, 7000+ icons em 6 weights
- [Phosphor GitHub](https://github.com/phosphor-icons/core)
- [Tabler Icons](https://tabler.io/icons) — MIT, 5400+ icons
- [Tabler GitHub](https://github.com/tabler/tabler-icons)
- [Iconify](https://iconify.design/) — meta-library, 200k+ icons
- [Iconify GitHub](https://github.com/iconify)
- [Material Symbols](https://fonts.google.com/icons) — Google, Apache 2.0
- [Bootstrap Icons](https://icons.getbootstrap.com/) — MIT
- [Feather Icons](https://feathericons.com/) — MIT, base do Lucide
- [Iconoir](https://iconoir.com/) — MIT, 1500+ icons
- [Remix Icon](https://remixicon.com/) — Apache 2.0
- [Hugeicons](https://hugeicons.com/) — comparativo cited

### Comparativos e guides

- [Lucide vs Heroicons vs Phosphor 2026 (PkgPulse)](https://www.pkgpulse.com/guides/lucide-vs-heroicons-vs-phosphor-react-icon-libraries-2026)
- [25+ Best Open Source Icon Libraries 2026](https://hugeicons.com/blog/development/best-open-source-icon-libraries)
- [5 Best Icon Libraries for shadcn/ui](https://www.shadcndesign.com/blog/5-best-icon-libraries-for-shadcn-ui)
- [Icon Library Comparisons 2026 (iconshub)](https://iconshub.netlify.app/compare)
- [Lucide vs Phosphor Market Share (wmtips)](https://www.wmtips.com/technologies/compare/lucide-vs-phosphor-icons/)

### Foundations e design systems

- [A complete guide to iconography (designsystems.com)](https://www.designsystems.com/iconography-guide/)
- [Icon Size Guidelines for UI/UX 2026 (ColorPark)](https://www.colorpark.io/blog/practical-icon-size-guidelines-for-ui-ux-design)
- [Icon Design Guidelines (Hugeicons)](https://hugeicons.com/blog/design/how-to-design-icons)
- [How to Design Icon Systems for Brand Consistency (Bigeye)](https://www.bigeyeagency.com/insights/design-icon-systems-brand-consistency)
- [Icon Grids and Keylines (Cieden)](https://cieden.com/book/sub-atomic/iconography/icon-grids-and-keylines)
- [How to Maintain Visual Consistency (DEV)](https://dev.to/albert_nahas_cdc8469a6ae8/how-to-maintain-visual-consistency-across-your-app-icons-14ac)
- [IBM Design Language — UI icons](https://www.ibm.com/design/language/iconography/ui-icons/design/)
- [Pajamas Design System — Iconography (GitLab)](https://design.gitlab.com/product-foundations/iconography/)
- [Material Symbols Guidance](https://m3.material.io/styles/icons/overview)
- [Polaris Iconography (Shopify)](https://polaris.shopify.com/design/icons)
- [Carbon Design System Icons (IBM)](https://carbondesignsystem.com/elements/icons/library/)

### Naming e tokens

- [Naming Tokens in Design Systems (Nathan Curtis)](https://medium.com/eightshapes-llc/naming-tokens-in-design-systems-9e86c7444676)
- [Nord Design System — Naming](https://nordhealth.design/naming/)
- [Duet Design System — Naming](https://www.duetds.com/naming/)
- [Token Naming Conventions (Southleft)](https://southleft.com/insights/design-systems/token-naming-conventions/)
- [Structure Over Style: 5 Pillars of Component Naming 2026 (Medium)](https://medium.com/@EmiliaBiblioKit/structure-over-style-the-5-pillars-of-component-naming-for-the-2026-era-333b44ae3ab2)

### Trends 2026

- [Icon Design Trends 2026 (Envato)](https://elements.envato.com/learn/icon-design-trends)
- [Icon Design Trends 2026 (Author Hub)](https://author.envato.com/hub/icon-design-trends-2026/)
- [2026 Icon Design Trends (iamvector)](https://iamvector.com/blog/2026-icon-design-trends-for-designers/)
- [Logo Design Trends 2026 (Creative Bloq)](https://www.creativebloq.com/design/logos-icons/these-logo-design-trends-will-define-2026)

### Brasil / design systems brasileiros

- [Lista Design Systems Brasileiros](https://designsystemsbrasileiros.com/)
- [Design Systems Brasileiros (Marcos Pagano)](https://mppagano.medium.com/design-systems-brasileiros-1bf317f381f9)
- [DS CAIXA case (Andre Ferreira)](https://andrewallacemf.medium.com/ds-caixa-o-design-system-do-maior-banco-social-do-brasil-case-ux-ui-620941c42487)
- [Tendencias Design 2026 (Canva via Exame)](https://exame.com/marketing/as-7-tendencias-que-vao-guiar-o-design-em-2026-segundo-o-canva/)
- [BCB — Manual de Marca PIX](https://www.bcb.gov.br/estabilidadefinanceira/pix)
- [Gov.br Design System](https://www.gov.br/ds/)

### IA + Claude SVG generation

- [Claude SVG via Artifacts (SVG Genie)](https://www.svggenie.com/blog/create-svg-with-claude-ai)
- [Logo Designer Skill for Claude Code (Jeremy Watt)](https://neonwatty.com/posts/logo-designer-skill-claude-code/)
- [Claude Design — Build a Brand from Scratch (MindStudio)](https://www.mindstudio.ai/blog/how-to-use-claude-design-build-brand)
- [Stop Hunting for Icons — AI Generated SVGs (DEV)](https://dev.to/albert_nahas_cdc8469a6ae8/how-i-built-an-mcp-server-for-ai-icon-generation-and-why-you-need-one-44b4)
- [Generate Icons in Cursor and Claude Code (AI Rabbit / Medium)](https://medium.com/@airabbitX/generate-awesome-icons-inside-cursor-claude-code-without-leaving-the-ide-cd057f72ad54)
- [icon-set-generator skill (explainx)](https://explainx.ai/skills/jezweb/claude-skills/icon-set-generator)
- [Logo Creator Claude Code Skill (mcpmarket)](https://mcpmarket.com/tools/skills/logo-creator-1)
- [Drawing and Animating with Claude (Ola Hungerford)](http://www.olahungerford.com/drawing-and-animating-with-claude/)

### Tooling

- [SVGO](https://github.com/svg/svgo) — SVG optimizer
- [svg-sprite](https://github.com/svg-sprite/svg-sprite) — sprite generator
- [vite-plugin-svg-icons](https://github.com/vbenjs/vite-plugin-svg-icons)
- [svg-symbol-sprite-loader](https://github.com/crystal-ball/svg-symbol-sprite-loader)
- [Storybook](https://storybook.js.org/)
- [webpack-bundle-analyzer](https://github.com/webpack-contrib/webpack-bundle-analyzer)
- [rollup-plugin-visualizer](https://github.com/btd/rollup-plugin-visualizer)

### Acessibilidade

- [WAI-ARIA Authoring Practices — Icons](https://www.w3.org/WAI/ARIA/apg/)
- [WCAG 2.2 Quick Reference](https://www.w3.org/WAI/WCAG22/quickref/)
- [Accessible SVG Icons (CSS-Tricks)](https://css-tricks.com/accessible-svg-icons/)

### Brand guidelines de terceiros (logos)

- [X Brand Toolkit](https://about.x.com/en/who-we-are/brand-toolkit)
- [Meta Brand Resources](https://about.meta.com/brand/resources/)
- [Google Brand Resource Center](https://about.google/brand-resource-center/)
- [Apple Identity Guidelines](https://developer.apple.com/design/human-interface-guidelines/)
- [Simple Icons](https://simpleicons.org/) — logos de marcas (CC0 mas marcas tem trademark proprio)

---

## Cross-Skill References

- **`svg-engineering-ia`** (CRITICO — base ferramental geracao SVG): viewBox, paths, optimization, geracao via Claude. Iconografia depende dessa skill para a parte tecnica.
- **`logo-design-process`**: logo da marca e ponto de partida estilistico — line weight, terminations, mood do logo informam mood dos icones.
- **`brand-book-methodology`**: brand book documenta WHEN ICON vs ILLUSTRATION vs PHOTO, regras de uso, do/dont.
- **`paleta-cores-corporativa`**: icones herdam paleta via currentColor; duotone usa cor primaria + secundaria do sistema.
- **`tipografia-corporativa`**: line weight do icone tem que dialogar com weight da tipografia (font-weight 400 = stroke 1.5px, 500 = 2px, 600 = 2.5px regra heuristica).
- **`design-system-basico`**: icones sao tokens visuais ao lado de cor, tipografia, espacamento, sombra.
- **`microcopy`**: icone + label de texto e dupla — microcopy define quando label e obrigatoria.
- **`acessibilidade-wcag`**: aria-label, aria-hidden, contrast ratio em icones interativos.
- **`fotografia-corporativa-direcao-arte`**: estilo fotografico e estilo iconografico devem dialogar (mood unico).
- **`marca-pessoal-personal-branding`**: avatares pessoais nao sao iconografia — disciplina separada.

---

## Integracao Ecossistema Frank-MKT

5a SKILL do Bloco "Identidade Visual Corporativa / Brand Design" do plugin frank-mkt.

Fluxo recomendado para um brand redesign completo:

1. `posicionamento-marca` -> definir territorio
2. `naming-marca` -> nome
3. `paleta-cores-corporativa` -> sistema cromatico
4. `tipografia-corporativa` -> sistema tipografico
5. `logo-design-process` -> marca grafica
6. **`iconografia-corporativa` (esta skill)** -> sistema de icones
7. `brand-book-methodology` -> consolidacao
8. `design-system-basico` -> componentizacao
9. `svg-engineering-ia` -> ferramental tecnico transversal
10. `microcopy` + `acessibilidade-wcag` -> camada UX

Esta skill consome inputs de #2-5 e gera output que alimenta #7-8. E uma das skills mais "tecnicas" do bloco brand — meio caminho entre design e engenharia.

Frank-MKT plugin: 84 skills no total (10 BLOCOS), foco em marketing, brand, conteudo, growth, dados, IA, juridico-marketing, infra. Esta skill cobre iconografia em profundidade que skills generalistas de design system nao cobrem.

---

## Disclaimer

Este material e educacional e referencia praticas conhecidas em 2026. NAO substitui:
- contratacao de brand designer / design system lead profissional para projetos de longo prazo;
- analise legal de licencas de icone libs e trademarks de terceiros — sempre valide com juridico antes de usar logos de marcas (PIX, X, Meta, etc) em produto;
- auditoria de acessibilidade real (WCAG 2.2) com ferramentas e testes com usuarios assistivos;
- testes de usabilidade reais com publico-alvo (free association testing, A/B em creatives).

Estatisticas (numero de icones por lib, market share, downloads npm) podem variar — sempre consulte a fonte oficial no momento do uso. Licencas mudam — valide MIT/Apache/CC0 atual no repositorio oficial. URLs de DS brasileiros e cases corporativos podem mudar — verifique se o link esta vivo antes de citar em apresentacao para cliente.

Iconografia e disciplina de oficio: ler cabe em horas, dominar exige anos de iteracao em produtos reais. Esta skill e ponto de partida solido, nao chegada.
