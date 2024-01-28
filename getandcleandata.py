import pandas as pd
import numpy
import json
import os
import csv
import codecs
import datetime as dt
from matplotlib import pyplot as plt

### json template of instagram messages
# """
# "participants": [
#     {
#       "name": "______amjad"
#     },
#     {
#       "name": "Salwa Design | \u00d8\u00b3\u00d9\u0084\u00d9\u0088\u00d9\u008a \u00d8\u00af\u00db\u008c\u00d8\u00b2\u00d8\u00a7\u00db\u008c\u00d9\u0086"
#     }
#   ],
#   "messages": [

#     {
#       "sender_name": "Salwa Design | \u00d8\u00b3\u00d9\u0084\u00d9\u0088\u00d9\u008a \u00d8\u00af\u00db\u008c\u00d8\u00b2\u00d8\u00a7\u00db\u008c\u00d9\u0086",
#       "timestamp_ms": 1705392963364,
#       "content": "\u00f0\u009f\u008e\u0081\u00e2\u0099\u00a5\u00ef\u00b8\u008f \u00d9\u0084\u00d8\u00a7 \u00d8\u00aa\u00d9\u0081\u00d9\u0088\u00d8\u00aa\u00d9\u0083\u00d9\u0085 \u00d8\u00b9\u00d8\u00b1\u00d9\u0088\u00d8\u00b6\u00d8\u00a7\u00d8\u00aa \u00d8\u00b3\u00d9\u0084\u00d9\u0088\u00d9\u008a \u00d8\u00af\u00d9\u008a\u00d8\u00b2\u00d8\u00a7\u00d9\u008a\u00d9\u0086 \u00d8\u00a8\u00d9\u0085\u00d9\u0086\u00d8\u00a7\u00d8\u00b3\u00d8\u00a8\u00d8\u00a9 Valentine's \u00e2\u0099\u00a5\u00ef\u00b8\u008f\u00f0\u009f\u008e\u0081\n\n\n\u00d8\u00a7\u00d9\u0087\u00d9\u0084\u00d8\u00a7 \u00d8\u00a8\u00d9\u0083 \u00f0\u009f\u0092\u009b\n\n\u00d8\u00a7\u00d9\u0086\u00d9\u0087\u00d8\u00a7 \u00d9\u0084\u00d9\u0088\u00d8\u00ad\u00d8\u00a7\u00d8\u00aa \u00d9\u0085\u00d9\u0086\u00d8\u00b3\u00d9\u0088\u00d8\u00ac\u00d8\u00a9 \u00d9\u008a\u00d8\u00af\u00d9\u0088\u00d9\u008a\u00d8\u00a7 \u00d9\u0085\u00d8\u00b9 \u00d8\u00aa\u00d9\u0081\u00d8\u00a7\u00d8\u00b5\u00d9\u008a\u00d9\u0084 \u00d8\u00a3\u00d9\u0086\u00d9\u008a\u00d9\u0082\u00d8\u00a9 \u00d8\u00b5\u00d8\u00a7\u00d8\u00ba\u00d9\u0087\u00d8\u00a7 \u00d9\u0081\u00d9\u0086\u00d8\u00a7\u00d9\u0086\u00d9\u0088\u00d9\u0086 \u00d9\u0085\u00d8\u00ad\u00d8\u00aa\u00d8\u00b1\u00d9\u0081\u00d9\u0088\u00d9\u0086 \u00d8\u008c \u00d9\u0085\u00d9\u0085\u00d8\u00a7 \u00d9\u008a\u00d8\u00ac\u00d8\u00b9\u00d9\u0084 \u00d8\u00a7\u00d9\u0084\u00d8\u00a7\u00d9\u0086\u00d8\u00b3\u00d8\u00ac\u00d8\u00a7\u00d9\u0085 \u00d8\u00a7\u00d9\u0084\u00d8\u00b1\u00d8\u00a7\u00d8\u00a6\u00d8\u00b9 \u00d9\u0084\u00d8\u00af\u00d9\u008a\u00d9\u0083\u00d9\u0088\u00d8\u00b1 \u00d8\u00a7\u00d9\u0084\u00d9\u0085\u00d9\u0086\u00d8\u00b2\u00d9\u0084 \u00d9\u0088\u00d8\u00a7\u00d9\u0084\u00d9\u0085\u00d9\u0083\u00d8\u00aa\u00d8\u00a8. \u00f0\u009f\u00a7\u00b5\n\u00d9\u0087\u00d8\u00af\u00d9\u008a\u00d8\u00a9 \u00d8\u00a5\u00d8\u00a8\u00d8\u00af\u00d8\u00a7\u00d8\u00b9\u00d9\u008a\u00d8\u00a9 \u00d9\u0085\u00d9\u0085\u00d9\u008a\u00d8\u00b2\u00d8\u00a9 \u00d8\u00ac\u00d8\u00af\u00d8\u00a7\u00d9\u008b \n\u00d9\u0086\u00d8\u00b8\u00d8\u00b1\u00d9\u008b\u00d8\u00a7 \u00d9\u0084\u00d8\u00a3\u00d9\u0086\u00d9\u0087\u00d8\u00a7 \u00d9\u0087\u00d8\u00af\u00d9\u008a\u00d8\u00a9 \u00d8\u00b1\u00d8\u00a7\u00d8\u00a6\u00d8\u00b9\u00d8\u00a9 \u00d8\u008c \u00d9\u0085\u00d8\u00a7 \u00d8\u00b9\u00d9\u0084\u00d9\u008a\u00d9\u0083 \u00d8\u00b3\u00d9\u0088\u00d9\u0089 \u00d8\u00a5\u00d8\u00b1\u00d8\u00b3\u00d8\u00a7\u00d9\u0084 \u00d8\u00b5\u00d9\u0088\u00d8\u00b1\u00d8\u00a9 \u00d9\u0085\u00d9\u0081\u00d8\u00b6\u00d9\u0084\u00d8\u00a9 \u00d9\u0084\u00d9\u0088\u00d8\u00ac\u00d9\u0087\u00d9\u0083 \u00d8\u008c \u00d8\u00ab\u00d9\u0085 \u00d8\u00b3\u00d9\u008a\u00d8\u00aa\u00d9\u0085 \u00d9\u0086\u00d8\u00b3\u00d8\u00ac\u00d9\u0087\u00d8\u00a7 \u00d9\u008a\u00d8\u00af\u00d9\u0088\u00d9\u008a\u00d9\u008b\u00d8\u00a7 \u00d8\u00a8\u00d8\u00ae\u00d9\u008a\u00d8\u00b7 \u00d9\u0088\u00d8\u00a7\u00d8\u00ad\u00d8\u00af \u00d8\u00a8\u00d8\u00b7\u00d9\u0088\u00d9\u0084 5 \u00d9\u0083\u00d9\u008a\u00d9\u0084\u00d9\u0088\u00d9\u0085\u00d8\u00aa\u00d8\u00b1\u00d8\u00a7\u00d8\u00aa.\n\u00f0\u009f\u009f\u00a1\u00d9\u0085\u00d8\u00b9 \u00d8\u00b4\u00d8\u00ad\u00d9\u0086 \u00d9\u0085\u00d8\u00ac\u00d8\u00a7\u00d9\u0086\u00d9\u008a \u00e2\u009c\u0088\u00ef\u00b8\u008f\u00f0\u009f\u0086\u0093\n\n\u00d9\u008a\u00d9\u0085\u00d9\u0083\u00d9\u0086\u00d9\u0083 \u00d8\u00a7\u00d9\u0084\u00d8\u00ad\u00d8\u00b5\u00d9\u0088\u00d9\u0084 \u00d8\u00b9\u00d9\u0084\u00d9\u0089 \u00d9\u0085\u00d9\u0082\u00d8\u00b7\u00d8\u00b9 \u00d9\u0081\u00d9\u008a\u00d8\u00af\u00d9\u008a\u00d9\u0088 \u00d9\u0084\u00d9\u0081\u00d8\u00aa\u00d8\u00b1\u00d8\u00a7\u00d8\u00aa \u00d8\u00b2\u00d9\u0085\u00d9\u0086\u00d9\u008a\u00d8\u00a9 \u00d9\u0084\u00d8\u00b5\u00d9\u0086\u00d8\u00b9 \u00d9\u0081\u00d9\u0086 \u00d8\u00a7\u00d9\u0084\u00d8\u00b3\u00d9\u0084\u00d8\u00b3\u00d9\u0084\u00d8\u00a9 \n\u00d8\u00a7\u00d9\u0084\u00d8\u00ae\u00d8\u00a7\u00d8\u00b5 \u00d8\u00a8\u00d9\u0083\u00f0\u009f\u0098\u008d\u00f0\u009f\u008e\u00a5\n\u00d9\u0085\u00d9\u0086 \u00d8\u00ae\u00d9\u0084\u00d8\u00a7\u00d9\u0084 \u00d8\u00a7\u00d8\u00ae\u00d8\u00aa\u00d9\u008a\u00d8\u00a7\u00d8\u00b1 Tabby\u00d8\u00b9\u00d9\u0086\u00d8\u00af \u00d8\u00a7\u00d9\u0084\u00d8\u00af\u00d9\u0081\u00d8\u00b9\u00d8\u008c \u00db\u008c\u00d9\u0085\u00da\u00a9\u00d9\u0086\u00d9\u0083 \u00d8\u00a3\u00d9\u0086 \u00d8\u00aa\u00d8\u00aa\u00d8\u00b3\u00d9\u0088\u00d9\u0082 \u00d8\u00a7\u00d9\u0084\u00d8\u00a2\u00d9\u0086 \u00d9\u0088 \u00d8\u00aa\u00d8\u00af\u00d9\u0081\u00d8\u00b9 \u00d9\u0084\u00d8\u00a7\u00d8\u00ad\u00d9\u0082\u00d9\u008b\u00d8\u00a7 \u00d8\u00b9\u00d9\u0084\u00d9\u0089 4 \u00d8\u00a3\u00d9\u0082\u00d8\u00b3\u00d8\u00a7\u00d8\u00b7 \u00d8\u00a8\u00d8\u00af\u00d9\u0088\u00d9\u0086 \u00d9\u0081\u00d9\u0088\u00d8\u00a7\u00d8\u00a6\u00d8\u00af \u00d8\u00b9\u00d9\u0086\u00d8\u00af \u00d8\u00a7\u00d9\u0084\u00d8\u00af\u00d9\u0081\u00d8\u00b9 \u00f0\u009f\u0098\u008d*",
#       "is_geoblocked_for_viewer": false
#     },
#     {
#       "sender_name": "Salwa Design | \u00d8\u00b3\u00d9\u0084\u00d9\u0088\u00d9\u008a \u00d8\u00af\u00db\u008c\u00d8\u00b2\u00d8\u00a7\u00db\u008c\u00d9\u0086",
#       "timestamp_ms": 1705392085004,
#       "content": "______amjad replied to an Ad. See post(https://www.instagram.com/p/C1KtYG-tnqO/)",
#       "is_geoblocked_for_viewer": false
#     },
#   ],
#   "title": "______amjad",
#   "is_still_participant": true,
#   "thread_path": "inbox/______amjad_1312630076798892",
#   "magic_words": [

#   ]
# }
# """
INBOX_DIRECTORY_ADDRESS = "your_instagram_activity/messages/inbox"
chatDataFrame = pd.DataFrame(
    columns=[
        "Customer ID",
        "Number of Salwa Messages",
        "Salwa Messages",
        "Number of Customer Messages",
        "Customer Messages",
        "timestamp of first message",
        "timestamp of last message",
        "inboxFolderPath",
    ]
)
listOfFolders = os.listdir(INBOX_DIRECTORY_ADDRESS)
for i in listOfFolders:
    with open(f"{INBOX_DIRECTORY_ADDRESS}/{i}/message_1.json") as f:
        data = json.load(f)
        customerId = data["participants"][0]["name"].encode("latin1").decode("utf-8")
        numberOfSalwaMessages = 0
        numberOfCustomerMessages = 0
        salwaMessages = []
        customerMessages = []
        timestamp = int(data["messages"][0]["timestamp_ms"]) / 1000
        timestampOfFirstMessage = dt.datetime.fromtimestamp(timestamp).strftime(
            "%Y-%m-%d"
        )
        timestamp = int(data["messages"][-1]["timestamp_ms"]) / 1000
        timestampOfLasttMessage = dt.datetime.fromtimestamp(timestamp).strftime(
            "%Y-%m-%d"
        )
        for message in data["messages"]:
            messageSender = message["sender_name"].encode("latin1").decode("utf-8")
            # messageContent = message["content"].encode("latin1").decode("utf-8")

            try:
                messageContent = message["content"].encode("latin1").decode("utf-8")
            except KeyError:
                # print(f"remove message from inbox {i}")
                continue
            if messageSender.startswith("Salwa"):
                numberOfSalwaMessages += 1
                salwaMessages.append(messageContent)
            else:
                numberOfCustomerMessages += 1
                customerMessages.append(messageContent)

        appendableDataRow = {
            "Customer ID": customerId,
            "Number of Salwa Messages": numberOfSalwaMessages,
            "Salwa Messages": salwaMessages,
            "Number of Customer Messages": numberOfCustomerMessages,
            "Customer Messages": customerMessages,
            "timestamp of first message": timestampOfFirstMessage,
            "timestamp of last message": timestampOfLasttMessage,
            "inboxFolderPath": i,
        }
        rowDataFrame = pd.DataFrame([appendableDataRow])
        # chatDataFrame = chatDataFrame.append(appendableDataRow, ignore_index=True)
        chatDataFrame = pd.concat(
            [chatDataFrame, rowDataFrame], ignore_index=True, axis=0
        )

chatDataFrame.to_excel("output.xlsx", index=False)
chatDataFrame.hist(column="Number of Customer Messages")

# Set the title and axis labels
plt.title("Histogram of Column Name")
plt.xlabel("Values")
plt.ylabel("Frequency")
