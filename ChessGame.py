def open_game():

    global board

    opening_books_path = "PolyGlot_opening_books"
    opening_books = os.listdir(opening_books_path)
    num_opening_books = len(opening_books)
    rand_idx = 0
    rand_opening_book = ""

    if num_opening_books > 0:
        rand_idx = random.randrange(0, num_opening_books)
        rand_opening_book = opening_books[rand_idx]

        opening_books_path = opening_books_path + "/" + rand_opening_book

        print(opening_books_path)
        with chess.polyglot.open_reader(opening_books_path) as reader:
            for entry in reader.find_all(board.board_chess):
                print(entry.move, entry.weight, entry.learn)