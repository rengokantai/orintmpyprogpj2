__author__ = 'Hernan Y.Ke'
mywords = [elt.strip() for elt in open("sonnet.txt","r").readlines()]
word_list = [elt.strip() for elt in open("pods.txt","r").readlines()]
word_dict = dict((elt,1)for elt in word_list)  # faster!

counter=0
for word in mywords:
    if word not in word_list:
        print(word)
        counter+=1

print("total %d" % counter)