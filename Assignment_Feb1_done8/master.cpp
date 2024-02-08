// from multiprocessing import Process

// from bank_server import run_server
// from atm_client import run_client

// import time

// import psutil



// if __name__ == '__main__':
//     client = Process(target=run_client)
//     server = Process(target=run_server)
//     try:
//         server.start()
//         time.sleep(1)
//         client.start()

//         server.join()
//         client.join()

//     except(KeyboardInterrupt):
//         server.join()
//         client.join()