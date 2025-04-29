# M3U8_LiveDL

## 项目简介
这是一个使用Python编写的简易m3u8直播流下载器，封装了ffmpeg命令行调用。
支持：

- 复制所有流，包括视频、音频、字幕（特别是ARIB字幕）等ffmpeg可以识别的流

- 不中断地下载直播流（m3u8格式）

- 实时打印并保存ffmpeg输出日志到本地log文件

- 通过键盘快捷键`q`或`Ctrl+C`优雅中止下载

---

## 使用说明

### 环境要求

- Windows（已经过测试）

- Python 3.x

- 安装并配置好ffmpeg到Windows系统环境变量

- 安装必要Python模块：`keyboard`，可在Powershell中执行下面的代码：

```bash
pip install keyboard
```

## 使用方法

**1. 运行脚本（双击文件或在目录下打开PowerShell / CMD）**
```bash
python download_m3u8.py
```

对于使用可执行程序的用户，可直接双击该exe文件。


**2. 根据提示输入：**

- m3u8流地址

- 输出文件路径（包含文件名，如 output/video.mp4）

**3. 下载过程中，你可以：**

- 实时输出ffmpeg日志

- 按下键盘 `q` 键或 `Ctrl+C` 中断录制

**4. 下载完成后：**

- 显示下载结果（成功/失败）

- 所有日志保存在同一目录下的 ffmpeg_output.log

## 输入示例
```bash
请输入m3u8地址：https://example.com/playlist.m3u8
请输入输出文件路径（带文件名）：C:/output/video.ts
```

（注意：Windows路径可以使用正斜杠 `/` 或双反斜杠 `\\`）


## 注意事项
- `keyboard`模块在某些平台需要管理员/Root权限才能监听快捷键。

    对于Windows用户，建议以管理员身份运行 PowerShell，然后执行安装模块的操作：
```bash
pip install keyboard
```
	
- 输入的m3u8地址需确保可直接访问（如需认证，请先处理好Cookie/Token）

- 断电、中断或其他外部异常可能导致文件不完整

---

## 许可证
本项目使用 MIT License 开源。
自由使用、修改、商用，但需保留原作者署名。

##  感谢

**本项目使用了开源工具[ffmpeg](https://ffmpeg.org/)进行媒体下载与处理。感谢ffmpeg开发社区的贡献！**
