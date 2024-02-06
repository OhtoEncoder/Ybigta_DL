import re
from typing import List

class Preprocessor:
    def __init__(self):
        pass

    def preprocess_corpus(self, corpus: List[str]) -> List[str]:
        return [self._preprocess_text(text) for text in corpus]

    def _preprocess_text(self, text: str) -> str:
        # 텍스트 전처리 메소드: 소문자로 변환 및 특수문자 제거 (간단한 예시)
        text = text.lower()
        text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
        return text

if __name__ == "__main__":
    #예제로 사용할 Preprocessor 객체 생성하자.
    preprocessor = Preprocessor()

    #예시 corpus 설정
    corpus = ["I love ybigta.", "I like python."]

    # 코퍼스 전처리 수행
    preprocessed_corpus = preprocessor.preprocess_corpus(corpus)

    # 결과 출력
    print(preprocessed_corpus)
