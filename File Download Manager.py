import os
from pathlib import Path
import shutil

Downloads = Path(r"C:\Users\amalh\Downloads") #Directory Listing 
desktop = Path.home() / 'Desktop' #get desktop directory path
target_dirs = {
    '.txt': desktop / r"C:\Users\amalh\OneDrive - MSFT\Desktop\Downloaded Texts",
    '.png': desktop / r"C:\Users\amalh\OneDrive - MSFT\Desktop\Downloaded Images",
    '.jpg': desktop / r"C:\Users\amalh\OneDrive - MSFT\Desktop\Downloaded Images",
    '.jpeg': desktop / r"C:\Users\amalh\OneDrive - MSFT\Desktop\Downloaded Images",
    '.mp3': desktop / r"C:\Users\amalh\OneDrive - MSFT\Desktop\Downloaded Music",
    '.mp4': desktop / r"C:\Users\amalh\OneDrive - MSFT\Desktop\Downloaded Videos",
    '.avi': desktop / r"C:\Users\amalh\OneDrive - MSFT\Desktop\Downloaded Videos"
}

for file in Downloads.iterdir():
    if file.is_file():
        extension = file.suffix
        if extension in target_dirs:
            target_dir = target_dirs[extension]
            target_dir.mkdir(parents=True, exist_ok=True)
            shutil.move(str(file), str(target_dir / file.name))
