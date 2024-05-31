class Star_Cinema:
    hall_list = []

    def entry_hall(self, hall):
        Star_Cinema.hall_list.append(hall)


class Hall(Star_Cinema):
    def __init__(self):
        self.seats = {}
        self.show_list = []
        self.rows = 5
        self.cols = 5
        self.hall_no = 5
        self.entry_hall(self)

        self.entry_show("10", "JODI EKDIN", "2:00")
        self.entry_show("11", "KACHER MANUSH", "6:00")

    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self.show_list.append(show_info)
        set_seat = [['O' for _ in range(self.cols)] for _ in range(self.rows)]
        self.seats[id] = set_seat

    def booked_seats(self, id, seat_list):
        if id not in self.seats:
            print("Invalid show id")
            return

        show_seat = self.seats[id]
        for row, col in seat_list:
            if 0 <= row < len(show_seat) and 0 <= col < len(show_seat[0]):
                if show_seat[row][col] == 'O':
                    show_seat[row][col] = '1'
                    print(f'Seat [{row}][{col}] booked successfully..')
                else:
                    print(f'Seat [{row}][{col}] Already booked..!')
            else:
                print(f'Invalid [{row}][{col}] Seat out of Row and colum..!')

    def view_show_list(self):
        print("\n\n\t---------Movie List:---------")
        print("\tID\tMovie_name:\tTime")
        for show in self.show_list:
            print(f'\t{show[0]},\t{show[1]},\t{show[2]}')

    def view_available_seats(self, id):
        if id not in self.seats:
            print("Invalid show id..")
            return
        print(f'Available seats for show id {id}:')

        show_seat = self.seats[id]
        for row in show_seat:
            for seat in row:
                if seat == 'O':
                    print("O", end=' ')
                else:
                    print("1", end=' ')
            print()


counter = Hall()

while True:
    print("\n\n<-----------Welcome to Our Ticket Booking System-------------->")
    print("\n1.Add Movie List")
    print("2.View Movie List")
    print("3.View Available Seats")
    print("4.Book Ticket")
    print("5.Exit")

    option = int(input("Enter your choice: "))

    if option == 1:
        id = input("Enter Movie ID: ")
        movie_name = input("Enter Movie Name: ")
        time = input("Enter Movie Time: ")
        counter.entry_show(id, movie_name, time)

    elif option == 2:
        counter.view_show_list()

    elif option == 3:
        movie_id = input("Enter Movie ID: ")
        counter.view_available_seats(movie_id)

    elif option == 4:
        value = int(input("How many ticket you wanted to purchase: "))
        movie_id = input("Enter Movie ID: ")

        for _ in range(value):
            row = int(input("Enter Number of Row: "))
            col = int(input("Enter Number of col: "))
            counter.booked_seats(movie_id, [(row, col)])
    elif option == 5:
        print("Exiting the program..!")
        break
    else:
        print("Invalid Option")
