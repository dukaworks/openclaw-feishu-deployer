# 🦞 OpenClaw + 飞书 一键部署工具

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![OpenClaw](https://img.shields.io/badge/OpenClaw-2026.2+-pink.svg)](https://openclaw.ai)

> **小龙虾出品，必属精品** 🦐✨

让 AI 助手飞入你的飞书！一键自动化部署 OpenClaw 飞书机器人。

![Demo](https://user-images.githubusercontent.com/demo.gif)

## ✨ 特性

- 🎨 **可爱的 CLI 界面** - 彩色输出 + 动画效果，部署不再枯燥
- 🤖 **全自动化流程** - 7 步向导，一键完成所有配置
- 🔍 **智能环境检测** - 自动检查 Node.js、npm 等依赖
- 🛡️ **错误处理** - 友好的错误提示和解决方案
- 📝 **配置保存** - 自动保存配置，方便后续管理
- 🌈 **跨平台支持** - Linux / macOS / Windows WSL

## 🚀 快速开始

### 方式一：直接运行（推荐）

```bash
# 下载并运行
curl -fsSL https://raw.githubusercontent.com/duka-works/openclaw-feishu-deployer/main/deploy.py | python3
```

### 方式二：克隆仓库

```bash
# 克隆项目
git clone https://github.com/duka-works/openclaw-feishu-deployer.git
cd openclaw-feishu-deployer

# 安装依赖
pip install -r requirements.txt

# 运行部署工具
python3 deploy.py
```

## 📋 部署流程

```
┌─────────────────────────────────────────────────────┐
│  1️⃣ 检查环境 → 🔍 检查 Node.js、npm、curl           │
│  2️⃣ 安装 OpenClaw → 🚀 自动下载安装                  │
│  3️⃣ 配置 OpenClaw → ⚙️  设置 LLM API Key            │
│  4️⃣ 启动 Gateway → 🌐 启动本地服务                  │
│  5️⃣ 飞书凭证 → 🤖 输入 App ID / Secret              │
│  6️⃣ 对接配置 → 🔗 连接飞书与 OpenClaw               │
│  7️⃣ 重启验证 → 🎉 完成！                            │
└─────────────────────────────────────────────────────┘
```

## 🎯 前置要求

- Python 3.7+
- Node.js 18+
- 飞书管理员账号（能创建企业自建应用）
- AI 模型 API Key（推荐：Kimi / DeepSeek / Gemini）

## 📖 飞书配置指南

### 1. 创建飞书应用

1. 访问 [飞书开放平台](https://open.feishu.cn)
2. 登录开发者后台
3. 点击「创建企业自建应用」
4. 填写应用名称和描述

### 2. 获取凭证

进入「凭据管理」，复制：
- **App ID**
- **App Secret**

### 3. 开通权限

权限管理 → 批量导入，粘贴以下 JSON：

```json
{
  "permissions": [
    "im:message:send",
    "im:message:receive",
    "im:chat:readonly",
    "contact:user.base:readonly"
  ]
}
```

### 4. 配置事件订阅

事件与回调 → 选择「使用长连接接收事件」→ 添加「接收消息」事件

### 5. 发布应用

版本管理与发布 → 创建版本 → 申请发布 → 审批通过

## 🖥️ 界面预览

```
🦞 ╔═══════════════════════════════════════╗
  ║     OpenClaw + Feishu 部署小助手      ║
  ║        让 AI 助手飞入你的飞书          ║
  ╚═══════════════════════════════════════╝

[████░░░░░░░░░░░] 步骤 1/7
📝 检查环境准备情况 🔍

✅ Node.js 已安装: v20.11.0
✅ npm 已安装
✅ curl 已安装

🦐 正在努力... 🦞 加油加载...
```

## 🛠️ 常用命令

```bash
# 查看状态
openclaw gateway status

# 查看日志
openclaw gateway logs

# 诊断问题
openclaw doctor

# 重启服务
openclaw gateway restart

# 停止服务
openclaw gateway stop
```

## 🐛 故障排查

### 收不到消息？

- [ ] 应用是否已发布为「在线应用」？
- [ ] 事件订阅是否选择「长连接」？
- [ ] 权限是否全部开通并审批？
- [ ] 是否重启了 `openclaw gateway restart`？

### Gateway 启动失败？

```bash
# 检查端口占用
lsof -i :18789

# 手动启动查看错误
openclaw gateway start
```

### 更多问题？

- 📚 [OpenClaw 文档](https://docs.openclaw.ai)
- 🐛 [GitHub Issues](https://github.com/openclaw/openclaw/issues)
- 💬 [飞书社区](https://open.feishu.cn/community)

## 🤝 贡献

欢迎 Issue 和 PR！让我们一起让部署更简单 🦞

## 📄 许可证

MIT License © 2025 Duka Works

---

<p align="center">
  🦞 <strong>Made with love by 小龙虾</strong> 🦞
</p>
