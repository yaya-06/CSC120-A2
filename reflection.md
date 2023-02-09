Use this file to record your reflection on this assignment. 

What worked, what didn't, what advice would you give someone taking this course in the future?

I approached this assignment using the approach demonstrated in the video and in class which was creating the computer instance within resale shop's buy method. I decided to pass in all of attributes because I figured a store would need it all eventually. But then I thought that would make it more difficult when trying to specify it later. I also couldn't call it by the name I felt because within the method it was still the general 'computer'. This necessitated a unique shorthand to reference the computers by and for that I used itemID. 

Adding an itemID specific to the computer felt like an attribute of it. Because of thsat it took me a while to figure out I needed to initialize itemID within the resale store. 

I felt as though going the itemID route made my OOP code very similar to the procedural code. It occured to me that instead of creating the whole itemID attribute that I could print out each the index value for each computer when checking the inventory. This way the user would be able to associate each computer  with a short ID but not have those extra lines of code. Then specify its index placement when removing it from the inventory list. 

While I'm sure this code would work, I'm a fan of the ID because then each computer whether it's sold or not will always be associated with that number rather than another computer taking than same number/index placement. 
--
This all came to a head though when I moved on from coding the buying and selling functions to the ones on updating the price and OS. To reference the computer I needed the resale shop buy() method because that's where the computer was initialized, where the inventory was, etc. So I imported oop_resale_shop.py to computer.py. The problem was I was already importing computer.py to oop_resale_shop.py. Took me a while to figure it out but it through me for an error because it led to a circular dependency.

I couldn't find a way to overcome the circular dependecy while still creating the computer instance within the buy method. I thought that putting the computer instance outside the buy method felt less regulated somehow than the store taking in a commputer an assigning it a number. Theoretically the programmer could call that computer anything they want. But assuming they themselves keep a proper tally then I feel still feel like it could be ordered enough with calling the object instance name.

Another problem that came up is in with updatePrice(), which I felt needed to be a method in the computer class for this assignment, I had a hard time finding a contingency for if the item was sold. Again I couldn't reference anything like whether it was in the resale shop anymore because this made it circular. I tried deleting the object as a whole when sellling it and then checking within the updateprice method whether it existed or not. 