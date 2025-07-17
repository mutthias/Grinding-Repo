class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        businesses = set(["electronics", "grocery", "pharmacy", "restaurant"])
        valid_codes = []
        for i in range(0, len(code)):
            cur_code = code[i].replace("_", "A")
            if cur_code != "" and cur_code.isalnum() == True and businessLine[i] in businesses and isActive[i] == True:
                valid_codes.append([code[i], ord(businessLine[i][0])])

        
        valid_codes = sorted(valid_codes, key = lambda x: (x[1], x[0]))
      
        return [code[0] for code in valid_codes]
