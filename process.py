import pandas as pd
import glob
#test以下のディレクトリのcsvファイルを選択 要変更
path = 'answer/answers/*.csv'
answers = glob.glob(path)
list = []
for file in answers:
    list.append(pd.read_csv(file))

    df = pd.concat(list)
    #アンケート結果追記先
    df.to_csv('answer/all_ansers.csv',index=False,encoding='utf_8_sig')

