import debugpy
import threading
import time
import os
import signal
import logging

# Configuring logging
logging.basicConfig(level=logging.INFO)


def monitor_debugger_connection():
    while True:
        time.sleep(2)  # Check every 2 seconds
        if not debugpy.is_client_connected():
            logging.warning("Debugging client has disconnected. Terminating execution.")
            os.kill(os.getpid(), signal.SIGTERM)  # Terminate the main process


def start_debugger_monitor():
    monitor_thread = threading.Thread(target=monitor_debugger_connection, daemon=True)
    monitor_thread.start()


def init_debugger():
    # This starts debugpy and makes it listen on port 5680
    debugpy.listen(("0.0.0.0", 5680))
    logging.info("Debugpy listening on 0.0.0.0:5680...")

    # If you want the script to wait for the debugger to connect before continuing:
    debugpy.wait_for_client()

    debugpy.breakpoint()
    start_debugger_monitor()
