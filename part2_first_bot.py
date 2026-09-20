import MetaTrader5 as mt5


def main() :


    if not mt5.initialize():
        print("MT5 initialization failed")
        return
   
    print("MT5 initialization succeeded")


    mt5.shutdown()


if __name__ == "__main__" :
    main()
