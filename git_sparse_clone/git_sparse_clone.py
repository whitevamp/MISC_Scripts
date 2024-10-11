import os
import subprocess
import sys

def git_sparse_clone(rurl, localdir, *args):
    try:
        # Create the local directory if it doesn't exist
        os.makedirs(localdir, exist_ok=True)
        print(f"Created directory: {localdir}")
        
        # Change to the local directory
        os.chdir(localdir)
        print(f"Changed directory to: {localdir}")

        # Initialize a new git repository
        result = subprocess.run(["git", "init"], check=True, capture_output=True, text=True)
        print(result.stdout)

        # Add the remote repository URL
        result = subprocess.run(["git", "remote", "add", "-f", "origin", rurl], check=True, capture_output=True, text=True)
        print("Updating origin\n", result.stdout)

        # Enable sparse checkout
        result = subprocess.run(["git", "config", "core.sparseCheckout", "true"], check=True, capture_output=True, text=True)
        print("Sparse checkout enabled.")
        
        # Write each argument (directory or file) to the sparse-checkout file
        sparse_checkout_path = os.path.join(".git", "info", "sparse-checkout")
        with open(sparse_checkout_path, "a") as sparse_file:
            for item in args:
                sparse_file.write(f"{item}\n")
                print(f"Added {item} to sparse checkout.")

        # Detect the default branch (usually master or main)
        result = subprocess.run(["git", "remote", "show", "origin"], check=True, capture_output=True, text=True)
        for line in result.stdout.splitlines():
            if "HEAD branch:" in line:
                default_branch = line.split(":")[1].strip()
                print(f"Default branch detected: {default_branch}")
                break
        else:
            raise Exception("Could not detect the default branch.")

        # Pull from the detected default branch
        result = subprocess.run(["git", "pull", "origin", default_branch], check=True, capture_output=True, text=True)
        print(result.stdout)

    except subprocess.CalledProcessError as e:
        print(f"Error during Git operation: {e.stderr}")
    except OSError as e:
        print(f"OS error: {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

# Example usage:
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python git_sparse_clone.py <repo_url> <localdir> [<dir1> <dir2> ...]")
    else:
        git_sparse_clone(sys.argv[1], sys.argv[2], *sys.argv[3:])
