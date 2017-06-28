

import os
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
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
	for filename in os.listdir(cwd+'/Categories/gender/' + dirName):

		with open (cwd + '/Categories/gender/'+ dirName + '/' + filename) as f: s= f.read()
		gender_categories.append(dirName)
		genderStrings.append(s)

for dirName in os.listdir(cwd+'/Categories/orientation'):
	fullString = ''
	for filename in os.listdir(cwd+'/Categories/orientation/' + dirName):

		with open (cwd + '/Categories/orientation/'+ dirName + '/' + filename) as f: s= f.read()
		orientation_categories.append(dirName)
		orientationStrings.append(s)

for dirName in os.listdir(cwd+'/Categories/race'):
	fullString = ''
	for filename in os.listdir(cwd+'/Categories/race/' + dirName):

		with open (cwd + '/Categories/race/'+ dirName + '/' + filename) as f: s= f.read()
		race_categories.append(dirName)
		raceStrings.append(s)

# vectorize and convert gender strings into matrix

gender_cats = []
current_val = 0
current_gender = gender_categories[0]
for person in gender_categories:
	if current_gender == person:
		gender_cats.append(current_val)

	else:
		current_gender = person
		current_val += 1
		gender_cats.append(current_val)

GX_train, GX_test, gy_train, gy_test = train_test_split(genderStrings, gender_cats, test_size=0.4)

genderTrain = tfidf_transformer.fit_transform(genderVect.fit_transform(GX_train))
g_clf = MultinomialNB().fit(genderTrain, gy_train)

genderTest = tfidf_transformer.transform(genderVect.transform(GX_test))

gy_pred = g_clf.predict(genderTest)
for i in gy_pred:
	print(gender_categories[i])

print(metrics.accuracy_score(gy_test, gy_pred))

new_quote = "You can't handle the truth! Son, we live in a world that has walls. And those walls have to be guarded by men with guns. Who's gonna do it? You? You, Lt. Weinberg? I have a greater responsibility than you can possibly fathom. You weep for Santiago and you curse the Marines. You have that luxury. You have the luxury of not knowing what I know: that Santiago's death, while tragic, probably saved lives. And my existence, while grotesque and incomprehensible to you, saves lives...You don't want the truth. Because deep down, in places you don't talk about at parties, you want me on that wall. You need me on that wall. We use words like honor, code, loyalty...we use these words as the backbone to a life spent defending something. You use 'em as a punchline. I have neither the time nor the inclination to explain myself to a man who rises and sleeps under the blanket of the very freedom I provide, then questions the manner in which I provide it! I'd rather you just said thank you"
new_quote2 = "and went on your way. Otherwise, I suggest you pick up a weapon and stand a post. Either way, I don't give a damn what you think you're entitled to!"
full_quote = new_quote + new_quote2
galadriel = "In the place of a Dark Lord you would have a Queen! Not dark but beautiful and terrible as the Morn! Treacherous as the Seas! Stronger than the foundations of the Earth! All shall love me and despair!"
viola = "Excuse me, but you don't know enough about life to say a thing like that, Sister...You know the rules maybe, but that don't cover it...You accept what you got to accept and you work with it....Well, he's got to be somewhere, maybe he's doin' some good, too...Well, maybe some of them boys want to get caught. That's why his father beat him. Not the wine...I'm talkin' about the boy's nature now. Not anything he's done. You can't hold a child responsible for what God gave him to be...But then there's the boy's nature...Forget it then. You're gonna force the people to say things. My boy came to your school 'cause they were gonna kill him in the public school. His father don't like him. He come to your school, kids don't like him."



newCounts = genderVect.transform([full_quote, galadriel, viola])
new_tfidf = tfidf_transformer.transform(newCounts)
g_predicted = g_clf.predict(new_tfidf)
#print(pd.DataFrame(genderTrain.toarray(), columns=genderVect.get_feature_names()))

# vectorize and convert orientation strings into matrix


orientationTrain = tfidf_transformer.fit_transform(orientationVect.fit_transform(orientationStrings))

orientation_cats = []
current_val = 0
current_or = orientation_categories[0]
for person in orientation_categories:
	if current_or == person:
		orientation_cats.append(current_val)

	else:
		current_or = person
		current_val += 1
		orientation_cats.append(current_val)

OX_train, OX_test, oy_train, oy_test = train_test_split(orientationStrings, orientation_cats, test_size=0.4)

orientation_Train = tfidf_transformer.fit_transform(orientationVect.fit_transform(OX_train))
o_clf = MultinomialNB().fit(orientation_Train, oy_train)

orientationTest = tfidf_transformer.transform(orientationVect.transform(OX_test))

oy_pred = o_clf.predict(orientationTest)
for i in oy_pred:
	print(orientation_categories[i])
print(metrics.accuracy_score(oy_test, oy_pred))

newCounts = orientationVect.transform([full_quote, galadriel, viola])
# print(newCounts)
new_tfidf = tfidf_transformer.transform(newCounts)
o_predicted = o_clf.predict(new_tfidf)

# print(pd.DataFrame(orientationTrain.toarray(), columns=orientationVect.get_feature_names()))

# vectorize and convert race strings into matrix


race_cats = []
current_val = 0
current_r = race_categories[0]
for person in race_categories:
	if current_r == person:
		race_cats.append(current_val)

	else:
		current_r = person
		current_val += 1
		race_cats.append(current_val)

RX_train, RX_test, ry_train, ry_test = train_test_split(raceStrings, race_cats, test_size=0.4)

race_Train = tfidf_transformer.fit_transform(raceVect.fit_transform(RX_train))
r_clf = MultinomialNB().fit(race_Train, ry_train)

raceTest = tfidf_transformer.transform(raceVect.transform(RX_test))

ry_pred = r_clf.predict(raceTest)
for i in ry_pred:
	print(race_categories[i])
print(metrics.accuracy_score(ry_test, ry_pred))

newCounts = raceVect.transform([full_quote, galadriel, viola])
# print(newCounts)
new_tfidf = tfidf_transformer.transform(newCounts)
r_predicted = r_clf.predict(new_tfidf)



# print(g_predicted)
# print(r_predicted)
# print(o_predicted)
# print(gender_categories[g_predicted[1]])
# print(race_categories[r_predicted[1]])
# print(orientation_categories[o_predicted[1]])
# print(gender_categories[g_predicted[2]])
# print(race_categories[r_predicted[2]])
# print(orientation_categories[o_predicted[2]])

# print(pd.DataFrame(raceTrain.toarray(), columns=raceVect.get_feature_names()))
