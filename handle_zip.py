import os
import shutil
import subprocess
import tempfile
import zipfile
import sys

def zip_files_in_directory(directory, output_zip):
    with zipfile.ZipFile(output_zip, 'w') as zipf:
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, directory)
                zipf.write(file_path, arcname)

def copy_directory(src, dst):
    if os.path.exists(dst):
        shutil.rmtree(dst)
    shutil.copytree(src, dst)

if __name__ == "__main__":
    
    # app location
    directory = "./app/"
    
    with tempfile.TemporaryDirectory() as tmpdirname:
        copy_directory(directory, tmpdirname)
        
        # install requirements if they exist
        requirements_path = os.path.join(tmpdirname, 'requirements.txt')
        if os.path.exists(requirements_path):
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', requirements_path, '-t', tmpdirname])
        
        zip_files_in_directory(tmpdirname, 'terraform/lambda_function.zip')
    
    # spin up docker-compose with localstack and deploy lambda function
    subprocess.check_call(['docker-compose', 'up', '-d'])