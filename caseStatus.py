import requests
from bs4 import BeautifulSoup
import traceback

import configurationParser as CP
import db.dbServiceCenter as SrcCtr

# Get the Status of the Case by Receipt Number
def getAppStatus(applicationNumber) -> list:
  # Prepare Payload
  payload = {'appReceiptNum': applicationNumber}

  # Make the request call
  caseResultHTMLResponse = requests.post(CP.CASE_STATUS_URL, payload)
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
  record = [ form, status, date ]

  return record

# Exception Counter
counter = 0

# Get Status for a Service Center and Application Number
def getStatusForReceiptNumber(serviceCenter, receiptStartNumber):
  global counter
  for index in range(CP.NUMBER_OF_RECORDS):
    appReceiptNumber = serviceCenter + str(receiptStartNumber + (index * 1) + 1)
    try:
      result = getAppStatus(appReceiptNumber)
      result.insert(0, appReceiptNumber)

      # Insert in DB
      SrcCtr.insertReceiptStatus(result)
    except Exception as ex:
      traceback.print_exception(type(ex), ex, ex.__traceback__)
      counter = counter + 1
      if counter > 3:
        counter = 0
        break
  print('----- DONE -----', '(', serviceCenter, ')')
  return
