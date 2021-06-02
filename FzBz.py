    def fizzBuzz(self, n: int) -> List[str]:
        
        cnt3 = 0
        cnt5 = 0
        result = []
        #
        for num in range(1,n+1):
            fzbz = ''
            cnt3 += 1
            cnt5 += 1
            if cnt3 == 3:
                fzbz += 'Fizz'
                cnt3 = 0
            if cnt5 == 5:
                fzbz += 'Buzz'
                cnt5 = 0
            
            result.append(fzbz or str(num))
        return result
            
print(fizzBuzzz(15)
Output:
      ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz","pawan"]
