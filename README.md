# Snake Game (贪吃蛇游戏)

这是一个基于 Python 和 Pygame 实现的经典贪吃蛇小游戏。

## 功能特性
- 方向键控制蛇移动
- 吃到食物蛇会变长，分数增加
- 撞墙或撞到自己游戏结束
- 游戏结束后按空格键重开，按 Q/q 退出
- 支持虚拟环境和依赖隔离
- 支持自动构建 Windows 可执行文件
- 支持 PyPI 包发布

## 环境依赖
- Python 3.11（推荐 3.10 及以上）
- Pygame 2.6.1 及以上

## 快速开始

### 方法一：从 PyPI 安装
```sh
pip install snake-game
python -m snake_game.game
```

### 方法二：从源码运行
1. **克隆仓库**
   ```sh
   git clone <your-repo-url>
   cd <your-repo-dir>
   ```
2. **创建并激活虚拟环境（推荐使用 uv 或 venv）**
   ```sh
   uv venv
   .venv\Scripts\activate  # Windows
   # 或 source .venv/bin/activate  # Linux/Mac
   ```
3. **安装依赖**
   ```sh
   pip install pygame
   ```
4. **运行游戏**
   ```sh
   python src/snake_game/game.py
   ```

## 获取可执行文件
项目使用 GitHub Actions 自动构建 Windows 可执行文件。你可以通过以下方式获取：

1. 访问项目的 [Releases 页面](https://github.com/hackcpp/snake_game/releases)
2. 下载最新版本的可执行文件

或者，你也可以在本地构建：
```sh
pip install pyinstaller
pyinstaller --onefile --windowed --name snake_game src/snake_game/game.py
```
构建完成后，可执行文件将位于 `dist` 目录中。

## 发布新版本
要发布新版本，请按以下步骤操作：

1. 更新代码并提交更改
2. 创建新的 tag（例如：v1.0.0）
   ```sh
   git tag v1.0.0
   git push origin v1.0.0
   ```
3. 在 GitHub 仓库页面创建新的 release
4. GitHub Actions 将自动：
   - 构建 Windows 可执行文件
   - 发布 PyPI 包
   - 创建 GitHub Release 并上传 exe 文件

## 详细使用方法
- **游戏控制**：使用方向键（↑、↓、←、→）控制蛇的移动方向。
- **游戏结束**：当蛇撞到墙壁或自身时，游戏结束。此时按空格键重新开始，按 Q/q 退出游戏。
- **分数计算**：每吃到一个食物，蛇的长度增加，分数加 1。

## 常见问题排查
- **窗口无法弹出/按键无响应**：请确保已激活虚拟环境并正确安装 pygame，且输入法为英文。
- **Q/q 退出无效**：请确保窗口获得焦点，且 pygame 版本为 2.0 及以上。
- **如遇其他问题**，建议升级 Python、Pygame 或在新环境下重试。

## 目录结构
```
├── src/
│   └── snake_game/
│       ├── game.py
│       └── __init__.py
├── .github/
│   └── workflows/
│       └── build.yml
├── .gitignore
├── README.md
├── pyproject.toml
├── requirements.txt
└── .venv/  # 虚拟环境（已被忽略）
```

## 贡献指南
欢迎提交 issue 或 PR 来改进项目！请确保你的代码符合项目规范，并附上详细的说明。

---
如有更多问题或建议，欢迎随时联系！ 