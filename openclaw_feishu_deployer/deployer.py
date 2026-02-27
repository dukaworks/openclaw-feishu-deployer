#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🦞 OpenClaw + 飞书 自动化部署工具
      小龙虾出品，必属精品
"""

import os
import sys
import json
import time
import subprocess
import requests
from pathlib import Path
from typing import Optional, Tuple

# 颜色代码 🎨
class Colors:
    PINK = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

# 可爱的 ASCII 艺术 🦞
LOGO = f"""
{Colors.PINK}
    🦞 ╔═══════════════════════════════════════╗
      ║     OpenClaw + Feishu 部署小助手      ║
      ║        让 AI 助手飞入你的飞书          ║
      ╚═══════════════════════════════════════╝
{Colors.END}
"""

SUCCESS_ART = f"""
{Colors.GREEN}
    ✨ 🎉 ✨ 🎉 ✨ 🎉 ✨ 🎉 ✨
    
         部署成功啦！
       🦞 小龙虾为你骄傲 🦞
    
    ✨ 🎉 ✨ 🎉 ✨ 🎉 ✨ 🎉 ✨
{Colors.END}
"""

ERROR_ART = f"""
{Colors.RED}
    💥 (╯°□°)╯︵ ┻━┻  
    
    哎呀！出错了...
    不过没关系，小龙虾陪你一起解决！
{Colors.END}
"""

# 可爱的加载动画
LOADING_FRAMES = [
    "🦐 正在努力",
    "🦐 正在努力.",
    "🦐 正在努力..",
    "🦐 正在努力...",
    "🦞 加油加载",
    "🦞 加油加载.",
    "🦞 加油加载..",
    "🦞 加油加载...",
]

def print_logo():
    """打印Logo"""
    print(LOGO)

def print_step(step_num: int, total: int, message: str):
    """打印步骤进度"""
    progress = "█" * step_num + "░" * (total - step_num)
    print(f"\n{Colors.CYAN}[{progress}] 步骤 {step_num}/{total}{Colors.END}")
    print(f"{Colors.BOLD}📝 {message}{Colors.END}\n")

def print_success(message: str):
    """打印成功信息"""
    print(f"{Colors.GREEN}✅ {message}{Colors.END}")

def print_error(message: str):
    """打印错误信息"""
    print(f"{Colors.RED}❌ {message}{Colors.END}")

def print_info(message: str):
    """打印信息"""
    print(f"{Colors.BLUE}ℹ️  {message}{Colors.END}")

def print_warning(message: str):
    """打印警告"""
    print(f"{Colors.YELLOW}⚠️  {message}{Colors.END}")

def cute_input(prompt: str) -> str:
    """可爱的输入提示"""
    return input(f"{Colors.PINK}🎯 {prompt} {Colors.END}")

def loading_animation(duration: float = 1.5):
    """加载动画"""
    import itertools
    start_time = time.time()
    for frame in itertools.cycle(LOADING_FRAMES):
        if time.time() - start_time > duration:
            break
        print(f"\r{frame}", end="", flush=True)
        time.sleep(0.3)
    print("\r" + " " * 20 + "\r", end="")

def run_command(cmd: str, description: str = "", check: bool = True) -> Tuple[bool, str]:
    """运行命令并返回结果"""
    if description:
        print_info(description)
    
    loading_animation(0.5)
    
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True,
            timeout=60
        )
        
        if check and result.returncode != 0:
            print_error(f"命令执行失败: {cmd}")
            if result.stderr:
                print(f"{Colors.RED}错误详情: {result.stderr[:200]}{Colors.END}")
            return False, result.stderr
        
        return True, result.stdout
    except subprocess.TimeoutExpired:
        print_error("命令执行超时")
        return False, "Timeout"
    except Exception as e:
        print_error(f"命令执行异常: {e}")
        return False, str(e)

def check_prerequisites() -> bool:
    """检查前置条件"""
    print_step(1, 7, "检查环境准备情况 🔍")
    
    all_good = True
    
    # 检查 Node.js
    success, version = run_command("node -v", "检查 Node.js 版本...", check=False)
    if success and version.strip():
        print_success(f"Node.js 已安装: {version.strip()}")
        # 检查版本号
        version_num = version.strip().replace('v', '').split('.')[0]
        if int(version_num) < 18:
            print_error("Node.js 版本需要 18+，请升级")
            all_good = False
    else:
        print_error("Node.js 未安装，请先安装 Node.js 18+")
        print_info("安装指南: https://nodejs.org/")
        all_good = False
    
    # 检查 npm
    success, _ = run_command("npm -v", "检查 npm...", check=False)
    if success:
        print_success("npm 已安装")
    else:
        print_error("npm 未安装")
        all_good = False
    
    # 检查 curl
    success, _ = run_command("which curl", "检查 curl...", check=False)
    if success:
        print_success("curl 已安装")
    else:
        print_warning("curl 未安装，某些功能可能受限")
    
    return all_good

def install_openclaw() -> bool:
    """安装 OpenClaw"""
    print_step(2, 7, "安装 OpenClaw 🚀")
    
    # 检查是否已安装
    success, _ = run_command("which openclaw", "检查 OpenClaw 是否已安装...", check=False)
    if success:
        print_success("OpenClaw 已安装，跳过安装步骤")
        return True
    
    print_info("正在安装 OpenClaw...")
    
    # 尝试多种安装方式
    install_methods = [
        ("curl 安装", "curl -fsSL https://openclaw.ai/install.sh | bash"),
        ("npm 全局安装", "npm install -g openclaw"),
    ]
    
    for method_name, cmd in install_methods:
        print_info(f"尝试 {method_name}...")
        success, _ = run_command(cmd, f"使用 {method_name}...")
        if success:
            print_success(f"OpenClaw 安装成功！({method_name})")
            return True
    
    print_error("OpenClaw 安装失败，请手动安装")
    print_info("手动安装指南: https://docs.openclaw.ai")
    return False

def configure_openclaw() -> bool:
    """配置 OpenClaw"""
    print_step(3, 7, "配置 OpenClaw ⚙️")
    
    print_info("启动 OpenClaw 配置向导...")
    print_warning("请按提示完成以下配置：")
    print("  1. 选择 LLM 提供商 (推荐: Gemini/Kimi/DeepSeek)")
    print("  2. 输入 API Key")
    print("  3. 其他选项保持默认即可")
    print("")
    
    input(f"{Colors.YELLOW}按 Enter 开始配置...{Colors.END}")
    
    # 运行 onboard
    success, _ = run_command("openclaw onboard", "运行配置向导...")
    if not success:
        print_warning("配置向导可能已运行过，继续下一步...")
    
    return True

def start_gateway() -> bool:
    """启动 Gateway"""
    print_step(4, 7, "启动 Gateway 服务 🌐")
    
    # 检查是否已在运行
    success, _ = run_command("pgrep -f 'openclaw gateway'", check=False)
    if success:
        print_success("Gateway 已在运行")
        return True
    
    print_info("正在启动 Gateway...")
    
    # 后台启动
    success, _ = run_command("openclaw gateway start --daemon", "启动 Gateway 服务...")
    if success:
        time.sleep(3)  # 等待启动
        print_success("Gateway 启动成功！")
        print_info("Dashboard: http://127.0.0.1:18789")
        return True
    else:
        print_error("Gateway 启动失败")
        return False

def collect_feishu_credentials() -> Optional[dict]:
    """收集飞书凭证"""
    print_step(5, 7, "配置飞书机器人 🤖")
    
    print(f"""
{Colors.CYAN}请先在飞书开放平台完成以下操作：
{Colors.END}
1. 访问 {Colors.UNDERLINE}https://open.feishu.cn{Colors.END}
2. 创建「企业自建应用」
3. 进入「凭据管理」获取 App ID 和 App Secret
4. 开通权限并发布应用

{Colors.YELLOW}📖 详细教程: https://github.com/dukaworks/openclaw-feishu-deployer{Colors.END}
    """)
    
    print(f"\n{Colors.GREEN}现在输入你的飞书应用凭证：{Colors.END}\n")
    print(f"{Colors.DIM}提示：App ID 是公开标识符，App Secret 是密钥（输入时可见）{Colors.END}\n")
    
    app_id = cute_input("App ID: ").strip()
    app_secret = cute_input("App Secret: ").strip()
    
    if not app_id or not app_secret:
        print_error("App ID 和 App Secret 不能为空")
        return None
    
    return {
        "app_id": app_id,
        "app_secret": app_secret
    }

def configure_feishu(credentials: dict) -> bool:
    """配置飞书集成"""
    print_step(6, 7, "对接飞书与 OpenClaw 🔗")
    
    # 创建配置目录
    config_dir = Path.home() / ".openclaw"
    config_dir.mkdir(exist_ok=True)
    
    # 尝试通过命令行配置
    print_info("正在配置飞书通道...")
    
    # 使用 openclaw config 命令
    config_script = f"""
import subprocess
import time

# 这里可以通过 subprocess 与 openclaw config 交互
# 或者修改配置文件
"""
    
    # 更直接的方式：提示用户使用 Dashboard
    print(f"""
{Colors.CYAN}请手动完成最后一步配置：{Colors.END}

1. 打开 Dashboard: {Colors.UNDERLINE}http://127.0.0.1:18789{Colors.END}
2. 点击「Config」
3. 找到 channels.feishu 部分
4. 填入以下信息：
   
   {Colors.GREEN}appId: {credentials['app_id']}{Colors.END}
   {Colors.GREEN}appSecret: {credentials['app_secret']}{Colors.END}
   {Colors.GREEN}domain: larkoffice.com (国内选这个){Colors.END}
   {Colors.GREEN}enabled: true{Colors.END}

5. 保存配置
    """)
    
    input(f"{Colors.YELLOW}配置完成后按 Enter 继续...{Colors.END}")
    
    return True

def restart_and_verify() -> bool:
    """重启并验证"""
    print_step(7, 7, "重启服务并验证 🎉")
    
    print_info("正在重启 Gateway...")
    success, _ = run_command("openclaw gateway restart", "重启 Gateway...")
    if not success:
        print_warning("重启命令失败，尝试手动重启...")
        run_command("pkill -f 'openclaw gateway'", check=False)
        time.sleep(2)
        run_command("openclaw gateway start --daemon", check=False)
    
    time.sleep(5)  # 等待服务启动
    
    # 检查状态
    print_info("检查服务状态...")
    success, output = run_command("openclaw gateway status", check=False)
    
    if success and "feishu" in output.lower():
        print_success("飞书通道状态正常！")
    else:
        print_warning("请手动检查状态: openclaw gateway status")
    
    print(f"""
{Colors.GREEN}🎊 部署完成！{Colors.END}

现在你可以在飞书中：
  1. 搜索你的机器人名称
  2. 发送消息测试
  3. 在群聊中 @机器人

{Colors.CYAN}常用命令：
  openclaw gateway status    # 查看状态
  openclaw gateway logs      # 查看日志
  openclaw doctor           # 诊断问题{Colors.END}
    """)
    
    return True

def save_config(credentials: dict):
    """保存配置到文件"""
    config = {
        "app_id": credentials["app_id"],
        "app_secret": "***隐藏***",
        "domain": "larkoffice.com",
        "enabled": True
    }
    
    config_file = Path.home() / ".openclaw" / "feishu_config.json"
    with open(config_file, 'w') as f:
        json.dump(config, f, indent=2)
    
    print_info(f"配置已保存到: {config_file}")

def main():
    """主函数"""
    import sys
    
    # 处理命令行参数
    if len(sys.argv) > 1:
        if sys.argv[1] in ('--version', '-v'):
            print(f"openclaw-feishu-deployer {__version__}")
            sys.exit(0)
        elif sys.argv[1] in ('--help', '-h'):
            print_logo()
            print(f"{Colors.CYAN}🦞 OpenClaw Feishu Deployer v{__version__}{Colors.END}\n")
            print("用法:")
            print("  ofd                    启动部署向导")
            print("  ofd --version, -v      显示版本号")
            print("  ofd --help, -h         显示帮助")
            print("\n命令别名:")
            print("  openclaw-feishu")
            sys.exit(0)
    
    print_logo()
    
    print(f"{Colors.CYAN}你好！我是你的 OpenClaw + 飞书部署小助手 🦞{Colors.END}")
    print(f"{Colors.CYAN}我会一步步带你完成部署~{Colors.END}\n")
    
    # 检查前置条件
    if not check_prerequisites():
        print(ERROR_ART)
        print_error("环境检查未通过，请修复后重试")
        sys.exit(1)
    
    # 安装 OpenClaw
    if not install_openclaw():
        print(ERROR_ART)
        print_error("OpenClaw 安装失败")
        sys.exit(1)
    
    # 配置 OpenClaw
    if not configure_openclaw():
        print_warning("配置可能未完成，继续尝试...")
    
    # 启动 Gateway
    if not start_gateway():
        print(ERROR_ART)
        print_error("Gateway 启动失败")
        sys.exit(1)
    
    # 收集飞书凭证
    credentials = collect_feishu_credentials()
    if not credentials:
        print(ERROR_ART)
        print_error("凭证收集失败")
        sys.exit(1)
    
    # 保存配置
    save_config(credentials)
    
    # 配置飞书
    if not configure_feishu(credentials):
        print_warning("飞书配置可能需要手动完成")
    
    # 重启验证
    restart_and_verify()
    
    # 成功！
    print(SUCCESS_ART)
    
    print(f"{Colors.PINK}🦞 感谢使用！有问题随时召唤我~{Colors.END}\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.YELLOW}👋 用户取消，下次再见！{Colors.END}")
        sys.exit(0)
    except Exception as e:
        print(ERROR_ART)
        print_error(f"发生错误: {e}")
        sys.exit(1)

# 为了兼容性，保留 main 函数名
def cli_main():
    """CLI 入口"""
    main()
