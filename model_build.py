import nltk
from nltk.corpus import stopwords
import string
from nltk import FreqDist
from flask import Flask, request
from flask.templating import render_template

#Instance of flask
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('home_page.html')

@app.route('/action', methods =['post'])
def word_count():
    para = request.form.get('paragraph')
    words_list = []
    common_words = []
    punct_count = []

    stopword = stopwords.words('english')

    punct = string.punctuation
    sentences = list(nltk.sent_tokenize(para))
    # print(sentences)
    words = nltk.word_tokenize(para.lower())
    # print(words)
    # print('starting for')
    for i in words:
        # print(i)
        if i in stopword:
            common_words.append(i)
        elif i in punct:
            punct_count.append(i)
        else:
            words_list.append(i)
    
    print(punct_count)
    freq = FreqDist(nltk.word_tokenize(' '.join(words_list)))
    freq_dict = dict(freq)
    # print(freq_dict)
    return render_template('results.html', sentences = sentences, words = words_list, 
                            punct_count = list(set(punct_count)), common_words = list(set(common_words)), freq_dict = freq_dict)


if __name__ == '__main__' :
    app.run(debug = True)

        
