import requests
import hashlib
import sys

def request_api_data(query_char):  #API request from the website
  url = 'https://api.pwnedpasswords.com/range/' + query_char
  res = requests.get(url)

  if res.status_code != 200:
    raise RuntimeError(f'Error fetching {res.status_code} check the api call')

  return res



def get_pssd_leaks_count(hashes, hash_to_check):    #print out all the res got from the api
  hashes = (line.split(':') for line in hashes.text.splitlines())
  for h, count in hashes:
    if h == hash_to_check:
      return int(count)
  return 0  




def pwned_api_check(password):   #Apply the hash function and sep 5 chr from rest

  sha1pssd = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
  first5, tail = sha1pssd[:5], sha1pssd[5:]
  response = request_api_data(first5)

  return get_pssd_leaks_count(response, tail)


def main(args):
  for password in args:
    count = pwned_api_check(password)
    if count > 0:
      print(f'The given password {password} has been leaked {count} times. You should probably change it.')
    else:
      print(f'The given password {password} is safe, secure and never been leaked.')

pssd_file = open('passwords.txt')
pssd_list = []

for pssd in pssd_file.readlines()[1:]:
  pssd_list.append(pssd.strip('\n'))

main(pssd_list)





