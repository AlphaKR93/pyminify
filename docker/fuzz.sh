#!/usr/bin/env bash

pip3 install --root-user-action=ignore .

# Check if --timeout is specified
timeout_duration=""
args=()
while [[ $# -gt 0 ]]; do
    case $1 in
        --timeout)
            timeout_duration="$2"
            shift 2
            ;;
        *)
            args+=("$1")
            shift
            ;;
    esac
done

# Run with timeout if specified, otherwise run normally
if [[ -n "$timeout_duration" ]]; then
    exec timeout "$timeout_duration" hypothesis fuzz hypo_test "${args[@]}"
else
    exec hypothesis fuzz hypo_test "${args[@]}"
fi