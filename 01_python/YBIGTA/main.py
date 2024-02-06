import argparse
from YBIGTA.tokenizers import BPETokenizer, WordTokenizer
from YBIGTA.preprocessing import Preprocessor

def main():
    # 커맨드 라인 argument parsing
    parser = argparse.ArgumentParser(description="Tokenizer CLI")
    parser.add_argument("--use_bpe", type=bool, default=True, help="Whether to use BPE tokenizer")
    parser.add_argument("--n_corpus", type=int, default=30000, help="Size of the corpus")
    parser.add_argument("--n_iter", type=int, default=10000, help="Number of iterations for training")
    args = parser.parse_args()

    #실험을 위한 예시 corpus
    corpus = ["This is a sample sentence.", "Another example sentence."]

    #corpus 전처리
    preprocessor = Preprocessor()
    preprocessed_corpus = preprocessor.preprocess_corpus(corpus)

    # Initialize&tokenizer 사용
    if args.use_bpe:
        bpe_tokenizer = BPETokenizer(corpus=preprocessed_corpus)
        bpe_tokenizer.train(n_iter=args.n_iter)
        result = bpe_tokenizer.tokenize("Test tokenization.")
    else:
        word_tokenizer = WordTokenizer()
        word_tokenizer.add_corpus(preprocessed_corpus)
        result = word_tokenizer.tokenize("Test tokenization.")

    print(result)

if __name__ == "__main__":
    main()
