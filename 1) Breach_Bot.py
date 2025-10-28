#Breach Bot Starter Code
breachYear = 2017

#Greets user
print("Hello! I'm Breach Bot.")
userName = input("What is your name?\n")
print("Nice to meet you " + userName)

#Recounts year of breach
todaysYear = input("What year is it?\n")
timePassed = int(todaysYear) - breachYear
print("Wow! That means it has been " + str(timePassed) + " years since the Hong Kong Registration and Electoral Office data breach!")


#Introduces breach
print("Would you like to learn about the Hong Kong Registration and Electoral Office data breach?")
giveInfo = input("Type 'yes' or 'no'\n")

#Explains breach
while giveInfo.lower() == "yes":
  print("What would you like to learn more about? Enter the lowercase letter of the following options: \n(a) breach details, (b) organization's response, (c) I would like to hear your reflection")
  topic = input()
  
  if topic.lower() == "a":
    print("Two laptops were stolen from a locked storeroom containing voter registration records and names of members of its Election Committee.\nThey were initially stored in a locked room at the AsiaWorld Expo, and the door to the room was locked, requiring a passcode and access card to enter. However, the door did not seem to be forced open. Five days after the laptops were stored in the room, it was discovered that the computers had been taken out of their bags.")
  
  elif topic.lower() == "b":
    print("The Registration and Electoral Office informed voters who were affected by the breach as soon as possible. However, they did not seem to recommend that affected users do anything, as the data that was stolen was voter registration data such as ID card numbers, physical addresses, and mobile phone numbers, along with the names of members of the Election Committee. None of which can be changed very quickly.")
  
  elif topic.lower() == "c":
    break
    
  else:
    print("Sorry, I didn't catch that. Choose one of the options listed.")
  
  input("\nPress enter to continue\n")

#Introduces my take
print("\nI'm excited to share my perspective with you. Are you ready to hear my take?")
giveInfo = input("Type 'yes' or 'no'\n")

#Shares my take
while giveInfo.lower() == "yes":
  print("What would you like to learn more about? Enter the lowercase letter of the following options: \n(a) relation to CIA Triad, (b) my reaction, (c) my advice, (d) none")
  topic = input()

  if topic.lower() == "a":
    print("The Hong Kong Registrations & Electoral Office data breach connects to the confidentiality pillar of the CIA triad because now people who are not meant to see sensitive voter information are allowed to access it.")

  elif topic.lower() == "b":
    print("I disagree with the organization's response because they did not seem as panicked as they should have been in their response to the breach. I feel like they should’ve offered a better plan of action to affected users so that they don’t feel completely useless during the breach.")

  elif topic.lower() == "c":
    print("I would convince victims to take action by ensuring that other sensitive information of theirs is secure and changing any passwords that have been compromised by the breach. My advice would be to continue monitoring the status of the breach and whether or not the organization has resolved the issue yet.")

  elif topic.lower() == "d":
    break

  else:
    print("Sorry, I didn't catch that. Choose one of the options listed.")

  input("\nPress enter to continue\n")


#Chatbot ends conversation
print("Thanks for chatting with me, and I hope you learned something new!")