from convertUtility import bytesToMessage

def processChat(message):
     print("\n" + bytesToMessage(message))

def processData(queue):
     while True:
          length = queue.qsize()
          if length == 0:
               continue
          processChat(queue.get())
