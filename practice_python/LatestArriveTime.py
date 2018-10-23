# 平日の朝、できるだけ長く寝ていたいと思ったあなたは、「何時に家を出発すれば遅刻せずに出社できるか？」ということを常々考えています。
#
# あなたの通勤ルートは次のようになっています。
#
# 1. 自宅から配座（ぱいざ）駅まで a 分間歩く。
# 2. 配座駅に着いた後、一番早く来た電車に b 分間電車に乗って儀野（ぎの）駅に到着する。
# 　(駅に到着してから電車に乗り込むまでの時間は考慮せず、駅に到着した時刻の電車にも乗り込めるものとします)
# 3. 儀野駅から会社まで c 分間歩く。

# input info
# a b c　　#配座駅へまで時間 a 分, 配座駅から儀野駅の乗車時間 b 分, 儀野駅から会社までの時間 c 分
# N　　　　#配座駅から出る電車の本数を表す整数 N
# h_1 m_1　#1本目の電車の発車時刻 h_1 時 m_1 分
# h_2 m_2　#2本目の電車の発車時刻 h_2 時 m_2 分
# ...
# h_N m_N　#N本目の電車の発車時刻 h_N 時 m_N 分

import datetime

input_lines = input()
base_time = input_lines.split(' ')

a_time = base_time[0]
b_time = base_time[1]
c_time = base_time[2]

input_lines = input()
train_times = int(input_lines)

i = 1
train_data = []
while i <= train_times:
    input_lines = input()
    time_of_train = input_lines.split(' ')
    train_data.append(time_of_train)
    i += 1

# ぎのに到着する時間の作成
arrived_time = '8:59'
gino_time_right = datetime.datetime.strptime(arrived_time, '%H:%M') - datetime.timedelta(minutes=int(c_time))

for j in (reversed(train_data)):

    if len(j[0]) == 1:
        j[0] = '0' + j[0]
    if len(j[1]) == 1:
        j[1] = '0' + j[1]
    train_time = ":".join(j)
    gino_time_left = datetime.datetime.strptime(train_time, '%H:%M') + datetime.timedelta(minutes=int(b_time))

    if gino_time_left > gino_time_right:
        continue

    # 出力値作成
    time_x = j[0] + ':' + j[1]
    print_time = datetime.datetime.strptime(time_x, '%H:%M') - datetime.timedelta(minutes=int(a_time))
    print(print_time.strftime('%H:%M'))
    break
