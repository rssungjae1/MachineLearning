import jsonReader
import WebScrappingCat
import catFaceRecognition

from PIL import Image
import os

# Scrapping keys
keys = jsonReader.jsonReader()

for key in keys:
    # Check the image save directory
    try:
        if not os.path.exists("./img/" + key):
            os.makedirs("./img/" + key)
    except OSError as err:
        print ("[" + key + "]" + err)

    # WebScrapping with keys
    WebScrappingCat.scrapping(key, 5)

# Check file cat face recognition
for key in keys:
    folder_path = "./img/" + key + "/"
    file_list = os.listdir(folder_path)
    for fl in file_list:
        file_path = folder_path + fl
        image = Image.open(file_path)
        format = image.format
        image.close()
        if image.format == "GIF":
            print("[type error]GIF파일 형식은 맞지않습니다. 해당 파일을 삭제하겠습니다." + file_path)
            os.remove(file_path)
            continue
        print("고양이 얼굴 인식 체크" + file_path)
        if catFaceRecognition.detectCatFace(file_path):
            # 고양이 얼굴 인식 가능 사진
            print("얼굴 인식 확인했습니다.")
            pass
        else:
            # 고양이 얼굴 인식 불가능 사진
            print("얼굴인식 불가, 이미지를 삭제합니다.")
            os.remove(file_path)