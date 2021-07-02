import ytdata
import re
import nltk
import heapq

def get_text_summary(id=None):
    if not id:
        return "No ID Was Provided"
    nltk.download('punkt')
    nltk.download('stopwords')
    # getting transcript from youtube (gets data and combines it to a string)
    full_transcript = ytdata.get_ytdata(id)
    # file = open('transcript.txt','w')
    # file.write(full_transcript)
    # file.close()

    # cleaning data (removes brackets , special characters etc)
    full_transcript = re.sub(r'\[[0-9]*\]', ' ', full_transcript)
    full_transcript = re.sub(r'\s+', ' ', full_transcript)
    formatted_transcript_text = re.sub('[^a-zA-Z]', ' ', full_transcript )
    formatted_transcript_text = re.sub(r'\s+', ' ', formatted_transcript_text)
    #print(formatted_transcript_text)

    #converting text to sentences
    sentence_list = nltk.sent_tokenize(full_transcript)

    #find weighted frequency of occurence
    stopwords = nltk.corpus.stopwords.words('english')
    word_frequencies = {}
    for word in nltk.word_tokenize(formatted_transcript_text):
        if word not in stopwords:
            if word not in word_frequencies.keys():
                word_frequencies[word] = 1
            else:
                word_frequencies[word] += 1

    maximum_frequency = max(word_frequencies.values())
    for word in word_frequencies.keys():
        word_frequencies[word] = (word_frequencies[word]/maximum_frequency)

    #calculate the sentence score
    sentence_scores ={}
    for sent in sentence_list:
        for word in nltk.word_tokenize(sent.lower()):
            if word in word_frequencies.keys():
                if len(sent.split(' '))  < 30:
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word]
                    else:
                        sentence_scores[sent] += word_frequencies[word]

    #getting summary
    summary_sentences = heapq.nlargest(7,sentence_scores,key=sentence_scores.get)

    summary = ' '.join(summary_sentences)

    return summary


