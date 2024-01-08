#!/bin/sh
echo "hello"
TOKEN=$1
REPO_OWNER=$2
REPO_NAME=$3
BUG_TITLE=$4
BUG_MSG=$5
curl -L -X POST -H "Accept: application/vnd.github+json" -H "Authorization: Bearer $TOKEN" -H "X-GitHub-Api-Version: 2022-11-28" https://api.github.com/repos/$REPO_OWNER/$REPO_NAME/issues -d "{\"title\":\"$BUG_TITLE\",\"body\":\"$BUG_MSG\",\"labels\":[\"bug\"]}"
