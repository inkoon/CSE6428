### Requirements
- Python 3.8.5
- grammar.tx and dictionary_TRIE.txt should be in the same directory as main.py

### Run
```python
python3 main.py --input manual_tagging.txt
```

### Results
all_pos_tagged_manual_tagging.txt : All possible answers.
pos_tagged_manual_tagging.txt : Select one of all possible answers.

#### Examples
- manual_tagging.txt
```txt
### 세종 품사 태그의 소분류를 기준으로 작성

# 어머니는 할머니 댁에 김장을 하러 가셨습니다.
어머니/NN+는/JX
할머니/NN
댁/NN+에/JK
김장/NN+을/JK
하/VV+러/E
가/VV+셨/E+습니다/E+./SF

# 아기의 냄새가 나는 이불을 덮고 잠이 듭니다.
아기/NN+의/JK
냄새/NN+가/JK
나/VV+는/E
이불/NN+을/JK
덮/NN+고/E
잠/NN+이/JK
듭/VV+니다/E+./SF

# 여름 감기는 열이 많이 나거나 배탈, 구토 등 소화기 증상을 동반하는 경우가 많다.
여름/NN
감기/NN+는/JX
열/NN+이/JK
많이/MA
나/VV+거나/E
배탈/NN+,/SP
구토/NN
등/NN
소화기/NN
증상/NN+을/JK
동반/NN+하/VV+는/E
경우/NN+가/JX
많/VA+다/E+./SF
 
# 리버풀의 위르겐 클롭 감독이 챔피언스리그 무대에서 성사된 레알마드리드와의 맞대결을 기대했다.
리버풀/NN+의/JK
위르겐/NN
클롭/NN
감독/NN+이/JK
챔피언스리그/NN
무대/NN+에서/JK
성사/NN+된/XS
레알마드리드/NN+와/JK+의/JK
맞대결/NN+을/JK
기대/NN+했/XS+다/E+./SF

# 수니파와 시아파가 오늘날 반목하는 이유를 설명하기 위해서는, 오랜 종교적 차이는 물론 1300년 동안 두 종족이 갈등한 역사의 모든 사회적, 경제적, 문화적 요인까지 알아야 한다.
수니파/NN+와/JC
시아파/NN+가/JK
오늘날/NN
반목/NN+하/XS+는/E
이유/NN+를/JK
설명/NN+하/XS+기/E
위해서/VV+는/JX+,/SP
오랜/MM
종교/NN+적/XS
차이/NN+는/JX
물론/MAG
1300/SN+년/NN
동안/NN
두/MM
종족/NN+이/JK
갈등/NN+한/XS
역사/NN+의/JK
모든/MM
사회/NN+적/XS+,/SP
경제/NN+적/XS+,/SP
문화/NN+적/XS
요인/NN+까지/JX
알/VV+아야/E
한/VX+다/E+./SF
```
- pos_tagged_manual_tagging.txt
```txt
# 어머니는 할머니 댁에 김장을 하러 가셨습니다.
어머니/NN+는/JX
할머니/NN
댁/NN+에/JK
김장/NN+을/JK
하/VV+러/E
가/VV+셨/E+습니다/E+./SF

# 아기의 냄새가 나는 이불을 덮고 잠이 듭니다.
아기/NN+의/JK
냄새/NN+가/VV
나/VV+는/JX
이불/NN+을/JK
덮/NN+고/E
잠/NN+이/JK
듭/VV+니다/E+./SF

# 여름 감기는 열이 많이 나거나 배탈, 구토 등 소화기 증상을 동반하는 경우가 많다.
여름/NN
감기/NN+는/JX
열/NN+이/JK
많이/MA
나/VV+거나/E
배탈/NN+,/SP
구토/NN
등/NN
소화기/NN
증상/NN+을/JK
동반/NN+하/VV+는/JX
경우/NN+가/VV
많/VA+다/E+./SF

# 리버풀의 위르겐 클롭 감독이 챔피언스리그 무대에서 성사된 레알마드리드와의 맞대결을 기대했다.
리버풀/NN+의/JK
위르겐/NN
클롭/NN
감독/NN+이/JK
챔피언스리그/NN
무대/NN+에서/JK
성사/NN+된/XS
레알마드리드/NN+와/JK+의/JK
맞대결/NN+을/JK
기대/NN+했/XS+다/E+./SF

# 수니파와 시아파가 오늘날 반목하는 이유를 설명하기 위해서는, 오랜 종교적 차이는 물론 1300년 동안 두 종족이 갈등한 역사의 모든 사회적, 경제적, 문화적 요인까지 알아야 한다.
수니파/NN+와/JK
시아파/NN+가/VV
오늘날/NN
반목/NN+하/VV+는/JX
이유/NN+를/JK
설명/NN+하/VV+기/E
위해서/VV+는/JX+,/SP
오랜/MM
종교/NN+적/XS
차이/NN+는/JX
물론/MAG
1300/SN+년/NN
동안/NN
두/MM
종족/NN+이/JK
갈등/NN+한/XS
역사/NN+의/JK
모든/MM
사회/NN+적/XS+,/SP
경제/NN+적/XS+,/SP
문화/NN+적/XS
요인/NN+까지/JX
알/VV+아야/E
한/XS+다/E+./SF
```

- all_pos_tagged_manual_tagging.txt
```txt
# 어머니는 할머니 댁에 김장을 하러 가셨습니다.
{'어머니/NN+는/E', '어머니/NN+는/JX'}
{'할머니/NN'}
{'댁/NN+에/JK'}
{'김장/NN+을/JK'}
{'하/XS+러/E', '하/VV+러/E'}
{'가/VV+셨/E+습니다/E+./SF'}

# 아기의 냄새가 나는 이불을 덮고 잠이 듭니다.
{'아기/NN+의/JK'}
{'냄새/NN+가/JK', '냄새/NN+가/JX', '냄새/NN+가/VV'}
{'나/VV+는/E', '나/VV+는/JX'}
{'이불/NN+을/JK'}
{'덮/NN+고/E'}
{'잠/NN+이/JK'}
{'듭/VV+니다/E+./SF'}

# 여름 감기는 열이 많이 나거나 배탈, 구토 등 소화기 증상을 동반하는 경우가 많다.
{'여름/NN'}
{'감기/NN+는/E', '감기/NN+는/JX'}
{'열/NN+이/JK'}
{'많이/MA'}
{'나/VV+거나/E'}
{'배탈/NN+,/SP'}
{'구토/NN'}
{'등/NN'}
{'소화기/NN'}
{'증상/NN+을/JK'}
{'동반/NN+하/VV+는/JX', '동반/NN+하/XS+는/E', '동반/NN+하/VV+는/E'}
{'경우/NN+가/JK', '경우/NN+가/JX', '경우/NN+가/VV'}
{'많/VA+다/E+./SF'}

# 리버풀의 위르겐 클롭 감독이 챔피언스리그 무대에서 성사된 레알마드리드와의 맞대결을 기대했다.
{'리버풀/NN+의/JK'}
{'위르겐/NN'}
{'클롭/NN'}
{'감독/NN+이/JK'}
{'챔피언스리그/NN'}
{'무대/NN+에서/JK'}
{'성사/NN+된/XS'}
{'레알마드리드/NN+와/JK+의/JK'}
{'맞대결/NN+을/JK'}
{'기대/NN+했/XS+다/E+./SF'}

# 수니파와 시아파가 오늘날 반목하는 이유를 설명하기 위해서는, 오랜 종교적 차이는 물론 1300년 동안 두 종족이 갈등한 역사의 모든 사회적, 경제적, 문화적 요인까지 알아야 한다.
{'수니파/NN+와/JK', '수니파/NN+와/JC'}
{'시아파/NN+가/JK', '시아파/NN+가/JX', '시아파/NN+가/VV'}
{'오늘날/NN'}
{'반목/NN+하/VV+는/E', '반목/NN+하/VV+는/JX', '반목/NN+하/XS+는/E'}
{'이유/NN+를/JK'}
{'설명/NN+하/VV+기/E', '설명/NN+하/XS+기/E'}
{'위해서/VV+는/JX+,/SP'}
{'오랜/MM'}
{'종교/NN+적/XS'}
{'차이/NN+는/JX', '차이/NN+는/E'}
{'물론/MAG'}
{'1300/SN+년/NN'}
{'동안/NN'}
{'두/MM'}
{'종족/NN+이/JK'}
{'갈등/NN+한/XS'}
{'역사/NN+의/JK'}
{'모든/MM'}
{'사회/NN+적/XS+,/SP'}
{'경제/NN+적/XS+,/SP'}
{'문화/NN+적/XS'}
{'요인/NN+까지/JX'}
{'알/VV+아야/E'}
{'한/VX+다/E+./SF', '한/XS+다/E+./SF'}
```
