#!/usr/bin/env bash
# check-skills-vencidas.sh
# Lista skills do frank-mkt com next_review anterior a hoje.
# Disparado pelo hook SessionStart (ver hooks.json).
# Portatil: bash (Linux/macOS/Git Bash Windows).

set -eu

PLUGIN_ROOT="${CLAUDE_PLUGIN_ROOT:-$(cd "$(dirname "$0")/.." && pwd)}"
SKILLS_DIR="$PLUGIN_ROOT/skills"
TODAY="$(date +%Y-%m-%d)"

[ -d "$SKILLS_DIR" ] || exit 0

vencidas=""
count=0
for skill_file in "$SKILLS_DIR"/*/SKILL.md; do
  [ -f "$skill_file" ] || continue
  skill_name="$(basename "$(dirname "$skill_file")")"
  next_review="$(grep -m1 '^next_review:' "$skill_file" 2>/dev/null | sed 's/^next_review:[[:space:]]*//' | tr -d '"' | tr -d "'" | awk '{$1=$1; print}')"
  [ -z "$next_review" ] && continue
  if [ "$next_review" \< "$TODAY" ]; then
    vencidas="${vencidas}  - ${skill_name} (next_review: ${next_review})
"
    count=$((count + 1))
  fi
done

if [ "$count" -gt 0 ]; then
  printf '\n[frank-mkt] %d skill(s) com next_review vencido:\n' "$count"
  printf '%s' "$vencidas"
  printf 'Re-grounding e sob demanda — validar em fonte oficial antes de publicar peca de marketing/midia.\n'
  printf 'Metodologia: skill `manutencao-skills`.\n\n'
fi

exit 0
