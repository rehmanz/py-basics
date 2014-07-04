'''
Created on Jul 4, 2014

@author: zrehman
'''
def hash_my_url(url):
    """Return a number between 1 and 1000

    url -- the website address
    """
    # Convert each char in url to an int and store in int_val_l list
    int_val_l = map(ord, url)

    # Sum up all the integer elements
    return (reduce(lambda x, y: x+y, int_val_l))%1000

if __name__ == "__main__":
    print hash_my_url('www.yahoo.com')
    print hash_my_url('www.yahoo.com')
    print hash_my_url('sports.yahoo.com')
    print hash_my_url('www.google.com')
    print hash_my_url('www.mysite.tv')
