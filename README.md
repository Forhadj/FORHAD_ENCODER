<h1 align="center">💻 FORHAD_ENCODER</h1>
<p align="center">
  <b>Marshal + Zlib + Base64 based Python Encoder</b><br>
  Cython compiled (.so) with colorful animated UI, banner and full CLI tool support.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Platform-Termux%20%7C%20Linux-green?style=flat-square">
  <img src="https://img.shields.io/badge/Protected-Cython.so-blue?style=flat-square">
  <img src="https://img.shields.io/badge/Obfuscation-Marshal%7CZlib%7CB64-red?style=flat-square">
</p>

---

## 📸 Screenshot

<p align="center">
  <img src="https://github.com/Forhadj/FORHAD_ENCODER/assets/your-screenshot-path.jpg" width="600"/>
</p>

> Banner, Encoding Result & Menu shown after 15x encoding and `.so` protection

---

## ⚙️ Features

- ✅ Python encoder using `marshal`, `zlib`, and `base64`
- ✅ Fully compiled `.so` protection via Cython
- ✅ Colorful ASCII art and menu-driven CLI
- ✅ Encode count, file size calculation
- ✅ Support for B16, B32, B64, Zlib, Marshal
- ✅ No decoding system – full obfuscation for protection

---

## 🔧 Installation & Usage

### 📱 For Termux:

```bash
pkg update && pkg install python -y
pip install cython

git clone https://github.com/Forhadj/FORHAD_ENCODER
cd FORHAD_ENCODER
chmod +x *
python Forhad.py
```

### 🐧 For Linux:

```bash
sudo apt update && sudo apt install python3 -y
pip3 install cython

git clone https://github.com/Forhadj/FORHAD_ENCODER
cd FORHAD_ENCODER
chmod +x *
python3 Forhad.py
```

---

## 🔐 How to Encode a `.py` File to `.so`

✅ **Step-by-step example (as shown in screenshot):**

Suppose you encoded a file **15 times** like this:

```bash
# Original file
/storage/emulated/0/Download/tow.py

# After encoding using FORHAD_ENCODER:
Encoded Count : 115
Saved as: /storage/emulated/0/download/tow_FORHAD-EHC99.py
```

Now, convert the encoded `.py` to `.so` using Cython:

```bash
cp /storage/emulated/0/download/tow_FORHAD-EHC99.py iq.py
cythonize -i iq.py
```

You will get:

```
iq.c
iq.cpython-312.so
```

✅ You can now import `iq` in any Python project as a protected `.so` module.

---

## 🛠 File Structure

```
FORHAD_ENCODER/
├── Forhad.py              # Launcher script (calls ff.MainMenu)
├── ff.cpython-312.so      # Main encoded tool as .so
├── LICENSE
├── README.md
└── [your encoded .py or .so files]
```

---

## ❗ Tips

- Use `cythonize -i filename.py` to convert `.py` to `.so`
- Rename file before conversion (e.g. to `iq.py`)
- To inspect methods in `.so`:
  ```bash
  python3 -c "import iq; print(dir(iq))"
  ```

---

## 🧠 Dev Info

- 👨‍💻 Developer: [@Forhadj](https://github.com/Forhadj)
- 📣 Telegram: [@f_forha](https://t.me/f_forha)
- 🌐 From: Bangladesh 🇧🇩
- 🛠 Tools Used: Python, Cython, Termux

---

## ⭐ Support

If you like this project:

- 🌟 Star this repo
- 📤 Share with your friends
- 🧠 Learn how Python protection works!

---
