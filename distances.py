distances = {
    'Voyager 1': '163',
    'Voyager 2': '136',
    'Pioneer 10': '80 au',
    'New Horizons': '58',
    'Pioneer 11': '44 au'
}



def main():
    spacecraft = input('Enter a spacecraft: ')
    try:
        au = float(distances[spacecraft])
    except KeyError:
        print(f'{spacecraft} is not in dict')
        return
    except ValueError:
        print(f'Distance = {distances[spacecraft]}')
        try:
            au = float(distances[spacecraft].split()[0])
        except ValueError:
            print(f'Distance = {distances[spacecraft]}')
            return
            return  # Exit if unable to extract numeric part

    m = convert(au)
    print(f'{m} m away')

def convert(au):
    return au * 149597870700


main()