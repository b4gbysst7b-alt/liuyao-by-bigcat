# 定义8种基础三爻卦（0阴1阳）
base_trigram = [
    (0,0,0), (0,0,1), (0,1,0), (0,1,1),
    (1,0,0), (1,0,1), (1,1,0), (1,1,1)
]

# 生成全部64种六爻卦（上卦+下卦组合）
hexagram_64 = []
for up in base_trigram:
    for down in base_trigram:
        six_yiao = up + down
        hexagram_64.append(six_yiao)

# 1. 原始二进制逐位运算
def calc_raw_bit(data):
    ops = 0
    for bit in data:
        _ = bit * 2
        ops += 1
    return ops

# 2. 按六爻卦单元封装运算
def calc_by_64hex(data):
    ops = 0
    unit_len = 6
    total_unit = len(data) // unit_len
    remain = len(data) % unit_len
    # 整卦单元批量运算
    for _ in range(total_unit):
        ops += 1
    # 剩余零散爻位
    if remain > 0:
        ops += 1
    return ops

# 3. 卦象匹配归类运算（复杂场景）
def calc_hex_match(data):
    ops = 0
    unit_len = 6
    chunks = [data[i:i+unit_len] for i in range(0, len(data), unit_len)]
    for chunk in chunks:
        # 匹配64卦模板库判定
        if tuple(chunk) in hexagram_64:
            ops += 1
    return ops

# 测试：3000个阴阳比特数据
total_bits = 3000
test_data = [i%2 for i in range(total_bits)]

raw_count = calc_raw_bit(test_data)
pack_count = calc_by_64hex(test_data)
match_count = calc_hex_match(test_data)

print(f"二进制逐位运算次数：{raw_count}")
print(f"六爻单元打包运算次数：{pack_count}")
print(f"64卦模板匹配运算次数：{match_count}")
print(f"封装后运算缩减比例：{1 - pack_count/raw_count:.2%}")