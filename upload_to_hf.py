import os
import sys
import subprocess
import getpass

def install_and_import(package):
    try:
        __import__(package)
    except ImportError:
        print(f"[INFO] Installing required dependency: {package}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Ensure huggingface_hub is installed
install_and_import("huggingface_hub")

from huggingface_hub import HfApi, login, whoami

def main():
    print("====================================================")
    print("Emotion Pro Analytics - Hugging Face Model Uploader")
    print("====================================================")
    
    # 1. Retrieve the write token
    token = os.environ.get("HF_TOKEN")
    if not token:
        print("\nPlease enter your Hugging Face Write Access Token.")
        print("(Go to https://huggingface.co/settings/tokens to generate one if needed)")
        token = getpass.getpass("Token (hidden input): ").strip()
    
    if not token:
        print("[ERROR] A valid token is required to upload the model.")
        sys.exit(1)
        
    # 2. Authenticate
    try:
        print("\n[INFO] Authenticating with Hugging Face...")
        login(token=token, write_permission=True)
        user_info = whoami(token=token)
        username = user_info['name']
        print(f"[SUCCESS] Successfully logged in as: {username}")
    except Exception as e:
        print(f"[ERROR] Authentication failed: {e}")
        sys.exit(1)
        
    # 3. Check for the local model folder
    local_folder = "./final_emotion_model_v2"
    if not os.path.exists(local_folder):
        print(f"[ERROR] Local model directory '{local_folder}' not found.")
        print("Please ensure you run this script from the project root and that the model is trained.")
        sys.exit(1)
        
    # 4. Determine repository name
    default_repo_name = "emotion-analytics-distilbert"
    repo_name = os.environ.get("HF_REPO_NAME")
    if not repo_name:
        if sys.stdin.isatty():
            repo_name = input(f"\nEnter a repository name [default: {default_repo_name}]: ").strip()
        else:
            repo_name = default_repo_name
    if not repo_name:
        repo_name = default_repo_name
        
    repo_id = f"{username}/{repo_name}"
    
    # 5. Create the repository
    api = HfApi()
    try:
        print(f"\n[INFO] Creating model repository on Hugging Face: {repo_id}...")
        api.create_repo(repo_id=repo_id, repo_type="model", exist_ok=True)
        print("[INFO] Repository is ready.")
    except Exception as e:
        print(f"[ERROR] Failed to create repository: {e}")
        sys.exit(1)
        
    # 6. Upload the folder
    try:
        print(f"\n[INFO] Uploading fine-tuned weights and configurations from '{local_folder}'...")
        print("This might take a minute or two depending on your upload speed. Please stand by...")
        
        api.upload_folder(
            folder_path=local_folder,
            repo_id=repo_id,
            repo_type="model"
        )
        
        print("\n[SUCCESS] Your fine-tuned model has been deployed to Hugging Face!")
        print(f"Model URL: https://huggingface.co/{repo_id}")
        print("\n----------------------------------------------------")
        print("NEXT STEP:")
        print("Update your 'engine.py' model name to use this repository:")
        print(f'   self.model_name = "{repo_id}"')
        print("----------------------------------------------------")
        
    except Exception as e:
        print(f"[ERROR] Failed to upload model folder: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
