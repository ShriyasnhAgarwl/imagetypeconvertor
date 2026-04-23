Here’s a **clean, beginner-friendly Markdown guide** you can drop into your repo as `README.md` 👇

---

# 🖼️ Image to WebP CLI Tool

Convert images (`jpg`, `png`, `jpeg`, etc.) into **optimized WebP format** with optional resizing and flexible naming.

---

## 🚀 Features

* Convert multiple image formats → **WebP**
* Optional **resize (width / height / both)**
* Keep original filename OR use prefix
* Recursive folder support
* Adjustable quality
* Safe handling of errors & unsupported files

---

## 📦 Installation

### 1. Install Python (if not already)

Make sure you have Python 3.7+ installed:

```bash
python --version
```

---

### 2. Install dependencies

```bash
pip install pillow
```

---

### 3. Save the script

Save the script as:

```bash
img_to_webp.py
```

---

## ▶️ How to Run

Basic command:

```bash
python img_to_webp.py <folder_path>
```

---

## 📌 Usage Examples

### ✅ 1. Convert all images in a folder

```bash
python img_to_webp.py ./images
```

---

### ✅ 2. Use custom prefix

```bash
python img_to_webp.py ./images --prefix webp_img
```

Output:

```
webp_img_1.webp
webp_img_2.webp
```

---

### ✅ 3. Keep original filenames

```bash
python img_to_webp.py ./images --keep-name
```

Output:

```
photo.webp
banner.webp
```

---

### ✅ 4. Resize (maintain aspect ratio)

```bash
python img_to_webp.py ./images --width 800
```

OR

```bash
python img_to_webp.py ./images --height 600
```

---

### ✅ 5. Resize to exact dimensions

```bash
python img_to_webp.py ./images --width 800 --height 600
```

⚠️ This may stretch images.

---

### ✅ 6. Recursive conversion (subfolders)

```bash
python img_to_webp.py ./images --recursive
```

---

### ✅ 7. Adjust quality (0–100)

```bash
python img_to_webp.py ./images --quality 70
```

💡 Recommended: `70–85` for good compression

---

### ✅ 8. Overwrite existing files

```bash
python img_to_webp.py ./images --overwrite
```

---

## 🧠 How It Works

* Scans the folder for supported image formats
* Converts them to **WebP**
* Saves them in the same directory
* Handles:

  * Corrupt files
  * Unsupported formats
  * Naming conflicts

---

## 📂 Supported Formats

* `.jpg`
* `.jpeg`
* `.png`
* `.bmp`
* `.tiff`
* `.webp`

---

## ⚠️ Common Issues

### ❌ Command not found

Use:

```bash
python3 img_to_webp.py ./images
```

---

### ❌ Permission issues (Linux/Mac)

```bash
chmod +x img_to_webp.py
```

---

### ❌ Pillow not installed

```bash
pip install pillow
```

---

## 🔥 Future Improvements (Optional)

* Multithreading (faster processing)
* GUI (drag & drop)
* Batch resize presets (e.g., thumbnails)
* Integration with frontend build tools

---

## 🙌 Contributing

Feel free to fork and improve!

---
