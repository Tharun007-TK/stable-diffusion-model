# Stable Bud - Text-to-Image Generator

Stable Bud is a simple desktop GUI application that uses the Stable Diffusion model to generate images from text prompts. Built with `tkinter` and `customtkinter`, this app allows users to enter a prompt, click a button, and see a beautiful AI-generated image — all within a desktop window.

<!-- Optional: Add screenshot -->

## 🚀 Features

* ✅ Generate high-quality AI images from text
* ✅ Uses Hugging Face's `diffusers` and `StableDiffusionPipeline`
* ✅ Works on both **CPU and GPU** automatically
* ✅ Simple, modern UI using `customtkinter`
* ✅ Images are saved locally as `generatedimage.png`

## 🛠️ Technologies Used

* `Python 3.8+`
* `torch` (PyTorch)
* `diffusers` from Hugging Face
* `transformers` (optional for token auth)
* `customtkinter` (modern UI wrapper for tkinter)
* `Pillow` (for image handling)

## 🖥️ Demo

<!-- Optional: Add a short GIF of the app in action -->

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/stable-bud.git
cd stable-bud
```

### 2. Create a Virtual Environment (optional but recommended)

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

**requirements.txt**

```txt
torch
diffusers
transformers
customtkinter
Pillow
```

## 🔐 Authentication (Hugging Face Token)

1. Go to https://huggingface.co/settings/tokens
2. Create an access token (read access is enough)
3. Create a file named `authtoken.py` in your project directory:

```python
# authtoken.py
auth_token = "your_huggingface_token_here"
```

🔒 **Never upload your token to public repositories.**

## 🧠 Usage

### Run the App

```bash
python app.py
```

### Using the App

1. Enter a **prompt** in the text box (e.g., *"A futuristic city with flying cars at sunset"*).
2. Click the **Generate** button.
3. The generated image appears below the prompt.
4. The image is saved as `generatedimage.png` in the same folder.

## 🧠 How It Works

1. Automatically checks if a **GPU is available** and loads the model accordingly.
2. Uses the `StableDiffusionPipeline` from Hugging Face's `diffusers` library.
3. Takes your text prompt → passes it to the model → outputs a generated image.
4. The image is displayed in the GUI and saved locally.

## 📌 Sample Prompts

* "A surreal galaxy of neon colors, ultra-detailed"
* "An ancient temple in the jungle, cinematic lighting"
* "A steampunk robot playing the violin in a dystopian city"

## 💡 Future Enhancements

* Add loading spinner or progress bar
* Add option to choose model version (v1.5, SDXL, etc.)
* Add history panel to view previous generations
* Let users save image with custom filename
* Async generation to avoid UI freeze

## ❓ Troubleshooting

| Problem | Solution |
|---------|----------|
| App window freezes during generation | Use threading or async to avoid blocking mainloop |
| Takes too long on CPU | Use a machine with GPU / try smaller models |
| Hugging Face token error | Ensure `auth_token` is correct and access is granted |

## 📜 License

MIT License — use freely for personal or commercial purposes. Attribution is appreciated.

## 👤 Author

**Your Name**  
[GitHub](https://github.com/Tharun007-TK) • [LinkedIn](https://linkedin.com/in/tharunkumarvmt-mldev) • [Website/Portfolio](https://tharunkumar.framer.website)
