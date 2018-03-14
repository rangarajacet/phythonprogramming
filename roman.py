def roman(a):
    rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    int_val = 0
    for i in range(len(a)):
        if i > 0 and rom_val[a[i]] > rom_val[a[i - 1]]:
                int_val += rom_val[a[i]] - 2 * rom_val[a[i - 1]]
        else:
                int_val += rom_val[a[i]]
    return int_val
string = input("Enter the roman no")
print(roman(string))
