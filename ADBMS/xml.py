from lxml import etree 
# Parse the XML file
tree = etree.parse('data.xml')
# Execute an XPath query to get all book titles
titles = tree.xpath('//book/title/text()')
print("Titles of books:\n")
for title in titles:
    print(title)
# Execute an XPath query to get all books in the 'Biography' genre
biography_books = tree.xpath("//book[genre='Biography']")
print("\nData Science Books:")
for book in biography_books:
    print(f"Title: {book.find('title').text}, Author: {book.find('author').text}, Genre: {book.find('genre').text}")
# Execute an XPath query to get all books written by 'Khaled Hosseini'
author = tree.xpath("//book[author='Khaled Hosseini']")
print("\nBooks by Khaled Hosseini:\n")
for book in author:
    print(f"Title: {book.find('title').text} \nAuthor: {book.find('author').text}\nGenre: {book.find('genre').text}\n")
# Execute an XPath query to get books in the 'Biography' genre written by author 'Paulo Coelho'
biography_books_paulocoelho = tree.xpath("//book[genre='Self-help]" and
"//book[author ='Paulo Coelho']")
print("\nBiography Books by Paulo Coelho:\n")
for book in biography_books_paulocoelho:
    print(f"Title: {book.find('title').text}\n")
