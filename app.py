import tkinter as tk
import customtkinter as ctk
from PIL import ImageTk, Image
from authtoken import auth_token

import torch
from diffusers import StableDiffusionPipeline

# Create the app
app = tk.Tk()
app.geometry("532x632")
app.title("Stable Bud")
ctk.set_appearance_mode("dark")

prompt = ctk.CTkEntry(app, height=40, width=512, font=("Arial", 20), text_color="black", fg_color="white")
prompt.place(x=10, y=10)

lmain = ctk.CTkLabel(app, height=512, width=512)
lmain.place(x=10, y=110)

model_id = "CompVis/stable-diffusion-v1-4"
device = "cuda" if torch.cuda.is_available() else "cpu"

# Load the pipeline based on device
if device == "cuda":
    pipe = StableDiffusionPipeline.from_pretrained(
        model_id,
        revision="fp16",
        torch_dtype=torch.float16,
        use_auth_token=auth_token
    )
else:
    pipe = StableDiffusionPipeline.from_pretrained(
        model_id,
        use_auth_token=auth_token
    )

pipe.to(device)

def generate():
    prompt_text = prompt.get()
    image = pipe(prompt_text, guidance_scale=8.5).images[0]
    image.save('generatedimage.png')
    img = ImageTk.PhotoImage(image.resize((512, 512)))
    lmain.configure(image=img)
    lmain.image = img  # keep a reference to avoid garbage collection

trigger = ctk.CTkButton(app, height=40, width=120, font=("Arial", 20), text_color="white", fg_color="blue",
                        command=generate)
trigger.configure(text="Generate")
trigger.place(x=206, y=60)

app.mainloop()

