#!/bin/bash

PROJECT_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
JOURNAL_DIR="./skills/JOURNAL"
SKILL_FILE="$PROJECT_ROOT/$JOURNAL_DIR/SKILL.md"
JOURNAL_FILE="$PROJECT_ROOT/JOURNAL.md"

case "$1" in
  "init")
    mkdir -p "$JOURNAL_DIR"
    
    cat > "$SKILL_FILE" << 'SKILL_EOF'
---
name: journal
description: Creates and maintains a JOURNAL.md file in the root of the project to keep crucial information about your project, keeping notes in *JOURNAL.md* of problems, conclusions, questions, what the plan is, and tick off tasks as you finish them.
---

# **Prompt:**

You are an expert engineer. Your task is to implement **Task X** (describe Task X here). You **must** maintain a file named `JOURNAL.md` throughout the implementation. Use it to track progress, record issues, capture decisions, and plan next steps.

### **Mandatory format for JOURNAL.md:**

# JOURNAL.md

## ✅ Task Tracking

- Task description (pending)
    
- Completed task description
    

## ❌ Problems Encountered

- Problem description + how it was fixed (or needs fixing)
    

## 💡 Conclusions & Decisions

- What you learned, why you chose approach A over B
    

## ❓ Open Questions

- Anything unclear, needs clarification, or blocked by external factors
    

## 📋 Next Steps

- Immediate actions to continue implementation


### **Rules you must follow:**

1. **Before coding** – Create `JOURNAL.md` with the initial plan under `📋 Next Steps` and list all known tasks under `✅ Task Tracking`.

2. **During implementation** –
   - Tick off tasks as you finish them (`[x]`).
   - If you hit a problem, log it under `❌ Problems` and note how you fixed it.
   - If you find something that needs fixing but **isn't part of your assignment**, write it in `❌ Problems` or `💡 Conclusions` and **continue with your assignment** – do not derail.

3. **After each work session** – Update `📋 Next Steps` with what to do next.

4. **Use persistent memory beads** – Treat `JOURNAL.md` as your external memory. Always read it before starting work and append to it during work.

5. **When you finish Task X completely** –
   - Mark all tasks as `[x]`.
   - Write a final `💡 Conclusion` summarizing the implementation.
   - List any leftover `❓ Open Questions` for future work.

6. **When editing JOURNAL.md**
   - Any change in this file has to be prefixed by '//'.
   - Any line prefixed with '//' in this file has to be ignored.
SKILL_EOF

    if [ ! -f "$JOURNAL_FILE" ]; then
      cat > "$JOURNAL_FILE" << 'JOURNAL_EOF'
# JOURNAL.md

## ✅ Task Tracking
- [ ] Initial project setup complete

## ❌ Problems Encountered

## 💡 Conclusions & Decisions

## ❓ Open Questions

## 📋 Next Steps
- Define first development task
JOURNAL_EOF
      echo "✅ JOURNAL.md y SKILL.md creados en $PROJECT_ROOT"
    else
      echo "✅ SKILL.md creado. JOURNAL.md ya existe."
    fi
    ;;

  "review")
    if [ ! -f "$JOURNAL_FILE" ]; then
      echo "❌ No existe JOURNAL.md. Ejecuta: journal init"
      exit 1
    fi

    # Detectar cambios en git desde último commit
    CHANGES=$(git diff HEAD~1 -- . 2>/dev/null || echo "No hay cambios git detectados")

    if [ -z "$CHANGES" ]; then
      echo "ℹ️  No hay cambios recientes para revisar."
      exit 0
    fi

    # Backup // prefixed
    TIMESTAMP=$(date +%Y%m%d_%H%M%S)
    TEMP_FILE=$(mktemp)
    
    echo "" >> "$JOURNAL_FILE"
    echo "## // Cambios detectados: $TIMESTAMP" >> "$JOURNAL_FILE"
    echo "// Archivos modificados:" >> "$JOURNAL_FILE"
    
    # List files changed
    git diff --name-only HEAD~1 >> "$TEMP_FILE" 2>/dev/null || echo "// No hay cambios git" >> "$TEMP_FILE"
    sed 's/^/\/\/ /' "$TEMP_FILE" >> "$JOURNAL_FILE"
    
    echo "// Resumen de cambios:" >> "$JOURNAL_FILE"
    echo "// - $(git log -1 --oneline 2>/dev/null || echo 'Cambios manuales')" >> "$JOURNAL_FILE"
    echo "" >> "$JOURNAL_FILE"

    echo "✅ JOURNAL.md actualizado con cambios del $(git log -1 --oneline 2>/dev/null || echo 'último cambio')"
    cat "$JOURNAL_FILE"
    ;;

  *)
    echo "Uso:"
    echo "  journal init   # Crea SKILL.md y JOURNAL.md"
    echo "  journal review   # Revisa cambios y actualiza JOURNAL.md"
    ;;
esac