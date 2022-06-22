text="abaabdcff"#first recurssive
# word_count={}
# for w in text:
#     if w in word_count:
#         print('first_reccursive',w)
#         break
#     else:
#         word_count[w]=1
# word_count={}
# rec_word=[]
# for w in text:
#     if w in word_count:
#         rec_word.append(w)
#     else:
#         word_count[w]=1
# print(max(rec_word))
word_count={"a":2,"b":4,"v":5}
wc_list=word_count.items()
print(sorted(wc_list,key=lambda items:items[1],reverse=True))
print(max(wc_list,key=lambda items:items[1]))
print(min(wc_list,key=lambda items:items[1]))