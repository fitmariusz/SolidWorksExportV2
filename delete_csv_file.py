import os

import pymsgbox


def delete_csv_file(filePath: str):
    os.remove(filePath)
    pymsgbox.alert(f"Zakończono generowanie pojedyńczych bomów", "Sukces!", timeout=5000, icon=0 )
