hypothesis_all = [
  ['John', {
    '0' : 0,
    '1' : 1,
    '2' : 2,
    '3' : 3,
    '4' : 2,
    '5' : 3,
    '6' : 1,
  }],
  ['Daniel', {
    '0' : 3,
    '1' : 2,
    '2' : 1,
    '3' : 0,
    '4' : 2,
    '5' : 0,
    '6' : 0,
  }],
  ['Wilhelm', {
    '0' : 1,
    '1' : 1,
    '2' : 1,
    '3' : 1,
    '4' : 1,
    '5' : 1,
    '6' : 1
  }],
  ]

expected = {
    '0' : ['Daniel'],
    '1' : ['Wilhelm'] ,
    '2' : ['John'],
    '3' : 3,
    '4' : 2,
    '5' : 3,
    '6' : 1,
}

tmp_result = {
    '4': (2, ['John', 'Daniel']),
    '2': (2, ['John']),
    '3': (3, ['John']),
    '0': (3, ['Daniel']),
    '1': (2, ['Daniel']),
    '5': (3, ['John'])}

def get_users(opponent, star, hypothesis_all):
    """ 
    Gets all users who can make 
    @star stars on the opponent @opponent
    """
    return [user for user, hyp in hypothesis_all
     if hyp[opponent]==star]

def count_member(search_member, dic):
    """
    How many times @search_member exists in dic
    (dic is {opponent: (max_star,[])})
    """

    count = 0
    # where = 0 #which opponent
    # print(arr)
    for opponent, best in dic.items():
        opponent = str(opponent)
        for member in best[1]:
            if search_member == member:
                count += 1
                # where = opponent
    return count
    
    
def remove_and_assign(member_row_to_del, tmp_result, result):
    opp, s, member_to_del = member_row_to_del
    for opponent, best in tmp_result.items():
        for member in best[1]:
            if member_to_del == member:
                best[1].remove(member)
                if opp == opponent and s==best[0]:
                    result[opp]=member
                
    return tmp_result, result
    

# print("Before")
# print(tmp_result)
# print("After")
# print("x" + str(remove_and_assign(('1','Daniel',2),tmp_result, {})))            
        

def asign_lonelies(tmp_result):
    def getKey(item):
        return item[1]  

    lonelies = [(opponent, star, users[0]) for opponent, (star, users) in tmp_result.items() if len(users)==1]
    lonelies.sort(key=getKey, reverse=True)
    
    # for o, s, u in lonelies:
    #     tmp_result.remove
    return tmp_result
    
    
def assign_people(hypothesis_all):
    result = {}
    tmp_result= {}
    assigned_people=set()
    
    for opponent in range(0,6):
        max_star = -1
        opponent=str(opponent)
        for user, hypothesis in hypothesis_all:
            assigned_people.add(user)
            if hypothesis[opponent] > max_star:
                max_star = hypothesis[opponent]
                tmp_result[opponent] = (max_star,
                                         get_users(opponent, max_star, hypothesis_all)) # finds all the members who can do 
                                                                                        # 'max_star' stars for the opponent 'opponent';
    # print(tmp_result)
    tmp_result = asign_lonelies(tmp_result) # if there are ppl  who are the only one                                                                                      
    # while(tmp_result.hasKeys):
    # print(tmp_result) 
    for member in assigned_people:
        # print('Searchin for ' + member)
        count, opponent = count_member(member, tmp_result)
        # print('Found' + str(count) + ' ' + str(opponent))

        # if (count == 1):
        #     result[opponent] = member
        #     print("Be4" + tmp_result)
        #     tmp_result.remove(opponent)
        #     print(tmp_result)
 
   # if (len(tmp_result[opponent]) == 1):
   #  result[opponent] = tmp_result[opponent][0]


# print(assign_people(hypothesis_all))  


# print(count_member('Daniel'))


