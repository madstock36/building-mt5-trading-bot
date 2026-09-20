import MetaTrader5 as mt5

def main() :
    # Read credentials line by line : path, account, pwd, server
    with open("key.txt") as f:
        path, account, pwd, server = [line.strip() for line in f if line.strip()]

    # Initialize and log in to MT5 terminal 

    if not mt5.initialize(
        path = path ,           # Line1 : MT5 folder
        login = int(account),   # Line2 : MT5 account (number, not string )
        password = pwd,         # Line3 : MT5 password
        server = server,        # server name ( depends on your broker )

    ):
        print("MT5 initialization failed")
        return

    
    print("MT5 initialization succeeded")

    mt5.shutdown()

if __name__ == "__main__" :
    main()