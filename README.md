OpenCV를 이용해 사진을 카툰풍으로 바꿔주는 프로그램입니다.
작동 과정은 다음과 같습니다.

1. 이미지를 불러옵니다.
2. 불러온 이미지를 흑백으로 바꿔줍니다. (cvtColor를 이용했습니다)
3. 흑백 이미지에 Bilateral Filter 효과를 줍니다. (다른 Smoothing Filter들과 달리 Bilateral Filter는 외곽선의 손상을 최소화하며 Smoothing이 가능합니다)
4. 그 이미지에 Canny Edge Detector를 적용합니다. (Bilateral Filter로 보정된 이미지기 때문에 보다 더 정확하게 외곽선을 판단해 그립니다)
5. 이미지를 반전시킵니다. (bitwise_not을 이용했으며 이로서 흰 배경에 검은 선으로 묘사가 됩니다)
6. 흑백 이미지를 다시 컬러로 변환해줍니다. (cvtColor를 이용했습니다)
7. 원본 이미지에 효과를 준 이미지를 혼합해줍니다. (bitwise_and를 이용했습니다)
8. 완성된 이미지를 창에 띄워줍니다.

이런 과정을 통해 만화 같은 느낌이 잘 표현되는 사진은 다음과 같습니다.
(https://github.com/HLife15/CV_Cartoon_Rendering/assets/162321808/b9868319-4fc6-4b96-a8a3-dc5a2b2c1fd8)

반대로 잘 표현되지 않은 사진은 다음과 같습니다.
(https://github.com/HLife15/CV_Cartoon_Rendering/assets/162321808/fda47ea7-90f9-4abe-84d3-dde2aae93a34)
