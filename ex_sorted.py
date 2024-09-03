#numbers =["20240903_11","20240903_12","20240903_13"]

import os
folderName =os.listdir('text')
#print(folderName)
sorted_numbers_dosc = sorted(folderName,reverse=False)
print(f"정렬 :{sorted_numbers_dosc}")