import dictionary as d

korToEng = d.KorToEngDictionary()

korToEng.registerWord('책', 'Book')
korToEng.registerWord('나비', 'Butterfly')
korToEng.registerWord('연필', 'pencil')
korToEng.registerWord('학생', 'student')
korToEng.registerWord('선생님', 'teacher')

korToEng.printWords()
print()

korToEng.updateWord('선생님', 'Professor')
korToEng.printWords()
print()

print(f'책 : {korToEng.searchWord('책')}')
print(f'연필 : {korToEng.searchWord('연필')}')
print(f'선생님 : {korToEng.searchWord('선생님')}')
print()

korToEng.removeWord('책')
korToEng.printWords()