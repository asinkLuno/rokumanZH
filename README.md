# 摇滚大陆漫游记转写+翻译仓库

此仓库用于存储《摇滚大陆漫游记》的转写和翻译内容。

## 文件结构

- **`transcriptions/`**: 存放原始的转写文件。
- **`docs/`**: 可用于存放翻译内容或其他相关文档。
- **`scripts/`**: ASR（自动语音识别）脚本。
  - `whisper.py`: 基于 Whisper 模型的本地转写脚本
  - `vibe_voice_asr.py`: 基于 Vibe Voice API 的在线转写脚本

## 使用方法

### Whisper 本地转写

```bash
python scripts/whisper.py
```

需要安装 PyTorch 和 Transformers 库。

### Vibe Voice API 转写

```bash
python scripts/vibe_voice_asr.py <音频文件路径>
```

需要安装 `gradio_client` 和 `click` 库。脚本会自动读取 `docs/术语表.md` 作为上下文信息。