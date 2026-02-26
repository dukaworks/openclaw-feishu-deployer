# 🦞 OpenClaw Feishu Deployer 贡献指南

感谢你的贡献！🎉

## 开发环境设置

```bash
# 1. Fork 并克隆仓库
git clone https://github.com/YOUR_USERNAME/openclaw-feishu-deployer.git
cd openclaw-feishu-deployer

# 2. 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. 安装开发依赖
pip install -e ".[dev]"
```

## 提交 Pull Request 流程

1. **创建分支**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **编写代码**
   - 遵循 PEP 8 规范
   - 添加类型注解
   - 编写测试用例

3. **测试**
   ```bash
   pytest
   black openclaw_feishu_deployer/
   flake8 openclaw_feishu_deployer/
   ```

4. **提交**
   ```bash
   git add .
   git commit -m "🦞 feat: 添加 xxx 功能"
   git push origin feature/your-feature-name
   ```

5. **创建 PR**
   - 描述清楚改动内容
   - 关联相关 Issue
   - 确保 CI 通过

## 代码规范

### 提交信息格式

```
🦞 type: 简短描述

详细说明（可选）

Fixes #123
```

**Type 类型：**
- 🦞 `feat`: 新功能
- 🐛 `fix`: Bug 修复
- 📚 `docs`: 文档更新
- 💅 `style`: 代码格式（不影响功能）
- ♻️ `refactor`: 重构
- 🚀 `perf`: 性能优化
- 🧪 `test`: 测试相关
- 🔧 `chore`: 构建/工具

### 代码风格

```python
# ✅ 正确示例
from typing import Optional, Dict

def deploy_openclaw(
    app_id: str,
    app_secret: str,
    verbose: bool = False
) -> Dict[str, str]:
    """部署 OpenClaw + 飞书
    
    Args:
        app_id: 飞书 App ID
        app_secret: 飞书 App Secret
        verbose: 是否显示详细日志
        
    Returns:
        部署结果字典
    """
    if not app_id or not app_secret:
        raise ValueError("App ID 和 App Secret 不能为空")
    
    # 实现代码...
    return {"status": "success"}
```

## 功能请求

有新想法？欢迎提交 Issue！

### Issue 模板

**标题格式：** `[功能请求] 简短描述`

**内容：**
```markdown
## 功能描述
清晰描述你想要的功能

## 使用场景
在什么情况下会用到这个功能？

## 期望行为
描述期望的功能行为

## 可能的实现方案
（可选）如果你有想法，可以分享
```

## 报告 Bug

**标题格式：** `[Bug] 简短描述`

**内容：**
```markdown
## 环境信息
- OS: macOS 14.1
- Python: 3.11.0
- OpenClaw 版本: 2026.2.2

## 复现步骤
1. 运行 '...'
2. 输入 '...'
3. 看到错误

## 期望结果
应该发生什么？

## 实际结果
实际发生了什么？（附上错误日志）
```

## 许可证

通过提交 PR，你同意你的代码将在 MIT 许可证下发布。

---

🦞 再次感谢你的贡献！
