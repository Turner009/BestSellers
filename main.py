from data import data_list


def run_analysis(books):
    print('')
    print("*******************************************************************")
    print('')
    example_analysis(books)
    print('')
    print("*******************************************************************")
    print('')
    analysis_one(books)
    print('')
    print("*******************************************************************")
    print('')
    analysis_two(books)
    print('')
    print("*******************************************************************")
    print('')
    analysis_three(books)


def example_analysis(book_list):
    print("Analysis of which book had the highest price in 2016")
    # Find all books from 2016
    # Use a Lambda filter function to find books who have a year of 2016
    # Converting to a list, and saving as variable books_2016
    books_2016 = list(filter(lambda book: book['year'] == 2016, book_list))
    # Calculating the maximum price, and saving that book as highest_cost_book
    # Using max(), with Lambda function
    highest_cost_book = max(books_2016, key=lambda book: book['price'])
    # Print that book's name & price to terminal
    print(
        f"The most expensive book in 2016 was {highest_cost_book['name']} with a price of {highest_cost_book['price']}")


def analysis_one(book_list):
    print("Analysis of which book had the lowest number of reviews in 2018")
    books_2018 = list(filter(lambda book: book['year'] == 2018, book_list))
    least_reviewed_book = min(books_2018, key=lambda book: book['number_of_reviews'])
    print(f"The least reviewed book in 2018 was {least_reviewed_book['name']}, being reviewed only {least_reviewed_book['number_of_reviews']} times!")
    pass

def analysis_two(book_list):
    print("Analysis of which genre (fiction or non-fiction) has appeared the most in the top 50's list")
    fiction = [books for books in book_list if books['genre'] == 'Fiction']
    non_fiction = [books for books in book_list if books['genre'] == 'Non Fiction']    
    compare = lambda genre1, genre2 :print(f"{str(genre1[0]['genre'])} appeared the most with {len(genre1)} appearances.") if  len(genre1) > len(genre2) else print(f"{str(genre2[0]['genre'])} appeared the most with {len(genre2)} appearances.")
    compare(fiction, non_fiction)
    # print(fiction[51]['name'])
    

def analysis_three(book_list):
    print("Analysis of which book has appeared the most in the top 50's list, and how many times it has appeared")
    names = [books['name'] for books in book_list]
    count = dict(map(lambda books  : (books, list(names).count(books)), names))
  
    max_keys = [key for key, value in count.items() if value == max(count.values())]
    max_value = max(count.values())

    print(f"The book {max_keys} has appeared the most times with {max_value} appearances")
     
     
    # print(f"{max(names)}")
    # print(min(names))

    
   

    
    

    

# BONUS USER STORIES:


def bonus_analysis_one(book_list):
    print("Analysis of which author has shown up on the top 50's list the most (Distinct books only!)")


def bonus_analysis_two(book_list):
    print("Analysis of the top book for each year, based on the book's user ratings and number of reviews")


def bonus_analysis_three(book_list):
    print("Analysis of which book has appeared the most consecutively on top 50's list")


run_analysis(data_list)
