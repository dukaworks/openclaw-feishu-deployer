#!/bin/bash
# 🦞 OpenClaw + 飞书 部署工具 - 一键安装脚本

set -e

echo ""
echo "    🦞 ╔═══════════════════════════════════════╗"
echo "      ║     OpenClaw + Feishu 部署小助手      ║"
echo "      ║        让 AI 助手飞入你的飞书          ║"
echo "      ╚═══════════════════════════════════════╝"
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

# 检查 pip
if ! command -v pip3 &> /dev/null && ! command -v pip &> /dev/null; then
    echo "❌ 未检测到 pip，请先安装 pip"
    exit 1
fi

PIP_CMD=$(command -v pip3 || command -v pip)
echo "✅ pip: $PIP_CMD"

# 安装工具
echo ""
echo "📦 正在安装 openclaw-feishu-deployer..."
"$PIP_CMD" install -q openclaw-feishu-deployer

if [ $? -eq 0 ]; then
    echo "✅ 安装成功！"
else
    echo "⚠️ pip 安装失败，尝试从源码安装..."
    
    # 克隆安装
    TEMP_DIR=$(mktemp -d)
    git clone --depth 1 https://github.com/dukaworks/openclaw-feishu-deployer.git "$TEMP_DIR"
    cd "$TEMP_DIR"
    "$PIP_CMD" install -q -e .
    cd -
    rm -rf "$TEMP_DIR"
fi

echo ""
echo "🚀 启动部署向导..."
echo ""

# 运行部署向导
if command -v openclaw-feishu &> /dev/null; then
    openclaw-feishu deploy
elif command -v ofd &> /dev/null; then
    ofd deploy
else
    python3 -m openclaw_feishu_deployer deploy
fi

echo ""
echo "🎉 安装完成！"
echo ""
echo "常用命令："
echo "  openclaw-feishu deploy    # 重新部署"
echo "  openclaw-feishu status    # 查看状态"
echo "  openclaw-feishu logs      # 查看日志"
echo ""
echo "简写命令："
echo "  ofd deploy"
echo "  ofd status"
echo "  ofd logs"
echo ""
