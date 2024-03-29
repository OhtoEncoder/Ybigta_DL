from typing import Union, List

#죄송합니다 WORD 토크나이저는 뭘 어떻게 해야할지 모르겠어용....
class WordTokenizer:
    def __init__(self):
        pass

    def add_corpus(self, corpus: Union[List[str], str]) -> None:
        pass

    def train(self) -> None:
        pass

    def tokenize(self, text: Union[List[str], str], padding: bool = False, max_length: int = None) -> Union[List[List[int]], List[int]]:
        pass

    def __call__(self, text, padding, max_length) -> Union[List[List[int]], List[int]]:
        return self.tokenize(text, padding, max_length)

    def _preprocess_corpus(self, corpus: Union[List[str], str]) -> List[str]:
        preprocessed_corpus = []
        if isinstance(corpus, str):
            preprocessed_corpus.append(self._preprocess_text(corpus))
        elif isinstance(corpus, list):
            preprocessed_corpus = [self._preprocess_text(text) for text in corpus]

        return preprocessed_corpus


if __name__ == "__main__":
    tokenizer = WordTokenizer()
    tokenizer.add_corpus(["I love Ybigta.", "I like python."])
    result = tokenizer.tokenize("Test tokenization.")
    print(result)
