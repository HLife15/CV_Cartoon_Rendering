OpenCV를 이용해 사진을 카툰풍으로 바꿔주는 프로그램입니다.
작동 과정은 다음과 같습니다.<br><br>

1. 이미지를 불러옵니다.
2. 불러온 이미지를 흑백으로 바꿔줍니다. (cvtColor를 이용했습니다)
3. 흑백 이미지에 Bilateral Filter 효과를 줍니다. (다른 Smoothing Filter들과 달리 Bilateral Filter는 외곽선의 손상을 최소화하며 Smoothing이 가능합니다)
4. 그 이미지에 Canny Edge Detector를 적용합니다. (Bilateral Filter로 보정된 이미지기 때문에 원본 이미지보다 더 깔끔해 보다 정확하게 외곽선을 판단해 그립니다)
5. 이미지를 반전시킵니다. (bitwise_not을 이용했으며 이로서 흰 배경에 검은 선으로 묘사가 됩니다)
6. 흑백 이미지를 다시 컬러로 변환해줍니다. (cvtColor를 이용했습니다)
7. 원본 이미지에 효과를 준 이미지를 혼합해줍니다. (bitwise_and를 이용했습니다)
8. 완성된 이미지를 창에 띄워줍니다.<br><br>

이런 과정을 통해 완성된 만화 같은 느낌이 잘 표현되는 사진은 다음과 같습니다.<br>
![good2](https://github.com/HLife15/CV_Cartoon_Rendering/assets/162321808/5f580f07-8ae3-4b36-b2f2-ce4283032904)
<br><br>

반대로 잘 표현되지 않은 사진은 다음과 같습니다.<br>
![bad3](https://github.com/HLife15/CV_Cartoon_Rendering/assets/162321808/6e6abe05-310a-4781-8eed-5bd1a11eadda)
<br><br>


이를 통해 이 프로그램의 한계를 알 수 있었습니다.<br>
첫번째로 화질이 좋지 않은 사진은 외곽선 인식이 어려워 만화 같은 느낌이 잘 드러나지 않는다는 점입니다.<br>
![20180117519186](https://github.com/HLife15/CV_Cartoon_Rendering/assets/162321808/3db2f8b8-5dbc-45e3-8995-ff54177a6dfc)<br>
잘 표현되지 않은 사진의 원본입니다. 화질이 좋지 않았기 때문에 제대로 효과가 적용되지 않았음을 알 수 있었습니다.<br><br>



두번째 문제는 투명한 물체를 들고 있는 사람의 사진에 작업할 때 나타났습니다.<br>
![bad1](https://github.com/HLife15/CV_Cartoon_Rendering/assets/162321808/6b5afce7-1a9f-487b-a49f-9fd13c2f95ec)<br>
전체적으로 만화 같은 느낌이 잘 나타났지만 위 사진에서 표시된 대로 투명한 잔의 외곽선이 제대로 표시가 되지 않으면서 뒷배경과 약간 섞이게 되었습니다.<br>
![image2](https://github.com/HLife15/CV_Cartoon_Rendering/assets/162321808/c9b54989-5c5e-40ce-9847-aaa82bab7a77)<br>
원본 사진은 투명한 잔과 뒷배경이 어느 정도 구분이 갔다는 점을 생각해보면 이 프로그램의 한계라고 볼 수 있겠습니다.<br><br>



마지막으로 작은 글씨 같은 경우 뭉개지는 경우가 많았다는 점이었습니다.<br>
![bad2](https://github.com/HLife15/CV_Cartoon_Rendering/assets/162321808/cee0542c-c9d4-4461-9df1-ff57ad082aa3)<br>
위 사진에 표시된 대로 사진 상에서 멀리 있는 글씨들은 형태가 뭉개져 제대로 알아볼 수 없었습니다.<br>
![image7](https://github.com/HLife15/CV_Cartoon_Rendering/assets/162321808/9018890a-a905-4ee2-b6ac-a7cae5333b7f)<br>
원본 사진의 경우 글씨가 작긴 해도 어느 정도 알아볼 수 있다는 점을 생각해보면 이 역시 한계라고 생각이 됩니다.<br>
이렇게 프로그램의 기능과 옳은 예와 잘못된 예, 한계점까지 작성해보았습니다.
