a, b = map(int, input().split())
tempUp = [10, 5, 1]
tempDown = [-10, -5, -1]
result = 0

if a<b:
    diff = b-a
    if diff%10==8 or diff%10==9 or diff%10==3 or diff%10==4:
        for i in range(0,3):
            for j in range(0,5):
                if diff == 0:
                    break
                if i == 0:
                    if diff < j*tempUp[i]:
                        diff -= (j)*tempUp[i]
                        result += j
                        #print("1","diff:",diff,"dec",j*tempUp[i],"result:",result)
                        break
                else:
                    if diff > (-j)*tempUp[i]:
                        diff += (j-1)*tempUp[i]
                        result += (j-1)
                        #print("2","diff:",diff,"dec",(j-1)*tempUp[i],"result:",result)
                        break

    else:
        for i in range(0,3):
            for j in range(0,5):
                if diff == 0:
                    break
                if diff < j*tempUp[i]:
                    diff -= (j-1)*tempUp[i]
                    result += (j-1)
                    #print("1","diff:",diff,"dec",(j-1)*tempUp[i],"result:",result)
                    break
                elif diff == j*tempUp[i]:
                    diff -= j*tempUp[i]
                    result += j
                    #print("2","diff:",diff,"dec",j*tempUp[i],"result:",result)
                    break
            if diff == 0:
                break

elif a>b:
    diff = b-a
    if diff%10==1 or diff%10==2 or diff%10==6 or diff%10==7:
        for i in range(0,3):
            for j in range(0,5):
                if diff==0:
                    break
                if i==0:
                    if diff>j*tempDown[i]:
                        diff -= j*tempDown[i]
                        result += j
                        print("1","diff:",diff,"inc",j*tempDown[i],"result:",result)
                        break
                else:
                    if diff < (-j)*tempDown[i]:
                        diff += (j-1)*tempDown[i]
                        result += (j-1)
                        print("2","diff:",diff,"inc",(j-1)*tempDown[i],"result:",result)
                        break
    
    else: 
        for i in range(0,3):
            for j in range(0,5):
                if diff == 0:
                    break
                if diff > j*tempDown[i]:
                    diff -= (j-1)*tempDown[i]
                    result += (j-1)
                    #print("1","diff:",diff,"inc",(j-1)*tempDown[i],"result:",result)
                    break
                elif diff == j*tempDown[i]:
                    diff -= j*tempDown[i]
                    result += j
                    #print("2","diff:",diff,"inc",j*tempDown[i],"result:",result)
                    break
            if diff == 0:
                break
else:
    result = 0
print(result)

# 22 3
# 3

# 7 34
# 5

# 27 3
# 4