import os

def main():
# host_id = os.environ["mysql_host"]

  token = os.environ.get("MYSQL_HOST")
    
  print("ALL good")
  print(token)

  print("hell0")
if __name__ == '_main__':
    main()
# print(host_id)
