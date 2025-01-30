### Main Function
The `main()` function prompts the user to input the name of a spacecraft. It then looks up the spacecraft in a dictionary (`distances`) and tries to extract the distance.
If the spacecraft is not found or if there’s an issue with the distance format, it handles the errors appropriately.

### Error Handling
- If the spacecraft is not in the dictionary, a `KeyError` is caught, and an error message is printed.
- If the distance contains "au" (astronomical units), the program extracts the numeric value, converts it to meters using the `convert()` function, and prints the result.
- If there’s an issue parsing the distance, another `ValueError` is caught, and the program exits after printing the original distance.

### Conversion Function
The `convert()` function takes the distance in AU (astronomical units) and converts it to meters using the conversion factor: 1 AU = 149,597,870,700 meters.
It returns the result in meters.
