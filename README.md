# Privacy Coin

  

As said in the name, privacy coin is based on privacy, all of the transactions are made will be encrypted and untraceable. This coin uses a unique system of user keys that identify the user. Privacy coin uses a primitive but secure way of storing your account balance, it latches the balance on the end of the user key, however a key can not be changed physically so no "fake" PRC will be on the chain;
```mermaid
sequenceDiagram
    Sender->>Function: senderkey_10
    Function->>Function: Checks if senderkey_10 exists
    Sender->>Function: reciverkey_0
    Function->>Function: Checks if reciverkey_0 exists
    Sender->>Function: 2 PRC
    Function->>Function: Checks if _num is bigger then amount
    Function->>Reciver: New key: reciverkey_2
    Function->>Sender: New key: senderkey_8
    Function->>Function: Updates userkeys.txt
```

This project is only in BETA version, if you have any suggestions, you are free to make a pull request or just leave a comment, and don't be afraid to snoop around the code :)