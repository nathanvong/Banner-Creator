# Banner Creator

[English](#english) | [繁體中文](#繁體中文) | [简体中文](#简体中文)

---

## Gallery / 截圖展示

### 1. Image to ASCII (圖片轉字元畫)

| Original Image (原圖) | ASCII Banner Output (終端機輸出) |
| :---: | :---: |
| <img src="https://github.com/user-attachments/assets/7401776d-9886-415b-be26-fa56616c78ea" width="400"> | <img src="https://github.com/user-attachments/assets/8515628f-fbbf-44b5-bab9-04f4fe4278e0" width="400"> |
| <img src="https://github.com/user-attachments/assets/5f0f7358-c472-4289-ad6b-d463d62f9a6a" width="400"> | <img src="https://github.com/user-attachments/assets/8059024f-9bfc-4d68-a766-d606bd1c88a2" width="400"> |
| <img src="https://github.com/user-attachments/assets/3fc3ce79-2d97-43a9-895f-c4f23b596abb" width="400"> | <img src="https://github.com/user-attachments/assets/7c832728-7bb6-4e6c-b393-a51e72aac76e" width="400"> |

### 2. Text to ASCII (純文字轉藝術字)

**Command:** `python banner_creator.py -t "NathanVong"`

```text
 _   _       _   _              __     __
| \ | | __ _| |_| |__   __ _ _ _\ \   / /__  _ __   __ _
|  \| |/ _` | __| '_ \ / _` | '_ \ \ / / _ \| '_ \ / _` |
| |\  | (_| | |_| | | | (_| | | | \ V / (_) | | | | (_| |
|_| \_|\__,_|\__|_| |_|\__,_|_| |_|\_/ \___/|_| |_|\__, |
                                                   |___/
```
<img src="https://github.com/user-attachments/assets/1f0a06b2-0d43-43a7-8bf7-b436e5c5f3ea" width="710">

---

## Command Line Arguments / 參數說明

```text
usage: banner-creator.py [-h] [-t <text>] [-i <file_path>] [-g <float>] [-p <file_path>] [-s] [-r]

Banner Creator - A Python CLI tool that converts images and text into ASCII art and safely integrates them as Linux
terminal startup banners (~/.bashrc).

options:
  -h, --help            show this help message and exit
  -t <text>, --title <text>
                        The text string you want to use as a banner
  -i <file_path>, --image <file_path>
                        File path to the image you want to use as a banner
  -g <float>, --gamma <float>
                        Manually set the gamma value to adjust brightness. Use > 1.0 to darken (increase contrast) or
                        < 1.0 to brighten. This overrides the auto-detection.
  -p <file_path>, --plain-text <file_path>
                        File path to a plain_text text file used as a startup message for new terminal sessions
  -s, --set-banner      Set the generated outputs as terminal banner
  -r, --remove-banner   Remove the banner from terminal
```

---

## English

A command-line interface (CLI) tool written in Python that converts text and images into ASCII art and integrates them as terminal startup banners via `~/.bashrc`.

### Features
*   **Text to ASCII:** Generates text banners using the `pyfiglet` library.
*   **Image to ASCII:** Converts images to ASCII art with adaptive resizing based on current terminal dimensions.
*   **Dynamic Gamma Correction:** Automatically adjusts image contrast based on pixel median to preserve details in overexposed or underexposed images. Manual override is supported.
*   **System Integration:** Provides automated, safe appending and removal of banner configurations in Linux `~/.bashrc` without altering existing user settings.

### Installation
1. Clone this repository or download the source code.
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

### Usage Examples
```bash
# Generate an ASCII text banner (-t)
python banner_creator.py -t "Hello Linux"

# Convert an image to an ASCII banner (-i)
python banner_creator.py -i my_image.jpg

# Append a plain text file below the banner (-p)
python banner_creator.py -i my_image.jpg -p message.txt

# Manually override gamma value (use > 1.0 to darken, < 1.0 to brighten) (-g)
python banner_creator.py -i my_image.jpg -g 1.5

# Combine arguments and set the output as the terminal startup banner (-s)
python banner_creator.py -i my_image.jpg -t "Welcome" -p message.txt -s

# Remove the banner configuration from ~/.bashrc (-r)
python banner_creator.py -r
```

---

## 繁體中文

基於 Python 開發的命令列工具，用於將純文字與圖片轉換為 ASCII 藝術字元，並支援將其整合至 Linux 終端機的啟動畫面 (`~/.bashrc`)。

### 核心功能
*   **文字轉 ASCII：** 透過 `pyfiglet` 產生字元標題。
*   **圖片轉 ASCII：** 支援自適應終端機視窗大小的圖片轉換，並維持視覺比例。
*   **動態 Gamma 校正：** 基於像素中位數自動調整對比度，保留過曝或過暗影像的細節，並支援手動覆蓋參數。
*   **系統整合：** 提供安全的 `.bashrc` 寫入與移除機制，確保不影響使用者現有的系統設定。

### 安裝說明
1. 下載此專案原始碼。
2. 安裝必要的依賴套件：
```bash
pip install -r requirements.txt
```

### 使用範例
```bash
# 生成 ASCII 藝術字標題 (-t)
python banner_creator.py -t "Hello Linux"

# 將圖片轉換為 ASCII 字元畫 (-i)
python banner_creator.py -i my_image.jpg

# 在 Banner 下方附加純文字檔案的內容 (-p)
python banner_creator.py -i my_image.jpg -p message.txt

# 手動設定 Gamma 值 (大於 1.0 增加對比度/變暗，小於 1.0 變亮) (-g)
python banner_creator.py -i my_image.jpg -g 1.5

# 組合多個參數，並將生成的結果設定為終端機啟動畫面 (-s)
python banner_creator.py -i my_image.jpg -t "Welcome" -p message.txt -s

# 從 ~/.bashrc 中移除 Banner 設定 (-r)
python banner_creator.py -r
```

---

## 简体中文

基于 Python 开发的命令行工具，用于将纯文本与图片转换为 ASCII 艺术字符，并支持将其集成至 Linux 终端的启动画面 (`~/.bashrc`)。

### 核心功能
*   **文字转 ASCII：** 通过 `pyfiglet` 生成字符标题。
*   **图片转 ASCII：** 支持自适应终端窗口大小的图片转换，并维持视觉比例。
*   **动态 Gamma 校正：** 基于像素中位数自动调整对比度，保留过曝或过暗图像的细节，并支持手动覆盖参数。
*   **系统集成：** 提供安全的 `.bashrc` 写入与移除机制，确保不影响用户现有的系统配置。

### 安装说明
1. 下载此项目源码。
2. 安装必要的依赖包：
```bash
pip install -r requirements.txt
```

### 使用示例
```bash
# 生成 ASCII 艺术字标题 (-t)
python banner_creator.py -t "Hello Linux"

# 将图片转换为 ASCII 字符画 (-i)
python banner_creator.py -i my_image.jpg

# 在 Banner 下方附加纯文本文件的内容 (-p)
python banner_creator.py -i my_image.jpg -p message.txt

# 手动设置 Gamma 值 (大于 1.0 增加对比度/变暗，小于 1.0 变亮) (-g)
python banner_creator.py -i my_image.jpg -g 1.5

# 组合多个参数，并将生成的结果设置为终端启动画面 (-s)
python banner_creator.py -i my_image.jpg -t "Welcome" -p message.txt -s

# 从 ~/.bashrc 中移除 Banner 配置 (-r)
python banner_creator.py -r
```
