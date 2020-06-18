from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


class Vader:
    def __init__(self):
        print("Vader")
        self.analyzer = SentimentIntensityAnalyzer()

    def updateScore(self, vs):
        print(vs)

        vs['positive']= vs['pos']
        vs['neutral']= vs['neu']
        vs['negative']= vs['neg']

        del vs['compound']
        del vs['pos']
        del vs['neu']
        del vs['neg']

        return vs

    def score(self, sentence):
        vs = self.analyzer.polarity_scores(sentence)
        self.updateScore(vs)

        return vs

if __name__=="__main__":

    sentences = ["VADER is smart, handsome, and funny.",  # positive sentence example
                "VADER is smart, handsome, and funny!",  # punctuation emphasis handled correctly (sentiment intensity adjusted)
                "VADER is very smart, handsome, and funny.", # booster words handled correctly (sentiment intensity adjusted)
                "VADER is VERY SMART, handsome, and FUNNY.",  # emphasis for ALLCAPS handled
                "VADER is VERY SMART, handsome, and FUNNY!!!", # combination of signals - VADER appropriately adjusts intensity
                "VADER is VERY SMART, uber handsome, and FRIGGIN FUNNY!!!", # booster words & punctuation make this close to ceiling for score
                "VADER is not smart, handsome, nor funny.",  # negation sentence example
                "The book was good.",  # positive sentence
                "At least it isn't a horrible book.",  # negated negative sentence with contraction
                "The book was only kind of good.", # qualified positive sentence is handled correctly (intensity adjusted)
                "The plot was good, but the characters are uncompelling and the dialog is not great.", # mixed negation sentence
                "Today SUX!",  # negative slang with capitalization emphasis
                "Today only kinda sux! But I'll get by, lol", # mixed sentiment example with slang and constrastive conjunction "but"
                "Make sure you :) or :D today!",  # emoticons handled
                "Catch utf-8 emoji such as such as 💘 and 💋 and 😁",  # emojis handled
                "Not bad at all"  # Capitalized negation
                ]

    # for sentence in sentences:
    #     vs= Vader().score(sentence)
    #     print("{:-<65} {}".format(sentence, str(vs)))

    s= "cool"
    Vader().score(s)
