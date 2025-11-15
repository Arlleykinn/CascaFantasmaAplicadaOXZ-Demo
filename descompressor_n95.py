import bz2, hashlib, numpy as np
from PIL import Image
import sys, time

def descomprimir_n95(path_in, path_out):
    inicio = time.time()

    with open(path_in, 'rb') as f:
        blob = f.read()

    cab = blob[:8]
    seed = blob[8]
    digest_esperado = blob[9:13]
    ordem_raw = blob[13:61].replace(b'_', b'')
    ordem = [ordem_raw[i:i+1].decode() for i in range(len(ordem_raw))]

    w = int.from_bytes(cab[4:6], 'little')
    h = int.from_bytes(cab[6:8], 'little')

    blocos = {}
    cursor = 61
    for nome in ordem:
        if cursor + 4 > len(blob): break
        size = int.from_bytes(blob[cursor:cursor+4], 'little')
        cursor += 4
        blocos[nome] = bz2.decompress(blob[cursor:cursor+size])
        cursor += size

    for L in ['A', 'D']:
        for S in ['B', 'E']:
            for P in ['C', 'F']:
                if all(k in blocos for k in [L, S, P]):
                    try:
                        data = blocos[L] + blocos[S] + blocos[P]
                        if hashlib.sha256(data).digest()[:4] == digest_esperado:
                            pal = np.frombuffer(blocos[L], dtype=np.uint8).reshape((256, 3))
                            px = np.frombuffer(blocos[S], dtype=np.uint8).reshape((h, w))
                            alpha = np.frombuffer(blocos[P], dtype=np.uint8).reshape((h, w))

                            img = np.zeros((h, w, 4), dtype=np.uint8)
                            img[:, :, :3] = pal[px]
                            img[:, :, 3] = alpha

                            Image.fromarray(img, "RGBA").save(path_out)
                            duracao = round(time.time() - inicio, 3)
                            print(f"✅ Imagem restaurada → {path_out} ({duracao} segundos)")
                            return
                    except Exception as e:
                        continue

    raise Exception("❌ Nenhum colapso antiforense válido encontrado.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python descompressor_n95.py entrada.oxz saida.png")
    else:
        descomprimir_n95(sys.argv[1], sys.argv[2])
