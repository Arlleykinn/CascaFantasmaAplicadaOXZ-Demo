# 🧬 Casca Fantasma — Execução Observável, Lógica Não-Observável  
## Formato Experimental de Imagem **.oxz** (Demonstração Pública N9.5)

Este repositório apresenta a **primeira demonstração pública da tecnologia Casca Fantasma**, aplicada ao formato de imagem comprimida **.oxz**.

Aqui você encontrará:

✔ **Um arquivo `.oxz` gerado por um compressor protegido pela Casca Fantasma**  
✔ **O descompressor oficial N9.5 (`descompressor_n95.py`)**  
✔ **Documentação mínima para reconstrução da imagem sem revelar a lógica interna**

> ⚠ **Importante:**  
> O compressor **não é público**. Ele pertence ao ecossistema da Casca Fantasma e sua lógica não pode ser deduzida, reconstruída ou replicada a partir do descompressor.

O `.oxz` atua é o *ambiente ideal* para se observar a Casca em ação, devido ao fato de ser um codigo privado.

---

# 🧠 O que é a Casca Fantasma?

A **Casca Fantasma** é uma camada antiforense de execução que transforma algoritmos comuns em **fenômenos não reconstruíveis**.

Ela não tenta esconder código.  
Ela destrói significado.

Ela não bloqueia depuração.  
Ela sabota o que o depurador tenta revelar.

Com a Casca, a computação segue um novo paradigma:

✔ A execução ocorre  
✔ O resultado é verificável  
✔ A lógica interna permanece invisível  
✔ O binário não revela intenção  
✔ A engenharia reversa encontra apenas um labirinto simbólico

A Casca Fantasma rompe o axioma clássico:

> “Se executa, pode ser entendido.”  
**Aqui, não pode.**

---

# 📦 O formato **.oxz** como prova operacional

O arquivo `.oxz` deste repositório foi comprimido através de mecanismos internos protegidos pela Casca, incluindo:

- 🔁 **Fragmentação simbólica dinâmica**  
- 🧬 **Seeds antiforenses por execução**  
- 🛡️ **Assinatura parcial SHA-256**  
- 📦 **Compressão de blocos com bz2**  
- 🎨 **Paletas adaptativas e buffers RGBA**  
- 🧩 **Cabeçalho proprietário com estrutura variável**

O descompressor reconstrói a imagem original, mas:

❌ não permite inferir o compressor  
❌ não revela a arquitetura simbólica  
❌ não expõe o processo interno de geração

Ele é apenas **uma vista controlada da superfície do sistema**.

---

# 📂 Conteúdo deste repositório

- **`arquivo.oxz`** — arquivo comprimido protegido pela Casca  
- **`descompressor_n95.py`** — descompressor oficial N9.5  
- **`README.md`** — documentação da demonstração

---

# 🚀 Como usar o Descompressor N9.5

### 1. Instale as dependências
```bash
pip install pillow numpy

2. **Execute a descompressão**
```bash
python descompressor_n95.py arquivo_saida.oxz imagem_final.png


