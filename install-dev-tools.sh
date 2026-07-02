#!/bin/bash
set -e

# Install dev tools to /workspace/bin/ (persists across container restarts)
# Run this from inside the Docker container.

BINDIR="/workspace/bin"
mkdir -p "$BINDIR"

echo "=== Installing gh CLI ==="
python3 -c "
import urllib.request, tarfile, io, os, shutil
url = 'https://github.com/cli/cli/releases/download/v2.58.0/gh_2.58.0_linux_amd64.tar.gz'
data = urllib.request.urlopen(url).read()
t = tarfile.open(fileobj=io.BytesIO(data))
t.extractall(path='/tmp/')
shutil.copy('/tmp/gh_2.58.0_linux_amd64/bin/gh', '/workspace/bin/gh')
os.chmod('/workspace/bin/gh', 0o755)
shutil.rmtree('/tmp/gh_2.58.0_linux_amd64')
"

echo "=== Installing curl ==="
python3 -c "
import urllib.request, os
url = 'https://github.com/moparisthebest/static-curl/releases/download/v8.10.0/curl-amd64'
data = urllib.request.urlopen(url).read()
with open('/workspace/bin/curl', 'wb') as f:
    f.write(data)
os.chmod('/workspace/bin/curl', 0o755)
"

echo "=== Installing sqlite3 CLI ==="
python3 -c "
import urllib.request, zipfile, io, os
# Use older build compatible with glibc 2.36 (Debian 12)
url = 'https://www.sqlite.org/2024/sqlite-tools-linux-x64-3450300.zip'
data = urllib.request.urlopen(url).read()
z = zipfile.ZipFile(io.BytesIO(data))
z.extract('sqlite3', '/workspace/bin/')
os.chmod('/workspace/bin/sqlite3', 0o755)
"

echo "=== Adding /workspace/bin to PATH ==="
# Add to .bashrc if not already there
grep -q 'workspace/bin' ~/.bashrc 2>/dev/null || echo 'export PATH="/workspace/bin:$PATH"' >> ~/.bashrc

echo "=== Done ==="
echo "Run 'source ~/.bashrc' or restart your shell to use the new tools."
