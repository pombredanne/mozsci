import re


class Simple_lda_tokenizer(object):
    """
    This one is based on nltk.
    """
    def __init__(self, pattern=r'''(?:[A-Z]\.)+[A-Z]?|\$?\d+(?:\.\d+)?|\w+(?:-\w+)*|\.\.\.'''):
        self.compiled_re = re.compile(pattern)

    def __call__(self, str):
        return re.findall(self.compiled_re, str)


class Combo_word_tokenizer(Simple_lda_tokenizer):
    def __init__(self):
        """
        Added a regular expression that can handles didn't it's etc. Removed '...' because it's useless to us.
        """
        super(Combo_word_tokenizer, self).__init__(
            pattern=r'''(?:[A-Z]\.)+[A-Z]?|\$?\d+(?:\.\d+)?|\w+'[ts]|\w+(?:-\w+)*''')


def get_lowercase_from_list(word_list):
    return [x.lower() for x in word_list]


if __name__ == '__main__':
#####
# Usage: 1 step, tokenize. 2nd step: get the lower case. 3rd step: get the counts for each word. 4th step: output.
#####
    str = r"haha woiejfwopej us-ab  U.S.A. 123 4.56 U.S.A $3.27 100.27 300 \n it's didn't "
    tokenizer = Combo_word_tokenizer()

    print tokenizer(str)

# print tokenize(str)
