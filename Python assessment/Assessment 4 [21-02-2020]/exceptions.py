class Error(Exception):
    pass


class AgeTooSmall(Error):
    pass


class AgeTooLarge(Error):
    pass


number = 18
number2 = 100

while True:
    try:
        age = int(input('Enter your age: '))
        print(number / age)
        print('number' + age)
        if age < number:
            raise AgeTooSmall
        elif age > number2:
            raise AgeTooLarge

        break

    # built in exception
    except ValueError:
        print('Please enter the age in number format.')

    except ZeroDivisionError:
        print('Age cannot be zero')

    except TypeError as e:
        print(e)

    # user defined exception
    except AgeTooSmall:
        print("You are a minor and cannot vote, please try when you are 18...")
        print()
    except AgeTooLarge:
        print("Your age is too much to vote")
        print()

print("Congratulations! You can vote.")
