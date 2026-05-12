#!/usr/bin/env python3
"""
CI lint cross-artifact para frank-mkt.

Detecta drift documental entre artefatos correlatos do plugin. Filesystem +
plugin.json sao ground truth. Outros arquivos correlatos devem refletir esses
valores. Mede contagens, versao, auto-contradicao mid-file, cross-refs,
frontmatter, ASCII compliance.

Background: 3 ciclos de drift em uma sessao (v2.32->v2.35, v2.37.0, v2.38.0)
provaram que disciplina humana nao previne esse vetor. Este script preveni
mecanicamente.

Uso:
    python3 scripts/lint-cross-artifact.py [--fix]

Exit codes:
    0 = todos os checks PASS
    1 = pelo menos um FAIL detectado

Author: Frank-MKT plugin (v2.39.0+)
License: UNLICENSED (mesmo do plugin)
"""

import json
import re
import sys
from pathlib import Path
from typing import Optional

# ============================================================
# CONFIGURACAO
# ============================================================

# Layout do repo (relative ao script em frank-mkt-plugin/scripts/)
SCRIPT_DIR = Path(__file__).resolve().parent
PLUGIN_DIR = SCRIPT_DIR.parent
REPO_ROOT = PLUGIN_DIR.parent

SKILLS_DIR = PLUGIN_DIR / "skills"
AGENTS_DIR = PLUGIN_DIR / "agents"
COMMANDS_DIR = PLUGIN_DIR / "commands"

PLUGIN_JSON = PLUGIN_DIR / ".claude-plugin" / "plugin.json"
MARKETPLACE_JSON = REPO_ROOT / ".claude-plugin" / "marketplace.json"
INDEX_MD = SKILLS_DIR / "INDEX.md"
HELP_MD = COMMANDS_DIR / "help.md"
INSTALACAO_MD = REPO_ROOT / "docs_mkt" / "INSTALACAO.md"
ROADMAP_MD = REPO_ROOT / "docs_mkt" / "ROADMAP-FRANK-MKT.md"
AGENTS_README = AGENTS_DIR / "README.md"
FRANK_MKT_AGENT = AGENTS_DIR / "frank-mkt.md"

# Arquivos que devem espelhar a versao do plugin.json
VERSION_FILES = {
    "marketplace.json (top)": MARKETPLACE_JSON,
    "marketplace.json (plugin entry)": MARKETPLACE_JSON,
    "INDEX.md status header": INDEX_MD,
    "help.md visao geral": HELP_MD,
    "INSTALACAO.md versao section": INSTALACAO_MD,
    "ROADMAP.md header": ROADMAP_MD,
    "agents/README.md header": AGENTS_README,
    "agents/frank-mkt.md (sem versao hardcoded - apenas contagens)": FRANK_MKT_AGENT,
}

# ============================================================
# COLETA DE GROUND TRUTH
# ============================================================


def count_skills() -> int:
    """Conta diretorios com SKILL.md."""
    return sum(
        1 for d in SKILLS_DIR.iterdir()
        if d.is_dir() and (d / "SKILL.md").exists()
    )


def count_agents() -> int:
    """Conta .md files em agents/ exceto README.md."""
    return sum(
        1 for f in AGENTS_DIR.glob("*.md")
        if f.name != "README.md"
    )


def count_commands() -> int:
    """Conta .md files em commands/."""
    return len(list(COMMANDS_DIR.glob("*.md")))


def load_plugin_version() -> str:
    """Le version do plugin.json (ground truth)."""
    with open(PLUGIN_JSON, encoding="utf-8") as f:
        return json.load(f)["version"]


# ============================================================
# CHECKS
# ============================================================


class LintError:
    def __init__(self, severity: str, file: str, line: Optional[int], msg: str):
        self.severity = severity  # HIGH / MEDIUM / LOW
        self.file = file
        self.line = line
        self.msg = msg

    def __str__(self) -> str:
        loc = f"{self.file}:{self.line}" if self.line else self.file
        return f"[{self.severity}] {loc} - {self.msg}"


def grep_line_numbers(file: Path, pattern: str) -> list[tuple[int, str]]:
    """Retorna [(linha, conteudo)] das ocorrencias do pattern."""
    if not file.exists():
        return []
    regex = re.compile(pattern)
    results = []
    with open(file, encoding="utf-8") as f:
        for n, line in enumerate(f, 1):
            if regex.search(line):
                results.append((n, line.rstrip()))
    return results


def _check_all_version_mentions(
    file: Path, pattern: str, version: str, label: str, errors: list[LintError],
    severity: str = "HIGH"
) -> None:
    """Helper: itera TODOS os matches do pattern e valida versao.

    Eliminou bug v2.39.0 onde apenas [0] era checado, deixando subsection
    headers com versao stale escapar.
    """
    matches = grep_line_numbers(file, pattern)
    if not matches:
        return  # arquivo nao tem pattern, ignora silenciosamente
    for line_no, content in matches:
        m = re.search(r"v([\d.]+)", content)
        if not m:
            continue
        found_v = m.group(1)
        if found_v != version:
            errors.append(LintError(
                severity, str(file), line_no,
                f"{label} L{line_no} diz v{found_v}, plugin.json {version}"
            ))


def check_version_consistency(version: str, errors: list[LintError]) -> None:
    """Verifica que cada arquivo correlato menciona a versao truth.

    v2.39.1: endurecido apos meta-finding lost-in-middle -- itera TODOS
    matches (nao so [0]), cobre subsection headers em INDEX.md.
    """
    # marketplace.json (top + plugin entry) -- defensive default removido
    with open(MARKETPLACE_JSON, encoding="utf-8") as f:
        mp = json.load(f)
    if mp.get("version") != version:
        errors.append(LintError(
            "HIGH", str(MARKETPLACE_JSON), None,
            f"marketplace.json top version={mp.get('version')} != plugin.json {version}"
        ))
    plugins_list = mp.get("plugins")
    if not plugins_list:
        errors.append(LintError(
            "HIGH", str(MARKETPLACE_JSON), None,
            "marketplace.json sem chave 'plugins' (estrutura quebrada)"
        ))
    else:
        plugins_entry = plugins_list[0]
        if plugins_entry.get("version") != version:
            errors.append(LintError(
                "HIGH", str(MARKETPLACE_JSON), None,
                f"marketplace.json plugin entry version={plugins_entry.get('version')} != plugin.json {version}"
            ))

    # INDEX.md: header principal + subsection headers (## Agentes (X/X — vY) etc)
    _check_all_version_mentions(
        INDEX_MD, r"## Status \(v[\d.]+", version, "INDEX.md status header", errors, "HIGH"
    )
    _check_all_version_mentions(
        INDEX_MD, r"## Agentes? \(\d+/\d+ — v[\d.]+\)", version,
        "INDEX.md ## Agentes subsection", errors, "HIGH"
    )
    _check_all_version_mentions(
        INDEX_MD, r"## Slash Commands \(\d+/\d+ — v[\d.]+\)", version,
        "INDEX.md ## Slash Commands subsection", errors, "HIGH"
    )

    # help.md visao geral
    _check_all_version_mentions(
        HELP_MD, r"Plugin frank-mkt v[\d.]+", version, "help.md visao geral",
        errors, "HIGH"
    )

    # INSTALACAO.md: itera TODAS as menções **vX.Y.Z** (nao so a ultima)
    matches = grep_line_numbers(INSTALACAO_MD, r"\*\*v[\d.]+\*\*")
    if not matches:
        errors.append(LintError(
            "MEDIUM", str(INSTALACAO_MD), None,
            "INSTALACAO.md sem **vX.Y.Z** marcador"
        ))
    else:
        # A ultima ocorrencia e a "secao Versao" — drift HIGH
        last_ln, last_content = matches[-1]
        m = re.search(r"\*\*v([\d.]+)\*\*", last_content)
        if m and m.group(1) != version:
            errors.append(LintError(
                "HIGH", str(INSTALACAO_MD), last_ln,
                f"INSTALACAO.md secao Versao (L{last_ln}) diz v{m.group(1)}, plugin.json {version}"
            ))

    # ROADMAP.md header
    _check_all_version_mentions(
        ROADMAP_MD, r"Vers[aã]o atual do plugin:.*v[\d.]+", version,
        "ROADMAP.md header", errors, "MEDIUM"
    )

    # agents/README.md header
    _check_all_version_mentions(
        AGENTS_README, r"## Agentes implementados \(\d+/\d+ — v[\d.]+\)", version,
        "agents/README.md header", errors, "MEDIUM"
    )


def _check_count_in_file(
    file: Path, pattern: str, expected: int, label: str, errors: list[LintError],
    severity: str = "HIGH"
) -> None:
    """Helper: itera TODOS os matches do pattern e valida contagem."""
    matches = grep_line_numbers(file, pattern)
    for line_no, content in matches:
        m = re.search(pattern.replace(r"\d+", r"(\d+)"), content)
        if m and int(m.group(1)) != expected:
            errors.append(LintError(
                severity, str(file), line_no,
                f"{label} L{line_no} diz {m.group(1)}, filesystem tem {expected}"
            ))


def check_count_consistency(
    skills: int, agents: int, commands: int, errors: list[LintError]
) -> None:
    """Verifica contagens declaradas em arquivos correlatos.

    v2.39.1: cobre subsection counts (Skills Avancadas tier, tabela INDEX celulas,
    soma por volatility tier, help.md exemplos inline, INSTALACAO/ROADMAP contagens).
    """
    expected_total = skills + agents + commands

    # plugin.json description
    with open(PLUGIN_JSON, encoding="utf-8") as f:
        plugin = json.load(f)
    desc = plugin.get("description", "")
    for label, expected in [
        ("skills", skills),
        ("commands", commands),
        ("agentes", agents),
        ("artefatos", expected_total),
    ]:
        m = re.search(rf"(\d+) {label}", desc)
        if m and int(m.group(1)) != expected:
            errors.append(LintError(
                "MEDIUM", str(PLUGIN_JSON), None,
                f"plugin.json description '{m.group(1)} {label}' != real {expected}"
            ))

    # marketplace.json plugin entry description (defensive default removido)
    with open(MARKETPLACE_JSON, encoding="utf-8") as f:
        mp = json.load(f)
    plugins_list = mp.get("plugins")
    if plugins_list:
        plugin_entry_desc = plugins_list[0].get("description", "")
        for label, expected in [
            ("skills", skills),
            ("slash commands", commands),
            ("agentes", agents),
            ("artefatos", expected_total),
        ]:
            m = re.search(rf"(\d+) {label}", plugin_entry_desc)
            if m and int(m.group(1)) != expected:
                errors.append(LintError(
                    "MEDIUM", str(MARKETPLACE_JSON), None,
                    f"marketplace.json plugin description '{m.group(1)} {label}' != real {expected}"
                ))

    # INDEX.md: status header agregado (93 skills + 10 commands + 16 agentes)
    matches = grep_line_numbers(INDEX_MD, r"\d+ skills \+ \d+ commands \+ \d+ agentes")
    for line_no, content in matches:
        m = re.search(r"(\d+) skills \+ (\d+) commands \+ (\d+) agentes", content)
        if m:
            s, c, a = int(m.group(1)), int(m.group(2)), int(m.group(3))
            if (s, c, a) != (skills, commands, agents):
                errors.append(LintError(
                    "HIGH", str(INDEX_MD), line_no,
                    f"INDEX.md L{line_no} diz {s}/{c}/{a} (skills/commands/agentes), real {skills}/{commands}/{agents}"
                ))

    # INDEX.md: celulas de tabela "orquestra X skills + Y agentes + Z commands"
    matches = grep_line_numbers(INDEX_MD, r"orquestra \d+ skills \+ \d+ agentes")
    for line_no, content in matches:
        m = re.search(r"orquestra (\d+) skills \+ (\d+) agentes \+ (\d+) commands", content)
        if m:
            s, a, c = int(m.group(1)), int(m.group(2)), int(m.group(3))
            if (s, a, c) != (skills, agents, commands):
                errors.append(LintError(
                    "MEDIUM", str(INDEX_MD), line_no,
                    f"INDEX.md tabela L{line_no} celula diz orquestra {s}/{a}/{c}, real {skills}/{agents}/{commands}"
                ))

    # INDEX.md: soma por volatility tier (24 high + 62 medium + 7 low = 93)
    matches = grep_line_numbers(INDEX_MD, r"\d+ skills `(?:high|medium|low)`")
    if matches:
        # Extrai todos os tier counts da linha
        for ln, content in matches[:1]:  # so primeira ocorrencia (linha Volatility)
            tier_high = re.search(r"(\d+) skills `high`", content)
            tier_medium = re.search(r"(\d+) skills `medium`", content)
            tier_low = re.search(r"(\d+) skills `low`", content)
            if tier_high and tier_medium and tier_low:
                total = int(tier_high.group(1)) + int(tier_medium.group(1)) + int(tier_low.group(1))
                if total != skills:
                    errors.append(LintError(
                        "MEDIUM", str(INDEX_MD), ln,
                        f"INDEX.md soma volatility tiers ({tier_high.group(1)}+{tier_medium.group(1)}+{tier_low.group(1)}={total}) != real {skills} skills"
                    ))

    # help.md visao geral (workflow + heading + exemplos)
    # Cobre tanto "- 10 slash commands" quanto "10 slash commands (inclui...)"
    help_patterns = [
        (r"(\d+) slash commands", commands, "slash commands"),
        (r"(\d+) agentes", agents, "agentes"),
        (r"(\d+) skills agrupadas", skills, "skills agrupadas"),
    ]
    for pattern, expected, label in help_patterns:
        for ln, content in grep_line_numbers(HELP_MD, pattern):
            m = re.search(pattern, content)
            if m and int(m.group(1)) != expected:
                errors.append(LintError(
                    "HIGH", str(HELP_MD), ln,
                    f"help.md L{ln} diz '{m.group(1)} {label}', real {expected}"
                ))


def check_auto_contradiction(errors: list[LintError]) -> None:
    """Detecta auto-contradicao mid-file (mesmo arquivo dizer 2 numeros distintos).

    Importante: extrair numero do MATCH GROUP correto (nao primeiro \\d+ da linha,
    porque listas numeradas em markdown comecam com '2.' ou similar).
    """
    # help.md: workflow vs heading - Slash Commands
    workflow_pattern = re.compile(r'bloco "(\d+) Slash Commands" completo')
    heading_pattern = re.compile(r"^## (\d+) Slash Commands")

    workflow_matches = []
    heading_matches = []
    with open(HELP_MD, encoding="utf-8") as f:
        for n, line in enumerate(f, 1):
            m = workflow_pattern.search(line)
            if m:
                workflow_matches.append((n, int(m.group(1))))
            m = heading_pattern.search(line)
            if m:
                heading_matches.append((n, int(m.group(1))))

    if workflow_matches and heading_matches:
        wf_line, wf_n = workflow_matches[0]
        hd_line, hd_n = heading_matches[0]
        if wf_n != hd_n:
            errors.append(LintError(
                "HIGH", str(HELP_MD), hd_line,
                f"help.md auto-contradicao Slash Commands: workflow L{wf_line} diz {wf_n}, heading L{hd_line} diz {hd_n}"
            ))

    # help.md: workflow vs heading - Agentes
    workflow_pattern_a = re.compile(r'bloco "(\d+) Agentes" completo')
    heading_pattern_a = re.compile(r"^## (\d+) Agentes")

    workflow_agt = []
    heading_agt = []
    with open(HELP_MD, encoding="utf-8") as f:
        for n, line in enumerate(f, 1):
            m = workflow_pattern_a.search(line)
            if m:
                workflow_agt.append((n, int(m.group(1))))
            m = heading_pattern_a.search(line)
            if m:
                heading_agt.append((n, int(m.group(1))))

    if workflow_agt and heading_agt:
        wf_line, wf_n = workflow_agt[0]
        hd_line, hd_n = heading_agt[0]
        if wf_n != hd_n:
            errors.append(LintError(
                "HIGH", str(HELP_MD), hd_line,
                f"help.md auto-contradicao Agentes: workflow L{wf_line} diz {wf_n}, heading L{hd_line} diz {hd_n}"
            ))


def check_ascii_compliance(errors: list[LintError]) -> None:
    """Verifica que arquivos com ascii_only:true nao tem em-dashes/emojis em conteudo novo.

    Aviso: este check e PERMISSIVO em v2.39.0 -- detecta mas reporta como LOW
    (nao bloqueador). Endurecer em release futura quando conteudo legado for
    convertido.
    """
    # Procurar SKILL.md com ascii_only: true
    for skill_md in SKILLS_DIR.glob("*/SKILL.md"):
        with open(skill_md, encoding="utf-8") as f:
            content = f.read()
        if not re.search(r"ascii_only:\s*true", content[:2000]):
            continue  # nao declara, ignora
        # Contar em-dashes e emojis
        emdash_count = content.count("—")  # em-dash
        emoji_warn = content.count("⚠️")  # warning emoji
        emoji_arrow = content.count("→") + content.count("↓") + content.count("←")
        total = emdash_count + emoji_warn + emoji_arrow
        if total > 0:
            errors.append(LintError(
                "LOW", str(skill_md), None,
                f"ascii_only:true declarado mas encontrou {emdash_count} em-dashes, {emoji_warn} warning emoji, {emoji_arrow} setas Unicode"
            ))


def check_cross_refs(errors: list[LintError]) -> None:
    """Verifica que cross-refs em skills/agents/commands apontam para arquivos reais."""
    # Skills existentes
    skills_set = {d.name for d in SKILLS_DIR.iterdir() if d.is_dir() and (d / "SKILL.md").exists()}
    agents_set = {f.stem for f in AGENTS_DIR.glob("*.md") if f.name != "README.md"}

    # Padrao: refs a `<nome>` em backticks dentro de SKILL.md/agent.md/command.md
    # Vamos checar APENAS arquivos novos de v2.37+ por enquanto (gradual rollout)
    files_to_check = [
        SKILLS_DIR / "render-loop-svg" / "SKILL.md",
        AGENTS_DIR / "renderer-visual.md",
        AGENTS_DIR / "atelier-criativo.md",
        COMMANDS_DIR / "gerar-infografico.md",
        COMMANDS_DIR / "atelier.md",
    ]
    # Lista canonica de cross-refs validas: skills + agents + alguns conhecidos
    known_skills = skills_set
    known_agents = agents_set

    for fp in files_to_check:
        if not fp.exists():
            continue
        with open(fp, encoding="utf-8") as f:
            content = f.read()
        # Pega refs a skills (`<nome>` proximo a "skill" keyword)
        for m in re.finditer(r"skill\s+`([a-z0-9-]+)`", content):
            ref = m.group(1)
            if ref not in known_skills and ref not in known_agents:
                errors.append(LintError(
                    "LOW", str(fp), None,
                    f"cross-ref skill '{ref}' nao encontrada em skills/ ou agents/"
                ))
        # Pega refs a agentes (`<nome>` proximo a "agente"/"agent" keyword)
        for m in re.finditer(r"agente\s+`([a-z0-9-]+)`", content):
            ref = m.group(1)
            if ref not in known_agents and ref not in known_skills:
                errors.append(LintError(
                    "LOW", str(fp), None,
                    f"cross-ref agente '{ref}' nao encontrado em agents/"
                ))


def check_skill_frontmatter(errors: list[LintError]) -> None:
    """Verifica que SKILL.md tem frontmatter YAML obrigatorio.

    Aceita sinonimos:
    - last_review OR last_verified (variacao historica do plugin)
    - next_review OR next_verified
    """
    # (campo principal, campos sinonimos aceitos)
    required = [
        ("name", []),
        ("description", []),
        ("volatility", []),
        ("last_review", ["last_verified"]),
        ("next_review", ["next_verified"]),
    ]
    for skill_md in SKILLS_DIR.glob("*/SKILL.md"):
        with open(skill_md, encoding="utf-8") as f:
            content = f.read()
        # Frontmatter entre primeiros dois ---
        m = re.match(r"^---\n(.+?)\n---", content, re.DOTALL)
        if not m:
            errors.append(LintError(
                "HIGH", str(skill_md), None,
                "SKILL.md sem frontmatter YAML entre --- separators"
            ))
            continue
        fm = m.group(1)
        for field, synonyms in required:
            candidates = [field] + synonyms
            if not any(re.search(rf"^{f}:", fm, re.MULTILINE) for f in candidates):
                shown = "/".join(candidates)
                errors.append(LintError(
                    "MEDIUM", str(skill_md), None,
                    f"SKILL.md frontmatter sem campo obrigatorio '{shown}'"
                ))


# ============================================================
# MAIN
# ============================================================


def main() -> int:
    errors: list[LintError] = []

    # Ground truth
    try:
        skills_real = count_skills()
        agents_real = count_agents()
        commands_real = count_commands()
        version_real = load_plugin_version()
    except Exception as e:
        print(f"FATAL: failed to load ground truth: {e}", file=sys.stderr)
        return 1

    print(f"Ground truth from filesystem + plugin.json:")
    print(f"  - Version: v{version_real}")
    print(f"  - Skills:  {skills_real}")
    print(f"  - Agents:  {agents_real}")
    print(f"  - Commands: {commands_real}")
    print(f"  - Total artifacts: {skills_real + agents_real + commands_real}")
    print()

    # Run checks
    check_version_consistency(version_real, errors)
    check_count_consistency(skills_real, agents_real, commands_real, errors)
    check_auto_contradiction(errors)
    check_skill_frontmatter(errors)
    check_cross_refs(errors)
    check_ascii_compliance(errors)

    # Report
    if not errors:
        print("PASS - all cross-artifact checks passed.")
        print()
        print(f"Plugin v{version_real} is consistent across:")
        print(f"  - plugin.json + marketplace.json")
        print(f"  - skills/INDEX.md + commands/help.md")
        print(f"  - agents/README.md + agents/frank-mkt.md")
        print(f"  - docs_mkt/INSTALACAO.md + docs_mkt/ROADMAP-FRANK-MKT.md")
        return 0

    # Agrupar por severidade
    by_sev = {"HIGH": [], "MEDIUM": [], "LOW": []}
    for e in errors:
        by_sev.get(e.severity, by_sev["LOW"]).append(e)

    high_count = len(by_sev["HIGH"])
    medium_count = len(by_sev["MEDIUM"])
    low_count = len(by_sev["LOW"])

    # Status:
    # - 0 HIGH + 0 MEDIUM + 0 LOW = PASS clean
    # - 0 HIGH + MEDIUM/LOW > 0 = PASS WITH WARNINGS (exit 0)
    # - HIGH > 0 = FAIL (exit 1)
    if high_count == 0:
        status_label = "PASS WITH WARNINGS"
    else:
        status_label = "FAIL"

    print(f"{status_label} - {high_count} HIGH + {medium_count} MEDIUM + {low_count} LOW issues found:")
    print()
    for sev in ("HIGH", "MEDIUM", "LOW"):
        if not by_sev[sev]:
            continue
        print(f"{sev}:")
        # Limitar output verbose para MEDIUM/LOW; HIGH sempre listar todos.
        items_to_show = by_sev[sev] if sev == "HIGH" else by_sev[sev][:10]
        for e in items_to_show:
            print(f"  {e}")
        if sev != "HIGH" and len(by_sev[sev]) > 10:
            print(f"  ... ({len(by_sev[sev]) - 10} more {sev} items omitted; rerun without head_limit to see all)")
        print()

    # Exit: HIGH bloqueia build (exit 1); MEDIUM/LOW alertam mas passa (exit 0)
    if high_count > 0:
        print(f"BLOCKED: {high_count} HIGH issue(s) bloqueiam o build.", file=sys.stderr)
        return 1
    print(f"OK: {medium_count + low_count} non-blocking issue(s) sao debito tecnico documentado (frontmatter legado + em-dashes pre-v2.38.0). Build prossegue.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
