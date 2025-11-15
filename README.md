# 🖼️ Formato de Imagem Comprimida **.oxz** 
Sistema proprietário de compressão e reconstrução de imagens.

Este repositório contém:

✔ **Um arquivo `.oxz` gerado pelo compressor proprietário**  
✔ **O descompressor oficial (`descompressor_n95.py`)**  
✔ **Documentação de uso para reconstrução da imagem**

> ⚠ O compressor **não é público** — apenas o descompressor é disponibilizado.  
> O objetivo é demonstrar a tecnologia sem expor a lógica de geração.

---

## 📌 Sobre o formato **N9.5 (.oxz)**

O formato `.oxz` é um sistema customizado de compressão, projetado para:

- Reorganizar e randomizar blocos internos  
- Aplicar **seed antiforense**  
- Usar assinatura parcial SHA-256  
- Comprimir blocos com **bz2**  
- Manipular paletas adaptativas, RGBA e buffers binários  
- Utilizar estrutura de cabeçalho própria

O descompressor reconstrói a imagem original a partir dessa arquitetura.

---

## 📂 Conteúdo deste repositório

- `arquivo.oxz` — arquivo de imagem comprimida  
- `descompressor_n95.py` — script oficial de descompressão  
- Documentação de uso

---

## 🚀 Como usar

1. **Instale as dependências**
```bash
pip install pillow numpy

2. **Execute a descompressão**
```bash
python descompressor_n95.py arquivo.oxz imagem_final.png


