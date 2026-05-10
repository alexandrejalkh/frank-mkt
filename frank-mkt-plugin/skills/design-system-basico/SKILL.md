---
name: design-system-basico
description: Design Systems fundamentos (design tokens W3C standard + component libraries + Material Design 3 + Apple HIG + Carbon IBM + Polaris Shopify + atomic design Brad Frost + Storybook + Figma libraries) para founders/PMs/designers/devs/agencias, com cobertura W3C Design Tokens Format Module 2024 + Tokens Studio + Style Dictionary + Brasil cases (Nubank Cantarell + Magalu MagaluUI + Itau ItauDesignSystem + Stone) + ROI medido (50% faster shipping enterprise + brand consistency). FECHA Bloco UX/UI 4/4.
volatility: medium
last_review: 2026-05-09
next_review: 2026-11-09
languages: [pt-BR]
audience: [founders, PMs, designers, devs, agencias, design-leads, design-ops]
ascii_only: true
---

# Skill: design-system-basico

Skill educacional sobre Design Systems aplicados a marketing, produto e operacao
de marca. Foco em fundamentos perenes (atomic design, tokens, governanca) com
camada Brasil 2026 (Nubank Cantarell, Magalu UI, Itau Design System, Stone) e
mensuracao de ROI baseada em estudos publicos. Esta skill FECHA o Bloco UX/UI
(skill 4/4), formando quarteto com ux-heuristicas, microcopy e
acessibilidade-wcag.

Disclaimer: conteudo educacional. Nao substitui design lead, design ops manager
ou consultoria especializada de DS. Numeros de ROI variam por organizacao,
maturidade e adocao real. Use como ponto de partida, nao como promessa.

## Decaimento Temporal

- volatility: medium
- last_review: 2026-05-09
- next_review: 2026-11-09

Componentes que envelhecem RAPIDO (revisar a cada 6 meses):
- Versao do W3C Design Tokens Format Module (2025.10 estavel; novas drafts).
- Versao majors de Material Design (M3 hoje; M4 pode chegar).
- Apple HIG visionOS / iOS / macOS (Apple atualiza a cada WWDC).
- Carbon IBM (versoes major + tokens v11+).
- Storybook majors (8.x atual; addons mudam).
- Figma features (Variables, Code Connect, Dev Mode, Make Designs).
- Tokens Studio + Style Dictionary v4 (DTCG first-class).

Componentes PERENES (revisar 12-18 meses):
- Atomic Design (Brad Frost, 2013) - estrutura de pensamento estavel.
- Hierarquia atoms/molecules/organisms/templates/pages.
- Conceito de design tokens (decisoes de design como dados).
- Padroes de governanca (centralizado, federado, hibrido).
- Princıpios de contribuicao (RFC, design-in-the-open).

Sinais para revisao antecipada:
- Nova major do W3C Tokens Spec.
- Mudanca grande em Apple HIG (novo device class).
- Material Design 4 lancado.
- Caso publico de DS no Brasil ganha tracao (livro, palestra, repo).

## Visao Geral

Um Design System (DS) e um produto interno que serve outros produtos. Nao e
biblioteca de componentes nem style guide isolado. E a uniao de:

1. Principios e valores de marca (linguagem visual + tom + voz).
2. Design tokens (decisoes de design como dados versionados).
3. Componentes (UI reutilizavel, codigo + design + docs).
4. Padroes (formularios, navegacao, feedback, layout).
5. Documentacao (uso, do/dont, acessibilidade, tokens).
6. Governanca (quem decide, quem contribui, como evolui).
7. Ferramentas (Figma, Storybook, pipeline de tokens).
8. Times (DS team, contribuidores, consumidores).

Para founders/PMs: DS e investimento que paga em escala (3+ produtos, 5+
designers, 10+ devs front). Abaixo desse limite, custo de manutencao do DS
pode superar beneficio. Para agencias: DS e entregavel premium e moat
defensavel.

Promessa desta skill: dar mapa mental para conversar com designers, contratar
DS lead, avaliar fornecedor, ler PR de componente e entender por que tokens
importam para marketing (consistencia de marca em emails, landing pages,
dashboards, app, comunicacao externa).

## Fundacao 1 - Atomic Design + Estrutura de Pensamento

Brad Frost publicou Atomic Design em 2013 (livro online gratuito em
atomicdesign.bradfrost.com). E a metafora mais adotada para estruturar DS.

Hierarquia de cinco niveis:

1. Atoms (atomos): elementos basicos indivisiveis.
   - Botao, label, input, icone, cor, tipografia, sombra.
   - Sozinhos, pouca utilidade. Combinados, formam tudo.

2. Molecules (moleculas): grupos pequenos de atoms com proposito.
   - Search field (label + input + button).
   - Form field (label + input + helper text + error).
   - Card header (avatar + nome + timestamp).

3. Organisms (organismos): grupos complexos de moleculas/atoms.
   - Header de site (logo + nav + busca + CTA).
   - Lista de produtos (cards repetidos).
   - Formulario completo (multiplos form fields + submit).

4. Templates: layout de pagina sem conteudo real.
   - Estrutura de dashboard (sidebar + main + topbar).
   - Estrutura de checkout (steps + form + summary).

5. Pages: instancia real de template com conteudo real.
   - Dashboard do usuario X com dados reais.
   - Checkout do produto Y com preco real.
   - Page e onde se valida se template funciona.

Importante: ordem nao e rigida nem estritamente bottom-up. Frost defende que se
projeta em movimento (atoms <-> molecules <-> pages). Comecar por pages e
extrair atoms tambem e valido.

Distincao critica:
- Component library = colecao de componentes reusaveis (codigo).
- Pattern library = colecao de padroes documentados (uso).
- Style guide = principios visuais e de marca.
- Design system = TUDO acima + governanca + tokens + docs + time.

DS sem governanca e zoo. DS sem adocao e museu.

## Fundacao 2 - Design Tokens + W3C Standard

Design tokens sao decisoes de design armazenadas como dados estruturados (JSON
geralmente). Saem do Figma/Photoshop e viram codigo consumivel por web, iOS,
Android, email, print.

Marco 2025: W3C Design Tokens Community Group (DTCG) publicou primeira versao
estavel do Design Tokens Format Module em outubro de 2025 (versao 2025.10).
Implementacoes de referencia em Style Dictionary (Amazon, v4 com first-class
DTCG support), Tokens Studio (Figma plugin), Terrazzo, alem de suporte em
Penpot, Sketch, Framer, Knapsack, Supernova, zeroheight.

Tipos canonicos de token (DTCG spec):
- color (hex, rgb, hsl, modern color spaces).
- dimension (px, rem, em).
- fontFamily, fontWeight, fontSize.
- duration (ms, s).
- cubicBezier (easing).
- shadow (composite).
- gradient.
- border.
- typography (composite).
- transition (composite).

Niveis de token (escala mais usada):

1. Primitive / global tokens.
   - color.blue.500 = #2563eb
   - spacing.4 = 16px
   - Cor crua, sem contexto.

2. Semantic / alias tokens.
   - color.text.primary = {color.gray.900}
   - color.bg.brand = {color.blue.500}
   - Dao significado, permitem theming.

3. Component tokens.
   - button.primary.bg = {color.bg.brand}
   - button.primary.text = {color.text.inverse}
   - Especificos de componente.

Beneficio cascata: trocar primary brand color = mudar 1 token primitive,
propagar para semantic, propagar para component, atualizar todos os produtos.

Pipeline tipico:
- Designer edita tokens no Figma via Tokens Studio plugin.
- Plugin exporta JSON DTCG-compliant para Git.
- Style Dictionary transforma JSON em CSS, iOS Swift, Android XML, JS, etc.
- CI publica artifacts versionados.
- Times consomem via npm package, CocoaPods, Maven.

Exemplo JSON DTCG simplificado:

```
{
  "color": {
    "brand": {
      "primary": {
        "$value": "#820AD1",
        "$type": "color",
        "$description": "Nubank purple - cor principal de marca"
      }
    }
  }
}
```

Risco comum: tratar tokens como features de Figma e nao como contrato de marca.
Sem versionamento semver e changelog, tokens viram chaos.

## Fundacao 3 - Component Libraries Maturos (Benchmarks)

Estudar DS publicos = atalho para nao reinventar. Sete benchmarks essenciais:

1. Material Design 3 (Google, material.io).
   - Open source, foco Android + cross-platform.
   - Material You: personalizacao dinamica baseada em wallpaper.
   - Tokens: M3 introduz tokens hierarquicos formais.
   - Bom para: apps consumer, Android-first, branding adaptativo.

2. Apple Human Interface Guidelines (developer.apple.com/design).
   - Guidelines, nao biblioteca de codigo (UIKit/SwiftUI sao a impl).
   - Cobre iOS, iPadOS, macOS, watchOS, tvOS, visionOS.
   - Foco em comportamento + interacao + sensacao "nativa".
   - Bom para: apps iOS/macOS, premium feel, padroes Apple.

3. Carbon Design System (IBM, carbondesignsystem.com).
   - Open source, foco enterprise + data-heavy.
   - Tokens v11+, multiplos themes (white, g10, g90, g100).
   - React, Vue, Angular, Svelte, Web Components.
   - Bom para: B2B SaaS, dashboards, ferramentas internas.

4. Polaris (Shopify, polaris.shopify.com).
   - Open source, foco e-commerce admin.
   - Forte em accessibility e consistency narrativa.
   - React + design tokens + Figma library.
   - Bom para: apps admin, ferramentas operacionais, marketplaces.

5. Lightning Design System (Salesforce, lightningdesignsystem.com).
   - Foco CRM, formularios complexos, listas, tabelas densas.
   - Bom para: B2B enterprise, workflows internos.

6. Atlassian Design System (atlassian.design).
   - Foco produtividade colaborativa (Jira, Confluence, Trello).
   - Bom para: ferramentas de produtividade, multi-product DS.

7. Spectrum (Adobe, spectrum.adobe.com).
   - Foco apps criativos, dark mode primeiro.
   - Tokens cross-platform, React Spectrum.
   - Bom para: ferramentas criativas, profundidade de UI.

Bonus 2026:
- Fluent (Microsoft, fluent2.microsoft.design): cross-platform M365.
- Mantine, Radix UI, shadcn/ui: open source bundles para times pequenos.
- Ant Design (Alibaba): foco enterprise China, popular global.

Para founders: NAO reinvente do zero. Forke um benchmark proximo do seu
contexto e itere.

## Fundacao 4 - Storybook + Documentation + Figma Libraries

Storybook (storybook.js.org) e ferramenta padrao de mercado para documentar e
desenvolver componentes em isolamento. Versao 8+ atual (2026), com addons para
acessibilidade, design tokens, testes visuais, integracao Figma.

Stack tipica de docs DS 2026:

1. Storybook 8+ como playground de componentes.
   - Cada componente vira "story" (exemplo isolado com props).
   - Addons: a11y (axe-core), interactions, viewport, themes, design.

2. Chromatic (chromatic.com) para visual regression testing.
   - Cada PR gera snapshot visual, compara com main.
   - Aprovacao humana para mudancas intencionais.

3. Zeroheight (zeroheight.com) ou Supernova (supernova.io) para docs textuais.
   - Wiki de DS com guidelines, principles, tokens, do/dont.
   - Conecta Figma + Storybook + GitHub.

4. Figma Libraries para fonte de verdade visual.
   - Components publicados, variants, properties, auto-layout.
   - Variables (Figma) sincronizadas com tokens via plugins.

5. Code Connect (Figma, 2024+) para conectar componente Figma ao codigo.
   - Dev Mode mostra snippet real do componente Storybook.
   - Reduz drift design <-> codigo.

Padroes de doc por componente (boilerplate minimo):

- Description (1 paragrafo: o que e, quando usar).
- Props / API (tabela com nome, tipo, default, descricao).
- Examples (3-5 stories: padrao, edge case, com erro).
- Do (3-5 boas praticas).
- Dont (3-5 antipattern).
- Accessibility notes (WCAG, ARIA, keyboard, screen reader).
- Related components (link para siblings).
- Changelog (versoes + breaking changes).

Anti-pattern: docs em PDF estatico. Vira folclore no segundo mes.

Plugins Figma essenciais 2026 (curadoria):
- Tokens Studio for Figma (tokens DTCG).
- Story.to.design (importa Storybook -> Figma).
- Figma Variables Connect.
- Iconify (icones).
- Stark (acessibilidade no Figma).
- Able (accessibility checker).

## Fundacao 5 - Governanca + Adocao + Design Ops

DS so cumpre promessa se for adotado. Adocao depende de governanca.

Tres modelos de governanca:

1. Centralized (centralizado).
   - Time dedicado de DS controla tudo.
   - Pros: consistencia maxima, qualidade alta.
   - Contras: bottleneck, lento, distante dos consumidores.
   - Bom para: organizacoes pequenas-medias, fase inicial.

2. Federated (federado).
   - Time core pequeno + contribuidores em squads.
   - Pros: escala, ownership distribuido, velocidade.
   - Contras: precisa governanca clara, risco de fragmentacao.
   - Bom para: enterprises grandes, multi-produto.

3. Hybrid (hibrido).
   - Core team mantem foundations + tokens + componentes core.
   - Squads contribuem padroes especificos via RFC.
   - Pros: balanco entre velocidade e consistencia.
   - Bom para: maioria das organizacoes maduras.

Estrutura tipica de DS team:
- DS Lead / Manager (1).
- Designers DS (1-3).
- Engineers DS (2-5).
- Design Ops / Program Manager (1).
- Accessibility specialist (0-1, ideal).
- Tech writer / docs (0-1, ideal).

Para founders: DS team comeca com 0 pessoas dedicadas, depois 1 designer +
1 dev part-time, depois 3-5 dedicados quando organizacao tem 50+ pessoas em
produto.

Modelo de contribuicao tipico:
- RFC (Request for Comments) para mudanca grande.
- Design-in-the-open via Figma compartilhado + Slack channel.
- PR padrao para mudanca pequena (token, componente novo simples).
- Office hours semanais do DS team para duvidas.
- Design review obrigatorio para componente novo entrar no DS.

Versionamento: semver (semver.org).
- Major (X.0.0): breaking change (renomeia token, remove componente).
- Minor (1.X.0): adiciona componente / token sem quebrar.
- Patch (1.0.X): bug fix.

Migration guides obrigatorios em majors.

Adocao - metricas para acompanhar:
- % de telas que usam componentes DS (vs custom).
- Tempo medio para shipping de feature nova.
- Numero de duplicatas detectadas (componente custom = sintoma).
- NPS do DS entre devs e designers consumidores.
- Cobertura de tokens em produtos.

## Fundacao 6 - Brasil 2026 (Nubank/Magalu/Itau cases + ABCDesign + UX Brasil)

Brasil tem cena madura de DS, com cases publicos e comunidade ativa.

1. Nubank - NuDS (Nu Design System).
   - Atende Brasil, Mexico, Colombia.
   - 100+ componentes reutilizaveis.
   - Acessibilidade prioritaria (Figma case publico).
   - Cantarell e tipografia/iniciativa de tipografia historicamente associada.
   - NuIS 3.0 (Nubank Illustration System): evolucao de cartoonish para sleek.
   - Building Nubank blog (building.nubank.com/design) publica casos.
   - Aprendizado: DS multi-pais exige tokens de moeda, formato data,
     numero, traducao, sem perder consistencia visual.

2. Magazine Luiza - MagaluUI.
   - Open source historicamente (verificar status atual).
   - Foco e-commerce + super app.
   - Multiplos squads consumidores (logistica, fintech, marketplace).
   - Aprendizado: DS de e-commerce precisa lidar com altıssimo volume de
     templates de produto, categorias, promocoes.

3. Itau - Itau Design System.
   - Foco bancario + multi-produto (app, internet banking, ferramentas
     internas).
   - Aprendizado: DS bancario tem regulatorio (Bacen), acessibilidade Lei
     Brasileira de Inclusao, alta densidade informacional.

4. Stone - Stone Design System.
   - Foco maquininha + adquirencia + banking PJ.
   - Aprendizado: DS para hardware (display da maquininha) + mobile + web.

5. Outros relevantes:
   - PicPay, iFood, Mercado Livre, B3, Globo, Hotmart - todos com DS
     internos, alguns com pecas publicas.

Comunidade Brasil:
- ABCDesign (abcdesign.com.br): conferencia anual.
- UX Brasil: comunidade grande no Slack/Discord.
- Brasileiros Criando (canal YouTube): casos.
- Front-end SP, ReactSP, Frontin: meetups regionais.
- Medium tags ux-brasil, design-system, designsystems.

Particularidades brasileiras a considerar:
- Conexao instavel: DS deve funcionar offline-first / lazy load.
- Devices low-end ainda relevantes: performance budget rigido.
- Acessibilidade: NBR 17225 / 17060 + Lei Brasileira de Inclusao
  (referenciar skill acessibilidade-wcag).
- LGPD: tokens nao guardam PII, mas componentes de form devem orientar
  consentimento (referenciar skill acessibilidade-wcag e microcopy).
- Multi-marca: holdings tem varias marcas (Itau Unibanco, IUPP, ION).

## Fundacao 7 - Mensuracao + Tools 2026

Stack canonica de DS em 2026:

Design + Tokens:
- Figma + Variables (fonte de verdade visual).
- Tokens Studio for Figma (DTCG-compliant).
- Style Dictionary v4 (transforma tokens para plataformas).
- Terrazzo (alternativa Style Dictionary).

Componentes + Codigo:
- Storybook 8+ (playground + docs).
- Chromatic (visual regression).
- Stark / Able (acessibilidade Figma).
- axe-core (acessibilidade runtime).

Documentacao:
- Zeroheight (wiki design system).
- Supernova (wiki + tokens + integration).
- Knapsack (DS platform).
- Backlight.dev (DS platform).

Governanca:
- GitHub / GitLab (RFC, PR, issues).
- Linear / Jira (roadmap DS).
- Notion / Confluence (docs internos).

CI/CD:
- GitHub Actions / GitLab CI.
- npm / Yarn / pnpm registries.
- Semantic-release (versionamento automatico).

ROI - dados publicos relevantes (sempre validar):

- Forrester (estudo classico): ate 671% ROI em DS, $100M revenue por
  $1M investido (caso especifico, nao garantia).
- Empresas 100+ funcionarios: 46% reducao em custos de design+dev,
  22% time-to-market mais rapido (relatos publicos agregados).
- Knapsack ROI Calculator: estima save baseado em head-count + numero
  de produtos.
- Figma 2024 report on DS ROI: dev time saving + brand consistency.

Modelo de calculo simplificado (ano):
- N = numero de devs front + designers consumidores.
- T = horas/ano por pessoa.
- S = % de tempo economizado com DS (10-30% e razoavel).
- C = custo medio hora (R$ 80-200).
- Save = N * T * S * C.

Exemplo: 30 devs * 1.800h * 0.20 * R$ 150 = R$ 1.620.000/ano.
Custo de DS team de 4 pessoas: ~R$ 1.200.000/ano.
ROI: positivo no ano 2 em diante (ano 1 e investimento).

Anti-pattern: justificar DS so com ROI quantitativo. Beneficios qualitativos
(brand consistency, accessibility compliance, retention de talentos)
importam tanto quanto.

## Fundacao 8 - Aplicacao em Content MKT (5 audiencias)

DS impacta marketing diretamente. Cinco audiencias, cinco angulos:

1. Founder / CEO (early-stage).
   - Pergunta: "preciso de DS agora?"
   - Resposta: NAO se equipe < 5 designers/devs front. SIM se
     vai escalar para 3+ produtos.
   - Atalho: forke shadcn/ui ou Mantine + Tokens Studio. Itere.
   - Foco MKT: consistencia entre landing page, app, email transacional,
     onboarding. Nao mais "Frankenstein de templates Wix".

2. PM / Product Lead.
   - Pergunta: "como acelero shipping?".
   - Resposta: DS bem adotado reduz 20-30% tempo de feature.
   - Padrao: cada feature nova consome 70% DS, 30% custom.
   - Foco MKT: feature funnel mais rapido = mais experimentos = mais
     aprendizado.

3. Designer.
   - Pergunta: "como saio do Figma para producao sem drift?".
   - Resposta: tokens + Figma Variables + Code Connect + Storybook.
   - Foco MKT: design system como portfolio (case study real, nao mock).
     Recrutamento de designers melhora.

4. Dev front-end.
   - Pergunta: "como evito reescrever botao 8x?".
   - Resposta: DS package + Storybook + tipos TypeScript exportados.
   - Foco MKT: contratacao de devs facilita. Onboarding de dev novo
     cai de semanas para dias.

5. Agencia / consultoria.
   - Pergunta: "como entrego DS como produto?".
   - Resposta: kit padrao (Figma library + tokens + Storybook seed +
     governanca template). Customiza por cliente.
   - Foco MKT: DS como entregavel premium (R$ 80-300k projeto). Moat
     defensavel, recorrencia de manutencao.

Para todos: MKT precisa de tokens proprios (cor de campanha, fonte de
hero, espacamento de email). Sem isso, MKT vira "ilha visual" e marca
fragmenta.

## Anti-Patterns 18

1. DS sem governanca - vira zoo, ninguem responde.
2. DS sem adocao - museu, ninguem usa.
3. DS sem versionamento - upgrade quebra producao.
4. DS sem changelog - consumidores no escuro.
5. Tokens sem niveis (so primitive ou so semantic) - perde flexibilidade.
6. Tokens hardcoded em componentes - cascata de mudanca quebra.
7. Componente "kitchen sink" - 30 props, ninguem entende.
8. Componente sem variants documentadas - cada squad reinventa.
9. Storybook sem stories de edge case - bugs vazam.
10. Sem accessibility check em PR - DS e barreira ironicamente.
11. Figma library descolada do codigo - drift permanente.
12. DS team isolado, sem office hours - virou torre de marfim.
13. RFC sem deadline - decisoes ficam em limbo eterno.
14. Forkar M3/Carbon e nao customizar marca - produto generico.
15. DS so para web, ignora email/print/iOS - inconsistencia cross-channel.
16. Sem token de moeda/data/numero em DS multi-pais - localizacao quebra.
17. Documentacao em PDF / wiki interna estatica - ninguem le.
18. Justificar DS so com ROI quantitativo - ignora brand + a11y + talento.

## 18 Regras de Ouro

1. DS e produto interno. Trate como tal (roadmap, OKRs, metrics).
2. Comece com tokens primitive + 5-10 componentes core.
3. Use W3C Design Tokens Format Module (DTCG) desde dia 1.
4. Forke benchmark (Carbon/Polaris/Material) em vez de criar do zero.
5. Adote Storybook 8+ como playground oficial.
6. Conecte Figma <-> codigo via Variables + Code Connect.
7. Versione com semver e publique changelog em todo release.
8. Acessibilidade e gate, nao add-on (axe-core no CI).
9. Cada componente: docs + props + 3-5 stories + a11y notes.
10. Governanca: defina centralized/federated/hybrid no comeco.
11. RFC publico para mudanca grande, PR para mudanca pequena.
12. Office hours semanais do DS team obrigatorias.
13. Meca adocao (% telas com DS) e velocidade (time-to-ship).
14. NPS interno do DS a cada trimestre.
15. Migration guide obrigatorio em toda major.
16. MKT tem tokens de campanha que herdam de tokens base.
17. Cross-channel: cobre web + email + iOS + Android + print.
18. Inclua a11y, microcopy e ux-heuristicas como sister-skills do DS.

## Exemplos Comportamentais

Quatro personas, quatro situacoes reais.

### Persona 1: Founder fintech B brasileira (15 pessoas, serie seed)

Situacao: tem app mobile + landing + back office. Usa shadcn/ui no front,
Figma com bagunca, sem tokens.

Pergunta: "preciso contratar designer de DS?".

Resposta da skill:
- Nao, ainda nao. Time pequeno demais para DS team dedicado.
- Acao 1: organizar Figma com Variables + Tokens Studio (1 designer
  existente pode fazer, ~2 semanas).
- Acao 2: definir 12-15 tokens primitive (color, spacing, typography,
  shadow) e 8-10 semantic.
- Acao 3: adicionar Storybook ao projeto front (2-3 dias dev senior).
- Acao 4: documentar 10 componentes top-of-mind no Storybook.
- Acao 5: revisitar em 6 meses ou quando contratar 2o designer.
- Custo: ~R$ 30-50k de tempo interno, sem hire novo.
- ROI esperado: consistencia entre app+landing, 15-20% velocidade extra
  em features.

### Persona 2: PM SaaS B2B (200 pessoas, 3 produtos, serie B)

Situacao: 3 produtos com DS divergentes, devs reclamando, brand sem
consistencia, NPS interno baixo.

Pergunta: "vale criar DS team unificado?".

Resposta:
- Sim. Estagio classico de "DS unification".
- Acao 1: hire DS Lead (designer senior + experiencia DS, ~6 meses).
- Acao 2: hire 1 designer DS + 2 engineers DS dedicados.
- Acao 3: auditar 3 produtos, criar matriz de overlap (componentes
  duplicados).
- Acao 4: lancar v1 com 20-25 componentes core + tokens shared.
- Acao 5: roadmap 12 meses para migrar 3 produtos para DS unificado.
- Acao 6: adotar Carbon ou Polaris como base (forkar) se contexto bate.
- Acao 7: governanca hibrida (core team + RFC + contribuicao squads).
- Custo: ~R$ 2-3M/ano (4 pessoas + tooling).
- ROI esperado ano 2-3: 25-40% time-to-ship, 50% reducao de retrabalho
  visual, brand consistency mensuravel.

### Persona 3: Designer senior contratada como DS Lead em e-commerce

Situacao: chega em empresa de 500 pessoas, 5 squads, DS legado de 2020
abandonado, consumidores frustrados.

Pergunta: "por onde comeco em 90 dias?".

Resposta:
- Dias 1-15: discovery. Entrevistas com 20 consumidores (designers, devs,
  PMs). Mapear dores. Auditar DS legado. Identificar quick wins.
- Dias 15-30: estrategia. Definir vision + roadmap + governanca + time
  necessario. Apresentar a stakeholders. Garantir budget.
- Dias 30-60: foundations. Refatorar tokens (DTCG). Fork de Polaris ou
  Carbon como base se aplicavel. Definir 10 componentes prioritarios para
  refazer.
- Dias 60-90: shipping inicial. Lancar v2 com tokens + 8-10 componentes.
  Rodar piloto com 1 squad. Coletar NPS.
- Dia 90+: expandir adocao. Office hours. RFC publico. Roadmap publico.
- Cuidado: nao tente "big bang rewrite". Evolucao incremental + migration
  guides.

### Persona 4: Agencia digital que entrega projetos para clientes corporativos

Situacao: agencia de 30 pessoas, entrega sites + apps. Cada projeto
recomeca do zero. Margem apertada.

Pergunta: "como uso DS como diferencial competitivo?".

Resposta:
- Acao 1: criar DS proprietario da agencia (Figma library + Storybook seed
  + tokens base) - investimento de ~3 meses de 2 pessoas.
- Acao 2: cada projeto cliente comeca com fork do DS + customizacao
  de tokens (cor, fonte, raio, sombra) = 70% economia em foundation.
- Acao 3: oferecer "DS como produto" para clientes enterprise como
  entregavel separado (R$ 80-300k projeto).
- Acao 4: contrato de manutencao mensal do DS do cliente (R$ 10-30k/mes).
- Acao 5: usar como case publico (com permissao) para atrair clientes
  similares.
- Acao 6: documentar metodologia (5-10 paginas) e usar em pitch.
- Resultado esperado: margem de projeto sobe 15-25%, ticket sobe 30-50%
  com DS premium, recorrencia entra na receita.

## Checklist Contraditorio Interno (10 perguntas)

Antes de assumir que precisa de DS ou que o seu DS atual e bom, pergunte:

1. Tenho >= 3 produtos OU >= 5 designers OU >= 10 devs front? Se NAO, DS
   talvez seja overkill.
2. Os consumidores do DS (devs, designers, PMs) usariam ou e imposicao
   top-down? Se imposicao, fadado a falhar.
3. Tenho budget para DS team dedicado por 12+ meses? Sem isso, DS regride
   para zoo em 6 meses.
4. Meus tokens seguem W3C DTCG ou estao em formato proprietario sem
   futuro? Se proprietario, planeje migracao.
5. Meus componentes Figma sao a fonte de verdade ou existem 3 versoes
   divergentes? Se divergentes, fix antes de expandir.
6. Tenho versionamento semver + changelog? Se nao, upgrade quebra
   producao silenciosamente.
7. Tenho metrica de adocao (% telas com DS, NPS, tempo de feature)?
   Sem metrica, decisao de roadmap e por achismo.
8. Acessibilidade e gate ou checklist opcional? Se opcional, DS e barreira
   para usuarios reais.
9. Marketing tem tokens proprios herdando de tokens base? Se nao, brand
   fragmenta entre produto e campanha.
10. Cross-channel (web+email+iOS+Android+print) ou so web? Se so web,
    DS resolve 30% do problema de consistencia de marca.

Se respondeu NAO em 4+ perguntas: pare, ajuste fundacoes antes de
expandir.

## Referencias

Atomic Design + fundamentos:
- [Atomic Design - Brad Frost (livro online)](https://atomicdesign.bradfrost.com/)
- [Outline Atomic Design](https://atomicdesign.bradfrost.com/outline/)
- [Atomic Design Methodology](https://atomicdesign.bradfrost.com/chapter-2/)
- [Designing Systems - Brad Frost](https://atomicdesign.bradfrost.com/chapter-1/)
- [DesignSystems.com - Brad Frost interview](https://www.designsystems.com/brad-frosts-atomic-design-build-systems-not-pages/)
- [Remarkable - Atomic Design Principles](https://remarkable.global/insights/atomic-design-principles/)
- [UXPin - 10 Essential DS Components 2026](https://www.uxpin.com/studio/blog/design-system-components/)

Design Tokens + W3C:
- [W3C Design Tokens Community Group](https://www.w3.org/community/design-tokens/)
- [W3C Tokens Spec Stable Version Announcement](https://www.w3.org/community/design-tokens/2025/10/28/design-tokens-specification-reaches-first-stable-version/)
- [Design Tokens Format Module 2025.10](https://www.designtokens.org/tr/drafts/format/)
- [Design Tokens Community Group homepage](https://www.designtokens.org/)
- [DTCG GitHub](https://github.com/design-tokens/community-group)
- [Tokens Studio for Figma docs](https://docs.tokens.studio/manage-settings/token-format)
- [Style Dictionary - DTCG support](https://styledictionary.com/info/dtcg/)
- [Style Dictionary - Design Tokens](https://styledictionary.com/info/tokens/)
- [UX Collective - Design tokens with confidence](https://uxdesign.cc/design-tokens-with-confidence-862119eb819b)
- [Zeroheight - whats new in tokens spec](https://zeroheight.com/blog/whats-new-in-the-design-tokens-spec/)

Component libraries benchmarks:
- [Material Design 3](https://m3.material.io/)
- [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/)
- [Carbon Design System (IBM)](https://carbondesignsystem.com/)
- [Polaris (Shopify)](https://polaris.shopify.com/)
- [Polaris React](https://polaris-react.shopify.com/design)
- [Lightning Design System (Salesforce)](https://www.lightningdesignsystem.com/)
- [Atlassian Design System](https://atlassian.design/)
- [Spectrum (Adobe)](https://spectrum.adobe.com/)
- [Fluent 2 (Microsoft)](https://fluent2.microsoft.design/)
- [Ant Design (Alibaba)](https://ant.design/)
- [Mantine](https://mantine.dev/)
- [Radix UI](https://www.radix-ui.com/)
- [shadcn/ui](https://ui.shadcn.com/)
- [Medium - Comparing Material 3 / Apple iOS / IBM Carbon](https://medium.com/design-bootcamp/understanding-and-comparing-design-systems-material-3-apple-ios-and-ibm-carbon-28c585f893ed)
- [Figma - 12 Design System Examples](https://www.figma.com/resource-library/design-system-examples/)
- [UXPin - 13 Best DS Examples 2026](https://www.uxpin.com/studio/blog/best-design-system-examples/)
- [DesignRush - 10 Best DS Examples 2026](https://www.designrush.com/best-designs/websites/trends/design-system-examples)
- [Backlight - Best DS Examples](https://backlight.dev/mastery/best-design-system-examples)
- [DesignSystems.surf - 11 Best DS 2026](https://designsystems.surf/articles/11-best-design-system-examples-in-2026)

Storybook + Figma + docs:
- [Storybook docs](https://storybook.js.org/docs/)
- [Storybook design integrations](https://storybook.js.org/docs/sharing/design-integrations)
- [Figma Learn - Storybook and Figma](https://help.figma.com/hc/en-us/articles/360045003494-Storybook-and-Figma)
- [Figma Code Connect Storybook](https://developers.figma.com/docs/code-connect/storybook/)
- [Steve Kinney - Integrating Figma into Storybook](https://stevekinney.com/courses/storybook/figma-in-storybook)
- [Story.to.design - Storybook to Figma guide](https://story.to.design/blog/from-storybook-to-figma)
- [Story.to.design - Best Figma plugins for DS 2026](https://story.to.design/blog/best-design-system-plugins-of-2026)
- [Supernova - Top Storybook docs examples](https://www.supernova.io/blog/top-storybook-documentation-examples-and-the-lessons-you-can-learn)
- [Escape.tech - Modern DS with Storybook + Figma](https://escape.tech/blog/escape-design-system/)
- [Parallel - Maintaining DS 2026](https://www.parallelhq.com/blog/building-maintaining-design-system)
- [Zeroheight](https://zeroheight.com/)
- [Supernova](https://www.supernova.io/)
- [Knapsack](https://www.knapsack.cloud/)
- [Backlight.dev](https://backlight.dev/)
- [Chromatic](https://www.chromatic.com/)

Governance + ROI + scaling:
- [UX Stalwarts - DS ROI](https://www.uxstalwarts.com/blog/how-scalable-design-cuts-costs-and-accelerates-growth/)
- [Knapsack - DS ROI Calculator](https://www.knapsack.cloud/calculator)
- [Netguru - ROI of DS](https://www.netguru.com/blog/roi-design-systems)
- [Dusted - Scaling DS for enterprise](https://www.dusted.com/insights/scaling-design-systems-enterprise-growth)
- [Supernova - Get Executive Buy-in](https://www.supernova.io/roi)
- [Boldare - Measuring impact of DS](https://www.boldare.com/blog/measuring-impact-of-design-system/)
- [Zeroheight - Calculating DS ROI](https://zeroheight.com/blog/calculating-the-roi-of-your-design-system/)
- [AppStudio - Real ROI of DS](https://www.appstudio.ca/blog/design-system-roi-feature-delivery-time/)
- [Figma - How to measure DS ROI](https://www.figma.com/reports/measure-design-system-roi/)
- [Reloadux - ROI of DS](https://reloadux.com/blog/roi-of-having-design-system/)

Brasil cases:
- [Figma - Nubank DS case](https://www.figma.com/customers/nubank-design-system-accessible-experiences-with-figma/)
- [Building Nubank - Design](https://building.nubank.com/design/)
- [Polar - Nubank Illustration System 3.0](https://polar.ltda/en/nubank-illustration-system-3.0)
- [Nubank Design Team](https://international.nubank.com.br/pt-br/careers/design-pt-br/)

Comunidade Brasil:
- [ABCDesign](https://abcdesign.com.br/)
- [UX Brasil](https://uxbrasil.com.br/)
- [Brasileiros Criando (YouTube)](https://www.youtube.com/c/BrasileirosCriando)

Auxiliares:
- [Semver.org](https://semver.org/)
- [GitHub - Platform Design Skills](https://github.com/ehmo/platform-design-skills)
- [Pattern Lab (Brad Frost)](https://patternlab.io/)

## Cross-Skill References

Sister skills do Bloco UX/UI (interlock direto):
- ux-heuristicas: principios de Nielsen + Krug aplicados a UX. DS bom
  segue heuristicas; DS ruim viola.
- microcopy: textos curtos de UI (botoes, errors, empty states). Sao
  tokens textuais do DS.
- acessibilidade-wcag: WCAG 2.2 + ARIA + Lei Brasileira de Inclusao.
  Acessibilidade e gate de qualquer componente DS.

Skills relacionadas (interlock indireto):
- branding: identidade visual, logos, paleta. Vira input para tokens
  primitive do DS.
- posicionamento-marca: tom de voz, narrative. Influencia microcopy
  embarcada em componentes.
- linkedin-orgs-grandes: DS rola dentro de empresas grandes; case
  studies de DS sao conteudo organico forte no LinkedIn.
- tecnicas-ia-claude-gemini-mkt: usar IA para gerar variacoes de
  componentes, draftar docs Storybook, sugerir nomes de tokens.

Quando NAO usar esta skill (use sister em vez):
- Se pergunta e so sobre acessibilidade WCAG: use acessibilidade-wcag.
- Se pergunta e so sobre texto de botao: use microcopy.
- Se pergunta e sobre identidade de marca / logo: use branding.
- Se pergunta e sobre heuristica de usabilidade isolada: use
  ux-heuristicas.

## Integracao Ecossistema Frank-MKT

Esta skill FECHA o Bloco UX/UI 4/4. Tabela do bloco completo:

| # | Skill | Foco | Status |
|---|-------|------|--------|
| 1 | ux-heuristicas | Nielsen + Krug + heuristicas perenes | OK |
| 2 | microcopy | Textos curtos de UI / botoes / errors | OK |
| 3 | acessibilidade-wcag | WCAG 2.2 + ARIA + LBI | OK |
| 4 | design-system-basico | Tokens + componentes + governanca | OK (esta) |

Bloco UX/UI 4/4 fechado. Quarteto cobre fundamentos de produto digital
para founders, PMs, designers, devs e agencias.

Macro-bloco maior (Pesquisa & Inteligencia, ja fechado em 6/6) e UX/UI
(agora 4/4) sao os dois pilares horizontais do plugin frank-mkt em 2026.

Recomendacao de leitura sequencial:
1. ux-heuristicas (fundamentos cognitivos).
2. microcopy (linguagem em UI).
3. acessibilidade-wcag (inclusao + compliance).
4. design-system-basico (estrutura + escala) - esta skill.

Trio + esta skill formam a base. Para founders/PMs/devs/agencias que
queiram capacidade plena de UX/UI sem virar designers ou contratar DS
team grande, o Bloco UX/UI completo da o vocabulario, o checklist e os
benchmarks necessarios.

---

Disclaimer: este material e educacional. Numeros de ROI, casos publicos
e benchmarks variam por organizacao, contexto, maturidade e adocao real.
Nao substitui design lead, DS lead, design ops manager ou consultoria
especializada. Use como mapa mental, nao como verdade absoluta. Dados de
empresas brasileiras (Nubank, Magalu, Itau, Stone) sao baseados em
fontes publicas; situacao interna pode diferir. W3C Design Tokens Format
Module evolui; verificar versao corrente em designtokens.org. Material
Design, Apple HIG, Carbon, Polaris evoluem por seus mantenedores;
verificar docs oficiais antes de implementar.
