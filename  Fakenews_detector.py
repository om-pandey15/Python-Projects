fake_keywords = ["shocking","breaking","secret","exposed","click here","miracle","you win","viral","guaranteed","unbelievable"]
real_keywords = ["report","officals","goverment","confirmed","research","data","study","statement","analysis","source"]

print("------FAKE NEWS DETECTOR-------\n")

NEWS=input("enter news text:\n").lower()#lower text used for in eng lang 
fake_count = 0
real_count = 0

for word in fake_keywords:
    if word in NEWS:
        fake_count += 1

for word in real_keywords:
    if word in NEWS:
        real_count += 1

total = fake_count+real_count
if total == 0:
    trust_score = 50
else:
    trust_score = int((real_count/total*100))

print("\n----RESULT----")
print("fake keywords count: ",fake_count)
print("real keywords count: ",real_count)
print("trust score : ",trust_score,"%")

if trust_score >= 70:
    print("result:😀 real news")

elif trust_score >=40:
    print("result:🙄 suspicious news")

else:
    print("result:😠 fake news")
