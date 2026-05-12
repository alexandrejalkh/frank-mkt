#!/usr/bin/env python3
"""
Testes unitarios para lint-cross-artifact.py.

Motivacao: arquiteto v2.39.0 reportou E1 "lint sem auto-teste" como CONCERN.
v2.39.2 fecha esse gap criando fixtures sinteticas + asserts.

Filosofia: cada fixture simula um cenario de drift conhecido. Cada teste valida
que o lint detecta (ou nao) corretamente. Garante regressao zero quando lint
crescer.

Uso:
    python3 frank-mkt-plugin/scripts/test_lint.py

Exit codes:
    0 = todos os testes PASSAM
    1 = pelo menos um teste FALHOU

Filosofia: nao usa pytest para minimizar deps externas. Implementacao manual
proxima ao stdlib (apenas unittest builtin).
"""

import json
import os
import re
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

# Adicionar scripts/ ao sys.path para importar lint-cross-artifact
SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

# Hyphen no nome de modulo nao funciona em import direto;
# usar importlib para carregar o script
import importlib.util


def load_lint_module():
    """Carrega lint-cross-artifact.py como modulo dinamicamente."""
    spec = importlib.util.spec_from_file_location(
        "lint_module",
        SCRIPT_DIR / "lint-cross-artifact.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


# ============================================================
# FIXTURE SINTETICA: known-good v2.39.2
# ============================================================


def make_fixture_known_good() -> Path:
    """Cria estrutura de plugin sintetica conhecida-boa para teste.

    Layout:
        <tmpdir>/
        ├── .claude-plugin/
        │   └── marketplace.json
        └── frank-mkt-plugin/
            ├── .claude-plugin/
            │   └── plugin.json
            ├── skills/
            │   ├── INDEX.md
            │   ├── skill-a/SKILL.md
            │   └── skill-b/SKILL.md
            ├── agents/
            │   ├── README.md
            │   ├── frank-mkt.md
            │   └── outro.md
            └── commands/
                ├── help.md
                └── outro-cmd.md
    """
    tmpdir = Path(tempfile.mkdtemp(prefix="lint-test-known-good-"))

    # Estrutura
    (tmpdir / ".claude-plugin").mkdir()
    (tmpdir / "frank-mkt-plugin" / ".claude-plugin").mkdir(parents=True)
    (tmpdir / "frank-mkt-plugin" / "skills" / "skill-a").mkdir(parents=True)
    (tmpdir / "frank-mkt-plugin" / "skills" / "skill-b").mkdir()
    (tmpdir / "frank-mkt-plugin" / "agents").mkdir()
    (tmpdir / "frank-mkt-plugin" / "commands").mkdir()
    (tmpdir / "docs_mkt").mkdir()

    # plugin.json
    (tmpdir / "frank-mkt-plugin" / ".claude-plugin" / "plugin.json").write_text(json.dumps({
        "name": "frank-mkt-test",
        "version": "1.0.0",
        "description": "test fixture -- 2 skills + 2 commands + 2 agentes = 6 artefatos",
    }), encoding="utf-8")

    # marketplace.json
    (tmpdir / ".claude-plugin" / "marketplace.json").write_text(json.dumps({
        "name": "frank-mkt-test",
        "version": "1.0.0",
        "plugins": [{"name": "frank-mkt-test", "version": "1.0.0", "description": "2 skills + 2 commands + 2 agentes = 6 artefatos"}]
    }), encoding="utf-8")

    # README.md raiz (sem mencao de versao)
    (tmpdir / "README.md").write_text("# Test plugin\n\nContent.\n", encoding="utf-8")

    # INDEX.md
    (tmpdir / "frank-mkt-plugin" / "skills" / "INDEX.md").write_text(
        "# INDEX\n\n"
        "## Status (v1.0.0 -- 2026-01-01) -- PLUGIN TEST\n\n"
        "**2 skills + 2 commands + 2 agentes / 100 linhas totais.**\n\n"
        "## Agentes (2/2 -- v1.0.0)\n\nTabela aqui.\n\n"
        "## Slash Commands (2/2 -- v1.0.0)\n\nTabela aqui.\n",
        encoding="utf-8"
    )

    # SKILL.md fixtures (frontmatter completo)
    skill_content = (
        "---\n"
        "name: skill-test\n"
        "description: test skill\n"
        "volatility: medium\n"
        "last_review: 2026-01-01\n"
        "next_review: 2026-07-01\n"
        "---\n\n# Skill\n"
    )
    (tmpdir / "frank-mkt-plugin" / "skills" / "skill-a" / "SKILL.md").write_text(skill_content, encoding="utf-8")
    (tmpdir / "frank-mkt-plugin" / "skills" / "skill-b" / "SKILL.md").write_text(skill_content, encoding="utf-8")

    # Agent files
    (tmpdir / "frank-mkt-plugin" / "agents" / "README.md").write_text(
        "# Agents\n\n## Agentes implementados (2/2 -- v1.0.0)\n\nTabela.\n",
        encoding="utf-8"
    )
    (tmpdir / "frank-mkt-plugin" / "agents" / "frank-mkt.md").write_text(
        "---\nname: frank-mkt\n---\n\n# Agent\n",
        encoding="utf-8"
    )
    (tmpdir / "frank-mkt-plugin" / "agents" / "outro.md").write_text(
        "---\nname: outro\n---\n\n# Agent\n",
        encoding="utf-8"
    )

    # Commands files
    (tmpdir / "frank-mkt-plugin" / "commands" / "help.md").write_text(
        "# /frank-mkt:help\n\n"
        "Plugin frank-mkt v1.0.0 - test.\n\n"
        "```\n"
        "2 slash commands\n"
        "2 agentes\n"
        "2 skills (2 blocos)\n"
        "```\n\n"
        "## 2 Slash Commands\n\nTabela.\n\n"
        "## 2 Agentes\n\nTabela.\n\n"
        "## 2 Skills (2 BLOCOS COMPLETOS)\n\n### Bloco 1\n- skill-a\n\n### Bloco 2\n- skill-b\n",
        encoding="utf-8"
    )
    (tmpdir / "frank-mkt-plugin" / "commands" / "outro-cmd.md").write_text(
        "# /frank-mkt:outro\n\nContent.\n",
        encoding="utf-8"
    )

    # docs_mkt
    (tmpdir / "docs_mkt" / "INSTALACAO.md").write_text(
        "# Instalacao\n\nValidado em 2026-01-01 (v1.0.0).\n\n"
        "## Versao\n\n**v1.0.0** (2026-01-01) -- Plugin: 2 skills + 2 commands + 2 agentes = 6 artefatos.\n",
        encoding="utf-8"
    )
    (tmpdir / "docs_mkt" / "ROADMAP-FRANK-MKT.md").write_text(
        "# Roadmap\n\n**Versao atual do plugin:** **v1.0.0** (test)\n",
        encoding="utf-8"
    )

    return tmpdir


# ============================================================
# TESTES
# ============================================================


class TestLintCrossArtifact(unittest.TestCase):
    """Suite de testes para o lint cross-artifact."""

    @classmethod
    def setUpClass(cls):
        """Carrega o modulo lint uma vez para todos os testes."""
        cls.lint = load_lint_module()

    def _override_paths(self, fixture_root: Path):
        """Patch as constantes globais do lint para apontar para a fixture."""
        self.lint.SCRIPT_DIR = fixture_root / "frank-mkt-plugin" / "scripts"
        self.lint.PLUGIN_DIR = fixture_root / "frank-mkt-plugin"
        self.lint.REPO_ROOT = fixture_root
        self.lint.SKILLS_DIR = fixture_root / "frank-mkt-plugin" / "skills"
        self.lint.AGENTS_DIR = fixture_root / "frank-mkt-plugin" / "agents"
        self.lint.COMMANDS_DIR = fixture_root / "frank-mkt-plugin" / "commands"
        self.lint.PLUGIN_JSON = fixture_root / "frank-mkt-plugin" / ".claude-plugin" / "plugin.json"
        self.lint.MARKETPLACE_JSON = fixture_root / ".claude-plugin" / "marketplace.json"
        self.lint.INDEX_MD = fixture_root / "frank-mkt-plugin" / "skills" / "INDEX.md"
        self.lint.HELP_MD = fixture_root / "frank-mkt-plugin" / "commands" / "help.md"
        self.lint.INSTALACAO_MD = fixture_root / "docs_mkt" / "INSTALACAO.md"
        self.lint.ROADMAP_MD = fixture_root / "docs_mkt" / "ROADMAP-FRANK-MKT.md"
        self.lint.AGENTS_README = fixture_root / "frank-mkt-plugin" / "agents" / "README.md"
        self.lint.FRANK_MKT_AGENT = fixture_root / "frank-mkt-plugin" / "agents" / "frank-mkt.md"
        self.lint.README_ROOT = fixture_root / "README.md"

    def _run_lint(self, fixture_root: Path):
        """Roda os checks principais retornando lista de errors."""
        self._override_paths(fixture_root)
        errors: list = []

        skills = self.lint.count_skills()
        agents = self.lint.count_agents()
        commands = self.lint.count_commands()
        version = self.lint.load_plugin_version()

        self.lint.check_version_consistency(version, errors)
        self.lint.check_count_consistency(skills, agents, commands, errors)
        self.lint.check_block_count_consistency(errors)
        self.lint.check_auto_contradiction(errors)
        self.lint.check_skill_frontmatter(errors)

        return errors, skills, agents, commands, version

    def _count_severity(self, errors, severity):
        return sum(1 for e in errors if e.severity == severity)

    # ============================================================
    # TEST: known-good fixture
    # ============================================================

    def test_known_good_fixture_passes(self):
        """Fixture conhecida-boa nao deve gerar HIGH."""
        tmpdir = make_fixture_known_good()
        try:
            errors, skills, agents, commands, version = self._run_lint(tmpdir)
            high_count = self._count_severity(errors, "HIGH")
            self.assertEqual(skills, 2)
            self.assertEqual(agents, 2)
            self.assertEqual(commands, 2)
            self.assertEqual(version, "1.0.0")
            self.assertEqual(high_count, 0,
                f"Known-good fixture nao deveria ter HIGH errors, mas teve: {[str(e) for e in errors if e.severity == 'HIGH']}"
            )
        finally:
            shutil.rmtree(tmpdir)

    # ============================================================
    # TEST: version drift detection
    # ============================================================

    def test_marketplace_version_drift_detected(self):
        """Marketplace.json com version != plugin.json deve gerar HIGH."""
        tmpdir = make_fixture_known_good()
        try:
            # Drift: marketplace.json top em 2.0.0, plugin.json em 1.0.0
            mp = json.loads((tmpdir / ".claude-plugin" / "marketplace.json").read_text())
            mp["version"] = "2.0.0"
            (tmpdir / ".claude-plugin" / "marketplace.json").write_text(json.dumps(mp), encoding="utf-8")

            errors, _, _, _, _ = self._run_lint(tmpdir)
            high_msgs = [str(e) for e in errors if e.severity == "HIGH"]
            self.assertTrue(
                any("marketplace.json top" in m for m in high_msgs),
                f"Drift em marketplace.json top nao detectado: HIGHs={high_msgs}"
            )
        finally:
            shutil.rmtree(tmpdir)

    def test_index_status_header_version_drift_detected(self):
        """INDEX.md ## Status com version != plugin.json deve gerar HIGH."""
        tmpdir = make_fixture_known_good()
        try:
            index = (tmpdir / "frank-mkt-plugin" / "skills" / "INDEX.md").read_text(encoding="utf-8")
            index = index.replace("## Status (v1.0.0", "## Status (v9.9.9")
            (tmpdir / "frank-mkt-plugin" / "skills" / "INDEX.md").write_text(index, encoding="utf-8")

            errors, _, _, _, _ = self._run_lint(tmpdir)
            high_msgs = [str(e) for e in errors if e.severity == "HIGH"]
            self.assertTrue(
                any("INDEX.md status header" in m for m in high_msgs),
                f"Drift em INDEX.md status header nao detectado: HIGHs={high_msgs}"
            )
        finally:
            shutil.rmtree(tmpdir)

    # ============================================================
    # TEST: count drift detection
    # ============================================================

    def test_help_md_skills_count_drift_detected(self):
        """help.md 'X skills agrupadas' com count != filesystem deve gerar HIGH."""
        tmpdir = make_fixture_known_good()
        try:
            help_content = (tmpdir / "frank-mkt-plugin" / "commands" / "help.md").read_text(encoding="utf-8")
            # Adicionar contagem errada
            help_content += "\n\n- 99 skills agrupadas em foo\n"
            (tmpdir / "frank-mkt-plugin" / "commands" / "help.md").write_text(help_content, encoding="utf-8")

            errors, _, _, _, _ = self._run_lint(tmpdir)
            high_msgs = [str(e) for e in errors if e.severity == "HIGH"]
            self.assertTrue(
                any("99 skills agrupadas" in m for m in high_msgs),
                f"Drift em help.md skills count nao detectado: HIGHs={high_msgs}"
            )
        finally:
            shutil.rmtree(tmpdir)

    # ============================================================
    # TEST: block count detection
    # ============================================================

    def test_block_count_drift_detected(self):
        """help.md 'X blocos completos' com count != ### Bloco N headers."""
        tmpdir = make_fixture_known_good()
        try:
            help_content = (tmpdir / "frank-mkt-plugin" / "commands" / "help.md").read_text(encoding="utf-8")
            # Fixture tem 2 ### Bloco N. Adicionar declaracao de 99
            help_content += "\n\n99 BLOCOS COMPLETOS contagem errada para teste\n"
            (tmpdir / "frank-mkt-plugin" / "commands" / "help.md").write_text(help_content, encoding="utf-8")

            errors, _, _, _, _ = self._run_lint(tmpdir)
            high_msgs = [str(e) for e in errors if e.severity == "HIGH"]
            self.assertTrue(
                any("99" in m and "BLOCOS COMPLETOS" in m for m in high_msgs),
                f"Drift de block count nao detectado: HIGHs={high_msgs}"
            )
        finally:
            shutil.rmtree(tmpdir)

    # ============================================================
    # TEST: marketplace.json sem "plugins" key
    # ============================================================

    def test_marketplace_without_plugins_key_fails_high(self):
        """marketplace.json sem chave 'plugins' deve gerar HIGH explicito (anti-defensive-default)."""
        tmpdir = make_fixture_known_good()
        try:
            mp = json.loads((tmpdir / ".claude-plugin" / "marketplace.json").read_text())
            del mp["plugins"]
            (tmpdir / ".claude-plugin" / "marketplace.json").write_text(json.dumps(mp), encoding="utf-8")

            errors, _, _, _, _ = self._run_lint(tmpdir)
            high_msgs = [str(e) for e in errors if e.severity == "HIGH"]
            self.assertTrue(
                any("plugins" in m.lower() and "estrutura quebrada" in m.lower() for m in high_msgs),
                f"Marketplace sem 'plugins' nao detectado como HIGH: HIGHs={high_msgs}"
            )
        finally:
            shutil.rmtree(tmpdir)

    # ============================================================
    # TEST: SKILL frontmatter incompleto
    # ============================================================

    def test_skill_missing_frontmatter_field_detected(self):
        """SKILL.md sem 'volatility' deve gerar MEDIUM."""
        tmpdir = make_fixture_known_good()
        try:
            skill = (tmpdir / "frank-mkt-plugin" / "skills" / "skill-a" / "SKILL.md").read_text(encoding="utf-8")
            # Remover linha volatility
            skill = re.sub(r"^volatility:.*\n", "", skill, flags=re.MULTILINE)
            (tmpdir / "frank-mkt-plugin" / "skills" / "skill-a" / "SKILL.md").write_text(skill, encoding="utf-8")

            errors, _, _, _, _ = self._run_lint(tmpdir)
            medium_msgs = [str(e) for e in errors if e.severity == "MEDIUM"]
            self.assertTrue(
                any("volatility" in m for m in medium_msgs),
                f"Frontmatter sem volatility nao detectado: MEDIUMs={medium_msgs}"
            )
        finally:
            shutil.rmtree(tmpdir)


# ============================================================
# MAIN
# ============================================================


if __name__ == "__main__":
    # Verbosity 2 = relatorio detalhado por teste
    unittest.main(verbosity=2)
