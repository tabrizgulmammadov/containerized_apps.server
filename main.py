import requests

def log_info() :
  # api-endpoint
  url = "http://dotnetclient/logger/write-to-console"

  # get passing text
  given_text = input("Please enter your text: ")

  # define a param for the parameters to be sent to the API
  param = {'text': given_text}

  # send post request and log user-defined information
  response = requests.post(url=url, params=param)

  # check result of request
  if response.ok:
    print("Entered text is logged")
  else:
    print(f"An error occured. Reason: '{response.reason}'")


if __name__ == '__main__':
    while True:
        log_info()
