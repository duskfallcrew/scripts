# Scripts
This repository contains a collection of code scripts primarily designed for use in our Colab and notebook spaces. These scripts have been sourced from various repositories and modified to suit our specific needs. While we strive for functionality, please note that these scripts may not be fully operational or optimized, as we are not expert programmers. Contributions and improvements from the community are highly encouraged!

Current Focus: Hugging Face Diffusers VAE Conversion
One of our primary focuses is converting Variational Autoencoder (VAE) models, particularly those in .safetensors, .pt, and .ckpt formats used with Stable Diffusion 1.5, into the diffusers library format, specifically targeting the .bin output.

## Challenges
We are currently facing issues with the VAE conversion process:

The script is producing .bin files that are only 9KB instead of the expected size (around 300MB), indicating that the conversion is not working as intended.

We're working to modify the script to correctly handle the .bin format, but we need a better understanding of the underlying logic.

Our current approach involves pulling a JSON file with KL encoder details, which we're considering handling either directly in this script or in a Colab notebook.

Any assistance or guidance on resolving these issues would be greatly appreciated!

### New File: textmaker.py
We've recently added textmaker.py, a script developed with the help of ChatGPT, designed to simplify the creation of text files alongside image datasets.

### Functionality
Purpose: textmaker.py creates a corresponding .txt file for each image file in a specified directory. It's useful for adding single-line text descriptions or tags to images, though it's not a full-fledged image tagging script.

Performance: Efficient and fast, taking approximately 5 seconds to process on a 2019 Mac.

## Usage
Command Line:
```
python textmaker.py /path/to/your/folder "Your words here"
Use code with caution.
```
#### Example:
```
python textmaker.py "/Users/YourUserName/Path/To/Your/Images" "Your desired text here"
```
Note: Replace /path/to/your/folder and "Your words here" with your actual file path and desired text. The example path has been modified for privacy.

## In Progress Scripts 
ComfyUI Nodes for Hugging Face Hub
HF Hub Upload ComfyUI Node
Functionality: This node is intended to facilitate uploading files from ComfyUI to the Hugging Face Hub, streamlining the process compared to manual uploads.

Testing Status: Not yet tested.

HF Download ComfyUI Node
Functionality: Designed to download from CivitAI, Hugging Face, and possibly other sources. It's built as a ComfyUI node.

Dependencies: May require Aria2. Further details on dependencies are not fully clear at this time.

Contributions
We welcome contributions, suggestions, and improvements to these scripts. If you have expertise in any of these areas, especially regarding the VAE conversion or ComfyUI nodes, your input would be invaluable.



