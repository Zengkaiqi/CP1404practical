from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def display_taxis(taxis):
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def main():
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]

    current_taxi = None
    bill = 0.0

    print("Let's drive!")

    menu = "q)uit, c)hoose taxi, d)rive"

    while True:
        print(menu)
        choice = input(">>> ").lower()

        if choice == "q":
            print(f"Total trip cost: ${bill:.2f}")
            print("Taxis are now:")
            for i, taxi in enumerate(taxis):
                print(f"{i} - {taxi}")
            break

        elif choice == "c":
            display_taxis(taxis)
            try:
                taxi_choice = int(input("Choose taxi: "))
                if 0 <= taxi_choice < len(taxis):
                    current_taxi = taxis[taxi_choice]
                else:
                    print("Invalid taxi choice")
            except ValueError:
                print("Invalid taxi choice")

            print(f"Bill to date: ${bill:.2f}")

        elif choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                try:
                    distance = float(input("Drive how far? "))
                    current_taxi.start_fare()
                    current_taxi.drive(distance)
                    fare = current_taxi.get_fare()

                    print(f"Your {current_taxi.name} trip cost you ${fare:.2f}")
                    bill += fare

                except ValueError:
                    print("Invalid distance")

            print(f"Bill to date: ${bill:.2f}")

        else:
            print("Invalid option")
            print(f"Bill to date: ${bill:.2f}")


if __name__ == "__main__":
    main()