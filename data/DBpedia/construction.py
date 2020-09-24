'''
本代码的目的是为了构造符合当前代码的数据集
原数据集的格式参考的是清华THUNLP的格式
原数据集中的第一行是介绍当前文档中的数据量，这一行已经被我删掉了
'''

entity2id = open("entity2id.txt", "r")
# entitiesDict = open("entities.dict", "w")
relation2id = open("relation2id.txt", "r")
# relationsDict = open("relations.dict", "w")

train2id = open("train2id.txt", "r")
train = open("train.txt", "w")
test2id = open("test2id.txt", "r")
test = open("test.txt", "w")
valid2id = open("valid2id.txt")
valid = open("valid.txt", "w")

'''
下面被注释掉的两个for循环，跟后面的代码有冲突
'''
# for item in entity2id.readlines():
#     name, num = item.split()[0], item.split()[1]
#     entitiesDict.write(num + "\t" + name + "\n")

# for item in relation2id.readlines():
#     name, num = item.split()[0], item.split()[1]
#     relationsDict.write(num + "\t" + name + "\n")

entity_dict = {}
relation_dict = {}

for item in entity2id.readlines():
    name, num = item.split()[0], item.split()[1]
    entity_dict[num] = name

for item in relation2id.readlines():
    name, num = item.split()[0], item.split()[1]
    relation_dict[num] = name

for item in train2id.readlines():
    h, t, r = item.split()[0], item.split()[1], item.split()[2]
    train.write(entity_dict[h] + "\t" + relation_dict[r] + "\t" + entity_dict[t] + "\n")

for item in test2id.readlines():
    h, t, r = item.split()[0], item.split()[1], item.split()[2]
    test.write(entity_dict[h] + "\t" + relation_dict[r] + "\t" + entity_dict[t] + "\n")

for item in valid2id.readlines():
    h, t, r = item.split()[0], item.split()[1], item.split()[2]
    valid.write(entity_dict[h] + "\t" + relation_dict[r] + "\t" + entity_dict[t] + "\n")
