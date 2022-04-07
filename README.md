<h2>Introduction</h2>
This repo contains all the exercises for both worksheet 2.1 and worksheet 2.2 for IOT

<h2><b>Different files</b></h2>
 <b>assert_test </b> => This file contains just one test for the encode function. 

 <b>ham_radio.py </b> => This file contains the function to encode and decode messages which are then passed to the server. 

 <b>heap.py</b> => This file is implementing the heap

 <b>main.py</b> => This file is just calling the test_encode_us() function from the assert_tests file.

 <b>morse_server.py</b>  => This file contains two functions used to connect to the server and receive or send messages and then return them. There are also comments trought all the file to understand better the different steps.

 <b>morse.py</b> => Inside this file, there are several functions, all used to decode and encode a message. The encode and decode functions are obvious. Then we have the initNode() function. This is initialising the Tree which will then be used to decode and encode the messages. The loopEncode() function is being used in the loop by the encode() function. There are comments in the file which will make you understand better the code.

 <b>morseunit.py </b> => This file contains all the tests used trought the two worksheets. Each test has a comment saying what it is about. Some tests are correct, other will fail. This was done on purpose to test that the code was working correctly.

 <b>tree.py </b> => This file contains the Node class which was used for encoding and decoding the messages. There are some examples (which are commented out) which were used for testing purposes and to make sure the code was working fine.
 In order to run this file from the terminal you can type: python tree.py


<h2>Binary Tree, Heap and dictionaries</h2>
 Morse code can be done using any of the three data structures. There are quite a few differences between the three of them, like performance or implementation. 
 
 We can definetely say that implementing the dictionary is pretty easy and straighforward. It's also obvious that in terms of performance is the worst one. If I were to implement a dictionary to encode and decode the morse code, I would use to dictionaries, one which has as keys the letters, one which has as keys the encoded string. This would make the search pretty fast, but have a big impact on memory.

 The heap is right in the middle between the two of them. It is quite easy to implement once you get the logic, a bit more difficult than the dictionaries, but definetely faster to implement than the tree. 
 
 The fastes is the binary tree, which might take longer to implement than the previous examples, but it is the best in performance.   

<h2>How to run the code</h2>
All files in this project can be ran by using the following command:
```
python3 morse.py
```

You just need to change 'morse.py', with the file you want to run

<h2>Tasks</h2>
<h3>Worksheet 2.1</h3>
File to check for <b>Task2</b>:
<li>morse.py</li>
<li>tree.py</li>
<li>main.py</li>
<br/><br/>
File to check for <b>Task3</b>:
<li>assert_tests.py</li>
<li>morseunit.py</li>
<br/><br/>

<h3>Worksheet 2.2</h3>
File to check for <b>Task1</b>:
<li>heap.py</li>
<br/><br/>
File to check for <b>Task2</b>:
<li>ham_radio.py</li>
<br/><br/>
File to check for <b>Task3</b>:
<li>morse_server.py</li>
<br/><br/>


