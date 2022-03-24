pswd = "psW@d1"

rule_1 = len(pswd) >= 5
rule_2 = not pswd.isupper() and not pswd.islower()
rule_3 = len({"1", "2", "3", "4", "5", "6", "7", "8", "9", "0"} & set(pswd)) > 0
rule_4 = len({"@", "#", "%", "&"} & set(pswd)) > 0

result = (rule_1 and rule_2 and rule_3 and rule_4)

if result :
    print("pswd is good")
else:
    print("pswd is not good")
