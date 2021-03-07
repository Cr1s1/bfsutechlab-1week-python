# 6.3 逻辑运算符

# 6.3.1 and运算符
'''
举例：想要实现 “if applicant has high income AND good credit
                Eligible for loan”   的判断逻辑 “是否有资格获得贷款”
'''
has_high_income = True
has_good_credit = True
if has_high_income and has_good_credit:
    print("Eligible for loan")
'''
运行结果：Eligible for loan
'''

has_high_income = False
has_good_credit = True
if has_high_income and has_good_credit:
    print("Eligible for loan")
'''
运行无输出
结论：and运算符需要左右两个表达式同时为真，整体才为真
'''

# 6.3.2 or运算符
'''
举例：想要实现 “if applicant has high income OR good credit
                Eligible for loan”   的判断逻辑 “是否有资格获得贷款”
'''
has_high_income = False
has_good_credit = True

if has_high_income or has_good_credit:
    print("Eligible for loan")
'''
运行结果：Eligible for loan
'''

has_high_income = False
has_good_credit = False

if has_high_income or has_good_credit:
    print("Eligible for loan")
'''
运行无输出
结论：or运算符，只有当左右两个表达式同时不成立，整体才为假
'''

# 6.3.3 not运算符
has_high_income = True
has_criminal_record = False

if has_high_income and not has_criminal_record:
    print("Eligible for loan")
'''
运行结果：Eligible for loan

结论：not运算符可以把原来设置成False的布尔值转换成与之相反的True
'''

has_high_income = False
has_criminal_record = False

if has_high_income and not has_criminal_record:
    print("Eligible for loan")
'''
运行无输出
'''