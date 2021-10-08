# PersonDetector-MaixPy
### # Passo a passo:

+ **Preparando o ambiente**:

***→ Primeira coisa é instalar o ambiente Anaconda:*** 

[Miniconda - Conda documentation](https://docs.conda.io/en/latest/miniconda.html)

***→ Segunda coisa é preparar as demais dependências:***

```bash
conda create -n yolo python=3.7

conda activate yolo
```

→ ***Baixando os arquivos do Git***:

```bash
git clone https://github.com/AIWintermuteAI/aXeleRate.git

cd aXeleRate/

# Instalando requisitos
pip install -r requiments.txt              
pip install -e .
```

→ ***Baixando o Dataset (nesse caso de pessoas)***:

```bash
https://drive.google.com/u/0/uc?export=download&confirm=mF7v&id=1UWwxlJm5JH_JiBY9PoLgGyHsRDzBqRGU
```

→ ***Editando arquivos para treinamento***:

```bash
cd configs/

# Editar o json de acordo com o quer treinar, para o nosso caso:
# Mudar o caminho para o dataset
# Train_times = 1
```
![img1](https://user-images.githubusercontent.com/46756608/136563642-84bae9ec-630a-4a6a-b2e6-e00051e43438.png)

![img2](https://user-images.githubusercontent.com/46756608/136563653-a1ac72b4-1b0e-4569-95b2-25f55eb0546c.png)

![img4](https://user-images.githubusercontent.com/46756608/136563663-36ba88db-df9f-49bd-a2f8-3f1f013824c0.png)

---

→ ***Treinando a rede***:

```bash
# É possível que nessa etapa de um erro, então a fim de evitar, segue o comando abaixo:
sudo chmod 777 home/

# Treinamento:
python3 axelerate/train.py -c configs/person_detector.json

# E aguarde, porque isso vai demorar um pouco 
```

→ ***Convertendo as redes***:

```bash
# Conversor da Maix Toolbox
git clone https://github.com/sipeed/Maix_Toolbox.git

bash get_nncase.sh

# Cola umas imagens de teste na pasta images

# Copia o modelo .tflite que foi gerado do treinamento e cola nessa pasta
sh tftlite2kmodel.sh model.tflite
```

→ ***Inserindo os arquivos no MaixPy***:

```bash
# Baixe essa ferramenta para transferir os arquivos  :
https://api.dl.sipeed.com/shareURL/MAIX/tools/kflash_gui

# Após descompactar acesse ela via:
cd kflash_gui/

# Execute...
./kflash_gui
```

- **Imagem da ferramenta:**
    
    → Primeiro arquivo kmodel, no endereço x600000
    
    → Depois o arquivo .bin disponibilizado nos arquivos abaixo.
    
   ![img5](https://user-images.githubusercontent.com/46756608/136563693-c360e96f-a8ad-437b-b2d7-eb64d0628748.png)


---

→ ***Executando o scipt*:**

```bash
# A IDE da MaixPy pode ser encontrada nesse link aqui: 
https://api.dl.sipeed.com/shareURL/MAIX/MaixPy/ide/

```

→ Após instalada, basta executar. 

→ Em *tools*, selecione a placa que estará usando. 

→ Depois, em *file*, abra o script desejado. Para nosso caso está no seguinte diretório: 

**→ examples_scripts/k210/detector/person_detector_v4.py**

→ Depois de abrir o arquivo, clica no canto inferior esquerdo nas correntes para conectar a placa, e selecione USB0 ou 1. 

→ Por fim, basta executar o *script*, clicando no *play*.
