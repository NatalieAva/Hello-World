#print('Natalie Fletcher')
#print('o----')
#print(' ||||')
#print('*' * 10)
#print('Andrew ' '<3 ' 'Natalie')

#price = 10
#rating = 4.9
#name = 'Natalie'
#is_published = True
#print(price)

#Name = 'John Smith'
#Age = 20
#is_newpatient = True

#name = input('What is your name? ')
#print('Hi ' + name)

#colour = input('What is your favourite colour? ')
#print(name + ' likes ' + colour)

#birth_year = input('Birth year: ')
#print(type(birth_year))
#age = 2022  - int(birth_year)
#print(type(age))
#print(age)

#weight_lbs = input('How much do you weigh in pounds? ')
#weight_kgs = int(weight_lbs) * 0.45
#print(weight_kgs)

#name = 'Jennifer'
#print(name[1:-1])

#first = 'John'
#last = 'Smith'
#msg = f'{first} {last} is a coder'
#print(msg)

#course = 'Python for Beginners'
#print(course.replace('Beginners', 'Absolute Beginners'))

#is_hot = False
#is_cold = False
#if is_hot:
    #print("It's a hot day")
    #print("Drink plenty of water")
#elif is_cold:
    #print("It's a cold day")
    #print("Wear warm clothes")
#else:
    #print("It's a lovely day")
#print("Enjoy your day")

price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down payment: £{down_payment}")


has_good_credit = True
has_criminal_record = True
if has_good_credit and not has_criminal_record:
    print("Eligible for loan")


name = 'Natalieavafletcherlovesandrewrichardcrawleysbottomandsillysausages'

if len(name) < 3:
    print('name must be at least 3 characters')
elif len(name) > 50:
    print('name can be a maximum of 50 characters')
else:
    print('name looks good!')

#weight_lbs = input('How much do you weigh in pounds? ')
#weight_kgs = int(weight_lbs) * 0.45
#print(weight_kgs)

#Weight = int(input('How much do you weigh? '))
#measurement = input('is this in (L)Pound or (K)Kilo? ')
#if measurement.upper() == 'L':
    #converted = Weight * 0.45
    #print(f'You are {converted} Kilo')
#else:
    #converted = Weight / 0.45
    #print(f'You are {converted} pounds')

#i = 1
#while i <= 5:
    #print('*' * i)
    #i = i + 1
#print('Done')

#secret_number = 9
#guess_count = 0
#guess_limit = 3
#while guess_count < guess_limit:
    #guess = int(input('Guess: '))
    #guess_count += 1
    #if guess == secret_number:
        #print('You won!')
        #break
#else:
    #print('Sorry, you failed')


#name = input('What is your name? ')

#if len(name) < 3:
    #print('name must be at least 3 characters')
#elif len(name) > 15:
    #print('name can not be more than 15 characters')
#else:
    #print('name looks good comrade')


secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print('you won!')
        break
else:
    print(' sorry, you failed')











