

str_zero: str = 'abcdefghijklmnopqrstuvwxyz'
str_one: str = "I am an alphanumberic string with numbers and no punctuation"
str_two: str = "I am an alphanumeric string with numbers and punctionation! Wow! So Cool! IsCool: True"
str_three: str = '1000'
str_four: str = '1000.0'
str_five: str = '*&@#&^(*&@#(&%'
str_six: str = ''
str_seven: str = str(10)
str_eight: str = 'abc123def458'
str_nine: str = '123abc456def'
str_ten: str = 'Hello' + 'World'
str_eleven: str = f'OneHundred{100}'
str_twevle: str = 'john_doe123'


print(f'#0: {str_zero} = ', str_zero.isalnum())
print(f'#1: {str_one} = ', str_one.isalnum())
print(f'#2: {str_two} = ', str_two.isalnum())
print(f'#3: {str_three} = ', str_three.isalnum())
print(f'#4: {str_four} = ', str_four.isalnum())
print(f'#5: {str_five} = ', str_five.isalnum())
print(f'#6: {str_six} = ', str_six.isalnum())
print(f'#7: {str_seven} = ', str_seven.isalnum())
print(f'#8: {str_eight} = ', str_eight.isalnum())
print(f'#9: {str_nine} = ', str_nine.isalnum())
print(f'#10:{str_ten} =  ', str_ten.isalnum())
print(f'#11:{str_eleven} = ', str_eleven.isalnum())
print(f'#12:{str_twevle} = ', str_twevle.isalnum())


try:
    assert str_zero.isalnum(), 'Must Be AlphaNumeric'
except AssertionError as e:
    print(f'{type(e).__name__}: {e}')
    # raise e

try:
    assert str_one.isalnum(), 'Must Be AlphaNumeric'
except AssertionError as e:
    print(f'{type(e).__name__}: {e}')
    raise e