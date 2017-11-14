from nltk.corpus import movie_reviews # malmongchi baggugi
from nltk.classify import NaiveBayesClassifier #   
from nltk.classify.util import accuracy as nltk_accuracy 
#입력 단어 리스트에서 자질 추출 
def extract_features(words): 
    return dict([(word, True) for word in words]) 
if __name__=='__main__': 
#말뭉치에서 리뷰를 로딩 
    fileids_pos = movie_reviews.fileids('pos') 
    fileids_neg = movie_reviews.fileids('neg') 
#리뷰에서 특징 추출
    features_pos = [(extract_features(movie_reviews.words( 
        fileids=[f])), 'Positive') for f in fileids_pos] 
    features_neg = [(extract_features(movie_reviews.words( 
        fileids=[f])), 'Negative') for f in fileids_neg] 
#학습셋과 데이터셋을 나눔 (80%:20%) 
    threshold = 0.8 
    num_pos = int(threshold * len(features_pos)) 
    num_neg = int(threshold * len(features_neg)) 
#학습, 데스트셋 만들기 
    features_train = features_pos[:num_pos] + features_neg[:num_neg] 
    features_test = features_pos[num_pos:] + features_neg[num_neg:] 
#데이터 수 출력 
    print('\nNumber of training datapoints:', len(features_train)) 
    print('Number of test datapoints:', len(features_test)) 
#나이브 베이즈 분류기 학습 
    classifier = NaiveBayesClassifier.train(features_train) 
    print('\nAccuracy of the classifier:', nltk_accuracy(classifier, features_test)) 
#감정분석의 결정적인 단어 N개 출력 
    N = 15 
    print('\nTop ' + str(N) + ' most informative words:') 
    for i, item in enumerate(classifier.most_informative_features()): 
        print(str(i+1) + '. ' + item[0]) 
        if i == N - 1: 
            break 
# 테스트에 사용할 샘플 문장 정의 
# 영화 리뷰를 입력 데이터로 사용 
    input_reviews = [

        'I know some people are worried about the humour on this movie'
        'The humor used excellently in this movie'
        'This movie to me,is at least on the same level with Guardians of the Galaxy'
        ' I mean both guardians and Thor 3 made me laugh but never felt cringe or sensed any forced jokes'
        ' There were also very intense and emotional moments in this Thor movie The fight sequences were so damn epic.When it comes to action,this movie is close to Lord of the Rings'
        ' They did a good job on reflecting the epicness of the Ragnarok event'
        ' I am not even into marvel.I just like epic movies like Lord of the Rings'
        ' But the last trailer of the movie got my attention'
        ' And I made one of the best decisions of my life by watching it'
    ] 
# 샘플 데이터에 대해 예측 결과 출력 
    print("\nMovie review predictions:") 
    for review in input_reviews: 
        print("\nReview:", review) 
# 확률 계산 
    probabilities = classifier.prob_classify(extract_features(review.split())) 
# 가장 높은 값 선택 
    predicted_sentiment = probabilities.max() 
# 결과 출력 
    print("Predicted sentiment:", predicted_sentiment) 
    print("Probability:", round(probabilities.prob(predicted_sentiment), 2))
