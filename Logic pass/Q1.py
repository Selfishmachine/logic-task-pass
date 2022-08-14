class remove():
   word = input("Enter your sentence: ")
   rw = input("Enter any thing you want to remove: ")

   print("\n Your sentence: ", word)
   word = word.replace(rw, "")

   print(" Your sentence after removing letter(s): ", word)
