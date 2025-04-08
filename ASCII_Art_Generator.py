import pyfiglet    #importing the library

print("Hi, there! \n Welcome to ASCII art")

# Taking the text input from the user
text = input("Enter a text that you want to convert into an ASCII Art : ")

# Dispalying available font styles
print("Available fonts : \n")
fonts = pyfiglet.FigletFont.getFonts() 
print(" , ".join(fonts[:20]))

# SElecting the font style
font_style = input("\n Choose a fontstyle from the above list : ")

# Check if the font style is valid
if font_style in fonts:
    ascii_art = pyfiglet.figlet_format(text, font=font_style)
    print("\nHere is your ASCII ART:\n")
    print(ascii_art)
else:
    print("\n Invalid font selected! Please choose a font from the list.")