class Hall:
    def __init__(self):
        self.seats = {}
        self.show_list = []
        self.rows = 8
        self.cols = 8
        self.hall_no = 101

        for i in range(1, self.rows + 1):
            row_seats = ['O' for _ in range(self.cols)] 
            self.seats[i] = row_seats

        self.entry_show("111", "Sujon Maji", "18:00")
        self.entry_show("999", "Jawan Maji", "20:00")

    def entry_show(self, show_id, movie_name, time):
        show_info = (show_id, movie_name, time)
        self.show_list.append(show_info)

        self.seats[show_id] = [['O' for _ in range(self.cols)] for _ in range(self.rows)] 

    def entry_show(self, show_id, movie_name, time):
        show_info = (show_id, movie_name, time)
        self.show_list.append(show_info)

       
        self.seats[show_id] = [['O' for _ in range(self.cols)] for _ in range(self.rows)] 

    def book_seats(self, show_id, seats_to_book):
        if show_id not in self.seats:
            print("Invalid show ID")
            return

        show_seats = self.seats[show_id]

        for seat in seats_to_book:
            row, col = seat
            if row < 1 or row > self.rows or col < 1 or col > self.cols:
                print(f"Invalid seat ({row}, {col}). Seat does not exist.")
                continue
            if show_seats[row-1][col-1] == 'X':
                print(f"Seat ({row}, {col}) is already booked.")
            else:
                show_seats[row-1][col-1] = 'X'
                print(f"Seat ({row}, {col}) booked successfully for show ID {show_id}")

    def view_show_list(self):
        if not self.show_list:
            print("No shows available.")
        else:
            print("List of Shows:")
            for idx, show in enumerate(self.show_list, start=1):
                print(f"{idx}. Show ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}")

    def view_available_seats(self, show_id):
        if show_id not in self.seats:
            print("Invalid show ID")
            return

        show_seats = self.seats[show_id]

        print(f"Available Seats for Show ID {show_id}:")
        for i in range(self.rows):
            for j in range(self.cols):
                if show_seats[i][j] == 'O':
                    print(f"Row: {i+1}, Col: {j+1}")

    def view_seats_matrix(self, show_id):
        if show_id not in self.seats:
            print("Invalid show ID")
            return

        print(f"Seat Matrix for Show ID {show_id}:")
        for row in self.seats[show_id]:
            print(' '.join(row))


class TicketCounter:
    def __init__(self):
        self.hall = Hall()

    def view_show_list(self):
        if self.hall:
            self.hall.view_show_list()

    def view_seats_matrix(self):
        if self.hall:
            show_id = input("Enter show ID to view seats matrix: ")
            self.hall.view_seats_matrix(show_id)
        else:
            print("No hall created yet.")

    def book_tickets(self):
        if self.hall:
            show_id = input("Enter show ID to book tickets: ")
            seats_str = input("Enter seats to book (format: row1,col1 row2,col2 ...): ")
            seats_to_book = [tuple(map(int, seat.split(','))) for seat in seats_str.split()]
            self.hall.book_seats(show_id, seats_to_book)
        else:
            print("No hall created yet.")


ticket_counter = TicketCounter()

while True:
    print("\n1. View Show List")
    print("2. View Available Seats")
    print("3. Book Tickets")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        ticket_counter.view_show_list()
    elif choice == '2':
        ticket_counter.view_seats_matrix()
    elif choice == '3':
        ticket_counter.book_tickets()
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")