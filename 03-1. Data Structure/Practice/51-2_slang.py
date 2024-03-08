sentence = '강도는 서로 쪼개다, 짭새를 보고 빠르게 따돌리며 먹튀했다.'

words = {'꺼지다': '가다',
         '쩔다': '엄청나다',
         '짭새': '경찰관',
         '꼽사리': '중간에 낀 사람',
         '먹튀': '먹고 도망',
         '지린다': '겁을먹다',
         '쪼개다': '웃다',
         '뒷담 까다': '험담하다'}

for key in words.keys():
    if key in sentence:
        print(f'key: {key}')
        sentence = sentence.replace(key, words[key])

print(sentence)

