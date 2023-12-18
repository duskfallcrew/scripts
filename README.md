# scripts
Code scripts from repositories - but with minor edits. Likely aren't really working, but if they are they are being used in our colab and notebook spaces.

Right now there's just the huggingface diffusers conversion for vae, and we can't even tell if it's doing what it needs to do, we're not great at programming.

We don't have security turned on this thing so if you're curious what we're trying to do basically it's this:

Convert 1.5 VAE (safetensors, PT, ckpt) etc to diffusers, but only the BIN format. 

Currently we're needing to also have our script pull off a json file with the KL encoder details - that's sort of either going to be handled ON this script or in colab later on. 

Problems we're facing:

- Vae keeps converting to bin but a 9kb file instead of 300mb file.

So the point is to try and modify the thing, to do the bin file, but we don't quite understand the logic requirements.

# New Files:

Textmaker: 

This is a new one we just got made via ChatGPT, which just adds text files next to well assumed to be your "IMAGES" - it's good for just single text lines, it's not an actual tagging script. 
This takes what 5 seconds on a 2019 mac and honestly is a breeze? 

Command line: python textmaker.py /path/to/your/folder "Your words here"

Example command line: python textmaker.py "/Users/CosetteXT/Desktop/Avon Diffusers Stuff/AIKittensRuS" "JeffyKitties"

Please note you're gonna replace your path with either your server details, or your hard drive details, and you'll clearly have your own tag.

We reworked that because wer'e not going to doxx our hard drive details to you!

HF Hub Upload Comfy UI Node:
allow you to upload easier to HF from comfyUI
instead of manually messing around - especially if you're on a server
Tested? No, i'm going to eventually.

