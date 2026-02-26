#!/bin/bash
# 🦞 OpenClaw + 飞书 部署工具 - 一键安装脚本

set -e

echo "🦞 欢迎使用 OpenClaw + 飞书一键部署工具！"
echo ""

# 检查 Python
if ! command -v python3 &> /dev/null; then
    echo "❌ 未检测到 Python3，请先安装 Python 3.7+"
    echo "安装指南: https://python.org/downloads"
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2 | cut -d'.' -f1)
if [ "$PYTHON_VERSION" -lt 3 ]; then
    echo "❌ Python 版本过低，需要 3.7+"
    exit 1
fi

echo "✅ Python 版本: $(python3 --version)"

# 下载部署脚本
echo "📥 正在下载部署脚本..."
DEPLOY_URL="https://raw.githubusercontent.com/duka-works/openclaw-feishu-deployer/main/deploy.py"

if command -v curl &> /dev/null; then
    curl -fsSL "$DEPLOY_URL" -o /tmp/openclaw_deploy.py
elif command -v wget &> /dev/null; then
    wget -q "$DEPLOY_URL" -O /tmp/openclaw_deploy.py
else
    echo "❌ 需要 curl 或 wget 来下载脚本"
    exit 1
fi

echo "✅ 下载完成"

# 运行部署脚本
echo ""
echo "🚀 启动部署向导..."
echo ""

python3 /tmp/openclaw_deploy.py

# 清理
rm -f /tmp/openclaw_deploy.py
