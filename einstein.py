def main():
    #enter the mass
    user_input = int(input('enter mass: '))
    #convert to energy
    print(convert(user_input))
    
def convert(m):
    #E=mc**2
    c = 300000000 #speed of light
    E = m*(c**2)
    return E

main()