import csv

def main():
    # read csv file if it exists
    exampleFile = open('Kirkland.csv')
    exampleDictReader = csv.DictReader(exampleFile)
    # extract fields that are necessary
    for row in exampleDictReader:
        order = row[r'Order No'],
        name = row[r'Recipient'], 
        phone = row[r'Recipient Phone'],
        address = row[r'Recipient Business'] +'\n'+ row[r'Recipient Address'] +'\n'+ row[r'Recipient Address2'] +'\n'+ row[r'Recipient City'] +'\n'+ row[r'Recipient State'] +'\n'+ row[r'Recipient Zip']
    
    # add message
    # Hi, this is Julie from edible Arrangements Kirkland store.
    # We have a delivery for " "  under an order number ending in " ”.
    # We wanted to verify the address given to us. The address is " "
    # Is this the correct address?
    # We make fresh orders in the morning and our driver will be out for delivery from 12 noon to 7pm. Delivery times cannot be guaranteed. You can find more information on Edible Arrangements delivery policy at  https://www.ediblearrangements.com/legal/delivery-policy.aspx 
    # As our product is perishable, we want to make sure that there will be someone to receive it.
    # Thank you

    # create new csv file with extracted fields

# entry point
if __name__ == "__main__":
    main()