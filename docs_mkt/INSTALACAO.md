# Instalação Frank-MKT

Guia de instalação validado em 2026-05-11 (v2.39.2) — testado e funcional.

## Pré-requisitos

- Claude Code instalado (versão May 2026+)
- Git configurado
- Acesso ao GitHub público

## Instalação passo a passo

### 1. Adicionar marketplace

```powershell
claude plugin marketplace add https://github.com/alexandrejalkh/frank-mkt.git
```

Output esperado:
```
Refreshing marketplace cache (timeout: 120s)…
Cloning repository (timeout: 120s): https://github.com/alexandrejalkh/frank-mkt.git
Clone complete, validating marketplace…
Cleaning up old marketplace cache…
√ Successfully added marketplace: frank-mkt (declared in user settings)
```

### 2. Instalar plugin

```powershell
claude plugin install frank-mkt --scope project
```

`--scope project` instala apenas no projeto atual. Para instalar globalmente, use `--scope user`.

### 3. Abrir Claude Code no projeto

```powershell
claude
```

### 4. Inicializar configuração do cliente/marca

Dentro do Claude Code:

```
/frank-mkt:init [nome-cliente]
```

Cria estrutura `.frank-mkt/` no projeto com pastas:
- `marca/` — identidade + voice/tone + visual
- `persona/` — ICP + JTBD
- `campanhas/` — campanhas ativas
- `decisoes/` — log decisões + ADRs
- `entregaveis/` — copy + visual + decks + docs
- `pesquisa/` — concorrência + trends

## Verificar instalação

```
/frank-mkt:help
```

Deve listar:
- 10 slash commands (inclui `/frank-mkt:atelier` + `/frank-mkt:gerar-infografico`)
- 16 agentes (inclui `atelier-criativo` artista digital + `renderer-visual` operacional render-loop)
- 93 skills agrupadas em 18 blocos (Skills Avancadas 2/2: svg-engineering-ia + render-loop-svg)

## Atualização

Quando uma nova versão estiver disponível:

```powershell
# Atualizar cache do marketplace
claude plugin marketplace update frank-mkt

# Atualizar o plugin
claude plugin update frank-mkt
```

## Resolução de problemas

### Erro: "Marketplace file not found at .claude-plugin/marketplace.json"

**Causa**: cache local desatualizado ou repo sem `marketplace.json`.

**Solução**:
```powershell
claude plugin marketplace remove frank-mkt
claude plugin marketplace add https://github.com/alexandrejalkh/frank-mkt.git
```

### Erro: "This plugin uses a source type your Claude Code version does not support"

**Causa 1**: Claude Code desatualizado.
```powershell
claude update
```

**Causa 2**: Cache local com `marketplace.json` antigo (após nós atualizarmos o repo).
```powershell
claude plugin marketplace remove frank-mkt
claude plugin marketplace add https://github.com/alexandrejalkh/frank-mkt.git
```

### Erro: "Failed to clone repository: git@github.com Permission denied (publickey)"

**Causa**: Claude Code tentando clonar via SSH ao invés de HTTPS (formato `source` antigo no marketplace.json).

**Solução**: aguardar fix no repo (já corrigido em v2.32.0+) ou reportar issue.

## Remoção

```powershell
# Desabilitar (mantém arquivos)
claude plugin disable frank-mkt

# Desinstalar (remove arquivos)
claude plugin uninstall frank-mkt

# Remover marketplace
claude plugin marketplace remove frank-mkt
```

O diretório `.frank-mkt/` no seu projeto **NÃO é removido** automaticamente — preserva contexto do cliente. Remova manualmente se desejar:

```powershell
Remove-Item -Recurse -Force .frank-mkt
```

## Estrutura do repo (referência)

Plugin segue padrão Claude Code marketplace canônico:

```
frank-mkt/                              # GitHub repo root
├── .claude-plugin/
│   └── marketplace.json                # Marketplace manifest
├── README.md                           # Visitors GitHub
├── docs_mkt/
│   ├── ROADMAP-FRANK-MKT.md
│   └── INSTALACAO.md (este arquivo)
└── frank-mkt-plugin/                   # Plugin em subpasta dedicada
    ├── .claude-plugin/
    │   └── plugin.json
    ├── CHANGELOG.md
    ├── settings.json
    ├── skills/                         # 93 skills (18 blocos)
    ├── commands/                       # 10 slash commands (inclui /atelier + /gerar-infografico)
    ├── agents/                         # 16 agentes (inclui atelier-criativo + renderer-visual)
    └── hooks/                          # SessionStart check-skills-vencidas
```

## Suporte

- **Issues**: https://github.com/alexandrejalkh/frank-mkt/issues
- **Roadmap**: [ROADMAP-FRANK-MKT.md](ROADMAP-FRANK-MKT.md)
- **Changelog**: [../frank-mkt-plugin/CHANGELOG.md](../frank-mkt-plugin/CHANGELOG.md)

## Versão

**v2.39.2** (2026-05-11) — Plugin: 93 skills (19 blocos) + 10 commands + 16 agentes = **119 artefatos**. v2.39.0 implementou CI lint. v2.39.1 endureceu lint. **v2.39.2 e meta-meta-fix**: auditoria pos-v2.39.1 detectou 3 drifts adicionais (README.md raiz congelado em v2.35.0, help.md "18 blocos" mas tem 19, marketplace narrativa stale). v2.39.2 corrige + adiciona README.md raiz ao lint VERSION_FILES + adiciona check_block_count_consistency contando `### Bloco N` headers vs declaracoes "X blocos". 5 ciclos de drift na sessao -- o lint cresceu de 5 checks (v2.39.0) para 9 checks (v2.39.2) atraves de auditoria iterativa.
