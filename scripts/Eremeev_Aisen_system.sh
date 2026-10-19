#!/usr/bin/env bash
set -euo pipefail
root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
printf '\n==============================\nStudent Information\n==============================\n'
if [[ -f "$root/Eremeev_Aisen_info.txt" ]]; then
  cat "$root/Eremeev_Aisen_info.txt"
  echo 'Student information file exists.'
else
  echo 'Student information file does not exist.'
fi
printf '\n==============================\nSystem Information\n==============================\n'
printf 'Username: '; whoami
printf 'Hostname: '; hostname
printf 'Current Date: '; date
printf 'Operating System: '; uname -a
echo 'Disk Usage:'; df -h
echo 'Memory Usage:'; free -h
