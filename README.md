# Computacao-Grafica-Opencv - Projeto Final

Desenvolvedor: Ketherly

O programa realiza a detecção de cadeiras de rodas que pode ser vir por exemplo pra avisar uma empresa ou até mesmo o porteiro de um predio que um cadeirante esta chegando, permitindo que possa ser remanejado, com mais rapidez, alguém para ajuda-lo.

Para este projeto foram utilizadas:

🎇Libs nativas do OpenCV como numpy e datetime

🎇Models haarcascade_frontalface

#Etapas

O sistema realizar o processamendo de imagem realizando as seguintes etapas:

➢Treinamento de Imagens: realiza o treinamento das imagens para reconhedimendo do Haar Cascade
![treinamento de imagens](https://user-images.githubusercontent.com/66181220/101227238-ecfcdc00-3675-11eb-9ddc-db47a24c5708.jpg)

➢ Redimencionamento – Aumenta o tamanho da imagem, porém perde a qualidade
![redimencionamento](https://user-images.githubusercontent.com/66181220/101227309-2a616980-3676-11eb-9261-ac3bf88b1bae.jpg)

➢ HSV – modifica a Saturação, matiz e valor da imagem
![hsv](https://user-images.githubusercontent.com/66181220/101227316-2cc3c380-3676-11eb-99ba-984135ca2623.jpg)

➢ Escala em cinza – deixa a imagem inteira em tons de cinza
![cinza](https://user-images.githubusercontent.com/66181220/101227422-81ffd500-3676-11eb-9ffb-6ec19004fb12.jpg)

➢ Binarização – transforma em preto e branco
![binario](https://user-images.githubusercontent.com/66181220/101227070-63e5a500-3675-11eb-940c-ca47d815aabf.jpg)

➢ Recorte – recorta ponto de interesse da imagem
![recorte](https://user-images.githubusercontent.com/66181220/101227446-a8257500-3676-11eb-9e92-5f52288a27cd.jpg)

➢ Log com data e hora – cria imagem com log indicando data
![log](https://user-images.githubusercontent.com/66181220/101227486-cee3ab80-3676-11eb-9926-c6432ee331c3.jpg)

➢ Reconhecimento facial – reconhece a face frontal de uma pessoa
![reconhecimento](https://user-images.githubusercontent.com/66181220/101227517-e58a0280-3676-11eb-8291-4915f3541f0f.jpg)

➢ Reconhecimento de Borda – coloca borda quando o ponto de interesse é detectado
![bordas](https://user-images.githubusercontent.com/66181220/101227561-08b4b200-3677-11eb-9124-da3677edcbca.jpg)

➢ Correção morfológica – ajusta imagem para tirar ruídos
![mofologica1](https://user-images.githubusercontent.com/66181220/101227317-2cc3c380-3676-11eb-9127-1fc784de5c3f.jpg)

➢ Skill selecionando objeto pela cor – fecha o programa pela cor verde detectada
![cor](https://user-images.githubusercontent.com/66181220/101227609-38fc5080-3677-11eb-8425-ee67b53c337b.jpg)
