# 🦞 OpenClaw Feishu Deployer

[![PyPI version](https://img.shields.io/pypi/v/openclaw-feishu-deployer.svg)](https://pypi.org/project/openclaw-feishu-deployer/)
[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![OpenClaw](https://img.shields.io/badge/OpenClaw-2026.2+-pink.svg)](https://openclaw.ai)
[![GitHub stars](https://img.shields.io/github/stars/dukaworks/openclaw-feishu-deployer.svg?style=social)](https://github.com/dukaworks/openclaw-feishu-deployer/stargazers)

> **小龙虾出品，必属精品** 🦐✨  
> 让 AI 助手飞入你的飞书！一键自动化部署，从未如此简单。

<p align="center">
  <img src="https://raw.githubusercontent.com/dukaworks/openclaw-feishu-deployer/main/assets/demo.gif" alt="Demo" width="600">
</p>

## ✨ 为什么选择我们？

| 特性 | 描述 |
|------|------|
| 🎨 **可爱 CLI** | 彩色输出 + 动画效果，部署不再枯燥 |
| 🤖 **全自动化** | 7 步向导，一键完成所有配置 |
| 🔍 **智能检测** | 自动检查环境依赖，给出解决方案 |
| 🛡️ **错误恢复** | 友好的错误提示，自动重试机制 |
| 📝 **配置管理** | 自动保存配置，支持多次部署 |
| 🌈 **跨平台** | Linux / macOS / Windows WSL 全支持 |

## 🚀 快速开始

### 方式一：pip 安装（推荐）

```bash
# 安装
pip install openclaw-feishu-deployer

# 运行
openclaw-feishu deploy
# 或简写
ofd deploy
```

### 方式二：一键脚本

```bash
curl -fsSL https://raw.githubusercontent.com/dukaworks/openclaw-feishu-deployer/main/install.sh | bash
```

### 方式三：克隆运行

```bash
git clone https://github.com/dukaworks/openclaw-feishu-deployer.git
cd openclaw-feishu-deployer
pip install -r requirements.txt
python -m openclaw_feishu_deployer deploy
```

## 📋 部署流程

```
┌────────────────────────────────────────────────────────────┐
│                                                            │
│   🦞 步骤 1/7  检查环境        🔍 Node.js / npm / curl     │
│   ─────────────────────────────────────────────────────   │
│   🚀 步骤 2/7  安装 OpenClaw   📦 自动下载安装              │
│   ─────────────────────────────────────────────────────   │
│   ⚙️  步骤 3/7  配置 OpenClaw   🔧 设置 LLM API Key        │
│   ─────────────────────────────────────────────────────   │
│   🌐 步骤 4/7  启动 Gateway    🔄 启动本地服务            │
│   ─────────────────────────────────────────────────────   │
│   🤖 步骤 5/7  飞书凭证        📝 输入 App ID / Secret     │
│   ─────────────────────────────────────────────────────   │
│   🔗 步骤 6/7  对接配置        🔌 连接飞书与 OpenClaw      │
│   ─────────────────────────────────────────────────────   │
│   🎉 步骤 7/7  重启验证        ✅ 完成！                   │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

## 🎯 前置要求

- Python 3.7+
- Node.js 18+
- 飞书管理员账号
- AI 模型 API Key（推荐：Kimi / DeepSeek / Gemini）

## 📖 详细教程

### 1. 飞书开放平台配置

<details>
<summary>点击查看详细步骤 👇</summary>

#### 1.1 创建应用

1. 访问 [飞书开放平台](https://open.feishu.cn)
2. 登录开发者后台 → 创建企业自建应用
3. 填写应用名称（如"AI助手"）、描述、上传图标

#### 1.2 获取凭证

进入「凭据管理」，复制以下信息（后面会用到）：
- **App ID**
- **App Secret**

#### 1.3 开通权限

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

#### 1.4 配置事件订阅

事件与回调 → 选择「使用长连接接收事件」→ 添加「接收消息」事件

#### 1.5 发布应用

版本管理与发布 → 创建版本（1.0.0）→ 申请发布 → 审批通过

</details>

### 2. 运行部署工具

```bash
# 运行部署向导
openclaw-feishu deploy

# 查看帮助
openclaw-feishu --help

# 查看状态
openclaw-feishu status

# 查看日志
openclaw-feishu logs
```

### 3. 测试机器人

1. 在飞书搜索你的机器人名称
2. 发送 "你好" 测试回复
3. 在群聊中 @机器人 测试

## 🖥️ 界面预览

```bash
$ openclaw-feishu deploy

    🦞 ╔═══════════════════════════════════════╗
      ║     OpenClaw + Feishu 部署小助手      ║
      ║        让 AI 助手飞入你的飞书          ║
      ╚═══════════════════════════════════════╝

你好！我是你的 OpenClaw + 飞书部署小助手 🦞
我会一步步带你完成部署~

[████░░░░░░░░░░░] 步骤 1/7
📝 检查环境准备情况 🔍

✅ Node.js 已安装: v20.11.0
✅ npm 已安装  
✅ curl 已安装

🦐 正在努力... 🦞 加油加载...

✅ OpenClaw 安装成功！

    ✨ 🎉 ✨ 🎉 ✨ 🎉 ✨ 🎉 ✨
    
         部署成功啦！
       🦞 小龙虾为你骄傲 🦞
    
    ✨ 🎉 ✨ 🎉 ✨ 🎉 ✨ 🎉 ✨
```

## 🛠️ CLI 命令

```bash
# 部署向导（交互式）
openclaw-feishu deploy

# 快速部署（非交互式，用于 CI/CD）
openclaw-feishu deploy --app-id xxx --app-secret xxx --api-key xxx

# 查看 OpenClaw 状态
openclaw-feishu status

# 查看日志
openclaw-feishu logs

# 重启服务
openclaw-feishu restart

# 停止服务
openclaw-feishu stop

# 诊断问题
openclaw-feishu doctor

# 配置管理
openclaw-feishu config get
openclaw-feishu config set key=value
```

## 🐛 故障排查

<details>
<summary>常见问题 👇</summary>

### Q: 收不到消息？
- [ ] 应用是否已发布为「在线应用」？
- [ ] 事件订阅是否选择「长连接」？
- [ ] 权限是否全部开通并审批？
- [ ] 是否重启了 `openclaw-feishu restart`？

### Q: Gateway 启动失败？
```bash
# 检查端口占用
lsof -i :18789

# 查看详细错误
openclaw-feishu logs
```

### Q: 如何更新？
```bash
pip install -U openclaw-feishu-deployer
```

</details>

## 🤝 贡献指南

欢迎贡献！请阅读 [CONTRIBUTING.md](CONTRIBUTING.md) 了解如何参与。

### 开发环境

```bash
# 克隆仓库
git clone https://github.com/dukaworks/openclaw-feishu-deployer.git
cd openclaw-feishu-deployer

# 创建虚拟环境
python -m venv venv
source venv/bin/activate

# 安装开发依赖
pip install -e ".[dev]"

# 运行测试
pytest

# 代码格式化
black openclaw_feishu_deployer/
flake8 openclaw_feishu_deployer/
```

## 📊 项目统计

![Alt](https://repobeats.axiom.co/api/embed/xxx "Repobeats analytics image")

## 📝 更新日志

查看 [CHANGELOG.md](CHANGELOG.md) 了解版本更新历史。

## 📄 许可证

[MIT License](LICENSE) © 2025 Duka Works

---

<p align="center">
  <img src="https://raw.githubusercontent.com/dukaworks/openclaw-feishu-deployer/main/assets/logo.png" width="100" alt="Logo">
  <br><br>
  🦞 <strong>Made with love by 小龙虾</strong> 🦞
  <br>
  <a href="https://github.com/dukaworks/openclaw-feishu-deployer">GitHub</a> •
  <a href="https://pypi.org/project/openclaw-feishu-deployer">PyPI</a> •
  <a href="https://openclaw.ai">OpenClaw</a>
</p>
