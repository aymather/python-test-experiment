import pandas

#trialseq = [(1, 1, 'left', .356), (2, 1, 'right', .444), (3, 1, 'right', .398)]
trialnum = [0,1,2,3,4,5,6,7,8,9,10]
blocknum = [1,1,1,1,1,1,2,2,2,2,2]
side = ['left', 'left', 'right', 'left', 'right', 'left', 'left', 'right', 'right', 'right']
rt = [.43, .44, .34, .35, .36, .26, .45, .55, .34, .40]

trialseq = list(zip(trialnum, blocknum, side, rt))
t = pandas.DataFrame(data = trialseq, columns = ['Trial_num', 'Block', 'Side', 'RT'])
t.to_csv('sequence.csv', index = False, header = True)
loc = r'/Users/alecmather/Desktop/python_proj/sequence.csv'
df = pandas.read_csv(loc)

values = t.sort_values('RT', ascending = False)
#print(t['RT'])
t.plot()
#print(values)
#print(df)
#print(t.RT.dtype)
