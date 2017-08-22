import sys
from helloworld import HelloWorld

def main():
    helloworld = HelloWorld("Oreo")
    print(helloworld.text())
    print(HelloWorld.class_text())
    print(sys.argv)

if __name__ == "__main__":
    main()
