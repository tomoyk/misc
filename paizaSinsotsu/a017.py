### INPUT
H,W,N = [int(i) for i in input().split()]
hei=[]
wid=[]
dis=[]
for _ in range(N):
    tmp = [ int(i) for i in input().split() ]
    hei.append(tmp[0])
    wid.append(tmp[1])
    dis.append(tmp[2])
mapper = [ ['.'  for width in range(W) ] for height in range(H)]
# mapper[x][y] :: 座標系は左上を基準にする

### DEBUG
def debug():
    for i in mapper:
        for j in i:
            print(j, end='')
        print()
# debug()

### CALC
def shift_block(NUMBER):
    # block_x, block_yは左上を基準とする
    block_x = dis[NUMBER]
    
    # 0番目の長方形を落とす(移動)[縦方向の移動]
    for block_y in range(0, H-hei[0]+1):
        # print(block_x, block_y)
        
        # 既存の長方形との当たり判定
        for dx in range(wid[NUMBER]):
            for dy in range(hei[NUMBER]):
                # 既存の長方形と衝突
                try:
                    if( mapper[block_y+dy][block_x+dx] == '#' ):
                        # 衝突する直前の座標を返す
                        return block_x, block_y-1
                except:
                    continue
    else:
        return block_x, block_y

def draw_block(x_top, y_top, NUMBER):
    for w in range(wid[NUMBER]):
        for h in range(hei[NUMBER]):
            # print('draw', w, h)
            try:
                mapper[y_top+h][x_top+w] = '#'
                # mapper[x_top+w][y_top+h] = '#'
            except:
                break

### MAIN
# mapper[3][3] = '#'
for i in range(N):
    tmp_x, tmp_y = shift_block(NUMBER=i)
    draw_block(tmp_x, tmp_y, NUMBER=i)
debug()

