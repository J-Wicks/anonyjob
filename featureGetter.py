categories = ['alt.atheism', 'soc.religion.christian','comp.graphics', 'sci.med']

import os
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics

genderVect = CountVectorizer()
raceVect = CountVectorizer()
orientationVect = CountVectorizer()
tfidf_transformer = TfidfTransformer()

genderStrings = []
orientationStrings = []
raceStrings = []

gender_categories = []
race_categories = []
orientation_categories = []


# X = vectorizer.fit_transform(corpus)
cwd = os.getcwd()


for dirName in os.listdir(cwd+'/Categories/gender'):
	fullString = ''
	gender_categories.append(dirName)
	for filename in os.listdir(cwd+'/Categories/gender/' + dirName):

		with open (cwd + '/Categories/gender/'+ dirName + '/' + filename) as f: s= f.read()
		fullString = fullString + s
	genderStrings.append(fullString)

for dirName in os.listdir(cwd+'/Categories/orientation'):
	fullString = ''
	orientation_categories.append(dirName)
	for filename in os.listdir(cwd+'/Categories/orientation/' + dirName):

		with open (cwd + '/Categories/orientation/'+ dirName + '/' + filename) as f: s= f.read()
		fullString = fullString + s
	orientationStrings.append(fullString)

for dirName in os.listdir(cwd+'/Categories/race'):
	fullString = ''
	race_categories.append(dirName)
	for filename in os.listdir(cwd+'/Categories/race/' + dirName):

		with open (cwd + '/Categories/race/'+ dirName + '/' + filename) as f: s= f.read()
		fullString = fullString + s
	raceStrings.append(fullString)

# vectorize and convert gender strings into matrix
genderTrain = tfidf_transformer.fit_transform(genderVect.fit_transform(genderStrings))

gender_cats = []

for i in range(0, len(gender_categories)):
	gender_cats.append(i)

g_clf = MultinomialNB().fit(genderTrain, gender_cats)

new_quote = "You can't handle the truth! Son, we live in a world that has walls. And those walls have to be guarded by men with guns. Who's gonna do it? You? You, Lt. Weinberg? I have a greater responsibility than you can possibly fathom. You weep for Santiago and you curse the Marines. You have that luxury. You have the luxury of not knowing what I know: that Santiago's death, while tragic, probably saved lives. And my existence, while grotesque and incomprehensible to you, saves lives...You don't want the truth. Because deep down, in places you don't talk about at parties, you want me on that wall. You need me on that wall. We use words like honor, code, loyalty...we use these words as the backbone to a life spent defending something. You use 'em as a punchline. I have neither the time nor the inclination to explain myself to a man who rises and sleeps under the blanket of the very freedom I provide, then questions the manner in which I provide it! I'd rather you just said thank you"
new_quote2 = "and went on your way. Otherwise, I suggest you pick up a weapon and stand a post. Either way, I don't give a damn what you think you're entitled to!"
full_quote = new_quote + new_quote2

galadriel = "In the place of a Dark Lord you would have a Queen! Not dark but beautiful and terrible as the Morn! Treacherous as the Seas! Stronger than the foundations of the Earth! All shall love me and despair!"

newCounts = genderVect.transform([full_quote, galadriel])
new_tfidf = tfidf_transformer.transform(newCounts)
g_predicted = g_clf.predict(new_tfidf)
#print(pd.DataFrame(genderTrain.toarray(), columns=genderVect.get_feature_names()))

# vectorize and convert orientation strings into matrix


orientationTrain = tfidf_transformer.fit_transform(orientationVect.fit_transform(orientationStrings))

orientation_cats = []

for i in range(0, len(orientation_categories)):
	orientation_cats.append(i)

o_clf = MultinomialNB().fit(orientationTrain, orientation_cats)

new_O_counts = orientationVect.transform([full_quote, galadriel])
new_O_tfidf = tfidf_transformer.transform(new_O_counts)
o_predicted = o_clf.predict(new_O_tfidf)

# print(pd.DataFrame(orientationTrain.toarray(), columns=orientationVect.get_feature_names()))

# vectorize and convert race strings into matrix

raceTrain = tfidf_transformer.fit_transform(raceVect.fit_transform(raceStrings))

race_cats = []

for i in range(0, len(race_categories)):
	race_cats.append(i)

r_clf = MultinomialNB().fit(raceTrain, race_cats)

new_R_counts = raceVect.transform([full_quote, galadriel])
new_R_tfidf = tfidf_transformer.transform(new_R_counts)
r_predicted = r_clf.predict(new_R_tfidf)

new_g_predicted = g_clf.predict(genderTrain)

print(metrics.classification_report(gender_cats, new_g_predicted,
     target_names=gender_categories))
print(gender_categories[g_predicted[0]])
print(race_categories[r_predicted[0]])
print(orientation_categories[o_predicted[0]])
print(gender_categories[g_predicted[1]])
print(race_categories[r_predicted[1]])
print(orientation_categories[o_predicted[1]])

# print(pd.DataFrame(raceTrain.toarray(), columns=raceVect.get_feature_names()))
