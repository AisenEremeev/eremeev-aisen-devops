#!/usr/bin/env bash
set -euo pipefail
cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.."
mkdir -p logs backup
touch logs/application.log
cat > logs/application.log <<'LOG'
INFO Application started
INFO User logged in
WARNING Configuration file missing
INFO Database connected
ERROR Database connection failed
INFO Application restarted
WARNING Memory usage is high
INFO Request received
ERROR Request failed
INFO Application stopped
LOG
printf 'Private student notes\n' > private.txt
printf 'Public project information\n' > public.txt
chmod 600 private.txt
chmod 644 public.txt
chmod +x scripts/*.sh
