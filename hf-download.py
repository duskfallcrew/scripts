class HuggingFaceDownloadNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "huggingface_token": ("STRING", {"default": "", "multiline": False}),
                "model_url": ("STRING", {"default": "https://civitai.com/api/download/models/95864?type=Model&format=SafeTensor&size=pruned&fp=fp16", "multiline": False}),
                "destination_directory": ("STRING", {"default": "/content/models", "multiline": False}),
            }
        }

    RETURN_TYPES = ("STRING",)

    FUNCTION = "execute"

    def execute(self, huggingface_token, model_url, destination_directory):
        try:
            # Download from Hugging Face Hub
            import os
            import re
            import json
            import gdown
            import requests
            import subprocess
            from urllib.parse import urlparse, unquote
            from pathlib import Path

            os.chdir(destination_directory)

            def get_supported_extensions():
                return tuple([".ckpt", ".safetensors", ".pt", ".pth"])

            def get_filename(url):
                extensions = get_supported_extensions()

                if url.endswith(tuple(extensions)):
                    filename = os.path.basename(url)
                else:
                    response = requests.get(url, stream=True)
                    response.raise_for_status()

                    if 'content-disposition' in response.headers:
                        content_disposition = response.headers['content-disposition']
                        filename = re.findall('filename="?([^"]+)"?', content_disposition)[0]
                    else:
                        url_path = urlparse(url).path
                        filename = unquote(os.path.basename(url_path))

                if filename.endswith(tuple(get_supported_extensions())):
                    return filename
                else:
                    return None

            def parse_args(config):
                args = []

                for k, v in config.items():
                    if k.startswith("_"):
                        args.append(f"{v}")
                    elif isinstance(v, str) and v is not None:
                        args.append(f'--{k}={v}')
                    elif isinstance(v, bool) and v:
                        args.append(f"--{k}")
                    elif isinstance(v, float) and not isinstance(v, bool):
                        args.append(f"--{k}={v}")
                    elif isinstance(v, int) and not isinstance(v, bool):
                        args.append(f"--{k}={v}")

                return args

            def aria2_download(dir, filename, url):
                user_header = f"Authorization: Bearer {huggingface_token}"

                aria2_config = {
                    "console-log-level"         : "error",
                    "summary-interval"          : 10,
                    "header"                    : user_header if "huggingface.co" in url else None,
                    "continue"                  : True,
                    "max-connection-per-server" : 16,
                    "min-split-size"            : "1M",
                    "split"                     : 16,
                    "dir"                       : dir,
                    "out"                       : filename,
                    "_url"                      : url,
                }
                aria2_args = parse_args(aria2_config)
                subprocess.run(["aria2c", *aria2_args])

            def gdown_download(url, dst, filepath):
                if "/uc?id/" in url or "/file/d/" in url:
                    return gdown.download(url, filepath, quiet=False)
                elif "/drive/folders/" in url:
                    os.chdir(dst)
                    return gdown.download_folder(url, quiet=True, use_cookies=False)

            def download(url, dst):
                filename = get_filename(url)
                filepath = os.path.join(dst, filename)

                if "drive.google.com" in url:
                    gdown = gdown_download(url, dst, filepath)
                elif url.startswith("/content/drive/MyDrive/"):
                    return url
                else:
                    if "huggingface.co" in url:
                        if "/blob/" in url:
                            url = url.replace("/blob/", "/resolve/")
                    aria2_download(dst, filename, url)

            model_path = model_url
            download(model_path, destination_directory)
            success_notification = f"Model downloaded at: {model_path}\n♻ Download Successful! Check the model at {destination_directory}"
            return (success_notification,)
        except Exception as e:
            # Handle errors gracefully
            return (str(e),)
