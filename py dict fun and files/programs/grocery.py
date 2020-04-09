# About : This is the implementation of while loop to calculate
# total price of the grocery by adding prices of each item
# and then returning the total and average amount of the grocery

# Add function
def checkout():

    # Init total
    total = 0

    # Init count to count number of items
    count = 0

    # Make more items always true to keep the loop working
    moreItems = True

    # Checks if more items are their or not
    while moreItems:
        # Message to enter price of each item
        price = float(input('Enter price of item (0 when done): '))

        # if price is zero then exit
        if price != 0:

            # if price not zero then execute below statments
            # Increment the counter
            count = count + 1

            # Add price f each item
            total = total + price

            # Print the sub total after adding each item
            print('Subtotal: $', total)

        else:
            # if price is zero
            # make the more item = false which will not execute the
            # while loop so it will exit the main while loop
            moreItems = False

    # Calculate the average
    average = total / count

    # prints how many items are their in the items bag
    print('Total items:', count)
    
    print('Total $', total)
    print('Average price per item: $', average)

# function called
checkout()
