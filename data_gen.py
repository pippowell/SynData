import subprocess
import glob

# List of job script files
job_files = glob.glob("job_scripts/*.yaml")


for job_file in job_files:
    # Construct the command
    cmd = ["syclops", "-j", job_file]

    print(f'generating images from template in {job_file}')

    try:
        # Run the command
        subprocess.run(cmd,check=True)

    except:
        print(f'failed to generate images from template in {job_file}')
        continue
