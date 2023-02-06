'''que = hide a number n=18
    enter a number  and tell the user that the number is greter or lesser and keep the limit of guess 9
    if guess are end  then print game over if number matched with hidden number then print congratulation'''
n = 18
count = 0
guesses = 9

while(guesses!=0):
    num = int(input("Enter any number : "))
    if num == n:
        print("congratulations you finded the number")
        break
    elif num<n:
        print("Lesser than hidden number")
    else:
        print("Greater than hidden number")

    count = count+1
    guesses = guesses-1
    if guesses==0:
        print("Game Over, You exceeded the limit")

print("No of Guesses you took to finish = ",count)
