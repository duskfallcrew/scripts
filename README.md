# scripts
Code scripts from repositories - but with minor edits. Likely aren't really working, but if they are they are being used in our colab and notebook spaces.

Right now there's just the huggingface diffusers conversion for vae, and we can't even tell if it's doing what it needs to do, we're not great at programming.

We don't have security turned on this thing so if you're curious what we're trying to do basically it's this:

Convert 1.5 VAE (safetensors, PT, ckpt) etc to diffusers, but only the BIN format. 

Currently we're needing to also have our script pull off a json file with the KL encoder details - that's sort of either going to be handled ON this script or in colab later on. 

Problems we're facing:

- Vae keeps converting to bin but a 9kb file instead of 300mb file.

So the point is to try and modify the thing, to do the bin file, but we don't quite understand the logic requirements.
