from cryptography.fernet import Fernet

key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='

# Oh no! The code is going over the edge! What are you going to do?
message = b'gAAAAABdUims0aAleM3Uf0EmrnDlOddfRoKMXc6bOpRFe-dC3bvjFO6ff-t7O0UcgYNcouiDpcDuZh03pvO3I2RHqjMUXG8VEt6YgwMyTq\
            DKgahvcTfhrk1SsQ7Oi3hBDP7P49LTv9QSjMT4FmFAThXYN2sMMkAt8eZAx1Joc5EoObm3KOMsQiQ='


def main():
    f = Fernet(key)
    print(f.decrypt(message))


if __name__ == "__main__":
    main()
