"""
WaitWise Studio
---------------
Interactive interface for the WaitWise system.

This application allows users to:

- Add service locations
- View all locations
- Analyze a specific location
- Compare waiting times
- Get the best location recommendation
"""

from wait_wise import WaitWise


class WaitWiseStudio:

    def __init__(self):

        self.system = WaitWise()

    # ----------------------------------
    # Add Service Location
    # ----------------------------------
    def add_location(self):

        print(
            "\n========== ADD SERVICE LOCATION ==========\n"
        )

        location_id = input(
            "Location ID: "
        ).strip()

        # Check duplicate ID
        if self.system.find_location(
                location_id):

            print(
                "\nLocation ID already exists."
            )

            return

        name = input(
            "Location Name: "
        ).strip()

        # ----------------------------------
        # Queue Size
        # ----------------------------------
        while True:

            try:

                queue_size = int(
                    input(
                        "Number of People in Queue: "
                    )
                )

                if queue_size < 0:

                    print(
                        "Queue size cannot be negative."
                    )

                    continue

                break

            except ValueError:

                print(
                    "Please enter a valid number."
                )

        # ----------------------------------
        # Service Counters
        # ----------------------------------
        while True:

            try:

                service_counters = int(
                    input(
                        "Number of Service Counters: "
                    )
                )

                if service_counters <= 0:

                    print(
                        "Service counters must be "
                        "greater than 0."
                    )

                    continue

                break

            except ValueError:

                print(
                    "Please enter a valid number."
                )

        # ----------------------------------
        # Average Service Time
        # ----------------------------------
        while True:

            try:

                average_service_time = float(
                    input(
                        "Average Service Time "
                        "(minutes): "
                    )
                )

                if average_service_time <= 0:

                    print(
                        "Service time must be "
                        "greater than 0."
                    )

                    continue

                break

            except ValueError:

                print(
                    "Please enter a valid number."
                )

        # ----------------------------------
        # Currently Serving
        # ----------------------------------
        while True:

            try:

                currently_serving = int(
                    input(
                        "People Currently Being Served: "
                    )
                )

                if currently_serving < 0:

                    print(
                        "Value cannot be negative."
                    )

                    continue

                if (

                    currently_serving
                    >
                    queue_size

                ):

                    print(
                        "Currently serving cannot be "
                        "greater than queue size."
                    )

                    continue

                break

            except ValueError:

                print(
                    "Please enter a valid number."
                )

        # ----------------------------------
        # Maximum Queue Capacity
        # ----------------------------------
        while True:

            try:

                max_queue_capacity = int(
                    input(
                        "Maximum Queue Capacity: "
                    )
                )

                if max_queue_capacity <= 0:

                    print(
                        "Maximum capacity must be "
                        "greater than 0."
                    )

                    continue

                if (

                    queue_size
                    >
                    max_queue_capacity

                ):

                    print(
                        "Queue size cannot be greater "
                        "than maximum capacity."
                    )

                    continue

                break

            except ValueError:

                print(
                    "Please enter a valid number."
                )

        # ----------------------------------
        # Add Location
        # ----------------------------------
        location = self.system.add_location(

            location_id,
            name,
            queue_size,
            service_counters,
            average_service_time,
            currently_serving,
            max_queue_capacity

        )

        print(
            "\nLocation added successfully."
        )

        print(
            f"Location: {location['Name']}"
        )

    # ----------------------------------
    # View All Locations
    # ----------------------------------
    def view_locations(self):

        if not self.system.locations:

            print(
                "\nNo service locations available."
            )

            return

        print(
            "\n========== SERVICE LOCATIONS ==========\n"
        )

        for location in self.system.locations:

            print(
                f"{location['ID']} | "
                f"{location['Name']}"
            )

            print(
                f"  Queue Size: "
                f"{location['Queue Size']}"
            )

            print(
                f"  Service Counters: "
                f"{location['Service Counters']}"
            )

            print(
                f"  Average Service Time: "
                f"{location['Average Service Time']} minutes"
            )

            print(
                f"  Currently Serving: "
                f"{location['Currently Serving']}"
            )

            print(
                f"  Maximum Capacity: "
                f"{location['Maximum Queue Capacity']}"
            )

            print()

    # ----------------------------------
    # Analyze Location
    # ----------------------------------
    def analyze_location(self):

        if not self.system.locations:

            print(
                "\nNo locations available."
            )

            return

        print(
            "\n========== ANALYZE LOCATION ==========\n"
        )

        location_id = input(
            "Enter Location ID: "
        ).strip()

        self.system.display_location_analysis(
            location_id
        )

    # ----------------------------------
    # Compare Locations
    # ----------------------------------
    def compare_locations(self):

        if not self.system.locations:

            print(
                "\nNo locations available."
            )

            return

        self.system.display_comparison()

    # ----------------------------------
    # Get Recommendation
    # ----------------------------------
    def get_recommendation(self):

        if not self.system.locations:

            print(
                "\nNo locations available."
            )

            return

        self.system.display_recommendation()

    # ----------------------------------
    # Update Queue Information
    # ----------------------------------
    def update_queue(self):

        if not self.system.locations:

            print(
                "\nNo locations available."
            )

            return

        print(
            "\n========== UPDATE QUEUE ==========\n"
        )

        location_id = input(
            "Enter Location ID: "
        ).strip()

        location = self.system.find_location(
            location_id
        )

        if not location:

            print(
                "\nLocation not found."
            )

            return

        print(
            f"\nLocation: {location['Name']}"
        )

        print(
            f"Current Queue Size: "
            f"{location['Queue Size']}"
        )

        while True:

            try:

                new_queue_size = int(
                    input(
                        "Enter Updated Queue Size: "
                    )
                )

                if new_queue_size < 0:

                    print(
                        "Queue size cannot be negative."
                    )

                    continue

                if (

                    new_queue_size
                    >
                    location[
                        "Maximum Queue Capacity"
                    ]

                ):

                    print(
                        "Queue size cannot exceed "
                        "maximum capacity."
                    )

                    continue

                break

            except ValueError:

                print(
                    "Please enter a valid number."
                )

        # Update queue
        location["Queue Size"] = (
            new_queue_size
        )

        # ----------------------------------
        # Update Currently Serving
        # ----------------------------------
        while True:

            try:

                currently_serving = int(
                    input(
                        "People Currently Being Served: "
                    )
                )

                if currently_serving < 0:

                    print(
                        "Value cannot be negative."
                    )

                    continue

                if (

                    currently_serving
                    >
                    new_queue_size

                ):

                    print(
                        "Currently serving cannot be "
                        "greater than queue size."
                    )

                    continue

                break

            except ValueError:

                print(
                    "Please enter a valid number."
                )

        location["Currently Serving"] = (
            currently_serving
        )

        print(
            "\nQueue information updated successfully."
        )

        # Display updated analysis
        print(
            "\nUpdated Queue Analysis:"
        )

        self.system.display_location_analysis(
            location_id
        )

    # ----------------------------------
    # Menu
    # ----------------------------------
    def menu(self):

        while True:

            print("\n" + "=" * 60)
            print(
                "                   WAITWISE"
            )
            print("=" * 60)

            print("1. Add Service Location")
            print("2. View All Locations")
            print("3. Update Queue Information")
            print("4. Analyze Location")
            print("5. Compare Locations")
            print("6. Get Best Location Recommendation")
            print("7. Exit")

            choice = input(
                "\nEnter Choice: "
            ).strip()

            if choice == "1":

                self.add_location()

            elif choice == "2":

                self.view_locations()

            elif choice == "3":

                self.update_queue()

            elif choice == "4":

                self.analyze_location()

            elif choice == "5":

                self.compare_locations()

            elif choice == "6":

                self.get_recommendation()

            elif choice == "7":

                print(
                    "\nThank you for using WaitWise."
                )

                break

            else:

                print(
                    "\nInvalid choice. Please try again."
                )


# ----------------------------------
# Main
# ----------------------------------

if __name__ == "__main__":

    studio = WaitWiseStudio()

    studio.menu()
