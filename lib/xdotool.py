from subprocess import call, check_output

def getmouselocation():
    location_raw = check_output(["xdotool", "getmouselocation"]).decode().split()
    
    return {
        "x": int(location_raw[0].split(":")[1]),
        "y": int(location_raw[1].split(":")[1]),
        "screen": int(location_raw[2].split(":")[1]),
        "window": int(location_raw[3].split(":")[1])
    }