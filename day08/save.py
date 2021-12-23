def savetofile(memberlist, avgfee):
    with open('record.txt','a',encoding='utf8') as f:
        # 通过列表推导式，产生    人：费用  这样的列表
        recordList = [f'{member}:{avgfee}' for member in memberlist]
        f.write(' | '.join(recordList) + '\n')