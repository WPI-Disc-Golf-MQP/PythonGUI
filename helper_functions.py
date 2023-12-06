import time 
def send_message_and_wait_for_response(ser, message, timeout=5, max_retries=4):
    retries = 0

    while retries <= max_retries:
        # Send the message
        ser.write(message.encode('utf-8'))
        print("Sent message:", message)

        start_time = time.time()

        while time.time() - start_time < timeout:
            # Check if there is data available to be read
            if ser.inWaiting() > 0:
                response = ser.readline().decode('utf-8').strip()
                print("Received response:", response)

                if True: 
                # if response == "GOT CAN MESSAGE: status is failure":
                    return response
                else: 
                    raise Exception("did not get expected response from microcontroller, got this: "+response)

        print("No response within the timeout period. Retrying...")
        retries += 1

    print("No response after retrying. Exiting.")



def send_msg(serialInst, message):
    try: 
        serialInst.write(message.encode('utf-8'))
    except: 
        raise Exception('seems like serial is not connected correctly')
