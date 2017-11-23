# 14011198 디지털콘텐츠학과 서보라

## 가설

1. 기호들이 문장에 적으면 probability가 낮아질 것이다.

2. 문장에 최상급 표현이 많으면 probability가 높아질 것이다.

3. 문장에 대문자가 많으면 probability가 낮아질 것이다.

- - - 

## 증명방법

문장 1 과 문장 2를 1번~3번 가설에 맞는 조건으로 비교하여 긴문장과 짧은 문장이 결과에 영향을 미치는지 확인하고 각 가설별로 조건에 맞게 바뀐 문장과 기본문장을 비교하여 각 가설이 맞는지 증명한다.

 ### <문장1>

In conclusion, I took a very pleasant surprise with Thor, and I can recommend it as a very good re-invention of a difficult to handle superhero. It might not be a great film, but it definitely made me have a good time. 

Predicted sentiment: Positive

Probability: 0.84

 

### <문장2>

I like the movie

Predicted sentiment: Negative

Probability: 0.54

 
- - - 
 

## 가설1.기호들이 문장에 적으면 probability가 낮아질 것이다.

 각 기본 문장에서 기호들을 빼고 다시 코딩을 돌렸을 때 결과는 다음과 같다.

### <문장1>

In conclusion I took a very pleasant surprise with Thor and I can recommend it as a very good reinvention of a difficult to handle superhero It might not be a great film but it definitely made me have a good time.

Predicted sentiment: Positive

Probability: 0.86

### <문장2>

I like the movie!!!!

Predicted sentiment: Negative

Probability: 0.52

 

I like the movie!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

Predicted sentiment: Negative

Probability: 0.52

### 결과

긴 문장은 기호를 뺐더니 감정은 바뀌지 않았지만 probability가 0.01이 높아졌다. 짧은 문자은 기본 문장에 기호를 추가하였더니 sentiment가 긍정에서 부정으로 바뀌었으며 Probability가 내려갔다. 이 결과에 따라 유추해보면 문장에 기호가 많은 수록 Probability가 되며 문장 내용과 상관없이 감성이 부정정으로 바뀌는 것을 볼 수 있다. 따라서 1번 가설은 사실이라고 결론 지었다.

 - - - 

## 가설2. 문장에 최상급 표현이 많으면 probability가 높아질 것이다.

 각 기본 문장에 최상급 표현을 추가하여 나온 결과는 다음과 같다.

### <문장1>

In conclusion, I took the most pleasant surprise with Thor, and I can recommend it as the best re-invention of a difficult to handle superhero. It might the worst film, but it definitely made me have the best time.

Predicted sentiment: Positive

Probability: 0.52

### <문장2>

"I like the movie the most"

Predicted sentiment: Positive

Probability: 0.51

### 결론
각 기본문장에 최상급 표현을 넣었더니 긴 문장인 문장1은 probability가 약 0.3줄었고 문장 2의 probability 또한0.03 낮아진것을 볼 수 있다. 입렬 문장에 최상급 표현이 들어가면 probability가 낮아지는 것을 알수 있다. 따라서 가설 2는 사실이 아니라는 결론을 냈다.

- - -

## 가설3. 문장에 대문자가 많으면 probability가 낮아질 것이다.

### <문장1>

IN CONCLUSION, I TOOK AVERY PLEASANT SURPRISE WITH THOR, AND I CAN RECOMEND IT AS A VERY GOOD RE-INVENTION OF A DIFFICULT TO SUPERHERO. It might not be a great film, but it definitely made me have a good time.

Predicted sentiment: Positive

Probability: 0.64

 

 IN CONCLUSION, I TOOK AVERY PLEASANT SURPRISE WITH THOR, AND I CAN RECOMEND IT AS A VERY GOOD RE-INVENTION OF A DIFFICULT TO SUPERHERO. IT MIGHT NOT BE A GREAT FILM, BUT IT DEFINITELY NOT ME HAVE A GOOD TIME

Predicted sentiment: Positive

Probability: 0.5

 

### <문장2>

I LIKE THE MOVIE

Predicted sentiment: Positive

Probability: 0.5

 

### 결론
문장 1에서는 첫번째 결과는 문장의 반만 대문자로 바꾼것이고 두번째 결과는 모든 문장을 대문자를 바꾼 것이다. 이 두 문장의 결과를 보면 문장에 대문자가 많을수록 probability가 낮아지는 것을 알 수 있다. 짧은 문장인 문장 2역시 probability가 낮아지는 것을 볼 수 있었다. 따라서 대문자가 많을수록 probability가 낮아진다는 가설 3은 사실이라고 결론지었다.

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
