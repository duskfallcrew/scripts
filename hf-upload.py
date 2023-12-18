class HuggingFaceUploadNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "model_path": ("STRING", {"default": "/content/models/voidnoiseVAE_basedonR0829", "multiline": False}),
                "path_in_repo": ("STRING", {"default": "voidnoiseVAE_basedonR0829", "multiline": False}),
                "commit_message": ("STRING", {"default": "Upload with \uD83D\uDE80\uD83E\uDD17 SD 1.5 Diffusers notebook", "multiline": False}),
            },
            "optional": {
                "is_diffusers_model": ("BOOLEAN", {"default": True}),
            }
        }

    RETURN_TYPES = ("STRING",)

    FUNCTION = "execute"

    def execute(self, model_path, path_in_repo, commit_message, is_diffusers_model=True):
        try:
            # Upload to Hugging Face Hub
            from huggingface_hub import HfApi
            from pathlib import Path
            import os

            api = HfApi()

            path_obj = Path(model_path)
            trained_model = path_obj.parts[-1]

            path_in_repo_local = path_in_repo if path_in_repo and not is_diffusers_model else ""

            notification = f"Uploading {trained_model} from {model_path} to https://huggingface.co/{model_repo}"
            print(notification)

            if os.path.isdir(model_path):
                if is_diffusers_model:
                    commit_message = f"Upload diffusers format: {trained_model}"
                    print("Detected diffusers model. Adjusting upload parameters.")
                else:
                    commit_message = f"Upload checkpoint: {trained_model}"
                    print("Detected regular model. Adjusting upload parameters.")

                api.upload_folder(
                    folder_path=model_path,
                    path_in_repo=path_in_repo_local,
                    repo_id=model_repo,
                    commit_message=commit_message,
                    ignore_patterns=".ipynb_checkpoints",
                )
            else:
                commit_message = f"Upload file: {trained_model}"
                api.upload_file(
                    path_or_fileobj=model_path,
                    path_in_repo=path_in_repo_local,
                    repo_id=model_repo,
                    commit_message=commit_message,
                )

            success_notification = f"♻ Upload Successful! Check the model at https://huggingface.co/{model_repo}/tree/main"
            return (success_notification,)
        except Exception as e:
            # Handle errors gracefully
            return (str(e),)
