def driver():   
  InfoDb = [] 
  InfoDb.append({  
                 "FirstName": "Athena",  
                 "LastName": "Wu",  
                 "DOB": "May 05",  
                 "Residence": "San Diego",  
                 "Email": "athenaw37980@stu.powayusd.com",  
                 "Fav_songs":["Closer","Life Goes On","See You Again"]  
                }) 
  print("The original list:", InfoDb)
  #x = InfoDb[0]["Fav_songs"][1]
  #print(x)
  
  def print_data(n):
      print(InfoDb[n]["FirstName"], InfoDb[n]["LastName"])
      print("\t", "Favorite songs: ", end="")
      print(", ".join(InfoDb[n]["Fav_songs"]))
      print()
    
  def for_loop():
    for n in range(len(InfoDb)):
      print_data(n)
  
  def while_loop(n):
      while n < len(InfoDb):
          print_data(n)
          n += 1
      return
  
  def recursive_loop(n):
      if n < len(InfoDb):
          print_data(n)
          recursive_loop(n + 1)
      return 
  
  def tester():
      print("For loop")
      for_loop()
      print("While loop")
      while_loop(0)
      print("Recursive loop")
      recursive_loop(0)
  print()
  print()
  tester()

if __name__ == "__main__":
    driver()
