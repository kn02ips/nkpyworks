import tkinter as tk
import datetime as dt
import random as r

cnt = 0
clear = 0

kanji_dic = {'信天翁':'あほうどり','金糸雀':'かなりあ','軽鴨':'かるがも','啄木鳥':'きつつき',
             '椋鳥':'むくどり','岩魚':'いわな','皮剥':'かわはぎ','秋刀魚':'さんま','柳葉魚':'ししゃも',
             '翻車魚':'まんぼう','海豚':'いるか','蝙蝠':'こうもり','海馬':'とど','馴鹿':'となかい',
             '土竜':'もぐら','栗鼠':'りす'}

# 問題作成
q_list = list(kanji_dic.keys())
r.shuffle(q_list)

# CGI
root = tk.Tk()
root.title('難読漢字クイズ')
root.minsize(600,400)

# 出題用ウィジェット
q_cnt = tk.Label()
title = tk.Label() 
q = tk.Label()
a = tk.Entry(width = 20)
btn = tk.Button()
tf = tk.Label()

#　結果用ウィジェット
rs =tk.Label()
rp = tk.Label()
pf = tk.Label(bg='#ffd700')
btn2 = tk.Button()


# 出題・結果発表/保存
def ques():
    if cnt < 10:
        tf['text'] = ''
        a.delete(0,tk.END)

        q_cnt['text']=f'{cnt+1}問/10問'
        title['text']='これは何と読む?'
        q['text']=f'{q_list[cnt]}'
        btn['text']='解答'
        btn.bind('<1>',ans_ck)
    else:
        # 出題用ウィジェットの削除
        q_cnt.destroy()
        title.destroy()
        q.destroy()
        a.destroy()
        btn.destroy()
        tf.destroy()

        rs['text']=f'10問中{clear}問正解' 
        if clear == 10:
            pf['text'] = '満点おめでとう！'
            pf.place(x=250,y=50)
        rs.place(x=250,y=80)
        with open('kanji_game_score.csv','a') as score:
            score.write(f'{dt.date.today()},{clear}/10問')
        rp['text'] = '記録を保存しました'
        rp.place(x=240,y=110)

        btn2['text'] ='最初から'
        btn2.bind('<1>',reset)
        btn2.place(x=270,y=135)

# 答え合わせ
def ans_ck(event):
    a['state'] = 'disabled'
    ans = a.get()
    # glibalで関数にclearを呼び込む
    global clear

    if kanji_dic[q_list[cnt]] == ans:
        tf['text'] ='正解！'
        tf.place(x=270,y=150)
        clear += 1
    else:
        tf['text'] = f'正解は {kanji_dic[q_list[cnt]]}'
        tf.place(x=250,y=150)
    
    btn['text'] = '次へ'
    btn.bind('<1>',next)

# 次の問題に進む
def next(event):
    # glibalで関数にcntを呼び込む
    global cnt
    cnt += 1
    a['state'] = 'normal'
    root.after(0,ques)

# 最初からやりなおす
def reset(event):
    global cnt,q_cnt,title,q,a,btn,tf,rs,rp,pf,btn2,q_list
    cnt = 0

    # 結果ウィジェットを削除
    rs.destroy()
    rp.destroy()
    pf.destroy()
    btn2 .destroy()

    # 出題ウィジェットの再構築
    q_cnt = tk.Label()
    title = tk.Label() 
    q = tk.Label()
    a = tk.Entry(width = 20)
    btn = tk.Button()
    tf = tk.Label()

    title.place(x=250,y=50)
    q.place(x=270,y=50+30)
    a.place(x=225,y=110)

    btn.bind('<1>',ans_ck)
    btn.place(x=270,y=150)
    tf.pack()

    # 問題の設定
    r.shuffle(q_list)

    root.after(0,ques)

q_cnt.place(x=260,y=20)
title.place(x=250,y=50)
q.place(x=270,y=50+30)
a.place(x=225,y=110)

btn.bind('<1>',ans_ck)
btn.place(x=270,y=180)

# 1問目出題
ques()

root.mainloop()
