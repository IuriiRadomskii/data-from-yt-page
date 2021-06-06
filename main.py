from youtube_parse import *
from db import *


def main():
    print('Hello!')
    connection = connect_to_db()
    flag = True
    while flag:
        url = input('Input url: ')
        data = collect_data_from_page(url)
        if not data:
            continue
        query = add_row_query(data)
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
            connection.commit()
        print('Entry added.')
        while True:
            cont = input('Would you like to continue? (y/n):\n')
            if cont == 'y':
                connection = connect_to_db()
                break
            elif cont == 'n':
                flag = False
                break
            else:
                print("Choose 'y' or 'n'...")
    print('Bye!')


if __name__ == '__main__':
    main()
