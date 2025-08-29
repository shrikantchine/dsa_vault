#!/bin/bash
# DSA Revision Helper Script
# Quick access to revision management commands

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON_SCRIPT="$SCRIPT_DIR/revision_manager.py"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

show_help() {
    echo -e "${BLUE}DSA Revision Helper${NC}"
    echo "===================="
    echo ""
    echo "Usage: $0 <command> [options]"
    echo ""
    echo "Commands:"
    echo -e "  ${GREEN}today${NC}           Show topics due for review today"
    echo -e "  ${GREEN}random${NC}          Get a random topic for quick review"
    echo -e "  ${GREEN}random ds${NC}       Get random data structure topic"
    echo -e "  ${GREEN}random algo${NC}     Get random algorithm topic"
    echo -e "  ${GREEN}random math${NC}     Get random math concept"
    echo -e "  ${GREEN}update${NC}          Update topic after review"
    echo -e "  ${GREEN}report${NC}          Generate daily review report"
    echo -e "  ${GREEN}stats${NC}           Show revision statistics"
    echo -e "  ${GREEN}help${NC}            Show this help message"
    echo ""
    echo "Examples:"
    echo "  $0 today"
    echo "  $0 random"
    echo "  $0 update \"Sorting\" 4 \"Need more heap sort practice\""
    echo ""
}

if [ $# -eq 0 ]; then
    show_help
    exit 0
fi

case "$1" in
    "today"|"due")
        echo -e "${YELLOW}📅 Today's Review Schedule${NC}"
        echo "=========================="
        python3 "$PYTHON_SCRIPT" due
        ;;
    "random")
        category=""
        if [ $# -gt 1 ]; then
            case "$2" in
                "ds"|"data"|"datastructures")
                    category="data_structures"
                    ;;
                "algo"|"algorithms")
                    category="algorithms"
                    ;;
                "math"|"mathematics")
                    category="math"
                    ;;
                "tech"|"techniques")
                    category="techniques"
                    ;;
            esac
        fi
        echo -e "${YELLOW}🎲 Random Topic${NC}"
        echo "==============="
        python3 "$PYTHON_SCRIPT" random $category
        ;;
    "update")
        if [ $# -lt 3 ]; then
            echo -e "${RED}Error: Missing arguments${NC}"
            echo "Usage: $0 update <topic> <confidence> [notes]"
            echo "Example: $0 update \"Sorting\" 4 \"Need more practice\""
            exit 1
        fi
        echo -e "${YELLOW}📝 Updating Topic${NC}"
        echo "=================="
        python3 "$PYTHON_SCRIPT" update "$2" "$3" "$4"
        ;;
    "report")
        echo -e "${YELLOW}📊 Daily Report${NC}"
        echo "==============="
        python3 "$PYTHON_SCRIPT" report
        ;;
    "stats"|"statistics")
        echo -e "${YELLOW}📈 Statistics${NC}"
        echo "============="
        python3 "$PYTHON_SCRIPT" stats
        ;;
    "help"|"-h"|"--help")
        show_help
        ;;
    *)
        echo -e "${RED}Error: Unknown command '$1'${NC}"
        echo ""
        show_help
        exit 1
        ;;
esac