
class Star_Cinema:
    hall_list=[]
    def entry_hall(self,hall):
        Star_Cinema.hall_list.append(hall)

class hall(Star_Cinema):
    def __init__(self) -> None:
        self.seats={}
        self.show_list=[]
        self.rows=5
        self.cols=5
        self.hall_no=5
        self.entry_hall(self)
        
        # self.entry_show("10", "JODI EKDIN", "2:00")
        # self.entry_show("11", "KACHER MANUSH DURE THUYE", "6:00")

    def entry_show(self,id,movie_name,time):
        show_info=(id,movie_name,time)
        self.show_list.append(show_info)
        set_seat = [['O' for _ in range(self.cols)] for _ in range(self.rows)]
        self.seats[id]=set_seat 

    def booked_seats(self, id, seat_list):
        if id not in self.seats:
            print("Invalid show id")
            return
        
        show_seat = self.seats[id]
        for row, col in seat_list:
            if 0 <= row < len(show_seat) and 0 <= col < len(show_seat[0]):
                if show_seat[row][col] == '0':
                    show_seat[row][col] = '1'
                    print(f'Seat [{row}][{col}] booked successfully..')
                else:
                    print(f'Seat [{row}][{col}] Already booked..!')
            else:
                print(f'Invalid [{row}][{col}]')

        self.seats[id] = show_seat


    def view_show_list(self):
        print("Running show list:")

        for show in self.show_list:
            print(f'id:{show[0]}, Movie: {show[1]}, Time: {show[2]}')

    def view_available_seats(self,id):
         if id not in self.seats:
             print("Invalid show id..")
             return
         print(f'Available seat for show if {id}')

         show_seat=self.seats[id]
         for row in show_seat:
             for seat in row:
                if seat =='0':
                 print("0",end=' ')

                else:
                 print("1",end=' ')

             print()


class Counter:
    def __init__(self):
        self.hall = hall()
    
    def Add_movie(self):
        if self.hall:
            id =int(input("Enter Movie id: "))
            Movie = input("Enter Movie Name: ")
            time = input("Enter Movie time: ")
            self.hall.entry_show(id,Movie,time)
    def view_show_list(self):
        if self.hall:
            self.hall.view_show_list()

    def view_seats_matrix(self):
        if self.hall:
            show_id = input("Enter show ID to view seats matrix: ")
            self.hall.view_available_seats(show_id)
        else:
            print("No hall created.")

    def book_tickets(self):
        if self.hall:
            show_id = input("Enter show ID to book tickets: ")
            seats_str = input("Enter seats to book (format: row1,col1 row2,col2 ...): ")
            seats_to_book = [tuple(map(int, seat.split(','))) for seat in seats_str.split()]
            self.hall.booked_seats(show_id, seats_to_book)
        else:
            print("No hall created.")


ticket = Counter()

while True:
    print("1.Add Movie List")
    print("2.View Movie List")
    print("3.View Available Seat")
    print("4.Booked ticket")
    print("5.Exit")

    Option =int(input("Enter your choice: "))
    if Option == 1:
        ticket.Add_movie()

    if Option == 2:
        ticket.view_show_list()

    elif Option == 3:
        ticket.view_seats_matrix()

    elif Option == 4:
        ticket.book_tickets()

    elif Option == 5:
        print("Exit the program..")
        break
    else:
        print("Invalid Option")
    







            








    
    
        





        




