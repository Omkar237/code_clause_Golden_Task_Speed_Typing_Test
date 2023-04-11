
import time


print("!!!!!!...Welcome to speed typing test...!!!!!!")

text = "you are so slow. you cannot catch me"

print("Lets start test you have to type this: ",text)

input("Press enter to start: ")

start_time = time.time()

written_text = input()

end_time = time.time()

elapsed_time = end_time - start_time

if written_text==text:
    print(f"Your time {elapsed_time: .2f} Seconds")
    print(f"you typing speed {len(text)/elapsed_time: .2f} per seconds")

else:
    print("You entered wrong text.")



