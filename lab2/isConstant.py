def isConstant(num: str) -> int:
  if len(num) == 0:  
    return 0

  if num[0] == '-' or num[0] == '+':
    if len(num) == 1:  
      return 0
    num = num[1:] 
  if num.isnumeric():
    return 1
  return 0


if __name__ == "__main__":
  while True:
    text = input("Enter a constant: ")
    if isConstant(text):
      print("Valid\n")
    else:
      print("Invalid")
