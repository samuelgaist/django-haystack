from whoosh.analysis.filters import LowercaseFilter
from whoosh.analysis.filters import StopFilter
from whoosh.analysis.morph import StemFilter
from whoosh.analysis.tokenizers import default_pattern
from whoosh.analysis.tokenizers import RegexTokenizer

def StemmingAnalyzer(expression=default_pattern, lang='en',
                     minsize=2, maxsize=None, gaps=False,
                     ignore=None, cachesize=50000):
    """Composes a RegexTokenizer with a lower case filter, a stop
    filter, and a stemming filter.

    >>> ana = StemmingAnalyzer()
    >>> [token.text for token in ana("Testing is testing and testing")]
    ["test", "test", "test"]

    :param expression: The regular expression pattern to use to extract tokens.
    :param lang: language of the StopFilter and StemFilter
    :param minsize: Words smaller than this are removed from the stream.
    :param maxsize: Words longer that this are removed from the stream.
    :param gaps: If True, the tokenizer *splits* on the expression, rather
        than matching on the expression.
    :param ignore: a set of words to not stem.
    :param cachesize: the maximum number of stemmed words to cache. The larger
        this number, the faster stemming will be but the more memory it will
        use. Use None for no cache, or -1 for an unbounded cache.
    """
    ret = RegexTokenizer(expression=expression, gaps=gaps)
    chain = ret | LowercaseFilter()
    chain = chain | StopFilter(lang=lang, minsize=minsize,
                               maxsize=maxsize)
    return chain | StemFilter(lang=lang, ignore=ignore,
                              cachesize=cachesize)