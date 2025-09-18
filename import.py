import time
import progressbar

#讀取大檔案,計算共有幾筆留言
data = []
count = 0
bar=progressbar.ProgressBar(max_value=1000000)
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
		count += 1
		#if (count % 400000) == 0:
		#	print(count)
		bar.update(count)
print('檔案讀取完成,總共有',count,'筆資料！')	
#print(data[0])
print('=====================')
# print(data[1])
#----------------------------------------

#計算留言的平均長度
dlen = 0
for d in data:
	dlen += len(d)

print('留言的平均長度為：',dlen / len(data))	 
#----------------------------------------

#獲取留言長度小於100
new=[]
for d in data:
	if len(d)<100 :
		new.append(d)
print('一共有',len(new),'筆留言長度小於100')		
#print(new[0])
#print(new[1])
#----------------------------------------

#留言內容有good字樣時,則存入good[]的list之中
good=[]
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有',len(good),'筆留言提到good')
# 以上四行快寫法:good = [d          for d in data if 'good' in d]
#              good = [1          for d in data if 'good' in d]
#              good = ['bad' in d for d in data if 'good' in d]		
#print(good[0])

bad=[]
for d in data:
	if 'bad' in d:
		bad.append(d)
#print(bad)	
print('一共有',len(bad),'筆留言提到bad')
#------------------------------------------

#dict 字典
# list 與 dict 區別 :
#     list = []                        # list 用法
#     dict = { key:value,key:value }   # dict 用法

# 統計所有的字分別放入dict------------------
start_time=time.time()
#for i in progressbar.progressbar(range(100)):
#    time.sleep(0.02)
wc= {}
for d in data:
	words=d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1		
#----------------------------------------
for word in wc:
	if wc[word] > 1000000:   #百萬以上
		print(word,wc[word])
end_time=time.time()
print('花了',end_time - start_time,'秒 建立字典,一共有',len(wc),'筆資料')
#print(len(wc))		
#print(wc['Allen'])

while True:
	word=input('請問你想查什麼字：(q)')
	if word == 'q':
		break
	if word in wc:
		print(word,'出現過的次數為：',wc[word])
	else:
		print('這個字沒有出現過喔！')

print('感謝使用本查詢功能！')				
