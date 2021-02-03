import requests
from bs4 import BeautifulSoup

# URL to get the Case Status
CASE_STATUS_URL = 'https://egov.uscis.gov/casestatus/mycasestatus.do'
NUMBER_OF_RECORDS = 50
SRC_START_NUMBER = 2190098000
MSC_START_NUMBER = 2190720000

# Get the Status of the Case by Receipt Number
def getAppStatus(applicationNumber):
  # Prepare Payload
  payload = {'appReceiptNum': applicationNumber}
  # Make the request call
  caseResultHTMLResponse = requests.post(CASE_STATUS_URL, payload)

  soup = BeautifulSoup(caseResultHTMLResponse.text, features="lxml")

  # Write the response in a temporary file
  with open('downloaded.html', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())

  # Detailed Case Status
  detailedStatus = soup.select('div.rows p')[0]

  # Parse Case Status to get date and form number
  statusParts = detailedStatus.text.split(', ')

  # Get the Status
  status = soup.select('h1')[0].text
  date = statusParts[0].split('On ')[1] + ', ' + statusParts[1]
  form = statusParts[2].split('your Form ')[1]

  # Prepare Response
  record = (form + '; ' + status + '; ' + date)
  print(record)

  return record

# Get Status for a Service Center and Application Number
def getStatusForReceiptNumber(serviceCenter, receiptStartNumber):
  for index in range(NUMBER_OF_RECORDS):
    appReceiptNumber = serviceCenter + str(receiptStartNumber + index + 1)
    try:
      result = appReceiptNumber + "; " + getAppStatus(appReceiptNumber)
      with open('result.csv', 'a', encoding='utf-8') as resultFile:
        resultFile.write(result + '\n')
    except:
      print('----- DONE -----')
      break

# Get SRC Application Status
def srcApplications():
  getStatusForReceiptNumber('SRC', SRC_START_NUMBER)

# Get MSC Application Status
def mscApplications():
  getStatusForReceiptNumber('MSC', MSC_START_NUMBER)

#####################
# MAIN
srcApplications()
