"""
Just a tiny module to stack some functions used in the exercise
"""

import re
from bs4 import BeautifulSoup

def cleaner(text:str=None, is_html=False):
    # remove html tags
    if is_html:
        text = BeautifulSoup(text).get_text()
    # converto to lower
    text = text.lower()
    # fetch only alphabetic characters
    text = re.sub(r'[^a-z]', ' ', text)
    # split into tokens to remove whitespaces
    tokens = text.split()

    return " ".join(tokens)


def classify(pred_prob, thres):
    """
    More useful when multilabel. But it works for binary as well
    """
    y_pred_seq = []
    for i in pred_prob:
        temp = []
        for j in i:
            if j>thres:
                temp.append(1)
            else:
                temp.append(0)
        y_pred_seq.append(temp)

    return y_pred_seq