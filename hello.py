import csv
import os, fnmatch

# clean up an address passed in 
def getCleanAddress(row):
    address = ""
    # extract address related fields
    Recipient_Business = row[r'Recipient Business']
    Recipient_Address = row[r'Recipient Address']
    Recipient_Address2 = row[r'Recipient Address2']
    Recipient_City = row[r'Recipient City']
    Recipient_State = row[r'Recipient State']
    Recipient_Zip = row[r'Recipient Zip']

    # add them to final address if they are not empty
    if Recipient_Business:
        address += Recipient_Business + ", "
    if Recipient_Address:
        address += Recipient_Address + ", "
    if Recipient_Address2:
        address += Recipient_Address2 + ", "
    if Recipient_City:
        address += Recipient_City + ", "
    if Recipient_State:
        address += Recipient_State + ", "
    if Recipient_Zip:
        address += Recipient_Zip 
    return address

# add then params to construct a custom message
def constructMessage(order, name, address):
    # add message
    message = (
    f"Hi,\nThis is Julie from Edible Arrangements Kirkland store.\nWe have a delivery for {name} under an order number {order}. We wanted to verify the address given to us.\n\nThe address is\n{address}\n\nIs this the correct address? Please respond over text.\n\nWe make fresh orders in the morning and our driver will be out for delivery from 12 noon to 7pm. Delivery times cannot be guaranteed. You can find more information on Edible Arrangements delivery policy at https://www.ediblearrangements.com/legal/delivery-policy.aspx As our product is perishable, we want to make sure that there will be someone to receive it.\nThank you"
    )
    print(f'\n======{name}======')
    print(message)
    return message

def process(inputFilePath):
    # read csv file if it exists
    inputFile = open(inputFilePath)
    exampleDictReader = csv.DictReader(inputFile)

    # prep output file too
    # outputFile = open(f'modified_{inputFilePath}', 'w', newline='')
    # outputDictWriter = csv.DictWriter(outputFile, ['Phone', 'Message'])
    

    # extract fields that are necessary
    for row in exampleDictReader:
        order = row[r'Order No']
        name = row[r'Recipient']
        phone = row[r'Recipient Phone']
        address = getCleanAddress(row)
        message = constructMessage(order, name, address)
        # outputDictWriter.writerow({'Phone': phone, 'Message': message})
        f = open(f"{phone}.txt", "w")
        f.write(f"{phone}\n\n{message}");
        f.close()

    # clean up files
    # outputFile.close()
    inputFile.close()

# enumerate all files in current folder
def start():
    listOfFiles = os.listdir('.')
    pattern = "*.csv"
    for csvFile in listOfFiles:
        if fnmatch.fnmatch(csvFile, pattern):
            if not 'modified' in csvFile: 
                process(csvFile)

# entry point
if __name__ == "__main__":
    start()