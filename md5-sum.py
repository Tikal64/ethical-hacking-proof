import os
import hashlib
import pandas as pd

def calculate_md5(file_path):
    """Calcola l'MD5 di un file specifico."""
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def generate_md5_table(folder_path):
    """Calcola l'MD5 di tutti i file nella cartella e restituisce una tabella."""
    table_data = []
    for root, _, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            md5_hash = calculate_md5(file_path)
            table_data.append({"File Name": file_name, "MD5": md5_hash})

    return pd.DataFrame(table_data)

if __name__ == "__main__":
    folder_path = "path/della/tua/cartella"  # Sostituisci con il percorso della tua cartella
    md5_table = generate_md5_table(folder_path)
    print(md5_table)


#pip install pandas
