"""
WaitWise
--------
File: wait_wise.py

Purpose
-------
WaitWise estimates waiting time for service locations such as:

- Clinics
- Hospitals
- Restaurants
- College offices
- Government service centers
- Customer service desks

The system considers:

- Number of people currently waiting
- Number of service counters
- Average service time
- Current people being served
- Queue capacity

It estimates:

- Expected waiting time
- Queue load
- Service pressure
- Overcrowding risk
- Recommended action
"""


class WaitWise:

    def __init__(self):

        self.locations = []

    # ----------------------------------
    # Add Service Location
    # ----------------------------------
    def add_location(
            self,
            location_id,
            name,
            queue_size,
            service_counters,
            average_service_time,
            currently_serving=0,
            max_queue_capacity=100):

        location = {

            "ID": location_id,

            "Name": name,

            "Queue Size": queue_size,

            "Service Counters":
                service_counters,

            "Average Service Time":
                average_service_time,

            "Currently Serving":
                currently_serving,

            "Maximum Queue Capacity":
                max_queue_capacity

        }

        self.locations.append(
            location
        )

        return location

    # ----------------------------------
    # Find Location
    # ----------------------------------
    def find_location(
            self,
            location_id):

        for location in self.locations:

            if location["ID"] == location_id:

                return location

        return None

    # ----------------------------------
    # People Ahead
    # ----------------------------------
    def people_ahead(
            self,
            location):

        waiting = location["Queue Size"]

        currently_serving = (
            location["Currently Serving"]
        )

        people_ahead = (
            waiting - currently_serving
        )

        return max(
            0,
            people_ahead
        )

    # ----------------------------------
    # Estimated Waiting Time
    # ----------------------------------
    def estimate_waiting_time(
            self,
            location):

        people_ahead = self.people_ahead(
            location
        )

        service_counters = (
            location["Service Counters"]
        )

        average_service_time = (
            location["Average Service Time"]
        )

        if service_counters <= 0:

            return float("inf")

        # Divide people ahead between
        # available service counters.

        waiting_time = (

            people_ahead
            /
            service_counters

        ) * average_service_time

        return round(
            waiting_time,
            2
        )

    # ----------------------------------
    # Queue Load Percentage
    # ----------------------------------
    def queue_load(
            self,
            location):

        queue_size = (
            location["Queue Size"]
        )

        max_capacity = (
            location[
                "Maximum Queue Capacity"
            ]
        )

        if max_capacity <= 0:

            return 100

        load = (

            queue_size
            /
            max_capacity

        ) * 100

        return round(
            min(load, 100),
            2
        )

    # ----------------------------------
    # Service Pressure Score
    # ----------------------------------
    def service_pressure(
            self,
            location):

        queue_size = (
            location["Queue Size"]
        )

        service_counters = (
            location["Service Counters"]
        )

        if service_counters <= 0:

            return 100

        pressure = (

            queue_size
            /
            service_counters

        ) * 10

        return round(
            min(pressure, 100),
            2
        )

    # ----------------------------------
    # Overcrowding Risk
    # ----------------------------------
    def overcrowding_risk(
            self,
            location):

        load = self.queue_load(
            location
        )

        pressure = self.service_pressure(
            location
        )

        score = (

            load * 0.60
            +
            pressure * 0.40

        )

        return round(
            min(score, 100),
            2
        )

    # ----------------------------------
    # Queue Status
    # ----------------------------------
    def queue_status(
            self,
            risk_score):

        if risk_score >= 80:

            return "Critical"

        elif risk_score >= 60:

            return "High"

        elif risk_score >= 30:

            return "Moderate"

        return "Low"

    # ----------------------------------
    # Recommended Action
    # ----------------------------------
    def recommended_action(
            self,
            location):

        waiting_time = (
            self.estimate_waiting_time(
                location
            )
        )

        risk_score = (
            self.overcrowding_risk(
                location
            )
        )

        if risk_score >= 80:

            return (
                "Avoid this location if possible "
                "or add more service counters."
            )

        elif risk_score >= 60:

            return (
                "Expect a long wait. "
                "Consider visiting later."
            )

        elif waiting_time >= 30:

            return (
                "Moderate waiting time expected. "
                "Plan your visit accordingly."
            )

        return (
            "Queue is manageable. "
            "Good time to visit."
        )

    # ----------------------------------
    # Analyze Location
    # ----------------------------------
    def analyze_location(
            self,
            location):

        waiting_time = (
            self.estimate_waiting_time(
                location
            )
        )

        queue_load = self.queue_load(
            location
        )

        pressure = self.service_pressure(
            location
        )

        risk = self.overcrowding_risk(
            location
        )

        return {

            "Location ID":
                location["ID"],

            "Location":
                location["Name"],

            "Queue Size":
                location["Queue Size"],

            "Service Counters":
                location["Service Counters"],

            "Estimated Wait":
                waiting_time,

            "Queue Load":
                queue_load,

            "Service Pressure":
                pressure,

            "Overcrowding Risk":
                risk,

            "Queue Status":
                self.queue_status(
                    risk
                ),

            "Recommendation":
                self.recommended_action(
                    location
                )

        }

    # ----------------------------------
    # Compare Locations
    # ----------------------------------
    def compare_locations(self):

        analysis = []

        for location in self.locations:

            result = self.analyze_location(
                location
            )

            analysis.append(
                result
            )

        return sorted(

            analysis,

            key=lambda location:
            location["Estimated Wait"]

        )

    # ----------------------------------
    # Recommend Best Location
    # ----------------------------------
    def recommend_location(self):

        if not self.locations:

            return None

        locations = (
            self.compare_locations()
        )

        return locations[0]

    # ----------------------------------
    # Display Location Analysis
    # ----------------------------------
    def display_location_analysis(
            self,
            location_id):

        location = self.find_location(
            location_id
        )

        if not location:

            print(
                "\nLocation not found."
            )

            return

        result = self.analyze_location(
            location
        )

        print(
            "\n========== LOCATION ANALYSIS ==========\n"
        )

        for key, value in result.items():

            if key == "Estimated Wait":

                print(
                    f"{key:<20}: "
                    f"{value} minutes"
                )

            elif key in [

                "Queue Load",
                "Service Pressure",
                "Overcrowding Risk"

            ]:

                print(
                    f"{key:<20}: "
                    f"{value}%"
                )

            else:

                print(
                    f"{key:<20}: {value}"
                )

    # ----------------------------------
    # Display Location Comparison
    # ----------------------------------
    def display_comparison(self):

        if not self.locations:

            print(
                "\nNo locations available."
            )

            return

        results = self.compare_locations()

        print(
            "\n========== WAIT TIME COMPARISON ==========\n"
        )

        for index, location in enumerate(
                results,
                start=1):

            print(
                f"{index}. "
                f"{location['Location']}"
            )

            print(
                f"   Queue Size: "
                f"{location['Queue Size']}"
            )

            print(
                f"   Service Counters: "
                f"{location['Service Counters']}"
            )

            print(
                f"   Estimated Wait: "
                f"{location['Estimated Wait']} minutes"
            )

            print(
                f"   Queue Status: "
                f"{location['Queue Status']}"
            )

            print(
                f"   Overcrowding Risk: "
                f"{location['Overcrowding Risk']}%"
            )

            print()

    # ----------------------------------
    # Display Recommendation
    # ----------------------------------
    def display_recommendation(self):

        location = self.recommend_location()

        if not location:

            print(
                "\nNo locations available."
            )

            return

        print(
            "\n========== WAITWISE RECOMMENDATION ==========\n"
        )

        print(
            f"Best Location to Visit: "
            f"{location['Location']}"
        )

        print(
            f"Estimated Wait: "
            f"{location['Estimated Wait']} minutes"
        )

        print(
            f"Queue Status: "
            f"{location['Queue Status']}"
        )

        print(
            f"Overcrowding Risk: "
            f"{location['Overcrowding Risk']}%"
        )

        print(
            f"Recommendation: "
            f"{location['Recommendation']}"
        )


# ----------------------------------
# Example
# ----------------------------------

if __name__ == "__main__":

    system = WaitWise()

    # ----------------------------------
    # Location 1
    # ----------------------------------
    system.add_location(

        "L001",

        "City Clinic",

        25,

        3,

        10,

        3,

        50

    )

    # ----------------------------------
    # Location 2
    # ----------------------------------
    system.add_location(

        "L002",

        "Central Service Center",

        40,

        5,

        8,

        5,

        80

    )

    # ----------------------------------
    # Location 3
    # ----------------------------------
    system.add_location(

        "L003",

        "College Administration Office",

        12,

        2,

        15,

        2,

        30

    )

    # Compare all locations
    system.display_comparison()

    # Get best recommendation
    system.display_recommendation()
