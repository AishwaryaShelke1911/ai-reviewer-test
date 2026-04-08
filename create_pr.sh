#!/bin/bash

# Get your GitHub token from environment or .netrc
GITHUB_TOKEN=$(git config --global github.token 2>/dev/null || echo "")

if [ -z "$GITHUB_TOKEN" ]; then
  echo "GitHub token not found. Please set GITHUB_TOKEN environment variable."
  echo "Using curl with authentication..."
fi

curl -X POST \
  -H "Accept: application/vnd.github.v3+json" \
  -H "Authorization: token ${GITHUB_TOKEN}" \
  https://api.github.com/repos/AishwaryaShelke1911/ai-reviewer-test/pulls \
  -d '{
    "title": "Security Analysis Test",
    "body": "Testing Claude AI security analysis with vulnerable code patterns",
    "head": "feature/security-test-2024",
    "base": "main"
  }'
