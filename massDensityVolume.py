mdv = input("Choose one to calculate(m, d, v) : ")

if mdv == 'm':
    d = float(input("Enter the density: "))
    v = float(input("Enter the volume: "))
    mass = d * v
    print("The mass is " + str(mass))
elif mdv == 'd':
    m = float(input("Enter the mass: "))
    v = float(input("Enter the volume: "))
    density = m / v
    print("The mass is " + str(density))
elif mdv == 'v':
    m = float(input("Enter the mass: "))
    d = float(input("Enter the density: "))
    volume = m / d
    print("The mass is " + str(volume))
