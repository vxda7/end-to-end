What = "ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"
score=0

score_list = map(lambda x : -(ord(x)-69), What)

for i in score_list:
    score+=i

print(score)