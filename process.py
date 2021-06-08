import pandas as pd
import glob
#test以下のディレクトリのcsvファイルを選択 要変更
path = '/Users/komakoma/Box/test/answers/*.csv'
answers = glob.glob(path)
list = []
for file in answers:
    list.append(pd.read_csv(file))

    df = pd.concat(list)
    #アンケート結果追記先
    df.to_csv('/Users/komakoma/Box/test/all_ansers.csv',index=False,encoding='utf_8_sig')

