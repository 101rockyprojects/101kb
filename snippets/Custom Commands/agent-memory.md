#!/bin/bash
case "$1" in
  init)
    bd init
    echo "✅ Beads inicializado"
    ;;
  start|"pour")
    bd mol pour "gt-proyecto-$(date +%Y%m%d)" "$2"
    echo "✅ Bead creado: gt-proyecto-$(date +%Y%m%d)"
    ;;
  list)
    bd mol list
    ;;
  show)
    bd mol show "$2"
    ;;
  *)
    echo "Uso: agent-memory [init|start|list|show <id>]"
    echo "  init    - Inicializa beads"
    echo "  start   - Crea nuevo bead: agent-memory start 'descripción'"
    echo "  list    - Lista beads activos"
    echo "  show id - Muestra bead específico"
    ;;
esac