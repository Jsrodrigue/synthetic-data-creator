import os
import glob

def cleanup_temp_files(temp_dir):
    """Function to delete temporary images"""
    for file_path in glob.glob(os.path.join(temp_dir, "*_hist.png")) + \
                     glob.glob(os.path.join(temp_dir, "*_box.png")):
        os.remove(file_path)
