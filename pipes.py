import multiprocessing

def child_process(conn):
    message = "Hello from child process!"
    conn.send(message)  # Send message through the pipe
    conn.close()

def parent_process():
    parent_conn, child_conn = multiprocessing.Pipe()

    # Create child process, pass one end of the pipe
    process = multiprocessing.Process(target=child_process, args=(child_conn,))
    process.start()

    # Read message from child process
    message = parent_conn.recv()
    print(f"Parent received: {message}")

    process.join()

if __name__ == "__main__":
    parent_process()
