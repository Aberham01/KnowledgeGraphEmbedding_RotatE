'''
本代码的目的就是为了得到 train_equal.txt，把它作为存放关系约束数据的地方

'''

equivalence2id = open("equivalence2id.txt", "r")
relation2id = open("relation2id.txt", "r")
train = open("train.txt", "r")
train_equal = open("train_equal.txt", "w")

# 先需要一个 relation dic
relation_dic = {}
# key 为 id
# value 为 relation name

for item in relation2id.readlines():
    name, num = item.split()[0], item.split()[1]
    relation_dic[num] = name

# 这里需要使用字典来存放等价关系
equivalence_relation_dic = {}
# key 为 relation name
# value 为 与其等价的关系的 list

for item in equivalence2id.readlines():
    r1, r2 = item.split()[0], item.split()[1]
    r1name, r2name = relation_dic[r1], relation_dic[r2]
    if r1name in equivalence_relation_dic:
        equivalence_relation_dic[r1name].append(r2name)
    else:
        equivalence_relation_dic[r1name] = [r2name]

for item in train.readlines():
    r = item.split()[1]
    if r in equivalence_relation_dic:
        train_equal.write(str(len(equivalence_relation_dic[r])))
        for i in equivalence_relation_dic[r]:
            train_equal.write("\t")
            train_equal.write(str(i))
        train_equal.write("\n")
    else:
        train_equal.write("0\n")


