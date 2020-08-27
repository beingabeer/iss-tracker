import os
import sys
import datetime
import requests


def iss_position():
    iss_url = "http://api.open-notify.org/iss-now.json"
    r = requests.get(iss_url)
    lat = r.json()["iss_position"]["latitude"]
    long = r.json()["iss_position"]["longitude"]
    unix_timestamp = r.json()["timestamp"]
    timestamp = datetime.datetime.fromtimestamp(int(unix_timestamp)).strftime(
        "%Y-%m-%d %H:%M:%S"
    )
    return lat, long, timestamp


def iss_people():
    iss_people_url = "http://api.open-notify.org/astros.json"
    r = requests.get(iss_people_url)
    number = r.json()["number"]
    craft = r.json()["people"][0]["craft"]
    people_json = [n for n in r.json()["people"]]
    names = [n["name"] for n in people_json]
    return number, craft, names


def iss_duration():
    lat = input("Enter latitude: ")
    long = input("Enter longitude: ")
    url = f"http://api.open-notify.org/iss-pass.json?lat={lat}&lon={long}"
    r = requests.get(url)

    if r.ok:
        print(f"The ISS will be overhead lat {lat} long {long} at -")
        for response in r.json()["response"]:
            print("")
            unix_timestamp = response["risetime"]
            timestamp = datetime.datetime.fromtimestamp(int(unix_timestamp)).strftime(
                "%Y-%m-%d %H:%M:%S"
            )
            print(f"{timestamp} for {response['duration']} seconds")
            datetime.datetime.fromtimestamp(int(unix_timestamp)).strftime(
                "%Y-%m-%d %H:%M:%S"
            )
            print("")
    else:
        print(r.json())


def main():
    if len(sys.argv) > 2:
        print(
            "You have specified too many arguments. Available arguments are loc, pass, people"
        )
        sys.exit()

    elif len(sys.argv) == 1:
        print("No arguments entered. Available arguments are loc, pass, people")
        sys.exit()

    elif sys.argv[1] == "loc":
        lat, long, timestamp = iss_position()
        print(f"Ths ISS current location at {timestamp} is {lat} {long}")

    elif sys.argv[1] == "people":
        number, craft, names = iss_people()
        names_string = ", ".join(names)
        print(f"There are {number} people aboard the {craft}. They are {names_string}.")

    elif sys.argv[1] == "pass":
        iss_duration()

    else:
        print("The available arguments are loc, pass, people")


if __name__ == "__main__":
    main()
