from multiprocessing import Process, Pipe

def child_process(conn):
    message = "Hello from child process"
    conn.send(message)
    conn.close()

if __name__ == "__main__":
    parent_conn, child_conn = Pipe()

    process = Process(target=child_process, args=(child_conn,))
    process.start()

    print("Parent received:", parent_conn.recv())
    process.join()