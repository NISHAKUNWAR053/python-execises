1. Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.

def is_two(input):
    
    return input == 2 or input == '2'

print(is_two(2))       
print(is_two('2'))     
print(is_two(3))       
print(is_two(4))     
print(is_two('two'))   

2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

def is_vowel(string):
    
    vowels = ['a','e','i','o','u']
    return string.lower() in vowels

print(is_vowel('a'))
print(is_vowel('A'))
print(is_vowel('d'))

3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.

def is_consonant(string):
    
        return False
   
        return True
print(is_consonant('i'))
print(is_consonant('e'))
print(is_consonant('k'))



4. Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.


def capitalize_first_letter(word):
    
    vowels = 'aeiou'
    
    if word and word[0].lower() not in vowels:
        
        word = word.capitalize()
        
    return word

print(capitalize_first_letter('nisha'))
print(capitalize_first_letter('sha'))
print(capitalize_first_letter('ell'))



def capitalize_first_letter(word):
    
    consonants = 'bcdfghjklmnpqrstvwxyz'
    
    if word and word[0].lower() in consonants:
        
        word = word.capitalize()
        
    return word
print(capitalize_first_letter('nisha'))
print(capitalize_first_letter('isha'))


5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.


def calculate_tip(tip_percent, bill_total):
    if tip_percent <=1:
        tip_amount = tip_percent * bill_total
        return tip_amount
    else:
        return "Please number between 0 and 1."
tip_percent = float(input("Enter tip (between 0 and 1):"))
bill_total = float(input("Enter the total bil:"))

tip = calculate_tip(tip_percent, bill_total)
print("The tip you got", tip)


#another way to code is
def calculate_tip(bill,pecentage):
    return bill*percentage

6. Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.



def apply_discount(original_price, discount_percentage):
    if  discount_percentage <= 100:
        discount_amount = (discount_percentage / 100) * original_price
        discounted_price = original_price - discount_amount
        return discounted_price
    else:
        return "Invalid, Please enter a value between 0 and 100."
    
original_price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage (between 0 and 100): "))

discounted_price = apply_discount(original_price, discount_percent)
print("The discounted price is:", discounted_price)



#another way to do 
def apply_discount(price, discount):
    return price - (price * discount)

apply_discount(100, .15)

7. Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.

def handle_commas(number_string):
    number_without_commas = number_string.replace(",", "")
    return int(number_without_commas)

input_number = "1,234,567"
result = handle_commas(input_number)
print(result) 

8.Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).


def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
input_score = 95
result = get_letter_grade(input_score)
print(result)  



9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.


def remove_vowels(input_string):
    vowels = "aeiouAEIOU"
    result = ""
    for char in input_string:
        if char not in vowels:
            result += char
    return result

input_string = "Hello, World!"
result = remove_vowels(input_string)
print(result)  

10. Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:

. anything that is not a valid python identifier should be removed

. leading and trailing whitespace should be removed

. everything should be lowercase

. spaces should be replaced with underscores

. for example:

  . Name will become name
  
  . First Name will become first_name
  
  . % Completed will become completed

def normalize_name(input):
    new_string = ''
    prev_letter = ''
    # remove leading and ending witespace
    input.strip()
    for letter in input:
        # if a letter is true for letter or number
        if letter.isalum() == True:
            new_string += letter.lower()
        # checks for leading alpanumeric with a space and replace with_
        elif letter == '' and prev_letter.isalnum() == True:
            new_string += '_'
         #increment to the next letter and save it too previous letter
        else:
            new_string +''
            prev_letter = letter
    if new_string [len(new_string)-1] == '_':
        new_string = new_string[:1]
    return new_string

print(normalize_name('name'))

11. Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.

cumulative_sum([1, 1, 1]) returns [1, 2, 3]

cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]


def cumulative_sum(input):
    new_list = []
    count = 1
    for num in input:
        list_sum = sum(input[:count])
        new_list.append(list_sum)
        count += 1
    return new_list

print(cumulative_sum([1, 1, 1]))
print(cumulative_sum([1, 2, 3, 4]))

