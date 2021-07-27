
def vowel_count(str):
      count = 0
      vowel = set("AEIOU")
      for alphabet in str:
    
         if alphabet in vowel:
            count = count + 1
      
      print("No. of vowels :", count) 

str = "INDIA IS MY COUNTRY"
  
vowel_count(str)