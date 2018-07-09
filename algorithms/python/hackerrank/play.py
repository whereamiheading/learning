def uniqueMorseRepresentations( words):
    """
    :type words: List[str]
    :rtype: int
    """

    dict_map = {
     "a":".-",
     "b":"-...",
     "c":"-.-.",
     "d": "-..",
     "e":".",
     "f":"..-.",
     "g":"--.",
     "h":"....",
     "i":"..",
     "j":".---",
     "k":"-.-",
     "l":".-..",
     "m":"--",
     "n":"-.",
     "o":"---",
     "p":".--.",
     "q":"--.-",
     "r":".-.",
     "s":"...",
     "t":"-",
     "u":"..-",
     "v":"...-",
     "w":".--",
     "x":"-..-",
     "y":"-.--",
     "z":"--.."}

    morse_word_list = []
    for word in words:
        morse_word = ""
        for char in word:
            morse_char = dict_map[char]
            morse_word += morse_char
        if morse_word not in morse_word_list:
            morse_word_list.append(morse_word)
    print morse_word_list
    return len(morse_word_list)

# def unique(words):
#     d = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
#          "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
#     return len({''.join(d[ord(ch) - ord('a')])for ch in word for word in words})




res = uniqueMorseRepresentations(["gin" , "zen", "gig", "msg"])
print res
words = ["gin" , "zen", "gig", "msg"]
# r=unique(words)


def numJewelsInStones(J, S):
    """
    :type J: str
    :type S: str
    :rtype: int
    """
    return sum(s in J for s in S)

J = 'aA'
S = 'aAAbbbb'
j= numJewelsInStones(J,S)
print j

class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return [[ 1-j for j in element[::-1]] for element in A]


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = re.sub('[^A-Za-z0-9]+', '', s).lower()
        return s == s[::-1]



Insert into tblEmployee values (1, 'Tom', 2);
Insert into tblEmployee values (2, 'Josh', null);
Insert into tblEmployee values (3, 'Mike', 2);
Insert into tblEmployee values (4, 'John', 3);
Insert into tblEmployee values (5, 'Pam', 1);
Insert into tblEmployee values (6, 'Mary', 3);
Insert into tblEmployee values (7, 'James', 1);
Insert into tblEmployee values (8, 'Sam', 5);
Insert into tblEmployee values (9, 'Simon', 1);




with empCTE  as
(
select employeeid, name, managerid, 1
from tblEmployee
where managerid is null

union all

select emp.employeeid, emp.name, emp.managerid , cte.leve+1
from tblEmployee emp
left join  empCTE cte
on tblEmployee.managerid = empCTE.EmployeeId
)
select emp.name , mgr.name , emp.leve
from empCTE as emp
left join empCTE as mgr
on emp.managerid = mgr.employeeid


With
 recursive EmployeesCTE
  as
  (

      Select tbl.EmployeeId, tbl.Name,
      tbl.ManagerId, cte.Lev + 1
      from tblEmployee tbl
      join EmployeesCTE cte
      on tbl.ManagerID = cte.EmployeeId
    )select name from EmployeesCTE


    Select EmployeeId, Name, ManagerId, 1
    from tblEmployee
    where ManagerId is null

    union all


' '.join((s.split())[::-1])





With
 recursive EmployeesCTE (EmployeeId, Name, ManagerId, Lev)
  as
  (
    Select EmployeeId, Name, ManagerId, 1
    from tblEmployee
    where ManagerId is null

    union all

    Select tblEmployee.EmployeeId, tblEmployee.Name,
    tblEmployee.ManagerId, EmployeesCTE.Lev + 1
    from tblEmployee
    join EmployeesCTE
    on tblEmployee.ManagerID = EmployeesCTE.EmployeeId
  )
Select EmpCTE.Name as Employee, coalesce(MgrCTE.Name, 'Super Boss') as Manager,
EmpCTE.Lev
from EmployeesCTE EmpCTE
left join EmployeesCTE MgrCTE
on EmpCTE.ManagerId = MgrCTE.EmployeeId

mo

def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        """
        O(paragraph) Time
        O(paragraph+banned) Space
        """

        banned = set(banned)
        # maintain dict of word frequency of words which are not in banned
        hashmap = {}
        mostcommon = ''
        count = 0
        for word in paragraph.split():
            word = word.strip('!?\',;.').lower()
            # while inserting words in frequency keep track of most frequent word
            if word not in banned:
                hashmap[word] = hashmap.get(word,0) + 1
                if hashmap[word] > count:
                    count = hashmap[word]
                    mostcommon = word
        return mostcommon
